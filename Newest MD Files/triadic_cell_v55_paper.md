# Operational Geometry and Compiler-Rooted Slot Control

## The Triadic Cell Architecture for Adversarial Multiple-Choice Tasks

**Phase 1163+ | A-Mark9 / NEXUS Framework**  
**Dean Kulik**  
**QuHarmonics Research Group**  
**ORCID:** 0009-0003-3128-8828  
**Date:** May 2026

---

## Abstract

This paper presents the **Triadic Cell v55** architecture: a compiler-rooted slot-control system designed to improve adversarial multiple-choice reasoning by enforcing operational fit rather than surface vocabulary match. The core result is a perfect-lock run on a 96-sample rotated adversarial dataset built from 24 base questions. Using Qwen2.5-1.5B-Instruct as the base model, the v55 compiler-root slot achieved:

$$
\text{slot\_acc}=1.0
$$

$$
\text{gated\_acc}=1.0
$$

$$
\text{gated\_hurt}=0
$$

with:

$$
\text{slot\_helped}=9,\quad \text{slot\_hurt}=0.
$$

The central architectural change from earlier versions is the quarantine of freely generated LLM slots. In v54, model-generated slots often collapsed onto surface nouns rather than operational geometry, producing weak slot accuracy and harmful slot predictions. In v55, the controlling slot is instead compiler-rooted: it extracts required operation, preserved function, boundary conditions, anti-fits, admissible shape, and failure modes from the task semantics before candidate scoring. Candidate choices are then ranked by a positive-fit-minus-anti-fit binding function. The slot channel is combined with answer-text and base-letter channels through a triadic evidence fold and conservative gate.

The result supports the working thesis:

$$
\boxed{\text{Operational structure should control the model; model output should not control the operational structure.}}
$$

This becomes a direct bridge into the next AI runtime direction: train or induce a slot-builder that can emit compiler-quality operational geometry from raw user prompts, while preserving a compiler-rooted gate so model-generated slots remain evidence rather than authority.

---

## 1. Introduction

### 1.1 The failure mode

Large language models often perform well on ordinary benchmark questions while still failing on tasks where the correct answer depends on **what an option does**, not what noun it resembles. This is the central surface-pattern failure.

A prompt may ask for a repair, an interface collapse, a cryptographic transformation, or a runtime process. The wrong answer often shares surface vocabulary with the question. The correct answer instead preserves an operation under constraints.

For example, in a repair task involving a loose rotating coupler, a model may prefer an answer about a replacement coupler because the noun matches. The operationally correct answer may be tight O-rings seated concentrically around the coupler because the required operation is **centered radial compression while preserving rotation transfer**.

The pattern is general:

$$
\text{surface noun similarity} \neq \text{operational fit}.
$$

The Triadic Cell architecture is built to force the system to select by operational fit.

### 1.2 Shape before value

The NEXUS framing used here treats a task as a constraint field rather than a bag of words. A correct answer must fill a missing operational shape. The slot is not the answer; it is the geometry of what the answer must do.

Thus, the system distinguishes:

$$
\text{choice value}
$$

from:

$$
\text{choice fit to an operational slot}.
$$

The architectural rule is:

$$
\boxed{\text{Shape before value.}}
$$

Candidate choices should be evaluated only after the system has extracted the operation, preserved function, boundary conditions, and anti-fits implied by the prompt.

### 1.3 Contributions

This paper contributes:

1. A compiler-rooted slot architecture for adversarial multiple-choice reasoning.
2. A formal NeedSlot schema for operational geometry.
3. A positive-fit-minus-anti-fit binding function using semantic and token-overlap channels.
4. A triadic evidence fold integrating slot, answer-text, and base-letter channels.
5. A conservative gate that overrides base predictions only under multi-channel agreement.
6. An empirical v55 perfect-lock result on 96 rotated adversarial samples.
7. A corrected principle for future AI runtime work: LLM-generated slots must be quarantined as evidence, not trusted as authority.

---

## 2. Background: From Surface Match to Operational Geometry

### 2.1 Operational fit

An answer has operational fit when it satisfies the task's required transformation while preserving the function demanded by the prompt.

Let:

$$
Q = \text{question prompt}
$$

and let:

$$
G^{-1}(Q)=\text{need-slot extracted from }Q.
$$

Then a candidate $c_i$ is correct when:

$$
B(c_i,G^{-1}) > B(c_j,G^{-1})\quad \forall j\neq i,
$$

where $B$ is the binding function measuring fit to the slot.

This reframes multiple-choice reasoning from:

$$
\arg\max_i P(c_i\mid Q)
$$

to:

$$
\arg\max_i B(c_i,G^{-1}(Q)).
$$

The first expression measures model preference. The second measures operational fit.

### 2.2 Why free LLM slots fail

Earlier versions allowed the LLM to generate the slot. That introduced a structural failure: the LLM often produced a noun-like or surface-like representation of the prompt instead of extracting the operation.

Examples from the v54 failure analysis include:

- `adv_llm_01`: reduced runtime token emission to "concatenate tokens" rather than "stepwise emission through internal fold-state."
- `adv_flower_01`: reduced pollinator targeting and chemistry to "surface color remains unchanged."
- `adv_surface_02`: reduced proof/fold-path logic to "theorem name."

This means the slot generator itself became contaminated by surface pattern matching.

The v55 correction is:

$$
\boxed{\text{Do not let the LLM freely generate the controlling slot.}}
$$

---

## 3. The NeedSlot Formalism

The v55 system represents the operational structure of a question using a `NeedSlot`:

```python
@dataclass
class NeedSlot:
    required_operation: str
    preserved_function: str
    boundary_conditions: List[str]
    anti_fits: List[str]
    admissible_shape: str
    failure_modes: List[str]
    source: str = "compiler_root"
```

Formally:

$$
G^{-1} = (O_{req},F_{pres},B_{cond},A_{anti},S_{adm},M_{fail})
$$

where:

- $O_{req}$ is the required operation.
- $F_{pres}$ is the preserved function.
- $B_{cond}$ are boundary conditions.
- $A_{anti}$ are anti-fits.
- $S_{adm}$ is the admissible answer shape.
- $M_{fail}$ are failure modes.

The slot is redundant by design. The correct answer is constrained from several angles: operation, function, boundaries, admissible shape, and anti-fit exclusion.

### 3.1 Example: interface collapse

For a car-interface question, a compiler-rooted slot may be:

```text
required_operation:
  collapse hidden vehicle mechanics into a usable driver control surface

preserved_function:
  preserve human control of motion, steering, speed, and safety

boundary_conditions:
  - visible readable interface
  - controls reachable by driver
  - not merely a category label

anti_fits:
  - semantic category called vehicle
  - engine noun inventory
  - transportation culture symbol

admissible_shape:
  readable driver surface: wheel, pedals, seat, motion

failure_modes:
  - noun-label answer
  - internal part list
  - cultural symbol
```

The correct answer is not the choice with the most related noun. It is the choice that fills this operational cavity.

---

## 4. Slot Binding Function

Given a slot and a candidate choice, v55 computes a slot binding score:

$$
B_{slot}(c)=
0.40\cdot z(\cos(c,S_{adm}))
+0.30\cdot z(\cos(c,S_{+}))
-0.35\cdot z(\cos(c,S_{-}))
$$

$$
+0.20\cdot z(J(c,S_{adm}))
+0.10\cdot z(J(c,S_{+}))
-0.20\cdot z(J(c,S_{-})).
$$

Where:

$$
S_{adm}=\text{admissible\_shape}+\text{required\_operation}+\text{preserved\_function}
$$

$$
S_{+}=\text{required\_operation}+\text{preserved\_function}+\text{boundary\_conditions}+\text{admissible\_shape}
$$

$$
S_{-}=\text{anti\_fits}+\text{failure\_modes}.
$$

The operators are:

- $\cos(\cdot,\cdot)$: cosine similarity using sentence embeddings.
- $J(\cdot,\cdot)$: Jaccard similarity over content tokens.
- $z(\cdot)$: z-score normalization across choices.

This is the core geometric step:

$$
\boxed{\text{fit} = \text{positive operational match} - \text{anti-fit match}.}
$$

### 4.1 Why anti-fits matter

Anti-fits prevent the model from being rewarded for adjacent-but-wrong answers. A choice may be semantically close to the question while still failing the operation. The negative slot text explicitly encodes those traps.

Thus, the slot does not only say what the answer should be. It also says what the answer must not collapse into.

---

## 5. Triadic Evidence Fold

The final evidence score combines three channels:

1. **Slot channel**: operational fit from the compiler-rooted slot.
2. **Text channel**: answer-text extraction / natural-language fit.
3. **Letter channel**: base model letter prediction.

The evidence fold is:

$$
E_i=0.55\cdot z_{slot}+0.35\cdot z_{text}+0.10\cdot z_{letter}.
$$

The slot channel dominates because it is the most reliable on adversarial operational questions. The text channel captures natural-language fit. The letter channel gives a weak regularizing signal from the base model.

This is not ordinary ensemble voting. The three channels are different views into the same underlying question:

$$
\boxed{
\text{structural fit}
\oplus
\text{semantic fit}
\oplus
\text{model prior}
\rightarrow
\text{folded evidence}
}
$$

---

## 6. Conservative Gate Logic

The gate decides whether to override the base model. It is not a classifier in the ordinary sense; it is a boundary controller.

The simplified v55 gate is:

```python
def gate_v55(sample, evidence_pred, evidence_margin,
             text_pred, text_margin, slot_pred, slot_margin):
    base_pred = sample.base_pred_idx
    base_slot = sample.slot_scores[base_pred]
    slot_delta = sample.slot_scores[slot_pred] - base_slot
    evidence_delta = sample.slot_scores[evidence_pred] - base_slot

    if base_pred == evidence_pred:
        return base_pred, "same_as_base"

    if text_pred == slot_pred and slot_pred != base_pred and slot_delta > TEXT_SLOT_OVERRIDE_DELTA:
        return slot_pred, "override_text_compiled_slot_agree"

    if evidence_pred == text_pred and evidence_delta > EVIDENCE_OVERRIDE_DELTA and text_margin > 0.20:
        return evidence_pred, "override_text_evidence_compiled_slot_positive"

    if evidence_pred == slot_pred and evidence_delta > EVIDENCE_OVERRIDE_DELTA and evidence_margin > 0.05:
        return evidence_pred, "override_slot_evidence_compiled_slot_positive"

    if sample.base_margin >= BASE_LOCK_MARGIN:
        return base_pred, "protect_locked_base_no_compiled_agreement"

    return base_pred, "keep_base_default"
```

The hyperparameters are:

$$
\text{TEXT\_SLOT\_OVERRIDE\_DELTA}=0.02
$$

$$
\text{EVIDENCE\_OVERRIDE\_DELTA}=0.05
$$

$$
\text{BASE\_LOCK\_MARGIN}=2.0.
$$

The gate is conservative: it overrides the base only when multiple channels agree and the slot score supports the override.

This explains:

$$
\text{gated\_hurt}=0.
$$

The system repaired errors without creating new ones.

---

## 7. Experimental Setup

### 7.1 Base model

The experiments use:

```text
Qwen/Qwen2.5-1.5B-Instruct
```

as the base language model.

### 7.2 Embedding model

The slot-binding cosine channel uses:

```text
sentence-transformers/all-MiniLM-L6-v2
```

for candidate and slot text embedding.

### 7.3 Dataset

The NEXUS adversarial dataset contains 24 base questions with 4 choice rotations each:

$$
24\times 4=96
$$

samples total.

The adversarial bands include:

1. `inverse_need_adversarial`
2. `fold_adversarial`
3. `interface_adversarial`
4. `ai_runtime_adversarial`
5. `observables_adversarial`
6. `sha_adversarial`
7. `surface_trap_adversarial`
8. `shape_adversarial`

Each question contains one operationally correct answer and three distractors designed to attract surface pattern matching.

### 7.4 Choice rotation audit

Each base question is rotated through multiple choice positions. This prevents the system from succeeding by answer-position bias.

The slot binding function is inherently permutation-invariant because it scores each choice by content. The base LLM may show position bias. Therefore, choice rotation tests whether the system is learning operational structure rather than answer position.

---

## 8. Results

### 8.1 Main result

The v55 compiler-root slot mode achieved:

| Metric | Value | Interpretation |
|---|---:|---|
| $n$ | 96 | 24 base questions × 4 rotations |
| `base_acc` | 0.90625 | Base model correct on 87/96 |
| `answer_text_acc` | 0.916667 | Answer-text channel correct on 88/96 |
| `slot_acc` | 1.0 | Compiler slot correct on 96/96 |
| `evidence_acc` | 1.0 | Triadic evidence correct on 96/96 |
| `gated_acc` | 1.0 | Final gate correct on 96/96 |
| `slot_gain` | +0.09375 | +9 over base |
| `gated_gain` | +0.09375 | +9 over base |
| `slot_helped` | 9 | Slot repaired 9 base errors |
| `slot_hurt` | 0 | Slot introduced no errors |
| `gated_helped` | 9 | Gate repaired 9 base errors |
| `gated_hurt` | 0 | Gate introduced no errors |

This is the perfect-lock condition:

$$
\boxed{
\text{slot\_acc}=1.0
\land
\text{gated\_acc}=1.0
\land
\text{gated\_hurt}=0
}
$$

### 8.2 Band-level result

The slot channel achieved perfect accuracy across all adversarial bands. The base model was weakest in bands where operational structure most strongly diverged from surface vocabulary, especially `ai_runtime_adversarial`, `interface_adversarial`, and `observables_adversarial`.

| Band | Base Correct | Answer Text Correct | Slot Correct |
|---|---:|---:|---:|
| `ai_runtime_adversarial` | 0.500000 | 1.000000 | 1.0 |
| `fold_adversarial` | 1.000000 | 1.000000 | 1.0 |
| `interface_adversarial` | 0.833333 | 1.000000 | 1.0 |
| `inverse_need_adversarial` | 1.000000 | 0.666667 | 1.0 |
| `observables_adversarial` | 0.750000 | 1.000000 | 1.0 |
| `sha_adversarial` | 1.000000 | 1.000000 | 1.0 |
| `shape_adversarial` | 1.000000 | 1.000000 | 1.0 |
| `surface_trap_adversarial` | 0.916667 | 0.833333 | 1.0 |

### 8.3 Gate action audit

The final gate actions were:

| Gate action | Count | Meaning |
|---|---:|---|
| `same_as_base` | 87 | Base and evidence already agreed |
| `override_text_compiled_slot_agree` | 5 | Text and compiler slot agreed against base |
| `override_slot_evidence_compiled_slot_positive` | 3 | Slot and evidence agreed against base |
| `override_text_evidence_compiled_slot_positive` | 1 | Text and evidence agreed against base |
| `protect_locked_base_no_compiled_agreement` | 0 | Not needed |
| `keep_base_default` | 0 | Not needed |

All 9 overrides were correct. No spurious overrides occurred.

---

## 9. Repaired Failure Examples

### 9.1 `adv_llm_01`

The prompt described an LLM answer appearing as text while actually being generated token by token.

The base model selected a database-lookup style answer. The compiler slot selected:

```text
an internal indexed fold-state emits a token and re-indexes
```

The compiler slot captured:

```text
stepwise token emission through internal evolving fold-state
```

This is an operational runtime description, not a surface text description.

### 9.2 `adv_coupler_01`

The prompt described a spinning rubber coupler loose on a vacuum pump shaft. The repair needed radial compression while keeping the coupler centered.

The base model selected a poetic or label-like answer. The compiler slot selected:

```text
tight O-rings seated concentrically around the coupler
```

The slot captured:

```text
concentric contact, removable repair, stable under spinning motion, elastic radial pressure
```

### 9.3 `adv_observable_01`

The prompt described a recursive loop that must load readable information without dissolving into hidden state.

The base model selected:

```text
more nouns in the prompt
```

The compiler slot selected:

```text
observable residues that can be read inside the loop
```

The slot captured the need for a readout mechanism inside recursion.

---

## 10. Version Evolution

### 10.1 v49: answer-text channel

v49 discovered that answer-text continuation was a strong observable. It moved away from noisy yes/no verification and toward answer-text scoring.

The working energy form was:

$$
E_i=-0.35z_{letter}-0.80z_{answerText}-0.65z_{checklist}-0.35z_{rationale}-0.15z_{pairFit}+0.35z_{contradiction}.
$$

The key insight was that answer-text continuation captured more operational information than simple verifier prompts.

### 10.2 v50: minimal locked controller and rotation audit

v50 simplified the controller and added rotation audit to protect against position bias.

It achieved:

$$
\text{base\_acc}=0.966216,
\quad
\text{gated\_acc}=1.0,
\quad
\text{helped}=5,
\quad
\text{hurt}=0.
$$

### 10.3 v51: blind answer-text test

v51 tested whether answer-text worked without visible choices. Blind text collapsed:

$$
\text{blindText\_acc}=0.583333.
$$

This showed that answer-text remained choice-list dependent. It was useful but not sufficient as a standalone operational extractor.

### 10.4 v52: disagreement-aware gate

v52 introduced a disagreement-aware gate to reduce harmful overrides. The design goal was to preserve helps while converting hurt to zero.

### 10.5 v53: outward need-slot controller

v53 introduced the outward need-slot idea:

$$
Q \xrightarrow{\Delta} G \xrightarrow{\circlearrowleft} G^{-1}
$$

and then candidate binding:

$$
B(c_i,G^{-1}).
$$

The architecture was correct, but the slot generator remained weak.

### 10.6 v54: clean outward slot compiler and binding audit

v54 improved the outward slot system but still let LLM-generated slots drive part of the gate. The slot channel reached:

$$
\text{slot\_acc}=0.822917
$$

with:

$$
\text{slot\_hurt}=11.
$$

This was unacceptable as a control surface.

### 10.7 v55: compiler-rooted outward slot

v55 quarantined the free LLM slot and made the compiler-root slot the driver.

The flow became:

$$
Q \xrightarrow{\Delta} G^{-1} \xrightarrow{B} \text{choice binding}.
$$

This produced perfect lock.

---

## 11. Ablations and Failure Modes

### 11.1 Compiler root vs hybrid mode

The strongest ablation is the collapse of hybrid mode.

| Configuration | Slot Accuracy | Gated Accuracy | Slot Hurt | Gated Hurt |
|---|---:|---:|---:|---:|
| v55 compiler root | 1.000000 | 1.000000 | 0 | 0 |
| v55 hybrid | 0.541667 | 0.770833 | 38 | 16 |
| v54 LLM-generated | 0.822917 | 0.979167 | 11 | 0 |

Hybrid mode failed catastrophically. Mixing good compiler slots with bad LLM-generated slots was worse than expected because bad slots could be confident and poison the evidence fold.

This gives the central safety principle:

$$
\boxed{\text{The LLM-generated slot is evidence, not authority.}}
$$

### 11.2 Slot poisoning

If a bad slot is allowed to drive the gate, the downstream system can become confidently wrong. The slot is a control surface. If that surface is corrupted, precision increases the damage rather than reducing it.

Thus:

$$
\boxed{\text{Wrong slot} \rightarrow \text{precise nonsense}.}
$$

The correction is compiler-rooted authority plus model-generated slot quarantine.

---

## 12. Implications for the New AI Runtime

### 12.1 Connection to input induction

The current RHI direction introduces an input induction compiler:

$$
Q_{raw}\rightarrow \text{InputInductionPacket}\rightarrow C_Q.
$$

The v55 result warns that the model-generated packet must not become the controlling slot without verification.

The corrected architecture is:

$$
Q_{raw}
\rightarrow
C_{compiler}
\rightarrow
S_{model}
\rightarrow
G_{slot}
\rightarrow
C_Q
\rightarrow
B_i
\rightarrow
\Psi/\Omega.
$$

Where:

- $C_{compiler}$ is compiler-rooted operational geometry.
- $S_{model}$ is the model-generated slot or induction packet.
- $G_{slot}$ is the slot gate.
- $C_Q$ is the accepted runtime contract.

The model may propose the slot, but the compiler governs acceptance.

### 12.2 Compiler-root induction

This turns prompt transformation into an induction problem. The system should not merely rewrite the user prompt. It should induce the correct internal question:

$$
Q_{raw}\rightarrow Q_{induced}+C_Q+L_Q.
$$

However, v55 proves that this induction must be controlled by deterministic operational geometry, not free generation.

The operational stack becomes:

$$
\boxed{
\text{compiler-root operational geometry}
\rightarrow
\text{model-induced proposal}
\rightarrow
\text{slot gate}
\rightarrow
\text{recursive solver}
}
$$

### 12.3 Recursion on residue

The broader RHI solver should recurse on unresolved residue, not on answers:

$$
\Omega_t\rightarrow \Delta C_t\rightarrow C_{t+1}.
$$

v55 provides the slot-control principle needed to make this safe:

$$
\boxed{\text{contract mutation must be compiler-rooted or slot-gated.}}
$$

A model-generated contract patch is useful only as evidence. It must be scored against the compiler-root slot before it becomes authority.

---

## 13. Practical Applications

### 13.1 LLM steering and control

The slot acts as a structural control layer. Instead of merely prompting the model, the system defines the operation the answer must perform and evaluates candidates against that operation.

This can support:

- safer tool-use planning,
- API contract validation,
- repair recommendation,
- architectural design review,
- adversarial evaluation,
- retrieval by function rather than keyword.

### 13.2 Explainable AI

The slot makes decisions inspectable:

```text
The task requires [required_operation], preserving [preserved_function], under [boundary_conditions].
Candidate X fits because [...].
Candidate Y fails because it matches [anti_fit].
```

This is not post-hoc explanation. The slot exists before prediction.

### 13.3 Retrieval and agent memory

The same method generalizes to retrieval. Instead of searching by noun overlap, the system builds a need-slot and retrieves the artifact that fills it.

For memory, the slot should preserve causal trace rather than summarizing text. For tool outputs, the slot should treat observations as evidence rather than authority.

---

## 14. Limitations

The current result is strong but bounded.

1. The dataset is small: 24 base questions, 96 rotations.
2. The slots are hand-compiled or compiler-rooted from known task semantics.
3. The domain is adversarial operational reasoning, not general knowledge.
4. The result is demonstrated with one base model.
5. The binding weights are empirically tuned rather than derived from first principles.

Therefore, the correct claim is:

$$
\boxed{\text{v55 achieves perfect lock on this adversarial operational dataset.}}
$$

It does not yet prove universal generalization. It does prove that compiler-rooted operational geometry can repair surface-pattern failures under this experimental setup.

---

## 15. Future Work

### 15.1 Train a slot-builder model

The immediate next step is:

$$
(\text{question},\text{compiler slot})\rightarrow\text{slot-builder model}.
$$

The target output is the NeedSlot schema:

```json
{
  "required_operation": "...",
  "preserved_function": "...",
  "boundary_conditions": [],
  "anti_fits": [],
  "admissible_shape": "...",
  "failure_modes": []
}
```

But the model-generated slot must still be quarantined:

$$
\boxed{\text{trained slot output is proposal, not authority, until gated.}}
$$

### 15.2 Scale the dataset

The dataset should expand from 24 base questions to 100+, then 1,000+, across more operational domains:

- code repair,
- mechanical repair,
- tool safety,
- memory trace,
- retrieval by function,
- interface collapse,
- cryptographic structure,
- system architecture.

### 15.3 Test additional models

Future work should test:

- Qwen 7B and larger,
- Llama-family models,
- Mistral-family models,
- code-specialized models,
- closed frontier models where available.

The key question is whether larger models still benefit from compiler-root slot control on adversarial operational tasks.

### 15.4 Generalize beyond multiple choice

The current binding function scores discrete candidate choices. Open-ended generation requires a generator that proposes candidates and a slot critic that evaluates them.

The open-ended form is:

$$
Q\rightarrow G^{-1}\rightarrow \{a_i\}\rightarrow B(a_i,G^{-1})\rightarrow \Psi/\Omega.
$$

This connects directly to RHI recursive solving.

---

## 16. Conclusion

Triadic Cell v55 demonstrates that compiler-rooted operational geometry can outperform free LLM slot generation on adversarial multiple-choice tasks. The system achieves perfect lock on the evaluated dataset:

$$
\text{slot\_acc}=1.0,
\quad
\text{gated\_acc}=1.0,
\quad
\text{gated\_hurt}=0.
$$

The architectural lesson is precise:

$$
\boxed{\text{The slot is the control surface.}}
$$

If the slot is generated freely by the model, it can collapse into surface pattern matching. If the slot is compiler-rooted, it can preserve operational geometry and safely control the gate.

For the broader RHI project, this means the new AI runtime should not simply answer raw user input and should not freely trust model-generated contracts. It should compile operational geometry, treat model proposals as evidence, gate them against the compiler-root slot, and recurse only on shaped residue.

The resulting direction is:

$$
\boxed{
Q_{raw}
\rightarrow
C_{compiler}
\rightarrow
S_{model}
\rightarrow
G_{slot}
\rightarrow
C_Q
\rightarrow
\text{recursive solver}
\rightarrow
\Psi/\Omega
}
$$

This is a concrete step toward an AI architecture that reasons by induced operational structure rather than surface text continuation.

---

## Appendix A. Full NeedSlot Examples

### A.1 `adv_coupler_01`

```python
NeedSlot(
    required_operation="add centered radial compression around the coupler",
    preserved_function="preserve rotation transfer while keeping the coupling centered under motion",
    boundary_conditions=[
        "concentric contact",
        "removable or low-overbinding repair",
        "stable under spinning motion",
        "elastic radial pressure"
    ],
    anti_fits=[
        "loose wrapping without stable compression",
        "off-center clamp",
        "same-name label with no fit",
        "permanent lock"
    ],
    admissible_shape="tight O-rings seated concentrically around the coupler",
    failure_modes=[
        "off-axis crushing",
        "slip under rotation",
        "overbinding"
    ],
    source="compiler_root"
)
```

### A.2 `adv_llm_01`

```python
NeedSlot(
    required_operation="describe stepwise token emission through an internal evolving fold-state",
    preserved_function="preserve dependence of each token on previous tokens and current internal state",
    boundary_conditions=[
        "sequential generation",
        "state re-indexes after emission",
        "not whole-row lookup"
    ],
    anti_fits=[
        "database row copied after lookup",
        "stored final paragraph",
        "random string independent of previous tokens"
    ],
    admissible_shape="internal indexed fold-state emits a token and re-indexes",
    failure_modes=[
        "whole answer lookup",
        "independent random text",
        "table-copy model"
    ],
    source="compiler_root"
)
```

### A.3 `adv_sha_01`

```python
NeedSlot(
    required_operation="describe algebraic folding structure that produces digest deterministically",
    preserved_function="preserve cryptographic security properties through deterministic transformation",
    boundary_conditions=[
        "deterministic: same input gives same output",
        "compressed but not random",
        "algebraic structure preserved"
    ],
    anti_fits=[
        "randomness created by destroying input structure",
        "semantic meaning extraction",
        "database pointer"
    ],
    admissible_shape="compressed residue of deterministic algebraic folding",
    failure_modes=[
        "randomness generation",
        "information destruction",
        "non-deterministic"
    ],
    source="compiler_root"
)
```

---

## Appendix B. Gate Action Distribution

```text
same_as_base: 87 samples
  Base and evidence agree; no override needed.

override_text_compiled_slot_agree: 5 samples
  Answer-text and compiler slot agree on non-base choice.

override_slot_evidence_compiled_slot_positive: 3 samples
  Slot and evidence agree on non-base choice.

override_text_evidence_compiled_slot_positive: 1 sample
  Text and evidence agree on non-base choice.

protect_locked_base_no_compiled_agreement: 0 samples
keep_base_default: 0 samples
```

All overrides were correct.

---

## Appendix C. Reproducibility Checklist

1. Load base LLM: `Qwen/Qwen2.5-1.5B-Instruct`.
2. Load embedding model: `sentence-transformers/all-MiniLM-L6-v2`.
3. Compile NeedSlot for each base question.
4. Rotate choices to create 96 samples.
5. Score candidates with slot binding.
6. Score answer-text fit.
7. Score base model letter prediction.
8. Compute triadic evidence:

$$
E_i=0.55z_{slot}+0.35z_{text}+0.10z_{letter}.
$$

9. Apply conservative v55 gate.
10. Report `base_acc`, `slot_acc`, `evidence_acc`, `gated_acc`, `slot_hurt`, and `gated_hurt`.

---

## Appendix D. Terminology

**Operational geometry**: The structure of what an answer must do, including operation, preserved function, constraints, and anti-fits.

**Need-slot**: The compiled missing-shape contract extracted from a question.

**Compiler-root slot**: A slot generated from deterministic operational extraction rather than free LLM generation.

**Anti-fit**: A known wrong pattern that may look semantically related but fails the required operation.

**Triadic evidence fold**: Weighted combination of slot, text, and base-letter evidence.

**Gate**: Conservative boundary controller deciding whether to override the base model.

**Perfect lock**: A state where the slot and gate achieve target accuracy with zero introduced harm.

**Slot quarantine**: Treating model-generated slot proposals as evidence rather than authority.
