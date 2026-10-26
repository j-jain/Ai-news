"""`ainews fetch`: fetch a URL and save its text + metadata under work/<week>/pages/ (Tier A evidence).

Also hosts the HTTP helper and the HTML-to-text extractor used by the other commands.
"""
import gzip
import html as htmlmod
import json
import os
import re
import time
import urllib.error
import urllib.request
import zlib
from html.parser import HTMLParser

from common import (UA, append_jsonl, canonical_url, host_of, norm_text, now_iso, parse_date, parse_loose_date,
                    read_json, read_text, url_id, word_count, work_dir, write_json, write_text)

BLOCK_TAGS = {"p", "div", "br", "li", "ul", "ol", "h1", "h2", "h3", "h4", "h5", "h6", "tr", "section", "article",
              "header", "footer", "blockquote", "pre", "table", "thead", "tbody", "figure", "figcaption", "dd", "dt",
              "dl", "nav", "aside", "main", "hr", "address", "summary", "details", "option"}
SKIP_TAGS = {"script", "style", "noscript", "svg", "template", "iframe", "canvas", "object", "video", "audio"}
DATE_META_KEYS = ("article:published_time", "og:article:published_time", "datepublished", "date", "dc.date",
                  "dc.date.issued", "dcterms.created", "dcterms.date", "pubdate", "publishdate", "publish-date",
                  "publish_date", "parsely-pub-date", "sailthru.date", "article.published", "article:published",
                  "citation_publication_date", "citation_date", "citation_online_date", "release_date", "og:release_date")


class Extractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.skip = 0
        self.in_title = False
        self.title = ""
        self.meta = {}
        self.ld = []
        self.in_ld = False
        self.ld_buf = []
        self.times = []

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if tag == "meta":
            key = a.get("property") or a.get("name") or a.get("itemprop")
            if key and a.get("content"):
                self.meta.setdefault(key.lower().strip(), a["content"].strip())
        elif tag in ("time", "relative-time"):
            if a.get("datetime"):
                self.times.append(a["datetime"])
        elif tag == "title":
            self.in_title = True
        elif tag == "script":
            if (a.get("type") or "").lower().strip() == "application/ld+json":
                self.in_ld = True
                self.ld_buf = []
            self.skip += 1
        elif tag in SKIP_TAGS:
            self.skip += 1
        if tag in BLOCK_TAGS:
            self.parts.append("\n")
        if tag in ("td", "th"):
            self.parts.append("\t")

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "script":
            if self.in_ld:
                self.in_ld = False
                raw = "".join(self.ld_buf).strip()
                if raw:
                    self.ld.append(raw)
            self.skip = max(0, self.skip - 1)
        elif tag in SKIP_TAGS:
            self.skip = max(0, self.skip - 1)
        if tag in BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.in_ld:
            self.ld_buf.append(data)
            return
        if self.skip:
            return
        self.parts.append(data)


def html_to_text(html):
    ex = Extractor()
    try:
        ex.feed(html)
        ex.close()
    except Exception:  # malformed markup: keep what we have
        pass
    text = "".join(ex.parts)
    text = text.replace("\r", "")
    text = re.sub(r"[ \t\f\v]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text, {"title": re.sub(r"\s+", " ", ex.title).strip(), "meta": ex.meta, "ld": ex.ld, "times": ex.times}


def _ld_dates(obj, out):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in ("datePublished", "dateCreated", "uploadDate") and isinstance(v, str):
                out.append(v)
            else:
                _ld_dates(v, out)
    elif isinstance(obj, list):
        for x in obj:
            _ld_dates(x, out)


def published_from(info, url):
    meta = info.get("meta", {})
    for key in DATE_META_KEYS:
        v = meta.get(key)
        d = parse_loose_date(v) if v else None
        if d:
            return d.isoformat(), f"meta {key}"
    for raw in info.get("ld", []):
        found = []
        try:
            _ld_dates(json.loads(raw), found)
        except json.JSONDecodeError:
            for m in re.finditer(r'"datePublished"\s*:\s*"([^"]+)"', raw):
                found.append(m.group(1))
        for v in found:
            d = parse_loose_date(v)
            if d:
                return d.isoformat(), "json-ld datePublished"
    for t in info.get("times", []):
        d = parse_loose_date(t)
        if d:
            return d.isoformat(), "time datetime"
    m = re.search(r"/(20\d\d)/(\d{1,2})/(\d{1,2})(?:/|$)", url)
    if m:
        try:
            import datetime as dt
            d = dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
            return d.isoformat(), "url path"
        except ValueError:
            pass
    m = re.search(r"(20\d\d-\d\d-\d\d)", url)
    if m and parse_date(m.group(1)):
        return m.group(1), "url path"
    return None, None


def http_get(url, timeout=20, retries=3, method="GET", max_bytes=4_000_000, accept=None):
    """GET/HEAD with a browser UA, gzip/deflate handling and retries. Returns a dict, never raises."""
    headers = {
        "User-Agent": UA,
        "Accept": accept or "text/html,application/xhtml+xml,application/xml;q=0.9,application/json;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "no-cache",
    }
    backoff = (2, 5, 10)
    last_err = None
    final = url
    for attempt in range(max(1, retries)):
        try:
            req = urllib.request.Request(url, method=method, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                final = resp.geturl()
                ctype = resp.headers.get("Content-Type", "") or ""
                body = b"" if method == "HEAD" else resp.read(max_bytes)
                enc = (resp.headers.get("Content-Encoding", "") or "").lower()
                if body and "gzip" in enc:
                    try:
                        body = gzip.decompress(body)
                    except Exception:
                        pass
                elif body and "deflate" in enc:
                    try:
                        body = zlib.decompress(body, -zlib.MAX_WBITS)
                    except Exception:
                        try:
                            body = zlib.decompress(body)
                        except Exception:
                            pass
                return {"status": resp.status, "final_url": final, "content_type": ctype, "body": body, "error": None}
        except urllib.error.HTTPError as e:
            if e.code in (408, 425, 429, 500, 502, 503, 504) and attempt < retries - 1:
                time.sleep(backoff[min(attempt, 2)])
                continue
            ctype = ""
            try:
                ctype = e.headers.get("Content-Type", "") or ""
            except Exception:
                pass
            return {"status": e.code, "final_url": getattr(e, "url", url) or url, "content_type": ctype, "body": b"",
                    "error": f"HTTP {e.code}"}
        except Exception as e:  # URLError, timeout, ssl, RemoteDisconnected, ConnectionReset
            last_err = f"{type(e).__name__}: {e}"
            if attempt < retries - 1:
                time.sleep(backoff[min(attempt, 2)])
    return {"status": 0, "final_url": final, "content_type": "", "body": b"", "error": last_err or "unknown error"}


def decode_body(body, ctype):
    m = re.search(r"charset=([\w-]+)", ctype or "", re.I)
    for enc in ([m.group(1)] if m else []) + ["utf-8", "cp1252", "latin-1"]:
        try:
            return body.decode(enc)
        except (UnicodeDecodeError, LookupError):
            continue
    return body.decode("utf-8", errors="replace")


def body_to_text(body, ctype, url):
    """Return (text, info) for an HTTP body. JSON becomes pretty text so quotes can be verified against it."""
    ctype = (ctype or "").lower()
    raw = decode_body(body, ctype)
    stripped = raw.lstrip()
    if "json" in ctype or (stripped[:1] in "{[" and "html" not in ctype):
        try:
            obj = json.loads(raw)
            return json.dumps(obj, ensure_ascii=False, indent=1), {"title": url, "meta": {}, "ld": [], "times": []}
        except json.JSONDecodeError:
            pass
    if "pdf" in ctype or body[:5] == b"%PDF-":
        return "", {"title": "", "meta": {}, "ld": [], "times": [], "unsupported": "pdf"}
    if ctype.startswith("text/plain") or ctype.startswith("text/markdown"):
        return raw, {"title": url, "meta": {}, "ld": [], "times": []}
    return html_to_text(raw)


def page_paths(week, id_):
    d = work_dir(week, create=False)
    return (os.path.join(d, "pages", f"{id_}.txt"),
            os.path.join(d, "pages", f"{id_}.webfetch.txt"),
            os.path.join(d, "pages", f"{id_}.meta.json"))


def load_page(week, id_):
    """Return (text, meta, tier) for a saved page, or (None, None, None)."""
    a, b, m = page_paths(week, id_)
    meta = read_json(m, {}) or {}
    if os.path.exists(a):
        return read_text(a), meta, "A"
    if os.path.exists(b):
        return read_text(b), meta, "B"
    return None, None, None


def fetch(week, url, tier="A", text_file=None, force=False, published=None, published_evidence=None):
    """Fetch (or register) a page. Returns the metadata dict (also saved as pages/<id>.meta.json)."""
    canon = canonical_url(url)
    id_ = url_id(url)
    a_path, b_path, m_path = page_paths(week, id_)
    work_dir(week, create=True)
    existing = read_json(m_path, None)
    if existing and not force and tier == "A" and existing.get("tier") == "A" and existing.get("status") == 200 \
            and os.path.exists(a_path):
        existing["cached"] = True
        return existing
    meta = {
        "id": id_, "url": url, "canonical_url": canon, "final_url": url, "status": None, "content_type": "",
        "title": "", "site_name": host_of(url), "published": None, "published_evidence": None,
        "fetched_at": now_iso(), "words": 0, "thin": True, "tier": tier, "error": None, "text_file": None,
        "source": "http",
    }
    if tier == "B":
        if not text_file or not os.path.exists(text_file):
            meta["error"] = "tier B needs --text-file with the text WebFetch returned"
            write_json(m_path, meta)
            return meta
        text = read_text(text_file).strip()
        meta["source"] = "webfetch"
        meta["status"] = 200 if text else 0
        d, ev = published_from({"meta": {}, "ld": [], "times": []}, url)
        meta["published"], meta["published_evidence"] = d, ev
        if published:
            ev_ok = bool(published_evidence) and norm_text(published_evidence) in norm_text(text)
            if ev_ok:
                meta["published"], meta["published_evidence"] = published, f"text: {published_evidence}"
            else:
                meta["published_note"] = "supplied date ignored: its evidence text was not found in the page"
        meta["words"] = word_count(text)
        meta["thin"] = meta["words"] < 400
        meta["text_file"] = os.path.relpath(b_path, work_dir(week, create=False)).replace("\\", "/")
        write_text(b_path, text + "\n")
        write_json(m_path, meta)
        append_jsonl(os.path.join(work_dir(week, create=False), "fetch-log.jsonl"), meta)
        return meta
    r = http_get(url)
    meta["status"] = r["status"]
    meta["final_url"] = r["final_url"]
    meta["content_type"] = r["content_type"]
    meta["error"] = r["error"]
    text = ""
    if r["status"] == 200 and r["body"]:
        text, info = body_to_text(r["body"], r["content_type"], url)
        if info.get("unsupported"):
            meta["error"] = f"unsupported content ({info['unsupported']}); find an HTML page that says the same"
            text = ""
        else:
            meta["title"] = info.get("title") or ""
            meta["site_name"] = info.get("meta", {}).get("og:site_name") or host_of(r["final_url"])
            meta["published"], meta["published_evidence"] = published_from(info, r["final_url"])
            if published and not meta["published"]:
                if published_evidence and published_evidence.startswith("text: "):
                    published_evidence = published_evidence[len("text: "):]
                ev_ok = bool(published_evidence) and norm_text(published_evidence) in norm_text(text)
                if ev_ok:
                    meta["published"], meta["published_evidence"] = published, f"text: {published_evidence}"
                else:
                    meta["published_note"] = "supplied date ignored: its evidence text was not found in the page"
    meta["words"] = word_count(text)
    meta["thin"] = meta["words"] < 400
    if text:
        write_text(a_path, text + "\n")
        meta["text_file"] = os.path.relpath(a_path, work_dir(week, create=False)).replace("\\", "/")
    elif os.path.exists(a_path) and force:
        os.remove(a_path)
    write_json(m_path, meta)
    append_jsonl(os.path.join(work_dir(week, create=False), "fetch-log.jsonl"), meta)
    return meta


def run(args):
    meta = fetch(args.week, args.url, tier=args.tier, text_file=args.text_file, force=args.force,
                 published=args.published, published_evidence=args.published_evidence)
    summary = {k: meta.get(k) for k in ("id", "status", "tier", "title", "site_name", "published",
                                        "published_evidence", "words", "thin", "text_file", "error", "cached",
                                        "final_url")}
    print(json.dumps(summary, ensure_ascii=False))
    if args.quiet:
        return 0 if meta.get("status") == 200 and meta.get("text_file") else 1
    text, _, _ = load_page(args.week, meta["id"])
    if text:
        print("---")
        print(text if args.full else text[: args.head] + ("\n[... truncated; read the saved file for the rest]"
                                                           if len(text) > args.head else ""))
    else:
        print("--- no text saved:", meta.get("error"))
    return 0 if meta.get("status") == 200 and meta.get("text_file") else 1
