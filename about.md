---
layout: default
title: About
permalink: /about/
---
# About

**Ai-news** is a personal weekly on artificial intelligence, written for one reader: a computer-science undergraduate in India who builds things, hunts for internships, and wants to know what actually happened this week without the hype.

Two editions come out every Monday:

- **India + Opportunities** — Sarvam and the Indian labs; government, compute and policy; startups and money; AI showing up in real Indian businesses; and a running list of internships, fellowships, campus programmes and competitions with their deadlines.
- **World** — the frontier labs; open-weight and local models (and what runs on an 8, 16, 24 or 32 GB machine); RAM, GPU and laptop prices; people and money; research, policy and safety; new ways to use AI; and white space worth building in.

## How it is made, and why you can trust the links

Each issue is produced by a scripted run of Claude Code, with one rule above all others: **a sentence may only state a fact if the page that says it was saved during the run and the supporting quote was found in that saved text.**

1. Eight research agents, one per beat, search the week and fetch candidate pages. The fetcher stores the page text locally and records its publication date.
2. A script checks that every candidate's supporting quote is really present in the saved page. Anything that fails is dropped and logged.
3. A writing agent drafts the edition using only the verified items. Every factual sentence carries a small link, like this: [Example](https://example.com). The link points at the page the sentence came from.
4. A separate fact-checking agent reads every sentence against its saved page and marks it pass, fix or reject. Sentences that cannot be fixed are deleted.
5. A linter enforces the rules mechanically: every paragraph has a link, every link is one of the verified pages, no banned hype words, length within four to five pages.
6. Every link is checked to resolve, and the issue is published. The per-week logs (`verified.json`, `factcheck-*.json`, `dropped.json`) are committed to the repo so anyone can audit a week.

Opinion is allowed and clearly marked: paragraphs beginning **My read:** are the newsletter's take and introduce no new facts.

What is not covered: anything that could not be fetched (posts on X, paywalled articles without a free primary source) is left out, and the footer of each issue says what was dropped and why.

Code and logs: [github.com/j-jain/Ai-news]({{ site.github_repo }}). Text is CC BY 4.0, code is MIT.
