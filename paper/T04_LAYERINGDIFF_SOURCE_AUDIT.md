# T04 / CGD-174 — LayeringDiff original-source audit

Reviewed **2026-11-05 JST** using the original [arXiv HTML](https://arxiv.org/html/2501.01197) §§3–5, Tables 1–4 and Figures 1–8. This is original-methods/results reading, not an independent replication or full supplementary-material audit.

## Identity and live-source reconciliation

- **Title:** LayeringDiff: Layered Image Synthesis via Generation, then Disassembly with Generative Knowledge.
- **Authors:** Kyoungkook Kang, Gyujin Sim, Geonung Kim, Donguk Kim, Seungho Nam, Sunghyun Cho.
- **Preprint:** [arXiv:2501.01197](https://arxiv.org/abs/2501.01197), first submitted **2025-01-02**; [author project page](https://kkang831.github.io/assets/publications/9993_ArXiv_LayeringDiff/). No independently verified accepted-venue DOI is asserted.
- Re-read live **Evidence Matrix 225 row 175 (CGD-174)**, **225 Citation and R-E-V Coverage**, **225 Source Tier Reconciliation**, and **Prior Survey and Screening**. Drive reports modification **2026-11-03T06:03:55Z**, earlier than the existing committed 2026-11-04 source-review snapshot. I did not re-date or modify the private workbook or committed source snapshot.

## Method, representation and editability boundary

Section 3 and Figure 1: generates an initial composite with an off-the-shelf image generative model (SDXL in its tests), determines a foreground using prompted Grounding DINO/SAM/ViTMatte and alpha matting, and decomposes this composite with a foreground/background diffusion decomposition (**FBDD**) and high-frequency alignment (**HFA**) module.
The delivered artifact is **foreground RGB plus alpha, background RGB, and a recomposited RGB image**.
Figure 7 demonstrates sequential recovery of multiple image foregrounds, while Figure 8 illustrates decomposition of existing real images.
The method does **not** supply native SVG/DOM/PSD text and design-object semantics or report controlled post-export edit instructions.
**Important:** the initial composite model is frozen, but **FBDD and HFA are trained on 20,000 synthetic composite images** (§3.4); classifying the whole pipeline as training-free is incorrect.

## Experiment evidence and limits

| Original locator | Observation | Boundary |
| --- | --- | --- |
| §4.1 and Table 1 | **572** foreground/background/composite prompt triplets at **768×768**; evaluate FID, KID, CLIP scores and detector/segmenter-derived FG-mIoU | Measures raster generation/disentanglement, not document edits |
| Table 1 | **Composite FID 121.05** versus LayerDiffuse T2L **134.51** (better); **foreground FID 133.76** versus **127.14** (worse) | No across-the-board superiority; baseline uses SD1.5 and initial LayeringDiff composite uses SDXL |
| Table 2 | Foreground longest-span mean **69.50** versus LayerDiffuse T2L **95.58**, with occupancy and spatial-center variation | Scale/position diversity, not editability |
| §4.1, Table 3 | **24** participants from the institution score **60 images each from 15 prompts** for text alignment and quality, 1–5; composite quality **4.07** versus T2L **2.97** | Human rendering preference, not completion time or instruction-edit success |
| §4.2, Table 4 | **1,000** synthetic composites; BG LPIPS **21.80** versus Germer **28.73** (better), but BG MSE **17.52** versus Germer **12.76** (worse; values table-scaled) | Pixel fidelity and perceptual reconstruction may disagree |
| §4.3 Figs 7–8 | Qualitative sequential decomposition and real-image decomposition | Not quantified native multilayer editing |
| §5 | Alpha prediction errors and residual shadows in background | Layer extraction reliability limitations |

## Decision and synchronization

**Include** as generation-then-decomposition for layered raster synthesis; independently compositable layers do not prove success on semantic edits of document objects.
Citation-level record marks `source_depth=methods_results`, `empirical_claim_audit=verified`, `representation_audit=verified`, `evaluation_audit=verified`, and **`editability_audit=not_verified`**.
New `layeringdiff2025` source-linked `layeringdiff` system, generic KID abbreviation and original-paper FG-mIoU evaluation resource are introduced in `acro`.
Updated manuscript representation, methods, evaluation, bibliography, citation-level audit, both private/public crosswalks, unresolved queue, negative validator fixture, and checklist; no source-tier promotion was inferred merely from identity matching.
**Checkpoint: 225 frozen records; 200 references; 193 acro (26 abbreviations, 149 systems, 18 evaluation); 171 linked; 54 unresolved (4 P1/13 P2/37 P3).**
**Still pending at source commit:** all CI, actual PDF and research-map QA, full supplementary inspection, independent reproduction, and author scientific sign-off.
Next only after review: **T05 / CGD-184 / UniWorld-Design**.
