#!/usr/bin/env python3
"""Discover likely paper artifacts in a manuscript workspace."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    "__pycache__",
    "node_modules",
    ".venv",
    "venv",
    "paper_revision_work",
}

MANUSCRIPT_EXTS = {".tex", ".md", ".docx", ".pdf", ".qmd", ".rmd"}
BIB_EXTS = {".bib", ".ris", ".enw", ".nbib"}
FIGURE_EXTS = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".svg", ".pdf", ".eps"}
TABLE_RESULT_EXTS = {".csv", ".tsv", ".xlsx", ".xls", ".json", ".jsonl", ".pkl", ".rds"}
SUPPLEMENT_EXTS = {".zip", ".docx", ".pdf", ".xlsx", ".csv", ".txt"}

MANUSCRIPT_NAME_HINTS = {
    "main",
    "manuscript",
    "paper",
    "article",
    "draft",
    "ms",
    "submission",
}

REVIEW_HINTS = {
    "review",
    "reviewer",
    "response",
    "rebuttal",
    "decision",
    "comments",
    "revision",
    "修回",
    "审稿",
    "回复",
}

FIGURE_DIR_HINTS = {"fig", "figure", "figures", "image", "images", "plot", "plots"}
RESULT_DIR_HINTS = {"result", "results", "table", "tables", "data", "output", "outputs"}
SUPP_HINTS = {"supp", "supplement", "supplementary", "appendix", "supporting"}
NON_MANUSCRIPT_DIR_HINTS = {
    "reference",
    "references",
    "scripts",
    "assets",
    "paper_revision_work",
}


def rel(path: Path, root: Path) -> str:
    return str(path.relative_to(root))


def score_manuscript(path: Path, root: Path) -> int:
    stem = path.stem.lower()
    name = path.name.lower()
    parts = {p.lower() for p in path.relative_to(root).parts}
    score = 0
    if stem in MANUSCRIPT_NAME_HINTS:
        score += 50
    if any(hint in name for hint in MANUSCRIPT_NAME_HINTS):
        score += 25
    if path.suffix.lower() == ".tex":
        score += 20
    if path.suffix.lower() in {".docx", ".md"}:
        score += 15
    if path.suffix.lower() == ".pdf":
        score += 8
    if "supp" in name or "appendix" in name:
        score -= 30
    if any(part in SUPP_HINTS for part in parts):
        score -= 15
    if any(part in NON_MANUSCRIPT_DIR_HINTS for part in parts):
        score -= 25
    if len(path.relative_to(root).parts) <= 2:
        score += 10
    return score


def is_manuscript_candidate(path: Path, root: Path) -> bool:
    suffix = path.suffix.lower()
    score = score_manuscript(path, root)
    depth = len(path.relative_to(root).parts)
    lower_name = path.name.lower()
    lower_parts = [p.lower() for p in path.relative_to(root).parts]

    if any(part in NON_MANUSCRIPT_DIR_HINTS for part in lower_parts):
        return False
    if any(any(hint in part for hint in FIGURE_DIR_HINTS) for part in lower_parts):
        return False
    if any(any(hint in part for hint in RESULT_DIR_HINTS) for part in lower_parts):
        return False
    if any(hint in lower_name for hint in REVIEW_HINTS | SUPP_HINTS):
        return False
    if suffix in {".tex", ".qmd", ".rmd"}:
        return True
    if suffix == ".md":
        return score >= 35
    if suffix in {".docx", ".pdf"}:
        return depth <= 2 or score >= 35
    return False


def bucket_file(path: Path, root: Path, buckets: dict[str, list]) -> None:
    suffix = path.suffix.lower()
    lower_parts = [p.lower() for p in path.relative_to(root).parts]
    lower_name = path.name.lower()

    if suffix in MANUSCRIPT_EXTS and is_manuscript_candidate(path, root):
        buckets["manuscript_candidates"].append(
            {"path": rel(path, root), "score": score_manuscript(path, root)}
        )

    if suffix in BIB_EXTS:
        buckets["bibliography"].append(rel(path, root))

    if suffix in FIGURE_EXTS and (
        any(any(hint in part for hint in FIGURE_DIR_HINTS) for part in lower_parts)
        or lower_name.startswith(("fig", "figure"))
    ):
        buckets["figures"].append(rel(path, root))

    if suffix in TABLE_RESULT_EXTS and (
        any(any(hint in part for hint in RESULT_DIR_HINTS) for part in lower_parts)
        or any(hint in lower_name for hint in RESULT_DIR_HINTS)
    ):
        buckets["tables_or_results"].append(rel(path, root))

    if suffix in SUPPLEMENT_EXTS and (
        any(any(hint in part for hint in SUPP_HINTS) for part in lower_parts)
        or any(hint in lower_name for hint in SUPP_HINTS)
    ):
        buckets["supplementary"].append(rel(path, root))

    if any(hint in lower_name for hint in REVIEW_HINTS):
        buckets["reviews_or_responses"].append(rel(path, root))


def discover(root: Path) -> dict:
    buckets: dict[str, list] = {
        "manuscript_candidates": [],
        "bibliography": [],
        "figures": [],
        "tables_or_results": [],
        "supplementary": [],
        "reviews_or_responses": [],
    }

    for path in root.rglob("*"):
        if path.is_dir():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        bucket_file(path, root, buckets)

    buckets["manuscript_candidates"].sort(
        key=lambda item: (-item["score"], item["path"])
    )
    for key in buckets:
        if key != "manuscript_candidates":
            buckets[key] = sorted(set(buckets[key]))

    return {"root": str(root), **buckets}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Discover likely manuscript, figure, bibliography, result, and review files."
    )
    parser.add_argument("root", nargs="?", default=".", help="Workspace root to scan")
    parser.add_argument("--out", help="Optional JSON output path")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    result = discover(root)
    text = json.dumps(result, indent=2, ensure_ascii=False)

    if args.out:
        out = Path(args.out).expanduser()
        out.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
