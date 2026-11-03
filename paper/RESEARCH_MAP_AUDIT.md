# Research map: selection, provenance and date policy

This is an **orientation figure**, not a systematic search result, a quantitative publication trend, or a map of verified citation/influence relationships. The current figure contains **67 selected milestones in six rows** (layout, posters, typography/vector, structured artifacts, document workflows, and reviews/evaluation). The extra document row makes slide generation/editing, infographic generation/editing, and scientific figures visible rather than subsuming them under posters.

## One label, one bibliography record

- The rendered diagram is `figs/tex/research_map.tex`.
- `figs/tex/research_map_sources.csv` connects **every displayed label** to the exact `references.bib` entry and chosen reference year.
- The manuscript checker compares the diagram, crosswalk, and BibTeX year, rejecting missing entries, duplicate displayed labels, or year/track disagreements.
- LayoutGAN++ is a **model described within** Kikuchi et al.'s 2021 *Constrained Graphic Layout Generation via Latent Optimization*, not an independent publication. Its map row points to `constraintlayout2021`. The original [paper](https://ktrk115.github.io/const_layout/files/mm21_const.pdf) and [author implementation](https://github.com/ktrk115/const_layout) both document this relationship.

## Reference year is not the first public date

The printed suffix (for example, `'24`) is **the year in the cited bibliography record**: ordinarily the publication year for conference/journal entries and the preprint year for preprint-only references. It is not a consistently verified first-public year. Several arXiv records were submitted earlier than their published-reference year:

| Map label | Cited year | arXiv identifier year | Source |
|---|---:|---:|---|
| LayoutTransformer | 2021 | 2020 | [arXiv:2006.14615](https://arxiv.org/abs/2006.14615) |
| BLT | 2022 | 2021 | [arXiv:2112.05112](https://arxiv.org/abs/2112.05112) |
| LayoutFormer++ | 2023 | 2022 | [arXiv:2208.08037](https://arxiv.org/abs/2208.08037) |
| LayoutDETR | 2024 | 2022 | [arXiv:2212.09877](https://arxiv.org/abs/2212.09877) |
| AnyText | 2024 | 2023 | [arXiv:2311.03054](https://arxiv.org/abs/2311.03054) |
| SVGDreamer | 2024 | 2023 | [arXiv:2312.16476](https://arxiv.org/abs/2312.16476) |
| LayoutNUWA | 2024 | 2023 | [arXiv:2309.09506](https://arxiv.org/abs/2309.09506) |

An arXiv identifier year is a useful version clue but is **not proof of the earliest dissemination date on all channels**. The review protocol separately calls for `first_public_date` and `venue_year` when the research register is fully adjudicated. The original diagram mixed these policies; this revision standardizes on the cited-reference year rather than silently implying first-public chronology.

## Interpretation and outstanding audits

Each paper is assigned one **primary visual row** for legibility, even when its contributions cross multiple tasks and representations. The evaluation row groups both technical benchmarks and research surveys; these are different kinds of evidence. Neighboring methods are not necessarily connected by citations or intellectual derivation.

The mapping check establishes **traceability and internal consistency**, not correctness of every original publication's metadata, not methods/results verification, and not 67 comprehensively screened studies. The bibliography's 144 cited works, the diagram's 67 selected labels, the public awesome catalogue, and the 225 provisional evidence-register entries are different sets. Do not compute a screening percentage or PRISMA diagram by dividing these counts. Before publication, verify uncertain metadata against proceedings, reconcile preprint/venue identities, audit critical experiments, and execute the planned search and deduplication protocol in `REVIEW_PROTOCOL.md`.
