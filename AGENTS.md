# Repository Agent Guidance

This repository is a curated, generated research index for creative graphic design generation. Keep durable instructions in their existing owners; do not duplicate policy across agent-specific files.

## Read Before Editing

- Read `CONTRIBUTING.md` for scope, taxonomy, publication-date rules, method classification, implementation metadata semantics, and contribution requirements.
- Read `data/README.md` for the canonical CSV/data model and its current metadata-scope constraints.
- Read `.github/workflows/catalog-check.yml` and `.github/workflows/awesome-lint.yml` before changing or naming repository validation gates.
- Treat this file as repository-level workflow guidance, not as a second copy of `CONTRIBUTING.md` or the data schema.

## Sources of Truth

- `data/resources.csv` owns all curated resource records, primary task/output taxonomy placement, and publication dates.
- `data/paper_methods.csv` owns the orthogonal multi-label method/architecture taxonomy for papers.
- `data/paper_metadata.csv` owns audited implementation and reproducibility metadata for entries in the `Papers` section.
- `data/venues.csv` owns the monitored conference, journal, and workshop index.
- `data/README.md` owns the structural rationale and schema-level responsibilities of the canonical data files.
- `CONTRIBUTING.md` owns curation policy, paper/resource taxonomy definitions, method-family semantics, metadata status semantics, and contributor-facing rules.
- `templates/README.md.j2` owns README presentation and generated count badges.
- `scripts/generate_readme.py` owns validation, joins, ordering, statistics, and rendering behavior.
- `README.md` is generated output. Never edit it directly.

Do not create topical, batch, or migration-time CSV shards for catalog data. The canonical catalogs are intentionally split by stable data responsibility rather than research topic. If they become operationally unwieldy, change the storage model explicitly and update `data/README.md`, the generator, contribution guidance, and CI in the same change.

## Research and Verification

Prefer primary sources: official papers, arXiv submission histories, conference programs or proceedings, author project pages, official repositories, model hubs, dataset pages, and publisher records.

Do not stop at a named paper supplied in a task. For a research-line expansion, inspect related work, citations, project pages, and neighboring contemporary work, then curate material omissions rather than mechanically importing every citation.

Do not invent or infer reproducibility metadata. A row in `data/paper_metadata.csv` means the public release state was actually inspected. If implementation details have not been verified, leave the paper without a metadata row instead of filling speculative values.

Release status is time-sensitive. Record `checked_at` whenever implementation metadata is added or refreshed, and preserve explicit states such as announced, withdrawn, inference-only, or training-plus-inference according to `CONTRIBUTING.md`.

Classify papers by their primary task/output in `data/resources.csv`, not by architecture family. Independently classify verified architectures in `data/paper_methods.csv`; hybrid systems may have multiple method-family rows. Do not infer an architecture from a model brand name alone.

Classify non-paper resources according to the canonical resource taxonomy in `CONTRIBUTING.md`: datasets and fixed benchmark tasks belong in `Datasets and Benchmarks`; reusable scoring procedures belong in `Evaluation Methods and Metrics`.

## Generated README Workflow

After changing structured data, metadata, taxonomy, or README presentation:

```bash
uv sync
uv run python scripts/generate_readme.py
uv run python scripts/generate_readme.py --check
npx awesome-lint
```

Commit the regenerated `README.md` together with the source change. The `Catalog Check` workflow verifies that the committed README exactly matches the canonical CSV data and template.

`awesome-lint` also checks GitHub repository metadata. If it fails only on repository description or required Awesome topics, report that repository-setting dependency separately; do not weaken the content checks to hide it.

## Public Repository Safety

Keep credentials, private infrastructure, internal endpoints, local machine paths, and environment-specific launch configuration out of this public repository. Do not persist issue or pull-request numbers, temporary migration state, or other expiring facts in repository guidance.

## Agent Adapters

`AGENTS.md` is the repository-level agent source of truth. Tool-specific root guidance should remain a thin adapter. In particular, `CLAUDE.md` should be a relative symlink to `AGENTS.md`, not a copied file or an import stub.
