# Manuscript author feedback and pre-commit review

**Read this file before drafting and again before each paper commit.** This is the durable record of prior author-review comments. Its qualitative criteria require author judgment; automated lint checks below cannot independently prove that the science or prose is correct.

## Mandatory built-in-first check before implementation (author decision, 2026-11-06)

- [ ] **Upstream documentation first:** before writing a LaTeX list template, formatter, index, wrapper, or custom CI guard, read the actually used package version's manual and look for built-in options matching the user's requirements.
- [ ] **Minimal proof and screenshot:** compile the smallest stock example, then inspect the **actual full manuscript PDF** at readable resolution. Test desired behavior, not merely whether compilation succeeds.
- [ ] **Preserve features while simplifying:** compare old and new visible behavior (particularly occurrence-page indexes, descriptions, first-use citations, and hyperlinks). Never silently drop a requirement because an implementation was simplified.
- [ ] **Author-approved `acro` behavior:** default `\\printacronyms` list for all three groups with `display=all`, plus the built-in `\\acsetup` options `pages/display=all`, `pages/name=true`, `pages/seq/use=false`. Keep the source-linked 198-term registry. No `survey-rich` or `\\NewAcroTemplate` unless the author requests a new capability that stock `acro` demonstrably cannot provide.
- [ ] **Customization exception:** state the specific unmet requirement and the smallest necessary deviation **before** adding bespoke formatting or a bespoke validator; do not equate custom CI success with a correct PDF.
- [x] **Why this exists:** earlier iterations repeatedly modified `survey-rich` rather than first checking `acro`'s documented built-in page-index support. The author ultimately accepted the **stock list plus occurrence pages**, and the original source-commit [Paper PDF #42153100997](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42153100997) was visually checked. The earlier design is a **superseded historical experiment**, not a recommended starting point.


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
- [x] **Superseded by direct author instruction (2026-11-06):** print all three groups using **acro's stock default list template**, with no `survey-rich` or hand-built list layout. Keep citations, year, venue, URL, DOI, task, representation and usage evidence stored in the registry, but **do not force the custom metadata into print**; continue structural provenance checks. The bibliography provides original source references.
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
- [x] **v3 main-paper verification:** directly inspected and compared the original arXiv v2/v3 PDF Table 1, Table 2, Figure 3 and methods on 2026-11-06; scores, task definitions and raster-output limits agree (see `T06_POSTERTEXT_SOURCE_AUDIT.md`). This does **not** constitute a fresh manuscript PDF build.
- [ ] **Scientific author review is distinct from build acceptance.** Independently obtain/review any separate supplementary implementation document; retain T04/T05/T06 author scientific approval before starting T07.

## acro two-column line wrapping — 2026-11-05

- [x] The two-column `survey-rich` index was visibly **fully justified**, with awkwardly stretched word spaces, unwanted word hyphenation and dense metadata wrapping on T06 PDF pp. 22/24; it is a typography issue rather than evidence that the `paperurl` property is a built-in acro field.
- [x] I tested a standalone `acro` LaTeX specimen containing PosterText, PosterLayout, PPTAgent and UniWorld-Design. Applying `\\raggedright`, non-hyphenating penalties and modest item spacing improved natural word-boundary wraps.
- [x] Keep **all 198 acro entries** and the printed source, year, venue, task, representation, paper and DOI links, and occurrence pages; this change is only typesetting, not source or citation curation.
- [x] Add a manuscript CI guard for the three wrapping controls so that a future template edit cannot silently restore justified, hyphenated acronym entries.
- [ ] Download and inspect the **full newly compiled anonymous manuscript** at representative beginning/middle/end acro pages; review the worst long venue and annotated PosterText entries, count/links/occurrence pages, PDF line-box warnings and page count before declaring production acceptance.

## acro compact index correction after actual full-PDF comparison (2026-11-05)

- [x] I downloaded and inspected the **31-page** real [Paper PDF #42025690265](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42025690265) from layout-only source `bfb577f`, compared pages **22** and **24** side by side with the T06 PDF. Although `\\raggedright` removed stretched spaces, **Task** and **Representation** still wrapped awkwardly across multiple short lines. The earlier fix alone was insufficient.
- [x] In `survey-rich`, retain the name/description, **publication year, venue, original source citation, paper URL link, DOI and occurrence pages** but suppress the *printed* Task and Representation paragraphs. The original `task` and `representation` `\\DeclareAcroProperty` definitions and all underlying registered values are retained; they can be used in structured comparative tables or later supplements.
- [x] I compiled and rendered a four-entry, two-column `acro` LaTeX comparison using PosterText, PosterText-Bench, PosterMaker and UniWorld-Design with the compact layout. It no longer inserts multi-line explanatory paragraphs between the description and source references.
- [x] Update `check_manuscript.py` so it requires source/year/venue/URL/DOI/pages while rejecting accidental printing of verbose task/representation fields in the two-column index.
- [x] I downloaded **artifact 13417988514** from the successful **source-commit** [Paper PDF #42033969385](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42033969385) (`0dbe879`) and inspected the actual **31-page** anonymous PDF. I compared index **pp. 18, 22, 24** with the ragged-right-only output, confirming that the printed long Task/Representation blocks disappeared while name, year, original citation, paper/DOI links and usage-page markers remain. I also examined the list-to-References transition on p. 24, found no text-word boxes outside any PDF page rectangle, and no undefined citation/reference, acro, overfull or underfull warnings in the build log. This is targeted visual QA, not scientific author sign-off or exhaustive high-resolution proofreading.

## Documentation stale-count reconciliation — 2026-11-05

- [x] Keep the T06 source-stage denominator explicit: **225 provisional IDs, 202 cited BibTeX works, 198 acro registry entries (27 abbreviations / 151 systems / 20 evaluation), 173 linked IDs, 52 unresolved**, with the separate public 207 catalogue **156 linked / 51 pending**. Do not infer publication readiness or full-text review of all 225 entries.
- [x] I labeled outdated **180/186 reference, 175/185 acro and 148/157 crosswalk** counts in `README.md` and `ACRO_AUDIT.md` as the appropriate earlier 2026-11-04 historical checkpoints, retaining their actual values for provenance. The T17 index list now reflects the **198-entry compact print output**, which keeps citation/year/link/page metadata but stores Task/Representation outside print.
- [ ] Continue to distinguish the **198 registered terms** from verified individual source-level experiments and from all papers in the 225-study provisional register; no author-scientific approval or current v3 PosterText result claim is implied by this documentation cleanup.
- [x] I completed a second pass on the old README index section: marked its **180-reference** and **22/130/16 acro** figures as dated checkpoints and corrected **both** to **all three** printed `acro` lists while leaving the historical numbers recoverable.

## Full acro index visual spot check — residual heading wrap (2026-11-05)

- [x] I rendered **all eight printed index pages (17–24)** from the actual **31-page**, source-verified anonymous PDF `0dbe879`. The 198-term compact index content is readable, and pages 18–24 show source citations/URLs and printed appearance pages.
- [x] The evaluation index heading on p. **23** was still **broken inside the word “Resources”** as `Re-` / `sources`, even though the PosterText entries on pp. 22/24 no longer had excessive metadata wraps. This was an independent leftover typography defect.
- [x] Shorten only the printed section heading to **“Evaluation Resources”** in `main.tex`, preserving all 20 evaluation entries, the `evaluation` tag, and all source/year/DOI/URL/page data. Add a structural CI guard to prevent reintroducing the long hyphenated heading.
- [ ] Compile the complete manuscript for this **heading-only source revision** and check the real p. 23 heading in GitHub Actions before claiming final visual acceptance. The prior 31-page PDF remains the most recently directly inspected full artifact until then.

## acro hyperlink target (not just visible label) defect — 2026-11-05

- [x] I inspected actual PDF link annotations on the **31-page source-build artifact 13417988514**. The 171 named resource `paper` labels were malformed remote-file (`GoToR`) PDF actions with `%5Cacroprintfield...` file names rather than accessible article URLs. The 25 `DOI` labels had `https://doi.org/\\acrowrite {doi}` as their literal URI. Printed blue labels were **not** proof of working links; earlier visual-only acceptance was incomplete.
- [x] I reproduced the defect in a local `acro` LaTeX test and resolved it by using `\\ExpandArgs{e}\\acrofield{\\AcronymID}{paperurl}` and the equivalent DOI field as **expandable href targets**. The compiled MWE yielded exact arXiv URIs and a DOI URI rather than remote-file actions.
- [x] I added an independent `pdfinfo -url` PDF-build gate: `check_acro_pdf_links.py` counts every expected **171 paperurl** and **25 DOI** occurrence by destination and **multiplicity** (not just a link label), and rejects raw/percent-encoded unexpanded TeX macros. Five positive/negative regression cases passed locally; the old production PDF correctly failed the new validator.
- [ ] Rebuild the **real current manuscript** and inspect PDF URI link annotations, the p. 23 shortened heading, original citations, index usage pages and remaining layout before marking this correction fully verified.

## Printed acro index: name/description alignment defect (2026-11-06)

- [x] I rendered a genuine full-size screenshot of the latest source-generated PDF **p. 19** (also pp. 17–24), not merely checked PDF-extracted text or the success state. The `description` environment creates a variable-length **label box** for names such as `CGL-GAN`, `CreatiParser`, and `De-Rendering Stylized Texts`, while the description's continuation lines start at the same fixed indentation. The mismatch gives the impression of erratic spaces and breaks even when `\\raggedright` and word-hyphenation penalties are active.
- [x] Independently compile and inspect a two-column `acro` LaTeX specimen with eight representative names (including `Attribute-conditioned Layout GAN`, `PosterText`, and `UniWorld-Design`) using the original `description` and a plain `list` with **zero left/label/item indentation**. Treat the prototype as layout-only validation.
- [x] Refactor `survey-rich` to a flat `list`: inline unbreakable bold short name + `\\enspace` + descriptive text; continuation lines now use the same text-column start; provenance metadata is independently indented **1 em**. Preserve all 198 registered terms, three groups, citations, year/venue, raw URL expansion, DOI and occurrence pages. Introduce a CI guard specifically forbidding `description` labels in this index.
- [ ] Build the **real updated manuscript** under source-commit Paper PDF CI, download the artifact, screenshot full pages **18–24**, and compare p. 19 with the prior full-sized screenshot. Verify line overflow, URI targets, page count and bibliography transition before declaring the spacing issue fixed.

## Author-requested simplification: use the acro default (2026-11-06)

- [x] Before doing any more hand-tuning, I compiled and rendered an actual two-column LaTeX example using **only** `\\usepackage{acro}` and `\\printacronyms[include=systems,heading=none,display=all]`. The built-in template successfully typeset the model names and descriptions without any `\\NewAcroTemplate` definition.
- [x] In `main.tex`, remove `\\input{acro_list_template}`, all three `template=survey-rich` arguments, and custom occurrence-page styling. Keep the 3 groups and `display=all`. Transfer pre-existing nonprint metadata-property registrations to the **top of `acronyms.tex`**, preserving all 198 definitions and citation-level consistency checks.
- [x] Remove the print-only URL-link multiplicity CI requirement: the built-in template does not promise 171 paper/25 DOI anchors. Continue ordinary PDF/metadata/citation validation; source BibTeX URLs and `acro` registry entries remain unchanged.
- [x] Modify `check_manuscript.py` to **require the default list setup**, reject custom template loads, and still verify that registered source metadata matches the bibliography.
- [x] I downloaded the **actual compiled source-run artifact 13433601126** from successful [Paper PDF #42062616167](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42062616167): a **28-page** anonymous manuscript. I rendered actual PDF **pp. 17–22**, inspected the entire **three-group index on pp. 17–21** (especially pp. 19–20 where `description` caused inconsistent indentation), and checked the transition to references on **p. 21**. No source-template hanging-indent defect, off-page words (0/28 pages), unresolved citations, `acro` warnings or TeX box warnings were observed. This verifies the standard formatter only, not scientific conclusions.
- [x] **Historical limitation before the 2026-11-06 page-index correction:** the standard-template PDF did not print occurrence pages because I omitted the built-in `pages/display` option. The bibliography metadata and custom external paper/DOI links were not printed either. The appearance-page omission has now been corrected using stock `acro` options (see newer checkpoint below).
- [x] Remove the now-dead `paper/acro_list_template.tex`, `paper/scripts/check_acro_pdf_links.py` and corresponding print-only unit tests, plus the no-longer-used PDF-link export from CI. No custom list template remains to accidentally reactivate.

## Restore occurrence-page index using only stock acro (2026-11-06)

- [x] Read the **acro v3.8** manual, Section **11.2 Add page numbers to the list**: `pages/display = all` displays usage pages, `pages/name = true` adds `p.`/`pp.`, and `pages/seq/use = false` avoids `f.`/`ff.` abbreviations. This requires **no custom list template**.
- [x] I compiled a three-page **two-column** LaTeX test using `\\acsetup{pages/display=all,pages/name=true,pages/seq/use=false}` with `LayoutGAN`, `PosterText`, `UniWorld-Design`. After the necessary LaTeX convergence passes, the stock index printed `p. 1`, `pp. 1, 2`, and `p. 2` correctly.
- [x] Add these stock options to `paper/main.tex` and enforce them with `paper/scripts/check_manuscript.py`. Keep all three `\\printacronyms[include=...,heading=none,display=all]` calls and all **198 registered** abbreviations/systems/evaluation resources. No custom template, bibliography changes, or supplementary formatting commands.
- [ ] Verify the exact **full-paper source-commit** CI artifact and screenshot the usage-page index, confirm actual PDF page references, citation output, and readable two-column wrapping; then update the author checklist and PR.

## Full-PDF occurrence page index: LaTeX convergence regression (2026-11-06)

- [x] I inspected the **actual failed** [Paper PDF #42150444462](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42150444462) job log and downloaded artifact **13472374278**. The 5 LaTeX passes produced PDF page counts **23 → 28 → 29 → 29 → 29**, with an indexed `PosterText pp. 7, 10, 14`, `UniWorld-Design pp. 7, 11, 13`, `PosterText-Bench pp. 14, 15`; the stock `acro` page index **rendered correctly**, but latexmk exited 12 because it exceeded the default **5-pass** `$max_repeat` limit. `main.aux` changed on every pass and BibTeX was rerun; no substantive TeX error caused the failure.
- [x] I added a **small build configuration**, `paper/.latexmkrc`, with `$max_repeat = 8;` so latexmk has sufficient passes for crossreferences/indices to converge. This does not modify `acro` rendering or introduce any custom template; the GitHub Actions job still uses `latexmk` through the same `latex-action`. Eight runs are a finite limit rather than forcibly accepting a non-convergent document.
- [x] The source build `117f247` **passed** [Paper PDF #42153100997](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42153100997), Awesome Lint and Catalog Check with a finite eight-pass `latexmk` cap. I downloaded artifact **13473718306** and inspected its genuine **29-page** anonymous PDF: `Abbreviations` pp. 17–18, `Selected Systems and Terminology` pp. 18–21, `Evaluation Resources` pp. 21–22, and `References` beginning p. 22. `PosterText pp. 7, 10, 14`, `UniWorld-Design pp. 7, 11, 13`, and `PosterText-Bench pp. 14, 15` were visibly present in the index. I rendered and inspected index **pp. 17–22**, checked both unchanged standalone narrative/atlas maps, found **zero** out-of-page text words in 29 pages, no `acro` warnings, no unresolved citations/references, and no TeX overfull/underfull box warnings. The stock list does **not** print the custom paper/DOI hyperlinks, as intended.

## Stock acro citation/paper-link pilot — four entries (2026-11-06)

- [x] Verify with an independently compiled two-column TeX example that stock `acro`'s `extra` property can display a parenthesized native `\\citealp` citation and a native `\\href{...}{paper}` link **alongside the existing occurrence pages**; inspect the PDF and verify all four exact URI annotations with `pdfinfo -url`.
- [x] Apply the minimal native `extra = {\\citealp{key}; \\href{url}{paper}}` to **only** LayoutGAN, PosterText, UniWorld-Design, and PosterText-Bench in `paper/acronyms.tex`. Keep `long`, `cite`, first-use formatting, 198 registered terms, all three default lists, and existing source metadata untouched. This pilot deliberately does not mass-populate 171 paper links or print year/venue/DOI annotations.
- [x] Add a small source-identity consistency check to the **existing** `check_manuscript.py`: if an `extra` citation/paper link exists, it must match the entry's registered original citation and `paperurl`, already crosschecked against BibTeX. Do **not** add any custom index template.
- [x] I verified source `dd1ee78`: [Paper PDF #42159374944](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42159374944), Catalog Check and Awesome Lint **all succeeded**; downloaded artifact **13476423122**, the **29-page** anonymous manuscript and both unchanged vector research maps. I rendered the affected **pp. 19–22** of the actual full PDF and compared them side-by-side against the previous stock-list PDF. Exactly **four URI annotations** resolve to the registered arXiv links: LayoutGAN (p. 19, arXiv 1901.06767), PosterText (p. 20, 2608.16289), UniWorld-Design (p. 21, 2608.03971), PosterText-Bench (p. 22, 2608.16289). Every original `p.`/`pp.` occurrence index is retained. The document remains **29 pages**, with **zero** off-page word boxes, `acro` warnings, undefined citations/references or TeX overfull/underfull box warnings. The pre-existing standalone `8` line in LayoutGAN's page list also exists in the baseline stock-PDF, not introduced by this pilot. The extra source lines are readable but take additional column space; **do not bulk-expand** until the author reviews readability and page budget.

## PosterText supplement provenance gate (2026-11-06)

- [x] Revisited the official arXiv v3 abstract, HTML contents and main PDF, and searched exact-title/author/arXiv-ID, PosterText-320K and PosterText-Bench code/data/project leads. The main paper points to supplementary implementation details but no independently accessible original supplement was confirmed in the sources inspected. See [T06 availability audit](T06_POSTERTEXT_SOURCE_AUDIT.md).
- [ ] Preserve **supplement not obtained** as an unresolved provenance limitation. The TeX source archive could not be inspected; do not infer that no supplement exists or promote training/reproducibility evidence from the verified v3 tables alone.
- [ ] If a source-identified supplement is retrieved, check method configuration, annotation quality, benchmark judging and release/licensing claims independently, and only then update evidence tiers or manuscript claims as needed. Keep T04–T06 scientific author sign-off separate.

## PosterText v3 main-paper reconciliation (2026-11-06)

- [x] Visually compare the version-identified **v2** and **v3** nine-page original arXiv PDFs, especially Table 1/Table 2 (PDF p. 7), Figure 3 and evaluation definitions (PDF p. 5), and four-stage method descriptions; record numeric and representation outcomes in [T06 source audit](T06_POSTERTEXT_SOURCE_AUDIT.md).
- [x] Confirm that all audited v2 Table 1–2 values still match v3 and that the model's deliverable is a **raster image**, not a native editable HTML/PSD/SVG/text-layer document. No numerical changes to the TeX manuscript or 225/202/198/173 source-stage snapshot were justified.
- [ ] Retrieve and review the independently available **supplementary implementation** details referenced by the nine-page main paper; the main PDF ends in references, without an appendix.
- [ ] Preserve separate T04–T06 **author scientific approval** and systematic literature-search gates; do not begin T07 on the strength of this main-paper comparison.


## Complete acro native citations and links — 171 items (2026-11-06)

- [x] Based on author feedback, use native `acro` `extra` to attach a textual `\citet{original_key}` and `\href{registered_paperurl}{paper}` to **all 171** source-registered systems/evaluation resources, not just four exemplars. This adds 167 and converts the four pilots from `\citealp`; all 27 generic abbreviations retain their normal treatment.
- [x] Maintain stock `\printacronyms`, 198 source-linked terms, source provenance and built-in explicit occurrence pages. Use no custom index template. Extend the existing checker to require the exact citation key/URL for **every** named resource.
- [x] Independently compile and inspect the two-column stock `acro`/natbib/hyperref specimen; `\citet` works, and a second two-column **numeric natbib** specimen gives `(Author [N]; paper)` in the stock list, with valid URIs and `p.` occurrence pages. The author–year-only specimen yields nested parentheses, but the actual CVPR-style numeric output should not. Inspect the real source-commit PDF rather than assuming either prototype is production evidence.
- [x] I downloaded source-commit [Paper PDF #42231751692](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42231751692) artifact **13510498476**, extracted its 29-page anonymous manuscript, final TeX log and two standalone research maps, and rendered index **pp. 17–22**. The stock lists preserve 198 terms in three groups, displayed author-plus-number `\\citet` citations, original-paper URL labels and `p.`/`pp.` occurrence pages; the bibliography begins on p. 22. The initial all-171 version had 175 URI annotations because UniWorld-Design and Rico split `paper` over lines. Using native `\\href{url}{\\mbox{paper}}` and the existing checker, I verified **exactly 171 URI annotations for 171 indexed links**, **167 unique destinations**, and **no lost URL destinations** versus the pre-fix artifact. All 171 annotations are on pp. 18–22; no page rectangle contains off-page words, and the final TeX log has no unresolved citations/references, `acro` warnings or overfull/underfull box warnings. I rendered/checked both standalone **26-study** and **67-study** vector maps. **Paper PDF, Catalog Check, and Awesome Lint all passed**. The stock index remains dense in two columns, but no clipping/overlap was detected in the inspected samples. This is **artifact acceptance**, not scientific author sign-off.
