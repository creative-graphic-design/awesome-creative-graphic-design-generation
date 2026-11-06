# T06 / CGD-103 — PosterText original-source audit

**Source checked on 2026-11-05:** original [arXiv:2608.16289v2 HTML](https://arxiv.org/html/2608.16289v2) Sections 3–4, Figure 3 and Tables 1–2, plus [arXiv version history](https://arxiv.org/abs/2608.16289).
**Source-version checkpoint (2026-11-06):** v1 was submitted **2026-08-17**, v2 **2026-08-18**, and v3 **2026-08-20**. The source audit first used v2. I have now directly compared the primary **v2 and v3 nine-page arXiv PDFs**, visually including **Table 1, Table 2, Figure 3, and the relevant methods/evaluation passages**. The tabulated scores and the audited task, representation, method, and metric definitions agree across these two versions. The PDF itself references further supplementary implementation details, but **no separate supplementary document has been independently retrieved or reviewed**. That narrower limitation, not the main-paper v3 comparison, remains open.
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
For the stated raster edit contract, set citation-level **methods_results**, **empirical_claim_audit=verified**, **representation_audit=verified**, **editability_audit=verified**, **evaluation_audit=verified**; retain the documented raster/native-output limits and the separately pending supplement review.
Update `postertext2026`, `postertext`, `postertextbench`, `postertext320k`, `sgsd`, both crosswalks, unresolved queue, validator and negative test.
**Expected:** 225 stable IDs / **202** cited references / **198** acro (27 abbreviations, 151 systems, 20 evaluation resources) / **173** linked / **52** unresolved (**2 P1 / 13 P2 / 37 P3**); public 207-paper catalogue **156 linked / 51 pending**.
These unmatched records remain pending, not excluded.
**Verified build/visual QA:** scientific source `729c2343ed94bba0d858b375f296c09fcb73a7e5` passed [Paper PDF #41997058915](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41997058915), **Awesome Lint** and **Catalog Check**. I downloaded the exact Paper PDF artifact **13401199657** (`survey-paper-eb247165469e5b12171de7af6734d3125f807166`) and extracted the **31-page anonymous CVPR-review manuscript**, the two standalone 26-/67-study vector maps and build log.
I rendered **all 31 pages** at overview resolution and inspected the research map in the manuscript (p. 3), the raster output boundary (p. 7), the four-stage method/PosterText-320K (p. 10), raster-edit results (p. 14), benchmark discussion (pp. 15–16), SGSD abbreviation (p. 18), PosterText source-linked `acro` index entry (p. 22), PosterText-320K and PosterText-Bench index entries (p. 24), and bibliographic reference **[99]** (p. 27).
I also rendered both standalone vector maps at **200 DPI** and inspected their labels and alignment. The TeX log contained no undefined citation/reference, acro warnings, or overfull/underfull box warnings; a programmatic word bounding-box inspection found **zero text words outside the 31 page rectangles**.
No evident overlap/clipping was found in the inspected figures, system entries or pages, and the first page visibly retains the anonymous CVPR-review header; PDF metadata has no author name. This is *artifact QA*, not an exhaustive high-resolution proof of every page, an independent experiment reproduction, or scientific author sign-off.
**Still required:** T04–T06 scientific author approval, retrieval/review of any separately available supplementary implementation material, and documented systematic multi-database retrieval before claiming review completeness; **T07 remains unstarted**.

## Supplement and public-artifact availability check (2026-11-06)

**Scope:** I revisited the [official arXiv v3 abstract/version page](https://arxiv.org/abs/2608.16289), [official v3 HTML](https://arxiv.org/html/2608.16289v3) and the already inspected [v3 main PDF](https://arxiv.org/pdf/2608.16289v3). I searched the exact paper title, arXiv ID, authors, **PosterText-320K**, and **PosterText-Bench** in public web results, including GitHub, Hugging Face, author/project-page leads, and public code finders. The main-paper *Implementation Details and Baselines* paragraph explicitly says more implementation details are in supplementary material. The HTML contents ends with **References** and presents no appendix or separately linked supplement; the nine-page PDF likewise contains no supplement.

**Result / evidence limitation:** I could **not identify an independently accessible, paper-matched supplementary PDF/appendix or an official PosterText code/data release** from the public surfaces inspected. This is **not** a proof that such materials do not exist or have never been published. The arXiv page offers **TeX Source**, but the source endpoint serves a compressed archive that the available web reader cannot open; a separate attempt to retrieve the source archive was unsuccessful. Therefore, the source-archive contents and any supplemental files within it **were not inspected**. Neither a related paper's similarly named codebase nor a third-party summary is acceptable as the PosterText supplement.

**Scientific consequence:** continue to cite the **verified v3 main-paper** Table 1/Table 2/Figure 3 and Sections 3–4 for the existing raster-edit classification; **do not mark supplementary hyperparameters, additional evaluation protocols, data licensing, annotation QA, model weights, or experiment reproducibility verified**. No TeX, BibTeX, numeric evidence tier, or 225-ID ledger change was justified by this availability check. Keep a specific *supplement not obtained* status, rather than claiming supplement parity or excluding PosterText. Recheck the official arXiv source and any author-designated release if a stable URL becomes available. **T04–T06 scientific author approval is separate and remains pending; T07 has not started.**

---

## Direct v2–v3 primary-PDF reconciliation (2026-11-06)

**Sources inspected:** [original v2 PDF](https://arxiv.org/pdf/2608.16289v2) and [original v3 PDF](https://arxiv.org/pdf/2608.16289v3), linked from the arXiv version history. Both have **nine pages**; their first pages identify `arXiv:2608.16289v2 [cs.CV] 18 Aug 2026` and `arXiv:2608.16289v3 [cs.CV] 20 Aug 2026`, respectively. I inspected both original **PDF page 7 (zero-based page 6)** as rendered images, not just external indexed extracts, to compare Table 1 and Table 2. I also inspected both **PDF page 5 (zero-based page 4)** for Figure 3, dataset construction, and the metric definitions, and read the v3 methods (PDF pp. 3–4). Thus the prior inability to access v3 in the 2026-11-05 audit is **resolved for the main paper**.

### Table 1: PosterText-Bench, same scores in v2 and v3

| Operation | PosterText (v3) | Comparison / important interpretation |
| --- | --- | --- |
| Patch addition | S.A. **0.763**, NED **0.899**, masked LPIPS **0.039**, instruction following **4.51**, visual quality **4.61** | Nano Banana 2: S.A. **0.500**, NED **0.635**, masked LPIPS **0.064**; this concerns raster output, not text-object editing |
| Patch deletion | masked LPIPS **0.040**, instruction following **4.70**, visual quality **4.78** | Nano Banana Pro: **0.061**, **4.66**, **4.91**; PosterText does **not** lead on visual quality |
| Patch modification | S.A. **0.771**, NED **0.902**, masked LPIPS **0.028**, instruction following **4.53**, visual quality **4.64** | Nano Banana 2: S.A. **0.819**, NED **0.907**, masked LPIPS **0.034**; PosterText preserves surrounding regions better but trails on target text |
| Poster generation | instruction following **4.21**, visual quality **4.46**, subject preservation **4.88** | Nano Banana 2: **4.63**, **4.76**, **4.86**; poster-generation scores must not be described as edit performance |

**Metric scope (v3 Evaluation Protocol and Table 1 caption):** S.A./NED apply to addition and modification text fidelity; masked LPIPS is computed over non-edited regions for the three editing operations; the VLM metrics assess instruction following and visual quality; poster generation adds a distinct subject-preservation metric. The original paper's table renders **best and second-best** per column, not an aggregate dominance claim.

### Table 2: training-stage ablation, same scores in v2 and v3

| Model / stage | S.A. | NED | Masked LPIPS | VLM instruction following | VLM visual quality |
| --- | ---: | ---: | ---: | ---: | ---: |
| Base Model | 0.490 | 0.666 | 0.417 | 3.27 | 3.37 |
| Stage II-only | 0.679 | 0.786 | 0.088 | 3.63 | 3.81 |
| Stage I (no curriculum) + II | 0.702 | 0.831 | 0.061 | 4.00 | 4.12 |
| Stage I + II | 0.712 | 0.866 | 0.053 | 4.03 | 4.24 |
| +SFT+RL | 0.735 | 0.883 | 0.037 | 4.22 | 4.51 |
| +SFT+RL+SGSD | **0.767** | **0.901** | **0.036** | **4.49** | **4.62** |

The Table 2 note specifies S.A./NED are averaged over **addition and modification**, masked LPIPS over **addition, deletion and modification**, and the VLM measures across **all four** tasks. Therefore **0.767** in Table 2 must not be substituted for the **0.763** in Table 1's addition-only result.

### Method, representation and availability boundary

- **Task and artifact:** v3 defines an image-valued `Iout = fθ(Iin, c, R)` and four instruction-controlled poster operations. Text-patch attributes are conceptual task variables; this does **not** imply model output as a native editable HTML, PSD, SVG, or live text-layer document.
- **Dataset and Figure 3:** **120K** editing and **200K** generation posters; OCR, image models and a VLM extract/construct patch records and HTML structure for training-pair synthesis. In both versions, Figure 3 places HTML in the **data pipeline**, not the model's output contract.
- **Four-stage method:** text rendering / patch reconstruction, instruction-following with mask-guided and mask-free samples, DiffusionNFT preference alignment (OCR/aesthetic/background rewards), and SGSD teacher–student distillation from mask-guided training to mask-free student inference. The v3 main text still gives LoRA and training-stage details. No material contradiction with the existing T06 method summary was found.
- **Supplement limitation:** the v3 **nine-page main PDF** ends with references and contains **no appendix or embedded supplement**. The methods section states that more implementation details are provided in supplementary material, but an independently accessible supplementary file was not verified here. Do **not** mark implementation-detail or supplement parity verified from main-paper tables alone, and do not infer exact sameness of every sentence/figure between the versions.
- **Editorial outcome:** keep T06's **quantitative instruction-guided raster text-patch editing** classification, methods-results evidence level, and original 225/202/198/173 source-stage counts. No TeX numerical claim, bibliography record, or source tier needed correction based on this comparison. **Author scientific approval is still pending** for T04–T06; **T07 remains unstarted**.
