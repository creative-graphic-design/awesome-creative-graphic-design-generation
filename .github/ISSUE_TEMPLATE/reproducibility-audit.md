---
name: Reproducibility metadata audit
about: Track project/code/weights/base-model/dataset metadata for papers
---

## Scope

List the papers or paper family being audited.

## Metadata to verify

For each paper, verify against primary sources and update `data/paper_metadata.csv`:

- [ ] project page
- [ ] official code repository
- [ ] code status (`train+inference`, `inference-only`, `evaluation-only`, `pipeline`, `announced`, `none`, `unknown`)
- [ ] released weights/checkpoints and `weights_status`
- [ ] method/model family
- [ ] backbone/base/foundation model
- [ ] training datasets
- [ ] evaluation datasets / benchmarks
- [ ] output representation / artifact format
- [ ] reproducibility limitations in `notes`
- [ ] `checked_at`

Do not add a metadata row solely to fill fields with `unknown`; a row means the release state was actually inspected.
