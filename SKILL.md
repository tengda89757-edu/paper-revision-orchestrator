---
name: paper-revision-orchestrator
description: Use when revising an existing academic manuscript, draft, outline, response package, or submission package through a dumb-proof workflow across target-journal calibration, recent literature search, evidence, structure, argument, prose, figures/tables, citations, de-AI polishing, pre-submission checks, or reviewer response. Trigger for 论文修改, 初稿精修, 目标模式, 爆模式, go目标模式, 结构调整, 顶刊叙事, 图表优化, 引用核查, 投稿前检查, 审稿回复.
---

# Paper Revision Orchestrator

## Purpose

Coordinate paper-related skills into one evidence-first manuscript revision
workflow. This is the routing layer for an existing draft or revision package:
it chooses the next highest-value action, calls the right specialist skill, and
keeps iterating until the paper reaches a clear `ready`, `mostly ready`,
`not ready`, or `blocked` state.

The intended user experience is simple: the user gives a target journal and a
manuscript or workspace; Codex discovers the artifacts, calibrates against
current target-journal guidance and recent comparable papers, revises the
manuscript, verifies the result, and asks only for real author decisions.

## Core Rules

1. Evidence comes before prose. Never polish an unsupported central claim.
2. Work from large risk to small risk: evidence, thesis, contribution, methods,
   figures/tables, section logic, paragraphs, sentences, style, formatting.
3. Maintain a compact claim-evidence-boundary ledger for major claims in the
   Abstract, Introduction, Results, Discussion, cover letter, and rebuttal.
4. If a claim is unsupported, verify it from artifacts, weaken it, delete it, or
   mark `[EVIDENCE GAP: ...]`.
5. Do not invent results, citations, baselines, experiments, reviewer sentiment,
   line numbers, journal requirements, dataset identifiers, or figure panels.
6. Browse for journal-specific or "latest/recent/current" requirements and cite
   current official sources before final submission advice.
7. Prefer direct edits when safe. Ask only for blocking author choices, missing
   source artifacts, expensive new experiments, or strategic claim narrowing.
8. End substantial work with verification and residual-risk reporting.

## Dumb-Proof Start

The user may start with only:

```text
目标期刊: [journal]
论文: [file/path or "current folder"]
开启目标模式
```

Default assumptions:

- full-manuscript revision;
- recent target-journal literature window: 12-24 months, extend to 36 months if
  few comparable papers exist;
- infer article type from the manuscript, otherwise ask one concise question;
- conservative claim strength, aggressive structure and clarity repair;
- propose new experiments or analyses only, never imply they were done;
- edit local manuscript files when the request implies direct help and the file
  type is safely editable.

If only a target journal is supplied, search the workspace for likely manuscript
files before asking for input. Ask only when no draft exists or multiple primary
drafts are equally plausible.

## First Move

1. Identify mode:
   - `normal`: user asks for one bounded revision task.
   - `goal`: user says `开启目标模式`, `go目标模式`, `goal mode`, or `自主打磨`.
   - `blast`: user says `爆模式`, `多模型`, `多agent`, `并行`, or `parallel review`.
2. Inventory artifacts with local tools first: manuscript, figures, tables,
   results, code, bibliography, reviews, supplements, and target constraints.
   If useful, run
   `python scripts/discover_paper_artifacts.py <workspace> --out paper_revision_work/artifacts.json`.
3. If a target journal is given, run target-journal calibration before the first
   full rewrite.
4. Create or update `paper_revision_work/` for goal/blast mode unless the user
   requests chat-only work.
5. Build the initial P0-P4 revision queue and start with the highest P0/P1 item.

## Reference Routing

Open only the files needed for the current stage:

| File | Open when |
|---|---|
| [references/practical-revision-workflow.md](references/practical-revision-workflow.md) | Full manuscript run, real-world revision sequence, stage handoffs |
| [references/modes-and-orchestration.md](references/modes-and-orchestration.md) | Goal mode, blast mode, model/subagent orchestration, work artifacts |
| [references/target-journal-calibration.md](references/target-journal-calibration.md) | Target journal supplied, latest guidance needed, recent same-journal paper scan |
| [references/skill-routing.md](references/skill-routing.md) | Need to choose among existing paper skills or resolve overlap |
| [references/language-fusion.md](references/language-fusion.md) | Language pass, SCIWRITE + humanizer fusion, de-AI risk guard |
| [references/audit-matrix-and-final-gate.md](references/audit-matrix-and-final-gate.md) | Goal/blast carpet audit, final gate, acceptance criteria, output templates |

## Default Workflow

When a target journal is supplied, first build a journal profile from current
official guidance and recent comparable papers. For a full manuscript run, open
`references/practical-revision-workflow.md` and follow its stage contracts. Then run:

1. **Orient and inventory**: identify available artifacts, missing evidence,
   target constraints, and highest-risk issue.
2. **Hard-risk triage**: rank risks by decision impact, not ease of editing.
3. **Top-journal narrative spine**: use `top-journal-narrative-writing` as the
   primary structure reference. Extract the factual contribution, diagnose the
   current story pattern, compare alternative defensible narratives, and select
   the strongest claim-evidence-boundary framing.
4. **Section architecture**: after the top-journal narrative is chosen, use
   `nature-writing` to implement title, abstract, introduction, related work,
   methods, results, discussion, and conclusion structure before sentence
   polishing.
5. **Detail alignment**: check numbers, methods, baselines, figures, captions,
   terminology, limitations, citations, data/code statements, and repository facts.
6. **Language fusion pass**: only after the evidence spine is stable. Use
   `nature-polishing` for section-level academic flow, then the SCIWRITE-style
   `manuscript-writing-review` passes for clarity and precision, then
   `humanizer_academic`/`academic-deai` to remove AI residue without meaning drift.
7. **Package pass**: figures, citations, data availability, cover letter,
   highlights, title page, reviewer response, or checklist as needed.
8. **Verification gate**: compile/render/check artifacts when possible and
   report checks that could not be run.

## Autonomous Loop

Use in goal mode until the final gate passes or a real blocker is hit:

```text
1. Refresh journal/literature profile if target-specific context is stale.
2. Run or update the carpet audit.
3. Select the highest unresolved P0/P1 issue.
4. Edit or produce patchable replacement text.
5. Verify evidence, numbers, citations, and section logic affected by the edit.
6. Re-rank remaining issues.
7. Repeat until no P0/P1 issues remain.
8. Run prose/de-AI and formatting passes.
9. Run final gate.
```

Do not loop just to make prose "nicer". Repeat only when a concrete audit item
remains unresolved or verification found a regression.

Priority queue:

```text
P0: evidence or claim breakage
P1: structural, journal-fit, or reviewer-risk issue
P2: section/paragraph logic
P3: sentence polish and de-AI
P4: formatting and package hygiene
```

## Output Contract

Keep user-facing updates compact. For full runs, maintain detailed state in
`paper_revision_work/` and summarize:

```text
Mode:
Target journal:
Primary manuscript:
Current queue:
Changed:
Verification:
Residual blockers:
Next action:
```

Final response:

```text
Ready status: ready / mostly ready / not ready / blocked
Passed checks:
Remaining blockers:
Manual author checks:
Files changed or delivered:
```

## When Not to Use

Do not use this orchestrator for a single isolated specialist task, such as
downloading one paper, making one selected-backend figure, converting a
bibliography file, or translating one article for reading only. Use the
specialist skill directly unless the task is part of a manuscript revision run.
