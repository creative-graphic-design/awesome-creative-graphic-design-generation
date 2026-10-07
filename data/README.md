# Data Model

The files in this directory are the canonical structured source for the generated catalog. `README.md` at the repository root is a generated view and must not be edited as the source of catalog data.

## Why the catalog is not split by research topic

The catalog intentionally keeps one canonical `resources.csv` instead of separate files such as `layout.csv`, `poster.csv`, or `scientific-figures.csv`.

Research-topic boundaries change as the taxonomy evolves, and many works span several topics. Splitting by topic would turn category changes into file moves and make duplicate detection harder. The stable distinction is the **kind of record**, while `section` and `category` describe how a record is presented.

At the current catalog size, the canonical files are:

- `resources.csv` — rendered catalog resources, bibliographic links, the primary task/output taxonomy, and optional paper architecture annotations.
- `paper_metadata.csv` — audited implementation and reproducibility metadata for papers in the `Papers` section.
- `venues.csv` — recurring conferences, journals, and workshop series monitored for relevant work. It intentionally keeps one row per stable series; use an authoritative series/archive URL when one exists, and record concise edition/recurrence evidence in `note`. Add a separate edition table only if concrete query/rendering needs justify the one-to-many model rather than for audit bookkeeping.

This is intentionally a small split by data responsibility, not by research topic. `resources.csv` answers **what the work is, what task/output it belongs to, which bibliographic links identify it, and the concise architecture annotation shown with it**; `paper_metadata.csv` answers **what implementation artifacts are publicly available and reproducible**.

If `resources.csv` later becomes operationally unwieldy, split it only as an explicit schema migration along stable semantic roles, and update the generator and validation in the same change. Do not create ad-hoc bibliographic side tables or temporary topic files.

## `resources.csv`

Each row corresponds to one canonical resource rendered into the root README.

Columns:

- `section` — top-level resource role. Allowed values are defined by `scripts/generate_readme.py`, currently `Surveys and Overviews`, `Papers`, `Datasets and Benchmarks`, `Evaluation Methods and Metrics`, `Models and Implementations`, and `Related Resources`.
- `category` — primary paper task/output taxonomy category. This is populated only for `Papers`; non-paper rows leave it empty.
- `name` — canonical display name.
- `url` — canonical primary link used by the list item. Prefer an authoritative publication/proceedings page once it is verified. Until such a page is available or verified, use the direct arXiv abstract URL; never use an arXiv DOI (`doi.org/10.48550/arXiv.*`) as a publication surrogate.
- `arxiv_url` — optional canonical `https://arxiv.org/abs/...` link when `url` points to a separate authoritative publication/proceedings page. Leave it blank when `url` itself is arXiv so the README does not duplicate the same link.
- `description` — concise objective description of why the resource belongs in the catalog.
- `architecture` — optional short method-family label for paper entries, such as `Diffusion`, `LLM`, `VLM`, or `GAN`; leave blank for non-paper resources. Multiple families may be separated with semicolons. The generator renders this field directly and does not join a separate architecture table.
- `venue` — publication venue or release context when useful.
- `venue_year` — venue/publication year when known.
- `arxiv_date` — arXiv v1 date in `YYYY-MM-DD`, when applicable.
- `venue_date` — normalized authoritative venue/release date in `YYYY-MM-DD`: conference start date for conference papers, the specific workshop edition date for workshop papers, first online/publication date for journals, or the authoritative release date for non-publication resources.
- `date_note` — short provenance note for the chronology decision.

### Bibliographic link contract

Paper links follow one canonical rule based on the best **verified** primary page available:

- **Authoritative publication/proceedings page verified:** `url` points to that page. If an arXiv preprint exists, `arxiv_url` stores the canonical direct arXiv abstract URL and the README renders it as a secondary link.
- **Publication/proceedings page not yet available or not yet verified:** `url` remains the canonical direct arXiv abstract URL and `arxiv_url` stays blank, even when a venue or future publication year is already known.
- **No arXiv preprint:** `url` points to the authoritative publication/resource page and `arxiv_url` stays blank.

Do not use `https://doi.org/10.48550/arXiv.*` as `url`: that DOI still identifies the arXiv preprint and is not a substitute for an authoritative venue/publisher page. Use the direct `https://arxiv.org/abs/...` URL until the publication page is verified.

Do not create a separate bibliographic-links CSV. Publication and arXiv links are intrinsic properties of the resource record and stay in `resources.csv`.

`scripts/validate_resource_contract.py` enforces the column schema and these structural link invariants. The `Catalog Check` workflow runs that validator before checking the generated README, so a contract violation fails CI. The validator deliberately does not infer publication state from `venue` alone because accepted/future papers can have a venue before proceedings are public.

The generator uses the earlier of `arxiv_date` and `venue_date` as the first-public-appearance sort key and orders research from newest to oldest within each category.

### Date semantics

`venue_date` is intentionally a **venue-level chronology field**, not a paper-session timestamp. For a conference paper, use the official start date of the conference edition rather than the individual poster/oral session date, acceptance date, camera-ready deadline, or proceedings publication timestamp. For a workshop paper, use the date of the specific workshop edition rather than the host conference start date. For journal work, use the first authoritative online/publication date. For datasets, models, implementations, or other non-publication resources, use an authoritative public release date when one exists.

When both `arxiv_date` and `venue_date` are present, chronology still uses the earlier date. `date_note` should record the evidence and any non-obvious choice, for example `CVPR 2025 conference start`, `ICCV 2025 HiGen workshop date`, `journal online publication`, or `official repository release date`.

### Datasets versus benchmarks

`Datasets and Benchmarks` is deliberately combined. A dataset provides reusable examples, annotations, or assets; a benchmark adds a fixed task, split, protocol, or test set. Many releases provide both and should not be duplicated into mutually exclusive sections.

`Evaluation Methods and Metrics` is separate because those entries define reusable ways to score or compare outputs independently of a single benchmark dataset, such as a learned metric or reward model.

## `paper_metadata.csv`

This table is keyed by the exact paper `name` in `resources.csv` and stores implementation/reproducibility information that changes independently from the bibliographic entry.

A row means that the public release state has actually been inspected. Do not create placeholder rows for unaudited papers.

Tracked fields include project page, official code repository, checkpoint/weights URL, release status, model family/base model, training/evaluation datasets, output representation, verification notes, and `checked_at`.

Bibliographic publication/arXiv links do **not** belong here; keep them in `resources.csv`.

## `venues.csv`

This file is a monitoring index of recurring conferences, journals, and relevant workshop series. A venue or workshop being listed does not imply that every paper from it is in scope.

## Validation

After changing catalog data, run:

```bash
uv sync
uv run python scripts/validate_resource_contract.py
uv run python scripts/generate_readme.py
uv run python scripts/generate_readme.py --check
```

The `Catalog Check` GitHub Actions workflow enforces the canonical resource contract and generated-file consistency. `Awesome Lint` separately checks Awesome-list conventions and repository metadata.
