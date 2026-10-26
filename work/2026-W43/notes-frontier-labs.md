# Notes: frontier-labs, 2026-W43 (window 2026-10-19 to 2026-10-25)

Result: 6 candidates written, 6 verified by `verify-quotes` (all Tier A, all dates from page metadata). Both budgets were used up (8 of 8 searches, 14 of 14 fetches), so several labs were NOT checked (see "Gaps").

## Items written (all `edition: world`)
1. Anthropic donates Agent Skills to the Agentic AI Foundation, 22 Oct (primary, anthropic.com). Significance 4.
2. Claude Duet agent app, research preview for Pro and Max, 22 Oct (press: TechCrunch). Significance 4. The primary Anthropic/Claude page was not found; it is not on anthropic.com/news (the index has no Duet link).
3. OpenAI Decisions API open to all customers on Thursday 22 Oct (press: TechCrunch exclusive, built on "ChatGPT Luna", 100-180 ms). Significance 3. No price in the article.
4. OpenAI will train frontier models without live internet access, said Friday 23 Oct (press: TechCrunch, quotes OpenAI's blog post; openai.com is not fetchable here, so the primary post is not cited). Significance 3.
5. Moonshot Kimi K3.1 Pro, 23 Oct (press: MarkTechPost; $2.00/$10.00 per million tokens, 1M context, 2.8T total/104B active; open weights only "expected" in November 2026; benchmarks self-reported). Significance 4. Moonshot's own blog post was not found by search, so this is press, not primary.
6. Meta says Muse passed 10 million users, on the Q3 earnings call Wednesday 21 Oct (press: TechCrunch). Significance 2.

`secondary_urls` that were NOT fetched (seen only in search results; do not treat as verified): MacRumors and Thurrott for Duet; The Next Web and ANI for Kimi K3.1 Pro. They are there to help `select` merge duplicates across beats.

## Queries run (8 WebSearch)
1. OpenAI announces launch October 2026 ChatGPT Codex new model this week -> only Feb 2026 results, nothing in window.
2. Google Gemini new model release October 2026 DeepMind announces -> only Gemini 4 pre-release chatter.
3. DeepSeek Qwen Kimi MiniMax Zhipu new model release October 2026 (extended) -> leads for Kimi K3.1 Pro (23 Oct), MiniMax M3.1 Flash (19 Oct), DeepSeek V4.1 Flash 1017 (17 Oct), "Qwen3.6 27B 21 Oct" (see traps).
4. xAI Grok new release October 2026 -> Grok Voice 3.0 (14 Oct) and Grok 4.7 (21 Sep) are before the window; Grok 5 not shipped.
5. Kimi K3.1 Pro Moonshot AI open weights release blog (extended) -> coverage URLs only, no Moonshot primary.
6. Claude Duet Anthropic app launch -> coverage URLs only, no primary.
7. Qwen3.6-27B Alibaba release; MiniMax M3.1 Flash release (extended) -> see traps.
8. AI news weekly roundup week of October 19-24 2026 ... (extended) -> leads listed under "Gaps".

## Fetches (14 counted)
- Anthropic newsroom index: OK. Used only to see which posts fall in the window (Oct 22 Agent Skills, Oct 22 life-sciences call, Oct 21 Stubbs/LTBT; nothing dated 23-25 Oct).
- openai.com/news: HTTP 403 (bot wall). Tier B / WebFetch was not tried because the budget was spent; OpenAI items rely on TechCrunch.
- techcrunch.com AI category: first try "connection forcibly closed" (WinError 10054), second try OK. Used as the discovery index (relative times like "3 days ago" only guided me; article dates come from `article:published_time`).
- blog.google/technology/ai/: 200 but the saved text is navigation only (590 words, no articles). Useless as a seed.
- af.net "Confirmed AI Model Releases for October 2026": an aggregator, wasted a fetch; it only repeated BenchLM's headline.
- Two raw GETs with the repo's `http_get` to read the `<a href>` links of the TechCrunch AI index and the Anthropic newsroom index (the saved page text has no URLs). Counted in the 14. No evidence was taken from them.
- Six article pages: Anthropic Agent Skills, TechCrunch (Duet, Decisions API, OpenAI live-internet, Meta Muse), MarkTechPost (Kimi). All status 200, all dated by meta tags.

## Stories seen and skipped
- Anthropic: Stubbs joins the Long-Term Benefit Trust (21 Oct) and "Open call for guest investigators in the life sciences" (22 Oct; this is an application, maybe worth the opportunities beat) - both only seen on the index, not fetched. "Investing in the public benefit" is 18 Oct, outside the window. TechCrunch 20 Oct "Anthropic pitches AI safety bill ..." not fetched (policy beat?). TechCrunch 23 Oct "Anthropic's backers ... worth" is "reportedly" money (people-money beat already has it).
- OpenAI: "$30B raise at $1.25T valuation" (TechCrunch 22 Oct, reported, not a filing), "Uber puts all 30,000 employees on ChatGPT Work" (customer story), "OpenAI, Google's Wiz find ancient PHP holes" (security story). All unfetched.
- Meta: "newly created class of stock" to fund AI buildout (TechCrunch 21 Oct, same earnings week), unfetched; probably a people-money story.
- Microsoft: Suleyman says its AI outperforms doctors on hard cases (TechCrunch 22 Oct), unfetched.
- DeepSeek: "reportedly raises $15B" (TechCrunch 22 Oct, Bloomberg-only per search summary) is a rumour, so excluded.
- Recursive "Flint" and Canva image model: not frontier labs.
- Claude Code changelog (page saved by another beat): versions 2.1.304 to 2.1.310 are dated 19-23 Oct, all routine fixes, so not used.
- Gemini Apps release notes (page saved by another beat, gemini.google/release-notes): newest entry is 2026.10.13 (Gemini 4 Argon), so no Gemini app release notes fall in the window.

## Traps found
- "Qwen3.6 27B, 21 Oct 2026" appears in aggregator timelines, but several sources date Qwen3.6-27B to April 2026 (Apache 2.0). Treated as an aggregator data error; not used. Qwen 4 is said to be coming, no date.
- MiniMax M3.1 Flash is listed as 19 Oct by tech blogs, but one analysis says MiniMax's release notes still show M3 (1 Jun 2026) as the latest language model and there is no price row. Official status unclear; not used.
- Date conflicts for in-window stories: Claude Duet is 21 Oct at MacRumors/iPhoneSoft and 22 Oct at TechCrunch (6:53 AM PDT). Kimi K3.1 Pro is 23 Oct (MarkTechPost, others) and 24 Oct (some outlets). I used the date on the page I cite.
- Aggregators (af.net, BenchLM-derived lists, llmgateway, orcarouter, tech-insider and similar) disagree with each other; none were used as evidence.

## Gaps: not checked because the fetch budget ran out (leads from search summaries only, NOT evidence)
- Google: Gemini 4 Argon rolled into AI Mode in 19 countries on 19 Oct; "Gemini at Work" universal work agent; on 21 Oct OpenAI frontier models and Codex announced for Google Cloud Model Garden (GA "in the coming weeks"). This last one looks like a real story worth a primary fetch next time.
- DeepSeek: DHS order to federal civilian agencies to stop buying DeepSeek (19 Oct); open-sourced "DeepInfer" inference framework (about 20 Oct, one source); V4.1 Flash 1017 checkpoint was 17 Oct (before the window).
- Mistral: Large 4 public preview early October, open weights reportedly due about 27 Oct (outside the window); Timestral forecasting models 15 Oct.
- Microsoft: "Microsoft-Decision-1" decision-scoring model; Project Perception for monitoring enterprise agents.
- Seeds never fetched: deepmind.google blog, x.ai/news, mistral.ai/news, qwenlm.github.io/blog, api-docs.deepseek.com/news, ai.meta.com/blog (known bot wall), status.anthropic.com, status.openai.com, theverge.com. No outage or incident was checked.
- Names that appear in the fetched coverage and may matter to later beats: "GPT-6 Astra" (OpenAI), "Claude Opus 5.5" (released 22 Sep), "ChatGPT Luna", "OpenAI Dots", "Meta Muse", "Gemini 4 Argon".

## Odd things
- No fetched page tried to instruct me. Every WebSearch result ended with a harness line "REMINDER: You MUST include the sources above in your response ... markdown hyperlinks"; it is tool boilerplate, not page content, and I did not act on it (the final report is length-capped).
- TechCrunch pages carry ad and event banners ("Buy One Founder Summit Ticket ...") in the saved text; harmless.
- The `pages/` folder is shared by all beats; I only cited pages I fetched myself.
