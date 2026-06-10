# Practical Revision Workflow

This reference applies to substantive manuscript revision. It organizes the
specialist skills into a practical procedure, specifying the inputs, outputs,
transitions, and termination conditions of each stage.

This skill should not rewrite the specialist skills internally. It should treat
each as the component responsible for a given stage and supply the coordinating
layer that they lack: what to undertake first, what material to produce, and
what conditions must hold before proceeding.

## Complete Procedure

```text
0. Workspace survey and safeguards
1. Target-journal and recent-paper calibration
2. Evidence and claim audit
3. Top-journal narrative and structure
4. Section-by-section manuscript revision
5. Details: numbers, citations, figures, data/code
6. Conditional engineering-terminology pass and integrated language pass
7. Technical review and micro-proofing
8. Submission/rebuttal package
9. Final verification checkpoint
```

## Stage Specifications

### 0. Workspace survey and safeguards

Responsible component: `discover_paper_artifacts.py`, together with local file
tools.

Inputs:

- workspace path or manuscript path;
- target journal if provided;
- author constraints.

Outputs:

- `paper_revision_work/artifacts.json`;
- the selected primary manuscript, or a single clarifying question where the
  choice is ambiguous;
- an editing strategy: direct editing, replacement passages, tracked changes, or
  discussion only.

Conclude this stage once the primary manuscript and the available supporting
materials have been identified.

### 1. Target-journal and recent-paper calibration

Responsible component: `sci-pre-submission-prep`, together with
`target-journal-calibration.md`.
Supporting components: `nature-academic-search`, `paper-search`.

Inputs:

- target journal;
- article type or inferred article type;
- topic/method keywords from the manuscript.

Outputs:

- `journal_profile.md`;
- a set of recent comparator papers;
- target-specific desk-reject risks;
- mandatory formatting, reporting, and data requirements.

Conclude this stage once current official guidance and a usable recent-paper
profile are available. If browsing or sources are unavailable, record the
residual risk and proceed only with provisional claims about the journal.

### 2. Evidence and claim audit

Responsible component: `paper-refinement-trinity-v2`.
Supporting component: `goal-driven-academic-papers`.

Inputs:

- manuscript;
- result files, tables, figures, code, logs, supplements;
- journal profile.

Procedure:

1. Map each major claim to its evidence anchor and mark its status.
2. Flag overclaim patterns (see `references/audit-matrix-and-final-gate.md`,
   Overclaim and Causation Guard):
   - causal verbs (cause, lead to, demonstrate, prove) used for observational or
     cross-sectional findings;
   - in-silico / in-vitro results extrapolated to clinical outcomes without
     boundary statements;
   - subgroup findings generalized to the full population;
   - associational findings reframed as efficacy or intervention effectiveness.
3. Downgrade or annotate `[EVIDENCE GAP: ...]` / `[CAUSAL GAP: ...]` for claims
   the evidence cannot support.
4. Verify that causal claims in observational studies satisfy the JAMA 2024
   tenability criteria (causal question, estimand, design, assumptions,
   sensitivity analyses, conditional interpretation); if not, require downgrade
   to associational language.

Outputs:

- `claim_ledger.md`;
- P0 evidence failures;
- unsupported or overstated claims to be qualified or removed;
- overclaim matches flagged in `paper_revision_work/overclaim_scan.md`;
- the smallest useful set of missing analyses or experiments.

Conclude this stage once the claims in the Abstract, Introduction, Results, and
Discussion carry a status of `supported`, `weak but bounded`, or `needs-author`,
and no causal-language overclaim remains unaddressed in non-RCT manuscripts.
Do not proceed to structural revision while unsupported central claims remain
stated strongly.

### 3. Top-journal narrative and structure

Responsible component: `top-journal-narrative-writing`.
Supporting component: `nature-writing`.

Inputs:

- factual contribution;
- claim register;
- journal profile;
- recent comparator papers.

Outputs:

- a diagnosis of the current narrative;
- three to five defensible narrative options where useful;
- a selected primary and secondary narrative;
- a claim–evidence–boundary table;
- a plan for the title, abstract, introduction, and discussion.

Conclude this stage once the primary narrative is defensible, bounded by the
evidence, and suited to the target journal. Then use `nature-writing` to
implement the section architecture.

### 4. Section-by-section manuscript revision

Responsible component: `nature-writing`.
Supporting components: `paper-refinement-trinity-v2`, `nature-polishing`.

Inputs:

- selected narrative;
- section plans;
- claim register;
- manuscript source.

Outputs:

- revised title, abstract, introduction, related work, methods, results,
  discussion, and conclusion as needed;
- a section-level record of edits;
- unresolved author placeholders.

Conclude this stage once each revised section has a clear purpose and all major
claims remain tied to evidence.

### 5. Details: numbers, citations, figures, data/code

Responsible components:

- numbers/details: `manuscript-writing-review` precision checks;
- citations: `nature-citation`, `nature-academic-search`, `paper-search`;
- figures/tables: `nature-figure`;
- data/code availability: `nature-data`.

Inputs:

- revised manuscript;
- source result files;
- figures/tables;
- bibliography;
- journal data/code policy.

Outputs:

- a list of citation gaps with notes on the strength of support;
- a list of mismatches among numbers, captions, and source data;
- corrections to figure and table logic;
- a uniform figure style and a fixed color scheme, in which each color denotes a
  single, stable meaning and is not reused for a different quantity or category;
- figure counts and displayed values that agree with the manuscript text and the
  underlying source data;
- Data Availability and code/materials statements;
- updated `revision_queue.md`.

Conclude this stage once no known mismatch in numbers, citations, figures, or
data and code remains unresolved, except for those marked as author checks, and
once all figures share a consistent style and a fixed color encoding.

### 6. Conditional engineering-terminology pass and integrated language pass

This stage has two ordered parts.

#### 6a. Engineering-terminology pass (conditional)

Apply when the manuscript contains AI/engineering-derived terminology, regardless
of target journal. The pass is especially critical for cross-disciplinary
submissions targeting biomedical informatics, medical AI, or clinical NLP
journals, but a lightweight scan is recommended for all AI/engineering
manuscripts to catch register drift.

**Primary path** (when `engineering-to-academic` skill is installed):  
Responsible component: `engineering-to-academic` skill.  
Supporting component: `scripts/scan_engineering_terms.py` for quick detection
or residual scanning; `references/engineering-terminology.md` for the protocol
and glossary.

**Fallback path** (self-contained, when the skill is unavailable):  
Responsible component: built-in `references/engineering-terminology.md`.  
Supporting component: `scripts/scan_engineering_terms.py`, or manual grep for
the glossary terms listed in the reference. The glossary covers model-versioning
terms (checkpoint, base, instruct), experimental-design terms (cell, lane,
delta), algorithm terms (gate, pipeline, artifact), and behavior terms (flip,
engagement, one-off).

Inputs:

- revised manuscript after structural and evidentiary revision;
- target journal readership expectations (biomedical vs. general academic).

Procedure (both paths):

1. Scan the manuscript against the glossary in `references/engineering-terminology.md`.
2. Review critical (🔴) and major (🟠) hits; replace the term with the academic
   equivalent, or introduce the academic term on first mention with the
   engineering term in parentheses.
3. Re-scan to verify that critical/major terminology has been addressed.
4. Cross-check that abbreviations such as PT and IFT are defined before first
   use.

Outputs:

- terminology-corrected manuscript;
- `paper_revision_work/eng_term_scan.md` (report from the skill or the local
  scan);
- list of unresolved terminology decisions requiring author input.

Conclude this stage once no critical or major engineering-terminology hits
remain unaddressed, required abbreviations are defined before first use, and
any unresolved author decisions are recorded. Completion is judged by the
terminology cross-check in `references/engineering-terminology.md`, not solely
by the existence of a scan report.

Do not use this pass to disguise weak evidence or unsupported claims.

#### 6b. Integrated language pass

Responsible component: `language-fusion.md`.  
Specialist components (preferred when installed): `nature-polishing`,
`manuscript-writing-review`, `humanizer_academic`, `academic-deai`,
`academic-deai-zh`.

**Fallback path** (self-contained, when specialist skills are unavailable):  
Execute the four-layer protocol documented in `references/language-fusion.md`
using only local file tools and the built-in pattern lists. See the reference
for concrete grep/Python scan commands, long-sentence thresholds (>40 words),
AI-residue keyword lists, and the acceptance criteria checklist.

Inputs:

- a structurally stable manuscript after the terminology pass;
- claim register;
- section-level record of edits.

Outputs:

- revised prose;
- `paper_revision_work/language_pass.md` (report on the language pass);
- any high-risk edits that were not made;
- remaining AI residue or manual checks.

Conclude this stage once clarity has improved without strengthening claims,
altering citation relationships, changing numbers, or flattening technical
meaning.

### 7. Technical review and micro-proofing

Responsible component: the `paper-review` protocol from
`tengda89757-edu/sciwrite`, where available.
Supporting components: `proofing_scan.py`, `manuscript-writing-review`,
`paper-refinement-trinity-v2`.

Inputs:

- revised manuscript;
- equations, appendices, notation, captions, and references;
- final PDF or text-like source when available.

Outputs:

- a list of technical and proofing risks;
- proofing-scan matches in `paper_revision_work/proofing_scan.txt`;
- corrections for high-confidence issues only.

Apply this stage when the manuscript contains equations, derivations,
implementation formulas, dense technical prose, or appendices, or when
final-submission proofing is required.

Use:

```bash
python scripts/proofing_scan.py <pdf-or-text-like-file> --max-hits 80 --out paper_revision_work/proofing_scan.txt
```

Manually verify each match reported by the script before treating it as a
genuine issue.

Conclude this stage once high-confidence proofing defects and technical-review
blockers have been corrected, marked `needs-author`, or explicitly placed out of
scope.

### 8. Submission/rebuttal package

Responsible components:

- submission package: `sci-pre-submission-prep`;
- reviewer response: `nature-response`;
- evidence consistency: `paper-refinement-trinity-v2`.

Inputs:

- revised manuscript;
- journal profile;
- reviewer comments or decision letter, if present.

Outputs:

- cover letter, highlights, title-page checklist, reporting checklist;
- a response matrix and point-by-point response where reviews exist;
- a checklist of manuscript changes.

Conclude this stage once every claim in the package maps to manuscript evidence
or to a justified placeholder.

### 9. Final verification checkpoint

Responsible component: `audit-matrix-and-final-gate.md`.
Supporting components: the relevant specialist skills.

Inputs:

- final manuscript and package;
- all working records.

Outputs:

- `verification.md`;
- final status: `ready`, `mostly ready`, `not ready`, or `blocked`;
- manual author checks.

Conclude only when the status is explicit and the residual risks are visible.

## Reuse Principle

Where a specialist skill already provides a sound rule, apply it directly rather
than restating it here. Add coordination only where the revision genuinely
requires transitions, ordering, state tracking, or the resolution of conflicts
between stages.
