"""`ainews week`: decide the week id and the date window; write work/<week>/meta.json."""
import datetime as dt
import json
import os

from common import iso_week, p, parse_date, read_json, today, week_bounds, work_dir, write_json

MIN_DAYS = 5
MAX_DAYS = 14


def compute(week=None, since=None, editions="both", dry_run=False, force=False, run_date=None, last=None):
    run_date = run_date or today()
    if last is None:
        last = read_json(p("state", "last-run.json"), {}) or {}
    reason = ""
    if week:
        monday, sunday = week_bounds(week)
        ws = monday
        we = min(sunday, run_date)
        week_id = week
        explicit = True
    else:
        we = run_date - dt.timedelta(days=1)
        last_end = parse_date(last.get("window_end"))
        if since:
            ws = parse_date(since)
            if not ws:
                raise SystemExit(f"bad --since {since!r}; expected YYYY-MM-DD")
        elif last_end:
            ws = last_end + dt.timedelta(days=1)
        else:
            ws = we - dt.timedelta(days=6)
        if (we - ws).days + 1 > MAX_DAYS:
            ws = we - dt.timedelta(days=MAX_DAYS - 1)
        week_id = iso_week(we)
        explicit = False
    days = (we - ws).days + 1
    ok = True
    if days < 1:
        ok, reason = False, f"window is empty (start {ws} is after end {we})"
    elif days < MIN_DAYS and not (force or explicit):
        ok, reason = False, (f"only {days} new day(s) since the last issue (covered up to {last.get('window_end')}); "
                             f"nothing to do until at least {MIN_DAYS} days have passed. Use --force to override.")
    if explicit and last.get("week") == week_id and not force:
        reason = f"note: week {week_id} was already published on {last.get('run_date')}; this run replaces it"
    eds = ["india", "world"] if editions in ("both", None, "") else [editions]
    return {
        "week": week_id,
        "run_date": run_date.isoformat(),
        "window_start": ws.isoformat(),
        "window_end": we.isoformat(),
        "days": days,
        "editions": eds,
        "dry_run": bool(dry_run),
        "ok": ok,
        "reason": reason,
        "last_run": {k: last.get(k) for k in ("week", "run_date", "window_end")},
    }


def run(args):
    meta = compute(week=args.week, since=args.since, editions=args.editions, dry_run=args.dry_run, force=args.force)
    if meta["ok"]:
        d = work_dir(meta["week"])
        write_json(os.path.join(d, "meta.json"), meta)
        meta["work_dir"] = d.replace("\\", "/")
    print(json.dumps(meta, ensure_ascii=False, indent=2))
    return 0 if meta["ok"] else 2
