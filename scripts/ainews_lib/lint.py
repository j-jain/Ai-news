"""`ainews lint`: the mechanical gate a draft must pass before publishing."""
import json
import os
import re

from common import (LINK_RE, URL_RE, canonical_url, p, parse_date, parse_front_matter, read_json, read_text, rel,
                    strip_links, word_count, work_dir, write_json, write_text)
from mdunits import INCLUDE_LINE, content_units, links_in, normalize_paragraphs, units

HARD_MIN, HARD_MAX, SOFT_MIN, SOFT_MAX = 1400, 2300, 1600, 2200
GENERIC_CHIPS = {"here", "link", "source", "this", "read more", "more", "article", "page", "website", "click here",
                 "see", "via", "details", "post", "blog"}
ALLOWED_PREFIXES = ("https://github.com/j-jain/Ai-news/", "https://j-jain.github.io/Ai-news/")
REQUIRED_FM = ("layout", "title", "edition", "week", "date", "window", "summary", "sources_fetched", "items_dropped")


def E(rule, line, msg):
    return {"rule": rule, "line": line, "msg": msg}


def load_banned():
    path = p("scripts", "banned-phrases.txt")
    out = []
    if not os.path.exists(path):
        return out
    for line in read_text(path).splitlines():
        ph = line.strip()
        if not ph or ph.startswith("#"):
            continue
        out.append((ph, re.compile(r"(?<![\w-])" + re.escape(ph).replace(r"\ ", r"[\s-]+") + r"(?![\w-])", re.I)))
    return out


def lint(path, verified_path=None, window=None, fix=False):
    text = read_text(path)
    errors, warnings = [], []
    fm, body, fm_text = parse_front_matter(text)
    original_body = body
    if not fm:
        errors.append(E("front-matter", 1, "missing front matter block (--- ... ---)"))
    for k in REQUIRED_FM:
        if k not in fm:
            errors.append(E("front-matter", 1, f"missing `{k}`"))
    if fm.get("layout", "issue") != "issue":
        errors.append(E("front-matter", 1, "layout must be `issue`"))
    if fm.get("edition") not in ("india", "world"):
        errors.append(E("front-matter", 1, "edition must be india or world"))
    if not re.fullmatch(r"\d{4}-W\d{2}", fm.get("week", "")):
        errors.append(E("front-matter", 1, "week must look like 2026-W43"))
    if not parse_date(fm.get("date", "")):
        errors.append(E("front-matter", 1, "date must be YYYY-MM-DD"))
    for k in ("sources_fetched", "items_dropped"):
        if k in fm and not re.fullmatch(r"\d+", fm.get(k, "")):
            errors.append(E("front-matter", 1, f"`{k}` must be an integer"))
    for k in ("title", "summary", "week", "window"):
        if k in fm and not re.search(rf'^{k}:\s*"', fm_text, re.M):
            errors.append(E("front-matter", 1, f"`{k}` must be double-quoted"))
        if '"' in fm.get(k, ""):
            errors.append(E("front-matter", 1, f"`{k}` contains a raw double quote; use single quotes inside"))
    if fm.get("title") and word_count(fm["title"]) > 16:
        warnings.append(E("front-matter", 1, "title longer than 16 words"))
    if fm.get("summary") and word_count(fm["summary"]) > 40:
        warnings.append(E("front-matter", 1, "summary longer than 40 words"))

    nb = normalize_paragraphs(body)
    if nb != body:
        if fix:
            body = nb
        else:
            warnings.append(E("wrapped-lines", 0, "paragraphs are hard-wrapped; run with --fix to join them"))
    lines = body.split("\n")
    for i, line in enumerate(lines, 1):
        if line.strip() == INCLUDE_LINE:
            continue
        if "{{" in line or "{%" in line:
            if fix:
                lines[i - 1] = line.replace("{{", "{ {").replace("{%", "{ %")
                warnings.append(E("liquid", i, "escaped raw Liquid braces"))
            else:
                errors.append(E("liquid", i, "raw `{{` or `{%` (only the opportunities include line is allowed)"))
        if re.search(r"<[a-zA-Z/!]", line) and not line.lstrip().startswith("<!--"):
            errors.append(E("raw-html", i, "raw HTML tag in Markdown body"))
    body = "\n".join(lines)
    us = units(body)
    cu = content_units(us)

    items_by_canon = {}
    if verified_path and os.path.exists(verified_path):
        v = read_json(verified_path, {}) or {}
        for it in v.get("items", []):
            if it.get("url"):
                items_by_canon[canonical_url(it["url"])] = it
    else:
        warnings.append(E("verified", 0, "no verified.json given; URL whitelist and date checks skipped"))
    ws = we = None
    if window:
        ws, we = window
    elif fm.get("window"):
        m = re.findall(r"\d{4}-\d{2}-\d{2}", fm["window"])
        if len(m) >= 2:
            ws, we = parse_date(m[0]), parse_date(m[1])

    link_count = 0
    for u in cu:
        links = links_in(u["text"])
        link_count += len(links)
        if not links and not u["exempt"] and u["kind"] != "row-header":
            errors.append(E("no-link", u["line"], f"no source link: {u['text'][:80]}"))
        if re.search(r"[.!?][\"”')\]]*\s+\[[^\]]+\]\(https?://", u["text"]):
            errors.append(E("chip-after-stop", u["line"], "the link sits after the full stop; move it inside the sentence"))
        for chip, url in links:
            words = chip.strip().split()
            if not 1 <= len(words) <= 4:
                errors.append(E("chip-text", u["line"], f"chip text must be 1-4 words: [{chip}]"))
            if chip.strip().lower() in GENERIC_CHIPS:
                errors.append(E("chip-text", u["line"], f"chip text is generic: [{chip}]; name the source"))
            c = canonical_url(url)
            if items_by_canon and c not in items_by_canon and not url.startswith(ALLOWED_PREFIXES):
                errors.append(E("url-not-verified", u["line"], f"{url} is not in verified.json"))
            it = items_by_canon.get(c)
            if it and ws and we and not u["footer"]:
                pub = parse_date(it.get("published"))
                if it.get("is_followup") or isinstance(it.get("opportunity"), dict):
                    pass
                elif pub is None:
                    errors.append(E("no-date", u["line"], f"{url} has no publication date"))
                elif not (ws <= pub <= we):
                    errors.append(E("date-outside-window", u["line"], f"{url} was published {pub}, outside {ws}..{we}"))
        rest = LINK_RE.sub("", u["text"])
        for m in URL_RE.findall(rest):
            errors.append(E("bare-url", u["line"], f"bare URL {m[:60]}; write it as [Source name](url)"))

    prose = "\n".join(u["text"] for u in us if not u["footer"] and u["kind"] in ("para", "li", "row", "quote", "heading"))
    prose_nolinks = strip_links(prose)
    seen_phrases = set()
    for ph, rx in load_banned():
        if rx.search(prose_nolinks) and ph not in seen_phrases:
            seen_phrases.add(ph)
            errors.append(E("banned-phrase", 0, f"banned phrase: '{ph}'"))
    words = word_count(prose_nolinks)
    if words < HARD_MIN or words > HARD_MAX:
        errors.append(E("word-count", 0, f"{words} words in the body; must be {HARD_MIN}-{HARD_MAX}"))
    elif words < SOFT_MIN or words > SOFT_MAX:
        warnings.append(E("word-count", 0, f"{words} words; aim for {SOFT_MIN}-{SOFT_MAX}"))

    tt = [u for u in us if u["kind"] == "heading" and re.search(r"three things|read nothing else|only read", u["text"], re.I)]
    if tt:
        sec = tt[0]["text"]
        lis = [u for u in us if u["section"] == sec and u["kind"] == "li"]
        if len(lis) != 3:
            errors.append(E("three-things", tt[0]["line"], f"needs exactly 3 bullets, found {len(lis)}"))
        for u in lis:
            ls = links_in(u["text"])
            if not ls:
                errors.append(E("three-things", u["line"], "each of the three things needs a source link"))
            for _, url in ls:
                it = items_by_canon.get(canonical_url(url))
                if it and it.get("fetch_tier") == "B":
                    errors.append(E("three-things", u["line"], "a Tier-B (WebFetch-only) source cannot headline the three things"))
    else:
        warnings.append(E("three-things", 0, "no 'If you only read three things' section"))
    h2 = [u for u in us if u["kind"] == "heading" and u.get("level") == 2]
    if len(h2) < 5:
        warnings.append(E("sections", 0, f"only {len(h2)} H2 sections"))
    if fix and body != original_body:
        head = text[: len(text) - len(original_body)]
        write_text(path, head + body)
    stats = {"words": words, "links": link_count, "units": len(cu), "h2": len(h2)}
    return {"path": rel(path), "errors": errors, "warnings": warnings, "stats": stats}


def run(args):
    if args.path:
        path, verified_path, window = args.path, args.verified, None
        out_path = None
    else:
        if not (args.week and args.edition):
            raise SystemExit("give --week and --edition, or --path")
        d = work_dir(args.week, create=False)
        path = os.path.join(d, f"draft-{args.edition}.md")
        verified_path = args.verified or os.path.join(d, "verified.json")
        meta = read_json(os.path.join(d, "meta.json"), {}) or {}
        window = (parse_date(meta.get("window_start")), parse_date(meta.get("window_end"))) if meta else None
        if window and not all(window):
            window = None
        out_path = os.path.join(d, f"lint-{args.edition}.json")
    if not os.path.exists(path):
        raise SystemExit(f"no such draft: {path}")
    res = lint(path, verified_path=verified_path, window=window, fix=args.fix)
    if out_path:
        write_json(out_path, res)
    for e in res["errors"]:
        print(f"ERROR {e['rule']:<20} L{e['line']:<4} {e['msg']}")
    for w in res["warnings"]:
        print(f"warn  {w['rule']:<20} L{w['line']:<4} {w['msg']}")
    print(json.dumps({"errors": len(res["errors"]), "warnings": len(res["warnings"]), **res["stats"]}))
    return 1 if res["errors"] else 0
