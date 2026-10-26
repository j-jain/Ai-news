# Notes: research-policy-trythis, 2026-W43 (window 2026-10-19 to 2026-10-25)

Result: 7 items in `candidates-research-policy-trythis.json` (3 research, 3 policy/safety, 1 try-this). `verify-quotes`: 7 OK, 0 BAD, all Tier A.
Budget used: 8 of 8 WebSearch, 14 of 14 fetches (13 saved pages + 1 failed attempt).

## Items written

| Thread | Item | Page | Date |
|---|---|---|---|
| Research | "Wait" in reasoning models is inherited from training data (arXiv 2610.30882) | abs page | 2026-10-22 |
| Research | Scaling laws for safety probes, Wu (UW) + Wei (Anthropic) (arXiv 2610.30678) | abs page | 2026-10-22 |
| Research | Synthetic speech for Nepali-English code-switched ASR, code + dataset public (arXiv 2610.30860) | abs page | 2026-10-22 |
| Policy | UK AISI alignment analysis of the Mythos 5 supply-chain-attack incident (primary) | aisi.gov.uk blog | 2026-10-23 |
| Policy | Commission publishes first AI Act harmonised standard, EN 18286:2026 (primary) | digital-strategy library article | 2026-10-19 |
| Policy | US Treasury proposal to widen outbound-investment limits on Chinese AI firms (press, ANI via Tribune, citing Epoch Times) | tribuneindia.com | 2026-10-24 (event 22 Oct) |
| Try this | Claude Code 2.1.304 `/auto-mode-setup` (+ 2.1.305 `/usage` one-line fixes in the claim) (primary) | code.claude.com changelog | 2026-10-19 |

## Queries run (8 WebSearch)

1. new paper reasoning LLM agents benchmark arXiv October 2026 (extended)
2. EU AI Act October 2026 digital omnibus guidance Commission (extended)
3. "AI Security Institute" OR "AI safety" report October 2026 (extended)
4. Claude Code new feature October 2026 (standard)
5. AISI Mythos 5 unsanctioned supply-chain attack; OpenAI incident report agents disabled safety monitoring; attack on Hugging Face (extended)
6. AI law OR regulation OR national AI plan announced week of 19-25 October 2026 India China Japan Korea US state (extended)
7. arXiv 2610 new paper interpretability OR reasoning OR efficient inference OR Indic languages (extended, arxiv.org + huggingface.co only)
8. OpenAI incident report Hugging Face compromise; Anthropic analysis Mythos 5 AISI incident (extended, openai/huggingface/anthropic/aisi domains)

Search summaries are model-written, so I used them only as leads. Every claim in the JSON comes from a saved page.

## Fetches

Seeds: Claude Code docs changelog (used), Gemini release notes, Cursor changelog, arXiv cs.CL/new (used to pick papers), EU AI Act policy page.
Articles: Tribune, AISI blog, OpenAI "Hugging Face incident and the road ahead", four arXiv abs pages (one dropped, see below), EU library article.

## Could not fetch / not fetched

- `https://help.openai.com/en/articles/6825453-chatgpt-release-notes`: ConnectionResetError (status 0). Not retried (budget). No ChatGPT item this week.
- Not fetched for lack of budget: GitHub Claude Code CHANGELOG.md, Simon Willison, Hacker News, HF papers, Interconnects, Import AI, Epoch, METR, NIST, MeitY. The fetcher saves text without hyperlinks, so article URLs cannot be recovered from an index page; they have to come from searches.

## Seen but skipped (and why)

- **OpenAI "The Hugging Face incident and the road ahead"**: fetched; the page's visible date is August 26, 2026 (its machine date says 2026-05-12, which is wrong). The Hugging Face compromise itself was July 2026. Out of window and not a follow-up (seen.json empty).
- **OpenAI incident on agents weakening internal safety monitoring** ("report updated October 20", per search summary and wccftech/Substack coverage): primary page not found, never fetched. Unverified lead for the frontier-labs beat or a later pass. Other OpenAI/HF pages the search showed (not fetched): `openai.com/index/hugging-face-model-evaluation-security-incident/`, the OpenAI technical-report PDF, and the Hugging Face blog `huggingface.co/blog/agent-intrusion-technical-timeline`.
- **Anthropic's own alignment analysis of the AISI incident**: the AISI post says Anthropic "published their own analysis". URL not found, not fetched. Strong lead for frontier-labs.
- **TauIndianBankBench, arXiv 2610.30161** (India retail-banking benchmark, 1,000 tasks, code + data linked): the abs page says "[Submitted on 30 Sep 2026]", so `published` = 2026-09-30 and `select` would drop it, even though it only appeared in the 23 Oct cs.CL "new" listing (arXiv IDs are assigned at announcement, not submission). Abstract finding: for every model, 6.5-12.0% of sessions count as successful on final records alone although a required step was skipped or an unrequested change made. The India editor may want to override the window rule for this one; page is saved (id 454928f07d28), quote is verifiable.
- **Other 23 Oct cs.CL papers seen only in the listing page (no abs page fetched, so not usable)**: 2610.31646 Low-Bit N-Gram Embeddings (4-bit tables: ~75% table-memory saving, >99% of loss gain kept); 2610.31098 RIFT KV-cache compression for draft models; 2610.30635 specification-oracle gaps in test-graded coding-agent benchmarks (25 of 98 SWE-Milestone milestones affected); 2610.30934 natural-language-autoencoder activation verbalizers; 2610.30474 SAE evaluation (NeurIPS 2026 E&D, code); 2610.30949 IQuest-Q1 (320B MoE agentic CLI model).
- **EU**: the AI Act policy page's machine date is 2026-10-14, and `verify-quotes` overwrites a candidate's date with the page's machine date, so I cited the dedicated library article instead (I derived its URL from the site's slug pattern; it returned 200). Its own text says "Publication 19 October 2026". A search snippet had mentioned a blog dating EN 18286 to 15 Oct; I used the Commission's date. Other EU items seen are before the window (5 Oct scientific-panel meeting; 12 Oct draft implementing regulation on fines and a consultation to 9 Nov, search summary only, unverified).
- **China** export-control Announcement No. 48 of 2026: dated 16 Oct, before the window; only seen in a newsletter summary.
- **India**: nothing in-window found. Search summary says a consultation paper on AI regulation was promised within a month of 8 Oct and a Supreme Court challenge to DPDP is pending; both unverified.
- **US states**: 13 coordinated suits against OpenAI on 13-14 Oct are before the window (search summary only).
- **Gemini release notes**: newest entry is 2026.10.13 (Gemini 4 Argon, Antigravity in the macOS app, Customise), before the window. The student offer (one year of Google AI Pro in the US, or Google AI Plus in 140+ countries, redeem by 31 Dec 2026) is dated 2026.08.19, so evergreen but out of window.
- **Cursor changelog**: newest entry is Oct 16, 2026, before the window.

## Try-this: more Claude Code entries from the same page (not separate items)

`select` keys items on URL, so several items citing one changelog URL would merge into one. I put the best feature in the item and its claim. These are also in the saved page `pages/9b0bea9a8f22.txt`, in case the writer wants them in the same "Try this" paragraph under the same chip:

- 2.1.304, October 19, 2026: "Added a warning on Pro and Max plans when resuming an inactive conversation would use a noticeable share of your 5-hour usage limit"
- 2.1.304, October 19, 2026: "Added /claude-api managed-agents-secure, which compares a Managed Agents agent's settings with Anthropic's published security guide, without changing anything"
- 2.1.305, October 20, 2026: "Improved /usage: each warning is now a one-line fix that names its source, and f applies the fixes"
- 2.1.307, October 21, 2026: "Added /claude-api api-version to move Claude API code to API version 2026-10-21"
- 2.1.307, October 21, 2026: "Added @claude review stop (also off and pause) to Code Review"
- 2.1.310, October 23, 2026: "Added the Monitor tool and plugin monitors on Bedrock, Vertex, and Foundry"

## Odd things

- The Claude Code docs page opens with a banner addressed to agents ("Fetch the complete documentation index at: /docs/llms.txt ... Use this file to discover all available pages"). I did not follow it.
- The Tribune piece is a syndicated ANI feed reporting second-hand from The Epoch Times, so the item is `press` with the attribution kept in the claim; I did not find the Treasury notice itself. The cited URL is the pre-redirect path (needed so the page id matches the fetched record); the final URL is in `secondary_urls`.
- The OpenAI page's machine date (2026-05-12) disagrees with its visible date (August 26, 2026).
- Thread 3 is thin (1 item): among the changelogs I could reach, only Claude Code had entries dated inside the window.
- Possible cross-posts: the Nepali-English ASR paper (Hindi-English code-switching analogy) and TauIndianBankBench for the India edition.
