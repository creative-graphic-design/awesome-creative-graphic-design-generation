# Data Model

The files in this directory are the canonical structured source for the generated catalog. `README.md` at the repository root is a generated view and must not be edited as the source of catalog data.

## Why the catalog is not split by research topic

The catalog intentionally keeps one canonical `resources.csv` instead of separate files such as `layout.csv`, `poster.csv`, or `scientific-figures.csv`.

Research-topic boundaries change as the taxonomy evolves, and many works span several topics. Splitting by topic would turn category changes into file moves and make duplicate detection harder. The stable distinction is the **kind of record**, while `section` and `category` describe how a record is presented.

At the current catalog size, the canonical files are:

- `resources.csv` — rendered catalog resources and the primary task/output taxonomy.
- `paper_metadata.csv` — audited implementation and reproducibility metadata for papers in the `Papers` section.
- `paper_methods.csv` — multi-label method/architecture classifications for papers.
- `venues.csv` — recurring conferences, journals, and workshops monitored for relevant work.

This is intentionally a normalized split by data responsibility, not by research topic. `resources.csv` answers **what the work is and what task/output it belongs to**; `paper_methods.csv` answers **how the paper is implemented**; `paper_metadata.csv` answers **what implementation artifacts are publicly available and reproducible**.

If `resources.csv` later becomes operationally unwieldy, split it only as an explicit schema migration along stable semantic roles, and update the generator and validation in the same change. Do not create ad-hoc files for a temporary research sweep or individual topic.

## `resources.csv`

Each row corresponds to one canonical resource rendered into the root README.

Columns:

- `section` — top-level resource role. Allowed values are defined by `scripts/generate_readme.py`, currently `Surveys and Overviews`, `Papers`, `Datasets and Benchmarks`, `Evaluation Methods and Metrics`, `Models and Implementations`, and `Related Resources`.
- `category` — primary paper task/output taxonomy category. This is populated only for `Papers`; non-paper rows leave it empty.
- `name` — canonical display name.
- `url` — canonical primary link used by the list item.
- `description` — concise objective description of why the resource belongs in the catalog.
- `venue` — publication venue or release context when useful.
- `venue_year` — venue/publication year when known.
- `arxiv_date` — arXiv v1 date in `YYYY-MM-DD`, when applicable.
- `venue_date` — normalized authoritative venue/release date in `YYYY-MM-DD`: conference start date for conference papers, the specific workshop edition date for workshop papers, first online/publication date for journals, or the authoritative release date for non-publication resources.
- `date_note` — short provenance note for the chronology decision.

The generator uses the earlier of `arxiv_date` and `venue_date` as the first-public-appearance sort key and orders research from newest to oldest within each category.

### Date semantics

`venue_date` is intentionally a **venue-level chronology field**, not a paper-session timestamp. For a conference paper, use the official start date of the conference edition rather than the individual poster/oral session date, acceptance date, camera-ready deadline, or proceedings publication timestamp. For a workshop paper, use the date of the specific workshop edition rather than the host conference start date. For journal work, use the first authoritative online/publication date. For datasets, models, implementations, or other non-publication resources, use an authoritative public release date when one exists.

When both `arxiv_date` and `venue_date` are present, chronology still uses the earlier date. `date_note` should record the evidence and any non-obvious choice, for example `CVPR 2025 conference start`, `ICCV 2025 HiGen workshop date`, `journal online publication`, or `official repository release date`.

### Datasets versus benchmarks

`Datasets and Benchmarks` is deliberately combined. A dataset provides reusable examples, annotations, or assets; a benchmark adds a fixed task, split, protocol, or test set. Many releases provide both and should not be duplicated into mutually exclusive sections.

`Evaluation Methods and Metrics` is separate because those entries define reusable ways to score or compare outputs independently of a single benchmark dataset, such as a learned metric or reward model.

## `paper_methods.csv`

This table provides an orthogonal, multi-label method/architecture index for papers in `resources.csv`. It is deliberately separate from `resources.csv` because a paper has exactly one primary task/output category but may combine several implementation families.

Every paper in the catalog should have at least one method classification. The generated `Method Classified` badge therefore acts as a coverage check: when it is lower than the paper count, architecture audit work remains.

Columns:

- `name` — exact paper name from `resources.csv`.
- `method_family` — normalized architecture/method family enforced by the generator.
- `note` — concise paper-specific clarification, such as the particular Transformer role or the form of diffusion.

The normalized vocabulary is maintained as a repository-level method/architecture taxonomy and currently includes:

- `Classical / Optimization`
- `VAE`
- `GAN`
- `Autoregressive / Transformer`
- `Diffusion`
- `Flow Matching`
- `LLM / VLM`
- `Agentic / Multi-stage System`
- `Graph Neural Network`
- `Encoder-only Neural Model`

A paper may appear in multiple families. For example, a diffusion Transformer can have both `Diffusion` and `Autoregressive / Transformer`; an LLM-based multi-agent system can have both `LLM / VLM` and `Agentic / Multi-stage System`. The `Agentic / Multi-stage System` family also covers system-framework contributions whose primary contribution is orchestration across multiple specialized stages rather than one monolithic model.

Do not classify methods from a product or model brand name alone. Use the paper, official project page, or implementation to verify the actual architecture. `Qwen-Image`-based diffusion, for example, is not automatically an `LLM / VLM` method merely because the model name contains `Qwen`.

Canonical paper names matter. If a commonly used method name is only one contribution inside a paper (for example, LayoutGAN++ inside *Constrained Graphic Layout Generation via Latent Optimization*), use the paper title as the resource key and explain the method name in the description or architecture note rather than creating a duplicate paper entry.

## `paper_metadata.csv`

This table is keyed by the exact paper `name` in `resources.csv` and stores implementation/reproducibility information that changes independently from the bibliographic entry.

A row means that the public release state has actually been inspected. Do not create placeholder rows for unaudited papers.

Tracked fields include:

- project page;
- official code repository;
- checkpoint/weights URL;
- code and weight release status;
- method family and base/backbone model;
- datasets actually used for training and evaluation;
- output representation;
- release limitations or other verification notes;
- `checked_at`, the date the release state was last verified.

The allowed status values and detailed verification policy are owned by `CONTRIBUTING.md` and enforced by `scripts/generate_readme.py`.

### Current metadata-scope limitation

`paper_metadata.csv` currently attaches only to entries whose display section is `Papers`. That keeps the bootstrap schema simple, but it means a research paper intentionally displayed under another role — for example a learned reward model under `Evaluation Methods and Metrics` — cannot yet expose the same project/code/weights details through this table.

If this becomes common, prefer a deliberate migration from `paper_metadata.csv` to a more general method/resource metadata table over adding parallel per-section metadata CSVs. The migration should define which resource roles may carry model/reproducibility fields and update generator validation atomically.

## `venues.csv`

This file is a monitoring index of recurring conferences, journals, and relevant workshop series. A venue or workshop being listed does not imply that every paper from it is in scope.

## Validation

After changing catalog data, run:

```bash
uv sync
uv run python scripts/generate_readme.py
uv run python scripts/generate_readme.py --check
```

The `Catalog Check` GitHub Actions workflow performs the generated-file consistency check. `Awesome Lint` separately checks Awesome-list conventions and repository metadata.
