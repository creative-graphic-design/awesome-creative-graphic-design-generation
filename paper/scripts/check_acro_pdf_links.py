#!/usr/bin/env python3
"""Ensure compiled acro-list paper/DOI links reach their real destinations.

Usage: check_acro_pdf_links.py <pdfinfo -url output> <acronyms.tex>
The pdftotext/index page may show a blue 'paper' label even when its actual
hyperref annotation is a broken GoToR link containing an unexpanded macro.
"""

from collections import Counter
from pathlib import Path
import re
import sys

PAPER_URL = re.compile(r"(?m)^\s*paperurl\s*=\s*\{(https?://[^{}\s]+)\}")
DOI = re.compile(r"(?m)^\s*doi\s*=\s*\{([^{}\s]+)\}")
ANNOTATION = re.compile(r"(?m)^\s*\d+\s+Annotation\s+(https?://\S+)\s*$")
BROKEN_MACROS = (r"\acrowrite", r"\acroprintfield", r"\AcronymID", "%5Cacro", "%5cacro")


def validate(links_text: str, source: str) -> tuple[int, int, list[str]]:
    """Return expected paper, DOI link counts and diagnostic errors."""
    papers = PAPER_URL.findall(source)
    dois = DOI.findall(source)
    expected = Counter(papers + [f"https://doi.org/{doi}" for doi in dois])
    actual = Counter(ANNOTATION.findall(links_text))
    errors: list[str] = []
    if not papers:
        errors.append("No acro paperurl fields were found; refuse empty index pass")
    for marker in BROKEN_MACROS:
        if marker in links_text:
            errors.append(f"Unexpanded TeX macro in PDF link annotation: {marker}")
    for url, n_missing in sorted((expected - actual).items()):
        errors.append(f"Missing {n_missing} of {expected[url]} PDF link annotations for {url}")
    return len(papers), len(dois), errors


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: check_acro_pdf_links.py pdf-links.txt acronyms.tex", file=sys.stderr)
        return 2
    links_text = Path(sys.argv[1]).read_text(encoding="utf-8")
    source = Path(sys.argv[2]).read_text(encoding="utf-8")
    paper_count, doi_count, errors = validate(links_text, source)
    print(f"Expected {paper_count} indexed paper links and {doi_count} DOI links")
    if errors:
        for msg in errors[:30]:
            print(f"ERROR: {msg}", file=sys.stderr)
        if len(errors) > 30:
            print(f"ERROR: ... and {len(errors)-30} more broken/missing links", file=sys.stderr)
        return 1
    print("All acro PDF paper/DOI hyperlink targets and multiplicities verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
