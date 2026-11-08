# acro conventions: citations, indexing, and provenance

This document records the author-approved conventions for the manuscript in PR #135. Read it before changing acronym markup, citations, or the printed indexes. Prefer the **stock \`acro\` package** over custom templates or commands. The implementation in \`main.tex\`, \`acronyms.tex\`, the two standalone source tables, and the checks under \`scripts/\` is authoritative if it changes; update this guide in the same commit.

## Why the rules differ between prose and tables

A named study has at least two separate roles in academic writing: (1) identifying a system and its original publication, and (2) supporting a specific factual or quantitative claim. An automatic citation on a system's *first* mention addresses the first role only. It is **not** evidence for every later claim mentioning that system. A table must also remain interpretable on its own, even if the study was introduced in an earlier section.

### Ordinary prose: first-use citation from \`acro\`

\`paper/main.tex\` uses:

\`\`\`latex
\acsetup{
  cite/cmd = \citep,
  cite/display = first,
  pages/display = all,
  pages/name = true,
  pages/seq/use = false
}
\`\`\`

For registered studies, give \`paper/acronyms.tex\` a real \`cite = {original_bibtex_key}\` (plus source metadata) and write **\`\ac{cole}\`**, not \`\ac{cole} \citep{cole2023}\`, when merely mentioning COLE. \`first-style=short\` retains the short system name at first use. The package adds the original publication citation at the first occurrence; subsequent mentions display the short name without repeating that automatic citation. Do not replace this with a custom formatter.

When a sentence states a result, makes a methodological comparison, or draws evidence from other work, **keep an explicit claim-level citation** (typically at the relevant clause or sentence end). Removing a redundant name citation does not license removing evidence. The same applies to groups of studies and comparisons whose source is not just the named study's registered original paper.

### Independent primary-study and benchmark tables

The tables \`tabs/tex/task_grounding.tex\` and \`tabs/tex/benchmark_coverage.tex\` must provide an explicit original-paper citation for each study/benchmark entry, including those already introduced in prose. Within each table's TeX group, use:

\`\`\`latex
\acsetup{cite/display=none}
...
\ac{posterlayout} \citep{posterlayout2023}
\`\`\`

This locally suppresses \`acro\`'s **automatic** citation, avoiding a duplicate when an entry happens to be its first occurrence. The explicit \`\citep\` remains visible regardless of earlier usage. Keep the citation key equal to the registered original publication. Outside this explicitly marked table context, \`\ac{key} \citep{same_original_key}\` is considered redundant.

**Do not substitute \`\ac*{key}\`** as a shortcut in those tables. A minimal compiled comparison showed that the starred form loses the appearance-page tracking needed by the printed indexes. We retain ordinary \`\ac\` inside a locally scoped citation-display setting instead. Scope is important: do not let \`cite/display=none\` leak into surrounding prose.

### Index and metadata preservation

Keep the three stock \`\printacronyms[include=...,heading=none,display=all]\` lists (abbreviations, systems, evaluation) and all occurrence-page indexes. Maintain original-source BibTeX keys, URLs, years and other metadata stored in \`acronyms.tex\`. Do not reintroduce \`survey-rich\`, \`\NewAcroTemplate\`, or a handwritten acronym list to solve a feature the stock package already supports. Source-linked metadata in the registry is not a claim that every field prints in the default list.

### Review and verification

- Run \`cd paper && make check\`; it includes manuscript, bibliography, named-resource and regression checks. \`check_manuscript.py\` rejects identical immediate \`\ac{key} \citep{registered_original}\` pairs in ordinary prose, but permits and verifies them in explicitly marked independent source tables. \`check_acro_names.py\` flags unwrapped registered names.
- Review claims previously accompanied by explicit citations **in context**, not by mechanical replacement alone; a first-use citation cannot guarantee later factual support.
- Compile a minimal real-\`acro\` example when changing package options, then build the **full PDF** and inspect the first-use citation, a repeated mention, both independent tables, and all three printed indexes with their appearance pages.
- Verify the current source-commit PDF and CI status before declaring completion. A passing lint, queued job, or successful toy example does not prove the manuscript PDF renders correctly.
- Document deviations and any still-unverified claims in \`WRITING_CHECKLIST.md\` rather than silently weakening the citation/index contract.

## Source locations

- Configuration: \`main.tex\`; registered terms and their original papers: \`acronyms.tex\`.
- Independent table exceptions: \`tabs/tex/task_grounding.tex\`, \`tabs/tex/benchmark_coverage.tex\`.
- CI and checks: \`scripts/check_manuscript.py\`, \`scripts/check_acro_names.py\`, \`scripts/tests/test_acro_citations.py\`, \`.github/workflows/paper-pdf.yml\` (repository root).
- Author feedback and acceptance requirements: \`WRITING_CHECKLIST.md\`; agent guidance: \`AGENTS.md\`.
