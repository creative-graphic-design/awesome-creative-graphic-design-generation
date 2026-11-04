# T01 / CGD-091 — TAUE primary-source audit

Reviewed 2026-11-04 JST. Science review prepared; author sign-off and TODO completion remain pending. Do not begin T02 before approval.

## Identity and source provenance

- Working-register stable ID: CGD-091; verified Google Sheet row 92 in Evidence Matrix 225, Citation and R-E-V Coverage, Source Tier Reconciliation.
- Published work: Daichi Nagai, Ryugo Morita, Shunsuke Kitada, and Hitoshi Iyatomi, TAUE: Training-free Noise Transplant and Cultivation Diffusion Model, CVPR 2026 Findings, pp. 3749–3758.
- Official publisher record: https://openaccess.thecvf.com/content/CVPR2026F/html/Nagai_TAUE_Training-free_Noise_Transplant_and_Cultivation_Diffusion_Model_CVPRF_2026_paper.html
- Original paper HTML (version 2, dated 2026-03-17): https://arxiv.org/html/2511.02580
- Preprint first appeared 2025-11-04 (arXiv:2511.02580). Publication year 2026 and first-public year 2025 describe one work, not two publications.
- Project: https://iyatomilab.github.io/TAUE/ ; code: https://github.com/IyatomiLab/TAUE

## Original methods and experimental evidence inspected

| Claim | Original locator | Verification and boundary |
| --- | --- | --- |
| Mechanism | Sections 3.1–3.4, Figure 2 | Training-free three-stage generation: foreground, composite, background. Intermediate diffusion latents are transplanted, with cross-layer attention for semantic coherence |
| Output artifact | Section 3.1, Figures 1 and 4 | Separate foreground, background and composite images. The output contract is not a native editable HTML/PPTX document or semantic text objects |
| Evaluation data | Sections 4.1–4.2 | 1,770 filtered MS-COCO samples; SDXL, 50 denoising steps |
| Quantitative endpoints | Sections 4.2, 4.4 and Table 2 | FID, CLIP-I, CLIP-S for image generation and visual alignment; foreground/background PSNR, SSIM, LPIPS for layer reconstruction |
| Reported numeric results | Table 2 | Authors report unconditioned TAUE FID 60.53 versus LayerDiffuse 61.46; layout-controlled TAUE variant reports FID 55.59. Not independently replicated, and not a universal head-to-head editability ranking |
| Editing applications | Section 5 and Figure 6 | Qualitative demonstrations of object layout/scale control, multiple-object synthesis, and background replacement |
| Edit-operation scoring | Table 2 and Sections 5–6 | Not verified: these results do not establish held-out edit-instruction success, protected-object preservation rate or designer time/effort |
| Explicit caveat | Section 6 | Pixel-perfect foreground identity may underperform inpainting when unchanged visual details are essential |

## Decision and open questions

Include as a layered-asset-generation contribution. It is a useful scientific counterexample to treating reconstructed layers, qualitative background replacement, and quantitative editing accuracy as equivalent. Source evidence for generation method and measured endpoints is tied to Sections 3–6 and Table 2/Figure 6.

The paper's source experiments were read but not independently reproduced; the supplementary material was not exhaustively audited. Native semantic-object editing and post-export protected-object editing success are not established by these inspected experiments. Do not infer native editing guarantees from layer separation.

## Files and next step

This study adds one BibTeX entry (taue2026), one acro system (taue) and specific methods/evaluation discussion. The registered study ID is linked through arXiv identity; source locators are in the citation-level audit. The full 225-ID sheet snapshot remains unchanged; the unresolved queue drops from 58 to 57, and P1 from 8 to 7. All queue/crosswalk validators must be run before accepting the new baseline.

Author sign-off is required before T02 / CGD-092 / TKG-DM.

## Generated PDF verification (completed 2026-11-04)

Source commit `9545d800babd0235e6b512efe836bb19480a470a` passed Paper PDF, Catalog Check and Awesome Lint. I retrieved artifact `13335137547`: the anonymous manuscript has **29 pages**, and standalone 26/67-milestone maps are intact. I rendered and visually inspected p. 3 (map), p. 11 (first TAUE citation), p. 12 (evaluation metrics), p. 21 (full acro listing with cite/year/venue/representation and appearance pages), and p. 26 (original bibliography entry). The TeX log did not show an undefined control sequence, an undefined citation/reference or an overfull/underfull hbox warning. The paper and maps were exported for the author to review. T01 **author approval remains pending** before T02 begins.

## Continuation (2026-11-05)

The user subsequently instructed the manuscript work to continue, so T02 was started. This authorization to proceed is **not** an assertion that all scientific interpretations in T01 received individual author sign-off; its review checkbox remains open.
