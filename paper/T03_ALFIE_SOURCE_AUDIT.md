# T03 / CGD-159 — Alfie original-source audit

Reviewed **2026-11-05 JST**. This is an original-methods/results review, **not** code replication or an exhaustive supplement audit.

## Identity and source

- Authors: **Fabio Quattrini, Vittorio Pippi, Silvia Cascianelli, Rita Cucchiara**.
- Canonical published title: *Alfie: Democratising RGBA Image Generation with No $$$*.
- [arXiv:2408.14826](https://arxiv.org/abs/2408.14826), submitted **2024-08-27**; [original HTML §§3–5.1](https://arxiv.org/html/2408.14826).
- Accepted at **ECCV 2024 AI for Visual Arts Workshop and Challenges**.
- Published **2025-05-12** by Springer in *Computer Vision -- ECCV 2024 Workshops*, LNCS vol. **15627**, pp. **38–55**, DOI [10.1007/978-3-031-92808-6_3](https://doi.org/10.1007/978-3-031-92808-6_3).
- **One contribution**, not two papers: the Sheet's workshop year is 2024; the BibTeX's publisher year is 2025 with the original 2024 `eprint`.
- Read the live private sheet's *Evidence Matrix 225* **row 160**, *225 Citation and R-E-V Coverage*, *225 Source Tier Reconciliation*, and *Prior Survey and Screening*. Drive metadata: modified **2026-11-03T06:03:55Z**, preceding the committed 2026-11-04 snapshot review. We did not modify the private spreadsheet or silently refresh the snapshot date.

## Method, artifact and editability boundary

The method runs **pretrained PixArt-Sigma** and combines spatially masked foreground/background latents during inference to encourage whole-subject illustrations (**§4, Figure 3**).
It estimates an alpha channel from cross- and self-attention maps, then uses **GrabCut** for edge cleanup.
The delivered output is a **single RGBA raster foreground**. A designer can composite, position or opacity-adjust this image externally; the paper does not deliver an SVG, DOM, PSD object tree, a separately editable text layer, or native layout operations.
**Figure 7** demonstrates qualitative compatibility with Collage Diffusion, not a scored natural-language edit transaction.

## Experimental evidence and limitations

| Original locator | Direct finding | Boundary |
| --- | --- | --- |
| §5 setup | 3,000 prompts; four-pixel empty border and CLIP-S measurements | Border absence is a proxy for subject containment, not edit success |
| **Table 1** | All borders empty: **53.10%** PixArt-Sigma+suffix versus **96.50%** +centering; CLIP-S **30.79** versus **30.08** | Better border containment trades off slightly with text-similarity score |
| §5.1, **Figures 5–6** | **10 people**, **100 images**; Alfie preferred about **63%** versus ViTMatte | Image/matte preference, not editing time or edit locality |
| §5 evaluation | Authors **do not report RGBA FID/KID**, citing lack of suitable reference transparent images | Do not infer these from CLIP or borders |
| **Figure 7** | Compositional scene using Alfie foreground compared qualitatively with a stock-image subject | Not native object editability or a quantitative instruction-edit benchmark |

**Editorial decision: include** as text-prompted transparent-asset synthesis with downstream compositing affordance, **not** as quantitatively validated post-export design editing.
The citation-level record sets `source_depth=methods_results`, `empirical_claim_audit=verified`, `representation_audit=verified`, `evaluation_audit=verified`, and **`editability_audit=not_verified`**, because an editing protocol was not conducted.
No independent implementation reproduction or full supplement review is claimed.

## Synchronization and acceptance

Added `alfie2025` to BibTeX and `alfie` to acro, revised representation/method/evaluation prose, synchronized citation audit, private 225-ID and public 207-paper crosswalks, removed only CGD-159 from the *identity* review queue, and tightened CI with a new negative arXiv identity test.
The frozen 225 study rows are unchanged.
**New checkpoint: 225 IDs / 199 BibTeX / 190 acro (25 abbreviations, 148 systems, 17 evaluation resources) / 170 linked / 55 unresolved (5 P1, 13 P2, 37 P3).**
**Verified PDF acceptance on 2026-11-05:** The original scientific source commit `0e308af88cab61a2f98377620e07ae093b20f34e` passed **Paper PDF**, **Catalog Check**, and **Awesome Lint**. I downloaded the original [Paper PDF workflow run #41871516836](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41871516836) artifact **13345402864** (`survey-paper-94cfcdde4960e192c5fda946b6c7e4be2915c62b`; the name uses GitHub's test-merge SHA) and checked the real **29-page anonymous review PDF**. I visually rendered and inspected manuscript pp. **3, 7, 11–12, 17 and 27**, covering the map embedding, initial Alfie discussion, method/evaluation, the source-linked acro entry, and the bibliography. I also rendered and examined both independent **26-study narrative map** and **67-study detailed atlas** PDFs. In the pages and figures checked, I found no visible overlaps or clipped labels; the LaTeX log has no undefined-citation/reference, acro-warning, overfull or underfull box messages. This is *targeted visual QA*, not a page-by-page review or experimental replication. **Author scientific sign-off remains pending** before T04.
