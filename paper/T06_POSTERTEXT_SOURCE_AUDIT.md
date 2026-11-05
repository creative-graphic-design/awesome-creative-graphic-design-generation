# T06 / CGD-103 — PosterText original-source audit

**Source checked on 2026-11-05:** original [arXiv:2608.16289v2 HTML](https://arxiv.org/html/2608.16289v2) Sections 3–4, Figure 3 and Tables 1–2, plus [arXiv version history](https://arxiv.org/abs/2608.16289).
**Important source-version qualification:** v1 was submitted **2026-08-17**, v2 **2026-08-18**, and arXiv records an updated **v3 (2026-08-20)**. The detailed results below were read from v2; v3 full-text table consistency and supplementary material have **not** been independently audited, so this remains a publication check.
No model replication, fresh annotator study or executed systematic database retrieval is claimed.

## Canonical identity and live register

- **Title:** PosterText: Towards Unified Visual Text Generation and Editing for E-commerce Poster.
- **Authors:** Xiaoan Liu, Lichen Ma, Zipeng Guo, Yu He, Xiaoyan Su, Shaojie Guo, Jingling Fu, Xiaolong Fu, Hao Yang, Tongxuan Liu, Yu Guo, Fei Wang, Xinyi Liu, Yongjun Zhang, Junshi Huang.
- **Status:** 2026 arXiv preprint; the arXiv-issued DataCite DOI is not an accepted proceedings record.
- **Source-of-truth workbook:** live [Evidence Matrix 225](https://docs.google.com/spreadsheets/d/1PJtvX34FYoOnF8LS4-0WHpiR3B_KQ6n5fqRBtTeF3Zc/edit), **row 104 / CGD-103**, plus row 104 of Citation and R-E-V Coverage and Source Tier Reconciliation and the Prior Survey and Screening tab.
- **Drive last modified:** **2026-11-03T06:03:55.045Z**, before the 2026-11-04 committed snapshot-review date. I re-read the actual Sheet rows without changing the frozen 225-row snapshot or artificially renewing its manifest.
- The historical `C: catalog-derived` / `paper_text_verified` labels do not automatically establish the citation-level evidence; the new audit statuses refer to the original sections inspected here.

## R–E–V: deliverable and permitted operations

The source's *Text Patch Generation and Editing* task treats a compositional region as a visual patch with text content, styling and placement, and supports **full poster generation**, **patch addition**, **patch deletion** and **patch modification** with optional reference-patch conditioning.
The original Section 3 presents text-rendering pretraining, instruction-following training, preference-aligned reinforcement learning, and **spatial guidance self-distillation (SGSD)** from a mask-conditioned teacher to mask-free inference.
**PosterText-320K** has **120K editing-task posters** and **200K generation-task posters**, with OCR/VLM-assisted patch extraction, text removal and HTML structure recovery used to form training instructions and before/after pairs (Figure 3).
The **HTML representation is in the data construction pipeline**, whereas the model delivers **rendered raster poster images**.
This distinction does not erase the method's genuine quantitative evaluation of **specified raster edit instructions**; it only restricts claims about *native* editable typography and document objects.

## Quantitative benchmarks and limitations

| Source | Original reported result | Boundary |
| --- | --- | --- |
| §4/Table 1, **patch addition** | Sentence Accuracy **0.763**, NED **0.899**, Masked-LPIPS **0.039**; Nano Banana 2 **0.500**, **0.635**, **0.064** | OCR-based text matching plus protected-region image difference, not native text-frame integrity |
| §4/Table 1, **patch deletion** | Masked-LPIPS **0.040**, VLM instruction following **4.70**, VLM visual quality **4.78**; Nano Banana Pro **0.061**, **4.66**, **4.91** | Background removal is scored but visual quality **does not** dominate the comparison |
| §4/Table 1, **patch modification** | Sentence Accuracy **0.771**, NED **0.902**, Masked-LPIPS **0.028**; Nano Banana 2 **0.819**, **0.907**, **0.034** | Lower background drift but **worse text fidelity** |
| §4/Table 1, **poster generation** | VLM instruction following **4.21**, visual quality **4.46**, subject preservation **4.88**; Nano Banana 2 **4.63**, **4.76**, **4.86** | New image generation, not patch editing or full supremacy |
| §4/Table 2, **training ablation** | Base sentence accuracy **0.490**, Masked-LPIPS **0.417**; all stages **0.767**, **0.036**, VLM I.F. **4.49**, V.Q. **4.62** | Text metrics average addition+modification; masked LPIPS averages three edit tasks, VLM scores all four |
| §3/Fig. 3, **automatic data** | **320K total posters**, 120K edit / 200K generation; patch descriptions and operation pairs automatically constructed | HTML annotations and automatically generated pairs do not guarantee original font recovery or manually validated labels |

The benchmark uses **OCR Sentence Accuracy and normalized edit distance** for addition/modification, **Masked-LPIPS in non-edited regions** for the three editing tasks, and a **VLM judge** for instruction-following and visual coherence.
Poster generation uses a different **VLM subject-preservation** measure; deletion has no applicable target-string score.
Neither the model nor benchmark reports native HTML/PSD/SVG export and post-export object edits, font-parameter editing, a controlled human productivity study, or independently calibrated VLM validity.

## Editorial decision and source-stage accounting

**Include** as **quantitative instruction-guided raster text-patch editing**, rather than either a native design-source editor or an unmeasured compositing affordance.
For the stated raster edit contract, set citation-level **methods_results**, **empirical_claim_audit=verified**, **representation_audit=verified**, **editability_audit=verified**, **evaluation_audit=verified**; retain scope limits and v3 recheck.
Update `postertext2026`, `postertext`, `postertextbench`, `postertext320k`, `sgsd`, both crosswalks, unresolved queue, validator and negative test.
**Expected:** 225 stable IDs / **202** cited references / **198** acro (27 abbreviations, 151 systems, 20 evaluation resources) / **173** linked / **52** unresolved (**2 P1 / 13 P2 / 37 P3**); public 207-paper catalogue **156 linked / 51 pending**.
These unmatched records remain pending, not excluded.
**Verified build/visual QA:** scientific source `729c2343ed94bba0d858b375f296c09fcb73a7e5` passed [Paper PDF #41997058915](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41997058915), **Awesome Lint** and **Catalog Check**. I downloaded the exact Paper PDF artifact **13401199657** (`survey-paper-eb247165469e5b12171de7af6734d3125f807166`) and extracted the **31-page anonymous CVPR-review manuscript**, the two standalone 26-/67-study vector maps and build log.
I rendered **all 31 pages** at overview resolution and inspected the research map in the manuscript (p. 3), the raster output boundary (p. 7), the four-stage method/PosterText-320K (p. 10), raster-edit results (p. 14), benchmark discussion (pp. 15–16), SGSD abbreviation (p. 18), PosterText source-linked `acro` index entry (p. 22), PosterText-320K and PosterText-Bench index entries (p. 24), and bibliographic reference **[99]** (p. 27).
I also rendered both standalone vector maps at **200 DPI** and inspected their labels and alignment. The TeX log contained no undefined citation/reference, acro warnings, or overfull/underfull box warnings; a programmatic word bounding-box inspection found **zero text words outside the 31 page rectangles**.
No evident overlap/clipping was found in the inspected figures, system entries or pages, and the first page visibly retains the anonymous CVPR-review header; PDF metadata has no author name. This is *artifact QA*, not an exhaustive high-resolution proof of every page, an independent experiment reproduction, or scientific author sign-off.
**Still required:** T04–T06 scientific author approval, detailed v3 Table 1–2/supplement reconciliation, and documented systematic multi-database retrieval before claiming review completeness; **T07 remains unstarted**.
