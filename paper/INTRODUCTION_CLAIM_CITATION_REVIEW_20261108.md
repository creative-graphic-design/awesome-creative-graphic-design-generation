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
- Introduction now uses 40 distinct BibTeX citations and 50 reference occurrences (as of this revision); citation count is descriptive and not a target.
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

## Complete Introduction evidence matrix (current cited keys)

The following matrix checks **all 40 distinct keys** used in Introduction against the existing `literature_citation_audit.csv`. Evidence-depth labels reflect the recorded ledger, **not** a new claim that we independently reviewed every complete source. `abstract_index` is insufficient to confirm detailed experimental results. **Counts:** abstract_index=16; methods_results=24.

| Citation key | Intro paragraph(s) | Claim this work is used to support | Ledger source depth |
| --- | --- | --- | --- |
| `huang2023survey` | P1, P5 | Graphic-design intelligence survey | abstract_index |
| `zou2025fragment` | P1, P5 | Graphic-design review (includes workflows) | methods_results |
| `mackinlay1986` | P1 | Graphical-presentation theory | abstract_index |
| `roth1994interactive` | P1 | Presentation-knowledge interaction | abstract_index |
| `jacobs2003adaptivegrid` | P1 | Adaptive document layout | abstract_index |
| `odonovan2014singlepage` | P1 | Learned page-layout design | abstract_index |
| `designscape2015` | P1 | Interactive layout suggestions | abstract_index |
| `posterlayout2023` | P1 | Poster layout and background context | methods_results |
| `cglgan2022` | P1 | Content-aware design layout | methods_results |
| `autoposter2023` | P1 | Advertising poster system | methods_results |
| `autopresent2025` | P1 | Presentation creation | methods_results |
| `pptagent2025` | P1 | Presentation creation and evaluation | methods_results |
| `deepslides2026` | P1 | Slide generation | abstract_index |
| `bizgen2025` | P1 | Text-rich infographics | methods_results |
| `gupta2026layercanvas` | P1 | Hybrid infographic layers | abstract_index |
| `autofigure2026` | P1 | Scientific illustration generation | abstract_index |
| `scifig2026` | P1 | Scientific figures | abstract_index |
| `postergen2026` | P1 | Academic poster generation | methods_results |
| `tang2024designinterviews` | P2 | Practitioner interview evidence, not edit benchmark | abstract_index |
| `vinci2021` | P2, P4 | Human-assisted poster workflow | methods_results |
| `designdiffusion2025` | P2, P4 | Rendered design-image synthesis | methods_results |
| `postermaker2025` | P2, P4 | Product poster and text rendering | abstract_index |
| `textdiffuser22024` | P2 | Text rendering in raster images | methods_results |
| `layoutgan2019` | P2 | Element geometry, not full design doc | methods_results |
| `layoutdm2023` | P2, P4 | Layout generation/metrics, not native editing | methods_results |
| `vectorfusion2023` | P2, P4 | SVG synthesis/visual score | methods_results |
| `starvector2025` | P2 | SVG code generation | methods_results |
| `chat2svg2025` | P2 | SVG generation/refinement | methods_results |
| `cole2023` | P2, P3 | Layered design and qualitative editor demo | methods_results |
| `opencole2024` | P2 | Layered composition, not edit benchmark | methods_results |
| `designascode2026` | P2 | HTML/CSS design and structure | methods_results |
| `editablevisual2026` | P2, P3 | Code-native editable representations | methods_results |
| `layerd2025` | P2 | Raster-to-layer recovery, NOT layered generation | methods_results |
| `mildedit2026` | P3, P4 | Instruction-driven multilayer editing | abstract_index |
| `yang2026infoedit` | P3 | Infographic edit and reflow | abstract_index |
| `svgeditbench2024` | P4 | SVG editing benchmark | methods_results |
| `vectorgym2026` | P4 | SVG editing task benchmark | methods_results |
| `shi2023layoutsurvey` | P5 | Layout survey | abstract_index |
| `tian2024vectorsurvey` | P5 | Vector survey | abstract_index |
| `malashenko2025svgreview` | P5 | LLM SVG generation/editing review | methods_results |

### Contrast validation

1. **Raster production versus structured generation**: DesignDiffusion, PosterMaker and TextDiffuser-2 support rendered-image synthesis/text claims; LayoutGAN/LayoutDM concern element geometry; VectorFusion/StarVector/Chat2SVG concern vector paths; COLE/OpenCOLE concern layered synthesis; DesignAsCode/Editable Visual Design concern code-oriented artifacts.
2. **Raster recovery is a separate problem**: LayerD decomposes an existing flattened design. It must not be cited as if it directly synthesized a new layered composition from a design brief.
3. **Affordance versus empirical editing**: COLE/Editable Visual Design indicate manipulable output possibilities; MiLDEdit, SVGEditBench and VectorGym address designated editing tasks. Neither property licenses a generic native-editing success claim.
4. **Evaluation contrast has both sides**: DesignDiffusion/PosterMaker provide image-generation evidence, LayoutDM/VectorFusion provide structure/generation evaluation, Vinci addresses user effort, and editing benchmarks address editing tasks. These scores must not be combined without matched tasks and protocols.
5. **Prior surveys**: Zou covers graphic-design workflows, and Malashenko includes SVG editing. The distinct aim of R–E–V is to cross-reference output representation, allowed operations and measured evidence, not to claim editing has never been surveyed.

### Remaining original-source depth limitation

Exactly 16 cited entries remain at the ledger's `abstract_index` depth. The manuscript uses them here to support **paper scope, research task, or broad perspective only**, not original-paper numerical claims. If the claim is expanded to include method implementation or measured performance, consult the original full paper and update the evidence ledger first. No unsupported claim of a fully verified 40-paper original-experiment audit is made.
