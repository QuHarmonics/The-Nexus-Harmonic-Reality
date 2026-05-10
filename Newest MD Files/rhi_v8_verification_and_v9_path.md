# RHI v8 Verification + v9 Path
**Phase 1163+ | QuHarmonics Research Group**  
**Dean Kulik, ORCID: 0009-0003-3128-8828**

---

## v8 Ψ-Lock: Composite Shape Collapse Confirmed

### Runtime Evidence

**Run 5** (rhi_v8_1ce09e09be):
```
Prompt: "Is the contract boundary condition a filter or a gate? Defend one operational reading."
State: Ψ (composite_shape_collapse)

Shape-field mass:
  FILTER: 0.276
  GATE:   0.253
  BOUNDARY: 0.189

Composite detected: BOUNDARY
Constituents: FILTER ⊕ GATE
Ratio: 0.918 (constituents nearly equal mass)
Normalized: FILTER=38.4%, GATE=35.3%
Relation: "FILTER ⊕ GATE → BOUNDARY"
```

**What this proves:**
1. The formula $M_K = \sum_i \psi_i \cdot \text{Audit}(A_i) \cdot \sigma_i \cdot \kappa_i \cdot s_{i,K}$ works
2. When FILTER and GATE both carry significant mass (>0.25) and are close (ratio > 0.65), they resolve to BOUNDARY
3. Individual branches voted differently (skeptical→BOUNDARY, operational→FILTER, residue_aware→FILTER, contract_fit→BOUNDARY)
4. But the **field mass** revealed the composite structure

### Training Signal Quality

**Shape training rows (4 total)** now include:
```json
{
  "shape_field_mass": {
    "FILTER": 0.276,
    "GATE": 0.253,
    "BOUNDARY": 0.189
  },
  "branch_mass_contribution": {
    "FILTER": 0.089,  // this branch's contribution to FILTER mass
    "GATE": 0.064,
    "BOUNDARY": 0.020
  },
  "composite": {
    "composite": "BOUNDARY",
    "constituents": ["FILTER", "GATE"],
    "ratio": 0.918,
    "relation": "FILTER ⊕ GATE → BOUNDARY"
  }
}
```

**This teaches shape_critic_v1:**
- Shape is a field property, not a branch property
- Branches contribute mass to multiple shapes
- Composites emerge from field structure, not label matching
- FILTER and GATE are dual aspects of BOUNDARY (interface control)

### v8 Corpus Summary

```
5 saved runs (fresh batch)
19 repair training rows
4 shape training rows

Repair distribution:
  scar_removal         : 6 (31.6%)
  positive_injection   : 6 (31.6%)
  forbidden_injection  : 4 (21.1%)
  generic_removal      : 2 (10.5%)
  polarity_rewrite     : 1 (5.3%)

Run states:
  Ψ collapse                  : 2
  Ψ consensus_collapse        : 1
  Ψ composite_shape_collapse  : 1 ← NEW in v8
  Ω contract_incomplete       : 1
```

---

## v8 → v9: Shape-Guided Answer Synthesis

### Current Flow

```text
v8 runtime:
  Q → slot_builder_lora_v2(Q) → C_raw
    → repair_gate(C_raw) → C_repaired
    → base_model({branch_i}) → {A_i}
    → deterministic_audit({A_i}) → {ψ_i, audit_i}
    → shape_stance({A_i}) → {s_{i,K}}
    → shape_field_mass → M_K
    → composite_detection → Ψ/Ω
```

**Gap:** Branches are generated independently, then evaluated. No shape guidance during generation.

### v9 Runtime

```text
v9 runtime:
  Q → slot_builder_lora_v3(Q) → C_raw
    → repair_gate(C_raw) → C_repaired
    → shape_critic_v1(C_repaired, Q) → dominant_shape_K
    → shape_guided_synthesis({A_i}, K) → A_final
    → audit(A_final) → Ψ/Ω
```

**Key changes:**
1. **slot_builder_lora_v3** trained on repair rows → fewer scars, better polarity
2. **shape_critic_v1** trained on shape rows → predicts dominant shape from contract
3. **shape_guided_synthesis** → generate answer conditioned on target shape

### Shape-Guided Synthesis

**Prompt template for v9:**
```python
def shape_guided_answer_prompt(prompt: str, contract: Dict, target_shape: str) -> str:
    shape_spec = SHAPE_ONTOLOGY[target_shape]
    
    return f"""Contract: {json.dumps(contract)}

Target operation-shape: {target_shape}
Gloss: {shape_spec['gloss']}

Key verbs: {', '.join(shape_spec['verbs'])}
Key nouns: {', '.join(shape_spec['nouns'])}

User prompt: {prompt}

Answer the prompt through the lens of {target_shape}, using the target verbs and nouns to ground the operational semantics. Do not just label it as "{target_shape}" — demonstrate the operation."""
```

**Example:**

If shape_critic_v1 predicts GATE for "Is X a filter or a gate?":
```
Target operation-shape: GATE
Gloss: conditionally permits or blocks transition across a boundary
Key verbs: allow, permit, open, close, blocks, transition, cross
Key nouns: condition, permission, transition, threshold, entry, passage, interface

Answer: The contract boundary condition is a **gate** because it **conditionally permits** or **blocks** the **transition** based on whether the **conditions** are satisfied. A gate operates on the **permission** level: when the boundary **conditions** hold, the **passage** is **allowed**; otherwise, the **transition** is **blocked** at the **threshold**.
```

This produces answers with operational vocabulary, not just labels.

---

## LoRA v3 Training Strategy

### Corpus Split

```
slot_builder_lora_v3:
  Source: rhi_repair_training_rows_v8.jsonl (19 rows)
  Target: Reduce scars, fragments, polarity inversions in contract generation
  Base: Qwen/Qwen2.5-1.5B-Instruct
  Modules: q_proj, v_proj (attention repair)
  Rank: 16-32
  Epochs: 3-5
  
shape_critic_v1:
  Source: rhi_shape_training_rows_v8.jsonl (4 rows)
  Target: Predict dominant shape from contract + prompt
  Base: Qwen/Qwen2.5-1.5B-Instruct
  Modules: q_proj, k_proj, v_proj (shape discrimination)
  Rank: 8-16
  Epochs: 5-8 (small dataset, higher epochs)
```

### Training Row Format

**Repair row → Training example:**
```python
{
  "messages": [
    {"role": "system", "content": "You are the Nexus Slot Constructor."},
    {"role": "user", "content": build_slot_user_prompt(prompt)},
    {"role": "assistant", "content": json.dumps(good_contract)}
  ]
}
```

**Shape row → Training example:**
```python
{
  "messages": [
    {"role": "system", "content": "You are the Nexus Shape Critic. Predict the dominant operation-shape from the contract and prompt."},
    {"role": "user", "content": f"Contract: {contract}\nPrompt: {prompt}"},
    {"role": "assistant", "content": json.dumps({
      "dominant_shape": "BOUNDARY",
      "dominant_mass": 0.276,
      "composite": {
        "relation": "FILTER ⊕ GATE → BOUNDARY",
        "constituents": ["FILTER", "GATE"]
      }
    })}
  ]
}
```

### Expected Improvements

**slot_builder_lora_v3:**
- Generic term removal: "current" → structured concepts (100% reduction target)
- Scar leakage: "general purpose" → forbidden anti-patterns (100% reduction target)
- Polarity inversion: boundary_conditions correctly gate tool action (90% reduction target)
- Fragment completion: family_class always complete noun phrase (95% target)

**shape_critic_v1:**
- Predict dominant shape from contract alone (no branches needed)
- Detect composite structure (FILTER ⊕ GATE → BOUNDARY)
- Output shape-field mass distribution for confidence
- Accuracy target: 85% on held-out binary stance prompts

---

## v9 Runtime Architecture

### Three-Stage Flow

**Stage 1: Contract Construction**
```python
C_raw = slot_builder_lora_v3(Q)
C_repaired = repair_gate(C_raw)  # Still needed for edge cases
```

**Stage 2: Shape Prediction**
```python
shape_result = shape_critic_v1(C_repaired, Q)
# Returns: {
#   "dominant_shape": "GATE",
#   "dominant_mass": 0.42,
#   "composite": null,
#   "confidence": 0.85
# }
```

**Stage 3: Shape-Guided Synthesis**
```python
if shape_result["composite"]:
    # Generate answer for composite (e.g., BOUNDARY from FILTER⊕GATE)
    target_shape = shape_result["composite"]
else:
    target_shape = shape_result["dominant_shape"]

A = base_model(
    prompt=shape_guided_answer_prompt(Q, C_repaired, target_shape),
    temperature=0.7
)

audit_result = deterministic_operational_audit(Q, C_repaired, A)
if audit_result["psi"] >= PSI_MIN and audit_result["support"] >= SUPPORT_MIN:
    return Ψ(A)
else:
    return Ω(audit_result)
```

### Collapse Logic

v9 **removes** branch enumeration (direct/operational/skeptical/contract_fit/residue_aware).

Instead:
1. Predict target shape
2. Generate one answer conditioned on that shape
3. Audit that answer
4. Ψ if audit passes, Ω if not

**Single-answer collapse is faster:**
- v8: 5 branches × ~900 tokens = 4500 tokens + audit overhead
- v9: 1 answer × ~900 tokens = 900 tokens + shape prediction (~200 tokens)
- Speedup: ~4x reduction in generation tokens

**Single-answer collapse is more coherent:**
- v8: Branches can contradict each other, need consensus/margin gates
- v9: One answer, aligned to predicted shape, either passes or fails

---

## v9 Testing Plan

### Phase 1: Adapter Training
1. Build training datasets from v8 corpus
2. Train slot_builder_lora_v3 (19 repair rows, 3-5 epochs)
3. Train shape_critic_v1 (4 shape rows, 5-8 epochs)
4. Validate both adapters on held-out prompts

### Phase 2: Integration
1. Load both adapters in v9 runtime
2. Test on 10 prompts (5 binary stance, 5 normal)
3. Measure:
   - Contract quality (scar rate, fragment rate, polarity correctness)
   - Shape prediction accuracy
   - Answer audit scores
   - Ψ/Ω collapse rates

### Phase 3: Corpus Expansion
1. Collect 20+ more runs with v9 runtime
2. Export repair + shape rows
3. Retrain adapters on expanded corpus
4. Iterate

---

## Expected v9 Corpus (After 20 Runs)

```
Repair rows:  19 (v8) + 30 (v9) = ~49 total
Shape rows:    4 (v8) + 15 (v9) = ~19 total
Total runs:    5 (v8) + 20 (v9) = 25 runs
```

**Breakdown by prompt type:**
- Binary stance (filter/gate, lock/contract, etc.): 8 runs → 32 shape rows
- Normal operational: 12 runs → minimal shape rows
- Composite triggers: 5 runs → 20 shape rows (FILTER⊕GATE, others)

---

## Critical Observations

### What v8 Proved

1. **Shape-field mass formula works**
   - $M_K = \sum_i \psi_i \cdot \text{Audit}(A_i) \cdot \sigma_i \cdot \kappa_i \cdot s_{i,K}$
   - Correctly identified FILTER + GATE → BOUNDARY composite

2. **Composite detection works**
   - Ratio threshold (0.65) correctly identified near-equal constituents
   - Mass threshold (0.25) prevented spurious composites
   - Relation capture ("FILTER ⊕ GATE → BOUNDARY") ready for training

3. **Branch contributions vary**
   - Same prompt → different branches contribute to different shapes
   - Field mass aggregates across branches → reveals true structure
   - Individual branch classification (v7) was incomplete

### What v9 Will Prove

1. **Shape can be predicted before answer generation**
   - shape_critic_v1(contract, prompt) → dominant_shape
   - This enables shape-guided synthesis

2. **Shape-guided answers have better operational fit**
   - Conditioned on target shape → use correct verbs/nouns
   - Not just label-matching ("it's a gate") but operation-demonstrating

3. **Single-answer collapse is sufficient**
   - No need for 5 branches + consensus gates
   - Shape prediction + audit → Ψ/Ω decision

---

## v9 Implementation Checklist

### Code Changes
- [ ] `slot_builder_lora_v3` training script
- [ ] `shape_critic_v1` training script
- [ ] `shape_guided_answer_prompt()` function
- [ ] `load_dual_adapters()` (slot + shape)
- [ ] `run_rhi_v9()` with single-answer flow
- [ ] Update collapse logic (remove branch enumeration)

### Config Updates
- [ ] `SLOT_ADAPTER_DIR_V3`
- [ ] `SHAPE_CRITIC_ADAPTER_DIR_V1`
- [ ] `SHAPE_GUIDED_TEMPERATURE = 0.7`
- [ ] Remove `N_BRANCHES`, `BRANCH_STYLES`

### Output Files
- [ ] `rhi_live_runs_v9.jsonl`
- [ ] `rhi_repair_training_rows_v9.jsonl`
- [ ] `rhi_shape_training_rows_v9.jsonl`
- [ ] `rhi_live_runtime_v9_manifest.json`

---

## Ψ-Convergence Path

```
v7 = repair memory + shape memory + collapse memory
v8 = v7 + shape-field mass + composite detection
v9 = v8 + shape prediction + shape-guided synthesis

Target:
  slot_builder_lora_v3: scar-free, fragment-free, polarity-correct contracts
  shape_critic_v1: contract → dominant shape (composite-aware)
  shape-guided synthesis: answer ← shape operational vocabulary
```

**Mathematical lock:**

$$
\boxed{
\begin{align}
\text{v8:} \quad & M_K = \sum_i \psi_i \cdot \text{Audit}(A_i) \cdot \sigma_i \cdot \kappa_i \cdot s_{i,K} \\
\text{v9:} \quad & A = \text{synthesize}(Q, C, \arg\max_K M_K) \\
\text{Result:} \quad & \text{Ψ if } \text{Audit}(A) \geq \text{threshold, else Ω}
\end{align}
}
$$

When:
$$
\boxed{ M_{\text{FILTER}} \approx M_{\text{GATE}} \implies \text{BOUNDARY} \implies A_{\text{BOUNDARY}} }
$$

The interface is named, the operation is grounded, the answer demonstrates the shape.

---

**Next fold: Train slot_builder_lora_v3 + shape_critic_v1, deploy v9 runtime.**
