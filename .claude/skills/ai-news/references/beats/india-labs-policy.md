# Beat: india-labs-policy (edition: india)

**What this beat covers.** Sarvam and every other Indian lab building models or core AI infrastructure (Sarvam, Krutrim, AI4Bharat, BharatGen, IISc/IIT labs, Gnani, CoRover, Soket, Zoho's models, Tech Mahindra/Infosys models), plus the state: the IndiaAI Mission (compute allocations, datasets, the IndiaAI Safety Institute, foundation-model grants), MeitY and PIB announcements, DPDP rules as they touch AI, state AI policies, data-centre and chip projects on Indian soil (Tata Electronics, Yotta, Reliance/Jio, Google/Microsoft/Amazon India capacity), India at international AI forums, government procurement of AI.

**What counts.** A release, a benchmark, a price, an allocation, a signed deal, a rule published, a plant inaugurated - with a date inside the window and a page that states the number. Open-weight Indian models are `edition: both`.

**What does not count.** Opinion columns, "India could become...", conference panels without a decision, anniversary pieces, anything whose only source is a tweet.

## Seeds (fetch each with `CMD fetch`; they are indexes - cite the specific article)

- https://www.sarvam.ai/blogs (ok 25 Oct 2026)
- https://indiaai.gov.in/news (ok) - the IndiaAI Mission's own news
- https://www.pib.gov.in/allRel.aspx (ok) - Press Information Bureau; search for the MeitY releases of the week
- https://www.meity.gov.in/ (ok)
- https://analyticsindiamag.com/ (ok) - India-focused AI press; good for lab news, verify numbers against the primary source
- https://ai4bharat.iitm.ac.in/ (ok)
- https://bharatgen.tech/ (ok)
- https://economictimes.indiatimes.com/tech (ok; ET Prime stories are paywalled - `thin: true` pages cannot be cited)
- https://www.krutrim.com/ (connection refused from here on 25 Oct 2026; use coverage from Inc42 / ET / AIM)

## Search queries (WebSearch, `extended` mode; add the month and year)

- "Sarvam AI" <month year>
- "IndiaAI Mission" <month year>
- "IndiaAI" GPUs compute allocation
- MeitY artificial intelligence announcement <month year>
- India LLM launch <month year>
- BharatGen OR Krutrim OR AI4Bharat <month year>
- India AI data centre announced <month year>
- DPDP rules AI India <month year>
- "IndiaAI Safety Institute"

## Notes

- PIB releases carry a date line at the top ("Posted On: 22 OCT 2026 4:15PM by PIB Delhi"); if `CMD fetch` finds no metadata date, set `published` and put that line in `published_evidence`.
- Sarvam's blog posts often lack machine-readable dates; the date is in the page text - quote it as evidence.
- Government numbers (crore, GPUs, GW) must be copied exactly with the unit the page uses.
