# Operating Regimes and Coordination

## Goal Regime

Activate when the author explicitly states `开启目标模式`, `go目标模式`,
`goal mode`, `自主打磨`, or an equivalent.

If a goal-setting tool is available, define the goal:

```text
Revise [manuscript] for [target journal] until the final assessment of the
revision is satisfied or a genuine blocker requires author input.
```

Behavior:

1. Proceed through journal calibration, audit, successive revision rounds, and
   verification without pausing for routine approval.
2. Request author input only for decisions that block progress, missing
   manuscripts, paid or unavailable sources, costly new experiments, or the
   strategic narrowing of claims.
3. Update the working records after each substantial round.
4. Mark the work complete only when the final assessment is satisfied.
5. Mark the work blocked only after a recurring external obstacle prevents
   meaningful progress and cannot be resolved locally.

If no goal-setting tool is available, emulate the goal regime with a local
priority list and an explicit status.

## Blast Regime

Activate only when the author explicitly requests `爆模式`, `多模型`, `多agent`,
`并行`, `parallel review`, or an equivalent. Employ parallel reviewers only where
the environment makes them available and authorized. Do not override the model
unless the author explicitly requests one or a clear task-specific reason exists.

The parallel roles are advisory; the coordinating skill retains responsibility
for the final edits.

| Role | Scope | Output |
|---|---|---|
| Journal Scout | official guidance and recent target-journal papers | journal profile, constraints, desk-reject risks |
| Literature Scout | topic-adjacent recent papers | areas of novelty pressure, gaps in citation |
| Evidence Auditor | manuscript claims against source materials | claim register, numerical mismatches, unsupported claims |
| Structure Architect | manuscript architecture | title/abstract/intro/results/discussion diagnosis |
| Language Reviewer | prose and de-AI editing | paragraph flow, redundancy, terminology, AI residue |
| Figure/Data Inspector | figures, captions, source data, availability | figure/data risk list, with checks on style and color-scheme consistency, fixed color semantics (one color = one meaning), and agreement between figure counts/values and the manuscript |
| Rebuttal Strategist | reviews and response package | reviewer matrix, traceability gaps |

Integrate the findings into the P0–P4 priority scheme. Verified manuscript
materials take precedence over the opinions of the individual roles.

## Working Records

In the goal and blast regimes, create `paper_revision_work/` alongside the
manuscript, unless the author requests discussion-only assistance.

| File | Purpose |
|---|---|
| `journal_profile.md` | target-journal requirements and recent comparator-paper patterns |
| `claim_ledger.md` | major claims, evidence anchors, boundaries, and status |
| `revision_queue.md` | P0–P4 issue list, responsible skill or role, status, and next action |
| `edit_log.md` | substantive edits and their rationale |
| `verification.md` | build/render/citation/number/figure/package checks and residual risks |

Keep these files concise. Do not create large duplicate copies of the manuscript
unless required for safety, tracked changes, or format conversion.

## Progress Updates

During extended runs, report progress to the author as follows:

```text
Current phase:
What changed:
What I am checking next:
Blocked items:
```

Do not reproduce full registers in conversation unless the author requests them.
