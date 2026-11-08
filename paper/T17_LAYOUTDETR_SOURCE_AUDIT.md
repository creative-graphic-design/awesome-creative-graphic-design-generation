# T17: LayoutDETR original method and evaluation audit (2026-11-08)

**Source:** [arXiv original full-text HTML](https://arxiv.org/html/2212.09877), §§3–5.3, Supplement B–C, Tables 1–4, and [ECCV 2024 publisher listing](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3022_ECCV_2024_paper.php). No PDF screenshot/figure-panel review was needed for this HTML-first pass.

**Representation and conditions.** The generative-conditional DETR predicts box center, height and width from supplied background images and foreground images plus caption text, text roles and text lengths. Its final compositing in a graphical interface is a render of that layout. It does not establish an exported fully editable text-source document or semantic editing benchmark.

**Original experimental population.** In §5 the authors report 7,196 ad banners in their own dataset, 59,978 valid CGL Chinese ad banners, and 32,063 CLAY mobile UI examples with 90/10 training/testing. Multimodal preprocessing includes OCR-extracted source texts and text-free background recovery by inpainting, which affects fair comparison to methods lacking those modalities. Six baselines are adapted with additional encoders where needed.

**Original human study.** In §5.3, 308 ad banners are rendered as paired alternatives; three AMT workers evaluate each pair, answering which *rendered design looks better*, without an explicitly specified aesthetic criterion. Table 4 is a preference matrix. This is **not** user efficiency, controlled post-export text editing, or a protected-object preservation test.

**Numerical limit.** The HTML rendering of the original Table 3 exposes the metrics and method labels, but its numerical cells are not available from the retrieved text. This audit **does not promote** specific LayoutDETR metric values or global rankings from secondary summaries. The paper's own method and evaluative setup are inspected, but independent reproduction and supplemental data verification are not complete.

**Citation audit:** `layoutdetr2024` promoted from `not_verified` to `methods_results` solely for source-verified methodology, dataset sizes, study protocol and outcome types. `editability_audit=not_verified` and `adjudication_status=pending` remain unchanged. LayoutFormer++ was separately confirmed only against the original CVPR publisher abstract and kept at `abstract_index`, because no original quantitative table was checked.
