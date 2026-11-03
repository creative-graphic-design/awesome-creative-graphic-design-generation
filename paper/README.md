# Graphic-design generation survey (CVPR-style working draft)

This directory contains an initial **research-survey manuscript**, not a submitted CVPR paper. The taxonomy, references, screening criteria, and claims must be reviewed before publication.

## Compile and read

From this directory, with TeX Live, latexmk, and BibTeX installed:

    make pdf

The local output is `paper/main.pdf`. The CI workflow `.github/workflows/paper-pdf.yml` builds the manuscript when a PR or push changes `paper/**` (or when manually dispatched). In the GitHub **Actions → Paper PDF** run, download the **survey-paper-<commit>** artifact from the Artifacts section. It includes the PDF, first-page PNG, extracted text, and diagnostic log. Generated PDFs are not committed.

## Official template

- CVPR/ICCV/3DV author kit: https://github.com/cvpr-org/author-kit
- CVPR2027-v1 pinned upstream commit: `a2369342011145be8c85e5ad21a9b61f9fa53473`
- Vendored, unmodified: `cvpr.sty` and `ieeenat_fullname.bst`. The original headers and license notices remain attached to those files.
- `main.tex` uses page-numbered draft mode; change to venue-required review mode before a real submission.

## Research evidence status (2026-11-03)

The public repository catalog and the broader research evidence register are *different snapshots*. The working register holds 225 provisional entries, with 88 studies reviewed at the methods/results level, 28 checked through abstracts or publication records, and 109 catalog-only. The existing public README currently counts fewer papers. Do not describe all 225 as full-text assessed or as PRISMA-complete. The present paper emphasizes a representation–editability–evaluation crosswalk rather than a benchmark leaderboard.

Citation keys in `references.bib` are traceable to source URLs. Bibliographic authors missing from provisional entries must be verified from publisher/proceedings sources instead of being guessed. Survey completion also requires a reproducible retrieval log, screening flow, deduplication, adjudicated scope boundaries, and full-text checks for eight remaining narrative papers.

## Writing and audit invariants

- Distinguish representation affordance, qualitative edit demonstration, human editing efficiency, and measured edit-instruction execution.
- Do not equate raster creation-time conditioning with post-export editing, or SVG/PSD/DOM export with quantitative editing success.
- FID, CLIP similarity, Chamfer reconstruction, and layout IoU are not editing performance metrics by themselves.
- Keep catalog changes in canonical data CSVs; do not manually modify the root README, which is generated.

## Related-survey and figure design notes

Six prior surveys were compared in `sections/related_surveys.tex`: Huang (2023), Shi (2023), Tian and G\u00fcnther (2024), Li et al. (2024), Zou et al. (2025), and Malashenko et al. (2025). Common figure roles are (1) overview/taxonomy, (2) survey discovery/counts, (3) specific research-line methods, and (4) synthesis/research challenges. This working draft adds two original **editable TikZ** figures: `figures/overview.tex` (R–E–V crosswalk) and `figures/edit_protocol.tex` (measured editing dimensions). We deliberately do not fabricate PRISMA exclusion counts or a publication-time histogram; those require a frozen and reconciled corpus. See the survey comparison table in the paper.

## Citation health checks

Run `python3 paper/scripts/check_bibliography.py` from the repository root (or `python3 scripts/check_bibliography.py` inside `paper/`) to validate citation resolution, required BibTeX fields, duplicate identifiers, placeholder authors and unused bibliography entries. CI executes the same script before TeX compilation. These checks test **structural consistency**, not the truth of author names, venues, empirical results or source selection. Source-level bibliographic verification remains an editorial responsibility.
