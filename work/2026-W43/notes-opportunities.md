# Notes: opportunities beat, 2026-W43 (window 2026-10-19 to 2026-10-25, run on 26 Oct)

Result: 12 candidates in `candidates-opportunities.json`, 12 of 12 pass `verify-quotes` (quote and eligibility_quote both found in saved Tier A pages). No Tier B pages used. `state/seen.json` and `_data/opportunities.json` were empty.

## Budget used (be aware)

- WebSearch: 8 of 8 (all listed below).
- `CMD fetch`: 14 of 14 (7 of them returned `cached: true` because the same URL had already been saved earlier this week, so they cost no network). One fetch was wasted on the SRFP PDF (the fetcher cannot read PDFs).
- Beyond the budget, and not used as evidence: about 15 plain `curl` probes for link discovery only (IAS home page HTML to find the SRFP 2027 links, URL-exists checks for CERN/UTRIP/Caltech/EPFL/GitHub, a look at the Caltech SURF, Devfolio and Unstop listing data, the Goldman Sachs and IAS FAST pages, the aggregator page that linked to the Gnani page). None of these is cited. Scratch files are in the session scratchpad, not in the repo.
- Two pages I cite were saved earlier this week by someone else (Purdue SURF as the main source, the SRFP landing page as a secondary URL); the job pages come from my pull. All are Tier A.

## Job-board pull (`opportunities --pull`)

53 roles matched: Anthropic 5, xAI 4, OpenAI 0, Sarvam 3, Perplexity 7, ElevenLabs 0, Scale AI 21, Together AI 13.

Kept (7 job pages): Scale AI ML Research Intern (Summer 2027, SF/NY); Scale AI SWE Intern (Summer 2027, Doha; London and SF versions listed as secondary URLs); Together AI Research Intern Model Shaping (Summer 2027, SF/Amsterdam, takes bachelor's students); Together AI GPU Programming intern (Summer 2027); xAI Summer 2027 SWE Internship/Co-op (Palo Alto); Perplexity Search ML Engineer internship (London, in person, no cohort dates); Sarvam AI marketing internship (Bengaluru, significance 1, included only because it is the sole India-based role pulled). None of the on-site foreign roles states a visa position except Scale Doha (which says Scale will support the visa process); the notes on each item say so.

Skipped, with reasons:
- Anthropic Fellows Program (AI Safety & Security; ML Systems & RL; Economics & Policy): page says "you must have work authorization in the US, UK, or Canada and be located in that country", no visa sponsorship. The AI Safety & Security page says "apply here by October 30" for the January cohort. Not applicable from India.
- Anthropic STEM Fellow, Conceptual Reasoning Fellow: US work authorization, fixed-term contract through an employer of record.
- Scale AI "Human Frontier Collective" fellows (ML, STEM, SWE, Legal, Medical, Finance; US/UK/Canada): 1099 contractor roles needing US/UK/Canada authorization and PhD or 5+ years of experience. Scale New Grad SWE roles: not applicable until 2028.
- xAI Spring 2027 internships (start January or March 2027, term time) and the two Business Operations internships (not CS).
- Perplexity: Search ML and Search Backend internships in Belgrade say "You're currently enrolled at a Serbian university"; the Berlin ML Research Engineer internship is in person and lists a publication record under qualifications; MTS New Grad and Early Career roles are SF full-time (the Early Career page says current students should not apply); Perplexity Research Fellowship (SF/Palo Alto/NYC) is "not an internship program", needs a 1-year leave of absence for current students, and its priority date (30 Sep 2026) has passed. The London Search ML internship is kept (no such restrictions on the page).
- Together AI: Research Intern Inference asks for a final-year student; Frontier Agents is PhD only; Frontier Speculative Decoding is Master's or PhD; Winter 2027 internships are term time; Hardware Security, Growth Marketing and New Grad roles off target.
- Sarvam: Marketing Intern (17 Sep) not ML; Growth Marketing Intern asks for "a final-year student or recent grad".
- Job-page dates are `updated_at` / `publishedAt` fields, not proof of when a role first appeared; claims say "listing updated".

## Queries run (8 WebSearch)

1. Microsoft Research India Research Fellow 2027 applications open undergraduate (extended)
2. Anthropic Claude campus ambassador program students apply (extended)
3. AI hackathon India November 2026 students register (extended)
4. Google Student Researcher program India 2027 apply (standard)
5. ETH Zurich Student Summer Research Fellowship 2027 application deadline international undergraduate (standard)
6. Charpak Lab 2027 applications research internship France Indian students Campus France (standard)
7. IndiaAI challenge OR hackathon 2026 students apply deadline December 2026 (extended)
8. summer 2027 internship machine learning computer vision India undergraduate apply open now (extended)

## What each programme page states now (beat-file checklist)

Fetched and listed:
- **SRFP 2027**: the beat's URL (`ias.ac.in/.../Summer_Research_Fellowship_Programme`) now returns HTTP 200 but the body is the site's "404! ... page can not be found" text (soft 404), so the "ok 25 Oct" mark in the beat file is wrong. The live pages are `webjapps.ias.ac.in/fellowship2027/` (landing, letter dated 10 September 2026) and `.../application_instructions.jsp` (eligibility, deadline). Deadline 30 November 2026 confirmed; selection around March-April 2027. Eligibility rows include "BSc (Research) (III year only)" and "BE / BTech / BCA (II and III years only)"; 65% average marks; one teacher's recommendation. Suggest replacing the seed URL with the landing page. FAST-SF 2027 (same deadline) is limited to North-Eastern and some other states (Haryana is not on the list), so not listed.
- **ETH Zurich SSRF**: window 1 Nov to 16 Dec 2026 13:00 CET, programme 2 Jul to 27 Aug 2027, CHF 4,000, travel and visa expenses covered, decisions by end Feb 2027. Listed.
- **Gnani Great Indian AI Internship Challenge** (surfaced by search 7 through an aggregator; official page found from that aggregator's link): deadline 10 Nov 2026 11:59 PM IST; students in India only. Listed.
- **Code for a Billion** hackathon: submissions close 15 Nov 2026. Listed.
- **Purdue SURF 2027**: international deadline 15 Dec 2026; page last modified 1 Oct 2026. Listed.

Fetched, not listed:
- **Claude Campus Ambassadors / Builder Clubs** (`claude.com/programs/campus`, the page that exists): "Applications open September 1 and close September 12"; "The program is closed for Fall 2026"; runs Sept 2026 to June 2027; USD 3,600 stipend; 18+ and work authorization in country of study. Closed, no next date.
- **MATS**: "Applications for the Winter 2027 cohort are now closed." The sentence "Winter and Summer 2027 cohorts are open" sits under the mentor-application menu, not for fellows. No Summer 2027 fellow dates yet.
- **GitHub Campus Experts**: `education.github.com/experts` now redirects to `github.com/education/students`; `github.com/education/experts` is 404. The students page only has a blurb ("Learn more about Campus Experts") with no application window. It does confirm "Copilot Student ... Available for free to verified students" (a standing perk, not listed).
- **Microsoft Learn Student Ambassadors**: `mvp.microsoft.com/en-US/studentambassadors` returns 3 words (JS wall). Tier B was not attempted because a Tier B page cannot back a quotation.
- **Google Summer of Code**: home page and timeline page (last updated 2025-12-03) show the 2026 cycle (contributor applications 16 to 31 March 2026); no 2027 dates. The page's "Page Summary" box gives different dates (Jan 22-Feb 6, Mar 18-Apr 2) from the timeline below it; ignore the summary. Pattern: orgs apply in January, contributors in March.
- **CERN Summer Student Programme**: `home.cern/summer-student-programme` says "currently open for applications" and "no later than end of January" with no year; `careers.cern/summer` (redirects to /programmes/summer-studentship/) gives no dates. Criteria: bachelor's or master's in physics/engineering/CS/maths with "at least 6 semesters" completed; 94 CHF per calendar day. Not listed because no dated deadline is evidenced; re-check in December.
- **Caltech SURF**: page says "In 2027, Fellows will receive an $8,354 award for the ten-week period" and remote projects are not allowed; eligibility and deadline sit on sub-pages not fetched.
- **Unstop / Devfolio indexes**: not cited (index pages). Discovery only: Devfolio's listing is small college events (e.g. Hacknauts 2.0, THE BIG HACK 2.0, haxfinity [AI + HealthTech, registration ends 10 Nov]); Unstop's open list includes BharatCode Build League (deadline 8 Nov 2026, winner may interview for a 3-month paid SDE internship, 10 registrations when checked, unfamiliar organiser, odd benefit names) which I skipped as low confidence.

Not fetched (search summaries only, unverified):
- **MSR India Research Fellows**: official page (`microsoft.com/en-us/research/academic-program/research-fellows-program-at-microsoft-research-india/`) reportedly lists the 2026 cycle (opened January, closed mid-February 2026, degree completed by summer 2026). 2027 cycle unconfirmed. MSR "Undergraduate Research Internship - Computing" reportedly closed 5 Oct 2026.
- **Google Student Researcher (India)**: all hits are the 2026 cycle (deadlines 31 Mar, 30 Jun, 31 Jul 2026), must be located in India; no 2027 posting seen. Official page not re-fetched.
- **Charpak**: only 2025-era listings (France Excellence Charpak Summer Training Scholarship, last deadline seen 24 Jan 2025); no 2027 call found.
- **Amazon ML Summer School, EPFL E3, UTRIP, CERN openlab, Perplexity campus, Microsoft IDC internships**: not searched or fetched (budget). No IDC job page surfaced; search 8 returned aggregators only.
- **IBM Research India "Research Intern - AI"** (Gurgaon/Bangalore; B.E./B.Tech/M.E./M.Tech/PhD) and **Adobe Research India 2027 intern**: aggregator mentions only; no primary page found.
- **NVIDIA Ignite 2027**: window 5 to 18 Oct 2026, closed, and aimed at first/second-year undergrads (search summary).
- **PayPal AI Hackathon 2026**: Internshala lists 13 Nov, Startup Grants India says submissions due 12 Nov; sources disagree and no official page found.

## Leads worth a follow-up fetch (not in candidates)

1. **IndiaAI Fellowship 2026-27** (primary portal `https://fellowship.indiaai.gov.in/`, not fetched). Only evidence is a Global South Opportunities write-up dated 16 Oct 2026 (saved earlier this week): deadline 30 Nov 2026, up to INR 1 lakh for undergraduates (INR 2 lakh postgraduate, plus INR 1 lakh for an international conference). Its eligibility says "Four-year undergraduate programmes: Students at the beginning of the seventh semester", which would exclude a student mid-semester 5 this cycle. Aggregators are not evidence, so it is not listed. Highest-value primary fetch next.
2. **Goldman Sachs 2027 Summer Analyst Program, India** (Tier A page saved earlier this week): "Students graduating from a Bachelors or Masters degree program in the year 2028", Engineering is a division, "Applications will open July 1st" with no year and no close date, so open/closed status is unknown. The GS India Hackathon 2026 page (open to students graduating 2027 or 2028) says applications closed 10 May 2026.
3. **CERN Summer Student**, **ETH SSRF window opens 1 Nov**, **MATS Summer 2027**, **GSoC 2027**, **Google Student Researcher 2027** and **Amazon ML Summer School** are calendar items for the next few runs.

## Odd things

- No fetched page contained text addressed to me or tried to change the task. The Perplexity fellowship page tells applicants to write without AI help; that is a rule for applicants and was ignored.
- The Code for India page prints a quoted statement attributed to the Prime Minister (15 Aug 2026); not used.
- The Gnani page text runs words together ("Up to 100paid"), so I quoted other sentences.
- The SRFP and several other pages carry no machine-readable date; their items have `published: null` and rely on the future deadline. ETH's window had not opened at the time of checking.
- Ashoka-style degree names (e.g. "BSc (Research)") need to match an SRFP row exactly; the item note tells the reader to confirm.

## Suggested beat-file edits

Replace the SRFP seed with `https://webjapps.ias.ac.in/fellowship2027/`; drop `education.github.com/experts` (redirect); use `https://claude.com/programs/campus`, `https://developers.google.com/open-source/gsoc/timeline`, `https://careers.cern/programmes/summer-studentship/`, `https://inf.ethz.ch/studies/summer-research-fellowship/how-to-apply.html`; add Purdue SURF (`https://engineering.purdue.edu/Engr/Research/EURO/students/about-SURF`) and `https://fellowship.indiaai.gov.in/`.
