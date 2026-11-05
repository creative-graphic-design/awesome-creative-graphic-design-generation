# T05 / CGD-184 — UniWorld-Design original-source audit

**Original source:** [arXiv:2608.03971v1](https://arxiv.org/html/2608.03971), first submitted **2026-08-04**.
**Sections read (2026-11-05 JST):** §§3.2–3.6, 4.1–4.3, 5, Appendix B, Tables 1–4 and Figs. 2–7. This is source-section reading, not reproduction of training or complete supplementary audit.

## Source identity and live register

- **Title:** UniWorld-Design: From Pixel Generation to Layer-Native Design.
- **Authors:** Zongjian Li, Zhiyuan Yan, Chenxu Bai, Chen Chen, Haoxiang Sun, Shaodong Wang, Feize Wu, Shenghai Yuan, Bin Lin, Zheyuan Liu, Yuwei Niu and Li Yuan.
- **Status:** 2026 arXiv preprint; no independently verified peer-reviewed venue or accepted DOI.
- **Live workbook:** [Evidence Matrix 225](https://docs.google.com/spreadsheets/d/1PJtvX34FYoOnF8LS4-0WHpiR3B_KQ6n5fqRBtTeF3Zc/edit) row 185 / CGD-184, 225 Citation and R-E-V Coverage row 185, 225 Source Tier Reconciliation row 185, and Prior Survey and Screening.
- **Drive modified:** **2026-11-03T06:03:55.045Z**, preceding the documented 2026-11-04 source review. I re-read these live ranges and did not redraft/re-date the unchanged checked-in 225-row source snapshot.
- The old catalogue-source label and latest selected-methods source-recheck label are not identical. The new reference-level verification comes from direct original-paper inspection, not copying either label.

## Representation–editability–evaluation boundary

- **T2RGBA:** creates one transparent RGBA asset from text; the RGBA autoencoder and flow-matching-based model are trained and post-trained (§§3.2–3.3, 3.6).
- **I2L:** predicts ordered, complete semantic RGBA layers given a finished RGB image, global instruction and per-layer prompts; layer-instruction binding and layer-indexed positions preserve layer identities (§3.4, Fig. 3).
- **PSD training provenance:** original PSD layer trees supply supervisory targets including occluded pixels, top-level decomposition, recursive decomposition and targeted extraction (§3.5, Fig. 4). The paper does **not** report exporting a native editable PSD file or reconstructing native font/vector semantics.
- **Editing evidence:** Figs. 2/6 show compositing and sequential decomposition, but no controlled evaluation of post-export edit-instruction success, original-object preservation or designer completion time. Independently compositable raster layers are a format affordance.

## Original experimental contracts

| Source | Reported outcome | Limits |
| --- | --- | --- |
| §4.1, Table 1 | **512** held-out Crello designs, four layers, LayerD alignment; RGB L1 **0.1264 vs 0.2014**, Alpha Soft IoU **0.7325 vs 0.5454** (Qwen-Image-Layered) | Layer reconstruction after stack alignment, not edits |
| Table 2, Appendix B | Stable-Layers structural proxy Bad Layers **1.32 vs 1.69**, blank **0.13 vs 0.35** per design; Feature Distribution **0.690 vs 0.658** | Structural editability proxy, not operation success |
| Table 3, Appendix B | Five-axis VLM judge **20.43/25 vs 17.60/25**, with **worse** alpha cleanliness **2.90 vs 3.33** (Qwen-Image-Layered) | Model judge sees input, recomposition and layer contact sheet, not human editing |
| §4.3, Table 4 | T2RGBA **512** prompts; CLIP Score **33.03 vs 31.00** (OmniAlpha), but **worse** FID **117.14 vs 87.86** and white-composite LPIPS **0.537 vs 0.462** | No universal superiority; different performance constructs |
| §4.1 and Appendix B | FID/CLIP from **512** outputs, reference distribution **1,000** real layers; paired alpha/LPIPS metrics on **479** prompts with matched source layers | Denominators not interchangeable |
| §5 | Alpha-edge failures and missing/incorrect dense Chinese text glyphs | Native typography reconstruction is not demonstrated |

Appendix B identifies the VLM judge as **GPT-5.6-terra**. The Qwen-Image-Layered comparison uses the official recommended **640px** setting while UniWorld-I2L runs at **512-equivalent** area. These are the reported settings, not a controlled architecture-only ablation.

## Decision, sync and gates

**Include** CGD-184 as instruction-controlled layered **raster** synthesis and decomposition.
The citation audit records source_depth=methods_results, empirical_claim_audit=verified, representation_audit=verified, evaluation_audit=verified, and editability_audit=not_verified.
Source-level expected tally: **225 IDs / 201 BibTeX / 194 acro (26 abbreviation / 150 systems / 18 evaluation) / 172 linked / 53 unresolved (3 P1 / 13 P2 / 37 P3)**. The separate public catalogue is **155/207 linked, 52 pending**; unmatched does not imply exclusion.
**Pending after source change:** verify the current commit's Paper PDF/Catalog/Awesome CI, actual anonymous PDF and both standalone map PDFs. Independent replication and author scientific sign-off of T04/T05 are not completed; do not proceed automatically to T06.
