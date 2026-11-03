#!/usr/bin/env python3
"""Check one sentence per physical TeX source line in manuscript prose.

Adapted for this paper from the design in shunk031/agentic-cognitive-writing
PR #89. Changes to wording become focused Git diffs; single newlines are
ordinary TeX whitespace, while blank lines still separate paragraphs.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

PAPER = Path(__file__).resolve().parents[1]
BOUNDARY = re.compile(r'(?P<punc>[.!?])(?P<closers>[}\])\'"”’]*)(?P<gap>[ \t]+)(?=[A-Z]|\\[A-Za-z@]+)')
ABBREVIATIONS = (
    "e.g.", "i.e.", "et al.", "Fig.", "Figs.", "Eq.", "Eqs.",
    "Sec.", "Secs.", "App.", "Dr.", "Prof.", "vs.", "U.S.",
)


def strip_comment(line: str) -> str:
    for i, char in enumerate(line):
        if char != "%":
            continue
        n = 0
        j = i - 1
        while j >= 0 and line[j] == "\\":
            n += 1
            j -= 1
        if n % 2 == 0:
            return line[:i]
    return line


def is_abbreviation(prefix: str) -> bool:
    prefix = prefix.rstrip("}])'\"”’ ")
    return prefix.endswith(ABBREVIATIONS) or bool(re.search(r"(?:^|\s)[A-Z]\.$", prefix))


def bad_sentence_line(line: str) -> bool:
    code = strip_comment(line)
    for match in BOUNDARY.finditer(code):
        before = code[: match.start("punc") + 1]
        if match.group("punc") == "." and is_abbreviation(before):
            continue
        return True
    return False


def check_files(paths: list[Path]) -> list[tuple[Path, int, str]]:
    errors = []
    for path in paths:
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if bad_sentence_line(line):
                errors.append((path, number, line.strip()))
    return errors


def main() -> int:
    paths = sorted((PAPER / "sections").glob("*.tex"))
    paths += sorted((PAPER / "tabs" / "tex").glob("*.tex"))
    paths += sorted((PAPER / "figs" / "tex").glob("*_figure.tex"))
    if not paths:
        print("ERROR: no manuscript prose files found", file=sys.stderr)
        return 1
    problems = check_files(paths)
    if problems:
        for path, line, content in problems:
            print(f"{path.relative_to(PAPER)}:{line}: multiple sentences on one physical source line")
            print("  " + content[:200])
        print("Use one sentence per physical TeX source line, blank lines between paragraphs.")
        return 1
    print(f"One-sentence-per-line check passed ({len(paths)} source files).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
