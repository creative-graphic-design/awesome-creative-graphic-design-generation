#!/usr/bin/env python3
"""Reject unwrapped registered resource names in manuscript prose.

Read the existing acro registry instead of maintaining a second name list.
This is a lexical guard, not a TeX parser or a scientific-name validator.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

PAPER = Path(__file__).resolve().parents[1]
REGISTRY = PAPER / "acronyms.tex"

ENTRY = re.compile(r"\\DeclareAcronym\{([^}]+)\}\{(.*?)\n\}", re.S)
SHORT = re.compile(r"(?m)^\s*short\s*=\s*\{([^}]+)\}")
TAG = re.compile(r"(?m)^\s*tag\s*=\s*\{([^}]+)\}")
PROTECTED = re.compile(
    r"\\(?:ac|acs|acl|acf|acp|Ac|Acs|Acl|Acf|Acp|cite|citep|citet|Citep|Citet|"
    r"ref|eqref|label|input|url|href|texttt|bibliography)"
    r"\*?(?:\[[^\]]*\])?\{[^{}]*\}"
)
# Do not interpret command identifiers or source comments as ordinary text.
COMMAND = re.compile(r"\\[A-Za-z@]+")
LITERAL = re.compile(r"(?<!\\)%.*$")


def registered_names(source: str) -> dict[str, str]:
    names: dict[str, str] = {}
    for key, options in ENTRY.findall(source):
        short, tag = SHORT.search(options), TAG.search(options)
        if not short or not tag or tag.group(1) not in {"systems", "evaluation"}:
            continue
        name = short.group(1)
        # TeX-formatted names require a real TeX parser: avoid speculative matches.
        if len(name) < 4 or "\\" in name or "{" in name or "}" in name:
            continue
        # An ambiguous label must not silently pick one bibliography identity.
        if name in names and names[name] != key:
            names.pop(name)
            continue
        names[name] = key
    return names


def strip_protected(line: str) -> str:
    # Preserve offsets by replacing protected spans with whitespace.
    line = LITERAL.sub(lambda m: " " * len(m.group()), line)
    for expr in (PROTECTED, COMMAND):
        line = expr.sub(lambda m: " " * len(m.group()), line)
    return line


def find_bare_names(source: str, names: dict[str, str]) -> list[tuple[int, str, str]]:
    if not names:
        return []
    # Longest-first and whole-token matching avoid COLE inside OpenCOLE.
    alternates = "|".join(re.escape(name) for name in sorted(names, key=len, reverse=True))
    pattern = re.compile(rf"(?<![A-Za-z0-9\\])(?:{alternates})(?![A-Za-z0-9])")
    findings = []
    for lineno, original in enumerate(source.splitlines(), 1):
        if original.lstrip().startswith("%"):
            continue
        for match in pattern.finditer(strip_protected(original)):
            findings.append((lineno, match.group(), names[match.group()]))
    return findings


def main() -> int:
    names = registered_names(REGISTRY.read_text(encoding="utf-8"))
    sources = sorted((PAPER / "sections").glob("*.tex"))
    sources += sorted((PAPER / "tabs" / "tex").glob("*.tex"))
    sources += sorted((PAPER / "figs" / "tex").glob("*_figure.tex"))
    findings = []
    for path in sources:
        for lineno, name, key in find_bare_names(path.read_text(encoding="utf-8"), names):
            findings.append(f"{path.relative_to(PAPER)}:{lineno}: {name!r} -> use \\ac{{{key}}}")
    if findings:
        print("\n".join(findings), file=sys.stderr)
        print(f"{len(findings)} unwrapped registered name(s)", file=sys.stderr)
        return 1
    print(f"acro name lint passed ({len(names)} registered literal names, {len(sources)} TeX files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
