# Integrated Language Pass

This reference governs the language pass for English manuscripts, undertaken once
the evidence, structure, section architecture, numbers, citations, and figure
claims are stable.

The sequence is:

```text
engineering-terminology -> nature-polishing -> manuscript-writing-review (SCIWRITE) ->
humanizer_academic -> academic-deai safeguard
```

The `engineering-terminology` pass is inserted first when the manuscript
originates from AI/engineering practice (Hugging Face, GitHub) and targets
biomedical informatics or medical AI journals. It replaces informal engineering
jargon—"checkpoint", "cell", "gate", "flip rate"—with rigorous academic
terminology before the prose-level passes begin. See
[`engineering-terminology.md`](engineering-terminology.md) for the glossary,
severity levels, and scanner usage.

This pass must not be used to disguise weak reasoning, unsupported claims,
missing evidence, or a mismatch with the journal.

## Self-Contained Execution Guide

When the specialist skills (`nature-polishing`, `manuscript-writing-review`,
`humanizer_academic`, `academic-deai`) are not installed, execute the four
passes below using only local file tools. The outputs must match the
deliverables of the specialist pipeline.

### Quick-scan commands

Run these at the start of the language pass to baseline the manuscript:

```bash
# AI residue scan (Python)
python3 -c "
import re
with open('main.tex') as f:
    text = f.read()
patterns = {
    'inflated': r'\b(groundbreaking|pivotal|crucial|landmark|seminal|paradigm-shifting)\b',
    'superficial_ing': r'\b(highlighting|underscoring|showcasing|ensuring|demonstrating|revealing)\b',
    'vague_attr': r'\b(studies have shown|experts argue|it is widely known|research suggests that)\b',
    'promotional': r'\b(showcase|landscape|testament|underscore|pave the way|open new avenues)\b',
    'copula': r'\b(serves as|stands as|represents|acts as|functions as)\b',
}
for name, pat in patterns.items():
    hits = len(re.findall(pat, text, re.IGNORECASE))
    print(f'{name}: {hits}')
"

# Long sentences (>40 words)
python3 -c "
import re
with open('main.tex') as f:
    text = f.read()
sents = re.split(r'[.!?]\s+', text)
long = [s for s in sents if len(s.split()) > 40]
print(f'Long sentences (>40 words): {len(long)}')
for s in long[:5]:
    print(f'  {len(s.split())} words: {s[:120]}...')
"

# Redundancy patterns
grep -c 'it is important to note that' main.tex
grep -c 'in order to' main.tex
grep -c 'due to the fact that' main.tex

# Passive voice estimate
python3 -c "
import re
with open('main.tex') as f:
    text = f.read()
passive = ['was', 'were', 'is', 'are', 'been', 'being']
count = sum(len(re.findall(rf'\b{p}\s+\w+ed\\b', text, re.I)) for p in passive)
print(f'Estimated passive constructions: ~{count}')
"

# Core term consistency
python3 -c "
import re
with open('main.tex') as f:
    text = f.read()
terms = ['generation availability', 'realized exposure', 'conditional shift',
         'target shift', 'self-gate', 'gating condition', 'attacker',
         'defender', 'intervention', 'baseline', 'target-unaware',
         'target-aware', 'strict-deception', 'broad-codebook',
         'partial identification', 'identification boundary']
for t in terms:
    print(f'{t:25s}: {len(re.findall(t, text, re.I)):3d}')
"
```

### Long-sentence repair heuristic

A sentence exceeding 40 words is a candidate for splitting. Before editing,
verify it is not a list, a definition, or a formal theorem statement.

Repair strategies (in order of preference):
1. **Split at a conjunction** (`, and`, `;`, `:`) into two independent sentences.
2. **Extract a parenthetical clause** into its own sentence.
3. **Demote a subordinate clause** to a preceding or following sentence.
4. **Avoid**: turning one long sentence into three or more short sentences; this
   can fragment the logical flow.

Example:
- Before: *"The paper contributes (i) an estimand taxonomy separating generation availability, realized exposure, generated-subset conditional shift, and partial-identification bounds; (ii) a measurement protocol separating observable decision shift from post-hoc tactic labels; and (iii) a reporting rule requiring the generation process, denominator, measurement label, and identification boundary before any target-aware rate is interpreted."* (51 words)
- After: *"The paper contributes three things: an estimand taxonomy...; a measurement protocol...; and a reporting rule.... The underlying selection principle is standard."*

## Contributing Components

| Layer | Skill | Contribution |
|---|---|---|
| Section flow | `nature-polishing` | Nature-leaning section logic, reader guidance, claim calibration |
| Scientific clarity | `manuscript-writing-review` | removal of redundancy, active voice, sentence structure, terminology, numerical and citation consistency |
| AI residue detection | `humanizer_academic` | inflated significance, superficial -ing clauses, vague attributions, AI vocabulary, copula avoidance, generic conclusions |
| Safeguard | `academic-deai` | meaning preservation, protection of citation relationships, edit-level control, transparent reporting of skipped risks |

For Chinese academic prose, use `academic-deai-zh` in place of the English
humanizer components, unless the output must be in English.

## Sequence of Passes

### 1. Section-flow check

Apply the principles of `nature-polishing`:

- confirm that the section serves the correct rhetorical purpose;
- correct paragraph order before local sentence-level edits;
- keep claims close to their supporting evidence;
- avoid polishing Results into Discussion or Discussion into Results;
- preserve bounded claims that are linked to evidence.

### 2. SCIWRITE precision pass

Use `manuscript-writing-review` as the core of this pass:

1. Remove redundancy and superfluous phrasing.
2. Convert passive voice only when it obscures accountability.
3. Repair buried predicates and overloaded sentences.
4. Enforce keyword, group-name, variable-name, and acronym consistency.
5. Check numerical and citation-sensitive statements.

Do not mechanically shorten technical definitions, methods, equations, or
statistical statements.

### 3. Humanizer residue pass

Use `humanizer_academic` to remove patterns characteristic of AI-generated text:

- inflated significance, legacy, or broader-trend claims;
- superficial present-participle explanations such as `highlighting`,
  `underscoring`, `showcasing`, `ensuring`;
- vague attributions such as `studies have shown` or `experts argue`;
- promotional words such as `groundbreaking`, `pivotal`, `crucial`,
  `showcase`, `landscape`, `testament`, `underscore`;
- copula avoidance such as `serves as`, `stands as`, `represents`;
- forced rule-of-three lists, negative parallelisms, false ranges, and elegant
  synonym cycling.

Replace vague language with specific evidence. Where evidence is absent, qualify
or remove the claim rather than smoothing it over.

### 4. Academic de-AI safeguard

Apply `academic-deai` before accepting the revised text:

- select an editing level: `No-op`, `Micro-edit only`, or `Full safe rewrite`;
- default to `Micro-edit only` for methods, exact result interpretation,
  citation-heavy related work, theorem-like text, and symbol-bearing passages;
- preserve technical meaning, citation intent, evidential strength, named
  algorithms, datasets, comparison bases, and numerical detail;
- report any high-risk edits not made, and any suspicious residue, where
  relevant.

## Acceptance Criteria

A language pass is acceptable only when:

- no unsupported claim has been strengthened;
- causal verbs (*cause, lead to, demonstrate, prove, induce*) are absent from
  observational/cross-sectional findings unless the causal assumptions are
  explicitly defended;
- citation relationships and numerical statements are unchanged or verified;
- terminology is consistent across Methods, Results, captions, and Discussion;
- AI-like residue has been reduced without rendering the prose generic;
- any risky text left unchanged is listed for manual review.

## Reporting Template

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
