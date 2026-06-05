# Language Fusion

Use this reference for English manuscript language passes after evidence,
structure, section architecture, numbers, citations, and figure claims are
stable.

The fusion order is:

```text
nature-polishing -> manuscript-writing-review (SCIWRITE) ->
humanizer_academic -> academic-deai safety guard
```

Do not run this pass to hide weak reasoning, unsupported claims, missing
evidence, or journal mismatch.

## Owner Roles

| Layer | Skill | What it contributes |
|---|---|---|
| Section flow | `nature-polishing` | Nature-leaning section logic, reader workflow, claim calibration |
| Scientific clarity | `manuscript-writing-review` | clutter removal, active voice, sentence architecture, terminology, numerical/citation consistency |
| AI residue detection | `humanizer_academic` | inflated significance, superficial -ing clauses, vague attributions, AI vocabulary, copula avoidance, generic conclusions |
| Safety guard | `academic-deai` | meaning preservation, citation relationship protection, edit-level control, transparent skipped-risk reporting |

For Chinese academic prose, use `academic-deai-zh` instead of the English
humanizer stack unless the output must be English.

## Fused Pass Sequence

### 1. Section-flow check

Use `nature-polishing` principles:

- confirm the section has the right rhetorical job;
- repair paragraph order before local sentence edits;
- keep claims near supporting evidence;
- avoid polishing Results into Discussion or Discussion into Results;
- preserve bounded, evidence-linked claims.

### 2. SCIWRITE precision pass

Use `manuscript-writing-review` as the precision core:

1. Remove clutter and dead-weight phrases.
2. Convert passive voice only when it obscures accountability.
3. Repair buried predicates and overloaded sentences.
4. Enforce keyword, group-name, variable-name, and acronym consistency.
5. Check numerical and citation-sensitive statements.

Do not mechanically shorten technical definitions, methods, equations, or
statistical statements.

### 3. Humanizer residue pass

Use `humanizer_academic` to remove AI-like patterns:

- inflated significance, legacy, or broader-trend claims;
- superficial present-participle explanations such as `highlighting`,
  `underscoring`, `showcasing`, `ensuring`;
- vague attributions such as `studies have shown` or `experts argue`;
- promotional words such as `groundbreaking`, `pivotal`, `crucial`,
  `showcase`, `landscape`, `testament`, `underscore`;
- copula avoidance such as `serves as`, `stands as`, `represents`;
- forced rule-of-three lists, negative parallelisms, false ranges, and elegant
  synonym cycling.

Replace vague language with specific evidence. If evidence is absent, weaken or
delete the claim instead of smoothing it.

### 4. Academic De-AI safety guard

Use `academic-deai` before accepting the rewrite:

- choose edit level: `No-op`, `Micro-edit only`, or `Full safe rewrite`;
- default to `Micro-edit only` for methods, exact result interpretation,
  citation-heavy related work, theorem-like text, and symbol-bearing passages;
- preserve technical meaning, citation intent, evidential strength, named
  algorithms, datasets, comparison bases, and numerical detail;
- report skipped high-risk edits and suspicious residue when relevant.

## Acceptance Criteria

A language pass passes only when:

- no unsupported claim became stronger;
- citation relationships and numerical statements are unchanged or verified;
- terminology is consistent across Methods, Results, captions, and Discussion;
- AI-like residue is reduced without making prose generic;
- any risky unchanged text is listed for manual review.

## Output Template

```text
Language pass:
Section(s):
Edit level:
Main changes:
Meaning/citation guard:
Remaining AI residue:
Skipped high-risk edits:
Manual checks:
```
