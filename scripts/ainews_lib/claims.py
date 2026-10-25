"""`ainews claims` (pair every sentence with its evidence) and `ainews apply-factcheck` (apply verdicts)."""
import json
import os
import re

from common import (canonical_url, parse_front_matter, read_json, read_text, rel, set_front_matter_value, url_id,
                    work_dir, write_json, write_text)
from fetch import load_page
from mdunits import content_units, links_in, normalize_paragraphs, sentences, units


def draft_path(week, edition):
    return os.path.join(work_dir(week, create=False), f"draft-{edition}.md")


def normalized_draft(path):
    """Join hard-wrapped lines so every sentence is a substring of one line; returns the body."""
    text = read_text(path)
    fm, body, _ = parse_front_matter(text)
    nb = normalize_paragraphs(body)
    if nb != body:
        head = text[: len(text) - len(body)]
        write_text(path, head + nb)
        body = nb
    return body


def context_for(page_text, quote, width=700):
    if not page_text:
        return ""
    q = (quote or "").strip().lower()
    if q:
        probe = q[:60]
        i = page_text.lower().find(probe)
        if i >= 0:
            return page_text[max(0, i - width): i + len(q) + width]
    return page_text[:1400]


def build_claims(week, edition):
    path = draft_path(week, edition)
    body = normalized_draft(path)
    d = work_dir(week, create=False)
    verified = read_json(os.path.join(d, "verified.json"), {}) or {}
    by_canon = {canonical_url(it["url"]): it for it in verified.get("items", []) if it.get("url")}
    claims, unlinked = [], []
    n = 0
    for u in content_units(units(body)):
        for s in sentences(u["text"]):
            links = links_in(s)
            if not links:
                if not u["exempt"] and u["kind"] != "row-header":
                    unlinked.append({"line": u["line"], "section": u["section"], "sentence": s})
                continue
            n += 1
            evidence = []
            for chip, url in links:
                it = by_canon.get(canonical_url(url))
                page_text, meta, tier = load_page(week, url_id(url))
                evidence.append({
                    "chip": chip, "url": url, "id": url_id(url), "in_verified": bool(it), "tier": tier,
                    "page_file": (meta or {}).get("text_file"), "headline": (it or {}).get("headline"),
                    "claim": (it or {}).get("claim"), "quote": (it or {}).get("quote"),
                    "published": (it or {}).get("published"),
                    "context": context_for(page_text, (it or {}).get("quote")),
                })
            claims.append({"n": n, "line": u["line"], "section": u["section"], "kind": u["kind"],
                           "opinion": u["exempt"], "sentence": s, "evidence": evidence})
    out = {
        "week": week, "edition": edition, "draft": rel(path), "claims": claims, "unlinked": unlinked,
        "how_to_answer": ("Write factcheck-<edition>.json as {\"verdicts\": [{\"n\": N, \"verdict\": \"pass|fix|reject\", "
                          "\"reason\": \"...\", \"replacement\": \"full corrected sentence incl. its chips (fix only)\"}]}. "
                          "pass = every name, number, date and causal claim in the sentence is supported by the saved page(s); "
                          "fix = supportable with a correction; reject = not supported by the cited page."),
    }
    write_json(os.path.join(d, f"claims-{edition}.json"), out)
    return out


def apply_factcheck(week, edition, strip=False, verdicts_path=None):
    d = work_dir(week, create=False)
    path = draft_path(week, edition)
    text = read_text(path)
    fm, body, _ = parse_front_matter(text)
    head = text[: len(text) - len(body)]
    body = normalize_paragraphs(body)
    claims = read_json(os.path.join(d, f"claims-{edition}.json"), {}) or {}
    raw = read_json(verdicts_path or os.path.join(d, f"factcheck-{edition}.json"), None)
    if raw is None:
        raise SystemExit(f"factcheck-{edition}.json missing")
    vlist = raw.get("verdicts") if isinstance(raw, dict) else raw
    vmap = {}
    for v in vlist or []:
        try:
            vmap[int(v["n"])] = v
        except (KeyError, TypeError, ValueError):
            continue
    fixed = rejected = kept_unjudged = 0
    notes = []
    for c in sorted(claims.get("claims", []), key=lambda c: c["n"]):
        v = vmap.get(c["n"])
        verdict = ((v or {}).get("verdict") or "").lower().strip()
        sent = c["sentence"]
        if verdict == "pass":
            continue
        if verdict == "fix" and (v.get("replacement") or "").strip():
            rep = v["replacement"].strip()
            if sent in body:
                body = body.replace(sent, rep, 1)
                fixed += 1
            else:
                notes.append(f"n={c['n']}: sentence not found for fix")
            continue
        if verdict == "reject" or (strip and verdict != "pass"):
            if sent in body:
                body = body.replace(sent, "", 1)
                rejected += 1
            else:
                notes.append(f"n={c['n']}: sentence not found for reject")
            continue
        if not v:
            kept_unjudged += 1
    body = re.sub(r"[ \t]{2,}", " ", body)
    body = re.sub(r"\s+([.,;:!?])", r"\1", body)
    src = body.split("\n")
    keep = []
    removed_units = 0
    for u in units(body):
        line = src[u["line"] - 1]
        if u["kind"] in ("para", "li", "quote", "row"):
            txt = u["text"]
            if not re.search(r"[A-Za-z0-9ऀ-ॿ]", txt):
                removed_units += 1
                continue
            if strip and not u["exempt"] and not u["footer"] and not links_in(txt):
                removed_units += 1
                continue
        keep.append(line)
    body = re.sub(r"\n{3,}", "\n\n", "\n".join(keep)).strip("\n") + "\n"
    new_text = head + body
    if rejected:
        try:
            cur = int(fm.get("items_dropped") or 0)
        except ValueError:
            cur = 0
        new_text = set_front_matter_value(new_text, "items_dropped", str(cur + rejected))
    write_text(path, new_text)
    summary = {"edition": edition, "claims": len(claims.get("claims", [])), "verdicts": len(vmap), "fixed": fixed,
               "rejected": rejected, "units_removed": removed_units, "kept_without_verdict": kept_unjudged,
               "notes": notes}
    return summary


def run_claims(args):
    out = build_claims(args.week, args.edition)
    print(json.dumps({"claims": len(out["claims"]), "unlinked_sentences": len(out["unlinked"]),
                      "file": f"work/{args.week}/claims-{args.edition}.json"}, ensure_ascii=False))
    for u in out["unlinked"][:20]:
        print(f"  unlinked line {u['line']} [{u['section']}]: {u['sentence'][:90]}")
    return 0


def run_apply(args):
    summary = apply_factcheck(args.week, args.edition, strip=args.strip, verdicts_path=args.verdicts)
    print(json.dumps(summary, ensure_ascii=False))
    return 0
