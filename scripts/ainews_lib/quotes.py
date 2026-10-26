"""`ainews verify-quotes`: a candidate's quote must be a substring of the saved page. A script decides, not a model."""
import json
import os

from common import host_of, norm_text, read_json, url_id, word_count, write_json
from fetch import load_page

MAX_QUOTE_WORDS = 25


def check_quote(quote, text):
    if not quote or not str(quote).strip():
        return False, "missing quote"
    n = word_count(quote)
    if n > MAX_QUOTE_WORDS:
        return False, f"quote is {n} words; the limit is {MAX_QUOTE_WORDS}"
    if norm_text(quote) in norm_text(text):
        return True, ""
    return False, "quote not found in the saved page (copy it verbatim, including punctuation)"


def verify_item(week, item):
    """Annotate one candidate in place. Returns True when its quote is verified."""
    url = (item.get("url") or "").strip()
    if not url:
        item["quote_verified"] = "none"
        item["verify_note"] = "missing url"
        return False
    id_ = url_id(url)
    item["id"] = id_
    text, meta, tier = load_page(week, id_)
    if text is None:
        item["quote_verified"] = "none"
        item["verify_note"] = "page not fetched: run `ainews fetch` on this exact url first"
        return False
    ok, why = check_quote(item.get("quote"), text)
    item["fetch_tier"] = tier
    item["page_file"] = (meta or {}).get("text_file")
    item["quote_verified"] = ("script" if tier == "A" else "model") if ok else "none"
    item["verify_note"] = why
    if meta:
        item.pop("published_unverified", None)
        if meta.get("published"):
            item["published"] = meta["published"]
            item["published_evidence"] = meta.get("published_evidence")
        elif item.get("published"):
            ev = item.get("published_evidence") or ""
            if ev.startswith("text: "):
                ev = ev[len("text: "):]
            if ev and norm_text(ev) in norm_text(text):
                item["published_evidence"] = f"text: {ev}"
            else:
                item["published_unverified"] = True
                item["verify_note"] = (why + "; " if why else "") + \
                    "published date has no evidence text found in the page (set published_evidence to a verbatim snippet)"
        if not item.get("source_name"):
            item["source_name"] = meta.get("site_name") or host_of(url)
        if not item.get("title") and meta.get("title"):
            item["title"] = meta["title"]
    opp = item.get("opportunity")
    if isinstance(opp, dict) and opp.get("eligibility_quote"):
        opp["eligibility_verified"] = norm_text(opp["eligibility_quote"]) in norm_text(text)
    return ok


def verify_file(week, path):
    items = read_json(path, None)
    if not isinstance(items, list):
        raise SystemExit(f"{path}: expected a JSON list of candidate items")
    results = []
    for it in items:
        ok = verify_item(week, it)
        results.append((ok, it))
    write_json(path, items)
    return results


def run(args):
    results = verify_file(args.week, args.file)
    bad = 0
    for ok, it in results:
        flag = "OK " if ok else "BAD"
        if not ok:
            bad += 1
        print(f"{flag} {it.get('id', '-'):<12} {it.get('quote_verified', '-'):<6} pub={it.get('published') or '----------'} "
              f"{(it.get('headline') or '')[:60]}")
        if not ok:
            print(f"      -> {it.get('verify_note')}")
    print(json.dumps({"file": os.path.basename(args.file), "items": len(results), "verified": len(results) - bad,
                      "failed": bad}))
    return 1 if bad else 0
