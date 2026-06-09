# Paper Revision Orchestrator

A Codex skill for target-journal-driven revision of academic manuscripts.

This skill coordinates specialist skills for manuscript writing, review,
citation, figure preparation, data-availability statements, reviewer response,
and language polishing into a single, coherent procedure for revising an
existing manuscript.

## Function

- identifies manuscript materials within a local workspace;
- calibrates the manuscript against current target-journal guidance and recent
  comparable papers;
- compiles a claim–evidence–boundary register;
- prioritizes top-journal narrative structure before sentence-level polishing;
- assigns each stage to the most suitable specialist skill;
- integrates Nature-style polishing, SCIWRITE clarity, AI-residue detection, and
  academic de-AI safeguards;
- conducts technical review and high-confidence proofing checks before final
  delivery;
- records its progress in `paper_revision_work/` during goal and blast runs.

## Recommended prompt

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

1. Workspace survey and safeguards
2. Target-journal and recent-paper calibration
3. Evidence and claim audit
4. Top-journal narrative and structure
5. Section-by-section manuscript revision
6. Details: numbers, citations, figures, data/code
7. Integrated language pass
8. Technical review and micro-proofing
9. Submission/rebuttal package
10. Final verification checkpoint

## Included scripts

- `scripts/discover_paper_artifacts.py`: surveys a manuscript workspace for
  likely manuscript files, bibliography, figures, result tables, supplements,
  and reviewer-response materials.
- `scripts/proofing_scan.py`: a high-confidence proofing scan for duplicated
  punctuation, malformed text adjacent to equations, capitalization issues, and
  selected patterns of technical ambiguity.

## Attribution

`scripts/proofing_scan.py` is adapted from
[`tengda89757-edu/sciwrite`](https://github.com/tengda89757-edu/sciwrite),
which is licensed under CC BY 4.0. This repository keeps attribution in the
script header and this README.

The remaining workflow files were created to coordinate manuscript revision in
Codex and are intended for adaptation to local academic-writing workflows.

## Install

Copy this folder into your Codex skills directory:

```bash
cp -R paper-revision-orchestrator ~/.codex/skills/
```

Restart Codex after installation.

## License

This exported skill package is provided under CC BY 4.0. See `LICENSE`.
