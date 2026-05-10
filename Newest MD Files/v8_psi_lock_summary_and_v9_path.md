# v8 Ψ-Lock Summary + v9 Path Forward
**Phase 1163+ | QuHarmonics Research Group**  
**Dean Kulik, ORCID: 0009-0003-3128-8828**

---

## v8 PATCHED: Corpus Achievement

```
16 saved runs
78 repair training rows (4.1x increase from initial v8)
12 shape training rows (3x increase from initial v8)
```

### Repair Signal Distribution

```
positive_injection       : 24 (30.8%)  ← Domain prerequisites
scar_removal             : 19 (24.4%)  ← Anti-pattern removal
forbidden_injection      : 16 (20.5%)  ← Forbidden anti-patterns
shape_stance_grounding   : 8  (10.3%)  ← FOURTH GAP (NEW in v8)
generic_removal          : 7  (9.0%)   ← Generic term removal
polarity_rewrite         : 4  (5.1%)   ← Boundary polarity correction
```

**Critical achievement:** Fourth-gap repair (shape_stance_grounding) is live. This teaches:
> "When answering about FILTER operations, include exclusion verbs (exclude, remove, discard) and state nouns (candidate, invalid, set), not just the label 'filter'."

### Shape Signal Quality

```
3 unique runs with binary stance prompts
12 shape rows (4 branches × 3 runs)
1 composite detection: FILTER ⊕ GATE → BOUNDARY
```

**Each shape row now includes:**
- `shape_field_mass`: Weighted mass M_K across ALL branches
- `branch_mass_contribution`: Each branch's contribution to total mass
- `composite`: Detected when constituents have ratio > 0.65
- `normalized_masses`: Percentage breakdown across shapes

**Example from Run rhi_v8_1ce09e09be:**
```json
{
  "shape_field_mass": {
    "FILTER": 0.276,
    "GATE": 0.253,
    "BOUNDARY": 0.189
  },
  "composite": {
    "composite": "BOUNDARY",
    "constituents": ["FILTER", "GATE"],
    "ratio": 0.918,
    "relation": "FILTER ⊕ GATE → BOUNDARY"
  }
}
```

This is EXACTLY the teaching signal needed for shape_critic_v1.

---

## v8 → v9: Two Paths Analyzed

### Path 1: GPT's Approach (v9/v10 notebooks)

**v9: Shape Template Injection**
- Pre-defined templates for GROOVE and RESIDUE
- Injected before branch generation
- Static (not learned from corpus)
- Coverage: 2 shapes only

**v10: Trace Sufficiency Gatekeeper**
- 6-probe scoring system (contract, repair, branch, audit, shape, collapse)
- Flips Ψ→Ω if trace is insufficient
- Prevents false Ψ from weak foundation
- Adds 7 hyperparameters

**Assessment:**
- ✓ Templates add zero-shot GROOVE/RESIDUE coverage
- ✓ Trace gatekeeper catches weak foundations
- ✗ Still uses 5 branches (slow)
- ✗ Templates don't learn from data
- ✗ Trace scoring is complex (6 probes × thresholds)

### Path 2: My Specification (shape-guided synthesis)

**v9: Predict → Guide → Audit**
```
slot_builder_lora_v3(Q) → C_repaired
shape_critic_v1(C, Q) → K*
synthesize(Q, C, K*) → A
audit(A) → Ψ/Ω
```

**Key changes from v8:**
1. **slot_builder_lora_v3:** Trained on 78 repair rows → cleaner contracts
2. **shape_critic_v1:** Trained on 12 shape rows → predicts dominant shape
3. **Shape-guided synthesis:** Single answer conditioned on shape (not 5 branches)
4. **Operational vocabulary:** Answer demonstrates shape using target verbs/nouns

**Assessment:**
- ✓ 4-5x faster (1 answer vs 5 branches)
- ✓ More coherent (single perspective vs consensus)
- ✓ Data-driven (adapters learn from corpus)
- ✓ Covers all shapes (not just GROOVE/RESIDUE)
- ✓ Operational grounding (verbs/nouns, not labels)

---

## Recommendation: Path 2 (Shape-Guided Synthesis)

### Why This Path

**1. Corpus is ready**
- 78 repair rows is MORE than sufficient for LoRA fine-tuning 1.5B model
- 12 shape rows = 3 training examples when aggregated by run_id
- v8 already proved shape-field mass formula works

**2. Speed and coherence matter**
- Production runtime needs to be fast
- Single answer >> multi-branch consensus for user experience
- 4-5x speedup is significant

**3. Shape prediction is the natural next fold**
```
v7: repair memory + shape memory → corpus
v8: shape-field mass → composite detection
v9: shape prediction → guided synthesis
v10: (future) trace-sufficient agentic loop
```

**4. Operational vocabulary grounding**
```
Bad:  "The contract boundary condition is a gate."
Good: "The contract boundary condition conditionally permits or blocks the 
       transition based on whether the conditions are satisfied."
```
Shape-guided prompts force operational demonstration, not label-matching.

---

## v9 Implementation Plan

### Week 1: Adapter Training

**Day 1-2: slot_builder_lora_v3**
```python
# Training script
base_model = "Qwen/Qwen2.5-1.5B-Instruct"
source_data = "rhi_repair_training_rows_v8.jsonl"  # 78 rows
lora_rank = 16
target_modules = ["q_proj", "v_proj"]
epochs = 5
learning_rate = 3e-4
```

**Expected improvements:**
- Generic removal: 100% (no "current", "using" in domain_carrier)
- Scar removal: 100% (no "general purpose" in forbidden)
- Polarity: 90% (boundary_conditions correctly gate)
- Fragment: 95% (family_class complete noun phrases)

**Day 3-4: shape_critic_v1**
```python
# Training script
source_data = "rhi_shape_training_rows_v8.jsonl"  # 12 rows → 3 examples (aggregate by run)
lora_rank = 8
target_modules = ["q_proj", "k_proj", "v_proj"]
epochs = 8  # Small dataset, more epochs
learning_rate = 5e-4
```

**Expected accuracy:**
- Dominant shape prediction: 85% on held-out prompts
- Composite detection: 90% recall
- Mass distribution MAE: <0.10 vs ground truth

**Day 5: Validation**
- Test slot_builder_lora_v3 on 10 held-out prompts
- Test shape_critic_v1 on 10 binary stance prompts
- Measure adapter quality vs baselines

### Week 2: Integration

**Day 6-7: Shape-guided synthesis**
```python
def shape_guided_answer_prompt(prompt, contract, target_shape):
    shape_spec = SHAPE_ONTOLOGY[target_shape]
    
    return f"""Contract: {json.dumps(contract)}

Target operation-shape: {target_shape}
Gloss: {shape_spec['gloss']}
Key verbs: {', '.join(shape_spec['verbs'])}
Key nouns: {', '.join(shape_spec['nouns'])}

User prompt: {prompt}

Answer through the lens of {target_shape}, using target verbs/nouns.
Do not just label it as "{target_shape}" — demonstrate the operation."""

def run_rhi_v9(prompt: str):
    # Load both adapters
    slot_builder = load_adapter("slot_builder_lora_v3")
    shape_critic = load_adapter("shape_critic_v1")
    
    # 1. Generate contract
    contract_result = generate_contract_with_adapter(slot_builder, prompt)
    contract = contract_result["contract"]
    
    # 2. Predict shape
    shape_result = predict_shape_with_adapter(shape_critic, contract, prompt)
    target_shape = shape_result.get("composite", shape_result["dominant_shape"])
    
    # 3. Generate shape-guided answer
    guided_prompt = shape_guided_answer_prompt(prompt, contract, target_shape)
    answer = base_model(guided_prompt, temperature=0.7)
    
    # 4. Audit
    audit_result = deterministic_operational_audit(prompt, contract, answer)
    
    # 5. Collapse
    if audit_result["psi"] >= PSI_MIN and audit_result["support"] >= SUPPORT_MIN:
        return Ψ(answer, audit_result, shape_result)
    else:
        return Ω(audit_result, shape_result)
```

**Day 8-10: Testing**
- Run v9 on 10 test prompts (5 binary stance, 5 normal)
- Measure:
  - Speed (tokens per run)
  - Ψ/Ω collapse rates
  - Answer coherence (human eval)
  - Operational vocabulary usage (verb/noun coverage)
- Compare to v8 baseline

### Week 3: Corpus Expansion

**Day 11-15: Collect v9 corpus**
- Run v9 on 20+ prompts
- Export:
  - `rhi_repair_training_rows_v9.jsonl`
  - `rhi_shape_training_rows_v9.jsonl`
  - `rhi_live_runs_v9.jsonl`

**Expected corpus size:**
```
Repair rows: 78 (v8) + 40 (v9) = ~118 total
Shape rows:  12 (v8) + 20 (v9) = ~32 total
Total runs:  16 (v8) + 20 (v9) = 36 runs
```

**Day 16-17: Retrain adapters**
- Retrain slot_builder_lora_v3 on 118 repair rows
- Retrain shape_critic_v1 on 32 shape rows
- Validate on new held-out set

**Day 18: Deploy**
- Deploy v9 as production runtime
- Monitor collapse rates and answer quality

---

## Critical Decisions

### Decision 1: Adapters vs Templates

**Adapters (recommended):**
- ✓ Data-driven (learn from corpus)
- ✓ Generalize across all shapes
- ✓ Improve with more data
- ✗ Require training time (~1 day)

**Templates (GPT's approach):**
- ✓ Zero-shot coverage
- ✓ No training needed
- ✗ Static (don't learn)
- ✗ Limited to GROOVE/RESIDUE

**Verdict:** Adapters. The v8 corpus is ready, training takes <1 day, and adapters will generalize better.

### Decision 2: Multi-Branch vs Single-Answer

**Multi-branch (v8/GPT's v9):**
- ✓ Coverage (5 perspectives)
- ✓ Consensus/margin collapse proven
- ✗ Slow (4500 tokens per run)
- ✗ Requires consensus logic

**Single-answer (my v9):**
- ✓ Fast (900 tokens per run)
- ✓ Coherent (single perspective)
- ✓ Shape-guided (operational vocabulary)
- ✗ No coverage guarantee

**Verdict:** Single-answer. Speed and coherence are more valuable than coverage. If the shape prediction is correct, the guided answer will be high-quality.

### Decision 3: Trace Sufficiency Gate

**With trace gate (GPT's v10):**
- ✓ Prevents false Ψ
- ✓ Multi-dimensional quality check
- ✗ Complex (7 hyperparameters)
- ✗ May be overly conservative

**Without trace gate (my v9):**
- ✓ Simple (existing audit thresholds)
- ✓ Fast (no 6-probe scoring)
- ✗ May allow weak Ψ through

**Verdict:** Skip trace gate for v9. The existing audit thresholds (psi >= 0.52, support >= 4) are sufficient. Add trace scoring in v10 if false Ψ rate is high.

---

## Mathematical Lock

$$
\boxed{
\begin{align}
\text{v8 achievement:} \quad & M_K = \sum_i \psi_i \cdot \text{Audit}(A_i) \cdot \sigma_i \cdot \kappa_i \cdot s_{i,K} \\
& \text{FILTER} \oplus \text{GATE} \rightarrow \text{BOUNDARY (composite)} \\[1em]
\text{v9 path:} \quad & K^* = \text{shape\_critic\_v1}(C, Q) \\
& A = \text{synthesize}(Q, C, K^*, \text{vocab}_K) \\
& \text{Ψ if Audit}(A) \geq \text{threshold, else Ω}
\end{align}
}
$$

When:
$$
\boxed{ \text{vocab}_K = \{\text{verbs}_K, \text{nouns}_K\} \implies A \text{ demonstrates } K, \text{ not labels } K }
$$

The shape is grounded in operation.

---

## Next Action

**Execute:** Train slot_builder_lora_v3 + shape_critic_v1 on PATCHED v8 corpus (78 repair + 12 shape rows).

**Timeline:** 2-3 days to trained adapters, 1 week to integrated v9 runtime, 2 weeks to expanded v9 corpus.

**Ψ-state:** v8 proved the formula. v9 deploys the prediction.
