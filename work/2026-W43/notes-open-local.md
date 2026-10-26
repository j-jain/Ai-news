# notes-open-local, week 2026-W43 (window 2026-10-19 .. 2026-10-25)

Result: 7 candidates written, 7 verified by `verify-quotes` (all Tier A, quote found by script, dates evidenced). All `edition: world`; no Indian open model fell in the window, so nothing is `both`.

Budget used: 8 of 8 WebSearch, 14 of 14 `CMD fetch` calls. I also made 2 plain `curl` status checks (HTTP code only, body discarded) on two guessed Unsloth URLs before spending the last fetch: `.../models/nvidia-nemotron-3.5-bolt` gave 404, `.../models/nemotron-3.5-bolt` gave 200 (that is the page I fetched). No Tier B / WebFetch was used.

## Items (id, page, published as the script set it)

| id | page | published | note |
|---|---|---|---|
| 46a3091cedc3 | MarkTechPost, Recursive Flint | 2026-10-21 | press; HF card is in secondary_urls (card has no date) |
| 2b9e0a635e7c | llama.cpp release b11870 | 2026-10-25 | date from page text "25 Oct 02:15" (no year shown) |
| f0c86e5012f8 | Unsloth DeepSeek-V4.1-Flash guide | 2026-10-19 | date = GitBook "Last updated 5 days ago" (a last-edit date) |
| c3063586601f | Unsloth Nemotron 3.5 Bolt guide | 2026-10-23 | date = "Last updated 1 day ago" (a last-edit date); source_type secondary |
| 35f57c1eaaf8 | IBM Granite Speech 5.0 2B card | 2026-10-19 (script) | card text says Release Date: October 20, 2026 |
| b0632526cd32 | NVIDIA Nemotron 3.5 Embed/Rerank/Parse (HF community article) | 2026-10-21 | json-ld |
| 2596ff929aee | HF blog, AnyLanguageModel 1.0 | 2026-10-20 | json-ld |

## Queries run (8 WebSearch)

1. (extended) new open weights model release this week October 2026 Hugging Face
2. (standard) Flint Recursive 39.8B mixture-of-experts coding agents open weights GGUF run locally
3. (standard) DeepSeek V4.1 Flash llama.cpp GGUF run locally RAM requirements
4. (standard, huggingface.co only) huggingface.co blog AnyLanguageModel 1.0 Granite Speech 5.0 Nemotron 3.5 Embed Rerank Parse
5. (extended) Recursive Flint announcement blog "Flint" 40B-A2.5B open-weight coding agent model release
6. (standard) Introducing Kimi K3.1 Pro Moonshot AI full model weights released by Nov 4 2026
7. (extended) "decision model" Liquid AI d3 Perplexity pplx-decider Cloudflare Clef Together tev1 ...
8. (extended) open-weight model released October 22 OR October 23 OR October 24 2026 Hugging Face Apache 2.0 OR MIT ...

Search summaries were used only to find URLs and leads. Nothing in an item rests on a search snippet.

## Fetches (14)

HF trending-models API (573f4e04a81a), HF blog index (0d95d58de1fe), Ollama newest (ff25755293f0), llama.cpp releases index (508712fbc8ca), LM Studio blog index (6cc256137fb2), Simon Willison home (a04fccc5d5ef), llama.cpp b11870 (2b9e0a635e7c), HF RecursiveSI/flint card (59f554d8046d), HF granite-speech-5.0-2b card (35f57c1eaaf8), MarkTechPost Flint (46a3091cedc3), HF Nemotron retriever post (b0632526cd32), HF AnyLanguageModel 1.0 post (2596ff929aee), Unsloth DeepSeek-V4.1-Flash guide (f0c86e5012f8), Unsloth Nemotron 3.5 Bolt guide (c3063586601f).

Already in pages/ before I started: the Sarvam blog index (11406abf86cd, fetched 15:02 on 25 Oct by someone else). I read it and did not re-fetch. Newest post is "Introducing Bulbul V4 Flash", 13 Oct; nothing dated in the window, so no Sarvam item.

## Could not fetch / not fetched

- https://huggingface.co/papers (seed): not fetched, budget.
- https://unsloth.ai/blog (seed, flagged unreachable in the beat file): not tried; two Unsloth docs pages loaded fine with status 200 instead.
- LM Studio blog loaded, but its newest post is 18 Sep ("Splash Engine ..."); nothing in the window. The LM Studio changelog is not a seed and was not checked.
- Recursive's own Flint blog post (linked as "Blog" from the HF card): URL never surfaced; not fetched.
- Moonshot's own Kimi K3.1 Pro page: search 6 found nothing on K3.1 Pro; not fetched.
- NVIDIA's own Nemotron 3.5 Bolt model card: URL unknown; I used the Unsloth guide instead (hence source_type secondary).
- LM Studio's Flint page (https://lmstudio.ai/models/recursivesi/flint) and Ollama's (https://ollama.com/library/flint): not fetched. A search summary said LM Studio states the smallest version needs "at least 24 GB of RAM" and Ollama's GGUF tags are about 23-26 GB. That is NOT in any item. The item uses MarkTechPost's figures (about 23 GB weights; Recursive recommends 48 GB). If the table wants a 24 GB row for Flint, fetch those two pages first.

## Seen but skipped, and why

Just before the window (published 13-18 Oct, so out of range; seen.json is empty so there is no follow-up route):
- Meta Muse Spark Open (816B total / 42B active, 1M context; research.meta.ai/blog/muse-spark-open, 15 Oct per search 1; on Ollama as cloud-only).
- NVIDIA Nemotron 3.5 Super VL (15 Oct), Tencent Hy-Memory-30B-A3B (15 Oct), inclusionAI Ling-3.1-flash (13 Oct), all from search 1 only.
- DeepSeek-V4.1-Flash-1017 itself: HF createdAt 2026-10-17 (trending JSON). Only its in-window follow-ons are items (llama.cpp support 25 Oct, Unsloth guide).
- Reflection Beam (501B; HF blog "Welcome Beam: a 501B open model you can own, customize, and scale" is dated October 16, 2026 on the blog index).
- MiniMax-M3.1-Flash (HF created 17 Oct; cloud-only on Ollama), Perplexity pplx-decider v1.2 (aicoder.com URL dated 20261017), Mistral Timestral-209M time-series model (HF created 14 Oct), black-forest-labs flux-3-image-klein-comfy (14 Oct).

Inside the window but no dated, citable page within budget:
- "Decision models" wave on Ollama's newest list (d3, d1, d1-omni, pplx-decider, clef, clef-flash, tev1, nimble-v3, strands-decider, kev, laya). Origin is pre-window (Forbes guide dated 12 Oct per search 7, Perplexity 17 Oct); Ollama's list is an index with no dates. Unsloth has a "Decision Models (Jev + Laya)" guide. A trend line is possible if someone fetches a dated primary page.
- Kimi K3.1 Pro (23 Oct). Simon Willison's home page (an index, so not cited) says it is "not yet open weights" and that Moonshot promised weights "by Nov 4, 2026". Not open yet, so out of scope this week; watch next week. The frontier-labs beat may cover the API launch.
- HF trending, created in window: XHToken/Spark-X2.6-4B (19 Oct, 4B), lodestones/Kromoss (19 Oct, image), ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF (23 Oct, 412k downloads, a new quant method), unsloth/flint-GGUF (20 Oct). HF cards carry no machine date, so I could not evidence them.
- Ollama newest list: bonsai-2 (Prism ML, ternary-weight vision models 2b/4b/9b/27b), mistral-large-4 (1.05T total / 52B active, cloud-only), phonon (Gradium TTS). No dates.
- HF blog index, in window, not fetched: "Granite Speech 5.0" post (21 Oct, same story as the card item), "Ensemble forecasting with IBM Granite time-series models" (22 Oct; relevant to Jai's forecasting work), "MPS in PyTorch 2.15" (20 Oct), "How Specializing the Vocabulary of SLMs Can Cut Inference Cost by 77% in Real Applications" (21 Oct), "Sort your prompts: a free speed-up for MoE batch inference" (about 19 Oct), OlmoEarth v1.3 (22 Oct), TorchTPU (20 Oct), TorchNeuron (19 Oct). NVIDIA's "Scaling Indic Pretraining: 2.8 Trillion Tokens ..." shows "9 days ago" on the index (about 16 Oct), so out of range.
- Unsloth Desktop (banner on every Unsloth docs page: "the first local app to run & train models"): no dated page.
- Minor llama.cpp builds on the index: b11871 (25 Oct, llama-server now answers 400 on JSON nested deeper than 128 levels, to stop crashes), b11868 (Hexagon NPU flash-attention split), b11861 (minimax-m3 NVFP4/MXFP8 scale fix).

## Odd things and caveats for the writer

- Granite card: the fetcher's `time datetime` is 2026-10-19 but the card text says "Release Date: October 20, 2026". `verify-quotes` overwrites the item's date with the metadata one (19 Oct). The claim says 20 Oct per the card. Both are in the window.
- Both Unsloth dates are GitBook "Last updated" stamps (19 Oct, 23 Oct), not first-publication dates. The DeepSeek guide (item 3) is about a model released 17 Oct; if the editor wants strictly new stories, drop it and keep the llama.cpp item (25 Oct), which lists it as a secondary URL. The two items are linked both ways.
- b11870: GitHub prints "25 Oct 02:15" with no year (it omits the current year). Year 2026 comes from the fetch date and build sequence. The page labels the build "Pre-release", as do the neighbouring builds on the index.
- Flint's HF card has no date anywhere in its text or metadata, so the dated cite is MarkTechPost (meta article:published_time 21 Oct). The HF API `createdAt` for RecursiveSI/flint is 2026-10-21T14:20:58Z (in the saved trending JSON, 573f4e04a81a), which agrees. All Flint benchmark numbers are Recursive's own. MarkTechPost notes dense Qwen 3.8 scores 73.0% on Terminal-Bench 2.1 versus Flint's 54.9%, and that Flint's SWE-bench Pro v2 score is not comparable with public SWE-Bench Pro. Context: card says 262,144 tokens, MarkTechPost says Recursive's blog cites up to 512k.
- Bolt guide: it says E4B is "an 8B parameter (4B effective)" model based on Gemma 4 E4B and states no licence anywhere (I grepped). Check NVIDIA's card before telling anyone the licence.
- DeepSeek size: Unsloth's page says "552B backbone + 196B Engram parameters". A search summary said HF metadata shows 763B total. I used neither as a total in any claim.
- Two search summaries (articles last updated Sept) said mainline llama.cpp had no deepseek_v41 architecture. Those predate b11870 and are superseded.
- The first heredoc attempt to write my build script failed in the shell wrapper; I rewrote it with the Write tool. The script (pre-checks every quote and every number in each claim against the saved text) is at D:/Temp/claude/C--Users-Jaidityaa-Jain-OneDrive-Desktop-Ml/ba4c84fd-365d-4ba5-9744-d90f06d712de/scratchpad/build_open_local.py.
- No fetched page contained text aimed at me. MarkTechPost's page has sponsored boxes ("Fund your AI agent's wallet ..."); ordinary ads, ignored.

## "What runs on what" rows available from these items (numbers copied from the pages; nothing computed)

| Model | Params | Stated size / memory | Context | Item |
|---|---|---|---|---|
| Flint (Recursive) | 39.8B total, about 2.5B active | 4-bit weights about 23 GB (INT4 MLX 22.6 GB; NVFP4 GGUF 22.9 GB); Recursive recommends 48 GB | 262,144 | 46a3091cedc3 |
| Nemotron-3.5-Bolt-E4B | 8B (4B effective) | Q4_K_M 6.18GB download; "roughly 4GB VRAM or 6GB RAM" | 64K | c3063586601f |
| Nemotron-3.5-Bolt-74B-A9B | 74B, 9B active | IQ2_XXS 22GB; "24-32GB RAM" | 128K | c3063586601f |
| DeepSeek-V4.1-Flash-1017 | 552B backbone + 196B Engram (Unsloth's words) | UD-IQ1_S 233.0 GB; 128-145 GB memory for 1-bit | 1,048,576 | f0c86e5012f8 |
| Gemma 4 E2B (GGUF) | n/a on page | about 3.4 GB at Q4_0 | n/a | 2596ff929aee |
| LFM2.5 2.6B (GGUF) | 2.6B | about 1.7 GB at Q4_K_M | n/a | 2596ff929aee |
| Qwen3.8 27B (MLX, 4-bit) | 27B | about 16 GB; "runs on a Mac with 32 GB of memory or more" | n/a | 2596ff929aee |
| Granite Speech 5.0 2B | 2B | no file size on the card | n/a | 35f57c1eaaf8 |

## If there were more budget

LM Studio and Ollama Flint pages (the 24 GB figure), Recursive's blog, the ISTA-DASLab GSQ-RCO GGUF card (quant method), HF blog "Ensemble forecasting with IBM Granite time-series models", HF blog "MPS in PyTorch 2.15", Moonshot's Kimi K3.1 Pro page, and a dated primary page for the decision-model wave.
