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
| Results | section claims, numbers, tables, figures, baselines, ablations, robustness, uncertainty; **causal language guard** (no cause/effect/demonstrate for associative/cross-sectional findings) |
| Discussion | interpretation, relation to prior work, limitations, practical/theoretical scope; **causation tenability** (if causal claims are made, assumptions are articulated and plausible per JAMA 2024 framework) |
| Citations | source support, primary vs secondary sources, missing recent work, citation formatting |
| Figures/tables | panel logic, caption claims, visual hierarchy, source data, export/readability, consistent style and color palette, fixed color semantics (one color = one meaning, no reuse), figure count and displayed values consistent with the manuscript |
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

## Overclaim and Causation Guard

Apply this guard to AI/biomedical-informatics manuscripts that report
observational, cross-sectional, or retrospective findings.

### Causal-verb audit

For each of the following verbs in the Abstract, Results, or Discussion,
confirm that the study design supports it; otherwise replace with an
associational equivalent:

| Causal verb (risky) | Safer associational equivalent |
|---|---|
| cause, lead to, result in | associate with, linked to, related to |
| demonstrate, prove, establish | show, report, observe, identify |
| indicate, suggest (as causation) | suggest a possible association |
| induce, trigger, drive | coincide with, accompany, correlate with |
| improve outcomes (without RCT) | associated with improved outcomes |
| predict risk (if no external validation) | associated with increased risk |

### Overclaim pattern checklist

- [ ] **Correlation → Causation**: cross-sectional or retrospective findings are
  not framed as causal mechanisms.
- [ ] **In-vitro / in-silico → Clinical**: cell-line or computational results are
  not extrapolated to patient outcomes without explicit caveats.
- [ ] **Single-center → Generalizable**: single-hospital or single-dataset
  findings do not claim universal clinical applicability.
- [ ] **Association → Efficacy**: observational associations are not reframed as
  treatment efficacy or intervention effectiveness.
- [ ] **Mechanism → Evidence**: biological pathway hypotheses are not presented
  as established mechanistic evidence.
- [ ] **Subgroup → Population**: subgroup findings are not generalized to the
  full population without boundary statements.

### Causal-interpretation tenability (JAMA 2024 framework)

If the manuscript uses causal language for observational data, verify the
following are explicitly addressed; if not, downgrade to associational language
or annotate `[CAUSAL GAP: ...]`:

1. **Causal question is explicit**: the research goal is framed in causal terms,
   comparing well-defined alternatives for a specific target population.
2. **Causal estimand is specified**: the quantity that would answer the causal
   question is defined (e.g., risk difference, hazard ratio under intervention).
3. **Study design supports the estimand**: time-zero, eligibility criteria,
   follow-up, and covariate measurement are aligned with the causal question.
4. **Causal assumptions are articulated**: no uncontrolled confounding,
   positivity, consistency, and other required assumptions are stated and
   discussed.
5. **Sensitivity / falsification analyses are reported**: quantitative bias
   analyses, negative controls, or triangulation across data sources are used
   to examine assumption plausibility.
6. **Interpretation is conditional**: the Discussion uses an "if-then" structure
   (e.g., "If the assumption of no unmeasured confounding holds, these findings
   suggest a possible causal effect of X on Y").

If the study is not an RCT and does not satisfy (1)–(6), causal language is a
**P0 / P1 blocker** for journals following AMA/JAMA style.

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
