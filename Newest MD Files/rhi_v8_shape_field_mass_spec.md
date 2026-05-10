# RHI Runtime v8 — Shape-Field Mass Collapse
**Phase 1163+ | QuHarmonics Research Group**

## v7 → v8 Correction

**v7 gap identified:**
```python
# v7 shape_stance_collapse (line ~450 in v7 notebook)
top_stance = shape_probe["rows"][0]["stance"]
if top_stance.get("confidence") < SHAPE_STANCE_CONF_MIN:
    return Ω
```

**Problem:** Classifies by top branch only. Ignores shape-field mass across all high-quality branches.

**v8 correction:** Classify the whole field with weighted mass:

```
M_K = Σ_i ψ_i · Audit(A_i) · σ_i · κ_i · s_{i,K}

where:
  M_K         = mass of shape K across all branches
  ψ_i         = psi score for branch i
  Audit(A_i)  = five-dimensional audit score for branch i
  σ_i         = support indicator: 1 if support_i ≥ SUPPORT_MIN, else 0
  κ_i         = confidence proxy: margin_i if available, else normalized audit
  s_{i,K}     = shape score for shape K in branch i (from shape_stance function)
```

## v8 Runtime Shape

```text
Q → C_raw → C_repaired(+fc_repair) → {A_i} → five-dim audit
  ↓
shape stance extraction (all branches)
  ↓
shape-field mass computation: M_K for K ∈ {FILTER, GATE, BOUNDARY, ...}
  ↓
composite detection: FILTER⊕GATE → BOUNDARY
  ↓
shape-mass collapse or Ω
  ↓
Ψ/Ω
```

## Shape-Field Mass Algorithm

### Step 1: Extract Shape Scores for All Branches

For each branch `i` in top N (typically N=4):
- If `high_quality(branch_i)` (support ≥ 4, audit ≥ 0.52, psi ≥ 0.52):
  - Compute `shape_stance(answer_i, shape_options)` → scores for each K
  - Store: `s_{i,K}` for all shapes K

### Step 2: Compute Mass for Each Shape

```python
def compute_shape_field_mass(
    score_df: pd.DataFrame,
    shape_options: List[str],
    top_n: int = 4
) -> Dict[str, float]:
    """
    Compute weighted mass M_K for each shape K.
    Returns: {shape: mass} dict
    """
    masses = {K: 0.0 for K in shape_options}
    
    for idx, row in score_df.head(top_n).iterrows():
        # Weight factors
        psi_i = float(row["psi"])
        audit_i = float(row["audit_score"])
        sigma_i = 1.0 if int(row["support"]) >= SUPPORT_MIN else 0.0
        
        # Confidence proxy (use margin if available, else audit)
        margin_i = float(row.get("margin", audit_i))
        kappa_i = margin_i
        
        # Shape scores for this branch
        stance = shape_stance(row["answer"], shape_options)
        
        for K in shape_options:
            s_iK = stance["scores"][K]
            masses[K] += psi_i * audit_i * sigma_i * kappa_i * s_iK
    
    return masses
```

### Step 3: Composite Detection

```python
def detect_composite_shape(
    masses: Dict[str, float],
    threshold: float = 0.25
) -> Optional[str]:
    """
    Detect if FILTER and GATE both score high → BOUNDARY composite.
    
    Rules:
    - If M_FILTER ≥ threshold AND M_GATE ≥ threshold:
        - If both are valid projections of the same interface:
            return "BOUNDARY" (composite)
    - Return None if no composite detected
    """
    if masses.get("FILTER", 0.0) >= threshold and masses.get("GATE", 0.0) >= threshold:
        # Check if they're describing the same operational interface
        # (both present in top 2 masses, close scores)
        sorted_masses = sorted(masses.items(), key=lambda x: x[1], reverse=True)
        top_two = {sorted_masses[0][0], sorted_masses[1][0]}
        
        if "FILTER" in top_two and "GATE" in top_two:
            ratio = min(masses["FILTER"], masses["GATE"]) / max(masses["FILTER"], masses["GATE"])
            if ratio >= 0.65:  # Close enough to be dual aspects
                return "BOUNDARY"
    
    return None
```

### Step 4: Collapse Decision

```python
def krrb_resolve_v8(
    score_df: pd.DataFrame,
    contract: Dict,
    contract_ok: bool,
    prompt: str
) -> Dict:
    """
    v8: Shape-field mass collapse with composite detection.
    """
    if not contract_ok or score_df.empty:
        return {"state": "Ω", "reason": "contract_incomplete_or_no_candidates", ...}
    
    # Detect binary stance prompt
    probe = detect_binary_stance_prompt(prompt)
    
    if not probe["is_binary"]:
        # Normal KRRB collapse path (unchanged from v7)
        return krrb_v7_normal_collapse(score_df, contract)
    
    # Binary stance path: compute shape-field mass
    masses = compute_shape_field_mass(score_df, probe["shape_options"])
    
    # Check for composite
    composite = detect_composite_shape(masses)
    
    if composite:
        return {
            "state": "Ψ",
            "reason": "composite_shape_collapse",
            "composite": composite,
            "constituent_masses": {
                "FILTER": masses["FILTER"],
                "GATE": masses["GATE"],
            },
            "resolved_shape": "BOUNDARY",
            "winner": score_df.iloc[0].to_dict(),
            "shape_field_mass": masses,
        }
    
    # Find dominant shape
    max_shape = max(masses.items(), key=lambda x: x[1])
    max_mass = max_shape[1]
    
    # Threshold for collapse
    SHAPE_MASS_MIN = 0.30  # Tunable
    
    if max_mass >= SHAPE_MASS_MIN:
        return {
            "state": "Ψ",
            "reason": "shape_mass_collapse",
            "dominant_shape": max_shape[0],
            "dominant_mass": max_mass,
            "shape_field_mass": masses,
            "winner": score_df.iloc[0].to_dict(),
        }
    else:
        return {
            "state": "Ω",
            "reason": "shape_mass_below_threshold",
            "max_mass": max_mass,
            "max_shape": max_shape[0],
            "shape_field_mass": masses,
            "winner": score_df.iloc[0].to_dict(),
        }
```

## Four-Gap Repair Extension

v7 handles three repair gaps well:
1. **Generic removal** — "current" → structured concepts
2. **Scar removal** — "general purpose" → forbidden anti-patterns  
3. **Positive injection** — missing → "intent", "boundary", "tool"

v8 adds the fourth gap:

4. **Shape-stance grounding** — When answer uses vocabulary but misses operational semantics

### Shape-Stance Repair Row Format

```json
{
  "run_id": "rhi_v8_...",
  "prompt": "...",
  "branch": "operational",
  "answer": "...",
  "repair_type": "shape_stance_grounding",
  "field": "operational_semantics",
  "bad_value": {
    "surface_vocab": ["filter", "filtering"],
    "shape_score": 0.30,
    "shape": "FILTER"
  },
  "good_value": {
    "grounded_vocab": ["filter", "exclude", "remove", "invalid"],
    "shape_score": 0.85,
    "shape": "FILTER",
    "verbs": ["excludes", "removes"],
    "nouns": ["state", "candidate"]
  },
  "instruction": "When answering about FILTER operations, include exclusion verbs (exclude, remove, discard) and state nouns (candidate, invalid, set), not just the label 'filter'."
}
```

This teaches the model: **shape stance requires operational vocabulary, not just labels.**

## Shape Training Row Enhancement

v7 shape rows capture:
- `best_shape`: top classification
- `confidence`: margin between top and second
- `scores`: all shape scores

v8 adds:
- `shape_field_mass`: weighted mass M_K for each shape
- `composite_detected`: bool
- `constituent_shapes`: list if composite

### v8 Shape Row Format

```json
{
  "run_id": "rhi_v8_...",
  "prompt": "Is X a filter or a gate?",
  "branch": "skeptical",
  "answer": "...",
  "shape_options": ["FILTER", "GATE", "BOUNDARY"],
  
  "best_shape": "GATE",
  "best_score": 0.72,
  "confidence": 0.35,
  "scores": {
    "FILTER": 0.37,
    "GATE": 0.72,
    "BOUNDARY": 0.25
  },
  
  "shape_field_mass": {
    "FILTER": 0.42,
    "GATE": 0.58,
    "BOUNDARY": 0.31
  },
  
  "composite_detected": false,
  "constituent_shapes": null,
  
  "runtime_state": "Ψ",
  "runtime_reason": "shape_mass_collapse",
  "instruction": "Map to operation-shape stance using weighted field mass, not just top branch."
}
```

## Implementation Checklist

### Core Changes
- [ ] `compute_shape_field_mass(score_df, shape_options)` function
- [ ] `detect_composite_shape(masses)` function
- [ ] `krrb_resolve_v8()` with shape-field mass path
- [ ] Update `build_shape_rows()` to include `shape_field_mass`
- [ ] Add `build_shape_stance_grounding_rows()` for fourth gap

### Config Updates
- [ ] `SHAPE_MASS_MIN = 0.30` threshold
- [ ] `COMPOSITE_RATIO_MIN = 0.65` for FILTER⊕GATE detection
- [ ] `SHAPE_FIELD_TOP_N = 4` branches to include in mass computation

### Output Files
- [ ] `rhi_repair_training_rows_v8.jsonl` (includes shape-stance grounding)
- [ ] `rhi_shape_training_rows_v8.jsonl` (includes shape_field_mass)
- [ ] `rhi_live_runs_v8.jsonl`
- [ ] `rhi_live_runtime_v8_manifest.json`

### Training Signal Targets
```text
slot_builder_lora_v3 ← rhi_repair_training_rows_v8.jsonl
shape_critic_v1      ← rhi_shape_training_rows_v8.jsonl
```

## Collapse State Summary

### v7 States
```
Ψ collapse              — normal margin collapse
Ψ consensus_collapse    — high agreement, low margin
Ψ shape_stance_collapse — binary prompt, top branch confident
Ω divergent_consensus   — high-quality branches disagree on stance
Ω support_below_min     — insufficient support
```

### v8 States (additions)
```
Ψ shape_mass_collapse      — dominant shape mass ≥ threshold
Ψ composite_shape_collapse — FILTER⊕GATE → BOUNDARY detected
Ω shape_mass_below_threshold — no shape reaches mass threshold
```

## Next Fold

```text
v8 runtime complete
  ↓
collect 50+ runs
  ↓
generate shape-field mass training rows
  ↓
build slot_builder_lora_v3 + shape_critic_v1 corpus
  ↓
train v3 adapters
  ↓
deploy v9: shape-guided answer synthesis
```

---

**Ψ-convergence path:**

$$
\boxed{
\begin{align}
v7 &= \text{repair memory} + \text{shape memory} + \text{collapse memory} \\
v8 &= v7 + \text{shape-field mass} + \text{composite detection} \\
\text{Target} &: M_K = \sum_i \psi_i \cdot \text{Audit}(A_i) \cdot \sigma_i \cdot \kappa_i \cdot s_{i,K}
\end{align}
}
$$

When:
$$
\boxed{ M_{\text{FILTER}} \approx M_{\text{GATE}} \implies \text{BOUNDARY composite} }
$$

The interface shape is revealed.
