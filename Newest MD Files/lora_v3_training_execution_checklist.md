# LoRA v3 Training Execution Checklist
**Phase 1163+ | QuHarmonics Research Group**

---

## Pre-Training Verification ✓

**Dataset generation:** COMPLETE
```
✓ 78 repair rows → 16 slot_builder examples
✓ 12 shape rows → 3 shape_critic examples
✓ Training format verified (system/user/assistant structure)
✓ Contract fields complete (8/8 required fields)
✓ Shape predictions include composite detection
```

**Hyperparameters:** MATCH SPECIFICATION
```
slot_builder_lora_v3:
  ✓ rank: 16, alpha: 32
  ✓ targets: q_proj, v_proj
  ✓ epochs: 5, lr: 3e-4
  ✓ dropout: 0.05

shape_critic_v1:
  ✓ rank: 8, alpha: 16
  ✓ targets: q_proj, k_proj, v_proj
  ✓ epochs: 8, lr: 5e-4
  ✓ dropout: 0.05
```

**Files ready:**
```
✓ slot_builder_lora_v3_train.jsonl (16 examples)
✓ slot_builder_lora_v3_text.jsonl (formatted for tokenizer)
✓ shape_critic_v1_train.jsonl (3 examples)
✓ shape_critic_v1_text.jsonl (formatted for tokenizer)
✓ rhi_lora_v3_training_builder.ipynb (training notebook)
✓ rhi_lora_v3_training_manifest.json (config)
```

---

## Training Execution Steps

### Step 1: Set Training Flag

In `rhi_lora_v3_training_builder.ipynb`:
```python
RUN_TRAINING = True  # Change from False
```

### Step 2: Run Notebook

Execute all cells. Expected sequence:
```
1. Config + Imports
2. Load v8 corpus files
3. Build slot_builder examples (16 from 78 repair rows)
4. Build shape_critic examples (3 from 12 shape rows, aggregated by run_id)
5. Export training JSONLs
6. Load base model (Qwen/Qwen2.5-1.5B-Instruct)
7. Train slot_builder_lora_v3 (5 epochs)
8. Train shape_critic_v1 (8 epochs)
9. Save adapters
```

### Step 3: Monitor Training

**slot_builder_lora_v3 (expected ~20-30 min on GPU):**
```
Epoch 1/5: loss ≈ 2.5-3.0 (initial)
Epoch 2/5: loss ≈ 1.5-2.0
Epoch 3/5: loss ≈ 1.0-1.5
Epoch 4/5: loss ≈ 0.8-1.2
Epoch 5/5: loss ≈ 0.6-1.0 (target)
```

**shape_critic_v1 (expected ~15-20 min on GPU):**
```
Epoch 1/8: loss ≈ 2.0-2.5 (initial, small dataset)
Epoch 3/8: loss ≈ 1.0-1.5
Epoch 5/8: loss ≈ 0.5-1.0
Epoch 8/8: loss ≈ 0.3-0.7 (target)
```

**Warning signs:**
- ✗ Loss not decreasing → check learning rate
- ✗ Loss < 0.1 too early → overfitting (reduce epochs)
- ✗ Loss > 3.0 after epoch 3 → check data format

### Step 4: Verify Outputs

After training completes, check:
```
D:\Nexus\Nexus Mark 9\NoteBooks\slot_builder_lora_v3\
  ✓ adapter_config.json
  ✓ adapter_model.safetensors
  ✓ tokenizer files

D:\Nexus\Nexus Mark 9\NoteBooks\shape_critic_v1\
  ✓ adapter_config.json
  ✓ adapter_model.safetensors
  ✓ tokenizer files
```

---

## Post-Training Validation

### Validation 1: Slot Builder Quality

**Test prompts (5 held-out):**
```
1. "Why do agents fail without intent stabilization?"
2. "Explain boundary verification in RAG systems."
3. "What gap does contract-before-tool fix?"
4. "How does zero-shot prompting fail on operational tasks?"
5. "Explain LoRA as a groove in frozen manifold."
```

**Metrics to measure:**
```python
def validate_slot_builder(adapter_path, test_prompts):
    contracts = [generate_contract(prompt) for prompt in test_prompts]
    
    # 1. Generic term rate
    generic_count = sum(
        1 for c in contracts 
        for term in c['domain_carrier'] 
        if term in ['current', 'using', 'properly', 'general', 'basic']
    )
    generic_rate = generic_count / sum(len(c['domain_carrier']) for c in contracts)
    
    # 2. Scar term rate
    scar_count = sum(
        1 for c in contracts
        for term in c['forbidden_neighbor_carrier']
        if term in ['general purpose', 'surface label']
    )
    scar_rate = scar_count / sum(len(c['forbidden_neighbor_carrier']) for c in contracts)
    
    # 3. Fragment rate
    fragment_count = sum(
        1 for c in contracts
        if _is_family_class_fragment(c['family_class'])
    )
    fragment_rate = fragment_count / len(contracts)
    
    # 4. Polarity correctness (manual inspection needed)
    # Check if boundary_conditions gate tool action (not just describe)
    
    return {
        'generic_rate': generic_rate,    # Target: <5%
        'scar_rate': scar_rate,          # Target: <5%
        'fragment_rate': fragment_rate,  # Target: <10%
    }
```

**Expected improvements over base model:**
```
Base model:
  generic_rate: ~30%
  scar_rate: ~20%
  fragment_rate: ~40%

slot_builder_lora_v3 target:
  generic_rate: <5%   (6x improvement)
  scar_rate: <5%      (4x improvement)
  fragment_rate: <10% (4x improvement)
```

### Validation 2: Shape Critic Accuracy

**Test prompts (5 held-out binary stance):**
```
1. "Is boundary verification a lock or a gate?"
2. "Does semantic grounding act as a filter or contract?"
3. "Is tool-use gating a lock or boundary?"
4. "Does LoRA modify as a groove or residue?"
5. "Is RAG retrieval a filter or gate operation?"
```

**Ground truth (from manual analysis):**
```
1. GATE (conditionally permits based on verification)
2. CONTRACT (establishes agreement before operation)
3. LOCK (prevents action until condition met)
4. GROOVE (low-rank modification in frozen manifold)
5. FILTER (removes non-relevant candidates)
```

**Metrics to measure:**
```python
def validate_shape_critic(adapter_path, test_prompts, ground_truth):
    predictions = []
    for prompt in test_prompts:
        contract = generate_contract(prompt)  # Use slot_builder_v3
        shape_pred = predict_shape(adapter_path, contract, prompt)
        predictions.append(shape_pred)
    
    # 1. Dominant shape accuracy
    correct = sum(
        1 for pred, truth in zip(predictions, ground_truth)
        if pred['dominant_shape'] == truth['expected_shape']
    )
    accuracy = correct / len(predictions)
    
    # 2. Composite detection (when applicable)
    composite_truth = [t for t in ground_truth if t.get('is_composite')]
    composite_preds = [p for p in predictions if p.get('composite')]
    
    composite_recall = len(composite_preds) / max(1, len(composite_truth))
    
    # 3. Mass distribution error
    mae_per_shape = []
    for pred, truth in zip(predictions, ground_truth):
        if 'shape_field_mass' in truth:
            for shape in pred['shape_field_mass']:
                pred_mass = pred['shape_field_mass'][shape]
                true_mass = truth['shape_field_mass'].get(shape, 0)
                mae_per_shape.append(abs(pred_mass - true_mass))
    
    mass_mae = sum(mae_per_shape) / len(mae_per_shape) if mae_per_shape else 0
    
    return {
        'accuracy': accuracy,              # Target: >85%
        'composite_recall': composite_recall,  # Target: >90%
        'mass_mae': mass_mae,              # Target: <0.10
    }
```

**Expected performance:**
```
Base model (no adapter):
  accuracy: ~40-50% (random + some knowledge)
  composite_recall: ~20%
  mass_mae: ~0.30

shape_critic_v1 target:
  accuracy: >85%
  composite_recall: >90%
  mass_mae: <0.10
```

---

## Integration Testing (v9 Runtime)

After both adapters are validated, test the full v9 flow:

### Test Script

```python
def run_rhi_v9_test(prompt: str):
    """
    v9 runtime: Q → C_v3 → K*_critic → A_guided → audit → Ψ/Ω
    """
    # 1. Generate contract with slot_builder_lora_v3
    contract_result = generate_contract_with_lora_v3(prompt)
    contract = contract_result['contract']
    
    # 2. Predict shape with shape_critic_v1
    shape_pred = predict_shape_with_lora_v1(contract, prompt)
    target_shape = shape_pred.get('composite', shape_pred['dominant_shape'])
    
    # 3. Generate shape-guided answer
    shape_spec = SHAPE_ONTOLOGY[target_shape]
    guided_prompt = f"""Contract: {json.dumps(contract)}

Target operation-shape: {target_shape}
Gloss: {shape_spec['gloss']}
Key verbs: {', '.join(shape_spec['verbs'])}
Key nouns: {', '.join(shape_spec['nouns'])}

User prompt: {prompt}

Answer through the lens of {target_shape}, using target verbs/nouns.
Do not just label it as "{target_shape}" — demonstrate the operation."""
    
    answer = base_model(guided_prompt, temperature=0.7)
    
    # 4. Audit
    audit_result = deterministic_operational_audit(prompt, contract, answer)
    
    # 5. Collapse
    if audit_result['psi'] >= 0.52 and audit_result['support'] >= 4:
        state = 'Ψ'
        reason = 'shape_guided_collapse'
    else:
        state = 'Ω'
        reason = f"psi={audit_result['psi']:.2f} support={audit_result['support']}"
    
    return {
        'state': state,
        'reason': reason,
        'contract': contract,
        'shape_prediction': shape_pred,
        'answer': answer,
        'audit': audit_result,
    }

# Test on 10 prompts (5 binary, 5 normal)
test_prompts = [
    # Binary stance
    "Is the contract boundary condition a filter or a gate?",
    "Does LoRA act as a groove or residue in the parameter space?",
    "Is zero-shot prompting a lock or filter on capabilities?",
    
    # Normal operational
    "Using the Nexus lens, explain why AI agents fail without contracts.",
    "What operational gap does RAG retrieval fix in LLMs?",
    "How does intent stabilization prevent semantic drift?",
    "Explain boundary verification as a gate operation.",
    "Why does tool-first action fail in agentic systems?",
    "What residue signal does answer quality expose?",
    "How does contract-before-tool prevent hallucination?",
]

results = [run_rhi_v9_test(p) for p in test_prompts]

# Metrics
psi_rate = sum(1 for r in results if r['state'] == 'Ψ') / len(results)
avg_psi = sum(r['audit']['psi'] for r in results if r['state'] == 'Ψ') / max(1, sum(1 for r in results if r['state'] == 'Ψ'))
avg_support = sum(r['audit']['support'] for r in results) / len(results)

print(f"Ψ rate: {psi_rate:.1%}")
print(f"Avg Ψ psi: {avg_psi:.3f}")
print(f"Avg support: {avg_support:.1f}")
```

**Expected v9 performance:**
```
Ψ rate: 70-80% (up from v8's 60-70%)
Avg Ψ psi: 0.85-0.90 (up from v8's 0.75-0.85)
Avg support: 5.0-5.5 (stable or slight improvement)
Speed: ~900 tokens/run (4-5x faster than v8's ~4500)
```

---

## Success Criteria

### Must Pass (Critical)

- ✓ **slot_builder_lora_v3 trains without errors**
- ✓ **shape_critic_v1 trains without errors**
- ✓ **Adapters save to correct directories**
- ✓ **Generic term rate <10%** (target <5%)
- ✓ **Shape accuracy >70%** (target >85%)

### Should Pass (Important)

- ✓ **Scar term rate <10%** (target <5%)
- ✓ **Fragment rate <15%** (target <10%)
- ✓ **Composite recall >80%** (target >90%)
- ✓ **Mass MAE <0.15** (target <0.10)

### Nice to Have (Optimization)

- ✓ Training loss converges smoothly
- ✓ No overfitting (validation loss ≈ training loss)
- ✓ v9 runtime achieves 4x speedup
- ✓ Ψ rate improves by 10-15%

---

## Troubleshooting Guide

### Issue: Training crashes with CUDA OOM

**Solution:**
```python
USE_4BIT = True  # Enable 4-bit quantization
# or reduce batch size / gradient accumulation
```

### Issue: Loss not decreasing

**Check:**
1. Data format (system/user/assistant structure)
2. Learning rate (try 1e-4 if 3e-4 too high)
3. Tokenizer padding (should pad to max_length)

### Issue: Overfitting (loss → 0 after 2 epochs)

**Solution:**
```python
SLOT_EPOCHS = 3  # Reduce from 5
SHAPE_EPOCHS = 5  # Reduce from 8
```

### Issue: Adapter doesn't load

**Check:**
1. `adapter_config.json` present
2. `adapter_model.safetensors` present
3. LoRA rank/alpha match config
4. Base model name matches

### Issue: Shape predictions are random

**Likely causes:**
1. Only 3 training examples → might need more epochs (try 12-15)
2. Learning rate too low → try 8e-4
3. Data format wrong → verify JSON structure

---

## Next Actions After Training

1. **Validate both adapters** (see validation scripts above)
2. **Test v9 runtime** on 10 prompts
3. **Measure improvements:**
   - Contract quality (scars, fragments, polarity)
   - Shape accuracy (dominant, composite, mass)
   - Runtime speed (tokens per run)
   - Collapse quality (Ψ rate, psi scores)

4. **If validation passes:** Deploy v9 as production runtime
5. **Collect v9 corpus:** Run 20+ prompts, export training rows
6. **Retrain adapters:** v4 with expanded corpus (118+ repair, 32+ shape rows)
7. **Iterate:** v10, v11, ... with trace sufficiency, agentic loops

---

## Final Checklist Before Training

```
□ v8 PATCHED corpus verified (78 repair + 12 shape rows)
□ Training datasets generated (16 slot + 3 shape examples)
□ Hyperparameters match specification
□ GPU available (CUDA-enabled)
□ Disk space sufficient (~2GB for adapters)
□ Base model downloaded (Qwen/Qwen2.5-1.5B-Instruct)
□ RUN_TRAINING flag ready to enable
□ Validation prompts prepared
□ Integration test script ready
```

**When all boxes checked:** Set `RUN_TRAINING = True` and execute notebook.

---

**Ψ-convergence ready. The corpus is locked. The datasets are formatted. Train when ready.**
