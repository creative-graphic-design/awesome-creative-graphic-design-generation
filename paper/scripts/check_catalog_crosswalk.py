#!/usr/bin/env python3
"""Reconcile the public-paper catalog with the manuscript bibliography.

This is a conservative automatic ID/title crosswalk, not an inclusion/exclusion audit.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAPER = ROOT / "paper"
CROSSWALK = PAPER / "catalog_citation_crosswalk.csv"
CATALOG = ROOT / "data" / "resources.csv"
BIB = PAPER / "references.bib"
errors = []

with CATALOG.open(newline="", encoding="utf-8") as f:
    catalog = {r["name"]: r for r in csv.DictReader(f) if r["section"] == "Papers"}
with CROSSWALK.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

bib = BIB.read_text(encoding="utf-8")
entries = {}
starts = list(re.finditer(r"(?m)^@(?:article|inproceedings|misc)\{([^,]+),", bib))
for i, m in enumerate(starts):
    part = bib[m.end():starts[i + 1].start() if i + 1 < len(starts) else len(bib)]
    def field(name):
        match = re.search(rf"(?m)^\s*{name}\s*=\s*\{{(.*)\}},?\s*$", part)
        return match.group(1).removeprefix("{").removesuffix("}") if match else ""
    entries[m.group(1)] = {name: field(name) for name in ("title", "url", "eprint")}

def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())

def arxiv(s):
    found = re.search(r"arxiv\.org/abs/(\d{4}\.\d+)", s or "")
    return found.group(1) if found else ""

seen = set()
for r in rows:
    title = r["catalog_title"]
    if title in seen:
        errors.append(f"duplicate title: {title}")
    seen.add(title)
    paper = catalog.get(title)
    if paper is None:
        errors.append(f"no catalog record: {title}")
        continue
    if r["catalog_url"] != paper["url"] or r["catalog_arxiv_url"] != paper["arxiv_url"]:
        errors.append(f"catalog URL out of date: {title}")
    candidates = []
    identifier = arxiv(paper["arxiv_url"] or paper["url"])
    for key, entry in entries.items():
        if identifier and identifier in (entry["eprint"], arxiv(entry["url"])):
            candidates.append((key, "arxiv_id"))
        elif paper["url"] == entry["url"]:
            candidates.append((key, "url"))
        elif norm(title) == norm(entry["title"]):
            candidates.append((key, "title"))
    matched = bool(candidates)
    if r["status"] != ("matched" if matched else "unmatched"):
        errors.append(f"stale catalog-match status: {title}")
    if matched and r["bibtex_key"] not in {key for key, _ in candidates}:
        errors.append(f"invalid bibliography match: {title} -> {r['bibtex_key']}")
    if not matched and (r["bibtex_key"] or r["match_method"]):
        errors.append(f"unmatched catalog entry has BibTeX key: {title}")

if seen != set(catalog):
    errors.append(f"catalog/crosswalk coverage differs (missing={len(set(catalog)-seen)}, extra={len(seen-set(catalog))})")
print(f"Public catalog: {len(catalog)} papers, crosswalk: {len(rows)} rows, "
      f"matched: {sum(r['status'] == 'matched' for r in rows)}")
if errors:
    for e in errors:
        print("ERROR:", e, file=sys.stderr)
    raise SystemExit(1)
print("Catalog-to-bibliography crosswalk validated; unresolved records are not exclusions")
