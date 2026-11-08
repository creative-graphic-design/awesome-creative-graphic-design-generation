# T15: LayoutGAN, PosterLayout and OpenCOLE original-source audit (2026-11-08)

This document records bounded original-methods-and-results evidence, **not** systematic inclusion, independent model evaluation or native editor edit-operation success.

## LayoutGAN — CGD-022

- Original [ICLR 2019 OpenReview PDF](https://openreview.net/pdf/6bea64344b5868c50f04a043422f06436b39c251.pdf), Sections 3–4.3, especially Section 4.2 and Table 2.
- The input/output consists of sets of typed 2D elements and bounding-box geometry; a differentiable wireframe discriminator is trained to distinguish realistic alignment and overlapping.
- Original Table 2 on around 25,000 one-column training layouts with up to nine boxes and six classes: relation discriminator overlap **1.52%**, wireframe **1.17%**, real layouts **0.05%**; alignment **6.4%**, **3.4%**, **0.5%**, respectively.
- No native saved document, semantic text-editing outcome or controlled revision benchmark was examined.
- **Evidence limitation:** OpenReview PDF was available as extracted original text, but its screenshot request returned a cache miss. Tables were checked from the original extraction; image-level PDF inspection was not successful.

## PosterLayout — CGD-046

- Original [CVPR 2023 paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Hsu_PosterLayout_A_New_Benchmark_and_Approach_for_Content-Aware_Visual-Textual_Presentation_CVPR_2023_paper.pdf), Sections 3–5.3 and Table 2. The [CVF publisher entry](https://openaccess.thecvf.com/content/CVPR2023/html/Hsu_PosterLayout_A_New_Benchmark_and_Approach_for_Content-Aware_Visual-Textual_Presentation_CVPR_2023_paper.html) confirms pages **6018–6026**; proceedings DOI **10.1109/CVPR52729.2023.00583**.
- PKU PosterLayout comprises **9,974 poster-layout pairs and 905 image canvases**; its elements are text, logo and underlay bounding boxes. The model combines design-sequence formation with saliency-conditioned CNN-LSTM adversarial layout generation.
- Original Table 2 DS-GAN vs CGL-GAN: validity **0.8788 vs 0.7066** (higher better), overlay **0.0220 vs 0.0605** (lower better), loose-underlay **0.8315 vs 0.8624** (lower/worse), saliency occlusion **0.2088 vs 0.1546** (higher/worse), and unreadability **0.1874 vs 0.1715** (higher/worse). The table does not support a universal metric win.
- Evaluates layout location against visual content, not whether a complete source document survives controlled editing.
- **Evidence limitation:** the CVF PDF extraction and publisher metadata were inspected, but the web screenshot failed to load; the visual figure panels were not independently inspected.

## OpenCOLE — CGD-074

- Original [CVPR Workshops 2024 paper](https://openaccess.thecvf.com/content/CVPR2024W/GDUG/papers/Inoue_OpenCOLE_Towards_Reproducible_Automatic_Graphic_Design_Generation_CVPRW_2024_paper.pdf), Sections 2.1–2.3 and 3.1–3.4, Table 1.
- Trains on publicly available Crello designs (approximately **22k** templates), with a GPT-3.5 in-context JSON plan, SDXL image module for a *single* text-free visual canvas and LLaVA typography styling. Original COLE used separate image-generation modules for background and objects; OpenCOLE changes that part of the pipeline.
- Original DESIGNERINTENTION benchmark contains **200** prompts across six types. Five-axis GPT-4V Table 1 averages: OpenCOLE **6.3**, COLE **6.0**, SDXL **7.2**, DALL-E 3 **7.9**. OpenCOLE typography/color **5.6** vs COLE **5.7**. The image baselines do not output editable text and can omit text.
- The authors themselves warn about proprietary black-box GPT-4V evaluation and illegible text. Published reproducibility of code/data is separable from editing-operation success.
- **Evidence limitation:** CVF original text and table extracted and inspected; the screenshot request returned HTTP 403. No claim of PDF image-level visual inspection.

## Audit meaning

Each of the three citations was upgraded to `source_depth=methods_results` only for the bounded original methods, metric descriptions and results inspected here. `editability_audit=not_verified` and `adjudication_status=pending` remain unchanged because no held-out editor-operation benchmark, native round-trip or author approval is established.
