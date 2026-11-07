#!/bin/sh
# Build only individually enabled original affiliation marks as vector PDFs.
# SHA-1 pinning prevents silent changes to upstream SVG files.
# Academic draft attribution does not establish permission for publication.
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
  if ! printf '%s  %s\n' "$expected" "$svg" | sha1sum -c --status; then
    command -v curl >/dev/null 2>&1 || { echo 'curl required for source-pinned draft mark' >&2; exit 1; }
    curl --fail --location --silent --show-error --retry 3 --connect-timeout 10 --max-time 60 "$url" -o "$svg"
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

if grep -Fq '\AffilBrand{1}{cyberagent}' "$figure"; then
  prepare_svg cyberagent 6e364a261c7cfc57a6f434fee0aeff3fb1184a88 \
    https://upload.wikimedia.org/wikipedia/commons/a/ae/CyberAgent_logo.svg
fi
if grep -Fq '\AffilBrandNamed{1}{pku}' "$figure"; then
  prepare_svg pku 965d9a8bdc1c391b75a0f88d729d54ea775ce180 \
    https://upload.wikimedia.org/wikipedia/commons/f/f4/Peking_University_seal.svg
fi
