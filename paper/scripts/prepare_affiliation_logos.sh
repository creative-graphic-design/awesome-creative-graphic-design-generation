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
    curl --fail --location --silent --show-error --retry-all-errors --retry 3 --retry-delay 2 --connect-timeout 12 --max-time 50 \
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

# Salesforce Brand Central directs small printed uses to the BLUE CLOUD ONLY,
# never to the text-in-cloud or horizontal wordmark. Extract the original
# filled cloud shape from the official corporate RGB SVG without redrawing.
if grep -Fq '}{salesforce}' "$figure"; then
  mkdir -p figs/assets/logos
  sf_zip=figs/assets/logos/salesforce-official.zip
  sf_sha=b8cca7fa6290153156dc0d260095079d0cb0708c
  if [ ! -f "$sf_zip" ] || ! printf '%s  %s\n' "$sf_sha" "$sf_zip" | sha1sum -c -s; then
    curl --fail --location --silent --show-error --retry 3 --connect-timeout 20 --max-time 120 \
      'https://salesforce.widen.net/s/mzhhvlhsdg/salesforce-corporate-logo-all' -o "$sf_zip"
  fi
  printf '%s  %s\n' "$sf_sha" "$sf_zip" | sha1sum -c
  python3 - "$sf_zip" <<'PY'
import hashlib
from pathlib import Path
from sys import argv
from xml.etree import ElementTree as ET
from xml.sax.saxutils import quoteattr
from zipfile import ZipFile

path = 'Salesforce-Corporate-Logo-All/Cloud Logo RGB/Salesforce-Corporate-Logo-Cloud-RBG.svg'
with ZipFile(argv[1]) as archive:
    original = archive.read(path)
actual = hashlib.sha1(original).hexdigest()
expected = 'a05d80d66796327adad13e0574c4fa78b526545c'
if actual != expected:
    raise SystemExit(f'FAIL Salesforce original SVG digest: {actual}, expected {expected}')
root = ET.fromstring(original)
assert root.attrib.get('viewBox') == '0 0 205.73 144', 'Cloud symbol source changed'
paths = [p for p in root.iter()
         if p.tag.endswith('path') and p.attrib.get('class') == 'cls-3']
if len(paths) != 1 or len(paths[0].attrib.get('d','')) < 100:
    raise SystemExit('FAIL Salesforce original blue cloud must be a single source path')
# Preserve the original blue path data and fill; omit only the white wordmark.
d = quoteattr(paths[0].attrib['d'])
out = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 205.73 205.73"><path fill="#00b3ff" transform="translate(0 30.865)" d=' + d + '/></svg>\n'
Path('figs/assets/logos/salesforce-symbol.svg').write_text(out)
print('Salesforce: SHA-1-pinned original RGB cloud path, symbol-only square.')
PY
  rsvg-convert --format pdf --output figs/assets/logos/salesforce.pdf \
    figs/assets/logos/salesforce-symbol.svg
  test -s figs/assets/logos/salesforce.pdf
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

# Official Meituan parent-company media archive (not delivery / Dianping marks).
# Its PDF-compatible Illustrator vector contains both a square emblem and a
# horizontal wordmark; preserve only the unaltered square using a TeX viewport.
if grep -Fq '}{meituan-symbol}' "$figure"; then
  command -v unzip >/dev/null 2>&1 || { echo 'unzip required for original Meituan AI' >&2; exit 1; }
  meituan_zip=figs/assets/logos/meituan-official.zip
  meituan_zip_sha=6817f88d95f95bb6e6b8238aa0c0e7d36dd93008
  meituan_ai=figs/assets/logos/meituan-original.ai
  meituan_ai_sha=0df68fc2b3b25ddbeaa7f4046c0f74b3aae2fb05
  mkdir -p figs/assets/logos
  if [ ! -f "$meituan_zip" ] || ! printf '%s  %s\n' "$meituan_zip_sha" "$meituan_zip" | sha1sum -c -s; then
    curl --fail --location --silent --show-error --retry 3 --connect-timeout 15 --max-time 75 \
      'https://s3plus.meituan.net/smart/22c45b30-80ba-4aa5-bfad-2bfaed7beb4e.zip' -o "$meituan_zip"
  fi
  printf '%s  %s\n' "$meituan_zip_sha" "$meituan_zip" | sha1sum -c
  meituan_entry="$(unzip -Z -1 "$meituan_zip" | grep -v '^__MACOSX/' | grep -Ei '\.ai$')"
  [ "$(printf '%s\n' "$meituan_entry" | wc -l)" -eq 1 ] || { echo 'Expected one Meituan original AI' >&2; exit 1; }
  unzip -p "$meituan_zip" "$meituan_entry" >"$meituan_ai"
  printf '%s  %s\n' "$meituan_ai_sha" "$meituan_ai" | sha1sum -c
  head -c 5 "$meituan_ai" | grep -q '^%PDF-' || { echo 'Meituan original is no longer PDF-compatible' >&2; exit 1; }
  cp "$meituan_ai" figs/assets/logos/meituan-original.pdf
  (
    cd figs/assets/logos
    pdflatex -interaction=nonstopmode -halt-on-error meituan-symbol.tex >/dev/null
    test -s meituan-symbol.pdf
    rm -f meituan-symbol.aux meituan-symbol.log
  )
  echo "meituan-symbol: original parent-company square vector mark, draft only."
fi

if grep -Fq '}{pku}' "$figure"; then
  prepare_svg pku 14ffd592f63fb7231f71639e37b586467be667ea \
    https://upload.wikimedia.org/wikipedia/commons/f/f4/Peking_University_seal.svg
fi

# Additional compact originals or unchanged short institutional wordmarks
# identify individual studies in the 26-node draft. Preserve source SHA-1 and
# treat institutional/trademark print permissions separately.
if grep -Fq '}{utokyo}' "$figure" || grep -Fq '\MapLogoPair{utokyo}{cyberagent-symbol}' "$figure"; then
  prepare_svg utokyo 3d2c55ba43c606c9c7563677aca709b49a797d9e \
    'https://upload.wikimedia.org/wikipedia/commons/d/d8/University_of_Tokyo_symbol.svg'
fi
if grep -Fq '}{berkeley}' "$figure"; then
  prepare_svg berkeley dfb5fb42fc8533a6a6b0d07cf350770a3cb88d6a \
    'https://upload.wikimedia.org/wikipedia/commons/6/6f/The_University_of_California_Berkeley_1868.svg'
fi
if grep -Fq '}{ucsd}' "$figure"; then
  prepare_svg ucsd c4d91d3aa318092f553439fa8e3820f62efb996e \
    'https://upload.wikimedia.org/wikipedia/commons/c/c1/Seal_of_the_University_of_California%2C_San_Diego.svg'
fi
if grep -Fq '}{adobe}' "$figure"; then
  prepare_svg adobe 471dcc4a658857f96ea2b85f40dadfa15a455319 \
    'https://upload.wikimedia.org/wikipedia/commons/b/b1/Adobe_Corporate_Horizontal_Red_HEX.svg'
fi
if grep -Fq '}{epfl}' "$figure"; then
  prepare_svg epfl 5aae170a1e6c06178309e87d19cca7e2770dd9ec \
    'https://upload.wikimedia.org/wikipedia/commons/9/95/Logo_EPFL_2019.svg'
fi
if grep -Fq '}{alibaba}' "$figure"; then
  prepare_svg alibaba 42e5896c316a2394d5744812174641cb5710cbcd \
    'https://upload.wikimedia.org/wikipedia/commons/4/41/Alibaba_en_logo.svg'
fi
