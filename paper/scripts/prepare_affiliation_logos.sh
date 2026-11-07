#!/bin/sh
# Build only individually enabled original affiliation marks as vector PDFs.
# SHA-1 pinning prevents silent changes to upstream SVG files.
# Academic draft attribution does not establish permission for publication.
# Only research nodes which display each institution may enable its mark.
set -eu
cd "$(dirname "$0")/.."
figure=figs/tex/research_map_narrative.tex

prepare_svg() {
  stem="$1"
  expected="$2"
  url="$3"
  svg="figs/assets/logos/$stem.svg"
  pdf="figs/assets/logos/$stem.pdf"
  mkdir -p figs/assets/logos
  if [ ! -f "$svg" ] || ! printf '%s  %s\n' "$expected" "$svg" | sha1sum -c -s; then
    command -v curl >/dev/null 2>&1 || { echo 'curl required for source-pinned draft mark' >&2; exit 1; }
    curl --fail --location --silent --show-error --retry 3 --connect-timeout 10 --max-time 60 "$url" -o "$svg"
  fi
  if ! printf '%s  %s\n' "$expected" "$svg" | sha1sum -c -s; then
    echo "Unexpected logo bytes for $stem: SHA-1 and byte count follow (do not render)." >&2
    sha1sum "$svg" >&2
    wc -c "$svg" >&2
    exit 1
  fi
  printf '%s  %s\n' "$expected" "$svg" | sha1sum -c
  if command -v rsvg-convert >/dev/null 2>&1; then
    rsvg-convert --format pdf --output "$pdf" "$svg"
  elif command -v inkscape >/dev/null 2>&1; then
    inkscape "$svg" --export-type=pdf --export-filename="$pdf" >/dev/null
  else
    echo 'An SVG-to-vector-PDF converter is required (rsvg-convert or inkscape).' >&2
    exit 1
  fi
  test -s "$pdf"
  echo "$stem: original SVG converted to vector PDF (draft affiliation identification only)."
}

if grep -Fq '\MapPaperBrand{C}{OpenCOLE}{24}{opencole2024}' "$figure"; then
  prepare_svg cyberagent 6e364a261c7cfc57a6f434fee0aeff3fb1184a88 \
    https://upload.wikimedia.org/wikipedia/commons/a/ae/CyberAgent_logo.svg
  # Make an exactly square, *vector* CA mark tile from the unchanged, source-
  # pinned original. This does not distort or redraw the CA identity mark.
  (
    cd figs/assets/logos
    pdflatex -interaction=nonstopmode -halt-on-error cyberagent-symbol.tex >/dev/null
    test -s cyberagent-symbol.pdf
    rm -f cyberagent-symbol.aux cyberagent-symbol.log
  )
fi
if grep -Fq '\MapPaperBrand{C}{COLE}{23}{cole2023}' "$figure"; then
  prepare_svg pku 14ffd592f63fb7231f71639e37b586467be667ea \
    https://upload.wikimedia.org/wikipedia/commons/f/f4/Peking_University_seal.svg
fi
