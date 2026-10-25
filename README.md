# Ai-news

Two short, verified reads on AI every week, written for Jai by a scripted Claude Code run and published with GitHub Pages at **https://j-jain.github.io/Ai-news/**.

- **India + Opportunities** - Sarvam and the Indian labs; government, compute and policy; startups and money; AI in real Indian businesses; internships, fellowships, campus programmes and hackathons with deadlines; ideas for India.
- **World** - frontier labs; open-weight and local models (what runs in 8/16/24/32 GB); RAM, GPU and laptop prices; people and money (Karpathy, Musk, Sequoia, YC, a16z); research; policy and safety; new ways to use AI; white space.

The one rule: **a sentence may state a fact only if the page that says it was saved during the run and its supporting quote was found in that saved text.** Every factual sentence carries a chip that opens that page.

## How a run works

```
/ai-news                      both editions for the current window
/ai-news india                one edition
/ai-news world --dry-run      research + draft + checks, no publish
/ai-news both --week 2026-W43 an explicit ISO week
```

1. `ainews week` picks the week and window (the days since the last issue; refuses to run if fewer than 5).
2. Eight researcher agents (Sonnet), one per beat, search the week and **fetch** every candidate page with `ainews fetch`, which saves the page text and its publication date. Each item carries a verbatim quote (25 words or fewer).
3. `ainews select` keeps only items whose quote a script finds in the saved page, whose date is inside the window, and which were not covered before -> `work/<week>/verified.json` (+ `dropped.json` with reasons).
4. Two writer agents (Opus) write the editions from `verified.json` only, following `references/style.md`, then `ainews lint` enforces the mechanics (every paragraph linked, every link verified, chip inside the sentence, no banned words, 1,400-2,300 words, three Tier-A things up top).
5. `ainews claims` pairs every sentence with its evidence; two fact-checker agents (Opus) return pass / fix / reject per sentence; `ainews apply-factcheck` applies them, twice at most, then strips anything still unsupported.
6. `ainews links` HTTP-checks every link (404/410 removes the sentence), `ainews opportunities --merge` updates the living opportunities table, and `ainews publish` moves the drafts into `_issues/`, commits, pushes `main` and polls the Pages build.

The per-week logs (`verified.json`, `factcheck-*.json`, `dropped.json`, `links-*.json`, `fetch-log.jsonl`) are committed under `work/<week>/` so any issue can be audited; the saved page texts are not (`work/*/pages/` is git-ignored).

## Layout

```
_config.yml, _layouts/, _includes/, assets/   the Jekyll site (built by GitHub Pages; nothing to build locally)
index.html, opportunities.md, about.md        pages
_issues/<week>-<edition>.md                   one Markdown file per edition per week
_data/opportunities.json                      the living table of open opportunities (deadline, link, last checked)
state/seen.json, state/last-run.json          what has been covered; the last window
work/<week>/                                  one folder per run (pages/ is local only)
scripts/ainews.py + scripts/ainews_lib/       the command behind everything (standard-library Python 3.10+)
.claude/skills/ai-news/SKILL.md               the run card the orchestrator follows
.claude/skills/ai-news/references/            beats/<beat>.md (seeds + queries), style.md, verification.md
.claude/skills/ai-news/assets/                skeleton-india.md, skeleton-world.md
.claude/agents/                               ai-news-researcher, ai-news-writer, ai-news-factchecker
```

## The command

Always this one spelling (so the permission rule matches), from any folder:

```bash
python -I "C:/Users/Jaidityaa Jain/OneDrive/Desktop/Ai-news/scripts/ainews.py" selftest
```

Sub-commands: `week`, `fetch`, `verify-quotes`, `select`, `claims`, `apply-factcheck`, `lint`, `links`, `opportunities --pull|--merge|--check`, `publish`, `selftest`. `--help` on any of them.

## Fixing an issue after it is live

Say "fix X in this week's World issue" to the skill, or by hand:

1. Edit `_issues/<week>-<edition>.md` (new facts need a fetched page and an item in `work/<week>/verified.json`).
2. `ainews lint --path _issues/<week>-<edition>.md --verified work/<week>/verified.json` must print `"errors": 0`.
3. `ainews publish --week <week> --no-issues --message "Fix ..."`.

## Changing what gets covered

- Beats, seed URLs and queries: `.claude/skills/ai-news/references/beats/<beat>.md`.
- Voice, sections, word budgets, banned words: `references/style.md` and `scripts/banned-phrases.txt`.
- Caps and windows: `scripts/ainews_lib/selectcmd.py` (22 India / 26 World items) and `weekcmd.py` (5-day minimum, 14-day maximum).
- Job boards polled for internships: `scripts/ainews_lib/opps.py` (`BOARDS`).

## The weekly schedule

A desktop-app scheduled task named `ai-news-weekly` runs the skill every Monday at 08:00 (local time) while the Claude app is open; if the app was closed, it runs on the next launch. It covers the seven days ending Sunday. Pause it from the app's scheduled-tasks list.

## Licence

Code: MIT. Issue text: CC BY 4.0. Quoted passages belong to their publishers.
