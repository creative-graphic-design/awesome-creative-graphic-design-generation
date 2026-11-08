#!/usr/bin/env python3
"""Read-only worklist of citation evidence still needing primary-source verification.

This report never assigns inclusion decisions or upgrades provenance.
"""
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

PAPER = Path(__file__).resolve().parents[1]
AUDIT = PAPER / "literature_citation_audit.csv"
DEPTH_ORDER = ("catalogue_only", "not_verified", "abstract_index", "methods_results")


def load_rows() -> list[dict[str, str]]:
    with AUDIT.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def priority(row: dict[str, str]) -> tuple[int, int, str]:
    depth = row["source_depth"]
    if depth not in DEPTH_ORDER:
        raise ValueError(f"Unknown source depth for {row['bibtex_key']}: {depth}")
    is_cited_study = bool(row["working_register_id"])
    return (DEPTH_ORDER.index(depth), 0 if is_cited_study else 1, row["bibtex_key"])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=0, help="Maximum rows to print; 0 = all")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    args = parser.parse_args()
    if args.limit < 0:
        parser.error("--limit must be nonnegative")
    rows = load_rows()
    depths = Counter(row["source_depth"] for row in rows)
    backlog = sorted((row for row in rows if row["source_depth"] != "methods_results"), key=priority)
    result = {
        "citation_count": len(rows),
        "depth_counts": {key: depths[key] for key in DEPTH_ORDER},
        "backlog_count": len(backlog),
        "unverified": [
            {
                "bibtex_key": row["bibtex_key"],
                "working_register_id": row["working_register_id"],
                "source_depth": row["source_depth"],
                "source_url": row["bib_url"],
                "next_action": (
                    "Read original methods, quantitative results and limitations"
                    if row["source_depth"] == "abstract_index"
                    else "Locate original source and adjudicate exact method/results evidence"
                ),
            }
            for row in (backlog[:args.limit] if args.limit else backlog)
        ],
    }
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return
    print(f"Citations: {len(rows)}; methods/results: {depths['methods_results']}; "
          f"remaining evidence worklist: {len(backlog)}")
    for key in DEPTH_ORDER:
        print(f"  {key}: {depths[key]}")
    print("key\tstudy_id\tdepth\turl")
    for row in result["unverified"]:
        print("\t".join((row["bibtex_key"], row["working_register_id"],
                         row["source_depth"], row["source_url"])))


if __name__ == "__main__":
    main()
