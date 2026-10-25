# Beat: open-local (edition: world; Indian open models are `both`)

**What this beat covers.** Open-weight and local AI: new open models (Qwen, Llama, Gemma, Mistral/Devstral, DeepSeek, Kimi, GLM, Phi, SmolLM, Sarvam, Nemotron, OLMo, speech and vision models), their licences, sizes and what the card says they need; the local-inference stack (llama.cpp, Ollama, LM Studio, vLLM, MLX, Unsloth) releases and features; quantisation results; benchmarks with method; what runs on an 8 / 16 / 24 / 32 GB laptop according to the model card or the runtime's docs; notable fine-tunes and datasets.

**What counts.** A model card, a GitHub release, a Hugging Face blog post, a runtime's changelog or docs, a benchmark page with its method. Reddit threads are unfetchable from here; do not cite them.

**What does not count.** Leaderboard screenshots on X, "runs great on my M2" anecdotes without a page, models without a licence.

## Seeds

- https://huggingface.co/blog (ok 25 Oct 2026)
- https://huggingface.co/api/models?sort=trendingScore&direction=-1&limit=20 (ok; JSON of trending models - then fetch each model's card page https://huggingface.co/<org>/<model> and cite the card)
- https://huggingface.co/papers (ok)
- https://ollama.com/search?o=newest (verify) - newest library models; cite the model's own page
- https://github.com/ggml-org/llama.cpp/releases (verify)
- https://lmstudio.ai/blog (verify)
- https://unsloth.ai/blog (verify)
- https://simonwillison.net/ (ok) - careful, dated write-ups of what new models actually do locally
- https://www.sarvam.ai/blogs (ok) - Indian open models go here too, as `edition: both`

## Search queries

- open weights model release <month year>
- new open source LLM <month year> Hugging Face
- GGUF 16GB laptop <model name>
- Ollama new model <month year>
- llama.cpp release <month year>
- local LLM benchmark <month year>
- Qwen OR Gemma OR Llama open model <month year>
- Sarvam open source model Hugging Face

## The "What runs on what" table (World edition)

Only models whose card or runtime page states sizes: parameter count, the quantised file size (e.g. "Q4_K_M 9.6 GB") or a stated memory requirement, and context length. Copy those numbers; never compute "so it fits in 16 GB" yourself - if the page does not say it fits, write the file size and let the reader judge. Each row needs the chip to the card.

## Notes

- Hugging Face model pages have the licence and the sizes in the Files tab; the card text is what the fetcher saves - quote from the card text.
- The trending API lists `createdAt`; use the card page for the publication date, or the HF blog post that announced it.
