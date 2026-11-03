# Manuscript author feedback and pre-commit review

**Read this file before drafting and again before each paper commit.** This is the durable record of prior author-review comments. Its qualitative criteria require author judgment; automated lint checks below cannot independently prove that the science or prose is correct.

## Introduction and research motivation

- [ ] Frame graphic design as visual communication and composed content, with authoritative survey citations near the definition. Avoid an unsupported slogan at the opening.
- [ ] Write **connected, natural scholarly prose**: graphic-design motivation → research advances → outstanding scientific gap → existing surveys → distinctive scope and contributions.
- [ ] Do not replace the argument with a bullet list of tasks, `Application tasks` / `Artifact and workflow` paragraph labels, or enumerated research questions in the Introduction.
- [ ] Name actual research tasks (posters, advertisements, presentation slides, infographics, scientific graphics, typography) with **task-specific original papers directly next to each claim**, not a single unrelated citation cluster.

## Literature and evidence

- [ ] Judge coverage by research lines and technical/empirical relevance rather than a raw citation target. The 225 provisional working records are not 225 thoroughly read or cited papers.
- [ ] For factual or numeric experimental claims, inspect original methods/results, relevant tables/figures and conditions. Keep `catalogue-only`, `abstract/index`, and `original methods/results examined` levels separate.
- [ ] Compare existing surveys in scope, structure, taxonomies, diagrams and what they cover. Do not claim prior work is silent on a topic without reading it.
- [ ] Source every task/method/evaluation claim to its actual paper; avoid overstating benchmarking, open-source state, artifact formats, model capabilities or study sample sizes.

## BibTeX and similar paper names

- [ ] Verify exact title, authors, year, venue and DOI from the original paper or publisher, preferably the published proceedings record, then retain a stable URL.
- [ ] Resolve preprint/published-version identity and possible title collisions. **LayoutDiffusion for graphic-layout generation and LayoutDiffusion for layout-to-image generation are different papers.**
- [ ] Run `python3 paper/scripts/check_bibliography.py`; eliminate missing/unused keys and placeholder authors. The script enforces structure, not bibliographic truth.

## Representation, editability and evaluation

- [ ] Keep generation-time control, structural/format affordance, qualitative editing demonstrations, human editing efficiency and quantitative editing evaluation **separate**.
- [ ] Do not infer post-export editability from a raster with reserved blank space, SVG paths, HTML/CSS, PSD layers or a user interface alone.
- [ ] Do not present FID, CLIP, Chamfer distance, a layout score and an instruction-edit success rate as one comparable scalar.
- [ ] Where editing requires dependent reflow, separate permitted neighboring changes from genuinely protected content.
- [ ] Describe what an original benchmark measures, the artifact it accepts/returns, and source-evidence limitations.

## Paper layout, anonymity and review

- [ ] Keep the author's actual identity out of review manuscripts. Use the official sample author block in source with `\\usepackage[review]{cvpr}`, which outputs an anonymous title block; **verify the rendered PDF**.
- [ ] Keep manuscript figures in `paper/figs/tex/` (editable TikZ and float wrappers) and the generated vector PDFs in `paper/figs/pdf/`. Keep complete table floats in `paper/tabs/tex/`. Do not duplicate float environments inline in section prose.
- [ ] Maintain captions, labels and citations after moving assets; compile the original figure PDFs from their TeX source and confirm visual quality.
- [ ] Refer to the manuscript simply as a graphic-design generation survey. Name the formatting template only when explaining its provenance.
- [ ] Do not copy prior survey figures without permission; do not invent a PRISMA selection flow or histogram before a reconciled, logged screening dataset exists.

## Required process before each commit

1. Re-read **this checklist** and the original papers needed for any changed scholarly claim.
2. Review the introduction's logic, adjacent task citations, figure/table references, metadata and empirical evidence tier.
3. Run `python3 paper/scripts/check_manuscript.py` and `python3 paper/scripts/check_bibliography.py`.
4. Run `cd paper && make pdf`; inspect the PDF and standalone figure PDFs, not only the LaTeX source.
5. After pushing, inspect the **Paper PDF** CI, its PDF/figure artifacts and any failure logs; update the PR with changes and remaining audits.

Install local hooks once at repo root with `uvx pre-commit install`. These hooks run the machine-checkable pre-commit gates for `paper/**`. **CI independently runs the same gates for every manuscript PR**, even if contributors did not install local hooks. This cannot replace manual scholarly review.
