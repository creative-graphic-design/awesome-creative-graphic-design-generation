# T16: DeepSVG, SVGformer, VectorFusion primary paper audit (2026-11-08)

These are **bounded original methods/result-table checks**, not independent code execution, exhaustive supplemental review, scientific acceptance, or semantic editing benchmarks.

## DeepSVG — CGD-223

Original [NeurIPS 2020 paper](https://proceedings.neurips.cc/paper/2020/file/bcf9d6bd14a2095866ce8c950b702341-Paper.pdf), Sections 3–4, Table 1 (SVG command vocabulary), Table 2 (ablation) and Figure 5.

A hierarchy of paths, each described by MoveTo/LineTo/Cubic Bézier/ClosePath commands, supports SVG icon generation and interpolation. A ten-person study ranks 100 icon interpolation pairs: ordered hierarchical model first-place **44.8%**, Hungarian **25.8%**, one-stage autoregressive **9.7%**. Test reconstruction errors ordered **0.012**, Hungarian **0.017**, one-stage autoregressive **0.170**. Lower average rank is preferable: ordered **1.99** versus Hungarian **2.29** despite the misleading upward arrow on the original table header. No natural-language native document edit score.

## SVGformer — CGD-225

Original [CVPR 2023 paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Cao_SVGformer_Representation_Learning_for_Continuous_Vector_Graphics_Using_Transformers_CVPR_2023_paper.pdf), Sections 3–5, Table 2.

Operates directly on continuous SVG command parameters, with medial-axis segment annotations and geometric self-attention. Original Table 2: SVGformer/DeepSVG font reconstruction Chamfer **26.9/32.7**, icon reconstruction **6.3/15.6**; font-family classification **69.7%/35.2%**, icon classification **64.7%/45.1%**. The source explicitly identifies non-smooth interpolation and data sufficiency as limitations. This is representation learning, not an evaluated designer instruction-edit benchmark.

## VectorFusion — CGD-222

Original [CVPR 2023 paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Jain_VectorFusion_Text-to-SVG_by_Abstracting_Pixel-Based_Diffusion_Models_CVPR_2023_paper.pdf), Sections 3–5, Table 1.

Uses Score Distillation Sampling to optimize SVG path geometry; prompt evaluation uses **128 captions** and iconography experiments use **64 Bézier paths**. Table 1 CLIP L/14 R-Precision: VectorFusion scratch **76.6**, initialized from SD+LIVE at K=1 **78.1**, reranked K=4 **81.3**, while CLIPDraw scratch **85.2**. The latter directly optimizes CLIP and yields different visual styles. Evaluated text-caption retrieval and similarity do not verify editable native semantic text objects.

## Source-verification limits

All three original source PDFs were accessible through text extraction for method/evaluation tables. Requested web PDF screenshots failed, so figure image-level inspection is **not claimed**. `source_depth=methods_results` is restricted to the claims above. `editability_audit=not_verified` and `adjudication_status=pending` remain intact.

A distinct local CI issue found in the preceding paper commit: `check_manuscript.py` rejected PosterLayout because the newly added official DOI in BibTeX had not also been added to its acro entry. The acro DOI was synchronized in this batch.
