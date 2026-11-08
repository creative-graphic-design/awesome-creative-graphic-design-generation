#!/usr/bin/env bash
# Fast, best-effort draft. For a fully converged, validated PDF use: make pdf
set -euo pipefail
cd "$(dirname "$0")/.."
for figure in overview edit_protocol research_map research_map_narrative; do
  if [[ ! -s "figs/pdf/$figure.pdf" ]]; then
    echo "One-time figure generation: $figure.pdf is missing"
    sh scripts/build_figures.sh
    break
  fi
done
flags=(-file-line-error -halt-on-error -interaction=nonstopmode)
# A completed canonical build already contains the bibliography generated from
# the same manuscript, since only the printed acro indexes differ.
if [[ ! -s main-fast.bbl && -s main.bbl ]]; then
  cp main.bbl main-fast.bbl
  echo "Reusing bibliography from main.bbl"
fi
if [[ -s main-fast.aux && -s main-fast.bbl ]]; then
  echo "Fast draft: one pdflatex pass (existing auxiliary files)"
  pdflatex "${flags[@]}" main-fast.tex
else
  echo "Fast draft: first-run bootstrap for references and citations"
  pdflatex "${flags[@]}" main-fast.tex
  if [[ ! -s main-fast.bbl ]]; then
    bibtex main-fast
  fi
  pdflatex "${flags[@]}" main-fast.tex
  # Resolve forward references introduced by the initial auxiliary file.
  pdflatex "${flags[@]}" main-fast.tex
fi
test -s main-fast.pdf
echo "Draft: paper/main-fast.pdf (not a fully converged proof; use make pdf for CI/print)"
