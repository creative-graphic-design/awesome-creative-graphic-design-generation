#!/usr/bin/env python3
"""Fail on structurally invalid or unused manuscript BibTeX entries.

This is deliberately a conservative lexical check for our restricted,
one-field-per-line BibTeX convention, not a general BibTeX parser.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
bibfile = ROOT / "references.bib"
source = bibfile.read_text(encoding="utf-8")
entries = {}
errors: list[str] = []

start_re = re.compile(r"(?m)^@(article|inproceedings|misc)\{([^,{}\s]+),\s*$")
starts = list(start_re.finditer(source))
if not starts:
    errors.append("No supported BibTeX entries found")

for idx, match in enumerate(starts):
    kind, key = match.groups()
    chunk = source[match.end() : starts[idx + 1].start() if idx + 1 < len(starts) else len(source)]
    if key in entries:
        errors.append(f"{key}: duplicate citation key")
    entries[key] = chunk
    # Inspect field starts; individual fields use a one-line field key.
    fields = set(re.findall(r"(?m)^\s*([a-z_]+)\s*=\s*\{", chunk))
    for needed in ("author", "title", "year", "url"):
        if needed not in fields:
            errors.append(f"{key}: missing {needed}")
    if kind == "article" and "journal" not in fields:
        errors.append(f"{key}: @article missing journal")
    if kind == "inproceedings" and "booktitle" not in fields:
        errors.append(f"{key}: @inproceedings missing booktitle")
    if re.search(r"(?im)^\s*author\s*=\s*\{[^}]*\band others\b", chunk):
        errors.append(f"{key}: unresolved author placeholder")
    if chunk.count("{") + 1 != chunk.count("}"):
        errors.append(f"{key}: unbalanced braces")

cite_re = re.compile(r"\\cite(?:p|t|alp|alt)?(?:\[[^\]]*\])?\{([^}]+)\}")
references = set()
usage_count = 0
for tex in sorted(ROOT.rglob("*.tex")):
    if "build" in tex.parts:
        continue
    text = tex.read_text(encoding="utf-8")
    for match in cite_re.finditer(text):
        for name in match.group(1).split(","):
            references.add(name.strip())
            usage_count += 1

unknown = references - set(entries)
unused = set(entries) - references
if unknown:
    errors.append("Undefined cite keys: " + ", ".join(sorted(unknown)))
if unused:
    errors.append("Unused BibTeX entries: " + ", ".join(sorted(unused)))

print(f"BibTeX entries: {len(entries)}, unique cited: {len(references)}, cite uses: {usage_count}")
if errors:
    for message in errors:
        print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)
print("BibTeX structural/citation check passed")
