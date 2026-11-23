---
layout: issue
title: "India: Sarvam ships a cheaper 105B, Token Factory sparks a sovereignty row"
edition: india
week: "2026-W47"
date: 2026-11-23
window: "2026-11-16 to 2026-11-22"
summary: "Sarvam's new 105B checkpoint and India-hosted Token Factory, a sovereignty fight over Chinese models, and Accel money for robot training data."
sources_fetched: 0
items_dropped: 0
---
## If you only read three things

- **Sarvam's 105B gets better, much cheaper** Sarvam released the open-weight Sarvam-105B-1711 on 22 Nov, with its eight-benchmark conversational agent average rising from 42.6 to 73.9 and blended price falling from $0.44 to $0.15 per million tokens [Sarvam](https://www.sarvam.ai/blogs/sarvam-105b-1711). If you are building an Indic voice or support agent, it is worth testing at that price.
- **Indian GPUs now serve open models** Sarvam launched Token Factory on 16 Nov, an inference stack that serves its own and leading open-weight models from GPU clusters located in India through one OpenAI-compatible API [Sarvam](https://www.sarvam.ai/blogs/sarvam-token-factory). That gives you a rupee-priced, India-hosted endpoint for side projects that touch user data.
- **Accel leads a $26M equity round for robot data** Bengaluru's Humyn Labs raised $47 million in Series A, $26 million in equity led by Accel plus $21 million in venture debt led by Lighthouse Canton [TechCrunch](https://techcrunch.com/2026/11/18/accel-backs-indias-humyn-labs-to-supply-training-data-needed-by-u-s-robotics-ai-developers/). Data pipelines for physical AI are a real business in India now.

## Sarvam and the Indian labs

Sarvam had the week. On 22 Nov it put out Sarvam-105B-1711, a new open-weight checkpoint of Sarvam 105B trained on its upgraded B200 infrastructure and pitched as a Flash-Lite model for customer support, voice agents and agentic tasks [Sarvam](https://www.sarvam.ai/blogs/sarvam-105b-1711).

The weights are on Hugging Face in BF16 and in a 65 GB NVFP4 version that, per the post, runs on a single workstation GPU [Sarvam blog](https://www.sarvam.ai/blogs/sarvam-105b-1711).

The gains since the February release are on exactly the skills a chat agent needs. Instruction following on IFBench rose from 32.5 to 82.5, tool use on Tau2 from 46.2 to 85.5, and the Indic suite from 30.1 to 79.1 [Sarvam](https://www.sarvam.ai/blogs/sarvam-105b-1711).

Sarvam says it averages 73.9 at a blended $0.15 per million tokens, against 74.0 for Gemini 3.5 Flash-Lite at $0.85 and 73.0 for Gemma 4 31B at $0.54 [Sarvam blog](https://www.sarvam.ai/blogs/sarvam-105b-1711). These are Sarvam's own evaluations on its own setup, so treat the leaderboard as a claim to test.

Six days earlier Sarvam launched Token Factory, which serves Sarvam 105B alongside GLM 5.3, GLM 5.3 Flash, DeepSeek V4.1 Flash 1017, DeepSeek V4 Pro, Kimi K3.1 Pro and Gemma 4 31B [Sarvam](https://www.sarvam.ai/blogs/sarvam-token-factory).

DeepSeek V4.1 Flash launches at an introductory ₹14 per million input tokens and ₹55 per million output tokens on the Standard endpoint [Token Factory](https://www.sarvam.ai/blogs/sarvam-token-factory).

Sarvam also says it runs India's largest B200 cluster and serves 450B+ tokens a day on DeepSeek V4.1 Flash, with 95.7% of prompt tokens served from cache [Sarvam](https://www.sarvam.ai/blogs/sarvam-token-factory).

Soket AI, maker of the IndiaAI-backed EKA-1, raised $4 Mn (around ₹37 Cr) from Bajaj Finserv's Finserv Intelligence and Pennant Technologies [Inc42](https://inc42.com/buzz/soket-ai-raises-4-mn-from-bajaj-finserv-to-expand-its-ai-model-horizon/).

Inc42 describes EKA-1 as a 26-Bn-parameter foundation model and says Soket is building models focused on mathematics, coding and reasoning [Inc42](https://inc42.com/buzz/soket-ai-raises-4-mn-from-bajaj-finserv-to-expand-its-ai-model-horizon/).

**My read:** The Tau2 and Indic jumps are the numbers that matter for anyone building agents, and Samvaad bench being public means you can check them yourself rather than trust a chart. A 65 GB checkpoint is not a laptop model, so for local work you will be calling it, not running it.

## Government, compute and policy

The sharpest policy argument of the week was about who Indian public compute is for. After criticism over hosting Chinese models on Token Factory, Sarvam said the platform runs on privately procured GPUs and that its IndiaAI Mission subsidised access ended in March 2026 [Business Standard](https://www.business-standard.com/technology/artificial-intelligence/explained-sarvam-ai-s-token-factory-and-debate-over-ai-sovereignty-goals-126112000685_1.html).

Business Standard frames the criticism as whether a company backed to build homegrown models should also build a commercial business around models developed in other countries, particularly China [Business Standard](https://www.business-standard.com/technology/artificial-intelligence/explained-sarvam-ai-s-token-factory-and-debate-over-ai-sovereignty-goals-126112000685_1.html).

The same explainer notes that Sarvam is not alone: E2E Networks launched its Blaze inference platform on November 2, 2026, offering DeepSeek, Qwen, GLM and Gemma through a single API [Business Standard](https://www.business-standard.com/technology/artificial-intelligence/explained-sarvam-ai-s-token-factory-and-debate-over-ai-sovereignty-goals-126112000685_1.html).

Sarvam says Token Factory does not send customer prompts to the overseas developers of those models and offers zero data retention on request [Business Standard](https://www.business-standard.com/technology/artificial-intelligence/explained-sarvam-ai-s-token-factory-and-debate-over-ai-sovereignty-goals-126112000685_1.html).

On physical capacity, CtrlS is targeting 4.4 GW by 2030 and recently announced a ₹10,000 crore, 150 MW AI factory in Bodh Gaya, Bihar, plus a ₹400 crore, 12 MW Patna data centre [AIM](https://analyticsindiamag.com/ai-features/inside-ctrlss-44-gw-bet-on-indias-data-centre-boom).

AIM reports that CtrlS plans more than 20 edge data centres across tier-2 and tier-3 cities and currently operates 19 data centres across 10 cities [AIM](https://analyticsindiamag.com/ai-features/inside-ctrlss-44-gw-bet-on-indias-data-centre-boom).

The bottleneck CtrlS names is power. Its operations president Rahul Dhar wants power demand forecasts cut from 7–8 year horizons to three to four years, and faster right-of-way approvals for fibre and transmission lines [AIM](https://analyticsindiamag.com/ai-features/inside-ctrlss-44-gw-bet-on-indias-data-centre-boom).

AIM also notes the central government introduced a 21-year tax holiday this year for foreign companies providing global cloud services using India-based data centres, and that CtrlS is giving MeitY inputs on the proposed data centre policy [AIM](https://analyticsindiamag.com/ai-features/inside-ctrlss-44-gw-bet-on-indias-data-centre-boom).

**My read:** Hosting a Chinese model in India is a data-residency answer, not a sovereignty answer, and Business Standard says as much. For you the practical question is simpler: is the endpoint fast, cheap and contractually clear about retention.

## Startups and money

One of the week's biggest India AI cheques went to robot training data. Humyn Labs raised $47 million in Series A financing, with $26 million in equity led by Accel and $21 million in venture debt led by Lighthouse Canton [TechCrunch](https://techcrunch.com/2026/11/18/accel-backs-indias-humyn-labs-to-supply-training-data-needed-by-u-s-robotics-ai-developers/).

It records people doing everyday tasks on its own two-camera hardware, labels the footage, and told TechCrunch it generated $10 million in revenue between April and October, with about 90% of revenue from the US [TechCrunch](https://techcrunch.com/2026/11/18/accel-backs-indias-humyn-labs-to-supply-training-data-needed-by-u-s-robotics-ai-developers/).

Dreamteam, an AI-first CRM founded in 2025 by former Freshworks leaders, raised $53 million from Together Fund, Accel and Premji Invest [StartupTalky](https://startuptalky.com/news/daily-indian-funding-roundup-key-news-17-november-2026/).

Its agents research accounts, draft follow-up emails and flag risks in the sales pipeline, and customers include InVideo and Plex [StartupTalky](https://startuptalky.com/news/daily-indian-funding-roundup-key-news-17-november-2026/).

August AI, founded by IIT-BHU alumnus Anuruddh Mishra, raised $12 million from Accel and Peak XV Partners and launched an AI agent that phones doctors, pharmacies and insurers for US patients [Indian Startup News](https://indianstartupnews.com/funding/iit-bhu-alumnus-anuruddh-mishras-august-ai-raises-12-million-to-take-on-us-healthcare-paperwork-12828862).

The calling feature is a free beta in the US behind a waitlist, and the company says its companion app is used by more than 9.5 million people in 160 countries [Indian Startup News](https://indianstartupnews.com/funding/iit-bhu-alumnus-anuruddh-mishras-august-ai-raises-12-million-to-take-on-us-healthcare-paperwork-12828862).

Disseqt AI, which builds AI agents for AI governance and testing, raised $8 Mn (about ₹75 Cr) led by Gresham House Ventures, with cricketer Rahul Dravid in as an angel [Inc42](https://inc42.com/buzz/ai-startup-disseqt-ai-raises-8-mn-to-scale-international-operations/).

It is headquartered in Ireland but its engineering and AI teams are in Bengaluru, and Inc42 says AI startup funding more than tripled YoY to $438 Mn in the September quarter [Inc42](https://inc42.com/buzz/ai-startup-disseqt-ai-raises-8-mn-to-scale-international-operations/).

**My read:** Several of these rounds look aimed at customers beyond India, with building done here. If that holds, it is good news for engineering internships, and a hint that the first customer for an Indian AI product may sit abroad.

## AI in the wild in India

Real deployments showed up in the funding pages more than in press releases. CountAI, which raised ₹10 Cr in a seed round, builds camera systems that check product quality on factory floors, and its Knit-I product spots fabric defects on knitting machines at textile firms such as KPR and Indorama [StartupTalky](https://startuptalky.com/news/daily-indian-funding-roundup-key-news-17-november-2026/).

JohnAIC, which raised $1.9 million, sells AI servers that run in customers' own offices to banks, healthcare firms and public sector units [StartupTalky](https://startuptalky.com/news/daily-indian-funding-roundup-key-news-17-november-2026/).

Sarvam says its voice fine-tune of the new 105B powers Samvaad, its enterprise voice-agent platform across 12 Indian languages, and that most Samvaad bench examples come from loan collection and loan sales [Sarvam](https://www.sarvam.ai/blogs/sarvam-105b-1711). CtrlS says it serves nearly 40 Indian public and private sector banks, with hyperscalers its largest source of demand [AIM](https://analyticsindiamag.com/ai-features/inside-ctrlss-44-gw-bet-on-indias-data-centre-boom).

Humyn Labs collects its robot training data across over 20 countries, with India among its main hubs, and has 51 full-time employees, most in Bengaluru [TechCrunch](https://techcrunch.com/2026/11/18/accel-backs-indias-humyn-labs-to-supply-training-data-needed-by-u-s-robotics-ai-developers/). Disseqt has partnered with Infosys, Cognizant, HCLTech, Mphasis and Tata Technologies as global system integrators to deploy its platform for their enterprise clients [Inc42](https://inc42.com/buzz/ai-startup-disseqt-ai-raises-8-mn-to-scale-international-operations/).

## Opportunities: open now

{% include opportunities-top5.html %}

- **CERN Summer Student Programme 2027** - for Bachelor's or Master's students in Physics, Engineering, Computer Science or Mathematics with at least 6 semesters completed by the start of summer, deadline not stated on the page, so check the listing soon [CERN](https://careers.cern/programmes/summer-studentship/).
- **What CERN pays** - the page lists a 94 CHF per calendar day net subsistence allowance, health insurance and a contract of 8 to 13 weeks, and asks for a CV, academic reference letter, enrolment certificate and transcripts [CERN careers](https://careers.cern/programmes/summer-studentship/).
- **ChatGPT for Academic Researchers, India** - for research faculty and postdocs with an arXiv, bioRxiv or ChemRxiv paper from the past three years, applications open Monday, November 30, first-come, first-served [Digital Terminal](https://digitalterminal.in/ai/openai-offers-free-chatgpt-plus-access-to-indian-researchers-under-global-initiative).
- **What the grant gives** - three ChatGPT Plus seats in a research workspace, free for 12 months, covering the recipient and up to two collaborators, from 50,000 new grants globally [Digital Terminal](https://digitalterminal.in/ai/openai-offers-free-chatgpt-plus-access-to-indian-researchers-under-global-initiative).

**My read:** Students cannot apply for the OpenAI grant, but a professor you already do research with can, and the third seat is meant for a collaborator. Ask this week, so the application is ready when the window opens on 30 Nov.

## Ideas for India

**A Samvaad-style eval harness for your own agent.** Sarvam's Samvaad bench has 338 next-turn evaluations in English and 12 Indian languages, often code-mixed, mostly from loan collection and loan sales [Sarvam](https://www.sarvam.ai/blogs/sarvam-105b-1711). Every NBFC and fintech running a voice bot needs the same thing for its own scripts.

**My read:** Build a small open-source tool this semester that turns a company's call transcripts into rubric-checked next-turn tests and runs them against any OpenAI-compatible endpoint. Collections teams would pay for the regression reports, and it is a strong portfolio piece for Sarvam-adjacent internships.

**A rupee cost router across India-hosted endpoints.** Token Factory prices in rupees per million tokens with separate Interactive and Standard endpoints for DeepSeek V4.1 Flash [Sarvam](https://www.sarvam.ai/blogs/sarvam-token-factory), and E2E Networks' Blaze serves overlapping open models through a single API [Business Standard](https://www.business-standard.com/technology/artificial-intelligence/explained-sarvam-ai-s-token-factory-and-debate-over-ai-sovereignty-goals-126112000685_1.html). Startups with data-residency needs have to pick between them by hand.

**My read:** A thin proxy that logs latency, cost and retention terms per request and routes by budget is a weekend prototype and a semester product. Indian SaaS teams selling to banks are the buyers.

**Consent tooling for physical-AI data.** TechCrunch notes that recording people inside their homes for robot training data has raised questions about privacy and consent [TechCrunch](https://techcrunch.com/2026/11/18/accel-backs-indias-humyn-labs-to-supply-training-data-needed-by-u-s-robotics-ai-developers/). Collectors selling to US labs will need consent records that survive a buyer's audit.

**My read:** A consent-and-redaction pipeline (face and screen blurring, signed consent tied to each clip) is a good computer-vision course project with a paying customer at the end of it.

## Sources and verification

This issue cites 113 pages fetched between 2026-11-16 and 2026-11-23; every link above opens the page its sentence came from. Dropped for lack of proof: 6 items - Microsoft raising Indian cloud prices 15.7% (outside the window, published 15 Nov); Science Academies SRFP 2027, ETH Zurich summer fellowship, Purdue SURF 2027, Scale AI ML research intern and the Claude Code /loop changelog (already covered in an earlier week). Links that answered 403 or timed out when re-checked: none among the links above. Full logs: [verified.json](https://github.com/j-jain/Ai-news/blob/main/work/2026-W47/verified.json), [fact-check](https://github.com/j-jain/Ai-news/blob/main/work/2026-W47/factcheck-india.json), [dropped](https://github.com/j-jain/Ai-news/blob/main/work/2026-W47/dropped.json).
