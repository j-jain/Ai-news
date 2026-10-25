"""Argument parsing and dispatch for the ainews command."""
import argparse


def build_parser():
    ap = argparse.ArgumentParser(prog="ainews", description="The one command behind the /ai-news skill.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("week", help="compute week id + window, write work/<week>/meta.json")
    s.add_argument("--week", help="explicit ISO week, e.g. 2026-W43 (window = Mon..min(Sun, today))")
    s.add_argument("--since", help="explicit window start YYYY-MM-DD")
    s.add_argument("--editions", default="both", choices=["both", "india", "world"])
    s.add_argument("--dry-run", action="store_true")
    s.add_argument("--force", action="store_true", help="run even if fewer than 5 new days")

    s = sub.add_parser("fetch", help="fetch a URL and save its text under work/<week>/pages/")
    s.add_argument("--week", required=True)
    s.add_argument("--url", required=True)
    s.add_argument("--tier", default="A", choices=["A", "B"], help="B registers text that WebFetch returned (--text-file)")
    s.add_argument("--text-file", help="tier B: file holding the verbatim text WebFetch returned")
    s.add_argument("--published", help="YYYY-MM-DD, used only if --published-evidence is found in the page text")
    s.add_argument("--published-evidence", help="verbatim snippet from the page that shows the date")
    s.add_argument("--force", action="store_true", help="re-fetch even if already saved")
    s.add_argument("--head", type=int, default=1500, help="characters of text to print (default 1500)")
    s.add_argument("--full", action="store_true", help="print the whole text")
    s.add_argument("--quiet", action="store_true", help="print only the JSON summary")

    s = sub.add_parser("verify-quotes", help="check every candidate's quote against its saved page")
    s.add_argument("--week", required=True)
    s.add_argument("--file", required=True, help="path to candidates-<beat>.json")

    s = sub.add_parser("select", help="merge candidates into verified.json / dropped.json")
    s.add_argument("--week", required=True)

    s = sub.add_parser("claims", help="pair every sentence of a draft with its evidence -> claims-<edition>.json")
    s.add_argument("--week", required=True)
    s.add_argument("--edition", required=True, choices=["india", "world"])

    s = sub.add_parser("apply-factcheck", help="apply factcheck-<edition>.json verdicts to the draft")
    s.add_argument("--week", required=True)
    s.add_argument("--edition", required=True, choices=["india", "world"])
    s.add_argument("--strip", action="store_true", help="delete every sentence that is not a pass")
    s.add_argument("--verdicts", help="alternative verdicts file")

    s = sub.add_parser("lint", help="mechanical checks on a draft")
    s.add_argument("--week")
    s.add_argument("--edition", choices=["india", "world"])
    s.add_argument("--path", help="lint an arbitrary file instead of work/<week>/draft-<edition>.md")
    s.add_argument("--verified", help="verified.json to whitelist URLs against")
    s.add_argument("--fix", action="store_true", help="join wrapped lines and escape Liquid braces in place")

    s = sub.add_parser("links", help="HTTP-check every link in a draft")
    s.add_argument("--week", required=True)
    s.add_argument("--edition", required=True, choices=["india", "world"])
    s.add_argument("--strip", action="store_true", help="remove sentences whose link is dead (404/410)")
    s.add_argument("--recheck", action="store_true", help="re-check links that were fetched fine this run")

    s = sub.add_parser("opportunities", help="--pull job boards | --merge verified rows | --check existing rows")
    s.add_argument("--week")
    g = s.add_mutually_exclusive_group(required=True)
    g.add_argument("--pull", action="store_true")
    g.add_argument("--merge", action="store_true")
    g.add_argument("--check", action="store_true")

    s = sub.add_parser("publish", help="copy drafts to _issues/, update state, commit, push, poll Pages")
    s.add_argument("--week", required=True)
    s.add_argument("--editions", default="both", choices=["both", "india", "world"])
    s.add_argument("--dry-run", action="store_true", help="write work/<week>/preview/ only; no git")
    s.add_argument("--ensure-pages", action="store_true", help="create the GitHub Pages site if it does not exist")
    s.add_argument("--no-issues", action="store_true", help="commit and push the repo without touching _issues/")
    s.add_argument("--force", action="store_true", help="publish even if lint-<edition>.json has errors")
    s.add_argument("--message", help="commit message")
    s.add_argument("--trailer", help="text appended to the commit message (e.g. a Co-Authored-By line)")
    s.add_argument("--poll-timeout", type=int, default=360)

    sub.add_parser("selftest", help="exercise the pieces on a scratch week")
    return ap


def main(argv):
    args = build_parser().parse_args(argv)
    if args.cmd == "week":
        import weekcmd
        return weekcmd.run(args)
    if args.cmd == "fetch":
        import fetch
        return fetch.run(args)
    if args.cmd == "verify-quotes":
        import quotes
        return quotes.run(args)
    if args.cmd == "select":
        import selectcmd
        return selectcmd.run(args)
    if args.cmd == "claims":
        import claims
        return claims.run_claims(args)
    if args.cmd == "apply-factcheck":
        import claims
        return claims.run_apply(args)
    if args.cmd == "lint":
        import lint
        return lint.run(args)
    if args.cmd == "links":
        import links
        return links.run(args)
    if args.cmd == "opportunities":
        import opps
        return opps.run(args)
    if args.cmd == "publish":
        import publish
        return publish.run(args)
    if args.cmd == "selftest":
        import selftest
        return selftest.run(args)
    return 2
