# Contribution Guidelines

Thank you for helping curate Awesome Creative Graphic Design Generation. The goal is a focused, high-signal list, not an exhaustive directory.

## Scope

A resource is in scope when it makes a direct contribution to the generation, editing, representation, understanding, or evaluation of composed graphic-design artifacts such as posters, advertisements, social-media graphics, magazine/editorial layouts, scientific figures and graphical abstracts, scientific posters, slides, banners, and related visual compositions.

Strong inclusion signals include:

- Explicit element-level layout or structured composition.
- Typography or text placement as part of design generation.
- Content-aware composition over a background, product image, or other visual asset.
- Layered, editable, transparent, isolated, or otherwise composable design assets.
- Graphic-design-specific multimodal agents or design assistants.
- Scientific figures, graphical abstracts, posters, or slide workflows that combine source understanding with visual communication.
- Datasets, benchmarks, or metrics created for graphic-design generation or evaluation.
- Historically important design-layout systems that establish a technique, representation, or interaction pattern used by later generation work.

Generally out of scope:

- Generic text-to-image generation without a graphic-design-specific contribution.
- Generic image editing without a composition or design focus.
- Generic UI, web, floorplan, scene, or document generation unless it materially advances graphic-design generation.
- Product catalogs, marketing-only pages, prompt collections, or uncurated directories.
- Resources that are deprecated, inaccessible, or too incomplete to evaluate, unless their historical or methodological relevance justifies retaining them with an explicit release-status note.

## Source of Truth

Structured data is authoritative; `README.md` is generated and should not be edited directly.

- `data/resources.csv` contains papers, datasets, benchmarks, evaluation methods, implementations, related resources, and optional inline paper architecture annotations.
- `data/paper_metadata.csv` stores optional implementation and reproducibility metadata for paper entries.
- `data/venues.csv` contains the relevant conference, journal, and workshop index.
- `templates/README.md.j2` defines the README presentation.
- `scripts/generate_readme.py` validates, joins, sorts, and renders the data.

The generator environment is managed with `uv` and `pyproject.toml`. After changing structured data or the template, run:

```bash
uv sync
uv run python scripts/generate_readme.py
```

The `Catalog Check` workflow verifies that the committed README exactly matches the canonical CSV data and template.

## Publication Dates and Ordering

The resource CSV records both `arxiv_date` and `venue_date` when known. These fields have distinct semantics:

- `arxiv_date` is the arXiv v1 submission date.
- For a **conference paper**, `venue_date` is the official start date of that conference edition, not the paper's individual poster/oral session date, acceptance date, camera-ready date, or proceedings publication timestamp.
- For a **workshop paper**, `venue_date` is the date of the specific workshop edition, not the start date of its host conference.
- For a **journal paper**, `venue_date` is the first authoritative online/publication date.
- For datasets, models, implementations, or other non-publication resources, `venue_date` may store an authoritative public release date.

The generated list is sorted by **first public appearance**, newest first, using the earlier of `arxiv_date` and `venue_date` when both are known. Thus an arXiv preprint normally determines chronology when it predates the venue, while a venue or release date determines chronology when no earlier arXiv version exists.

Use ISO dates (`YYYY-MM-DD`). Prefer primary evidence such as the arXiv submission history, the official conference or workshop site, publisher publication metadata, or an official model/dataset release record. `date_note` should briefly state the basis for the date, for example `CVPR 2025 conference start`, `ICCV 2025 HiGen workshop date`, `journal online publication`, or `official repository release date`.

Do not use a paper-specific presentation slot or an early proceedings-publication timestamp as `venue_date` merely because it is easier to locate. The field is normalized deliberately so that two papers at the same conference edition share the same venue date unless they belong to different colocated workshops.

If neither date is known, leave both blank and document the reason in `date_note`; the generator places the resource in `Other`.

The year headings in `README.md` correspond to the first-public-appearance date, not necessarily the eventual conference or journal year. For example, an ECCV 2026 paper first posted to arXiv in December 2025 appears under 2025.

Within a year, the exact first-public date determines ordering. The resource name is used only as a deterministic tie-breaker when two resources have the same date.

## Paper Taxonomy

Classify papers by their **primary output and task**, not by model family. `LLM`, `VLM`, `diffusion`, `agent`, or similar terms describe a method and should not determine the category by themselves.

- **Content-Agnostic Layout Generation**: the primary output is structured element geometry or arrangement, without depending on the visual content of a target canvas.
- **Content-Aware Layout Generation**: the primary output is still layout or placement, but geometry is conditioned on a background image, product/brand assets, saliency, element content, or another visual canvas.
- **Graphic Design Generation**: the system goes beyond layout coordinates and creates a composed design artifact, including some combination of background imagery, visual assets, typography, styling, layers, or editable HTML/CSS/PSD/PPTX structure.
- **Composable and Layered Asset Generation**: the primary output is a transparent, separable, layered, chroma-keyed, or intentionally empty-space visual asset intended for downstream composition or independent editing. This includes RGBA layer generation, layer decomposition when the emphasis is asset extraction, chroma-key generation, and negative-space-preserving generation.
- **Typography and Text Rendering**: the primary contribution is faithful, legible, spatially controlled, or stylized text rendering within designed imagery.
- **Graphic Design Editing and Reconstruction**: the primary contribution is iterative editing, layer-level manipulation, raster-to-editable reconstruction, or recovery of design structure.
- **Scientific Figure and Graphical Abstract Generation**: the system converts scholarly papers or long-form technical content into methodology diagrams, Figure 1-style summaries, scientific illustrations, or graphical abstracts. Editable SVG/vector outputs and source-grounded figure refinement belong here when figure generation is the primary task.
- **Scientific Poster and Slide Generation**: the system targets research communication through posters or slide decks and combines source-document understanding or content selection with layout, typography, rendering, and often editable output.

When a work spans categories, choose the category that best describes its principal output. For example, a VLM that predicts poster bounding boxes is a layout paper; an agent that creates editable HTML/CSS posters is a graphic-design-generation paper; a model whose main output is a reusable stack of RGBA assets belongs under composable and layered asset generation; a system that turns a paper into an editable methodology SVG belongs under scientific figure and graphical abstract generation.

## Architecture Annotations

For paper entries, use the optional `architecture` field in `data/resources.csv` for a short method-family label. Prefer compact values such as `Diffusion`, `Autoregressive / Transformer`, `LLM`, `VLM`, `Agentic / Multi-stage System`, `GAN`, `VAE`, `Flow Matching`, or `Knowledge-Based / Rule-Based`. Use `LLM` for language-only model components and `VLM` only when the model materially consumes visual input.

When more than one family materially applies, separate them with semicolons, for example `Diffusion; VLM`. Keep implementation details in the paper description or reproducibility metadata rather than expanding `architecture` into a long method summary.

## Resource Taxonomy

Do not force `dataset` and `benchmark` into separate, mutually exclusive buckets. Research artifacts frequently serve both roles.

- **Datasets and Benchmarks** contains reusable corpora, design assets, annotations, training examples, benchmark test sets, and fixed evaluation tasks/splits/protocols. A dataset becomes benchmark-like when the release defines how systems should be tested or compared, but it remains a single canonical entry in this section.
- **Evaluation Methods and Metrics** contains reusable scoring functions or evaluation procedures that can be applied across models or datasets, such as learned layout-distribution distances, structural similarity measures, or design-principle evaluators.

Examples:

- A corpus of posters used for training belongs in **Datasets and Benchmarks**.
- A fixed scientific-figure test set with prompts and an evaluation protocol also belongs in **Datasets and Benchmarks**.
- A resource that includes both a training corpus and an official benchmark is listed once in **Datasets and Benchmarks**, with the description stating both roles.
- A metric such as Layout FID or LTSim belongs in **Evaluation Methods and Metrics**.

New resource rows should use the canonical section names `Datasets and Benchmarks` or `Evaluation Methods and Metrics`. All resource rows must use these canonical section names; legacy bootstrap section names are no longer accepted.

## Implementation Metadata

`data/paper_metadata.csv` is optional per paper, but strongly encouraged when an official implementation, model release, or project page exists. The row key must exactly match the paper `name`.

Track the following when they can be verified from primary sources:

- project page;
- official code repository;
- released weights or checkpoints;
- code release status;
- weights release status;
- model family and backbone/base model;
- training datasets;
- evaluation datasets or benchmarks;
- output representation or artifact format;
- concise notes about partial, withdrawn, or otherwise limited releases;
- `checked_at`, the date on which the implementation/release status was last verified.

A metadata row means the implementation status has actually been inspected. If a paper has not been checked yet, omit the metadata row rather than filling every field with `unknown`. Blank URLs in an inspected row mean no canonical URL was located at `checked_at`; the status fields should explain whether a release is absent, announced, withdrawn, not applicable, or simply uncertain.

Allowed `code_status` values:

- `train+inference` — public training and inference paths are available;
- `inference-only` — released code runs a trained model but does not reproduce training;
- `evaluation-only` — public code primarily covers evaluation;
- `pipeline` — an agent/tool or training-free workflow without a task-specific training release;
- `announced` — authors state that code is forthcoming;
- `withdrawn` — code was previously available but the official maintainers explicitly removed or disabled the usable release;
- `none` — authors explicitly do not release code;
- `unknown` — release status could not be established.

Allowed `weights_status` values are `released`, `partial`, `announced`, `withdrawn`, `not-applicable`, and `unknown`.

Do not infer `train+inference` merely because a paper describes training. Inspect the public repository and distinguish a released training implementation from an inference-only demo. Likewise, mark weights as `released` only when an actual checkpoint/model artifact is linked or the official repository provides a working download path. Use `withdrawn` when an official source states that a previously available release has been removed; do not silently downgrade it to `unknown`.

For `model_family` and `backbone`, distinguish the task-level architecture from the reused foundation model. For example, `Multi-conditional diffusion transformer` belongs in `model_family`, while `FLUX.1-dev` belongs in `backbone`.

For `train_datasets` and `eval_datasets`, record the datasets actually used by the paper or released implementation, not merely datasets that the codebase could theoretically load. Separate multiple datasets with semicolons.

## Curation Standard

Before proposing an entry, verify that it is materially useful to this topic and that you can explain why it belongs. Prefer leaving borderline resources out rather than broadening the scope.

Do not stop at a user-supplied paper name. When adding a research line, inspect the paper's related work, citations, project page, and neighboring contemporary work to identify material omissions. Curate the resulting family rather than mechanically importing every cited paper.

External bibliographies, surveys, spreadsheets, technology maps, and reading lists are useful discovery sources, but they are not completeness targets or repository-level sources of truth. Inclusion is determined by this repository's scope and curation standard.

Use primary sources whenever possible:

1. Official paper, project, repository, model, or dataset page.
2. Author-maintained mirror or institutional page.
3. Reputable archival source when the primary resource is unavailable.

Avoid duplicate entries. If one work exposes a paper, code, dataset, and project page, choose one canonical entry and include secondary links through `data/paper_metadata.csv` when they add material value. If a released dataset is itself the main benchmark artifact, prefer one dataset/benchmark entry rather than duplicating the associated paper under another resource section.

## V1 Baseline and Ongoing Maintenance

The initial catalog is ready to be treated as **v1** when all of the following are true:

- The scope and task/output taxonomy are documented and stable enough for normal contributions.
- Publication dates are sufficient for deterministic first-public-appearance ordering, or an explicit `date_note` explains why a date is unavailable.
- The major task families are represented by foundational work and a useful set of recent work; no known omission changes the shape of the taxonomy itself.
- `README.md` is fully generated from canonical data and `Catalog Check` passes.
- Awesome-list content checks pass; repository-setting failures such as description/topics are handled separately.

The following are **not** v1 blockers:

- Exhaustively importing every paper from a survey, citation graph, spreadsheet, technology map, workshop, or external bibliography.
- Completing implementation/reproducibility metadata for every paper.
- Proving that no relevant paper exists outside the catalog.
- Listing every potentially relevant venue, workshop, commercial tool, or adjacent UI/document-generation system.

After v1, maintain the catalog incrementally. Prefer focused pull requests that add a coherent research line, refresh implementation status, repair links, or refine taxonomy. Periodic coverage audits are useful, but they should produce concrete, scoped changes rather than keep the bootstrap phase open indefinitely.

## Entry Format

Each resource CSV row corresponds to one rendered list item. Descriptions should be objective and concise.

Requirements:

- Start the description with an uppercase letter.
- End the description with a period.
- Describe the contribution rather than using promotional language.
- Use the canonical name used by the authors or maintainers.
- Add venue and year when they are known and useful.
- Do not add badges to individual entries.

## Pull Requests

Keep pull requests focused. A PR that adds one research line or a few related entries is easier to review than a large unsorted import.

Before submitting:

- Confirm every link resolves to the intended resource.
- Search `data/resources.csv` for duplicates and alternate names.
- Confirm the resource is within scope and in the narrowest task/output category.
- Add or update the paper `architecture` value in `data/resources.csv` when it materially helps explain the paper.
- Check related work and neighboring research for obvious omissions in the same line.
- Verify `arxiv_date` and/or `venue_date` from primary sources and apply the normalized date semantics above.
- Verify any implementation metadata against the official project/repository/model release.
- Set `checked_at` whenever adding or refreshing implementation metadata.
- Write an objective description that explains why the resource is useful.
- Run `uv run python scripts/generate_readme.py`.
- Run `uv run python scripts/generate_readme.py --check`.
- Run `npx awesome-lint` from a full Git checkout.

In the pull request description, briefly explain why each new resource belongs in this list. For less obvious entries, state the graphic-design-specific contribution explicitly.

## Commercial Tools

Commercial systems may be included only when they provide substantial research, reproducibility, or technical value that cannot be represented by a paper, dataset, or open implementation. This list should not become a vendor directory.

## Maintenance

Broken, superseded, or abandoned resources may be removed when they no longer provide enough value to justify inclusion. If an authoritative replacement exists, prefer updating the canonical link over retaining multiple versions. When a historically important release is intentionally withdrawn, keep the paper if it remains in scope and record the current release status explicitly.
