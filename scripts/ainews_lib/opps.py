"""`ainews opportunities`: --pull job boards into verifiable pages, --merge verified rows into _data, --check rows."""
import datetime as dt
import html as htmlmod
import json
import os
import re

from common import (append_jsonl, canonical_url, now_iso, p, parse_date, parse_loose_date, read_json, rel, url_id,
                    word_count, work_dir, write_json, write_text)
from fetch import decode_body, html_to_text, http_get, page_paths
from links import check_url

BOARDS = [
    {"name": "Anthropic", "kind": "greenhouse",
     "url": "https://boards-api.greenhouse.io/v1/boards/anthropic/jobs?content=true"},
    {"name": "xAI", "kind": "greenhouse", "url": "https://boards-api.greenhouse.io/v1/boards/xai/jobs?content=true"},
    {"name": "OpenAI", "kind": "ashby", "url": "https://api.ashbyhq.com/posting-api/job-board/openai"},
    {"name": "Sarvam AI", "kind": "ashby", "url": "https://api.ashbyhq.com/posting-api/job-board/sarvam"},
    {"name": "Perplexity", "kind": "ashby", "url": "https://api.ashbyhq.com/posting-api/job-board/perplexity"},
    {"name": "ElevenLabs", "kind": "ashby", "url": "https://api.ashbyhq.com/posting-api/job-board/elevenlabs"},
    {"name": "Scale AI", "kind": "greenhouse", "url": "https://boards-api.greenhouse.io/v1/boards/scaleai/jobs?content=true"},
    {"name": "Together AI", "kind": "greenhouse", "url": "https://boards-api.greenhouse.io/v1/boards/togetherai/jobs?content=true"},
]
TITLE_RE = re.compile(r"\b(intern|interns|internship|student|students|campus|fellow|fellows|fellowship|residen\w*|"
                      r"ambassador|apprentice\w*|new\s*grad\w*|early[-\s]?career|graduate|phd|scholar\w*)\b", re.I)
DATA_PATH = p("_data", "opportunities.json")
EXPECTED_AFTER_DAYS = 42
PRUNE_GRACE_DAYS = 3


def parse_board(b, data):
    out = []
    kind = b["kind"]
    if kind == "greenhouse":
        for j in data.get("jobs", []) or []:
            desc, _ = html_to_text(htmlmod.unescape(j.get("content") or ""))
            d = parse_loose_date(j.get("updated_at") or j.get("first_published"))
            out.append({"board": b["name"], "title": j.get("title") or "", "location": (j.get("location") or {}).get("name", ""),
                        "url": j.get("absolute_url") or "", "date": d.isoformat() if d else None,
                        "date_field": "updated_at", "employment": "", "description": desc})
    elif kind == "ashby":
        for j in data.get("jobs", []) or []:
            loc = j.get("location") or ""
            sec = ", ".join(s.get("location", "") for s in (j.get("secondaryLocations") or []) if s.get("location"))
            if sec:
                loc = f"{loc}; {sec}" if loc else sec
            if j.get("isRemote"):
                loc = (loc + "; remote").strip("; ")
            desc = j.get("descriptionPlain") or html_to_text(j.get("descriptionHtml") or "")[0]
            d = parse_loose_date(j.get("publishedAt"))
            out.append({"board": b["name"], "title": j.get("title") or "", "location": loc,
                        "url": j.get("jobUrl") or j.get("applyUrl") or "", "date": d.isoformat() if d else None,
                        "date_field": "publishedAt", "employment": j.get("employmentType") or "", "description": desc})
    elif kind == "lever":
        for j in data if isinstance(data, list) else []:
            cats = j.get("categories") or {}
            d = parse_loose_date(j.get("createdAt"))
            out.append({"board": b["name"], "title": j.get("text") or "", "location": cats.get("location") or "",
                        "url": j.get("hostedUrl") or "", "date": d.isoformat() if d else None,
                        "date_field": "createdAt", "employment": cats.get("commitment") or "",
                        "description": j.get("descriptionPlain") or ""})
    return [r for r in out if r["url"]]


def render_job_text(row):
    return (f"{row['title']}\nCompany: {row['board']}\nLocation: {row['location'] or 'not stated'}\n"
            f"Employment: {row.get('employment') or 'not stated'}\nPosted or updated: {row.get('date') or 'unknown'}\n"
            f"URL: {row['url']}\n\n{row.get('description') or ''}".strip())


def pull(week):
    d = work_dir(week, create=True)
    jobs, report = [], []
    for b in BOARDS:
        r = http_get(b["url"], accept="application/json")
        if r["status"] != 200:
            report.append({"board": b["name"], "status": r["status"], "error": r["error"], "jobs": 0, "matched": 0})
            continue
        try:
            data = json.loads(decode_body(r["body"], r["content_type"]))
        except json.JSONDecodeError as e:
            report.append({"board": b["name"], "status": 200, "error": f"bad JSON: {e}", "jobs": 0, "matched": 0})
            continue
        rows = parse_board(b, data)
        matched = [row for row in rows if TITLE_RE.search(row["title"])]
        report.append({"board": b["name"], "status": 200, "error": None, "jobs": len(rows), "matched": len(matched)})
        for row in matched:
            id_ = url_id(row["url"])
            text = render_job_text(row)
            a_path, _, m_path = page_paths(week, id_)
            write_text(a_path, text + "\n")
            meta = {"id": id_, "url": row["url"], "canonical_url": canonical_url(row["url"]), "final_url": row["url"],
                    "status": 200, "content_type": "application/json", "title": row["title"], "site_name": b["name"],
                    "published": row.get("date"),
                    "published_evidence": f"api field {row.get('date_field')}" if row.get("date") else None,
                    "fetched_at": now_iso(), "words": word_count(text), "thin": False, "tier": "A", "error": None,
                    "text_file": os.path.relpath(a_path, d).replace("\\", "/"), "source": "api"}
            write_json(m_path, meta)
            append_jsonl(os.path.join(d, "fetch-log.jsonl"), meta)
            row = dict(row)
            row.pop("description", None)
            row["id"] = id_
            row["page_file"] = meta["text_file"]
            jobs.append(row)
    write_json(os.path.join(d, "jobs.json"), {"pulled_at": now_iso(), "boards": report, "jobs": jobs})
    for rep in report:
        print(f"{rep['board']:<12} status={rep['status']} jobs={rep['jobs']} matched={rep['matched']} {rep['error'] or ''}")
    print(json.dumps({"matched_total": len(jobs), "file": f"work/{week}/jobs.json"}))
    return 0


def prune(rows, today_d):
    keep, pruned = [], []
    expected = 0
    for r in rows:
        dl = (r.get("deadline") or "rolling").strip()
        if dl.lower() != "rolling":
            d = parse_date(dl)
            if not d:
                pruned.append((r, "bad deadline"))
                continue
            if d < today_d - dt.timedelta(days=PRUNE_GRACE_DAYS):
                pruned.append((r, "deadline passed"))
                continue
        vo = parse_date(r.get("verified_on"))
        if vo and (today_d - vo).days > EXPECTED_AFTER_DAYS and r.get("status") == "open":
            r["status"] = "expected"
            expected += 1
        keep.append(r)
    keep.sort(key=lambda r: ((r.get("deadline") or "rolling").lower() == "rolling",
                             r.get("deadline") if (r.get("deadline") or "rolling").lower() != "rolling" else (r.get("title") or "").lower()))
    return keep, pruned, expected


def merge(week, today_d):
    d = work_dir(week, create=False)
    v = read_json(os.path.join(d, "verified.json"), {}) or {}
    rows = read_json(DATA_PATH, []) or []
    by_id = {r["id"]: r for r in rows if r.get("id")}
    added = updated = skipped = 0
    for it in v.get("items", []):
        opp = it.get("opportunity")
        if not isinstance(opp, dict):
            continue
        url = (opp.get("apply_url") or it.get("url") or "").strip()
        deadline = (opp.get("deadline") or "rolling").strip()
        if not url or (deadline.lower() != "rolling" and not parse_date(deadline)):
            skipped += 1
            continue
        id_ = url_id(url)
        row = {"id": id_, "title": opp.get("title") or it.get("headline"), "org": opp.get("org") or it.get("source_name") or "",
               "type": opp.get("type") or "opportunity", "audience": opp.get("audience") or "",
               "deadline": "rolling" if deadline.lower() == "rolling" else deadline, "url": url,
               "verified_on": today_d.isoformat(), "note": opp.get("note") or "", "status": "open", "first_seen": week}
        if id_ in by_id:
            by_id[id_].update({k: val for k, val in row.items() if k != "first_seen"})
            updated += 1
        else:
            by_id[id_] = row
            added += 1
    rows, pruned, expected = prune(list(by_id.values()), today_d)
    write_json(DATA_PATH, rows)
    diff = [f"# Opportunities diff, week {week}", "", f"- added: {added}", f"- updated: {updated}",
            f"- skipped (bad deadline or no url): {skipped}", f"- pruned: {len(pruned)}", f"- marked expected: {expected}", ""]
    for r, why in pruned:
        diff.append(f"- pruned `{r.get('title')}` ({why})")
    write_text(os.path.join(d, "opportunities-diff.md"), "\n".join(diff) + "\n")
    print(json.dumps({"added": added, "updated": updated, "skipped": skipped, "pruned": len(pruned),
                      "expected": expected, "rows": len(rows)}))
    return 0


def check(today_d):
    rows = read_json(DATA_PATH, []) or []
    removed = []
    for r in rows:
        st, verdict, note = check_url(r.get("url", ""))
        if verdict == "ok":
            r["verified_on"] = today_d.isoformat()
            dl = (r.get("deadline") or "rolling").lower()
            if dl == "rolling" or (parse_date(dl) and parse_date(dl) >= today_d):
                r["status"] = "open"
        elif verdict == "dead":
            removed.append(r)
        print(f"{verdict:<4} {st:<3} {r.get('title', '')[:50]:<50} {r.get('url', '')[:70]}")
    rows = [r for r in rows if r not in removed]
    rows, pruned, expected = prune(rows, today_d)
    write_json(DATA_PATH, rows)
    print(json.dumps({"checked": len(rows) + len(removed), "removed_dead": len(removed), "pruned": len(pruned),
                      "expected": expected, "rows": len(rows)}))
    return 0


def run(args):
    today_d = dt.date.today()
    if args.pull:
        if not args.week:
            raise SystemExit("--pull needs --week")
        return pull(args.week)
    if args.merge:
        if not args.week:
            raise SystemExit("--merge needs --week")
        return merge(args.week, today_d)
    if args.check:
        return check(today_d)
    raise SystemExit("choose one of --pull, --merge, --check")
