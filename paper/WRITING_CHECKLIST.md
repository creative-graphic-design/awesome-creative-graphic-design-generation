# Manuscript author feedback and pre-commit review

**Read this file before drafting and again before each paper commit.** This is the durable record of prior author-review comments. Its qualitative criteria require author judgment; automated lint checks below cannot independently prove that the science or prose is correct.

## Incremental review workflow

- [ ] Review [T01 TAUE original source audit](T01_TAUE_SOURCE_AUDIT.md) for source Sections 3–6, Table 2 and Figure 6. Keep generation/layer reconstruction scores separate from edit-instruction success and require author sign-off before T02.

- [ ] Work from [TODO.md](TODO.md) **one study at a time**, with an explicit per-study evidence record, decision, validator checks, PDF inspection and author sign-off before proceeding.
- [ ] Keep the current 225-ID triage backlog in `evidence_review_queue.csv`; don't duplicate all its rows in prose or treat an automatic match as a verified experiment.
- [ ] Keep the dated baseline in `TODO.md` synchronized with source records after each completed ticket. A passing CI validates the checked-in snapshot, not the private live Sheet.

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

## Mandatory spreadsheet and prior-survey audit before citation edits

- [ ] Read the live Google Sheet before every bibliography or literature-expansion commit: Evidence Matrix 225, 225 Citation and R-E-V Coverage, Prior Survey and Screening, and 225 Source Tier Reconciliation. Verify the exact tabs and source update time documented in EVIDENCE_REGISTER_RECONCILIATION.md.
- [ ] Refresh evidence_register_225_snapshot.csv from the real workbook when the Sheet changes. Refresh evidence_register_225_crosswalk.csv and per-paper working_register_id in literature_citation_audit.csv against BibTeX.
- [ ] Run python3 paper/scripts/check_evidence_register.py and its negative tests. CI must fail for missing CGD IDs, stale BibTeX matches, lost audit links, and an increase in unresolved records.
- [ ] Every needs_review row is an unresolved identity or citation-selection question, not an excluded study. Require primary-source evidence and a reason before changing inclusion status or source tier.
- [ ] Read the original prior-survey selection method and denominators before comparing survey size. Zou et al. (2025) describes a final selected set of 500 papers; its survey comparison table reports 267, which must be handled as a discrepancy, not a second selection count.
- [ ] After every manuscript change, review the actual compiled PDF and show a link; a passing bibliography test is not visual acceptance.

- [ ] For publication/preprint aliases, verify the original primary source and add its arXiv `eprint` to the existing BibTeX entry rather than creating a duplicate citation.
- [ ] When adding papers, update BibTeX, `acro`, relevant manuscript discussion, the 225-ID crosswalk, the public catalogue crosswalk, and citation-level audit in the same work cycle; preserve the original source-depth limitations.
- [ ] Keep the 30-day spreadsheet-review manifest current after **actually reading** the live Sheet, and run both the positive and negative crosswalk tests; never renew its date without checking the live workbook.

- [ ] Maintain `evidence_review_queue.csv` as an explicit **one-row-per-unresolved-study** backlog with the original source URL, task, evidence-tier note, manual review action and pending status. The evidence-register CI validator and negative tests must fail if a record disappears or its priority drifts.
- [ ] Review the 18 primary-source-labeled, 13 abstract-source-labeled and 37 catalogue-only unresolved records independently; these labels describe workbook history and are **not** automatically promoted proof of full-text review.

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
- [ ] Enable `pages/display = all` to report every page where a named system or abbreviation appears, and inspect all three printed acro lists in the generated PDF.
- [ ] After manuscript changes, build and inspect the updated anonymous PDF; **include the actual generated PDF and key figure PDF links in the user-facing response every time**, not only the GitHub PR or TeX source.
- [ ] Treat the public catalogue crosswalk (207 papers, 64 currently unresolved matches) as a conservative ID/title lookup, not an exclusion audit; run `python3 paper/scripts/check_catalog_crosswalk.py`.

## Comprehensive acro registry (2026-11-04)

- [ ] Keep three distinct `acro` tags: `abbreviations` for genuine short forms, `systems` for research models and systems, and `evaluation` for benchmarks, datasets and evaluation metrics.
- [ ] Require an original-paper `cite` key and `first-style=short` for every named system and evaluation resource; do not invent expanded model names.
- [ ] Convert ordinary prose mentions to `\\ac{key}` instead of populating the registry with never-used names; check appearance pages in the compiled list.
- [ ] Do not conflate identical model names from unrelated papers (notably two `LayoutDiffusion` studies and generation/editing uses of `ReLayout`); retain explicit bibliographic disambiguation.
- [ ] Preserve direct `\\citet` citations when referring to authors, and avoid duplicate `\\citep` next to a model's first automatic citation.

- [ ] Distinguish `LayoutGAN` from `Attribute-conditioned Layout GAN`, and treat `PDA-GAN` as a named model rather than expanding the embedded `GAN` token independently.

## Exhaustive list-first acro review

- [ ] For now, display **all registered entries** in the paper's three `acro` groups rather than selecting a small final-paper shortlist.
- [ ] Include the description, source citation, BibTeX reference year, available venue, paper URL, DOI and usage pages via `survey-rich`; keep bibliography metadata synchronized in CI.
- [ ] Keep the new `source` list citation distinct from `cite` on first prose use.
- [ ] Do **not** invent task, representation, venue, DOI, or experimental findings when the primary evidence or bibliography lacks them; optional source-grounded fields may be populated later.
- [ ] Inspect the complete PDF for long venues, citation-wrapping, link behavior, page number legibility and overall page count before curating the final index.

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
3. Run `python3 paper/scripts/check_evidence_register.py`, `python3 paper/scripts/check_sentence_lines.py`, `python3 paper/scripts/check_manuscript.py`, and `python3 paper/scripts/check_bibliography.py`; run `python3 -m unittest discover -s paper/scripts/tests -p 'test_*.py'` to cover negative cases.
4. Run `cd paper && make pdf`; inspect the PDF and standalone figure PDFs, not only the LaTeX source.
5. After pushing, inspect the **Paper PDF** CI, its PDF/figure artifacts and any failure logs; update the PR with changes and remaining audits.

Install local hooks once at repo root with `uvx pre-commit install`. These hooks run the machine-checkable pre-commit gates for `paper/**`. **CI independently runs the same gates for every manuscript PR**, even if contributors did not install local hooks. This cannot replace manual scholarly review.

## CTAN acro package and technical vocabulary

- [ ] Use CTAN acro v3.8 (https://ctan.org/pkg/acro); use its tag property, not the deprecated class property. Do not use the glossaries package. Define entries centrally in `paper/acronyms.tex` with `\DeclareAcronym`.
- [ ] Use `\ac{key}` for first-use abbreviation expansion and subsequent short forms, `\acp{key}` for plurals, and `\printacronyms` for separate tag lists.
- [ ] Classify real abbreviations (GAN, VAE, LLM, VLM, SVG, PSD, FID, etc.) as `tag={abbreviations}` and named systems (LayoutGAN, COLE, DesignAsCode, etc.) as `tag={systems}`.
- [ ] Use `first-style=short` for named systems: their descriptive long field must NOT be misrepresented as a formally expanded name.
- [ ] Run the manuscript checker and PDF build, inspect both lists and first-use rendering, and confirm no obsolete `\gls` or `\newglossaryentry` remains.
- [ ] Print all three groups with `display=all` and inspect the resulting PDF; acro defaults to displaying only used entries, which can otherwise produce an empty Abbreviations list.

## T02 original-methods/results checkpoint (2026-11-05)

- [ ] Preserve the original TKG-DM §3–7, Table 1 and Figure 10 evidence (CVPR 2025 / 2024 preprint); in SDXL its four listed scores do not surpass LayerDiffuse.
- [ ] Distinguish chroma-key RGB synthesis from independent alpha-layer export, native SVG/HTML/PSD objects and controlled editing success.
- [ ] Read CGD-092 in the **live** 225-study Sheet alongside prior-survey and source-tier tabs before changing source keys or evidence depth.
- [ ] Require the 56-unresolved CI ceiling and TKG-DM preprint identity negative regression test; do not exclude unmatched studies by default.
- [ ] Build and visually inspect the current PDF and both figure PDFs before advancing T03; keep author scientific review pending until feedback.

## P1 original-source expansion checkpoint (2026-11-04)

- [ ] Keep all 225 stable study IDs; re-run the citation join after adding source records and do not mark the remaining 58 unmatched IDs as excluded.
- [ ] Record each newly added study's original author/title/venue and abstract or introduction evidence before expanding BibTeX or source-linked acro fields.
- [ ] Never transfer previously recorded source tiers from the separate 225-study working register into a new citation-level audit without checking its original method/result locations.
- [ ] Update the actual bibliography, prose, original-source evidence, acro index, private/public citation crosswalk, unresolved queue and the CI regression ceiling in one work cycle.
- [ ] Build and inspect the actual PDF including all 185 acro entries, bibliography and both research maps; provide verified PDF links with each update.

## T03 Alfie methods/results checkpoint (2026-11-05)

- [ ] Preserve the distinction between a *single RGBA foreground raster* and an editable document with independently addressable design objects; downstream compositing is not edit-instruction accuracy.
- [ ] Keep Table 1's four-pixel empty-border criterion separate from CLIP-S, the 10-person/100-image (~63%) matting preference and the qualitative Collage Diffusion example.
- [ ] Do not invent RGBA FID/KID: the authors explicitly omit them because a compatible reference distribution is unavailable.
- [ ] Treat ECCV 2024 workshop/arXiv and 2025 Springer LNCS as one source; keep arXiv `eprint` and publisher DOI/volume/pages aligned.
- [ ] Ensure the 225-ID gate rejects regression above 55 pending and catches corrupt Alfie publication/preprint links; inspect actual PDF and figures before T04.

## T03 compiled output verification (2026-11-05)

- [x] At scientific source commit `0e308af`, [Paper PDF #41871516836](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41871516836), Catalog Check and Awesome Lint passed. I retrieved the **29-page** anonymous PDF and inspected Alfie representation, methods, evaluation, acro list, bibliography and both map figures; no visible overlaps/clips in inspected regions or unresolved citation/reference warnings in its TeX log.
- [ ] Preserve the author's **scientific approval gate** before starting T04 / CGD-174 / LayeringDiff. Compiled-PDF acceptance is not consent to scientific conclusions.

## T04 LayeringDiff source and figure acceptance (2026-11-05)

- [ ] Distinguish initial composite generation using fixed pretrained weights from training FBDD/HFA on 20,000 composites; never call the entire LayeringDiff pipeline training-free.
- [ ] Model output as foreground RGB plus alpha, reconstructed background RGB and recomposited RGB; sequential decomposition does not imply native text/vector document editing.
- [ ] Separate 572-triplet FID/KID/CLIP/FG-mIoU generation results (Table 1), scale/position diversity (Table 2), 24-person ratings (Table 3) and reconstruction on 1,000 synthetic composites (Table 4) from editing.
- [ ] Preserve counterexamples: worse foreground FID and worse background MSE despite improvements in composite FID and perceptual background LPIPS.
- [ ] Retain Section 5 failure modes (alpha estimation, shadows) and require actual PDF and map artifact inspection before T05.

## T04 compiled PDF acceptance (2026-11-05)

- [x] Scientific source `1750e184`: [Paper PDF #41944766288](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41944766288), Catalog Check and Awesome Lint passed; I inspected the genuine **30-page** anonymous PDF, KID/LayeringDiff/FG-mIoU index items, reference record, research map in the manuscript and both standalone map PDFs. No visible clipping/collision on inspected regions or unresolved citation/reference, acro and overfull/underfull box warnings.
- [ ] Do not treat PDF quality acceptance as author scientific approval. Preserve the review gate before **T05 / CGD-184 / UniWorld-Design**.

## T05 UniWorld-Design source and empirical-contract checks (2026-11-05)

- [ ] Distinguish PSD-derived **training documents** from **exported RGBA semantic raster layers**; do not assert native PSD, font, SVG, DOM or original-vector editability without evidence.
- [ ] Separate I2L Crello reconstruction (**512** designs, four layers) from T2RGBA image synthesis (**512** prompts, **479** reference-paired alpha/LPIPS cases).
- [ ] Treat Bad Layers / VLM scores as **proxies**; retain the worse alpha cleanliness **2.90 vs 3.33** and worse FID **117.14 vs 87.86** relative to the reported comparators.
- [ ] Enforce **53-unresolved** 225-study ceiling, a negative original-arXiv-ID test and human scientific-review gates.
- [ ] Inspect actual source-commit anonymous PDF and maps before reporting publication-quality acceptance; hold T06 pending approval.

## T05 actual PDF/map QA checkpoint — 2026-11-05

- [x] Source commit `fb1f41e` passed [Paper PDF #41989947985](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41989947985), Catalog Check and Awesome Lint after correcting stale count assertions in the negative-case test.
- [x] Downloaded exact artifact **13398466465**, inspected the 30-page anonymous PDF's original research map (p. 3), UniWorld-Design representation (p. 7), methods (p. 11), evaluation (p. 13), source-linked acro entry (p. 22), bibliography (p. 26) and both standalone 26-/67-study maps. No obvious layout collisions or unresolved citation/acro/box warnings in the checked regions and log.
- [ ] **Author scientific review remains separate from artifact QA.** Do not proceed to T06 / PosterText until T04/T05 scientific scope and evidence interpretation have been reviewed.

## T06 PosterText scientific and PDF gate (2026-11-05)

- [ ] Read original [arXiv v2 §§3–4, Tables 1–2](https://arxiv.org/html/2608.16289v2) and record v3 revision metadata separately; recheck whether v3 experiment numbers differ before final publication.
- [ ] Distinguish HTML-generated **training patch annotations** from the **raster poster output**; do not call the method native text-frame, SVG, PSD or HTML object editing.
- [ ] Preserve **quantitatively scored raster edit operations** for addition, deletion and modification: OCR Sentence Accuracy/NED, non-target Masked-LPIPS, VLM instruction/quality, with poster generation as a separate task.
- [ ] Keep Table 1 counterexamples: modification SenAcc **0.771 vs 0.819** (Nano Banana 2, worse), deletion VLM quality **4.78 vs 4.91** (Nano Banana Pro, worse), poster-generation quality **4.46 vs 4.76** (Nano Banana 2, worse).
- [ ] Table 2's **0.767** SenAcc and **0.036** Masked-LPIPS are **different task aggregates**, not per-operation measures; image-based masking is not object-tree integrity or human editing time.
- [ ] Verify **52 unresolved/173 linked**, a PosterText arXiv mutation negative test, bibliography/audit/acro source citation, real compiled PDF and standalone maps before marking the source stage accepted.
- [ ] Treat this fresh continuation as authorization to work on T06, but preserve T04/T05/T06 **scientific author review** before T07.

## T06 actual PDF and map acceptance — 2026-11-05

- [x] Source commit `729c2343` passed [Paper PDF #41997058915](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41997058915), Catalog Check and Awesome Lint.
- [x] I downloaded exact artifact **13401199657**, extracted the **31-page anonymous manuscript**, final TeX log, and both standalone **26-/67-study** vector research maps. Rendered all pages for an overview and inspected the relevant scientific claims and tabular evaluation pages **7, 10, 14–16**, map **3**, acro system/abbreviation/dataset/benchmark index **18, 22, 24**, bibliography reference **[99] on 27**, and both research maps at 200 DPI.
- [x] I found no apparent layout clipping/overlap in the inspected pages/maps; no undefined citations, references, acro warnings, overfull or underfull box warnings in the final log; and **0** out-of-page text word bounding boxes across 31 pages. The first page and PDF metadata preserve anonymity.
- [ ] **Scientific author review is distinct from build acceptance.** Recheck the latest arXiv v3 results and supplements; retain T04/T05/T06 scientific review before starting T07.
