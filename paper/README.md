# Graphic-design generation survey (working draft)

This directory contains an initial **research-survey manuscript**, not a submitted CVPR paper. The taxonomy, references, screening criteria, and claims must be reviewed before publication.

## Compile and read

From this directory, with TeX Live, latexmk, and BibTeX installed:

    make pdf

The local output is `paper/main.pdf`. The CI workflow `.github/workflows/paper-pdf.yml` builds the manuscript when a PR or push changes `paper/**` (or when manually dispatched). In the GitHub **Actions → Paper PDF** run, download the **survey-paper-<commit>** artifact from the Artifacts section. It includes the PDF, first-page PNG, extracted text, and diagnostic log. The manuscript and figure PDFs are generated and uploaded in CI artifacts, not committed to Git.

## Official template

- CVPR/ICCV/3DV author kit: https://github.com/cvpr-org/author-kit
- CVPR2027-v1 pinned upstream commit: `a2369342011145be8c85e5ad21a9b61f9fa53473`
- Vendored, unmodified: `cvpr.sty` and `ieeenat_fullname.bst`. The original headers and license notices remain attached to those files.
- `main.tex` uses the official review mode, which hides the sample author block and renders **Anonymous CVPR submission**. Update dummy fields only for the final version.

## Research evidence status (2026-11-03)

The public repository catalog and the broader research evidence register are *different snapshots*. The working register holds 225 provisional entries, with 88 studies reviewed at the methods/results level, 28 checked through abstracts or publication records, and 109 catalog-only. The existing public README currently counts fewer papers. Do not describe all 225 as full-text assessed or as PRISMA-complete. The present paper emphasizes a representation–editability–evaluation crosswalk rather than a benchmark leaderboard.

Citation keys in `references.bib` are traceable to source URLs. I expanded `literature_citation_audit.csv` to 180 citation-level records: 144 still `not_verified` by individual source key and 36 newly added references whose original author/title/abstract records were checked (`abstract_index`), without claiming methods/results verification. The aggregate historical 88/28/109 source-depth figures cannot be assigned to those citations without identity matching. The audit is checked by `scripts/check_literature_audit.py` in pre-commit and CI. Bibliographic authors missing from provisional entries must be verified from publisher/proceedings sources instead of being guessed. Survey completion also requires a reproducible retrieval log, screening flow, deduplication, adjudicated scope boundaries, and full-text checks for eight remaining narrative papers.

## Writing and audit invariants

- Distinguish representation affordance, qualitative edit demonstration, human editing efficiency, and measured edit-instruction execution.
- Do not equate raster creation-time conditioning with post-export editing, or SVG/PSD/DOM export with quantitative editing success.
- FID, CLIP similarity, Chamfer reconstruction, and layout IoU are not editing performance metrics by themselves.
- Keep catalog changes in canonical data CSVs; do not manually modify the root README, which is generated.

## Related-survey and figure design notes

Seven prior surveys were compared in `sections/related_surveys.tex`: Huang (2023), Shi (2023), Liu (2024), Tian and G\u00fcnther (2024), Li et al. (2024), Zou et al. (2025), and Malashenko et al. (2025). Common figure roles are (1) overview/taxonomy, (2) survey discovery/counts, (3) specific research-line methods, and (4) synthesis/research challenges. This working draft adds two original **editable TikZ** figures: `figs/tex/overview.tex` (R–E–V crosswalk) and `figs/tex/edit_protocol.tex` (measured editing dimensions). We deliberately do not fabricate PRISMA exclusion counts or a publication-time histogram; those require a frozen and reconciled corpus. See the survey comparison table in the paper.

## Citation health checks

Run `python3 paper/scripts/check_bibliography.py` from the repository root (or `python3 scripts/check_bibliography.py` inside `paper/`) to validate citation resolution, required BibTeX fields, duplicate identifiers, placeholder authors and unused bibliography entries. CI executes the same script before TeX compilation. These checks test **structural consistency**, not the truth of author names, venues, empirical results or source selection. Source-level bibliographic verification remains an editorial responsibility.

### Review provenance and sample count
The Zou et al. (2025) paper describes a 500-item dataset in its methodology narrative and lists 267 reviewed papers in its earlier-survey comparison table. We document both numbers rather than silently choosing one. Tang et al. (2024) is a seven-designer interview study, included as practitioner context and explicitly distinguished from technical surveys.

## New evidence and benchmark comparison

I added a comparison section covering SVGEditBench, VectorGym, MiLDEdit, InfoEdit, MPTc-Bench, GraphicDesignBench, BizGenEval and AesEval-Bench. The paper now distinguishes protected objects from necessary dependent layout reflow rather than requiring every non-target pixel to remain fixed.

`REVIEW_PROTOCOL.md` is a **prospective protocol, not an executed search log**. It specifies database/query templates, screening and exclusion codes, source-depth labels, and requirements for eventual inclusion-flow figures. Do not present its planned searches as completed.

The bibliography contains newly verified benchmark primary-source records; older entries still require final title/author/DOI checks before publication.

## Source layout and writing-review gates

- `figs/tex/`: standalone TikZ figure sources and float wrappers with captions and labels.
- `figs/pdf/`: generated vector PDFs, created by `make figures` and included in CI artifacts.
- `tabs/tex/`: five independent TeX tables, included by their original narrative sections.
- Before every paper commit, read `WRITING_CHECKLIST.md`, run `python3 paper/scripts/check_manuscript.py` and `python3 paper/scripts/check_bibliography.py`, then run `cd paper && make pdf` and check the rendered PDF. Agent instructions are in `paper/AGENTS.md`. Local hooks can be installed by `uvx pre-commit install` at repository root; CI checks paper changes even when hooks are absent.

## Numbered sections, sentence diffs and historical research map

Manuscript sections follow `01_abstract.tex`, `02_introduction.tex`, through `10_conclusion.tex`. TeX prose uses **one sentence per physical source line** (blank lines separate paragraphs), making version-control diffs and PR reviews sentence-granular without changing rendered paragraph breaks. Use `\\citet{key}` when an author is part of a sentence; use `\\citep{key}` for a parenthetical citation, without manually repeating author names.

`figs/tex/research_map.tex` contains an original chronological, task-colored research map motivated by the SSII2024 overview shared for visual reference; `figs/tex/research_map_figure.tex` holds its caption and label. The map groups selected 2019–2026 studies and **does not assert direct causal or citation relationships**. The source is independently compilable; `make figures` generates `figs/pdf/research_map.pdf`.

The paper CI runs the same source-line checker as the pre-commit hook, plus its negative-fixture unit tests. The checker is an intentionally conservative static lint, not a guarantee of grammatical correctness or source verification.

## Survey figure design review (2026-11-04)

`FIGURE_DESIGN_SURVEY.md` compares figures visually inspected in the Huang (2023), Zou (2025), Luo (2025) and Zhang (2026) surveys, with separately labelled publisher/author-summary observations for Shi (2023) and Tian & Günther (2024). It defines a richer diagram architecture inspired by the SSII2024 map without copying it. `figs/tex/affiliation_logo_provenance.csv` records paper-date institutional evidence; official visual logos have not yet been retrieved or cleared for publication. A standalone original TikZ **concept** was compiled locally for review, but the vetted 67-milestone map remains the current manuscript figure.

## Citation coverage checkpoint (2026-11-03)

The manuscript bibliography now has **180 distinct references**, 36 added from author-supplied original abstract pages across six graphic-design research lines. `catalog_citation_crosswalk.csv` reconciles these against 207 public catalogue papers, conservatively matching 138 and flagging 69 unmatched for further work. Those 69 are not screened exclusions; the separate provisional 225-study register is not yet joined to citation keys. See `LITERATURE_COVERAGE_AUDIT.md` and the `check_catalog_crosswalk.py` validator.

## Acronyms and named systems (CTAN acro)

The central registry is `paper/acronyms.tex`, using CTAN `acro` v3 instead of `glossaries`.
Genuine abbreviations expand on first use through `\ac{key}`; subsequent mentions display the short form.
Named model and system entries use `first-style=short` to preserve published names without fabricating expansions.
Two `\printacronyms` lists separate abbreviations and named systems. `acro` also attaches a source key to 70 named systems (`cite`) and prints all usage pages (`pages/display=all`) in both lists.
The manuscript checker rejects missing or duplicate definitions and obsolete package commands; the PDF CI verifies LaTeX compilation.

The research map is a curated **six-track by four-era** matrix with **67 representative milestones**, not a citation graph or complete publication census.
Its year labels use the cited bibliography year (venue year when available, otherwise preprint year); they do not always equal the first public version date.
Its editable source is `figs/tex/research_map.tex` and its compiled vector output is `figs/pdf/research_map.pdf`.
The 67 figure labels are cross-referenced to actual BibTeX entries in `figs/tex/research_map_sources.csv`, checked in CI; see `RESEARCH_MAP_AUDIT.md` for date and selection caveats.

Both `\printacronyms` lists use `display=all`, so every declared abbreviation and named system is included even if it has not yet appeared in the paper. PDF CI verifies representative entries and rejects an empty acronym-list warning.
