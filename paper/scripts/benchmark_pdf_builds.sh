#!/usr/bin/env bash
# Compare canonical and index-free draft TeX runs on the same machine.
set -euo pipefail
cd "$(dirname "$0")/.."
if [[ ! -s figs/pdf/overview.pdf || ! -s figs/pdf/edit_protocol.pdf || ! -s figs/pdf/research_map.pdf || ! -s figs/pdf/research_map_narrative.pdf ]]; then
  echo "Build figures first with: make figures" >&2
  exit 1
fi
mkdir -p build-timings
for base in main main-fast; do
  latexmk -C "$base.tex" >/dev/null
  start=$(date +%s)
  /usr/bin/time -f 'elapsed_seconds=%e max_rss_kb=%M' -o "build-timings/$base.time" \
    latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode "$base.tex" \
    >"build-timings/$base.build.log" 2>&1
  end=$(date +%s)
  echo "$base wall_seconds=$((end-start)) $(cat "build-timings/$base.time")"
  grep -c "Run number .* of rule 'pdflatex'" "build-timings/$base.build.log" || true
  test -s "$base.pdf"
done
echo "This compares fresh LaTeX/BibTeX runs, excluding source-figure compilation."
echo "The two modes differ in page count, so timings estimate the cost of the printed indexes plus downstream layout/reference convergence, not acro's total runtime."
