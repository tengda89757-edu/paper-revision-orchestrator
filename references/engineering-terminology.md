# Engineering-to-Academic Terminology Pass

This reference governs the **engineering-to-academic terminology pass** for
manuscripts authored by AI/engineering researchers targeting biomedical
informatics, medical AI, or clinical NLP journals (e.g., *CMPB*, *JAMIA*,
*npj Digital Medicine*).

Researchers from open-source communities (Hugging Face, GitHub) routinely use
informal engineering terms—"checkpoint", "cell", "gate", "flip rate"—that
appear unprofessional or confusing to medical-informatics reviewers. This pass
systematically replaces such jargon with rigorous academic equivalents.

## Relationship to the `engineering-to-academic` skill

This reference is part of `paper-revision-orchestrator` and is intended to be
used **together with** the specialist `engineering-to-academic` skill. The
orchestrator should invoke that skill as the primary component for this pass;
this file provides the protocol, severity rules, and cross-check list. The
local `scripts/scan_engineering_terms.py` is a fallback scanner that prefers
the skill's `glossary.yaml` when installed, and otherwise uses an embedded
glossary so the orchestrator remains usable on its own.

## When to Apply

Apply this pass **before** the integrated language pass (`language-fusion.md`)
and after the structural/evidentiary revision is stable. The sequence becomes:

```text
engineering-terminology → language-fusion (nature-polishing → SCIWRITE → humanizer → de-AI)
```

## Severity Levels

| Level | Action | Typical Impact |
|-------|--------|----------------|
| **🔴 Critical** | Must fix before submission | Reviewer confusion, journal rejection risk |
| **🟠 Major** | Strongly recommended | Noticeable informality, domain mismatch |
| **🟡 Minor** | Fix if time permits | Slight register mismatch |
| **🔵 Style** | Optional polish | Preferred but not mandatory |

## Standard Replacement Protocol

### Step 1: Automated scan

Run the scanner against the manuscript:

```bash
python scripts/scan_engineering_terms.py paper/main.tex --out term_report.md
```

This produces a severity-ranked report with line numbers, context snippets, and
suggested replacements.

### Step 2: First-mention disambiguation

When an engineering term may be unfamiliar to the journal's readership,
introduce the academic term with the engineering term in parentheses **once**,
then use only the academic term:

> *"We evaluated three **model variants** (referred to as 'checkpoints' in
> open-source communities)..."*

### Step 3: Consistent abbreviation

Define abbreviations in the Introduction or Methods:

> *"In this study, 'pre-trained' (**PT**, colloquially 'base') and
> 'instruction-fine-tuned' (**IFT**, colloquially 'instruct') model variants
> were compared."*

### Step 4: Figure and table labels

Elevate figure legends and table headers:

| Original (Engineering) | Revised (Academic) |
|------------------------|--------------------|
| Instruction-tuning delta on separate axes | Performance differential induced by instruction fine-tuning |
| Prediction flip rate | Prediction inconsistency rate under perturbation |
| Low-engagement subset | Low-confidence-allocation subset |
| Evaluation lane 1 | Evaluation phase 1 |

### Step 5: Cross-check

After replacement, verify:
- [ ] No `checkpoint` remains except in code repository names
- [ ] `Cell`/`Lane` replaced in methodology descriptions
- [ ] `Gate` replaced with `decision rule` or `selection mechanism`
- [ ] `Flip`/`Engagement` replaced in results/discussion
- [ ] All abbreviations (PT, IFT) defined before first use

---

## Glossary

### 一、模型版本与状态类（Hugging Face 命名后缀）

| 工程术语 | 科研术语 (英文) | 科研术语 (中文) | 级别 | 修改理由 |
|----------|----------------|-----------------|------|----------|
| **Checkpoint** | **Model / Model variant / Model weights** | 模型 / 模型变体 / 模型权重 | 🔴 Critical | "Checkpoint"本意是训练过程中保存的断点文件。在科研评估中，我们评估的是"模型"本身或其"权重实例"。 |
| **Base / Base model** | **Pre-trained model (PT) / Foundation model** | 预训练模型 / 基础模型 | 🔴 Critical | "Base"是开源社区的命名后缀。科研上应准确描述其处于"预训练"阶段，尚未进行任务对齐。 |
| **Instruct / IT** | **Instruction-fine-tuned (IFT) / Aligned model** | 指令微调模型 / 对齐模型 | 🔴 Critical | "Instruct"是平台后缀。科研上应强调其经历了"指令微调"或"人类对齐"过程。 |

**Usage guidance:**
- *Checkpoint*: "trained model (often referred to as a 'checkpoint' in engineering contexts)"
- *Base/PT*: "pre-trained (PT, colloquially termed 'base' in open-source communities)"
- *Instruct/IFT*: 与 Base/PT 配对使用时，统一写为 PT/IFT 对比框架

### 二、实验设计与矩阵类（数据分析与流程图黑话）

| 工程术语 | 科研术语 (英文) | 科研术语 (中文) | 级别 | 修改理由 |
|----------|----------------|-----------------|------|----------|
| **Cell** (如 54 full cells) | **Experimental condition / Evaluation setting / Configuration** | 实验条件 / 评估设置 / 配置 | 🟠 Major | "Cell"是表格或实验矩阵的"单元格"（工程/数据黑话）。科研上应称为一个具体的"实验条件"。 |
| **Lane** (如 evaluation lane) | **Phase / Module / Evaluation branch** | 阶段 / 模块 / 评估分支 | 🟠 Major | "Lane"是画流程图（Swimlane diagram）时的"泳道"。在方法论描述中，应称为"阶段"或"模块"。 |
| **Delta** (如 tuning deltas) | **Performance differential / Marginal change** | 性能差异 / 边际变化 | 🟡 Minor | "Delta (Δ)"是理工科口语化的"差值"。正文中应规范表述为"性能差异"或"变化量"。 |

### 三、算法机制与策略类（代码逻辑术语）

| 工程术语 | 科研术语 (英文) | 科研术语 (中文) | 级别 | 修改理由 |
|----------|----------------|-----------------|------|----------|
| **Gate / Gating** (如 CCR gates) | **Decision rule / Selection mechanism / Filtering policy** | 决策规则 / 选择机制 / 过滤策略 | 🟠 Major | "Gate"在代码中指 if-else 路由或门控机制。在科研方法论中，本质上是一种"选择性预测的决策规则"。 |
| **Pipeline** | **Evaluation framework / Methodological workflow** | 评估框架 / 方法论工作流 | 🟡 Minor | "Pipeline"偏向工程上的代码脚本流。在科研论文中，使用"Framework"或"Workflow"更具学术高度。 |
| **Artifact / Bundle** | **Reproducibility package / Audit evidence / Supplementary materials** | 可重复性数据包 / 审计证据 / 补充材料 | 🟡 Minor | "Artifact"是软件工程（CI/CD）中的"构建产物"。在强调可重复性的科研论文中，应称为"可重复性数据包"。 |

### 四、模型行为与现象描述类（开发者社区俗语）

| 工程术语 | 科研术语 (英文) | 科研术语 (中文) | 级别 | 修改理由 |
|----------|----------------|-----------------|------|----------|
| **Flip / Flip rate** | **Prediction instability / Inconsistency rate** | 预测不稳定性 / 不一致率 | 🟠 Major | "Flip"指结果翻来覆去，太口语化。科研上描述模型对扰动的敏感度，通常使用"不稳定性"。 |
| **Engagement** (如 Low-engagement) | **Confidence allocation / Predictive conservatism** | 置信度分配 / 预测保守性 | 🟠 Major | 用"Engagement"形容模型不愿意输出高置信度不够准确，应改为"置信度分配稀疏"或"预测保守性"。 |
| **One-off artifact** | **Spurious correlation / Prompt-specific bias** | 伪相关 / 提示词特异性偏差 | 🟠 Major | 形容高置信度只是碰巧因为 Prompt 格式引起的。科研上应定义为"提示词诱导的偏差"。 |

---

## Before-and-After Examples

### Model versioning
- **Avoid:** *"We evaluated three checkpoints on the benchmark."*
- **Use:** *"We evaluated three model variants on the benchmark."*

- **Avoid:** *"The base model was fine-tuned on clinical notes."*
- **Use:** *"The pre-trained model (PT) was fine-tuned on clinical notes."*

### Experimental design
- **Avoid:** *"The experiment comprised 54 full cells."*
- **Use:** *"The experiment comprised 54 experimental conditions."*

### Algorithm mechanisms
- **Avoid:** *"The CCR gates filter low-confidence predictions."*
- **Use:** *"The CCR decision rules filter low-confidence predictions."*

### Model behavior
- **Avoid:** *"The flip rate increased under adversarial perturbation."*
- **Use:** *"The prediction inconsistency rate increased under adversarial perturbation."*

- **Avoid:** *"Low-engagement predictions were excluded."*
- **Use:** *"Predictions with low confidence allocation were excluded."*

---

## Maintenance

To extend this glossary:

1. Edit this file (`references/engineering-terminology.md`)
2. Add new rows to the appropriate category table
3. Update `scripts/scan_engineering_terms.py` regex patterns if automated scanning is desired
4. Update the version note in the scanner script

Contributions should focus on terms that cause **reviewer friction** in
cross-disciplinary submissions (AI → medicine/biology).
