# Paper-scoped agent guidance

Applies to every manuscript file under `paper/**` in addition to the repository-root `AGENTS.md`.

**Before editing and before every commit:** read `paper/WRITING_CHECKLIST.md` in full. It is the source of truth for author comments accumulated across manuscript revisions. Do not duplicate or bypass it.

For manuscript changes:
1. Follow the original paper/publisher record when writing scientific and bibliographic claims. Keep evidence tiers explicit; the awesome catalogue alone is not a paper-level experiment audit.
2. Write the Introduction as coherent argumentation with specific original citations for task claims, not an artificial taxonomy list. Use **one sentence per physical TeX line**, a blank line between paragraphs, and `\\citet{key}` for textual author mentions. Keep numbered section files (`01_abstract.tex`, `02_introduction.tex`, etc.).
3. Keep diagrams in `paper/figs/tex/`, generated vector PDFs in `paper/figs/pdf/`, and tables in `paper/tabs/tex/`. Keep figure captions in float wrappers and table captions with tables.
4. Keep `\\usepackage[review]{cvpr}` and non-identifying template author placeholders so the rendered manuscript remains anonymous.
5. Before committing run `python3 paper/scripts/check_sentence_lines.py`, `python3 paper/scripts/check_manuscript.py`, `python3 paper/scripts/check_bibliography.py` and `cd paper && make pdf`. Examine the resulting PDF for layout quality.
6. After pushing verify the **Paper PDF** Actions check and inspect its generated PDFs. Record unfinished audits rather than claiming research is complete.

The root `AGENTS.md`, `CONTRIBUTING.md`, and `data/README.md` still govern the research catalogue; this file governs paper-specific work only.

When introducing an acronym or a named model, add an entry to `paper/acronyms.tex` using CTAN `acro` and `\DeclareAcronym`.
Use `\ac{key}` (or `\acp{key}` for plurals) in prose.
Keep separate abbreviation and named-system classes; use `first-style=short` for named systems, avoiding invented backronyms.
The manuscript and CI checks must validate all keys, and the rendered lists and first mentions must be visually reviewed.
