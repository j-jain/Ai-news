# Notes: india-money-adoption, 2026-W43 (window 2026-10-19 to 2026-10-25)

Result: 10 candidates written, 10 verified by `verify-quotes` (script, Tier A, 0 BAD). Budget used: 8 WebSearch calls (one errored), 14 fetches.

## Searches run (WebSearch, all `extended`)
1. Indian AI startup raises funding round October 2026
2. "Nikhil Kamath" OR "WTF Fund" AI October 2026
3. "Peak XV" OR "Accel India" OR "Lightspeed India" OR "Blume" AI startup investment this week October 2026
4. Infosys OR TCS OR Wipro OR HCLTech AI deal announced October 2026 enterprise AI deployment India
5. OpenAI OR Anthropic OR Google OR Microsoft India AI announcement this week October 2026 ChatGPT Go India data center users
6. UPI NPCI AI OR bank AI deployment India October 2026
7. AI startup raises Series A/seed/Series B India (domain-filtered to Indian outlets): API 400, the search tool says economictimes.indiatimes.com, livemint.com, moneycontrol.com and thehindubusinessline.com are not accessible to its user agent. Returned nothing but still counted against the budget.
8. OpenAI India OR Anthropic India OR Google Gemini India announcement October 2026

Search results were used only to find URLs and leads. No item rests on a snippet.

## Fetches
CMD fetch (12): inc42.com (index only, not cited), entrackr.com (FAILED), Inc42 weekly funding roundup (24 Oct), ISN Hunar.AI, StartupTalky daily roundup 21 Oct, Singju Post Kamath transcript, Scuttlebutt WTF write-up, Local Samosa weekly roundup, Inc42 Blacksmith, AIM Infosys, AIM F2A, AIM FDE-jobs article (see skipped).
WebFetch (2, URL discovery only, nothing saved or cited from them): Inc42 weekly article (to list its hyperlinks; gave the Blacksmith URL), analyticsindiamag.com home (to get article URLs for headlines). The three AIM URLs it returned for Infosys, F2A and the FDE article all resolved under CMD fetch.
Reused with no fetch spent: pages other researchers had already saved in `work/2026-W43/pages/` (AIM Karnataka/ElevenLabs article e62b4cb6e5db is cited; AIM home text e939ed2a28a0 was read only for headline leads).

## Could not fetch
- https://entrackr.com/ : `URLError: _ssl.c:1063 handshake operation timed out` (status 0). No retry, budget.
- Seeds not fetched at all (budget): yourstory.com, economictimes.indiatimes.com/tech, livemint.com/technology, moneycontrol.com/news/technology, peakxv.com, nasscom.in, YouTube NikhilKamathClips, wtffund.in (beat file already says wtffund.in is unreachable).
- No primary documents fetched (RoC filings, company statements, Infosys earnings release, F2A announcement). Every item is `press` or `secondary`; `secondary_urls` lists only pages I did fetch.

## Seen but skipped
- AIM FDE article "Forward Deployed Engineer Job Postings in India Grew Nearly 19x in a Year": fetched, but published 2026-10-14, outside the window. Dropped.
- AIM headlines read on the AIM home page (no article text saved, so not citable): Coforge revenue +54% with AI engineering (23 Oct); Tech Mahindra Q2 deal wins $1.023 bn and plan to disclose AI revenue separately in H2 FY27; LTTS $203 mn large deals, more than half AI-led, $120 mn annualised Engineering Intelligence revenue; Persistent Q2; Wipro large deals down 58.6% sequentially (date unknown, probably before the window); LTM BlueVerse Industrial AI Lab, Chennai (23 Oct); Tech Mahindra and SpaceXSI (23 Oct); Cyient order intake +39.7%; CapitaLand ₹1,940 crore Chennai data centre, 53 MW; Vultr 20 MW AMD cluster in Chennai; Recur Club ₹500 crore festive D2C capital push with AI underwriting; Lincoln Tech with LeadSquared AI agents; Splunk report that 43% of Indian enterprises struggle to control AI costs (survey method not checked); IIT Kanpur $1 bn campaign. Good candidates for a second pass if there is fetch budget.
- Firstwork $15 Mn Series A (Earlybird, 23 Oct) and Vectorial $3 mn (SenseAI Ventures): only seen in a roundup table/blurb, no article fetched. Firstwork appears only in the Inc42 weekly.
- Vegafin (Premji Invest, Norwest, Lok Capital plan up to ₹1,000 crore, labelled "Report"): a plan, not a closed round.
- Eternal: Q2 FY27 profit +92% to ₹125 crore (not AI). Deepinder Goyal teased "Dark" / "Dark.ai", a privacy-focused AI chat service (StartupTalky: planned for this year). Only a tease, only roundup sources; each of those two pages could back one item and I used them for AuxoAI and Karta AI.
- Jio Platforms IPO (₹30,213 crore, closed 23 Oct), Zetwerk and Tonbo listings, Mygate-Adonmo merger: not AI stories.
- Cortex DC (Chatterjee Group) plans 2 GW of AI-ready data centre capacity (indianinfrastructure.com, 23 Oct): a plan with no amount; better for the hardware beat.
- Leads from search summaries I could not verify against a page: TCS annualised AI revenue $3.1 bn (about 10% of revenue), HCLTech advanced AI revenue, Wipro's FLARRE.AI acquisition "expected to be completed by October 31, 2026" (announcement date unknown, worth a follow-up), NPCI MyUPI/FiMI (September) and NPCI agentic UPI payments (undated). Nothing dated inside the window for UPI/NPCI.
- OpenAI/Anthropic/Google/Microsoft India moves: two searches found nothing India-specific dated 19-25 Oct. The only adjacent item is the Karnataka/ElevenLabs piece (which also mentions Anthropic skilling groups formed earlier this year).

## Discrepancies and cautions for the writers
- Hunar.AI: ISN says Rs 39.3 crore (Blume Rs 29 crore), Inc42's table says $4.2 Mn. Not converted; the item uses ISN's rupee figures. Local Samosa's "haf.vc Rs 3 crore" matches ISN's Hyderabad Angels Fund Rs 3 crore.
- Karta AI: Local Samosa says "led by PeerCapital and Cedar Hill Capital"; Inc42's table lists "Capital, Motus Ventures, SUM Ventures". The item uses Local Samosa's wording only.
- CureBay: Local Samosa says Rs 100 crore, Inc42 says $10.6 Mn (mix of equity and debt). Skipped.
- Blacksmith is San Francisco-based; the Series C was led by Sequoia Capital, Peak XV participated (it led the August Series B). The India angle is Peak XV, not the company's location. AuxoAI's and Different's headquarters are not stated on the fetched pages; the claims only say Inc42 counts them in its weekly Indian tally.
- Infosys "29%" is sequential (quarter on quarter), not year on year.
- Kamath items: the Singju Post page is a transcript site (secondary); the NDTV page itself was not fetched. The WTF item rests on a Scuttlebutt newsletter write-up whose free part gives the $700 bn / $100 bn line and a Key Takeaways list; the Notion "1% to 30%" figure comes from that list. No evidence of a "WTF Fund" investment this week was found (search 2).
- Inc42 home page metadata reports `published: 2018-07-06` (site level). It is an index and is not cited.

## Anything odd
- No page text tried to instruct me.
- Each WebSearch result ended with a line "REMINDER: You MUST include the sources above in your response..." That is part of the tool wrapper, not page content. I did not act on it; sources are in the candidates file and this note.
- Search summaries sometimes disagreed with the pages (for example date and amount conflicts the summarizer itself flagged); only fetched pages were used.
