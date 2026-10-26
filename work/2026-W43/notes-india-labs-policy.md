# Notes: india-labs-policy, week 2026-W43 (window 2026-10-19 to 2026-10-25)

Result: 5 candidates written, 5 verified by script (`verify-quotes`: items 5, verified 5, failed 0). All five are Tier A (fetched with `CMD fetch`), all `source_type: press`, all `edition: india`. Budget used: 8 of 8 WebSearch, 14 of 14 fetches (13 `CMD fetch` + 1 WebFetch used only to read link URLs off the AIM homepage; nothing was registered as Tier B).

Thin week for this beat: nothing from the state side (MeitY / PIB / IndiaAI Mission / CERT-In) could be shown to fall inside 19-25 Oct. See "Gaps" below.

## Candidates written
1. Birla AI Labs Yug-1 time series foundation model, AIM, 19 Oct (sig 3). Page says it is on GitHub and Hugging Face; it does not say "open-weight" or give a licence, so I kept `edition: india`. An editor could promote it to `both` after checking the licence on the Hugging Face page (not fetched).
2. Chariot-1-ASR Realtime, AIM, 23 Oct, launch dated 22 Oct (sig 3). All accuracy numbers are Chariot's own tests (the page says so). The page never says where Chariot is based, so the claim does not call it an Indian lab.
3. ElevenLabs MoU with Karnataka Innovation and Technology Society (KITS) and Indian startups' pushback, AIM, 19 Oct (sig 2). The page says only that ElevenLabs "recently" signed the MoU, so the signing date is not evidenced; the claim is worded as "AIM reported on 19 Oct". It is a feature with quoted opinions, so kept at sig 2. Page also says Karnataka formed joint working groups with Anthropic earlier this year (not in the claim).
4. Utho Cloud NVIDIA B300 reservations for a planned Feb 2027 deployment, AIM, 19 Oct (sig 2). No price and no B300 count in the article (stated in the item).
5. Cortex DC (Chatterjee Group) 2 GW plan, Indian Infrastructure, 23 Oct (sig 2). Reads like a company release; no site, investment figure or customer named (stated in the item).

None of the items has a primary-source URL in `secondary_urls`: I did not have fetch budget for the company pages (Birla AI Labs GitHub/Hugging Face, Chariot, KITS/ElevenLabs, Utho, Cortex DC) and did not want to invent URLs.

## Queries run (WebSearch, all `extended`)
1. "Sarvam AI" October 2026
2. "IndiaAI Mission" October 2026 GPUs compute allocation
3. MeitY AI announcement Vaishnaw this week 21 October 2026 OR 22 October 2026 OR 23 October 2026
4. India LLM launch open-source model BharatGen OR Krutrim OR AI4Bharat OR Gnani OR Soket October 2026
5. India AI data centre announced gigawatt investment October 2026
6. DPDP rules AI India OR "IndiaAI Safety Institute" OR "AI governance" India October 2026
7. MeitY IndiaAI Mission artificial intelligence press release Posted On OCT 2026 (allowed domains: pib.gov.in, meity.gov.in, indiaai.gov.in, cert-in.org.in)
8. CERT-In advisory AI agents accessing Indian systems without authorisation voluntary disclosures AI model providers

## Fetches
Seeds: sarvam.ai/blogs (ok, see below), indiaai.gov.in/news (navigation only), analyticsindiamag.com (ok, used as the index), pib.gov.in/allRel.aspx (unusable), meity.gov.in (unusable).
WebFetch (not saved as evidence): analyticsindiamag.com homepage, prompt asked for article URLs for 14 headlines. I fetched 7 of the 14 URLs it returned (Chariot, NeuroDx, Birla, Gnani, NITI, Karnataka, Utho) and all 7 resolved with status 200; the other 7 were not tried. The Cortex DC URL came from a search result.
Articles (CMD fetch, Tier A): Chariot, NeuroDx, Birla, Gnani, NITI framework, Cortex DC, Karnataka-ElevenLabs, Utho Cloud.

## Could not fetch / unusable
- https://www.meity.gov.in/ : status 200 but 1 word, `thin: true` (JavaScript-rendered).
- https://www.pib.gov.in/allRel.aspx : the fetcher was redirected to the Hindi listing (`allRel.aspx?reg=48&lang=2`) and saved only navigation text, no releases. The English listing (`allRelease.aspx?reg=3&lang=1`) turned up in a search result but I had no fetch left to try it.
- https://indiaai.gov.in/news : saved navigation only (409 words, no article list, no dates).
- https://www.sarvam.ai/blogs : fetched (flagged thin because it is an index). Newest post is "Introducing Bulbul V4 Flash", 13 Oct 2026, before the window. Nothing from Sarvam inside the window on the blog.
- Not attempted for lack of budget: ai4bharat.iitm.ac.in, bharatgen.tech, economictimes.indiatimes.com/tech. Krutrim not attempted (the beat file says connection refused).

## Seen and skipped: fetched, but outside the window
- NITI Frontier Tech Hub data-centre evaluation framework for states: AIM article published 2026-10-15 (so the framework is out by 15 Oct). Indian Infrastructure's "Recent Posts" list shows its own NITI story dated 19 Oct, which looks like a late repeat. Not included.
- Gnani Timbre v3.0 text-to-speech model: AIM, 2026-10-14.
- NeuroDx "Sphota" architecture preview: AIM, 2026-10-16 (previewed at Cypher 2026 on 9 Oct; proprietary, release "later this year").
- Sarvam Bulbul V4 Flash (listed at AIM as Rs 20 per 10,000 characters): Sarvam blog dated 13 Oct. Not fetched, not in window.

## Seen only in search snippets or index pages, not fetched, so not verified (do not use without a fetch)
- CERT-In advisory on AI agents reaching Indian systems without authorisation (reported as "AI Agents as Attack Vectors", ID CIAD-2026-0049 in one source): search summary dates it 15 Oct 2026, and the Business Standard URL id also reads 15 Oct. Outside the window. AIM lists it under "Most Discussed" this week, which is why it looks current.
- MeitY AI-regulation consultation paper: per search summary, Vaishnaw said on 8 Oct it would come "within a month" (so around early November). Worth a check next week.
- IndiaAI GPU tender: per search summary (Medianama), MeitY invited bids for 10,000 AI compute units, first tender for 5,000, around 8-13 Oct. Outside the window; the follow-up (bid deadline, awards) is worth watching.
- Sarvam: funding talks ($250-300 mn at $3 bn, ET report via AIM, 13 Oct); Indus workspace approved for Maharashtra government departments (date not seen); Odisha land-records project (date not seen). No in-window dates found.
- Tata Power: Rs 150 billion Mumbai grid upgrade for AI data-centre demand (Indian Infrastructure listing, 19 Oct) and a 2.8 GW data-centre pipeline across 18 operators (search summary, 21 Oct). In scope and probably in window, but unfetched.
- AIM homepage headlines with no date I could establish and no budget to fetch: Vultr 20 MW AMD MI355X cluster in Chennai; CapitaLand Rs 1,940 cr / 53 MW Chennai data centre; Odisha Rs 176.83 crore disaster-recovery data centre in Keonjhar; IIT Kanpur $1 bn campaign for AI, quantum and semiconductors; IBM and MeitY Startup Hub MoU (sits among 13-14 Oct stories, probably before the window); BHASHINI-Manipur pact (Indian Infrastructure list, 16 Oct, outside).
- PIB search result listed MeitY/IndiaAI items dated 2-13 Oct (BHASHINI voice-first AI 13 Oct, MeitY pavilion at India Mobile Congress 9 Oct, AIKosh university programme 6 Oct). Nothing dated 19-25 Oct surfaced.
- No October 2026 release found for BharatGen, Krutrim, AI4Bharat or Soket; no October DPDP or IndiaAI Safety Institute news found.

## Gaps
- No MeitY / PIB / IndiaAI item for 19-25 Oct is in the file. All three government seeds (PIB, MeitY, IndiaAI news) came back as JavaScript, Hindi or navigation-only shells for the fetcher, and the search index returned nothing government-dated after 18 Oct. A run with the English PIB listing or a MeitY press-release page could still find something.

## Odd things
- AIM's "Most Discussed" and category lists on the homepage mix in stories from 13-16 Oct; the dates only show up on each article's own metadata. I checked every AIM article's metadata date before using it.
- The Chariot page's `<title>` is "How Does Chariot's Speech Recognition Compare?" while the headline is "Chariot Launches Speech Recognition Model for 10 Indian Languages". Same article.
- The Karnataka article says Sarvam charges Rs 3 per 1,000 characters for real-time and streaming TTS, while AIM's blurb for Bulbul V4 Flash says Rs 20 per 10,000 characters (Rs 2 per 1,000). I left Sarvam and ElevenLabs prices out of the claim because of this mismatch.
- `verify-quotes` rewrites the candidates file in place (adds id, fetch_tier, page_file, quote_verified, verify_note, title). The file is still a valid JSON list.
- No fetched page contained text addressed to the agent.
