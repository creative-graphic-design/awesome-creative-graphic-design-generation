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
