#!/usr/bin/env python3
"""High-confidence proofing scan for scientific manuscripts.

Adapted from tengda89757-edu/sciwrite `proofing_scan.py` (CC BY 4.0).
Changes: lazy PDF dependency handling, broader plain-text support, and wording
aligned with paper-revision-orchestrator final-gate use.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Iterable


RuleHit = tuple[str, int, str]


def _read_pdf_pages(pdf_path: Path) -> list[str]:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise SystemExit(
            "PDF scanning requires pypdf. Install it or scan a text/tex/md file instead."
        ) from exc

    reader = PdfReader(str(pdf_path))
    pages: list[str] = []
    for page in reader.pages:
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        pages.append(re.sub(r"\s+", " ", text).strip())
    return pages


def _read_text_pages(path: Path) -> list[str]:
    text = path.read_text(errors="ignore")
    text = re.sub(r"\s+", " ", text).strip()
    return [text]


def _snip(text: str, start: int, end: int, window: int = 70) -> str:
    lo = max(0, start - window)
    hi = min(len(text), end + window)
    return text[lo:hi].strip()


def _find_regex(
    rule_id: str,
    pattern: re.Pattern[str],
    pages: Iterable[str],
    max_hits: int,
) -> list[RuleHit]:
    hits: list[RuleHit] = []
    for page_number, page_text in enumerate(pages, start=1):
        if not page_text:
            continue
        for match in pattern.finditer(page_text):
            hits.append(
                (rule_id, page_number, _snip(page_text, match.start(), match.end()))
            )
            if len(hits) >= max_hits:
                return hits
    return hits


def scan(path: Path, max_hits: int) -> list[RuleHit]:
    if path.suffix.lower() == ".pdf":
        pages = _read_pdf_pages(path)
    else:
        pages = _read_text_pages(path)

    rules: list[tuple[str, re.Pattern[str]]] = [
        ("PUNC_DOUBLE_COMMA", re.compile(r",\s*,")),
        ("PUNC_DOUBLE_PERIOD", re.compile(r"\.\s*\.")),
        ("PUNC_QUOTE_DOUBLE_COMMA", re.compile(r"\"\s*,\s*,")),
        ("SEMICOLON_CAP", re.compile(r";\s+[A-Z]")),
        ("FRAME_INTO_INTO", re.compile(r"\binto\b.{0,80}?\binto\b", re.I)),
        ("FRAME_WITH_INTO", re.compile(r"\bwith\b.{0,80}?\binto\b", re.I)),
        ("FRAME_PLUGGING_INTO_TOGETHER", re.compile(r"plugging\s+into\s+together", re.I)),
        ("CAP_JAVASCRIPT", re.compile(r"\bjavascript\b")),
        ("CAP_IOS", re.compile(r"\bios\b")),
        ("CAP_IPHONE", re.compile(r"\biphone\b")),
        (
            "ARCTAN_DIV",
            re.compile(r"\barctan\s*\(\s*[^()]{0,40}?/[^()]{0,40}?\)", re.I),
        ),
    ]

    remaining = max_hits
    output: list[RuleHit] = []
    for rule_id, pattern in rules:
        if remaining <= 0:
            break
        hits = _find_regex(rule_id, pattern, pages, remaining)
        output.extend(hits)
        remaining = max_hits - len(output)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan a PDF/text/TeX/Markdown manuscript for high-confidence proofing defects."
    )
    parser.add_argument("path", help="PDF or text-like manuscript file")
    parser.add_argument("--max-hits", type=int, default=80)
    parser.add_argument("--out", help="Optional output text file")
    args = parser.parse_args()

    path = Path(args.path).expanduser().resolve()
    if not path.exists():
        raise SystemExit(f"File not found: {path}")

    hits = scan(path, args.max_hits)
    if not hits:
        lines = ["[OK] No high-confidence pattern-scan hits found."]
    else:
        lines = [f"[{rule_id}] p{page}: {snippet}" for rule_id, page, snippet in hits]

    text = "\n".join(lines)
    if args.out:
        Path(args.out).expanduser().write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
