# Repository Agent Guidance

This repository is a curated, generated research index for creative graphic design generation. Keep durable instructions in their existing owners; do not duplicate policy across agent-specific files.

## Read Before Editing

- Read `CONTRIBUTING.md` for scope, taxonomy, publication-date rules, implementation metadata semantics, and contribution requirements.
- Read `.github/workflows/awesome-lint.yml` before changing or naming repository validation gates.
- Treat this file as repository-level workflow guidance, not as a second copy of `CONTRIBUTING.md`.

## Sources of Truth

- `data/resources*.csv` owns curated resource records and publication dates.
- `data/paper_metadata*.csv` owns audited implementation and reproducibility metadata.
- `data/venues.csv` owns the monitored venue index.
- `CONTRIBUTING.md` owns curation policy, paper/resource taxonomy definitions, metadata status semantics, and contributor-facing rules.
- `templates/README.md.j2` owns README presentation.
- `scripts/generate_readme.py` owns validation, joins, compatibility normalization, ordering, and rendering behavior.
- `README.md` is generated output. Never edit it directly.

New topical CSV files may be added under `data/` when they use the existing resource or paper-metadata schema and are intentionally consumed by the generator globs. Do not create a second catalog format for the same records.

## Research and Verification

Prefer primary sources: official papers, arXiv submission histories, conference programs or proceedings, author project pages, official repositories, model hubs, dataset pages, and publisher records.

Do not stop at a named paper supplied in a task. For a research-line expansion, inspect related work, citations, project pages, and neighboring contemporary work, then curate material omissions rather than mechanically importing every citation.

Do not invent or infer reproducibility metadata. A row in `data/paper_metadata*.csv` means the public release state was actually inspected. If implementation details have not been verified, leave the paper without a metadata row instead of filling speculative values.

Release status is time-sensitive. Record `checked_at` whenever implementation metadata is added or refreshed, and preserve explicit states such as announced, withdrawn, inference-only, or training-plus-inference according to `CONTRIBUTING.md`.

Classify papers by their primary task/output, not by architecture family. Classify non-paper resources according to the canonical resource taxonomy in `CONTRIBUTING.md`: datasets and fixed benchmark tasks belong in `Datasets and Benchmarks`; reusable scoring procedures belong in `Evaluation Methods and Metrics`.

## Generated README Workflow

After changing structured data, metadata, taxonomy, or README presentation:

```bash
uv sync
uv run python scripts/generate_readme.py
uv run python scripts/generate_readme.py --check
npx awesome-lint
```

Commit the regenerated `README.md` together with the source change. The generated-file check must pass before considering the edit complete.

`awesome-lint` also checks GitHub repository metadata. If it fails only on repository description or required Awesome topics, report that repository-setting dependency separately; do not weaken the content checks to hide it.

## Public Repository Safety

Keep credentials, private infrastructure, internal endpoints, local machine paths, and environment-specific launch configuration out of this public repository. Do not persist issue or pull-request numbers, temporary migration state, or other expiring facts in repository guidance.

## Agent Adapters

`AGENTS.md` is the repository-level agent source of truth. Tool-specific root guidance should remain a thin adapter. In particular, `CLAUDE.md` should be a relative symlink to `AGENTS.md`, not a copied file or an import stub.
