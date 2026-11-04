# Manuscript author feedback and pre-commit review

**Read this file before drafting and again before each paper commit.** This is the durable record of prior author-review comments. Its qualitative criteria require author judgment; automated lint checks below cannot independently prove that the science or prose is correct.

## Introduction and research motivation

- [ ] Frame graphic design as visual communication and composed content, with authoritative survey citations near the definition. Avoid an unsupported slogan at the opening.
- [ ] Write **connected, natural scholarly prose**: graphic-design motivation → research advances → outstanding scientific gap → existing surveys → distinctive scope and contributions.
- [ ] Do not replace the argument with a bullet list of tasks, `Application tasks` / `Artifact and workflow` paragraph labels, or enumerated research questions in the Introduction.
- [ ] Name actual research tasks (posters, advertisements, presentation slides, infographics, scientific graphics, typography) with **task-specific original papers directly next to each claim**, not a single unrelated citation cluster.

## Sentence-oriented TeX and citations

- [ ] Put **one prose sentence per physical source line** in `sections/*.tex`, table prose and figure captions. Preserve blank lines between paragraphs. A normal source newline is whitespace in TeX: do not insert `\\` or `\\newline` merely to break a source line.
- [ ] Keep sections in a stable numbered sequence: `01_abstract.tex`, `02_introduction.tex`, ..., `10_conclusion.tex`; keep `main.tex` inputs in the same order.
- [ ] Use `\\citet{key}` for grammatical author references (e.g. `\\citet{huang2023survey}`) and `\\citep{key}` for parenthetical evidence. Never redundantly write `Huang et al.~\\citep{huang2023survey}`.
- [ ] Run `python3 paper/scripts/check_sentence_lines.py`. The conservative checker catches two or more sentences on one line and exempts common abbreviations, initials, TeX comments and non-prose TikZ statements. Its positive/negative unit tests run in CI.
- [ ] Review diffs at sentence granularity to make copy edits, attribution changes and merges easy to inspect. See [the reference repository's PR #89](https://github.com/shunk031/agentic-cognitive-writing/pull/89) for the analogous convention.

## Literature and evidence

- [ ] Judge coverage by research lines and technical/empirical relevance rather than a raw citation target. The 225 provisional working records are not 225 thoroughly read or cited papers.
- [ ] For factual or numeric experimental claims, inspect original methods/results, relevant tables/figures and conditions. Keep `catalogue-only`, `abstract/index`, and `original methods/results examined` levels separate.
- [ ] Compare existing surveys in scope, structure, taxonomies, diagrams and what they cover. Do not claim prior work is silent on a topic without reading it.
- [ ] Source every task/method/evaluation claim to its actual paper; avoid overstating benchmarking, open-source state, artifact formats, model capabilities or study sample sizes.

## Citation-level evidence audit

- [ ] Maintain a row in `paper/literature_citation_audit.csv` for **each cited BibTeX key**; never infer that the 225-entry provisional register has the same identity set as the manuscript bibliography.
- [ ] Keep `source_depth=not_verified` until the exact primary evidence and work identity are linked; a historical aggregate of methods/results reads is not evidence for a specific reference key.
- [ ] Record source section/table/figure locators before promoting any claim audit to `verified`. Distinguish original evidence from the bibliography's bibliographic metadata.
- [ ] Run `python3 paper/scripts/check_literature_audit.py` in local hooks and CI, alongside structural bibliography checks. This check enforces key alignment and evidence-state hygiene, not scientific correctness.

## acro citations, occurrence pages, and PDF deliverables

- [ ] Give every named-system `\DeclareAcronym` a `cite = {bibtex_key}` tied to its original work; use `cite/cmd = \citep` with first-use citations and do not misread group citations as experimental evidence.
- [ ] Enable `pages/display = all` to report every page where a named system or abbreviation appears, and inspect both printed acro lists in the generated PDF.
- [ ] After manuscript changes, build and inspect the updated anonymous PDF; **include the actual generated PDF and key figure PDF links in the user-facing response every time**, not only the GitHub PR or TeX source.
- [ ] Treat the public catalogue crosswalk (207 papers, 69 currently unresolved matches) as a conservative ID/title lookup, not an exclusion audit; run `python3 paper/scripts/check_catalog_crosswalk.py`.

## Comprehensive acro registry (2026-11-04)

- [ ] Keep three distinct `acro` tags: `abbreviations` for genuine short forms, `systems` for research models and systems, and `evaluation` for benchmarks, datasets and evaluation metrics.
- [ ] Require an original-paper `cite` key and `first-style=short` for every named system and evaluation resource; do not invent expanded model names.
- [ ] Convert ordinary prose mentions to `\\ac{key}` instead of populating the registry with never-used names; check appearance pages in the compiled list.
- [ ] Do not conflate identical model names from unrelated papers (notably two `LayoutDiffusion` studies and generation/editing uses of `ReLayout`); retain explicit bibliographic disambiguation.
- [ ] Preserve direct `\\citet` citations when referring to authors, and avoid duplicate `\\citep` next to a model's first automatic citation.

- [ ] Distinguish `LayoutGAN` from `Attribute-conditioned Layout GAN`, and treat `PDA-GAN` as a named model rather than expanding the embedded `GAN` token independently.

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
- [ ] For technology maps, show dated, cited research milestones on task-specific lanes; explain that neighboring boxes are not evidence of direct intellectual influence. Generate an **original** editable standalone TikZ PDF, and visually inspect label legibility.

## Required process before each commit

1. Re-read **this checklist** and the original papers needed for any changed scholarly claim.
2. Review the introduction's logic, adjacent task citations, figure/table references, metadata and empirical evidence tier.
3. Run `python3 paper/scripts/check_sentence_lines.py`, `python3 paper/scripts/check_manuscript.py`, and `python3 paper/scripts/check_bibliography.py`; run `python3 -m unittest discover -s paper/scripts/tests -p 'test_*.py'` to cover negative cases.
4. Run `cd paper && make pdf`; inspect the PDF and standalone figure PDFs, not only the LaTeX source.
5. After pushing, inspect the **Paper PDF** CI, its PDF/figure artifacts and any failure logs; update the PR with changes and remaining audits.

Install local hooks once at repo root with `uvx pre-commit install`. These hooks run the machine-checkable pre-commit gates for `paper/**`. **CI independently runs the same gates for every manuscript PR**, even if contributors did not install local hooks. This cannot replace manual scholarly review.

## CTAN acro package and technical vocabulary

- [ ] Use CTAN acro v3.8 (https://ctan.org/pkg/acro); use its tag property, not the deprecated class property. Do not use the glossaries package. Define entries centrally in `paper/acronyms.tex` with `\DeclareAcronym`.
- [ ] Use `\ac{key}` for first-use abbreviation expansion and subsequent short forms, `\acp{key}` for plurals, and `\printacronyms` for separate tag lists.
- [ ] Classify real abbreviations (GAN, VAE, LLM, VLM, SVG, PSD, FID, etc.) as `tag={abbreviations}` and named systems (LayoutGAN, COLE, DesignAsCode, etc.) as `tag={systems}`.
- [ ] Use `first-style=short` for named systems: their descriptive long field must NOT be misrepresented as a formally expanded name.
- [ ] Run the manuscript checker and PDF build, inspect both lists and first-use rendering, and confirm no obsolete `\gls` or `\newglossaryentry` remains.
- [ ] Print both groups with `display=all` and inspect the resulting PDF; acro defaults to displaying only used entries, which can otherwise produce an empty Abbreviations list.
