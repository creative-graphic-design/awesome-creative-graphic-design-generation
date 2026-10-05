# Contribution Guidelines

Thank you for helping curate Awesome Creative Graphic Design Generation. The goal is a focused, high-signal list, not an exhaustive directory.

## Scope

A resource is in scope when it makes a direct contribution to the generation, editing, representation, understanding, or evaluation of composed graphic-design artifacts such as posters, advertisements, social-media graphics, magazine/editorial layouts, banners, and related visual compositions.

Strong inclusion signals include:

- Explicit element-level layout or structured composition.
- Typography or text placement as part of design generation.
- Content-aware composition over a background, product image, or other visual asset.
- Layered, editable, or structured design outputs.
- Graphic-design-specific multimodal agents or design assistants.
- Datasets, benchmarks, or metrics created for graphic-design generation or evaluation.

Generally out of scope:

- Generic text-to-image generation without a graphic-design-specific contribution.
- Generic image editing without a composition or design focus.
- Generic UI, web, floorplan, scene, or document generation unless it materially advances graphic-design generation.
- Product catalogs, marketing-only pages, prompt collections, or uncurated directories.
- Resources that are deprecated, inaccessible, or too incomplete to evaluate.

## Curation Standard

Before proposing an entry, verify that it is materially useful to this topic and that you can explain why it belongs. Prefer leaving borderline resources out rather than broadening the scope.

Use primary sources whenever possible:

1. Official paper, project, repository, or dataset page.
2. Author-maintained mirror or institutional page.
3. Reputable archival source when the primary resource is unavailable.

Avoid duplicate entries. If one work exposes a paper, code, dataset, and project page, choose one canonical entry and include secondary links only when they add material value.

## Entry Format

Use one line per resource:

```markdown
- [Resource Name](https://example.com) - Objective sentence explaining what the resource contributes (Venue Year).
```

Requirements:

- Start the description with an uppercase letter.
- End the description with a period.
- Describe the contribution rather than using promotional language.
- Keep the description concise and specific enough to justify inclusion.
- Use the canonical name used by the authors or maintainers.
- Add venue and year when they are known and useful.
- Do not add badges to individual entries.

## Categories

Choose the narrowest existing category that fits. Do not create a new top-level or paper subsection for a single item. Category changes should be motivated by a meaningful cluster of resources.

The current taxonomy is:

- Papers
  - Layout Generation.
  - Content-Aware Graphic Design.
  - Language and Multimodal Design Agents.
  - End-to-End Graphic Design Generation.
- Datasets.
- Benchmarks and Evaluation.
- Models and Implementations.
- Related Resources.

## Pull Requests

Keep pull requests focused. A PR that adds one or a few related entries is easier to review than a large unsorted import.

Before submitting:

- Confirm every link resolves to the intended resource.
- Search the README for duplicates and alternate names.
- Confirm the resource is within scope.
- Write an objective description that explains why it is useful.
- Keep Markdown formatting consistent with neighboring entries.
- Run `npx awesome-lint` from a full Git checkout.

In the pull request description, briefly explain why each new resource belongs in this list. For less obvious entries, state the graphic-design-specific contribution explicitly.

## Commercial Tools

Commercial systems may be included only when they provide substantial research, reproducibility, or technical value that cannot be represented by a paper, dataset, or open implementation. This list should not become a vendor directory.

## Maintenance

Broken, superseded, or abandoned resources may be removed when they no longer provide enough value to justify inclusion. If an authoritative replacement exists, prefer updating the canonical link over retaining multiple versions.
