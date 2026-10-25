"""`ainews publish`: move drafts into _issues/, update state, commit, push, enable/poll GitHub Pages."""
import datetime as dt
import json
import os
import time

from common import (LINK_RE, SITE_URL, canonical_url, git, gh, p, parse_front_matter, read_json, read_text, rel,
                    repo_slug, set_front_matter_value, today, week_bounds, work_dir, write_json, write_text)
from fetch import http_get

EDITION_NAMES = {"india": "India + Opportunities", "world": "World"}


def issue_filename(week, edition):
    return f"{week}-{edition}.md"


def ensure_pages(slug):
    r = gh("api", f"repos/{slug}/pages", check=False)
    if r.returncode == 0:
        try:
            return {"created": False, **json.loads(r.stdout)}
        except json.JSONDecodeError:
            return {"created": False}
    body = json.dumps({"build_type": "legacy", "source": {"branch": "main", "path": "/"}})
    r = gh("api", "-X", "POST", f"repos/{slug}/pages", "--input", "-", input_text=body, check=False)
    if r.returncode != 0:
        raise SystemExit(f"could not enable GitHub Pages: {(r.stderr or r.stdout).strip()}")
    try:
        return {"created": True, **json.loads(r.stdout)}
    except json.JSONDecodeError:
        return {"created": True}


def poll_build(slug, sha, timeout=360):
    deadline = time.time() + timeout
    last = None
    while time.time() < deadline:
        r = gh("api", f"repos/{slug}/pages/builds/latest", check=False)
        if r.returncode == 0:
            try:
                b = json.loads(r.stdout)
            except json.JSONDecodeError:
                b = {}
            last = {"status": b.get("status"), "commit": b.get("commit"),
                    "error": (b.get("error") or {}).get("message"), "duration_ms": b.get("duration")}
            if last["commit"] == sha and last["status"] in ("built", "errored"):
                return last
        time.sleep(15)
    return last or {"status": "unknown", "commit": None, "error": "no build information yet"}


def run(args):
    week = args.week
    d = work_dir(week, create=False)
    meta = read_json(os.path.join(d, "meta.json"), {}) or {}
    editions = ["india", "world"] if args.editions in ("both", None, "") else [args.editions]
    slug = repo_slug()
    if os.path.exists(p(".nojekyll")):
        raise SystemExit(".nojekyll is present; it would make Pages serve raw Markdown. Delete it.")
    verified = read_json(os.path.join(d, "verified.json"), {}) or {}
    published_files = []
    cited_urls_by_ed = {}
    if not args.no_issues:
        for ed in editions:
            draft = os.path.join(d, f"draft-{ed}.md")
            if not os.path.exists(draft):
                raise SystemExit(f"missing draft: {draft}")
            lint = read_json(os.path.join(d, f"lint-{ed}.json"), None)
            if not args.force and (lint is None or lint.get("errors")):
                raise SystemExit(f"lint for {ed} is not clean; run `ainews lint --week {week} --edition {ed}` (or --force)")
            text = read_text(draft)
            fm, body, _ = parse_front_matter(text)
            urls = {canonical_url(u) for _, u in LINK_RE.findall(body)}
            cited = sorted(u for u in urls if not u.startswith(("https://github.com/j-jain", "https://j-jain.github.io")))
            cited_urls_by_ed[ed] = set(cited)
            text = set_front_matter_value(text, "sources_fetched", str(len(cited)))
            if not fm.get("items_dropped"):
                text = set_front_matter_value(text, "items_dropped", "0")
            if args.dry_run:
                write_text(os.path.join(d, "preview", issue_filename(week, ed)), text)
            else:
                dest = p("_issues", issue_filename(week, ed))
                write_text(dest, text)
                published_files.append(rel(dest))
    expected_urls = ([f"{SITE_URL}/issues/{week}-{ed}/" for ed in editions] if not args.no_issues else [SITE_URL + "/"])
    if args.dry_run:
        print(json.dumps({"dry_run": True, "preview_dir": rel(os.path.join(d, "preview")), "would_publish": expected_urls}))
        return 0

    seen = read_json(p("state", "seen.json"), {}) or {}
    for ed in editions:
        for it in verified.get("items", []):
            if canonical_url(it.get("url", "")) in cited_urls_by_ed.get(ed, set()):
                prev = seen.get(it["id"], {})
                seen[it["id"]] = {"story_key": it.get("story_key"), "url": it.get("url"), "headline": it.get("headline"),
                                  "first_seen": prev.get("first_seen", week), "edition": ed}
    cutoff = today() - dt.timedelta(days=120)
    for id_, v in list(seen.items()):
        try:
            if week_bounds(v.get("first_seen", ""))[0] < cutoff:
                del seen[id_]
        except ValueError:
            pass
    write_json(p("state", "seen.json"), seen)
    last = {"week": week, "run_date": today().isoformat(), "window_start": meta.get("window_start"),
            "window_end": meta.get("window_end"), "editions": editions, "counts": verified.get("counts", {}),
            "published_files": published_files, "urls": expected_urls}
    if not args.no_issues:
        write_json(p("state", "last-run.json"), last)

    git("add", "-A")
    changed = git("status", "--porcelain").stdout.strip()
    committed = False
    if changed:
        if args.message:
            msg = args.message
        elif args.no_issues:
            msg = "Site update"
        else:
            msg = f"Week {week}: " + " and ".join(EDITION_NAMES[e] for e in editions) + " edition" + ("s" if len(editions) > 1 else "")
        if args.trailer:
            msg += "\n\n" + args.trailer
        git("commit", "-q", "-m", msg)
        committed = True
    sha = git("rev-parse", "HEAD").stdout.strip()
    pushed, err = False, None
    for attempt in range(3):
        r = git("push", "-u", "origin", "HEAD:main", check=False)
        if r.returncode == 0:
            pushed = True
            break
        err = (r.stderr or r.stdout).strip()
        time.sleep(5 * (attempt + 1))
    if not pushed:
        raise SystemExit(f"git push failed after 3 attempts: {err}")
    pages = ensure_pages(slug) if args.ensure_pages else None
    build = poll_build(slug, sha, timeout=args.poll_timeout)
    live = []
    if build.get("status") == "built":
        time.sleep(5)
        for u in expected_urls:
            r = http_get(u, retries=2)
            live.append({"url": u, "status": r["status"]})
    summary = {"week": week, "editions": editions, "committed": committed, "sha": sha, "pushed": pushed,
               "pages": {k: pages.get(k) for k in ("created", "html_url", "status")} if pages else None,
               "build": build, "live": live, "published_files": published_files}
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if build.get("status") == "built" else 1
