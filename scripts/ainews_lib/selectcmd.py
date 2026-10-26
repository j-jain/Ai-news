"""`ainews select`: merge candidate files into verified.json (what writers may cite) and dropped.json (why not)."""
import datetime as dt
import glob
import json
import os

from common import (INDIA_BEATS, canonical_url, now_iso, p, parse_date, read_json, read_jsonl, story_key, url_id,
                    work_dir, write_json)
from quotes import verify_item

CAPS = {"india": 26, "world": 26}
MIN_PER_BEAT = 2
MAX_FOLLOWUPS = 3
FOLLOWUP_GRACE_DAYS = 7


def default_edition(beat):
    b = (beat or "").lower()
    return "india" if b in INDIA_BEATS or b.startswith("india") else "world"


def editions_for(item):
    e = (item.get("edition") or "").lower().strip()
    if e == "both":
        return ["india", "world"]
    if e in ("india", "world"):
        return [e]
    return [default_edition(item.get("beat"))]


def _drop(it, reason):
    return {"id": it.get("id") or (url_id(it["url"]) if it.get("url") else None), "beat": it.get("beat"),
            "headline": it.get("headline"), "url": it.get("url"), "reason": reason}


def _deadline_ok(opp, today_d):
    dl = (opp.get("deadline") or "").strip().lower()
    if dl == "rolling":
        return True
    d = parse_date(dl)
    return bool(d and d >= today_d)


def _score(it):
    try:
        s = float(it.get("significance") or it.get("score") or 2)
    except (TypeError, ValueError):
        s = 2.0
    s = max(1.0, min(5.0, s))
    if it.get("fetch_tier") == "A":
        s += 0.5
    if (it.get("source_type") or "").lower() == "primary":
        s += 0.5
    return s


def _merge(keep, other):
    extra = [other.get("url")] + list(other.get("secondary_urls") or [])
    sec = list(keep.get("secondary_urls") or [])
    for u in extra:
        if u and canonical_url(u) != canonical_url(keep["url"]) and u not in sec:
            sec.append(u)
    keep["secondary_urls"] = sec
    keep["editions"] = sorted(set(keep.get("editions", [])) | set(other.get("editions", [])))


def _sort_key(it):
    d = parse_date(it.get("published"))
    return (-it["score"], -(d.toordinal() if d else 0))


def run(args):
    week = args.week
    d = work_dir(week, create=False)
    meta = read_json(os.path.join(d, "meta.json"), None)
    if not meta:
        raise SystemExit("meta.json missing: run `ainews week` first")
    ws, we = parse_date(meta["window_start"]), parse_date(meta["window_end"])
    today_d = dt.date.today()
    seen = read_json(p("state", "seen.json"), {}) or {}
    seen_keys = {v.get("story_key") for v in seen.values() if isinstance(v, dict)}
    files = sorted(glob.glob(os.path.join(d, "candidates-*.json")))
    if not files:
        raise SystemExit("no candidates-*.json files found in " + d)
    dropped = []
    kept = {}
    story_index = {}
    n_candidates = 0
    for path in files:
        beat_from_file = os.path.basename(path)[len("candidates-"):-len(".json")]
        items = read_json(path, [])
        if not isinstance(items, list):
            dropped.append({"id": None, "beat": beat_from_file, "headline": os.path.basename(path), "url": None,
                            "reason": "file is not a JSON list"})
            continue
        for it in items:
            if not isinstance(it, dict):
                continue
            n_candidates += 1
            it.setdefault("beat", beat_from_file)
            missing = [k for k in ("headline", "url", "quote", "claim") if not str(it.get(k) or "").strip()]
            if missing:
                dropped.append(_drop(it, "missing " + ", ".join(missing)))
                continue
            if not verify_item(week, it):
                dropped.append(_drop(it, it.get("verify_note") or "quote not verified"))
                continue
            if it.get("published_unverified"):
                dropped.append(_drop(it, "published date has no evidence text in the page"))
                continue
            pub = parse_date(it.get("published"))
            is_opp = isinstance(it.get("opportunity"), dict)
            it["is_followup"] = False
            if pub is None:
                if not (is_opp and _deadline_ok(it["opportunity"], today_d)):
                    dropped.append(_drop(it, "no publication date found on the page"))
                    continue
            else:
                if pub > we and not is_opp:
                    dropped.append(_drop(it, f"published {pub} is after the window end {we}"))
                    continue
                if pub < ws:
                    fu = it.get("follow_up_of")
                    if fu and (fu in seen or fu in seen_keys) and pub >= ws - dt.timedelta(days=FOLLOWUP_GRACE_DAYS):
                        it["is_followup"] = True
                    elif is_opp and _deadline_ok(it["opportunity"], today_d):
                        pass
                    else:
                        dropped.append(_drop(it, f"published {pub} is before the window start {ws}"))
                        continue
            it["id"] = url_id(it["url"])
            it["canonical_url"] = canonical_url(it["url"])
            it["story_key"] = story_key(it.get("headline"))
            it["editions"] = editions_for(it)
            if (it["id"] in seen or it["story_key"] in seen_keys) and not it["is_followup"]:
                dropped.append(_drop(it, "already covered in an earlier week"))
                continue
            it["score"] = _score(it)
            if it["id"] in kept:
                other = kept[it["id"]]
                if it["score"] > other["score"]:
                    _merge(it, other)
                    kept[it["id"]] = it
                else:
                    _merge(other, it)
                continue
            if it["story_key"] in story_index:
                oid = story_index[it["story_key"]]
                other = kept[oid]
                if it["score"] > other["score"]:
                    _merge(it, other)
                    del kept[oid]
                    kept[it["id"]] = it
                    story_index[it["story_key"]] = it["id"]
                else:
                    _merge(other, it)
                continue
            kept[it["id"]] = it
            story_index[it["story_key"]] = it["id"]

    selected = {}
    for ed in ("india", "world"):
        pool = sorted([it for it in kept.values() if ed in it["editions"]], key=_sort_key)
        by_beat = {}
        for it in pool:
            by_beat.setdefault(it["beat"], []).append(it)
        chosen = []
        for lst in by_beat.values():
            chosen.extend(lst[:MIN_PER_BEAT])
        for it in pool:
            if len(chosen) >= CAPS[ed]:
                break
            if it not in chosen:
                chosen.append(it)
        chosen = sorted(chosen[:CAPS[ed]], key=_sort_key)
        fus = [it for it in chosen if it["is_followup"]]
        for it in fus[MAX_FOLLOWUPS:]:
            chosen.remove(it)
            dropped.append(_drop(it, f"more than {MAX_FOLLOWUPS} follow-ups"))
        selected[ed] = chosen
    used = {}
    for ed, lst in selected.items():
        for it in lst:
            used.setdefault(it["id"], it)
            it.setdefault("used_in", [])
            if ed not in it["used_in"]:
                it["used_in"].append(ed)
    for it in kept.values():
        if it["id"] not in used:
            dropped.append(_drop(it, "below the cut (edition cap reached)"))
    items = sorted(used.values(), key=lambda x: (x["beat"], _sort_key(x)))
    fetch_log = read_jsonl(os.path.join(d, "fetch-log.jsonl"))
    pages_ok = {e.get("id") for e in fetch_log if e.get("status") == 200 and e.get("text_file")}
    counts = {
        "candidates": n_candidates, "verified": len(items), "dropped": len(dropped), "pages_fetched": len(pages_ok),
        "india": len(selected["india"]), "world": len(selected["world"]),
        "tier_b": sum(1 for it in items if it.get("fetch_tier") == "B"),
        "followups": sum(1 for it in items if it.get("is_followup")),
    }
    out = {"week": week, "window_start": meta["window_start"], "window_end": meta["window_end"],
           "generated_at": now_iso(), "counts": counts, "items": items}
    write_json(os.path.join(d, "verified.json"), out)
    write_json(os.path.join(d, "dropped.json"), dropped)
    print(json.dumps(counts, ensure_ascii=False))
    for ed in ("india", "world"):
        beats = {}
        for it in selected[ed]:
            beats[it["beat"]] = beats.get(it["beat"], 0) + 1
        print(f"{ed:>5}: {len(selected[ed])} items  " + ", ".join(f"{b}={n}" for b, n in sorted(beats.items())))
    reasons = {}
    for x in dropped:
        key = x["reason"].split(":")[0].split(" is ")[0][:60]
        reasons[key] = reasons.get(key, 0) + 1
    if reasons:
        print("dropped: " + "; ".join(f"{k} ({v})" for k, v in sorted(reasons.items(), key=lambda kv: -kv[1])))
    return 0 if items else 1
