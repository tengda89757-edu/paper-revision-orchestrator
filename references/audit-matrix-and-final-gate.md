# Audit Matrix and Final Gate

## Carpet Audit Matrix

For goal or blast mode, mark each item as `pass`, `fix-now`, `needs-author`, or
`not-applicable`.

| Layer | Checks |
|---|---|
| Journal fit | article type, scope, word limits, abstract format, reporting checklist, data/code policy |
| Recent literature | comparator papers, novelty pressure, terminology, citation gaps, framing conventions |
| Top-journal narrative | factual contribution, current story pattern, alternative defensible narratives, claim-evidence-boundary framing |
| Core argument | thesis, gap, contribution, evidence, boundary, implications |
| Abstract/Title | target-journal pattern, concrete evidence, no unsupported novelty or impact claim |
| Introduction | problem, unresolved gap, prior limitation, contribution, evidence-backed bullets |
| Methods | reproducibility detail, data, models, statistics, ethics, software, parameters |
| Results | section claims, numbers, tables, figures, baselines, ablations, robustness, uncertainty |
| Discussion | interpretation, relation to prior work, limitations, practical/theoretical scope |
| Citations | source support, primary vs secondary sources, missing recent work, citation formatting |
| Figures/tables | panel logic, caption claims, visual hierarchy, source data, export/readability |
| Data/code | availability statement, repositories, identifiers, restrictions, FAIR metadata |
| Language fusion | section flow, clutter, passive voice, sentence architecture, terminology, numerical/citation consistency, AI residue, meaning-preservation guard |
| Technical proofing | notation drift, undefined symbols, equation-adjacent grammar, duplicated punctuation, reference-list glitches, implementation-facing ambiguity |
| Package | cover letter, highlights, response letter, title page, checklist, supplementary files |

## Claim Ledger

For major claims:

```text
Claim:
Location:
Evidence anchor:
Boundary:
Status: supported / weak / unsupported / unknown
Action: keep / verify / weaken / delete / ask author
```

A claim with `unsupported` or `unknown` status cannot remain strong in the
Abstract, Introduction, cover letter, or response letter.

## Structure Gate

Before rewriting sections, verify that the top-journal narrative spine is stable:

```text
Factual contribution:
Current story pattern:
Primary narrative:
Backup narrative:
Evidence required:
Unsafe claims to avoid:
Reviewer risk:
```

Do not proceed to sentence-level polishing if the primary narrative is still
method-first, result-only, or unsupported by evidence.

## Verification Gate

Run relevant checks when possible:

- compile or render LaTeX, Markdown, DOCX, PDF, figures, or tables;
- inspect undefined citations/references, missing figures, fatal build errors,
  severe layout warnings, and broken cross-references;
- compare manuscript numbers against source tables, logs, or result files;
- verify citations and bibliography files;
- check figure captions against panels and source data;
- check data/code availability statements;
- check reviewer responses against manuscript changes.
- run the language fusion acceptance criteria when prose was rewritten.
- run `scripts/proofing_scan.py` on a final PDF or text-like source when the
  manuscript has equations, appendices, dense technical prose, or final proofing
  is requested; spot-check hits before reporting them.

If a check cannot be run, say why and record residual risk.

## Stop States

| State | Meaning |
|---|---|
| `ready` | final gate passes and no known blocking issue remains |
| `mostly ready` | only author-fill placeholders or minor formatting remain |
| `not ready` | P0/P1 issue remains but can be fixed with available inputs |
| `blocked` | external input, inaccessible source, or author decision is required |

## Output Templates

### Triage

```text
Mode:
Assumption:
Top risks:
1.
2.
3.
Revision order:
Immediate next edit:
Missing author inputs:
```

### Edit Report

```text
Changed:
Evidence or source basis:
Claim calibration:
Residual risks:
Next recommended pass:
Verification:
```

### Final Gate

```text
Ready status:
Passed checks:
Remaining blockers:
Manual author checks:
Files changed or delivered:
```
