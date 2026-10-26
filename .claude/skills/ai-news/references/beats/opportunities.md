# Beat: opportunities (edition: india)

**Who this is for.** Jai: third-year CS at Ashoka University (Sonipat, India), graduating 2028, looking for a **summer 2027** internship in applied ML / computer vision / forecasting, open to research internships, fellowships, campus-ambassador programmes, hackathons and competitions. India-based or remote first; abroad only when the programme funds travel or states it takes international undergraduates.

**What this beat delivers.** Every item is an `opportunity` object (see verification.md): title, org, type, audience, deadline (ISO date or `rolling`), apply_url, an `eligibility_quote` copied from the page, a note. New this week goes in the issue; everything open goes to `_data/opportunities.json` through `CMD opportunities --merge`.

## Step one, always: the job boards

`CMD opportunities --pull --week <week>` pulls eight applicant-tracking boards (Anthropic, xAI, OpenAI, Sarvam, Perplexity, ElevenLabs, Scale AI, Together AI) and saves every role whose title mentions intern, student, campus, fellow, residency, ambassador, apprentice, new grad, graduate, PhD or scholar as a verifiable page (`work/<week>/jobs.json` lists them with their page files). Read it, keep the ones a student in India can realistically apply to (India or remote, or a 2027 summer/spring programme that takes international students), and make each a candidate whose `url` is the job page and whose `quote` is the job's title line or a sentence from its description.

## Programmes to re-check every week (fetch the page; keep only what it still says; status as of the 2026-W43 run)

- Indian Academy of Sciences SRFP 2027 - https://webjapps.ias.ac.in/fellowship2027/ (landing page; the old ias.ac.in URL is a soft 404 and the form is a PDF the fetcher cannot read). Deadline on the page: 30 Nov 2026; needs a teacher's recommendation.
- IndiaAI Fellowship - https://fellowship.indiaai.gov.in/ (deadline reported as 30 Nov 2026; check the UG eligibility row - "beginning of the seventh semester" may exclude a third-year)
- Claude Campus Ambassadors / Builder Clubs - https://claude.com/programs/campus (applications were 1-12 Sep; "closed for Fall 2026"; re-check from August)
- MATS - https://www.matsprogram.org/ (Winter 2027 closed; watch for Summer 2027 fellow dates)
- GitHub Education for students - https://github.com/education/students (Campus Experts has no open window; the old /experts URL redirects)
- Microsoft Learn Student Ambassadors - https://mvp.microsoft.com/en-US/studentambassadors (JavaScript wall, 3 words to the fetcher; search for coverage or skip)
- Google Summer of Code timeline - https://developers.google.com/open-source/gsoc/timeline (orgs apply in January, contributors in March; 2027 dates appear around December)
- ETH Zurich Student Summer Research Fellowship - https://inf.ethz.ch/studies/summer-research-fellowship/how-to-apply.html (window 1 Nov to 16 Dec 2026; travel and visa covered)
- CERN Summer Student Programme - https://careers.cern/programmes/summer-studentship/ (needs "at least 6 semesters" completed; dated deadline appears around December)
- Purdue SURF - https://engineering.purdue.edu/Engr/Research/EURO/students/about-SURF (international deadline 15 Dec 2026)
- Caltech SURF - https://sfp.caltech.edu/undergraduate-research/programs/surf (eligibility and deadline on sub-pages; remote projects not allowed)
- Gnani Great Indian AI Internship Challenge, Code for a Billion hackathon - found via search in W43 (deadlines 10 Nov and 15 Nov 2026); re-find the official pages
- Microsoft IDC internships - search careers.microsoft.com for "intern" + India (no public API; fetch the job page you cite)
- MSR India Research Fellows - https://www.microsoft.com/en-us/research/academic-program/research-fellows-program-at-microsoft-research-india/ (2026 cycle opened January, closed mid-February; watch for 2027)
- Google Student Researcher (India) - search for the current page; 2026 cycle had deadlines 31 Mar, 30 Jun, 31 Jul; no 2027 posting seen yet
- Amazon ML Summer School India, EPFL E3, UTRIP (Tokyo), CERN openlab, Charpak, Perplexity campus - not yet verified; search and fetch when budget allows (EPFL E3 closes 1 Nov 2026 per Jai's own calendar; confirm on the page)
- Unstop / Devfolio - https://unstop.com/hackathons and https://devfolio.co/hackathons are discovery indexes only; cite the specific competition page and skip unfamiliar organisers with odd terms

## Search queries

- summer 2027 internship machine learning India apply
- "summer 2027" internship AI undergraduate remote
- campus ambassador program AI 2026 apply students India
- AI hackathon India <next month> <year>
- fellowship undergraduate AI 2027 deadline
- research internship 2027 undergraduate India deadline
- "IndiaAI" hackathon OR challenge <year>
- Kaggle competition launched <month year>
- student developer program AI credits 2026

## Rules for this beat

- `deadline` must be on the page (quote the sentence that states it in `eligibility_quote` or `note`). "Applications open" with no date -> `rolling`.
- Audience must say who is eligible (year, degree, country) in the page's words.
- Never list a role Jai cannot apply to (e.g. "5+ years experience", US citizens only) - note it in `notes-opportunities.md` instead.
- Expired or closed -> not a candidate; the merge step prunes old rows automatically.
