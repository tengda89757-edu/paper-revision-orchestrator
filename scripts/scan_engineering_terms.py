#!/usr/bin/env python3
"""Scan manuscripts for engineering terminology and suggest academic replacements.

Part of paper-revision-orchestrator. Run this pass before the integrated
language pass to catch engineering jargon that confuses medical-informatics
reviewers.

This script prefers the canonical glossary from the `engineering-to-academic`
skill when it is available locally, and falls back to an embedded glossary
otherwise. This keeps the orchestrator self-contained while avoiding drift
from the specialist skill.

Usage:
    python scripts/scan_engineering_terms.py <file.tex|md|txt> [--out report.md] [--fix]
    python scripts/scan_engineering_terms.py <file> --glossary /path/to/glossary.yaml
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any


# Embedded fallback glossary — used when the engineering-to-academic skill is
# not installed locally. Keep this in sync with the canonical glossary.yaml.
GLOSSARY: dict[str, Any] = {
    "categories": {
        "model_version": {
            "name": "模型版本与状态类",
            "description": "Hugging Face naming suffixes and model states",
        },
        "experiment_design": {
            "name": "实验设计与矩阵类",
            "description": "Experimental matrices, flowcharts, configurations",
        },
        "algorithm_mechanism": {
            "name": "算法机制与策略类",
            "description": "Code logic, routing, system architecture",
        },
        "model_behavior": {
            "name": "模型行为与现象描述类",
            "description": "Informal descriptions of model phenomena",
        },
    },
    "terms": [
        {
            "engineering_term": "Checkpoint",
            "variants": ["checkpoint", "ckpt", "check point"],
            "academic_terms": {
                "primary": "model",
                "alternatives": ["model variant", "model weights", "trained model instance"],
                "chinese": "模型 / 模型变体 / 模型权重",
            },
            "category": "model_version",
            "severity": "critical",
            "rationale": '"Checkpoint" is a training snapshot file. In research we evaluate the model itself, not filesystem checkpoints.',
            "examples": {
                "bad": "We evaluated three checkpoints on the benchmark.",
                "good": "We evaluated three model variants on the benchmark.",
            },
            "regex_patterns": [r"\bcheckpoint[s]?\b", r"\bckpt[s]?\b"],
        },
        {
            "engineering_term": "Base / Base model",
            "variants": ["base model", "Base", "base version"],
            "academic_terms": {
                "primary": "pre-trained model (PT)",
                "alternatives": ["foundation model", "pre-trained foundation model"],
                "chinese": "预训练模型 / 基础模型",
            },
            "category": "model_version",
            "severity": "critical",
            "rationale": '"Base" is an open-source naming suffix. In research we should describe it as the pre-training stage, before task alignment.',
            "examples": {
                "bad": "The base model was fine-tuned on clinical notes.",
                "good": "The pre-trained model (PT) was fine-tuned on clinical notes.",
            },
            "regex_patterns": [r"\bbase model[s]?\b"],
        },
        {
            "engineering_term": "Instruct / IT",
            "variants": ["instruct model", "instruction-tuned", "IT version"],
            "academic_terms": {
                "primary": "instruction-fine-tuned (IFT)",
                "alternatives": ["aligned model", "instruction-aligned model", "supervised fine-tuned (SFT)"],
                "chinese": "指令微调模型 / 对齐模型",
            },
            "category": "model_version",
            "severity": "critical",
            "rationale": '"Instruct" is a platform suffix. In research we should emphasize the instruction-fine-tuning or alignment process.',
            "examples": {
                "bad": "We compared the instruct version with the base version.",
                "good": "We compared the instruction-fine-tuned (IFT) variant with the pre-trained (PT) variant.",
            },
            "regex_patterns": [r"\binstruct\b(?!ion)", r"\bIT version\b"],
        },
        {
            "engineering_term": "Cell",
            "variants": ["full cell", "experimental cell", "matrix cell"],
            "academic_terms": {
                "primary": "experimental condition",
                "alternatives": ["evaluation setting", "configuration", "experimental configuration"],
                "chinese": "实验条件 / 评估设置 / 配置",
            },
            "category": "experiment_design",
            "severity": "major",
            "rationale": '"Cell" is a spreadsheet/data-matrix cell (engineering slang). In research we describe a specific experimental condition or configuration.',
            "examples": {
                "bad": "The experiment comprised 54 full cells.",
                "good": "The experiment comprised 54 experimental conditions.",
            },
            "regex_patterns": [r"\b(?<!\w)(full )?cell[s]?(?!\w)(?! phone)"],
        },
        {
            "engineering_term": "Lane",
            "variants": ["evaluation lane", "experiment lane", "processing lane"],
            "academic_terms": {
                "primary": "phase",
                "alternatives": ["module", "evaluation branch", "stage", "arm"],
                "chinese": "阶段 / 模块 / 评估分支",
            },
            "category": "experiment_design",
            "severity": "major",
            "rationale": '"Lane" is a swimlane-diagram lane. In methodological descriptions we call it a phase or module.',
            "examples": {
                "bad": "Each evaluation lane processes a distinct subset.",
                "good": "Each evaluation phase processes a distinct subset.",
            },
            "regex_patterns": [r"\blane[s]?\b"],
        },
        {
            "engineering_term": "Delta",
            "variants": ["tuning delta", "performance delta", "delta score"],
            "academic_terms": {
                "primary": "performance differential",
                "alternatives": ["marginal change", "change in performance", "performance gap"],
                "chinese": "性能差异 / 边际变化",
            },
            "category": "experiment_design",
            "severity": "minor",
            "rationale": '"Delta (Δ)" is colloquial STEM slang for difference. In prose, use "performance differential" or "change".',
            "examples": {
                "bad": "The tuning delta was significant across all tasks.",
                "good": "The performance differential induced by fine-tuning was significant across all tasks.",
            },
            "regex_patterns": [r"\bdelta[s]?\b"],
        },
        {
            "engineering_term": "Gate / Gating",
            "variants": ["gate", "gating mechanism", "routing gate"],
            "academic_terms": {
                "primary": "decision rule",
                "alternatives": ["selection mechanism", "filtering policy", "routing mechanism"],
                "chinese": "决策规则 / 选择机制 / 过滤策略",
            },
            "category": "algorithm_mechanism",
            "severity": "major",
            "rationale": '"Gate" in code means an if-else router. In research methodology it is essentially a selective-prediction decision rule or filtering mechanism.',
            "examples": {
                "bad": "The CCR gates filter low-confidence predictions.",
                "good": "The CCR decision rules filter low-confidence predictions.",
            },
            "regex_patterns": [r"\bgate[s]?\b", r"\bgating\b"],
        },
        {
            "engineering_term": "Pipeline",
            "variants": ["data pipeline", "inference pipeline", "training pipeline"],
            "academic_terms": {
                "primary": "evaluation framework",
                "alternatives": ["methodological workflow", "processing workflow", "analytical pipeline"],
                "chinese": "评估框架 / 方法论工作流",
            },
            "category": "algorithm_mechanism",
            "severity": "minor",
            "rationale": '"Pipeline" leans toward engineering script flows. In academic papers, "framework" or "workflow" carries more scholarly weight.',
            "examples": {
                "bad": "Our inference pipeline consists of three stages.",
                "good": "Our evaluation framework consists of three stages.",
            },
            "regex_patterns": [r"\bpipeline[s]?\b"],
        },
        {
            "engineering_term": "Artifact / Bundle",
            "variants": ["model artifact", "output artifact", "artifact bundle"],
            "academic_terms": {
                "primary": "reproducibility package",
                "alternatives": ["audit evidence", "supplementary materials", "supporting files"],
                "chinese": "可重复性数据包 / 审计证据 / 补充材料",
            },
            "category": "algorithm_mechanism",
            "severity": "minor",
            "rationale": '"Artifact" is a software-engineering build artifact (CI/CD). In reproducibility-focused research, call it a "reproducibility package" or supplementary materials.',
            "examples": {
                "bad": "All artifacts are available in the repository.",
                "good": "All supplementary materials are available in the repository.",
            },
            "regex_patterns": [r"\bartifact[s]?\b"],
        },
        {
            "engineering_term": "Flip / Flip rate",
            "variants": ["prediction flip", "label flip", "flip rate"],
            "academic_terms": {
                "primary": "prediction instability",
                "alternatives": ["inconsistency rate", "prediction toggling", "response variability"],
                "chinese": "预测不稳定性 / 不一致率",
            },
            "category": "model_behavior",
            "severity": "major",
            "rationale": '"Flip" is overly colloquial. In research, model sensitivity to perturbation is described as instability or inconsistency rate.',
            "examples": {
                "bad": "The flip rate increased under adversarial perturbation.",
                "good": "The prediction inconsistency rate increased under adversarial perturbation.",
            },
            "regex_patterns": [r"\bflip( rate|ped|ping)?\b"],
        },
        {
            "engineering_term": "Engagement",
            "variants": ["low-engagement", "high-engagement", "engagement score"],
            "academic_terms": {
                "primary": "confidence allocation",
                "alternatives": ["predictive conservatism", "confidence distribution", "certainty level"],
                "chinese": "置信度分配 / 预测保守性",
            },
            "category": "model_behavior",
            "severity": "major",
            "rationale": '"Engagement" describes a model unwilling to output high confidence. In medical AI, this is more accurately termed confidence allocation sparsity or predictive conservatism.',
            "examples": {
                "bad": "Low-engagement predictions were excluded.",
                "good": "Predictions with low confidence allocation were excluded.",
            },
            "regex_patterns": [r"\bengagement\b"],
        },
        {
            "engineering_term": "One-off artifact",
            "variants": ["one-off", "spurious result", "chance artifact"],
            "academic_terms": {
                "primary": "spurious correlation",
                "alternatives": ["prompt-specific bias", "non-robust correlation", "ephemeral association"],
                "chinese": "伪相关 / 提示词特异性偏差",
            },
            "category": "model_behavior",
            "severity": "major",
            "rationale": 'Describing high confidence as a chance artifact of prompt formatting should be defined as prompt-induced bias or non-robust spurious correlation.',
            "examples": {
                "bad": "This high confidence appears to be a one-off artifact.",
                "good": "This high confidence appears to reflect a prompt-specific bias.",
            },
            "regex_patterns": [r"\bone-off\b"],
        },
    ],
}


def _canonical_glossary_path() -> Path | None:
    """Return the canonical glossary path if the engineering-to-academic skill is installed."""
    home = Path.home()
    candidates = [
        home / ".agents" / "skills" / "engineering-to-academic" / "glossary.yaml",
        home / ".codex" / "skills" / "engineering-to-academic" / "glossary.yaml",
        home / "skills" / "engineering-to-academic" / "glossary.yaml",
    ]
    for c in candidates:
        if c.exists():
            return c
    return None


def load_glossary(glossary_path: Path) -> dict[str, Any]:
    """Load glossary from YAML, converting it to the same shape as GLOSSARY."""
    try:
        import yaml
    except ImportError as exc:
        raise SystemExit(
            "PyYAML is required to load glossary.yaml. Install: pip install pyyaml"
        ) from exc

    text = glossary_path.read_text(encoding="utf-8")
    docs = list(yaml.safe_load_all(text))
    glossary: dict[str, Any] = {"categories": {}, "terms": []}
    for doc in docs:
        if doc is None:
            continue
        if "categories" in doc:
            for cat in doc["categories"]:
                glossary["categories"][cat["id"]] = {
                    "name": cat.get("name", cat["id"]),
                    "description": cat.get("description", ""),
                }
        if "terms" in doc:
            for term in doc["terms"]:
                glossary["terms"].append(term)
    return glossary


def get_glossary(preferred_path: Path | None = None) -> dict[str, Any]:
    """Resolve the glossary to use: preferred > canonical > embedded."""
    if preferred_path is not None and preferred_path.exists():
        return load_glossary(preferred_path)

    canonical = _canonical_glossary_path()
    if canonical is not None:
        return load_glossary(canonical)

    return GLOSSARY


def compile_patterns(terms: list[dict]) -> list[tuple[dict, re.Pattern]]:
    """Compile regex patterns from glossary terms."""
    compiled: list[tuple[dict, re.Pattern]] = []
    for term in terms:
        patterns = term.get("regex_patterns", [])
        if not patterns:
            candidates = [term["engineering_term"]] + term.get("variants", [])
            for c in candidates:
                pat = re.compile(r"\b" + re.escape(c) + r"\b", re.IGNORECASE)
                compiled.append((term, pat))
        else:
            for p in patterns:
                # YAML single-quoted backslashes are doubled; normalize for regex
                fixed = p.replace("\\\\", "\\")
                try:
                    pat = re.compile(fixed, re.IGNORECASE)
                    compiled.append((term, pat))
                except re.error:
                    print(f"[WARN] Invalid regex: {p}", file=sys.stderr)
    return compiled


def scan_file(path: Path, compiled: list[tuple[dict, re.Pattern]]) -> list[dict]:
    """Scan a file and return all hits."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    hits: list[dict] = []

    for line_no, line in enumerate(lines, start=1):
        for term, pattern in compiled:
            for match in pattern.finditer(line):
                hits.append({
                    "line": line_no,
                    "column": match.start() + 1,
                    "match": match.group(),
                    "context": line.strip(),
                    "term": term,
                    "severity": term.get("severity", "minor"),
                    "category": term.get("category", "unknown"),
                })
    severity_order = {"critical": 0, "major": 1, "minor": 2, "style": 3}
    hits.sort(key=lambda h: (h["line"], severity_order.get(h["severity"], 99)))
    return hits


def generate_report(path: Path, hits: list[dict], glossary: dict) -> str:
    """Generate a Markdown report."""
    categories = glossary["categories"]
    lines: list[str] = []
    lines.append("# Engineering-to-Academic Scan Report")
    lines.append("")
    lines.append(f"**File:** `{path}`  ")
    lines.append(f"**Total hits:** {len(hits)}  ")
    lines.append(f"**Generated:** auto  ")
    lines.append("")

    if not hits:
        lines.append("✅ No engineering terminology detected.")
        return "\n".join(lines)

    by_severity: dict[str, list[dict]] = {"critical": [], "major": [], "minor": [], "style": []}
    for h in hits:
        by_severity.setdefault(h["severity"], []).append(h)

    for sev in ["critical", "major", "minor", "style"]:
        group = by_severity.get(sev, [])
        if not group:
            continue
        emoji = {"critical": "🔴", "major": "🟠", "minor": "🟡", "style": "🔵"}[sev]
        lines.append(f"## {emoji} {sev.upper()} ({len(group)})")
        lines.append("")
        for h in group:
            term = h["term"]
            cat_name = categories.get(h["category"], {}).get("name", h["category"])
            acad = term.get("academic_terms", {})
            primary = acad.get("primary", "N/A")
            alt = ", ".join(acad.get("alternatives", []))
            cn = acad.get("chinese", "")

            lines.append(f"### `{h['match']}` → `{primary}`")
            lines.append(f"- **Location:** Line {h['line']}, Col {h['column']}")
            lines.append(f"- **Category:** {cat_name}")
            lines.append(f"- **Context:** `{h['context']}`")
            lines.append(f"- **Alternatives:** {alt or 'N/A'}")
            if cn:
                lines.append(f"- **中文:** {cn}")
            if "rationale" in term:
                rationale = term["rationale"].strip().replace("\n", " ")
                lines.append(f"- **Rationale:** {rationale}")
            if "examples" in term:
                ex = term["examples"]
                if "bad" in ex:
                    lines.append(f"- **Example (avoid):** {ex['bad']}")
                if "good" in ex:
                    lines.append(f"- **Example (use):** {ex['good']}")
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Summary Statistics")
    lines.append("")
    lines.append("| Severity | Count |")
    lines.append("|----------|-------|")
    for sev in ["critical", "major", "minor", "style"]:
        lines.append(f"| {sev} | {len(by_severity.get(sev, []))} |")
    lines.append("")
    lines.append("## Recommended Actions")
    lines.append("")
    lines.append("1. Address all 🔴 **critical** and 🟠 **major** hits before submission.")
    lines.append("2. Use `--fix` to auto-replace (review output manually).")
    lines.append(
        "3. Prefer the `engineering-to-academic` skill for a full terminology pass; "
        "use this scanner only for quick detection or when the skill is unavailable."
    )
    lines.append("")

    return "\n".join(lines)


def apply_fixes(path: Path, hits: list[dict], out_path: Path | None = None) -> str:
    """Apply replacements and return the modified text."""
    text = path.read_text(encoding="utf-8", errors="ignore")

    seen: dict[str, dict] = {}
    severity_order = {"critical": 0, "major": 1, "minor": 2, "style": 3}
    for h in hits:
        m = h["match"].lower()
        if m not in seen or severity_order.get(h["severity"], 99) < severity_order.get(seen[m]["severity"], 99):
            seen[m] = h

    replacements = sorted(seen.values(), key=lambda h: len(h["match"]), reverse=True)
    modified = text
    for h in replacements:
        term = h["term"]
        acad = term.get("academic_terms", {})
        replacement = acad.get("primary", h["match"])
        pattern = re.compile(re.escape(h["match"]), re.IGNORECASE)
        modified = pattern.sub(replacement, modified)

    if out_path:
        out_path.write_text(modified, encoding="utf-8")
    return modified


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan manuscripts for engineering terminology."
    )
    parser.add_argument("path", help="Manuscript file (.tex, .md, .txt)")
    parser.add_argument("--glossary", help="Path to an external glossary.yaml")
    parser.add_argument("--out", help="Output report file (.md)")
    parser.add_argument("--fix", action="store_true", help="Generate fixed version")
    parser.add_argument("--fix-out", help="Output path for fixed file")
    args = parser.parse_args()

    path = Path(args.path).expanduser().resolve()
    if not path.exists():
        raise SystemExit(f"File not found: {path}")

    glossary_path = Path(args.glossary).expanduser().resolve() if args.glossary else None
    glossary = get_glossary(glossary_path)
    compiled = compile_patterns(glossary["terms"])
    hits = scan_file(path, compiled)

    report = generate_report(path, hits, glossary)

    if args.out:
        Path(args.out).expanduser().write_text(report, encoding="utf-8")
        print(f"Report written to: {args.out}")
    else:
        print(report)

    if args.fix:
        fix_out = Path(args.fix_out).expanduser().resolve() if args.fix_out else path.with_suffix(path.suffix + ".fixed")
        apply_fixes(path, hits, fix_out)
        print(f"Fixed version written to: {fix_out}")

    return 0 if not any(h["severity"] in ("critical", "major") for h in hits) else 1


if __name__ == "__main__":
    raise SystemExit(main())
