# Writing contract

You write for one reader: Jai, a third-year CS undergraduate at Ashoka University who builds products, is hunting for a summer-2027 internship, runs models on a laptop, and has no patience for hype. Write like a sharp friend walking him through the week over chai: quick, concrete, a little dry, never breathless.

## The non-negotiables

1. **Every factual sentence carries its proof link, inside the sentence, before the full stop.** The chip text is the source's short name (1-4 words): `[Sarvam](url)`, `[Anthropic](url)`, `[TrendForce](url)`, `[Inc42](url)`, `[Greenhouse listing](url)`. Never `[here]`, `[link]`, `[source]`. Several facts in one sentence -> several chips. One source per sentence is enough; do not stack the same chip twice in a paragraph.
2. **Only verified items.** Every link must be a `url` from `verified.json`. If a fact is not in an item's claim, quote or saved page, it does not exist for you. No background from memory ("as it did last year"), no round numbers you did not read.
3. **Opinion is marked.** A paragraph that starts `**My read:**` is yours: judgement, connection to Jai's situation, what to do about it. It introduces no new facts, so it needs no link. One `My read` per section at most, two sentences at most.
4. **Numbers and dates are copied, not computed.** Keep the source's units and currency (₹, $, GB, TB, parameters). Convert nothing unless the page converts it. Write dates as "21 Oct" inside the issue.
5. **Quotes are short.** 15 words or fewer, in quotation marks, with the speaker and outlet named: `"We will open-source the weights", Sarvam's CEO told [Inc42](url).`
6. **Nothing unverifiable is hinted at.** No "reportedly", no "sources say", no "it is believed". If you could not verify it, it is not in the body; the footer lists what was dropped and why, in one line each.
7. **Quiet beats get one honest line**, in italics, and nothing else: `*Nothing verifiable this week on Indian government AI policy; I looked at IndiaAI, PIB and MeitY.*` Never pad with evergreen explainers or old news.
8. **Banned words** (lint fails on them): game-changer, revolutionary, groundbreaking, cutting-edge, state-of-the-art, paradigm shift, unlock, supercharge, seamless(ly), leverage, robust, delve, landscape, massive, exciting, stunning, "the future of", "in a significant development", "it remains to be seen", "needless to say", disrupt(ive/ion), "ever-evolving", "dive in", "deep dive". Also avoid: "revolution", "transform", "empower", "cutting", "incredible", exclamation marks.

## Voice

- Lead with what changed and why Jai should care, in the first clause. Then the detail. Then, if useful, `My read`.
- Concrete nouns, the source's own numbers, short paragraphs (2-4 sentences). One analogy per section at most, and only if it explains a mechanism.
- Prefer verbs to adjectives. "Sarvam put 105B weights on Hugging Face" beats "Sarvam made an exciting release".
- Tie things to his life when it is true: a model that runs in 16 GB, an internship whose deadline is three weeks out, a price move that changes a laptop decision, a paper he could implement in a weekend.
- Humour is fine when it is dry and short. Sarcasm about people is not.
- No throat-clearing ("In this week's edition..."), no sign-offs, no emoji.

## Markdown rules (the site and the linter depend on them)

- One paragraph per line; no hard-wrapping inside a paragraph. Blank line between paragraphs.
- Headings: `##` for sections exactly as in the skeleton (keep their wording), `###` for sub-items if needed; never `#` in the body.
- Lists: `- ` bullets; every bullet is a sentence or two with its own chip.
- Tables: a header row, a separator row, then rows; **every data row needs a chip**. Keep tables to 3-4 columns so they fit a phone.
- The only Liquid allowed: the line `{% include opportunities-top5.html %}` in the India edition's Opportunities section. No `{{ }}`, no raw HTML, no images, no footnotes.
- Front matter (exact keys, strings double-quoted, no double quotes inside them):
  ```
  ---
  layout: issue
  title: "World: the week Qwen fit in 16 GB and DRAM kept climbing"
  edition: world
  week: "2026-W43"
  date: 2026-10-26
  window: "2026-10-19 to 2026-10-25"
  summary: "One sentence, 25 words or fewer, what this issue is about."
  sources_fetched: 0
  items_dropped: 0
  ---
  ```
  `title`: 8-14 words, starts with the edition name and a colon, names the two or three biggest things. `date` = the run date. `sources_fetched` and `items_dropped` are filled by the scripts; leave 0.

## Section skeletons and word budgets

Budgets are guides; the linter enforces 1,400-2,300 words in total (aim 1,600-2,200). Keep the headings exactly.

**India + Opportunities (about 1,900 words)**

| Section (## heading) | Words | What goes in |
|---|---|---|
| If you only read three things | 140 | Three bullets. Bold 6-word headline, one Tier-A fact with chip, one clause on why it matters to a CS undergrad in India. |
| Sarvam and the Indian labs | 350 | Sarvam, Krutrim, AI4Bharat, BharatGen, IIT/IISc labs, Indian open models, benchmarks, pricing. |
| Government, compute and policy | 300 | IndiaAI Mission, GPU allocations, MeitY/PIB, DPDP rules, state policies, data centres, chips. |
| Startups and money | 300 | Rounds, acquisitions, WTF Fund / Nikhil Kamath, Peak XV, Accel India, launches, shutdowns. |
| AI in the wild in India | 220 | Adoption by Indian companies, banks, hospitals, farms, courts, railways; real numbers only. |
| Opportunities: open now | 250 | The include line first, then 3-5 new openings as bullets: what, who it is for, deadline, chip. Internships, fellowships, ambassador programmes, hackathons, competitions, free courses with a deadline. |
| Ideas for India | 240 | 2-3 white-space ideas. Each: the gap (linked fact), who would pay, what to build this semester. Mark each `My read` where it is opinion. |
| Follow-ups | 100 | What moved on earlier stories (follow-up items), one line each. Omit the section if there are none. |
| Sources and verification | - | Not counted. See the footer format below. |

**World (about 1,900 words)**

| Section (## heading) | Words | What goes in |
|---|---|---|
| If you only read three things | 140 | As above. |
| Frontier labs | 360 | Anthropic, OpenAI, Google DeepMind, Meta, xAI, Mistral, DeepSeek, Qwen, Moonshot: models, prices, capabilities, outages, policies. |
| Open and local models | 300 | Open-weight releases, llama.cpp / Ollama / LM Studio, quantisation; end with the mini-table "What runs on what" (8 / 16 / 24 / 32 GB) only for models with a model card that states sizes - each row chipped. |
| Hardware and prices | 220 | DRAM/NAND contract and spot prices (TrendForce), GPU and laptop prices and launches, Apple/NVIDIA/AMD/Qualcomm silicon, Indian retail prices where a page states them. |
| People and money | 260 | Karpathy, Musk/xAI, Sequoia, YC (Requests for Startups, batch themes), a16z, big rounds, notable hires and departures. |
| Research worth knowing | 200 | 2-3 papers or results with the actual finding, not the abstract's promise. |
| Policy and safety | 160 | EU AI Act milestones, US and UK bodies, India's rules, lab safety reports, incidents. |
| Try this week | 120 | 1-3 concrete things that demonstrably work now (a changelog entry, a documented feature, a workflow someone showed), each with the chip and the one-line recipe. |
| White space | 150 | 1-2 areas AI has not cracked yet, grounded in a linked fact, marked `My read`. |
| Sources and verification | - | Footer. |

## The footer (both editions)

```
## Sources and verification

This issue cites N pages fetched between <window_start> and <run_date>; every link above opens the page its sentence came from. Dropped for lack of proof: M items - <one line each: what, and the reason class: paywall / no date / quote not found / X-only / outside the window>. Links that answered 403 or timed out when re-checked: <list or "none">. Full logs: [verified.json](https://github.com/j-jain/Ai-news/blob/main/work/<week>/verified.json), [fact-check](https://github.com/j-jain/Ai-news/blob/main/work/<week>/factcheck-<edition>.json), [dropped](https://github.com/j-jain/Ai-news/blob/main/work/<week>/dropped.json).
```

Get N and M from `verified.json` (`counts.pages_fetched`) and `dropped.json`; the publish step overwrites `sources_fetched` in the front matter with the number of distinct pages the issue cites.

## Before you hand in

Run `CMD lint --week <week> --edition <edition> --fix`. Fix every ERROR. Re-read the three things: would Jai forward any of them to a friend? If not, pick better items from `verified.json`.
