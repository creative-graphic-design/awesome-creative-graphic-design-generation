#!/bin/sh
# Render both original TikZ diagrams to vector PDFs.
set -eu
cd "$(dirname "$0")/.."
mkdir -p figs/pdf
for stem in overview edit_protocol research_map; do
  latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode \
    -outdir=figs/pdf "figs/tex/${stem}.tex"
  test -s "figs/pdf/${stem}.pdf"
done
