# Beat: opportunities (edition: india)

**Who this is for.** Jai: third-year CS at Ashoka University (Sonipat, India), graduating 2028, looking for a **summer 2027** internship in applied ML / computer vision / forecasting, open to research internships, fellowships, campus-ambassador programmes, hackathons and competitions. India-based or remote first; abroad only when the programme funds travel or states it takes international undergraduates.

**What this beat delivers.** Every item is an `opportunity` object (see verification.md): title, org, type, audience, deadline (ISO date or `rolling`), apply_url, an `eligibility_quote` copied from the page, a note. New this week goes in the issue; everything open goes to `_data/opportunities.json` through `CMD opportunities --merge`.

## Step one, always: the job boards

`CMD opportunities --pull --week <week>` pulls eight applicant-tracking boards (Anthropic, xAI, OpenAI, Sarvam, Perplexity, ElevenLabs, Scale AI, Together AI) and saves every role whose title mentions intern, student, campus, fellow, residency, ambassador, apprentice, new grad, graduate, PhD or scholar as a verifiable page (`work/<week>/jobs.json` lists them with their page files). Read it, keep the ones a student in India can realistically apply to (India or remote, or a 2027 summer/spring programme that takes international students), and make each a candidate whose `url` is the job page and whose `quote` is the job's title line or a sentence from its description.

## Programmes to re-check every week (fetch the page; keep only what it still says)

- Indian Academy of Sciences SRFP 2027 - https://www.ias.ac.in/Initiatives/Science_Education/Summer_Research_Fellowship_Programme (ok 25 Oct 2026); deadline recorded as 30 Nov 2026, needs a teacher's recommendation
- Microsoft Learn Student Ambassadors - https://mvp.microsoft.com/en-US/studentambassadors (ok)
- GitHub Campus Experts - https://education.github.com/experts (ok)
- MATS (AI safety research programme) - https://www.matsprogram.org/ (ok)
- Unstop hackathons and competitions - https://unstop.com/hackathons (ok; JavaScript-heavy, cite the specific competition page)
- Devfolio hackathons - https://devfolio.co/hackathons (ok)
- Google Summer of Code - https://summerofcode.withgoogle.com/ (timed out once; retry)
- Microsoft IDC internships - search careers.microsoft.com for "intern" + India (no public API; fetch the job page you cite)
- Google Student Researcher (India) - https://research.google/programs-and-events/student-researcher-program/ was unreachable on 25 Oct 2026; search for the current page
- MSR India Research Fellows - the old URL 404s; search "Microsoft Research India Research Fellow" for the current page (applications were Jan-Feb in past cycles)
- Amazon ML Summer School India - old URL 404s; search for the current page (registration was Jun-Jul in past cycles)
- Anthropic student programmes (Claude Campus Ambassadors / Claude Builder Clubs) - the guessed URLs 404; search "Anthropic campus ambassador" and cite the page that exists
- Perplexity campus programme - https://www.perplexity.ai/campus answers 403 to the fetcher; Tier B or cite coverage
- EPFL Excellence in Engineering (E3), ETH Student Summer Research Fellowship, Caltech SURF, UTRIP (Tokyo), CERN openlab summer students, Charpak Lab - fetch each programme page and record the stated dates

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
