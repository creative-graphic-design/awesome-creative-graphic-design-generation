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

# Two compact, period-appropriate symbols (2012 Microsoft four-square mark,
# 2015 Google G) are independent original icons, not squeezed wordmarks.
# BIT main-campus 2026 A1-02 Illustrator master is in fact PDF 1.5.
# Preserve the exact official bytes and crop *only the artboard viewport*
# around the standalone emblem, not the logo paths themselves.
if grep -Fq '}{bit-symbol}' "$figure"; then
  bit_ai=figs/assets/logos/bit-original.ai
  bit_pdf=figs/assets/logos/bit-original.pdf
  bit_sha=6fcb6505b213d2f858e82ff51aab605a1771dc7c
  mkdir -p figs/assets/logos
  if [ ! -f "$bit_ai" ] || ! printf '%s  %s\n' "$bit_sha" "$bit_ai" | sha1sum -c -s; then
    curl --fail --location --silent --show-error --retry 3 --connect-timeout 15 --max-time 120 \
      'https://www.bit.edu.cn/docs//2026-03/023888b516cb4b939a6a1103cfb356ce.ai' -o "$bit_ai"
  fi
  printf '%s  %s\n' "$bit_sha" "$bit_ai" | sha1sum -c
  head -c 5 "$bit_ai" | grep -q '^%PDF-' || { echo 'BIT source no longer PDF-compatible; reject changed original' >&2; exit 1; }
  cp "$bit_ai" "$bit_pdf"
  (
    cd figs/assets/logos
    pdflatex -interaction=nonstopmode -halt-on-error bit-symbol.tex >/dev/null
    test -s bit-symbol.pdf
    rm -f bit-symbol.aux bit-symbol.log
  )
  echo "bit-symbol: square artboard crop from source-pinned official BIT vector (draft only)."
fi

if grep -Fq '}{google}' "$figure"; then
  prepare_svg google 2cc789a02534557380d92124e2f8b9483d198fb3 \
    'https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg'
fi
if grep -Fq '}{microsoft}' "$figure"; then
  prepare_svg microsoft 5b170117926ae5a5e451aa24676b5a124c2fa122 \
    'https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg'
fi

if grep -Fq '}{cyberagent-symbol}' "$figure"; then
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
if grep -Fq '}{pku}' "$figure"; then
  prepare_svg pku 14ffd592f63fb7231f71639e37b586467be667ea \
    https://upload.wikimedia.org/wikipedia/commons/f/f4/Peking_University_seal.svg
fi
