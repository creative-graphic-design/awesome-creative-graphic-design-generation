# T19: Original layout, layer, typography and poster evidence — 2026-11-08

These source-specific checks inspected original arXiv HTML or primary supplementary author HTML. They do not establish independent replication, the completeness of a systematic search, a native editor round-trip, or scientific author approval.

## CGD-025 — `layoutnuwa2024`

Primary source: [original author HTML](https://arxiv.org/html/2309.09506).

Original locator: Original sections 3.1-3.2 and 4.1-4.3; Table 1.

Original full-text methods/results inspected 2026-11-08. LayoutNUWA uses code instruction tuning for LLM-predicted layout boxes and tests layout generation/completion across layout datasets. Layout box placement is not an evaluated operation on text or imagery in a saved native graphic-design document.

## CGD-048 — `posterllava2026`

Primary source: [original author HTML](https://arxiv.org/html/2406.02884).

Original locator: Original supplementary HTML Appendices A-B (GPT-4o rating and human evaluation prompts).

Original author supplementary evaluation methods inspected 2026-11-08; accessible source primarily contains the appendix. Main original numerical results and tables were not independently checked. Source depth is bounded to the original supplementary experiment protocol, not a validated quantitative superiority or native edit success.

## CGD-077 — `posterverse2026`

Primary source: [original author HTML](https://arxiv.org/html/2601.03993).

Original locator: Original method Blueprint Creation and Unified Layout-Text Rendering; experiment Table 1; appendix Tables 8-9.

Original HTML methods/results inspected 2026-11-08. PosterVerse uses HTML-based scalable typographic rendering to build posters. Original main Table 1 reports character-recognition 92.33%, text F1 78.58%, FID 62.54 under its own protocol; HTML typography rendering is not independent downstream editing success in a saved poster.

## CGD-085 — `layerdiffuse2024`

Primary source: [original author HTML](https://arxiv.org/html/2402.17113).

Original locator: Original sections 3.1-3.4 and 4.2-4.7, especially section 4.7 user study.

Original arXiv HTML methods/results inspected 2026-11-08. The latent transparency pipeline outputs compositable RGBA and multiple raster layers. Section 4.7 reports a transparency aesthetic preference study of 14 participants and 100 randomized prompt groups, not a test of editing semantic text, native document object IDs, or persistent file round trips.

## CGD-089 — `qwenimagelayered2026`

Primary source: [original author HTML](https://arxiv.org/html/2512.15603).

Original locator: Original sections 3.1-3.3, 4.3.1-4.3.3; Tables 1-3; section 4.4.2 qualitative layer editing.

Original HTML methods/result tables inspected 2026-11-08. Raster RGBA layer decomposition evaluates layer RGB, alpha overlap and reconstruction on Crello and AIM-500. Table 3 RGBA VAE PSNR 38.8252 and LPIPS 0.0123 versus LayerDiffuse 32.0879 and 0.0418 in this paper's matched protocol. Image layers are not semantically typed editable font objects, and depicted layer edits are qualitative.

## CGD-097 — `textdiffuser22024`

Primary source: [original author HTML](https://arxiv.org/html/2311.16465).

Original locator: Original sections 3.1-3.2, 4.1-4.3; Tables 2-3 and Figure 7.

Original full HTML methods/results inspected 2026-11-08. Character-level LM predicts text-line placement and diffusion renders the text pixels. Tables 2-3 examine tokenization and MARIO-Eval OCR/visual-text outcomes; Figure 7 multi-round layout chat is not an editor-native semantic font edit benchmark.

## CGD-118 — `paper2poster2025`

Primary source: [original author HTML](https://arxiv.org/html/2505.21497).

Original locator: Original sections 3.1-3.3, 4.1-4.3 and 5.1-5.4; original evaluation and runtime tables.

Original arXiv HTML methods/results inspected 2026-11-08. Paper-to-Poster defines source-paper content acquisition and visual poster generation evaluations while PosterAgent separates parsing, planning, rendering and critique. Source-content fidelity, visual quality, and later edit operations are different constructs; no common saved-document editing success protocol established.

The source-depth promotion for PosterLLaVa is restricted to its original supplementary evaluation protocol: no main-paper numerical experiment audit is claimed. None of the seven editing-audit fields was promoted.
