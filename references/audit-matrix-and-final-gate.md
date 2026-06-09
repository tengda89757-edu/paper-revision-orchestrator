# Audit Matrix and Final Assessment

## Comprehensive Audit Matrix

In the goal or blast regime, mark each item as `pass`, `fix-now`, `needs-author`,
or `not-applicable`.

| Layer | Checks |
|---|---|
| Journal fit | article type, scope, word limits, abstract format, reporting checklist, data/code policy |
| Recent literature | comparator papers, novelty pressure, terminology, citation gaps, framing conventions |
| Top-journal narrative | factual contribution, current narrative pattern, alternative defensible narratives, claim-evidence-boundary framing |
| Core argument | thesis, gap, contribution, evidence, boundary, implications |
| Abstract/Title | target-journal pattern, concrete evidence, no unsupported novelty or impact claim |
| Introduction | problem, unresolved gap, prior limitation, contribution, evidence-backed bullets |
| Methods | reproducibility detail, data, models, statistics, ethics, software, parameters |
| Results | section claims, numbers, tables, figures, baselines, ablations, robustness, uncertainty |
| Discussion | interpretation, relation to prior work, limitations, practical/theoretical scope |
| Citations | source support, primary vs secondary sources, missing recent work, citation formatting |
| Figures/tables | panel logic, caption claims, visual hierarchy, source data, export/readability |
| Data/code | availability statement, repositories, identifiers, restrictions, FAIR metadata |
| Language | section flow, redundancy, passive voice, sentence structure, terminology, numerical/citation consistency, AI residue, meaning-preservation safeguard |
| Technical proofing | notation drift, undefined symbols, equation-adjacent grammar, duplicated punctuation, reference-list glitches, implementation-facing ambiguity |
| Package | cover letter, highlights, response letter, title page, checklist, supplementary files |

## Claim Register

For each major claim:

```text
Claim:
Location:
Evidence anchor:
Boundary:
Status: supported / weak / unsupported / unknown
Action: keep / verify / weaken / delete / ask author
```

A claim with `unsupported` or `unknown` status cannot remain stated strongly in
the Abstract, Introduction, cover letter, or response letter.

## Structural Checkpoint

Before rewriting sections, confirm that the top-journal narrative structure is
stable:

```text
Factual contribution:
Current narrative pattern:
Primary narrative:
Secondary narrative:
Evidence required:
Unsafe claims to avoid:
Reviewer risk:
```

Do not proceed to sentence-level polishing if the primary narrative is still
method-first, result-only, or unsupported by evidence.

## Verification Checkpoint

Perform the relevant checks where possible:

- compile or render LaTeX, Markdown, DOCX, PDF, figures, or tables;
- inspect undefined citations/references, missing figures, fatal build errors,
  severe layout warnings, and broken cross-references;
- compare manuscript numbers against source tables, logs, or result files;
- verify citations and bibliography files;
- check figure captions against panels and source data;
- check data/code availability statements;
- check reviewer responses against manuscript changes;
- apply the acceptance criteria of the integrated language pass when prose has
  been rewritten;
- run `scripts/proofing_scan.py` on a final PDF or text-like source when the
  manuscript contains equations, appendices, or dense technical prose, or when
  final proofing is requested; verify each match manually before reporting it.

If a check cannot be performed, state why and record the residual risk.

## Completion States

| State | Meaning |
|---|---|
| `ready` | the final assessment is satisfied and no known blocking issue remains |
| `mostly ready` | only author-fill placeholders or minor formatting remain |
| `not ready` | a P0/P1 issue remains but can be resolved with available inputs |
| `blocked` | external input, an inaccessible source, or an author decision is required |

## Reporting Templates

### Initial Assessment

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

### Final Assessment

```text
Ready status:
Passed checks:
Remaining blockers:
Manual author checks:
Files changed or delivered:
```
