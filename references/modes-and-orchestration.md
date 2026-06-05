# Modes and Orchestration

## Goal Mode

Trigger when the user explicitly says `开启目标模式`, `go目标模式`, `goal mode`,
`自主打磨`, or equivalent.

If the goal tool is available, create a goal:

```text
Revise [manuscript] for [target journal] until the paper-revision final gate
passes or a real blocker requires author input.
```

Behavior:

1. Continue through journal calibration, audit, revision rounds, and verification
   without routine approval pauses.
2. Ask only for blocking author choices, missing manuscripts, paid/unavailable
   sources, expensive new experiments, or strategic claim narrowing.
3. Update the work artifacts after each substantial round.
4. Mark complete only when the final gate passes.
5. Mark blocked only after a repeated external blocker prevents meaningful
   progress and cannot be resolved locally.

If the goal tool is unavailable, simulate goal mode with a local queue and
explicit status.

## Blast Mode

Trigger only when the user explicitly asks for `爆模式`, `多模型`, `多agent`,
`并行`, `parallel review`, or equivalent. Use subagents only when available and
authorized by the environment. Do not override models unless the user explicitly
requests a model or a clear task-specific reason exists.

Parallel roles are report-only. The controller owns final edits.

| Role | Scope | Output |
|---|---|---|
| Journal Scout | official guidance and recent target-journal papers | journal profile, constraints, desk-reject risks |
| Literature Scout | topic-adjacent recent papers | novelty pressure, missing citation zones |
| Evidence Auditor | manuscript claims vs artifacts | claim ledger, number mismatches, unsupported claims |
| Structure Architect | manuscript architecture | title/abstract/intro/results/discussion diagnosis |
| Language Sweeper | prose and de-AI | paragraph flow, clutter, terminology, AI residue |
| Figure/Data Inspector | figures, captions, source data, availability | figure/data risk list |
| Rebuttal Strategist | reviews and response package | reviewer matrix, traceability gaps |

Merge reports into the P0-P4 queue. Verified manuscript artifacts override role
opinions.

## Work Artifacts

For goal/blast mode, create `paper_revision_work/` next to the manuscript unless
the user asks for chat-only work.

| File | Purpose |
|---|---|
| `journal_profile.md` | target-journal requirements and recent comparator-paper patterns |
| `claim_ledger.md` | major claims, evidence anchors, boundaries, and status |
| `revision_queue.md` | P0-P4 issue queue, owner skill/role, status, next action |
| `edit_log.md` | substantive edits made and why |
| `verification.md` | build/render/citation/number/figure/package checks and residual risks |

Keep these files concise. Do not create large duplicate manuscript copies unless
needed for safety, tracked changes, or format conversion.

## User Updates

During long runs, update the user with:

```text
Current phase:
What changed:
What I am checking next:
Blocked items:
```

Avoid dumping full ledgers in chat unless the user asks.
