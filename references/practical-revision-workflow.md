# Practical Revision Workflow

Use this file for real manuscript modification runs. It turns the specialist
skills into a practical pipeline with stage inputs, outputs, handoffs, and stop
conditions.

The orchestrator should not rewrite specialist skills internally. It should use
them as stage owners and add the missing coordination layer: what to do first,
what artifact to produce, and what must be true before moving on.

## Full Pipeline

```text
0. Workspace discovery and safety
1. Target-journal and recent-paper calibration
2. Evidence and claim audit
3. Top-journal narrative and structure
4. Section-by-section manuscript revision
5. Details: numbers, citations, figures, data/code
6. Language fusion
7. Technical review and micro-proofing
8. Submission/rebuttal package
9. Final verification gate
```

## Stage Contracts

### 0. Workspace discovery and safety

Owner: `discover_paper_artifacts.py` plus local file tools.

Inputs:

- workspace path or manuscript path;
- target journal if provided;
- author constraints.

Outputs:

- `paper_revision_work/artifacts.json`;
- selected primary manuscript or one blocking question if ambiguous;
- edit strategy: direct edit, patch text, tracked-change workflow, or chat-only.

Exit when the primary manuscript and available support artifacts are known.

### 1. Target-journal and recent-paper calibration

Owner: `sci-pre-submission-prep` plus `target-journal-calibration.md`.
Support: `nature-academic-search`, `paper-search`.

Inputs:

- target journal;
- article type or inferred article type;
- topic/method keywords from the manuscript.

Outputs:

- `journal_profile.md`;
- recent comparator set;
- target-specific desk-reject risks;
- hard formatting/reporting/data requirements.

Exit when current official guidance and a usable recent-paper profile exist.
If browsing or sources are unavailable, mark residual risk and continue only with
provisional journal claims.

### 2. Evidence and claim audit

Owner: `paper-refinement-trinity-v2`.
Support: `goal-driven-academic-papers`.

Inputs:

- manuscript;
- result files, tables, figures, code, logs, supplements;
- journal profile.

Outputs:

- `claim_ledger.md`;
- P0 evidence breaks;
- unsupported or overstrong claims to weaken/delete;
- smallest useful missing analyses or experiments.

Exit when Abstract/Introduction/Results/Discussion claims have status:
`supported`, `weak but bounded`, or `needs-author`. Do not proceed to structure
polish while unsupported central claims remain strong.

### 3. Top-journal narrative and structure

Owner: `top-journal-narrative-writing`.
Support: `nature-writing`.

Inputs:

- factual contribution;
- claim ledger;
- journal profile;
- recent comparator papers.

Outputs:

- current story diagnosis;
- 3-5 defensible narrative options when useful;
- selected primary and backup narrative;
- claim-evidence-boundary table;
- title/abstract/introduction/discussion plan.

Exit when the primary narrative is defensible, evidence-bounded, and target-fit.
Then use `nature-writing` to implement section architecture.

### 4. Section-by-section manuscript revision

Owner: `nature-writing`.
Support: `paper-refinement-trinity-v2`, `nature-polishing`.

Inputs:

- selected narrative;
- section plans;
- claim ledger;
- manuscript source.

Outputs:

- revised title, abstract, introduction, related work, methods, results,
  discussion, and conclusion as needed;
- section-level edit log;
- unresolved author placeholders.

Exit when each revised section has a clear job and all major claims remain tied
to evidence.

### 5. Details: numbers, citations, figures, data/code

Owners:

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

- citation gap list and support-grade notes;
- number/caption/source-data mismatch list;
- figure/table logic fixes;
- Data Availability and code/materials statements;
- updated `revision_queue.md`.

Exit when no known number, citation, figure, or data/code mismatch remains
unresolved except marked author checks.

### 6. Language fusion

Owner: `language-fusion.md`.
Specialists: `nature-polishing`, `manuscript-writing-review`,
`humanizer_academic`, `academic-deai`, `academic-deai-zh`.

Inputs:

- structurally stable manuscript;
- claim ledger;
- section-level edit log.

Outputs:

- revised prose;
- language pass report;
- skipped high-risk edits;
- remaining AI residue or manual checks.

Exit when clarity improves without strengthening claims, altering citation
relationships, changing numbers, or flattening technical meaning.

### 7. Technical review and micro-proofing

Owner: `paper-review` protocol from `tengda89757-edu/sciwrite` when available.
Support: `proofing_scan.py`, `manuscript-writing-review`,
`paper-refinement-trinity-v2`.

Inputs:

- revised manuscript;
- equations, appendices, notation, captions, and references;
- final PDF or text-like source when available.

Outputs:

- technical/proofing risk list;
- proofing-scan hits in `paper_revision_work/proofing_scan.txt`;
- fixes for high-confidence issues only.

Run when the manuscript has equations, derivations, implementation formulas,
dense technical prose, appendices, or final submission proofing needs.

Use:

```bash
python scripts/proofing_scan.py <pdf-or-text-like-file> --max-hits 80 --out paper_revision_work/proofing_scan.txt
```

Spot-check every script hit before treating it as a real issue.

Exit when high-confidence proofing defects and technical-review blockers are
fixed, marked `needs-author`, or explicitly out of scope.

### 8. Submission/rebuttal package

Owners:

- submission package: `sci-pre-submission-prep`;
- reviewer response: `nature-response`;
- evidence consistency: `paper-refinement-trinity-v2`.

Inputs:

- revised manuscript;
- journal profile;
- reviewer comments or decision letter, if present.

Outputs:

- cover letter, highlights, title-page checklist, reporting checklist;
- response matrix and point-by-point response when reviews exist;
- manuscript-change checklist.

Exit when every package claim maps to manuscript evidence or a justified
placeholder.

### 9. Final verification gate

Owner: `audit-matrix-and-final-gate.md`.
Support: relevant specialist skills.

Inputs:

- final manuscript and package;
- all work artifacts.

Outputs:

- `verification.md`;
- final status: `ready`, `mostly ready`, `not ready`, or `blocked`;
- manual author checks.

Exit only when the status is explicit and the residual risks are visible.

## Optimization Rule

If a specialist skill already contains a strong rule, use it directly rather
than rewriting it in the orchestrator. Add orchestration only where the real
workflow needs handoffs, ordering, state tracking, or cross-stage conflict
resolution.
