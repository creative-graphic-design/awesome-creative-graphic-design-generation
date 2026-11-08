#!/bin/sh
# Render all original standalone TikZ diagrams to vector PDFs.
set -eu
cd "$(dirname "$0")/.."
mkdir -p figs/pdf
# The only remote mark is fetched by an explicit opt-in with a pinned digest.
sh scripts/prepare_affiliation_logos.sh
for stem in overview edit_protocol research_map research_map_narrative; do
  latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode \
    -outdir=figs/pdf "figs/tex/${stem}.tex"
  test -s "figs/pdf/${stem}.pdf"
done

# Source-audited, data-driven vector narrative map for the manuscript.
# Logos are prepared above; convert the generated SVG without rasterization.
python3 scripts/render_research_map_concept.py
python3 scripts/check_research_map_concept.py
rsvg-convert --format pdf --output figs/pdf/research_map_concept.pdf figs/pdf/research_map_concept.svg
test -s figs/pdf/research_map_concept.pdf

# Experimental 67-study SVG atlas: run separately when reviewing alternatives.
# python3 scripts/render_research_landscape.py
# rsvg-convert -f pdf -o figs/pdf/research_landscape.pdf figs/pdf/research_landscape.svg
