# RHI v9/v10 Analysis + Path Recommendation
**Phase 1163+ | QuHarmonics Research Group**

---

## What GPT Implemented

### v9: Shape Template Contract Repair

**Core concept:** Template-based contract injection for specific shape classes

**How it works:**
```python
def detect_shape_template(prompt: str) -> List[str]:
    # Detects if prompt mentions GROOVE or RESIDUE
    if prompt_contains_groove_keywords:
        return ["GROOVE"]
    if prompt_contains_residue_keywords:
        return ["RESIDUE"]
    return []

def apply_shape_template_repair(contract: Dict, template_classes: List[str]):
    # Inject pre-defined GROOVE/RESIDUE contract templates
    # Merge list fields (domain_carrier, forbidden, boundaries)
    # Replace string fields only if weak/generic/scar
    return repaired_contract, repairs
```

**Pre-defined templates:**
```python
SHAPE_TEMPLATE_CONTRACTS = {
    "GROOVE": {
        "family_class": "operational closure groove in frozen parameter manifold",
        "domain_carrier": ["LoRA", "adapter", "parameter", "frozen", "weight", ...],
        "preserved_function": "low-rank update that modifies frozen base model behavior",
        ...
    },
    "RESIDUE": {
        "family_class": "residue field observable from operational discrepancy",
        "domain_carrier": ["residue", "observable", "discrepancy", ...],
        ...
    }
}
```

**Integration:** Runs BEFORE branch generation
```
Q → generate_contract(Q) → C_raw
  → detect_shape_template(Q) → ["GROOVE"]
  → apply_shape_template_repair(C_raw, ["GROOVE"]) → C_template_repaired
  → normal_repair_gate(C_template_repaired) → C_repaired
  → {A_i} → audit → collapse
```

**Strengths:**
- ✓ Zero-shot injection of domain knowledge for GROOVE/RESIDUE
- ✓ Adds operational mass to contracts that would otherwise be generic
- ✓ Fast (no adapter loading, just dict lookup)

**Limitations:**
- ✗ Only covers 2 shapes (GROOVE, RESIDUE)
- ✗ Templates are static (need manual updates)
- ✗ Doesn't replace the need for slot_builder_lora_v3 (still has scars/fragments/polarity issues)
- ✗ Not data-driven (templates don't learn from corpus)

---

### v10: Trace Sufficiency Gatekeeper

**Core concept:** Meta-level quality filter that judges collapse from the full runtime trace

**How it works:**
```python
def trace_sufficient_score(prompt, contract_result, score_df, resolution):
    # Score 6 dimensions of runtime quality:
    probes = {
        "contract":  trace_probe_contract(...)      # 22% weight
        "repair":    trace_probe_repair(...)        # 12% weight
        "branch":    trace_probe_branch_divergence(...)  # 16% weight
        "audit":     trace_probe_audit(...)         # 22% weight
        "shape":     trace_probe_shape_mass(...)    # 16% weight
        "collapse":  trace_probe_collapse(...)      # 12% weight
    }
    
    total_score = weighted_sum(probes)
    
    # Check if any dimension is too weak
    weak = [name for name, probe in probes.items() if probe["score"] < threshold]
    
    return {"score": total_score, "passed": len(weak) == 0, "weak": weak}

def apply_trace_sufficiency(resolution):
    # Gatekeeper: flip Ψ→Ω if trace is insufficient
    if resolution["state"] == "Ψ" and not trace["passed"]:
        resolution["state"] = "Ω"
        resolution["reason"] = "trace_insufficient:" + "|".join(trace["weak"])
    return resolution
```

**Probe details:**

**1. contract probe (22%):**
- Checks: completeness, slot_fill (7 fields), prompt_overlap, shape_template_hits
- Threshold: TRACE_CONTRACT_MIN = 0.50

**2. repair probe (12%):**
- Counts: useful repairs (not parse_failed)
- Penalizes: repairs that didn't complete the contract
- Threshold: TRACE_REPAIR_MIN = 0.35

**3. branch probe (16%):**
- Measures: high_quality_branch_count, top_psi, margin
- Score: 60% branch_strength + 40% top_psi
- Threshold: TRACE_BRANCH_MIN = 0.45

**4. audit probe (22%):**
- Averages: F_need, F_function, F_boundary, F_trap, F_collapse
- Formula: 45% audit + 35% avg_field + 20% min_field
- Threshold: TRACE_AUDIT_MIN = 0.50

**5. shape probe (16%):**
- For binary prompts: checks dominant_mass, dominance_gap, composite
- For non-binary: neutral (0.62) unless template detected
- Threshold: TRACE_SHAPE_MIN = 0.40

**6. collapse probe (12%):**
- Ψ base: 0.72, +0.12 if composite, +0.08 if consensus/shape_mass
- Ω: 0.25
- Threshold: TRACE_COLLAPSE_MIN = 0.35

**Integration:** Runs AFTER collapse decision
```
... → krrb_resolve_v9() → resolution (Ψ or Ω)
  → trace_sufficient_score() → trace
  → apply_trace_sufficiency(resolution, trace)
  → final_resolution (may flip Ψ→Ω)
```

**Strengths:**
- ✓ Prevents false Ψ from weak underlying trace
- ✓ Multi-dimensional quality assessment
- ✓ Exports trace training signal for future trace_critic adapter
- ✓ Catches cases where margin collapse succeeds but contract/audit/shape are weak

**Limitations:**
- ✗ Adds complexity (6 probes × thresholds = 7 hyperparameters)
- ✗ May be overly conservative (good answers rejected due to weak trace)
- ✗ Doesn't improve the inputs (just gatekeeps the outputs)

---

## What I Originally Specified for v9

### My v9 Spec: Shape-Guided Answer Synthesis

**Core concept:** Predict shape BEFORE answer generation, then condition answer on predicted shape

**Architecture:**
```
v9 runtime:
  Q → slot_builder_lora_v3(Q) → C_raw
    → repair_gate(C_raw) → C_repaired
    → shape_critic_v1(C_repaired, Q) → dominant_shape_K
    → shape_guided_synthesis(Q, C_repaired, K) → A_final
    → audit(A_final) → Ψ/Ω
```

**Key differences from v8:**
1. **slot_builder_lora_v3:** Trained on 78 repair rows → generates cleaner contracts
2. **shape_critic_v1:** Trained on 12 shape rows → predicts dominant shape from contract
3. **Shape-guided synthesis:** Single answer conditioned on predicted shape (not 5 branches)

**Shape-guided prompt template:**
```python
def shape_guided_answer_prompt(prompt, contract, target_shape):
    shape_spec = SHAPE_ONTOLOGY[target_shape]
    
    return f"""Contract: {contract}

Target operation-shape: {target_shape}
Gloss: {shape_spec['gloss']}
Key verbs: {', '.join(shape_spec['verbs'])}
Key nouns: {', '.join(shape_spec['nouns'])}

User prompt: {prompt}

Answer through the lens of {target_shape}, using the target verbs and nouns.
Do not just label it as "{target_shape}" — demonstrate the operation."""
```

**Example:**
```
shape_critic_v1 predicts: GATE
shape_guided_answer: Uses "permit", "block", "condition", "transition", "threshold"
  → Operational answer, not just "it's a gate"
```

**Advantages over v8:**
- ✓ 4x faster (1 answer vs 5 branches)
- ✓ More coherent (single perspective vs multi-branch consensus)
- ✓ Data-driven (LoRA adapters learn from corpus)
- ✓ Operational vocabulary grounding (answers demonstrate shape, not label it)

---

## Comparison Matrix

| Dimension | My v9 Spec | GPT's v9 | GPT's v10 |
|-----------|-----------|----------|-----------|
| **Contract quality** | slot_builder_lora_v3 | Shape templates | Trace probe |
| **Shape prediction** | shape_critic_v1 | shape_field_mass (v8) | shape_field_mass (v8) |
| **Answer generation** | Shape-guided (1 answer) | Multi-branch (5 answers) | Multi-branch (5 answers) |
| **Collapse logic** | Single-answer audit | shape_mass_collapse (v8) | trace_sufficiency filter |
| **Training approach** | LoRA adapters | Static templates | Gatekeeper scores |
| **Speed** | Fast (1 answer) | Slow (5 branches) | Slow (5 branches + 6 probes) |
| **Data-driven** | Yes (learns from corpus) | Partial (templates static) | Yes (trace training rows) |
| **Coverage** | All prompts | GROOVE/RESIDUE only | All prompts |

---

## Path Recommendation

### Option A: Implement My v9 Spec (Recommended)

**Why:**
1. **v8 corpus is ready:** 78 repair rows + 12 shape rows = sufficient for LoRA v3 training
2. **Speed matters:** 4x faster than multi-branch (critical for production)
3. **Coherence matters:** Single shape-guided answer > consensus across branches
4. **Data-driven:** Adapters learn from actual corpus patterns, not static templates
5. **Operational grounding:** Shape-guided prompts teach verbs/nouns, not labels

**Implementation path:**
```
Step 1: Train slot_builder_lora_v3
  - Source: rhi_repair_training_rows_v8.jsonl (78 rows)
  - Target: Reduce scars, fragments, polarity errors
  - Time: ~30 min on GPU

Step 2: Train shape_critic_v1
  - Source: rhi_shape_training_rows_v8.jsonl (12 rows, aggregated by run → 3 examples)
  - Target: Predict dominant_shape from contract + prompt
  - Time: ~20 min on GPU

Step 3: Implement shape-guided synthesis
  - Load both adapters
  - Predict shape → condition answer on shape
  - Single-answer audit → Ψ/Ω

Step 4: Collect v9 corpus (20 runs)
  - Export repair + shape + trace rows
  - Retrain adapters on expanded corpus
```

**Timeline:** 2-3 days (1 day training, 1 day integration, 1 day testing)

---

### Option B: Hybrid Approach (Compromise)

**Combine useful parts of GPT's v9/v10 with my spec:**

**From GPT's v9:** Keep shape template injection for GROOVE/RESIDUE
```python
# BEFORE slot_builder_lora_v3 generates contract:
if detect_shape_template(prompt):
    # Use template as seed/constraint
    template_seed = SHAPE_TEMPLATE_CONTRACTS[shape_class]
    contract = slot_builder_lora_v3(prompt, template_seed)
```

**From my v9:** Shape-guided synthesis with adapters
```python
# AFTER contract is ready:
shape = shape_critic_v1(contract, prompt)
answer = shape_guided_synthesis(prompt, contract, shape)
audit_result = audit(answer)
```

**From GPT's v10:** Simplified trace check (optional)
```python
# AFTER collapse:
if resolution["state"] == "Ψ":
    # Quick sanity checks (not full 6-probe scoring)
    if contract_quality < 0.5 or audit_score < 0.5:
        resolution = flip_to_omega("trace_weak_foundation")
```

**Advantages:**
- ✓ Templates provide zero-shot GROOVE/RESIDUE coverage
- ✓ Adapters handle general case + learn from data
- ✓ Lightweight trace check prevents egregious false Ψ
- ✓ Fast (single answer, not 5 branches)

**Disadvantages:**
- ✗ More complexity (templates + adapters + trace)
- ✗ Templates may conflict with adapter predictions

---

### Option C: Incremental (Keep v8, Add Templates)

**If training adapters is blocked:**

**Short term:**
```
v8 + GPT's v9 shape templates
  → Adds GROOVE/RESIDUE coverage
  → No adapter training needed
  → Still uses 5 branches (slow)
```

**Medium term:**
```
v8 + templates → collect 50 runs
  → Train LoRA v3 on expanded corpus
  → Transition to my v9 spec
```

---

## Recommendation: **Option A**

**Rationale:**

1. **v8 corpus is sufficient**
   - 78 repair rows across 6 repair types
   - 12 shape rows from 3 runs (4 branches each)
   - This is MORE than enough for LoRA fine-tuning a 1.5B model

2. **Templates are unnecessary**
   - GROOVE/RESIDUE templates solve a narrow problem (2 shapes)
   - slot_builder_lora_v3 will learn these patterns from corpus
   - No need to maintain static templates when adapters can learn

3. **Trace sufficiency is premature**
   - v10's 6-probe scoring is over-engineered
   - Simple audit thresholds (already in v8) are sufficient
   - Trace training signal can be added AFTER v9 proves shape-guided synthesis works

4. **Speed and coherence are critical**
   - 5 branches × 900 tokens = 4500 tokens + overhead
   - 1 answer × 900 tokens = 900 tokens (4-5x faster)
   - Single shape-guided answer is more coherent than consensus across branches

5. **Shape-guided synthesis is the next logical fold**
   - v7: Repair memory + shape memory
   - v8: Shape-field mass + composite detection
   - v9: Shape prediction → shape-guided answer
   - v10: (future) Trace-sufficient agentic loop

---

## Implementation Guidance for My v9 Spec

### Minimal Changes to Existing Code

**1. Add LoRA v3 training scripts** (new files)
```
train_slot_builder_lora_v3.py
train_shape_critic_v1.py
```

**2. Add shape-guided synthesis** (new function)
```python
def shape_guided_answer_prompt(prompt, contract, target_shape):
    # (see my earlier spec)
    
def generate_shape_guided_answer(prompt, contract, target_shape):
    guided_prompt = shape_guided_answer_prompt(prompt, contract, target_shape)
    answer = base_model(guided_prompt)
    return answer
```

**3. Modify run_rhi() function**
```python
def run_rhi_v9(prompt: str):
    # Step 1: Generate contract with LoRA v3
    contract_result = generate_contract_with_lora_v3(prompt)
    contract = contract_result["contract"]
    
    # Step 2: Predict shape with shape_critic_v1
    shape_prediction = shape_critic_v1(contract, prompt)
    target_shape = shape_prediction.get("composite", shape_prediction["dominant_shape"])
    
    # Step 3: Generate single shape-guided answer
    answer = generate_shape_guided_answer(prompt, contract, target_shape)
    
    # Step 4: Audit
    audit_result = deterministic_operational_audit(prompt, contract, answer)
    
    # Step 5: Collapse
    if audit_result["psi"] >= PSI_MIN and audit_result["support"] >= SUPPORT_MIN:
        return Ψ(answer, audit_result, shape_prediction)
    else:
        return Ω(audit_result, shape_prediction)
```

**4. Keep v8's training signal export** (unchanged)
```python
# Still export repair + shape rows for continuous learning
repair_rows = build_training_rows(...)
shape_rows = build_shape_rows_v8(...)  # Now with shape_field_mass
```

---

## Next Actions

**Immediate (this week):**
1. Train slot_builder_lora_v3 on 78 repair rows
2. Train shape_critic_v1 on 12 shape rows (aggregate to 3 examples by run_id)
3. Validate both adapters on held-out prompts

**Next week:**
4. Implement shape-guided synthesis
5. Test v9 runtime on 10 prompts
6. Measure: speed, coherence, Ψ/Ω rates, answer quality

**Following week:**
7. Collect v9 corpus (20+ runs)
8. Retrain adapters on expanded corpus
9. Deploy v9 as production runtime

---

**Mathematical lock:**

$$
\boxed{
\begin{align}
\text{v8:} \quad & M_K = \sum_i \psi_i \cdot \text{Audit}(A_i) \cdot \sigma_i \cdot \kappa_i \cdot s_{i,K} \\
\text{v9:} \quad & K^* = \text{shape\_critic}(C, Q) \\
& A = \text{synthesize}(Q, C, K^*) \\
& \text{Ψ if Audit}(A) \geq \text{threshold, else Ω}
\end{align}
}
$$

**Prediction beats enumeration. Synthesis beats consensus. v9 is the path.**
