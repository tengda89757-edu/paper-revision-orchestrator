# Paper Revision Orchestrator

Codex skill for target-journal-driven academic manuscript revision.

This skill coordinates specialist paper-writing, review, citation, figure,
data-availability, reviewer-response, and language-polishing skills into one
practical workflow for revising an existing manuscript.

## What it does

- discovers manuscript artifacts in a local paper workspace;
- calibrates against current target-journal guidance and recent comparable papers;
- builds a claim-evidence-boundary ledger;
- prioritizes top-journal narrative structure before sentence polishing;
- routes each stage to the strongest available specialist skill;
- fuses Nature-style polishing, SCIWRITE clarity, AI-residue detection, and
  academic de-AI safety checks;
- runs technical review and high-confidence proofing checks before final delivery;
- tracks work in `paper_revision_work/` during goal/blast runs.

## Best prompt

```text
使用 paper-revision-orchestrator

目标期刊: [journal]
论文: [path/to/manuscript-folder or main.tex/docx]
开启目标模式

要求:
- 先查目标期刊最新 author guidelines
- 再查近 12-24 个月同刊相近论文
- 按真实投稿前修改流程推进
- 从证据链、顶刊叙事结构、section revision、数字/引用/图表/数据、
  语言融合到 final gate 自主打磨
- 缺证据就标记，不要编造
```

For parallel review:

```text
目标期刊: [journal]
论文: [path]
开启爆模式
```

## Workflow

1. Workspace discovery and safety
2. Target-journal and recent-paper calibration
3. Evidence and claim audit
4. Top-journal narrative and structure
5. Section-by-section manuscript revision
6. Details: numbers, citations, figures, data/code
7. Language fusion
8. Technical review and micro-proofing
9. Submission/rebuttal package
10. Final verification gate

## Included scripts

- `scripts/discover_paper_artifacts.py`: scans a manuscript workspace for likely
  manuscript files, bibliography, figures, result tables, supplements, and
  reviewer-response artifacts.
- `scripts/proofing_scan.py`: high-confidence proofing scan for duplicated
  punctuation, equation-adjacent malformed text, capitalization issues, and
  selected technical ambiguity patterns.

## Attribution

`scripts/proofing_scan.py` is adapted from
[`tengda89757-edu/sciwrite`](https://github.com/tengda89757-edu/sciwrite),
which is licensed under CC BY 4.0. This repository keeps attribution in the
script header and this README.

Other workflow files were created for Codex manuscript-revision orchestration
and are intended to be adapted for local academic-writing workflows.

## Install

Copy this folder into your Codex skills directory:

```bash
cp -R paper-revision-orchestrator ~/.codex/skills/
```

Restart Codex after installation.

## License

This exported skill package is provided under CC BY 4.0. See `LICENSE`.
