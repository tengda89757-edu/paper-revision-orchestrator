# Skill Routing

Use the smallest specialist layer that matches the current failure mode.

Specialist skills are used as upstream stage owners. This orchestrator does not
patch their source files by default; it adds ordering, handoff contracts, state
tracking, and conflict resolution for real manuscript revision runs.

| Failure mode or task | Prefer these skills |
|---|---|
| Overall revision, evidence audit, major revision, rebuttal, paper rescue | `paper-refinement-trinity-v2` |
| Long-horizon pipeline, repository fidelity, reporting guideline, final gate | `goal-driven-academic-papers` or `academic-research-suite` |
| Target-journal requirements, desk-reject risk, cover letter, highlights | `sci-pre-submission-prep`, plus current web verification |
| Paper structure, top-journal story, contribution positioning, title/abstract/intro framing | `top-journal-narrative-writing`, then `nature-writing` |
| Section drafting or rebuilding from claims, figures, notes, or Chinese drafts | `nature-writing` |
| Nature-leaning academic polish and section-level prose repair | `nature-polishing` |
| Sentence clarity, clutter, passive voice, terminology, numerical consistency | `manuscript-writing-review` as SCIWRITE precision layer |
| English de-AI academic editing without meaning drift | `humanizer_academic` + `academic-deai` |
| Chinese academic de-AI editing | `academic-deai-zh` |
| Medical-paper AI-writing residue | `humanizer_academic`, with `academic-deai` safety guard |
| Literature discovery, paper download, paper reading | `paper-search`, `nature-academic-search`, `nature-reader` |
| Citation support for manuscript statements or CNS/Nature-family references | `nature-citation` |
| Publication figures, multi-panel plots, figure logic, export QA | `nature-figure` |
| Data availability, FAIR metadata, repository and dataset citation plan | `nature-data` |
| SCI/SSCI target-journal alignment, cover letter, highlights, final submission | `sci-pre-submission-prep` |
| Point-by-point reviewer response package | `nature-response` |
| Medical systematic review or meta-analysis | `medical-meta-analysis-writing` |
| AI + empirical repo-to-paper checking, outline, fidelity verification | `ai-empirical-repo-checker`, `ai-empirical-outline-synthesizer`, `ai-empirical-fidelity-verifier` |

## Overlap Rules

- Default direct-revision executor: `paper-refinement-trinity-v2`.
- Default structure/narrative reference: `top-journal-narrative-writing`.
  Treat paper structure as a top-journal narrative problem before treating it as
  a section-formatting problem.
- Use `goal-driven-academic-papers` when the task spans multiple rounds or needs
  a final criterion-by-criterion gate.
- Use `top-journal-narrative-writing` before `nature-writing` and
  `nature-polishing` when the task touches manuscript structure, title,
  abstract, introduction, discussion, contribution framing, or reviewer-facing
  story.
- Use `nature-writing` before `manuscript-writing-review` when a section needs
  rebuilding, not local cleanup.
- For English language polishing, use the fused language pass:
  `nature-polishing` for section flow, `manuscript-writing-review` for SCIWRITE
  clarity/precision, `humanizer_academic` for AI-pattern detection, and
  `academic-deai` as the meaning-preservation safety guard.
- Use `academic-deai-zh` for Chinese academic text. Do not use de-AI editing to
  hide weak reasoning.
- Use `nature-figure` only for figure tasks. Respect its backend gate: if Python
  or R is not chosen, ask that question and stop figure generation.
- Use `sci-pre-submission-prep` only for target-journal submission package work
  or journal-specific desk-reject risk checks.

## Routing Priority

When several skills apply, choose in this order:

```text
evidence/reviewer risk -> target-journal fit -> top-journal narrative spine ->
section architecture -> details/numbers/citations/figures -> fused language pass ->
format/submission package
```

## Stage Owners

| Stage | Primary owner | Secondary support |
|---|---|---|
| Artifact discovery | `discover_paper_artifacts.py` | local `rg/find/ls` |
| Journal calibration | `sci-pre-submission-prep` | `target-journal-calibration.md`, web verification |
| Recent literature and citation gaps | `nature-academic-search` / `paper-search` | `nature-citation` |
| Evidence and claim audit | `paper-refinement-trinity-v2` | `goal-driven-academic-papers` |
| Top-journal structure | `top-journal-narrative-writing` | `nature-writing` |
| Section architecture | `nature-writing` | `nature-polishing` |
| Figures and tables | `nature-figure` | `paper-refinement-trinity-v2` evidence logic |
| Data/code availability | `nature-data` | target journal policy |
| Language precision | `manuscript-writing-review` | `nature-polishing` |
| AI residue / humanization | `humanizer_academic` | `academic-deai` / `academic-deai-zh` |
| Technical review and micro-proofing | `paper-review` protocol from `tengda89757-edu/sciwrite` when available | `proofing_scan.py`, `paper-refinement-trinity-v2` |
| Reviewer response | `nature-response` | `paper-refinement-trinity-v2` |
| Final submission package | `sci-pre-submission-prep` | `audit-matrix-and-final-gate.md` |

## Top-Journal Structure Protocol

For structure work, apply `top-journal-narrative-writing` in this order:

1. Extract the factual contribution:
   research object, dominant view/method/assumption, concrete gap or failure
   mode, new contribution, main evidence, scope and limitations.
2. Diagnose the current story pattern:
   incremental improvement, method-first, application-only, result-only,
   isolated contribution, or other.
3. Generate 3-5 narrative options only if the evidence can support them:
   assumption challenge, problem-driven method, application-to-principle,
   result-to-explanation, reliability/generalization, or field-enabling resource.
4. Build a claim-evidence-boundary table for the strongest 1-2 narratives.
5. Select one primary narrative and one backup narrative by importance, novelty,
   evidence strength, scope control, reviewer plausibility, and target-journal fit.
6. Only then use `nature-writing` to implement section-level architecture.
