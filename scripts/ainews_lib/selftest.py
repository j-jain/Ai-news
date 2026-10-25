"""`ainews selftest`: exercise the pieces end to end on a scratch week (work/selftest). Network tests are skipped
with a note when the network is down, never faked."""
import datetime as dt
import json
import os
import shutil

from common import canonical_url, p, read_json, read_text, write_json, write_text, work_dir

WEEK = "selftest"
RESULTS = []


def ok(name, cond, note=""):
    RESULTS.append((name, "PASS" if cond else "FAIL", note))
    return cond


def skip(name, note):
    RESULTS.append((name, "SKIP", note))


def test_week():
    import weekcmd
    m = weekcmd.compute(run_date=dt.date(2026, 11, 2), last={"window_end": "2026-10-25"})
    ok("week.rolling", m["week"] == "2026-W44" and m["window_start"] == "2026-10-26" and m["window_end"] == "2026-11-01"
       and m["ok"], json.dumps({k: m[k] for k in ("week", "window_start", "window_end", "ok")}))
    m = weekcmd.compute(run_date=dt.date(2026, 10, 26), last={"window_end": "2026-10-25"})
    ok("week.empty-window", not m["ok"] and m["days"] == 0, m["reason"][:80])
    m = weekcmd.compute(run_date=dt.date(2026, 10, 29), last={"window_end": "2026-10-25"})
    ok("week.too-short", not m["ok"] and m["days"] == 3 and "nothing to do" in m["reason"], m["reason"][:80])
    m = weekcmd.compute(week="2026-W43", run_date=dt.date(2026, 10, 25), last={})
    ok("week.explicit", m["window_start"] == "2026-10-19" and m["window_end"] == "2026-10-25" and m["ok"],
       f"{m['window_start']}..{m['window_end']}")
    m = weekcmd.compute(run_date=dt.date(2026, 12, 1), last={"window_end": "2026-10-25"})
    ok("week.capped-14", m["days"] == 14, f"days={m['days']}")


def test_urls():
    ok("url.canonical", canonical_url("http://www.Example.com/a/b/?utm_source=x&id=2#frag") == "https://www.example.com/a/b?id=2",
       canonical_url("http://www.Example.com/a/b/?utm_source=x&id=2#frag"))


def test_normalize():
    from mdunits import normalize_paragraphs, units
    body = "## Head\n\nFirst line of a paragraph\nwraps here [Src](https://a.example/x).\n\n- item one\n  continues\n- item two\n"
    nb = normalize_paragraphs(body)
    ok("md.normalize", "paragraph wraps here" in nb and "item one continues" in nb, nb.replace("\n", "|")[:120])
    us = [u for u in units(nb) if u["kind"] in ("para", "li")]
    ok("md.units", len(us) == 3 and us[1]["kind"] == "li", f"{[u['kind'] for u in us]}")


def test_fetch_and_quotes():
    from fetch import fetch, load_page
    meta = fetch(WEEK, "https://example.com/", force=True)
    if meta.get("status") != 200 or not meta.get("text_file"):
        skip("fetch.example", f"network: status={meta.get('status')} err={meta.get('error')}")
        return None
    text, _, tier = load_page(WEEK, meta["id"])
    ok("fetch.example", bool(text) and tier == "A", f"{meta['words']} words, title={meta.get('title')!r}")
    words = text.split()
    true_quote = " ".join(words[:8])
    cand_path = os.path.join(work_dir(WEEK), "candidates-selftest.json")
    write_json(cand_path, [
        {"headline": "Example domain exists", "url": "https://example.com/", "quote": true_quote,
         "claim": "example.com is a reserved example domain", "beat": "selftest", "significance": 1},
        {"headline": "Fake quote", "url": "https://example.com/", "quote": "purple elephants negotiate quarterly budgets",
         "claim": "nonsense", "beat": "selftest", "significance": 1},
        {"headline": "Never fetched", "url": "https://example.org/never-fetched-page", "quote": "anything",
         "claim": "nonsense", "beat": "selftest", "significance": 1},
    ])
    from quotes import verify_file
    res = verify_file(WEEK, cand_path)
    flags = [r[0] for r in res]
    ok("quotes.verify", flags == [True, False, False], f"{flags}; notes={[r[1].get('verify_note') for r in res]}")
    return true_quote


def test_lint(true_quote):
    from lint import lint
    d = work_dir(WEEK)
    verified = {"week": WEEK, "window_start": "2026-10-19", "window_end": "2026-10-25", "items": [
        {"id": "x", "url": "https://example.com/", "headline": "h", "published": "2026-10-20", "fetch_tier": "A",
         "quote": true_quote or "q"}]}
    vpath = os.path.join(d, "verified-selftest.json")
    write_json(vpath, verified)
    filler = " ".join(["Verified words keep coming here [Example](https://example.com/)."] * 1)
    good_para = ("The example domain still answers on the web this week, which matters because every test needs a fixed point "
                 "[Example](https://example.com/).")
    bad = "\n".join([
        "---", 'layout: issue', 'title: "Test issue"', "edition: world", 'week: "2026-W43"', "date: 2026-10-25",
        'window: "2026-10-19 to 2026-10-25"', 'summary: "A test"', "sources_fetched: 1", "items_dropped: 0", "---", "",
        "## If you only read three things", "",
        "- **One** fact [Example](https://example.com/).", "- **Two** fact [Example](https://example.com/).",
        "", "## Frontier labs", "",
        "This paragraph has no link at all and is a game-changer.",
        "This one links after the stop. [Example](https://example.com/)",
        "This one cites an unverified page [Elsewhere](https://nowhere.example.net/page).",
        "Raw liquid {{ site.title }} appears here [Example](https://example.com/).",
        "Generic chip text [here](https://example.com/).",
        "", "## Sources & verification", "", "Pages fetched: 1.",
    ])
    bpath = os.path.join(d, "draft-selftest-bad.md")
    write_text(bpath, bad + "\n")
    res = lint(bpath, verified_path=vpath, window=(dt.date(2026, 10, 19), dt.date(2026, 10, 25)))
    rules = {e["rule"] for e in res["errors"]}
    expected = {"no-link", "banned-phrase", "chip-after-stop", "url-not-verified", "liquid", "chip-text", "word-count", "three-things"}
    ok("lint.catches", expected <= rules, f"missing={sorted(expected - rules)} extra={sorted(rules - expected)}")
    body = "\n".join([good_para] * 90)
    goodtext = "\n".join([
        "---", 'layout: issue', 'title: "Good test issue"', "edition: world", 'week: "2026-W43"', "date: 2026-10-25",
        'window: "2026-10-19 to 2026-10-25"', 'summary: "A good test"', "sources_fetched: 1", "items_dropped: 0", "---", "",
        "## If you only read three things", "",
        "- **One** fact [Example](https://example.com/).", "- **Two** fact [Example](https://example.com/).",
        "- **Three** fact [Example](https://example.com/).", "",
        "## Frontier labs", "", body, "", "**My read:** opinion needs no link.", "",
        "## Open and local", "", good_para, "", "## Hardware", "", good_para, "", "## People", "", good_para, "",
        "## Sources & verification", "", "Pages fetched: 1.",
    ])
    gpath = os.path.join(d, "draft-selftest-good.md")
    write_text(gpath, goodtext + "\n")
    res2 = lint(gpath, verified_path=vpath, window=(dt.date(2026, 10, 19), dt.date(2026, 10, 25)))
    ok("lint.passes-clean", not res2["errors"], f"errors={[e['rule'] + ':' + e['msg'][:40] for e in res2['errors']][:5]} words={res2['stats']['words']}")


def test_claims_apply():
    from claims import apply_factcheck, build_claims
    d = work_dir(WEEK)
    week_meta = {"week": WEEK, "window_start": "2026-10-19", "window_end": "2026-10-25"}
    write_json(os.path.join(d, "meta.json"), week_meta)
    write_json(os.path.join(d, "verified.json"), {"items": [
        {"id": "x", "url": "https://example.com/", "headline": "h", "claim": "c", "quote": "Example Domain", "published": "2026-10-20"}]})
    draft = "\n".join([
        "---", 'layout: issue', 'title: "T"', "edition: india", 'week: "2026-W43"', "date: 2026-10-25",
        'window: "2026-10-19 to 2026-10-25"', 'summary: "s"', "sources_fetched: 1", "items_dropped: 0", "---", "",
        "## Section", "",
        "First claim is wrong [Example](https://example.com/). Second claim is fine [Example](https://example.com/). Third claim is bad [Example](https://example.com/).",
        "", "**My read:** opinion stays.", "",
    ])
    path = os.path.join(d, "draft-india.md")
    write_text(path, draft + "\n")
    out = build_claims(WEEK, "india")
    ok("claims.count", len(out["claims"]) == 3, f"{len(out['claims'])} claims")
    write_json(os.path.join(d, "factcheck-india.json"), {"verdicts": [
        {"n": 1, "verdict": "fix", "replacement": "First claim is corrected [Example](https://example.com/)."},
        {"n": 2, "verdict": "pass"}, {"n": 3, "verdict": "reject", "reason": "not supported"}]})
    s = apply_factcheck(WEEK, "india")
    text = read_text(path)
    ok("claims.apply", "corrected" in text and "Third claim" not in text and "Second claim is fine" in text
       and "items_dropped: 1" in text and "opinion stays" in text, json.dumps(s)[:120])


def test_links():
    from links import check_url
    st, verdict, note = check_url("https://github.com/j-jain/Ai-news/this-page-does-not-exist-selftest")
    if st == 0:
        skip("links.dead", f"network: {note}")
        return
    ok("links.dead", verdict == "dead", f"status={st} verdict={verdict}")


def run(args):
    d = work_dir(WEEK)
    try:
        test_week()
        test_urls()
        test_normalize()
        tq = test_fetch_and_quotes()
        test_lint(tq)
        test_claims_apply()
        test_links()
    finally:
        shutil.rmtree(d, ignore_errors=True)
    width = max(len(n) for n, _, _ in RESULTS)
    for name, status, note in RESULTS:
        print(f"{status:<4} {name:<{width}}  {note}")
    fails = [r for r in RESULTS if r[1] == "FAIL"]
    print(json.dumps({"pass": sum(1 for r in RESULTS if r[1] == 'PASS'), "fail": len(fails),
                      "skip": sum(1 for r in RESULTS if r[1] == 'SKIP')}))
    return 1 if fails else 0
