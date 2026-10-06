# Contribution Guidelines

Thank you for helping curate Awesome Creative Graphic Design Generation. The goal is a focused, high-signal list, not an exhaustive directory.

## Scope

A resource is in scope when it makes a direct contribution to the generation, editing, representation, understanding, or evaluation of composed graphic-design artifacts such as posters, advertisements, social-media graphics, magazine/editorial layouts, scientific posters, slides, banners, and related visual compositions.

Strong inclusion signals include:

- Explicit element-level layout or structured composition.
- Typography or text placement as part of design generation.
- Content-aware composition over a background, product image, or other visual asset.
- Layered, editable, or structured design outputs.
- Graphic-design-specific multimodal agents or design assistants.
- Scientific-poster or slide workflows that combine source understanding with visual communication.
- Datasets, benchmarks, or metrics created for graphic-design generation or evaluation.
- Historically important design-layout systems that establish a technique, representation, or interaction pattern used by later generation work.

Generally out of scope:

- Generic text-to-image generation without a graphic-design-specific contribution.
- Generic image editing without a composition or design focus.
- Generic UI, web, floorplan, scene, or document generation unless it materially advances graphic-design generation.
- Product catalogs, marketing-only pages, prompt collections, or uncurated directories.
- Resources that are deprecated, inaccessible, or too incomplete to evaluate.

## Source of Truth

Structured data is authoritative; `README.md` is generated and should not be edited directly.

- `data/resources*.csv` contains papers, datasets, benchmarks, implementations, and related resources.
- `data/paper_metadata.csv` stores optional implementation and reproducibility metadata for paper entries.
- `data/venues.csv` contains the relevant conference and journal index.
- `templates/README.md.j2` defines the README presentation.
- `scripts/generate_readme.py` validates, joins, sorts, and renders the data.

The generator environment is managed with `uv` and `pyproject.toml`. After changing structured data or the template, run:

```bash
uv sync
uv run python scripts/generate_readme.py
```

CI regenerates the README and fails if the committed output differs.

## Publication Dates and Ordering

The resource CSV records both `arxiv_date` and `venue_date` when known. The generated list is sorted by **first public appearance**, newest first:

1. Use the arXiv v1 date when it is the earliest public appearance.
2. If the work was presented or formally published at a venue before its arXiv upload, use the venue/presentation date instead.
3. Journal-only work uses its first public publication date.
4. If neither date is known, leave both blank and document the reason in `date_note`; the generator places the resource in `Other`.

Use ISO dates (`YYYY-MM-DD`). Prefer primary evidence such as the arXiv submission history, official conference program/schedule, proceedings page, or publisher publication date. `date_note` should briefly record the basis for any non-obvious date.

The year headings in `README.md` correspond to the first-public-appearance date, not necessarily the eventual conference or journal year. For example, an ECCV 2026 paper first posted to arXiv in December 2025 appears under 2025.

Within a year, the exact first-public date determines ordering. The resource name is used only as a deterministic tie-breaker when two resources have the same date.

## Paper Taxonomy

Classify papers by their **primary output and task**, not by model family. `LLM`, `VLM`, `diffusion`, `agent`, or similar terms describe a method and should not determine the category by themselves.

- **Layout Generation**: the primary output is structured element geometry or arrangement, without depending on the visual content of a target canvas.
- **Content-Aware Layout Generation**: the primary output is still layout or placement, but geometry is conditioned on a background image, product/brand assets, saliency, element content, or another visual canvas.
- **Graphic Design Generation**: the system goes beyond layout coordinates and creates a composed design artifact, including some combination of background imagery, visual assets, typography, styling, layers, or editable HTML/CSS/PSD/PPTX structure.
- **Typography and Text Rendering**: the primary contribution is faithful, legible, spatially controlled, or stylized text rendering within designed imagery.
- **Graphic Design Editing and Reconstruction**: the primary contribution is iterative editing, layer-level manipulation, raster-to-editable reconstruction, or recovery of design structure.
- **Scientific Poster and Slide Generation**: the system targets research communication and combines source-document understanding or content selection with layout, typography, rendering, and often editable poster/slide output.

When a work spans categories, choose the category that best describes its principal output. For example, a VLM that predicts poster bounding boxes is a layout paper; an agent that creates editable HTML/CSS posters is a graphic-design-generation paper.

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
- concise notes about partial releases or reproducibility limitations;
- `checked_at`, the date on which the implementation/release status was last verified.

A metadata row means the implementation status has actually been inspected. If a paper has not been checked yet, omit the metadata row rather than filling every field with `unknown`. Blank URLs in an inspected row mean no canonical URL was located at `checked_at`; the status fields should explain whether a release is absent, announced, not applicable, or simply uncertain.

Allowed `code_status` values:

- `train+inference` — public training and inference paths are available;
- `inference-only` — released code runs a trained model but does not reproduce training;
- `evaluation-only` — public code primarily covers evaluation;
- `pipeline` — an agent/tool workflow without a task-specific training release;
- `announced` — authors state that code is forthcoming;
- `none` — authors explicitly do not release code;
- `unknown` — release status could not be established.

Allowed `weights_status` values are `released`, `partial`, `announced`, `not-applicable`, and `unknown`.

Do not infer `train+inference` merely because a paper describes training. Inspect the public repository and distinguish a released training implementation from an inference-only demo. Likewise, mark weights as `released` only when an actual checkpoint/model artifact is linked or the official repository provides a working download path.

For `model_family` and `backbone`, distinguish the task-level architecture from the reused foundation model. For example, `Multi-conditional diffusion transformer` belongs in `model_family`, while `FLUX.1-dev` belongs in `backbone`.

For `train_datasets` and `eval_datasets`, record the datasets actually used by the paper or released implementation, not merely datasets that the codebase could theoretically load. Separate multiple datasets with semicolons.

## Curation Standard

Before proposing an entry, verify that it is materially useful to this topic and that you can explain why it belongs. Prefer leaving borderline resources out rather than broadening the scope.

Use primary sources whenever possible:

1. Official paper, project, repository, or dataset page.
2. Author-maintained mirror or institutional page.
3. Reputable archival source when the primary resource is unavailable.

Avoid duplicate entries. If one work exposes a paper, code, dataset, and project page, choose one canonical entry and include secondary links through `paper_metadata.csv` when they add material value.

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

Keep pull requests focused. A PR that adds one or a few related entries is easier to review than a large unsorted import.

Before submitting:

- Confirm every link resolves to the intended resource.
- Search all `data/resources*.csv` files for duplicates and alternate names.
- Confirm the resource is within scope and in the narrowest task/output category.
- Verify `arxiv_date` and/or `venue_date` from primary sources.
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

Broken, superseded, or abandoned resources may be removed when they no longer provide enough value to justify inclusion. If an authoritative replacement exists, prefer updating the canonical link over retaining multiple versions.
