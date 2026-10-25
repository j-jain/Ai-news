"""`ainews links`: HTTP-check every link in a draft. 404/410 are dead; 403/429/timeouts are warnings."""
import json
import os
import re
import time

from common import (LINK_RE, canonical_url, parse_front_matter, read_json, read_jsonl, read_text, rel,
                    set_front_matter_value, work_dir, write_json, write_text)
from fetch import http_get
from mdunits import content_units, links_in, normalize_paragraphs, sentences, units

WARN_STATUSES = {0, 401, 403, 405, 406, 408, 429, 500, 502, 503, 504, 520, 521, 522, 523, 524, 525, 526}


def check_url(url, timeout=15):
    r = http_get(url, timeout=timeout, retries=2, method="HEAD")
    if 200 <= (r["status"] or 0) < 400:
        return r["status"], "ok", ""
    r2 = http_get(url, timeout=timeout, retries=2, method="GET")
    st = r2["status"] or 0
    if 200 <= st < 400:
        return st, "ok", ""
    if st in (404, 410):
        return st, "dead", r2["error"] or f"HTTP {st}"
    return st, "warn", r2["error"] or "blocked or unreachable"


def run(args):
    d = work_dir(args.week, create=False)
    path = os.path.join(d, f"draft-{args.edition}.md")
    text = read_text(path)
    fm, body, _ = parse_front_matter(text)
    head = text[: len(text) - len(body)]
    body = normalize_paragraphs(body)
    ok_cache = set()
    for e in read_jsonl(os.path.join(d, "fetch-log.jsonl")):
        if e.get("status") == 200 and e.get("text_file") and e.get("source") != "webfetch":
            ok_cache.add(canonical_url(e.get("url", "")))
            ok_cache.add(canonical_url(e.get("final_url", "")))
    urls = []
    for _, url in LINK_RE.findall(body):
        if url not in urls:
            urls.append(url)
    results = []
    for url in urls:
        c = canonical_url(url)
        if c in ok_cache and not args.recheck:
            results.append({"url": url, "status": 200, "verdict": "ok", "note": "fetched successfully earlier this run"})
            continue
        st, verdict, note = check_url(url)
        results.append({"url": url, "status": st, "verdict": verdict, "note": note})
        time.sleep(0.3)
    dead = [r for r in results if r["verdict"] == "dead"]
    warn = [r for r in results if r["verdict"] == "warn"]
    removed = 0
    if dead and args.strip:
        dead_urls = {r["url"] for r in dead}
        for u in content_units(units(body)):
            for s in sentences(u["text"]):
                if any(url in dead_urls for _, url in links_in(s)) and s in body:
                    body = body.replace(s, "", 1)
                    removed += 1
        src = body.split("\n")
        keep = []
        for u in units(body):
            if u["kind"] in ("para", "li", "quote", "row") and not re.search(r"[A-Za-z0-9ऀ-ॿ]", u["text"]):
                continue
            keep.append(src[u["line"] - 1])
        body = re.sub(r"\n{3,}", "\n\n", "\n".join(keep)).strip("\n") + "\n"
        new_text = head + body
        if removed:
            try:
                cur = int(fm.get("items_dropped") or 0)
            except ValueError:
                cur = 0
            new_text = set_front_matter_value(new_text, "items_dropped", str(cur + removed))
        write_text(path, new_text)
    out = {"week": args.week, "edition": args.edition, "checked": len(results), "dead": len(dead), "warn": len(warn),
           "removed_sentences": removed, "results": results}
    write_json(os.path.join(d, f"links-{args.edition}.json"), out)
    for r in dead:
        print(f"DEAD {r['status']} {r['url']}")
    for r in warn:
        print(f"warn {r['status']} {r['url']}  ({r['note']})")
    print(json.dumps({k: out[k] for k in ("checked", "dead", "warn", "removed_sentences")}))
    return 1 if (dead and not args.strip) else 0
