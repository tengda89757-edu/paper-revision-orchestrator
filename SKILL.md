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
9. Maintain figure consistency. All figures should share a uniform visual style
   and a fixed color scheme, in which each color carries a single, stable meaning
   and is never reused for a different quantity or category. The number of
   figures and panels, and every value they display, must agree with the
   manuscript text and the underlying source data.
10. **Exercise causal conservatism.** Observational, cross-sectional, or
    retrospective designs do not support causal conclusions unless the
    manuscript explicitly articulates and defends the necessary causal
    assumptions (JAMA 2024 framework). Replace causal verbs—*cause, lead to,
    demonstrate, prove, induce*—with associational equivalents when the
    evidence does not warrant them. Annotate unresolved causal gaps as
    `[CAUSAL GAP: ...]`.
11. **Do not trust existing assessment files.** When inheriting a workspace that
    already contains `paper_revision_work/` with prior assessments, claims,
    ledgers, or scan reports, treat every prior declaration as unverified.
    Re-run the relevant scripts (`discover_paper_artifacts.py`,
    `scan_engineering_terms.py`, `proofing_scan.py`) and re-verify every
    claim against the current manuscript source. A prior file stating
    "no hits" or "passed" is not sufficient evidence; only script output
    on the current file state counts.

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
   target constraints. **Always run**
   `python scripts/discover_paper_artifacts.py <workspace> --out paper_revision_work/artifacts.json`
   at the start of every session, even if the workspace already contains
   prior `paper_revision_work/` files. The script output is the ground-truth
   inventory; do not rely on a prior `artifacts.json` without re-running.
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
| [references/engineering-terminology.md](references/engineering-terminology.md) | Engineering-to-academic terminology pass for AI→medicine manuscripts |
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
6. **Engineering-terminology pass** (mandatory for all AI/engineering
   manuscripts): run `scripts/scan_engineering_terms.py` against the current
   manuscript source and produce `paper_revision_work/eng_term_scan.md`.
   Review every hit individually against the context in the manuscript and the
   glossary in `references/engineering-terminology.md`. Do not dismiss hits
   solely because they are numerous or because a prior assessment claimed
   "no hits". For each hit, decide: (a) replace with the academic equivalent,
   (b) keep with a written justification in the scan report (e.g. "core defined
   term", "model name", "raw variable name"), or (c) introduce the academic
   term on first mention with the engineering term in parentheses. After
   editing, re-run the scanner to confirm the addressed hits are resolved.
   For cross-disciplinary submissions targeting biomedical informatics, medical
   AI, or clinical NLP journals, additionally invoke the `engineering-to-academic`
   skill as the primary component.
7. **Integrated language pass**: undertaken only after the evidentiary structure
   is stable. Prefer the specialist pipeline (`nature-polishing` →
   `manuscript-writing-review` → `humanizer_academic`/`academic-deai`) when
   installed. When specialist skills are unavailable, execute the self-contained
   protocol in `references/language-fusion.md`: (a) section-flow check, (b)
   SCIWRITE precision pass (redundancy, passive voice, buried predicates,
   terminology consistency, numerical checks), (c) humanizer residue pass
   (AI-pattern detection), and (d) academic de-AI safeguard. Both paths produce
   the same deliverables: revised prose, a language-pass report, and a list of
   manual checks.
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
3. **Re-verify any claims inherited from prior sessions** (e.g. a prior
   `final_assessment.md` stating "no hits" or "ready"). Run the relevant
   scripts and overwrite stale working files rather than appending to them.
4. Select the highest unresolved P0/P1 issue.
5. Edit the text or produce a discrete replacement passage.
6. Verify the evidence, numbers, citations, and sectional logic affected by the revision.
7. Re-rank the remaining issues.
8. Repeat until no P0/P1 issues remain.
9. Carry out the integrated language pass in order: engineering-terminology
   (mandatory scan + hit-by-hit review), prose polishing, de-AI editing, and formatting.
10. Conduct the final assessment.
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
