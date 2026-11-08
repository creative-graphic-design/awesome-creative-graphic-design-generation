# Introduction claim–citation review (2026-11-08)

Scope: PR #135, `paper/sections/02_introduction.tex`. This review covers argument structure, claim–citation fit, and paragraph writing, not an exhaustive review of every study's experiments.

| Paragraph | Central claim | Evidence and limitations |
| --- | --- | --- |
| P1: background | Generation coordinates content and visual organization | Huang and Zou (communication); Mackinlay and DesignScape (historical presentation/design support); PosterLayout and CGL-GAN (poster placement); AutoPresent and PPTAgent (slides); BizGen (infographics); AutoFigure (scientific illustrations). These citations document heterogeneous tasks, not equivalent outcomes. |
| P2: workflow | For work requiring subsequent revision, initial appearance is insufficient | Tang documents designers' use of AI tools, Vinci tests interactive assistance; LayoutGAN and LayoutDM concern boxes, while COLE, OpenCOLE, Design-as-Code, and Editable Visual Design motivate representation differences. Practitioner interviews are not edit-success benchmarks. |
| P3: editability | Separately manipulable objects do not demonstrate reliable instruction editing | COLE and Editable Visual Design support format/workflow affordances; MiLDEdit studies multi-layer editing; InfoEdit assesses dependent reflow. Do not infer an export round-trip or measured editing accuracy from a demonstration. |
| P4: evaluation | Evaluation protocols answer non-interchangeable questions | LayoutDM (geometry/distribution); VectorFusion (visual/vector generation); Vinci (human efficiency); SVGEditBench, VectorGym and MiLDEdit (instruction-driven editing). Avoid an aggregate score across these protocols. |
| P5: survey niche | Existing reviews motivate a crosswalk between artifacts, operations and evaluation | Huang and Zou cover broad design intelligence; Shi covers layouts; Tian covers vector representation; Malashenko covers language-model SVG generation/editing. Zou already discusses creative workflows and Malashenko already covers editing, so novelty must be the explicit *crosswalk*, not a claim that existing surveys ignore either subject. |
| P6: contribution | R–E–V organizes the above into distinct evidence axes | An authored synthesis, not a claim of a new experimental ranking. |

## Paragraph-writing and scholarly-writing checks

- Each of six paragraphs opens with one bounded topic sentence; supporting sentences substantiate that sentence instead of starting a named-model review.
- Coherent progression: visual communication → revision in workflows → format affordances versus execution → evaluation heterogeneity → prior surveys → this survey's contribution.
- Introduction now uses 40 distinct BibTeX citations and 51 reference occurrences (as of this revision); citation count is descriptive and not a target.
- All cited keys were checked against `references.bib`; TeX source uses one prose sentence per line.
- The universal editability-importance claim was limited to workflows that require revisions. The too-strong prior-survey novelty claim was narrowed.
- The first-hand original records consulted include Huang (arXiv:2309.01371), Zou (J. Imaging 11(9):289), Mackinlay (ACM TOG 1986), Shi (Information Fusion 2023), Tian (IEEE TVCG 2024), Tang (arXiv:2406.13436), CGL-GAN (IJCAI 2022), AutoPresent and BizGen (CVPR 2025), AutoFigure (arXiv:2602.03828), Editable Visual Design (arXiv:2609.04034), SVGEditBench (CVPRW 2024), MiLDEdit (arXiv:2601.04589), VectorGym and InfoEdit (EMNLP 2026). Remaining key-to-claim matches rely in part on existing in-repository evidence records. This does **not** upgrade `not_verified` study records to full-text audited.

## Outcome

The Introduction's paragraph-level academic-writing and claim–citation review has been updated through the raster-versus-structured comparison. Citation coverage is subject to further source-level verification. Full methods/results verification of each cited study, live spreadsheet reconciliation, and survey-wide experimental-evidence review remain separate tasks. PDF visual QA is excluded here at the author's request.

## Required comparison and citation check for subsequent edits

- For every contrast such as raster versus vector, generative output versus document, or visual quality versus edit accuracy, identify the **evidence on both sides** before making a comparative claim.
- Check that the cited sources actually study the claimed output artifact or measurement; do not use an image generator as evidence for native editing, nor treat format-level affordances as measured edit success.
- Check for omitted research families (raster image synthesis, spatial layouts, vector paths, decomposed layers, code-native documents) whenever summarizing the breadth of generation approaches.
- After editing a supporting sentence, reread the complete paragraph and its topic sentence, then reevaluate claim scope and citation placement across all sentences.
- Source examples checked directly for the raster side: DesignDiffusion (CVPR 2025, direct design-image synthesis); PosterMaker (CVPR 2025, image/text product posters); TextDiffuser-2 (ECCV 2024, text rendering in images); LayerD (ICCV 2025, raster design decomposition into layers). This is evidence for the scoped claims in the Introduction, not a full independent replication.
