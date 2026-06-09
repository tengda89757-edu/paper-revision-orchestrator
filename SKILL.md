---
name: paper-revision-orchestrator
description: Use when revising an existing academic manuscript, draft, outline, response package, or submission package through a structured, guided workflow spanning target-journal calibration, recent literature search, evidence, structure, argument, prose, figures/tables, citations, de-AI polishing, pre-submission checks, or reviewer response. Trigger for 论文修改, 初稿精修, 目标模式, 爆模式, go目标模式, 结构调整, 顶刊叙事, 图表优化, 引用核查, 投稿前检查, 审稿回复.
---

# Paper Revision Orchestrator

## Purpose

This skill coordinates the available manuscript-related skills into a single,
evidence-first revision procedure. It serves as the coordinating layer for an
existing draft or revision package: it identifies the most consequential next
action, delegates it to the appropriate specialist skill, and proceeds
iteratively until the manuscript attains a clearly defined status of `ready`,
`mostly ready`, `not ready`, or `blocked`.

The intended workflow is straightforward. The author supplies a target journal
together with a manuscript or workspace; the skill then catalogues the available
materials, calibrates the manuscript against current target-journal guidance and
recent comparable publications, revises the text, verifies the outcome, and
requests author input only where a genuine authorial decision is required.

## Guiding Principles

1. Evidence precedes prose. A central claim that lacks support should never be
   refined stylistically.
2. Proceed from the most consequential risks to the least: evidence, thesis,
   contribution, methods, figures and tables, sectional logic, paragraphs,
   sentences, style, and formatting.
3. Maintain a concise claim–evidence–boundary register for the principal claims
   in the Abstract, Introduction, Results, Discussion, cover letter, and rebuttal.
4. Where a claim is unsupported, verify it against the source materials, qualify
   it, remove it, or annotate it as `[EVIDENCE GAP: ...]`.
5. Do not fabricate results, citations, baselines, experiments, reviewer
   sentiment, line numbers, journal requirements, dataset identifiers, or figure
   panels.
6. Consult journal-specific or "latest/recent/current" requirements and cite
   current official sources before offering final submission advice.
7. Apply direct edits where doing so is safe. Request author input only for
   decisions that block progress, missing source materials, costly new
   experiments, or the strategic narrowing of claims.
8. Conclude any substantial revision with verification and a report of residual
   risk.

## Minimal-Input Start

The author may begin with no more than:

```text
目标期刊: [journal]
论文: [file/path or "current folder"]
开启目标模式
```

Default assumptions:

- revision of the complete manuscript;
- a recent target-journal literature window of 12–24 months, extended to 36
  months where few comparable papers exist;
- the article type is inferred from the manuscript; failing that, a single
  concise question is posed;
- conservative calibration of claim strength, with thorough repair of structure
  and clarity;
- new experiments or analyses are proposed only, never represented as having
  been performed;
- local manuscript files are edited when the request implies direct assistance
  and the file type can be edited safely.

If only a target journal is supplied, the workspace is searched for likely
manuscript files before any input is requested. Input is sought only when no
draft exists, or when several primary drafts are equally plausible.

## Initial Steps

1. Identify the operating regime:
   - `normal`: the author requests a single, bounded revision task.
   - `goal`: the author indicates `开启目标模式`, `go目标模式`, `goal mode`, or `自主打磨`.
   - `blast`: the author indicates `爆模式`, `多模型`, `多agent`, `并行`, or `parallel review`.
2. Catalogue the available materials using local tools first: manuscript,
   figures, tables, results, code, bibliography, reviews, supplements, and
   target constraints. Where helpful, run
   `python scripts/discover_paper_artifacts.py <workspace> --out paper_revision_work/artifacts.json`.
3. If a target journal is provided, perform target-journal calibration before
   the first complete rewrite.
4. Create or update `paper_revision_work/` in the goal and blast regimes, unless
   the author requests discussion-only assistance.
5. Construct the initial P0–P4 priority ordering and begin with the
   highest-priority P0/P1 item.

## Selecting Reference Material

Consult only the files relevant to the current stage:

| File | Consult when |
|---|---|
| [references/practical-revision-workflow.md](references/practical-revision-workflow.md) | Complete manuscript run, real-world revision sequence, stage transitions |
| [references/modes-and-orchestration.md](references/modes-and-orchestration.md) | Goal regime, blast regime, model/auxiliary-reviewer coordination, working records |
| [references/target-journal-calibration.md](references/target-journal-calibration.md) | Target journal supplied, latest guidance needed, recent same-journal paper survey |
| [references/skill-routing.md](references/skill-routing.md) | Need to select among existing paper skills or resolve overlap |
| [references/language-fusion.md](references/language-fusion.md) | Language pass, SCIWRITE + humanizer integration, de-AI risk safeguard |
| [references/audit-matrix-and-final-gate.md](references/audit-matrix-and-final-gate.md) | Goal/blast comprehensive audit, final assessment, acceptance criteria, output templates |

## Standard Procedure

When a target journal is supplied, first construct a journal profile from current
official guidance and recent comparable papers. For a complete manuscript run,
consult `references/practical-revision-workflow.md` and follow its stage
specifications. Then proceed as follows:

1. **Orientation and inventory**: identify the available materials, missing
   evidence, target constraints, and the highest-risk issue.
2. **Risk prioritization**: rank risks by their impact on the manuscript's
   acceptability, not by ease of editing.
3. **Top-journal narrative structure**: use `top-journal-narrative-writing` as
   the principal structural reference. Extract the factual contribution, diagnose
   the current narrative pattern, compare alternative defensible narratives, and
   select the strongest claim–evidence–boundary framing.
4. **Section architecture**: once the narrative is chosen, use `nature-writing`
   to structure the title, abstract, introduction, related work, methods,
   results, discussion, and conclusion before sentence-level polishing.
5. **Detail alignment**: verify numbers, methods, baselines, figures, captions,
   terminology, limitations, citations, data and code statements, and repository
   facts.
6. **Integrated language pass**: undertaken only after the evidentiary structure
   is stable. Use `nature-polishing` for section-level academic flow, then the
   SCIWRITE-style `manuscript-writing-review` passes for clarity and precision,
   and finally `humanizer_academic`/`academic-deai` to remove AI residue without
   altering meaning.
7. **Submission package**: prepare figures, citations, data-availability
   statements, cover letter, highlights, title page, reviewer response, or
   checklist as required.
8. **Verification checkpoint**: compile, render, or otherwise check the materials
   where possible, and report any checks that could not be performed.

## Iterative Revision Cycle

Apply in the goal regime until the final assessment is satisfied or a genuine
blocker is encountered:

```text
1. Refresh the journal and literature profile if target-specific context has become outdated.
2. Conduct or update the comprehensive audit.
3. Select the highest unresolved P0/P1 issue.
4. Edit the text or produce a discrete replacement passage.
5. Verify the evidence, numbers, citations, and sectional logic affected by the revision.
6. Re-rank the remaining issues.
7. Repeat until no P0/P1 issues remain.
8. Carry out the prose, de-AI, and formatting passes.
9. Conduct the final assessment.
```

Do not iterate merely to refine prose. Repeat only when a specific audit item
remains unresolved or verification has revealed a regression.

Priority scheme:

```text
P0: failure of evidence or an unsupported claim
P1: structural, journal-fit, or reviewer-risk issue
P2: sectional or paragraph-level logic
P3: sentence-level polishing and de-AI editing
P4: formatting and submission-package consistency
```

## Reporting Format

Keep author-facing updates concise. For complete runs, maintain detailed state in
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
```

## When Not to Use

This skill should not be used for a single, isolated specialist task — for
example, downloading one paper, producing a single figure in a chosen backend,
converting a bibliography file, or translating one article for reading only. In
such cases, use the relevant specialist skill directly, unless the task forms
part of a complete manuscript revision.
