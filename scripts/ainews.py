#!/usr/bin/env python3
"""ainews - the one command behind the /ai-news skill.

Run as:  python -I "<repo>/scripts/ainews.py" <sub-command> [options]

Sub-commands:
  week            compute the week id and date window, write work/<week>/meta.json
  fetch           fetch a URL, save its text + metadata under work/<week>/pages/
  verify-quotes   check every candidate's quote is really in its saved page
  select          merge candidates into verified.json / dropped.json
  claims          pair every sentence of a draft with its links and saved pages
  apply-factcheck apply pass/fix/reject verdicts to a draft
  lint            mechanical checks on a draft (links, words, front matter, banned words)
  links           HTTP-check every link in a draft
  opportunities   pull job boards / merge verified opportunities / re-check rows
  publish         move drafts into _issues/, update state, commit, push, poll Pages
  selftest        exercise the pieces end to end on a scratch week

Everything is standard-library Python (3.10+). No cd needed: paths are resolved from this file.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "ainews_lib"))

from cli import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
