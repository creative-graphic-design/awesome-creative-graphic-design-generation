# T21: Product-poster and advertising-generation original methods/results — 2026-11-08

This review directly inspected the original author HTML for ten studies, including source-specific methods, dataset protocols and evaluation tables. These are original experiments as reported by the authors, not independent reproductions or proof of reusable semantic design-editing artifacts.

## CGD-059 — `autopp2025`

Original primary HTML: https://arxiv.org/html/2512.21921

Checked: Original Method: Automated Product Poster Generator and Optimizer; Experiments §§5.2-5.3, Table 1

Product poster generation jointly plans background, text and layout and optimizes feedback. Source Table1 AutoPP Sentence Accuracy 65.19 vs PosterMaker 57.87 and FID 43.19 vs 49.76, but CLIP-T 30.49 vs PosterMaker 30.43; authors' own metric and dataset. Measured output is poster raster, not the correctness of subsequent native document edits.

## CGD-065 — `designyourad2026`

Original primary HTML: https://arxiv.org/html/2605.12138

Checked: Original §§3.1-3.3, §§4.1-4.4 and §§5.2-5.3, Table 1

Unified autoregressive ad-image and ad-text token generation with product foreground image conditioning and multimodal preference cues; source Table1 reports Sentence Accuracy, NED, product similarity and image reward with several incomparable baseline capability columns. This measures ad quality and personalization, not a native layered editing benchmark.

## CGD-069 — `innoads2026`

Original primary HTML: https://arxiv.org/html/2603.05898

Checked: Original §§3-5.4, Tables 1-2 including efficiency ablation

Original Table2 InnoAds-Composer Stage II latency 47.32 seconds versus Flux-Kontext 76.02 seconds, FLOPs 135.25T vs 218.45T, memory 39.41G vs 55.29G in the authors' evaluated hardware setting. Original Table1 mixes visual text, foreground/background consistency and aesthetic scores, so latency improvement is not proof of all-metric superiority or a measured edit-command outcome.

## CGD-075 — `planningrendering2023`

Original primary HTML: https://arxiv.org/html/2312.08822

Checked: Original §§3.1-3.4, §4 dataset and §§5.1-5.4 quantitative and qualitative evaluations; Table 1 task distinctions

PlanNet predicts layouts and RenderNet generates image background, while a separate heuristically rendered text stage protects legibility. PPG task is joint product/text/background/layout generation with PPG30k dataset, unlike placement-only PLG. Source output is rendered poster artwork; later native edit operation success is not measured.

## CGD-079 — `refadgen2026`

Original primary HTML: https://arxiv.org/html/2508.11695

Checked: Original §§3.1-3.2 AdProd-100K, §§4.1-4.3 and §§5.1-5.5 including user study

Reference U-Net and generation U-Net transfer product identity into masked advertising scenes without per-product fine tuning; source study separately evaluates subject preservation and human preference. Reference-asset preservation in generated rasters is not editing an already delivered multi-layer source file.

## CGD-080 — `simpleposter2026`

Original primary HTML: https://arxiv.org/html/2605.08784

Checked: Original §3 subject-extension Table 1; §4.1-4.4; §5.1-5.6 quantitative benchmark

Original Table1 measures product subject extension under inpainting: FLUX-Fill base 41%, ControlNet conditioned 23.6%, LoRA-adapted 2.8%, full-parameter tuning 0.6% under the paper's test protocol. This is fixed-product region preservation during background generation, not post-export editing or independent native object-identity verification.

## CGD-082 — `reliablead2024`

Original primary HTML: https://arxiv.org/html/2408.00418

Checked: Original §§3-5.6, Tables 1-2 and supplementary human-involved experiment §9

RFNet inspection and recurrent feedback fine-tuning use availability/reliability rather than a generic designer editing metric. Source Table1 inspection F1 85.83 vs ViT 76.93 and AP 87.58 vs ViT 79.31; the source discusses reward collapse when availability rises while aesthetic diversity degrades. No post-export layer/edit success quantified.

## CGD-088 — `prismlayers2025`

Original primary HTML: https://arxiv.org/html/2505.22523

Checked: Original §§3.1-3.4, §4.1-4.2, Table 1 and Figures 3-5

Source Table1 reports PrismLayers approximately 200k synthetic multi-layer images, PrismLayersPro approximately 20k, each with 2-50 layers; source §3.1 reports average seven layers and median six, with 85% having 3-14 layers. These represent data composition, RGBA geometry and transparent-image aesthetics, not native text objects or quantified post-export edit instruction success.

## CGD-131 — `ecommercebanners2024`

Original primary HTML: https://arxiv.org/html/2403.05578

Checked: Original §3 methodology, §§4.1-4.2 human ratings, Table 4

Original human evaluation 24 participants rate 15 products on three-point image relevance. Table4 product-name-only baseline PNAME 2.413, LLM-generated chained prompts 2.077, product-type-only baseline 1.227; authors caution variability precludes a clear benefit of LLM prompts over simply using product names. Ratings concern image relevance, not editable document text or instruction edits.

## CGD-153 — `cg4ctr2024`

Original primary HTML: https://arxiv.org/html/2401.10934

Checked: Original §§3.1-3.4, §4.1-4.3, Table 1 online CTR evaluation

Original online deployed advertising CTR trial evaluates automated creative generation and impression-based click-through uplift in five product categories; Table1 aggregate first/second online uplift reported 10.4/9.7% vs without self-cycling 4.2/3.8%, though category-by-category dominance varies. CTR uplift is a commercial online response metric, not designer editing performance or protected-object preservation.

All records retain `editability_audit=not_verified` and `adjudication_status=pending` until editing-operation evidence and author screening are completed. CGD-061, CGD-081 and CGD-178 remain unpromoted because the exact original HTML results were not available in this pass. Training-time control and user preference are distinct from editability.
