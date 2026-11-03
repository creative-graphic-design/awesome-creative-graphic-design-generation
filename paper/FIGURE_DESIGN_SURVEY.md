# Survey figure design review and research-map redesign

Checkpoint: 2026-11-04 (JST). This review distinguishes **original figures visually inspected** from publisher/author summaries. It is a design study, not a corpus-screening result. The [SSII2024 technology map](https://shunk031.me/event/ssii2024-tech-map/) is a design reference to learn from, not trace or reproduce.

## Examples from the shunk031 Speaker Deck and original papers

1. **[Zou et al. (2025), From Fragment to One Piece](https://arxiv.org/pdf/2503.18641)**, presented in [Speaker Deck](https://speakerdeck.com/shunk031/from-fragment-to-one-piece-a-survey-on-ai-driven-graphic-design): visually inspected Fig. 1 (intent-to-design workflow) and Fig. 2 (three distribution charts). **Lesson:** give the conceptual pipeline and the empirical evidence different graphic roles. Do not reuse the publication histogram without reproducible denominators.
2. **[Luo et al. (2025), Large Language Model Agent](https://arxiv.org/pdf/2503.21460)**, presented in [Speaker Deck](https://speakerdeck.com/shunk031/large-language-model-agent-a-survey-on-methodology-applications-and-challenges): visually inspected Fig. 1, p. 2. Four color-coded panels explain a technical ecosystem through small icons, subtopics and examples. **Lesson:** combine abstract organization and concrete objects on a single readable overview.
3. **[Zhang et al. (TMLR 2026), The Landscape of Agentic RL](https://arxiv.org/pdf/2509.02547)**, presented in [Speaker Deck](https://speakerdeck.com/shunk031/the-landscape-of-agentic-reinforcement-learning-for-llms-a-survey): visually inspected Fig. 1, p. 4 (hierarchical organization) and Fig. 2, p. 5 (fan-shaped paradigm transition). Fig. 2 combines color-coded regions, real system/tool logos and annotations; the fan shape itself carries the argument. **Lesson:** logos should serve a research contrast, not decorate a list.
4. **[Huang et al. (2023), A Survey for Graphic Design Intelligence](https://arxiv.org/pdf/2309.01371)**: visually inspected Fig. 1, p. 1 (compact representation/understanding/generation pipeline) and Fig. 2, p. 4 (actual artwork annotated with element-level and design-level explanations). **Lesson:** a real or clearly schematic design example is more intuitive than a purely abstract category list.
5. **[Shi et al. (2023), Intelligent Layout Generation Based on Deep Generative Models](https://doi.org/10.1016/j.inffus.2023.101940)**: the publisher explicitly describes Fig. 9 as a taxonomy across model architectures, content dependence and application. The **actual graphic was not visually inspected** due to restricted full-text access. **Lesson:** keep independent taxonomy dimensions visually independent.
6. **[Tian and Günther (TVCG 2024), A Survey of Smooth Vector Graphics](https://vc.tf.uni-erlangen.de/publications/Tian22TVCG/)**: inspected author publication description (mathematical representation plus creation/rasterization/vectorization stages); the **exact figure artwork was not inspected**. **Lesson:** associate categories with the artifact-creation pipeline rather than treating names as the content.

## Why our existing 67-label map is inadequate as the only overview

The current six-row, four-era TikZ research map is bibliography-traceable but is mainly a **date × application listing**. Missing channels include actual outputs, architectural developments, example edits, model-family distinctions independent of task, visible research argument, and verified institutional affiliations. It should remain as a detailed atlas, not the sole main-paper introduction figure.

The SSII2024 reference distinguishes a genuine year axis, model-family colored borders, task groupings, selected output thumbnails, venue citations, annotations of technical transitions and a legend. The correct lesson is a **multichannel visual grammar**, not simply adding more paper boxes or copying the layout.

## Proposed figure architecture

| Figure | Location | Information design | Scientific claim |
| --- | --- | --- | --- |
| **A. Visual workflow** | Main paper | Original examples: human brief → plan → composition → native artifact → edit; annotate which structure persists | Different representations have different editability affordances |
| **B. Narrative research map** | Main paper, full-width | 4 task lanes and ~20–30 audited representative works; x = chronology, lane = task, outline color = computational family, small icon = output format, selective logo = verified affiliation | Generative graphic design has expanded beyond layout prediction into integrated and revisable artifacts |
| **C. Detailed research atlas** | Supplement / high-res PDF | Retain 67 traceable milestones and enlarge after primary-source audit | Broad navigation and citation lookup, not a complete census or causal graph |
| **D. Editing contract** | Main paper | Same illustrative design in raster/SVG/layers/HTML or native deck with before/after edits, protected content, permitted reflow | Format support, qualitative edit demos and scored edits are not interchangeable |
| **E. Evaluation validity** | Main paper | Matrix of representations × task × target metric × native validity × human testing | Different benchmarks score different claims |

**Evidence controls:** No arrow should assert an influence/citation relationship without original-paper evidence. A broad progression arrow may be captioned as an author interpretation. Do not create paper-count plots before deduplication and retrieval logs exist. Do not use third-party result screenshots without attribution and a rights check.

## University / company logos: provenance before artwork

Default to **the lead author's affiliation at the date of the original publication**, with a second organization only where the source clearly documents a joint project. Show at most 6–10 official logos in the main map; the supplement may carry more. Every logo needs a documented authoritative asset URL and redistribution/attribution review. A verified affiliation **does not** imply permission to copy a trademark asset.

Fields for each logo candidate: bibtex_key, year, institution, affiliation_role, evidence_url, locator, official_logo_url, rights_notes, review_status. The [affiliation evidence CSV](figs/tex/affiliation_logo_provenance.csv) holds an initial set; no official logo artwork has yet been imported.

For example, original author blocks identify Beijing Institute of Technology and Adobe Research for LayoutGAN ([ICLR 2019 PDF](https://openreview.net/pdf?id=HJxB5sRcFQ)), CyberAgent for OpenCOLE ([CVPRW 2024 PDF](https://www.openaccess.thecvf.com/content/CVPR2024W/GDUG/papers/Inoue_OpenCOLE_Towards_Reproducible_Automatic_Graphic_Design_Generation_CVPRW_2024_paper.pdf)), and Microsoft Research Asia/Peking University on the [COLE project page](https://graphic-design-generation.github.io/). Do not extrapolate these to other works.

## Editable prototype and acceptance criteria

An **original standalone TikZ design storyboard** has been compiled locally, with 25 representative labels across 4 task lanes and small *schematic* output examples. It deliberately contains no official logos, copied paper figures, or alleged causal influence edges. It is a **concept PDF, not a replacement of the 67-paper audited map**.

To promote it into the main paper: (1) audit every node against BibTeX and source year; (2) map examples to input/output claims; (3) add approved source-aware thumbnails and verified institutional marks; (4) use a clear mutually independent encoding for task, model family, artifact and evidence; (5) render and visually inspect at the actual 17.5cm two-column print width; (6) retain the 67-label atlas and export both PDFs; (7) include a generated manuscript PDF in each user-facing update.
