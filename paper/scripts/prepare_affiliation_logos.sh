#!/bin/sh
# Convert ONLY opt-in source-verified affiliation logos to vector PDFs.
# Every remote SVG is pinned to its original SHA-1, not a mutable CDN image.
set -eu
cd "$(dirname "$0")/.."

figure=figs/tex/research_map_narrative.tex
if grep -Fq '\AffilBrand{1}{cyberagent}' "$figure"; then
  # Commons' PD-textlogo concerns copyright only; academic trademark use is
  # a separate, explicitly provisional nominative-use review (see registry).
  svg=figs/assets/logos/cyberagent.svg
  pdf=figs/assets/logos/cyberagent.pdf
  expected=6e364a261c7cfc57a6f434fee0aeff3fb1184a88
  url=https://upload.wikimedia.org/wikipedia/commons/a/ae/CyberAgent_logo.svg
  mkdir -p figs/assets/logos
  if ! printf '%s  %s\n' "$expected" "$svg" | sha1sum -c --status; then
    command -v curl >/dev/null 2>&1 || { echo 'curl required for opt-in CyberAgent mark' >&2; exit 1; }
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
  echo 'CyberAgent logo: pinned original SVG converted to vector PDF (academic preview only).'
fi
