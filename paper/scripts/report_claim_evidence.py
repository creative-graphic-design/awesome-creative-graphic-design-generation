#!/usr/bin/env python3
"""Read-only citation-to-claim inventory for the scientific survey manuscript.

This lexical inventory does not decide whether the original paper supports
a claim. It never upgrades evidence or writes to the citation audit.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

PAPER = Path(__file__).resolve().parents[1]
CITE_RE = re.compile(r"\\cite(?:p|t|alp|alt)?(?:\[[^\]]*\])?\{([^}]+)\}")
ACRO_RE = re.compile(r"\\ac(?:p|f|s|l)?\{([^}]+)\}")
DECL_RE = re.compile(r"\\DeclareAcronym\{([^}]+)\}\{([\s\S]*?)\n\}")
QUANT_RE = re.compile(
    r"\b\d+(?:[.,]\d+)?(?:\\%|%)?\b|Table~|Fig(?:ure)?~|"
    r"\\ac\{(?:fid|iou|psnr|ssim|lpips)\}", re.I
)


def get_source_depths() -> dict[str, dict[str, str]]:
    with (PAPER / "literature_citation_audit.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        return {row["bibtex_key"]: row for row in csv.DictReader(handle)}


def get_acro_citations() -> dict[str, str]:
    declarations = (PAPER / "acronyms.tex").read_text(encoding="utf-8")
    answer = {}
    for match in DECL_RE.finditer(declarations):
        cite = re.search(r"(?m)^\s*cite\s*=\s*\{([^}]+)\}", match.group(2))
        if cite:
            answer[match.group(1)] = cite.group(1)
    return answer


def collect() -> list[dict[str, object]]:
    audit = get_source_depths()
    acro = get_acro_citations()
    findings = []
    sources = sorted((PAPER / "sections").glob("*.tex"))
    sources += sorted((PAPER / "tabs" / "tex").glob("*.tex"))
    for path in sources:
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip() or line.lstrip().startswith("%"):
                continue
            explicit = [
                name.strip() for match in CITE_RE.finditer(line)
                for name in match.group(1).split(",")
            ]
            implied = [acro[name] for name in ACRO_RE.findall(line) if name in acro]
            keys = sorted(set(explicit + implied))
            if not keys:
                continue
            missing = sorted(key for key in keys if audit.get(key, {}).get(
                "source_depth") != "methods_results")
            is_quant = bool(QUANT_RE.search(line))
            findings.append({
                "source_file": str(path.relative_to(PAPER)),
                "source_line": number,
                "citation_keys": keys,
                "source_depths": {key: audit.get(key, {}).get("source_depth", "missing")
                                  for key in keys},
                "mentions_quantity_or_table": is_quant,
                "requires_primary_claim_check": bool(missing and is_quant),
                "not_methods_results_keys": missing,
                "source_sentence": line.strip(),
            })
    return findings


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", action="store_true", help="Print counts and risks")
    parser.add_argument("--json", action="store_true", help="Print structured JSON")
    parser.add_argument("--limit", type=int, default=0, help="Limit printed rows")
    args = parser.parse_args()
    if args.limit < 0:
        parser.error("--limit must be non-negative")
    data = collect()
    if args.summary:
        grouped = Counter(item["source_file"] for item in data)
        risks = [item for item in data if item["requires_primary_claim_check"]]
        print(f"Citation-bearing source lines: {len(data)}")
        print(f"Numerical/table claims with non-methods-results sources: {len(risks)}")
        for name, count in sorted(grouped.items()):
            print(f"{name}: {count}")
        for item in risks[:args.limit or len(risks)]:
            print(f"{item['source_file']}:{item['source_line']} "
                  f"{','.join(item['not_methods_results_keys'])}")
        return
    if args.json:
        print(json.dumps(data[:args.limit or None], ensure_ascii=False, indent=2))
        return
    print("file\tline\tkeys\tunverified\tquantitative_or_table")
    for item in data[:args.limit or None]:
        print("\t".join((
            str(item["source_file"]), str(item["source_line"]),
            ",".join(item["citation_keys"]),
            ",".join(item["not_methods_results_keys"]),
            str(item["mentions_quantity_or_table"]),
        )))


if __name__ == "__main__":
    main()
