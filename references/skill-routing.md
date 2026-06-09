# Skill Selection

Use the smallest specialist component that addresses the current shortcoming.

The specialist skills act as the components responsible for the upstream stages.
This skill does not modify their source files by default; it supplies ordering,
transition specifications, state tracking, and conflict resolution for
substantive manuscript revision.

| Shortcoming or task | Preferred skills |
|---|---|
| Overall revision, evidence audit, major revision, rebuttal, paper rescue | `paper-refinement-trinity-v2` |
| Long-horizon procedure, repository fidelity, reporting guideline, final assessment | `goal-driven-academic-papers` or `academic-research-suite` |
| Target-journal requirements, desk-reject risk, cover letter, highlights | `sci-pre-submission-prep`, plus current web verification |
| Paper structure, top-journal narrative, contribution positioning, title/abstract/intro framing | `top-journal-narrative-writing`, then `nature-writing` |
| Section drafting or rebuilding from claims, figures, notes, or Chinese drafts | `nature-writing` |
| Nature-leaning academic polish and section-level prose repair | `nature-polishing` |
| Sentence clarity, redundancy, passive voice, terminology, numerical consistency | `manuscript-writing-review` as SCIWRITE precision layer |
| Engineering-to-academic terminology replacement for AI→medicine manuscripts | `engineering-to-academic` before the integrated language pass; `scripts/scan_engineering_terms.py` as fallback or residual scan |
| English de-AI academic editing without meaning drift | `humanizer_academic` + `academic-deai` |
| Chinese academic de-AI editing | `academic-deai-zh` |
| Medical-paper AI-writing residue | `humanizer_academic`, with `academic-deai` safeguard |
| Literature discovery, paper download, paper reading | `paper-search`, `nature-academic-search`, `nature-reader` |
| Citation support for manuscript statements or CNS/Nature-family references | `nature-citation` |
| Publication figures, multi-panel plots, figure logic, style and color-scheme consistency, export QA | `nature-figure` |
| Data availability, FAIR metadata, repository and dataset citation plan | `nature-data` |
| SCI/SSCI target-journal alignment, cover letter, highlights, final submission | `sci-pre-submission-prep` |
| Point-by-point reviewer response package | `nature-response` |
| Medical systematic review or meta-analysis | `medical-meta-analysis-writing` |
| AI + empirical repo-to-paper checking, outline, fidelity verification | `ai-empirical-repo-checker`, `ai-empirical-outline-synthesizer`, `ai-empirical-fidelity-verifier` |

## Resolving Overlap

- Default component for direct revision: `paper-refinement-trinity-v2`.
- Default reference for structure and narrative: `top-journal-narrative-writing`.
  Treat manuscript structure as a question of top-journal narrative before
  treating it as one of section formatting.
- Use `goal-driven-academic-papers` when the task spans multiple rounds or
  requires a final, criterion-by-criterion assessment.
- Use `top-journal-narrative-writing` before `nature-writing` and
  `nature-polishing` when the task concerns manuscript structure, title,
  abstract, introduction, discussion, contribution framing, or the
  reviewer-facing narrative.
- Use `nature-writing` before `manuscript-writing-review` when a section requires
  rebuilding rather than local correction.
- For English language polishing, use the integrated language pass:
  `engineering-to-academic` first when the manuscript originates from AI/engineering
  practice and targets biomedical journals, then `nature-polishing` for section
  flow, `manuscript-writing-review` for SCIWRITE clarity and precision,
  `humanizer_academic` for the detection of AI patterns, and `academic-deai` as
  the meaning-preservation safeguard.
- Use `academic-deai-zh` for Chinese academic text. Do not use de-AI editing to
  disguise weak reasoning.
- Use `nature-figure` only for figure tasks. Respect its backend requirement: if
  neither Python nor R has been chosen, pose that question and halt figure
  generation.
- Use `sci-pre-submission-prep` only for target-journal submission-package work
  or journal-specific desk-reject risk checks.

## Order of Precedence

When several skills apply, select in the following order:

```text
evidence/reviewer risk -> target-journal fit -> top-journal narrative structure ->
section architecture -> details/numbers/citations/figures -> integrated language pass ->
format/submission package
```

## Components by Stage

| Stage | Primary component | Secondary support |
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
| Engineering-to-academic terminology | `engineering-to-academic` | `references/engineering-terminology.md`, `scripts/scan_engineering_terms.py` |
| AI residue / humanization | `humanizer_academic` | `academic-deai` / `academic-deai-zh` |
| Technical review and micro-proofing | `paper-review` protocol from `tengda89757-edu/sciwrite` when available | `proofing_scan.py`, `paper-refinement-trinity-v2` |
| Reviewer response | `nature-response` | `paper-refinement-trinity-v2` |
| Final submission package | `sci-pre-submission-prep` | `audit-matrix-and-final-gate.md` |

## Top-Journal Structure Procedure

For structural work, apply `top-journal-narrative-writing` in the following
order:

1. Extract the factual contribution:
   research object, dominant view/method/assumption, a concrete gap or
   limitation, the new contribution, the main evidence, and the scope and
   limitations.
2. Diagnose the current narrative pattern:
   incremental improvement, method-first, application-only, result-only,
   isolated contribution, or other.
3. Generate three to five narrative options only where the evidence can support
   them: assumption challenge, problem-driven method, application-to-principle,
   result-to-explanation, reliability/generalization, or field-enabling resource.
4. Construct a claim–evidence–boundary table for the strongest one or two
   narratives.
5. Select one primary and one secondary narrative according to importance,
   novelty, strength of evidence, control of scope, plausibility to reviewers,
   and fit with the target journal.
6. Only then use `nature-writing` to implement the section-level architecture.
