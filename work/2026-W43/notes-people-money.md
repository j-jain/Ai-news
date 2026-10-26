# notes-people-money, 2026-W43 (window 2026-10-19 to 2026-10-25)

Result: 7 candidates written, 7 verified (`verify-quotes`: items 7, verified 7, failed 0). All seven are Tier A TechCrunch pages with `published` taken from `meta article:published_time`. Budget used: 8 of 8 searches, 14 of 14 fetches (the CNBC attempt counted and failed).

## Items (in file order)
1. Anthropic's backers' stakes ahead of an IPO "expected this year" at up to $2T (TC, 23 Oct), sig 4
2. Flapping Airplanes $1B Series A at reported $6B, Index + Lux (TC, 21 Oct), sig 4
3. Tenstorrent $1.5B at $6.2B, Trace Capital + Innovation X (TC, 19 Oct), sig 3
4. Legora $550M Series E at $8.8B, Atreides led, ARR over $200M (TC, 21 Oct), sig 3
5. Town $108M Series B at a unicorn valuation, Forerunner + Menlo (TC, 19 Oct), sig 3
6. Tesla starts Optimus production in Fremont, Q3 net income $787M (-43%) (TC, 21 Oct), sig 3
7. a16z Crypto renamed a16z Frontier, mandate widened to AI/robotics (TC, 22 Oct), sig 3

Possible overlap with other beats (selector merges, better-sourced survives): Tenstorrent (hardware & prices), Tesla Optimus (hardware/robotics), Anthropic IPO (frontier labs).

## Searches run (WebSearch, all `standard` mode, 8 of 8)
1. Andrej Karpathy new project OR post October 2026
2. AI startup raises funding round valuation this week October 2026
3. Anthropic IPO filing confidential S-1 October 2026
4. Elon Musk xAI news October 2026
5. Flapping Airplanes raises $1B $6B valuation; Legora $550M Series E; Tenstorrent $6.2B valuation techcrunch
6. acquires AI startup acquisition announced October 2026
7. Altman Amodei Hassabis LeCun Sutskever Jensen Huang announcement October 21 22 2026
8. Tesla Q3 2026 earnings Optimus Musk SpaceX xAI Grok this week

Search snippets were used only to find leads; nothing in the JSON rests on a snippet. Queries containing "this week" or "October 2026" mostly returned stale items (Decagon Jan 2026, Cursor Nov 2025, Sierra Oct 2025, Cognition Sep 2025).

## Fetches (14)
- CMD fetch https://karpathy.bearblog.dev/ : 200 but thin (28 words, only "Home Blog" nav). The post list is at /blog/.
- CMD fetch https://karpathy.bearblog.dev/blog/ : 200. Latest post is 30 Apr 2026 "Sequoia Ascent 2026 summary"; nothing in the window.
- CMD fetch https://techcrunch.com/category/venture/ : 200, 946 words. Used as an index only (never cited). Its `published` 2026-10-23 is just the newest article on the page.
- WebFetch https://techcrunch.com/category/venture/ : used only to read off the article links (URL discovery), not registered, not cited. Every URL it returned that I then fetched came back 200 with the expected title, so the links were real.
- CMD fetch https://www.ycombinator.com/blog : 200. Index only. Dated posts 10/19 and 10/20/2026 are "Founding Engineer Series" stories, not news for this beat. The featured "Vivian Midha Shen and Raphael Schaad Join YC as General Partners" shows no date, so it cannot be dated.
- CMD fetch https://www.sequoiacap.com/stories/ : 200 (redirects to sequoiacap.com/stories). Cards carry no dates, so nothing could be placed in the window.
- CMD fetch x7 TechCrunch articles (Anthropic backers, Flapping Airplanes, Tenstorrent, Legora, Tesla Optimus, Town, a16z Frontier): all 200, Tier A, dates from meta tags.

## Could not fetch / not fetched
- https://www.cnbc.com/technology/ : WebFetch returned HTTP 403. The beat file lists it as ok for the repo fetcher on 25 Oct, but I did not retry with CMD fetch (budget, and it saves text only, so I would not have got article URLs).
- Not fetched for budget: github.com/karpathy, ycombinator.com/rfs, ycombinator.com/launches.
- Per the beat file, a16z.com/news-content and news.crunchbase.com are unreachable from here; I did not try them.
- Primary sources were not fetched (no URLs known, no budget): Flapping Airplanes' announcement, Tenstorrent's release, Legora's and Town's posts, Tesla's Q3 shareholder letter, Chris Dixon's a16z blog post, any Anthropic statement. That is why every item is `press` with empty `secondary_urls`. The writer should treat the figures as single-source (TechCrunch, which itself cites Bloomberg for the stake values and Bloomberg for the Keller quote).
- Leads seen only in search results, unfetched and therefore not cited: thenextweb.com/news/flapping-airplanes-1b-6b-valuation (second source for item 2); dealroom.co and aiweekly.co pages on Tenstorrent; electrek.co/2026/10/21/tesla-tsla-q3-2026-financial-results/ (second source for item 6). Electrek's snippet said revenue $28.05B; TechCrunch's page says $28.04B and the item uses TechCrunch's figure.

## Seen but skipped
- Warhound $200M (TC, 22 Oct): defense / "war dogs", not AI-focused; not fetched.
- Blacksmith unicorn after Sequoia-led Series C (TC, 21 Oct): not fetched (budget), AI relevance unknown. Best remaining Sequoia item if someone has budget.
- Inspired Capital $450M fourth fund (TC, 20 Oct): VC fund close, not AI-specific.
- Uber puts all 30,000 employees on ChatGPT Work (TC, 22 Oct): adoption/frontier-labs story; not fetched.
- Disrupt session write-ups (Series A advice, "secret to fast startup growth", Superhuman founder on PMF), Carta/NewView, Foursquare, Airbnb, PHP, smart TVs: not news for this beat.
- Benchmark "AI eroding the venture pact" (15 Oct) and the Nvidia-insider-turned-VC robotics piece (16 Oct): before the window.
- Search-snippet items outside the window or from aggregators, not used: Anthropic's confidential S-1 and the $65B Series H at $965B post-money (reported June 2026; TC's page only confirms $965B as the latest private valuation); Crunchbase News count of 195 AI-on-AI acquisitions in 2026 (6 Oct); SpaceX completing a $60B Cursor acquisition and xAI folding into SpaceX / "SpaceXAI" (Aug and later, aggregator pages only); OpenAI acquiring NextSlide (Aug); Karpathy joining Anthropic (announced May 2026 per snippets).

## Coverage gaps for the editor
- Karpathy: no blog post or announcement in the window found (latest blog post 30 Apr 2026). GitHub not checked.
- Musk/xAI/SpaceX: only the Tesla Q3 item. No in-window xAI or SpaceX item found.
- Altman, Amodei, Hassabis, LeCun, Sutskever, Huang, Nadella, Pichai, Zuckerberg: the one combined search returned only background profiles. No per-person searches (budget), so absence here is not evidence nothing happened.
- Acquisitions and IPO filings: nothing in-window found beyond the Anthropic IPO context in item 1.
- Earnings: only Tesla. I did not check other companies' reporting dates or results.
- YC Requests for Startups: not fetched, so no "new areas" item from YC; item 7 (a16z Frontier) is the only thesis-type item.

## Odd things
- TechCrunch pages still show a stale "Disrupt doors open Oct. 13" banner and ticket promos. Ignored; no page text tried to instruct me.
- The Tesla article's URL slug has a typo ("tesla-stars-optimus..."); the URL in the JSON is exactly what was fetched.
- The Anthropic article carries "Updated to include Coatue's returns". The figures used in the claim (Iconiq $17B, Menlo $14B) are attributed there to Bloomberg; Coatue's roughly $7.5B is attributed to "a person familiar" and was left out of the claim.
- Flapping Airplanes' $6B valuation is "reportedly" in TechCrunch's wording; the headline and claim keep that hedge. The Anthropic "$2 trillion" is likewise an expectation, not a filed figure.
