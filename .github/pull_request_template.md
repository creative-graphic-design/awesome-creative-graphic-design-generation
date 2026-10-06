## Summary

Describe what this pull request adds, removes, or reorganizes.

## Why it belongs

Explain the graphic-design-specific contribution of each proposed resource. For borderline entries, state why the work is more than generic image, UI, or document generation.

## Checklist

- [ ] I read `CONTRIBUTING.md` and confirmed the resource is in scope.
- [ ] I edited structured data rather than `README.md` directly.
- [ ] I linked to a primary or authoritative paper/resource source where possible.
- [ ] I searched the structured data for duplicates and alternate names.
- [ ] I verified `arxiv_date` / `venue_date` from primary evidence where applicable.
- [ ] I used the narrowest existing category that fits.
- [ ] If implementation metadata is included, I verified project/code/weights status from official sources and set `checked_at`.
- [ ] Training/evaluation datasets and base models reflect what the paper or released implementation actually uses.
- [ ] Each description is objective, concise, starts with an uppercase letter, and ends with a period.
- [ ] I verified that all added links resolve to the intended resources.
- [ ] I ran `uv run python scripts/generate_readme.py` and committed the generated `README.md`.
- [ ] I ran `uv run python scripts/generate_readme.py --check`.
- [ ] I ran `npx awesome-lint` from a full Git checkout.
