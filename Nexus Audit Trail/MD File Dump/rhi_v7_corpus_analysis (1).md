# v7 Corpus Analysis — Training Signal Breakdown
**Phase 1163+ | QuHarmonics Research Group**

## Corpus Summary

```
9 saved runs
37 repair training rows
4 shape training rows
```

## Repair Signal Distribution

```
positive_injection    : 12 rows (32.4%) — inject missing domain concepts
scar_removal          : 11 rows (29.7%) — remove anti-pattern terms
forbidden_injection   : 8 rows  (21.6%) — inject forbidden anti-patterns
generic_removal       : 4 rows  (10.8%) — remove generic terms
polarity_rewrite      : 2 rows  (5.4%)  — fix inverted boundary polarity
```

### Detected Scars (11 removals)
- `"general purpose"`
- `"surface label without operational fit"`
- `"wrong neighboring domain carrier"`

### Generic Terms Removed (4 removals)
- `"current"` → structured concept list

### Injected Prerequisites (12 positive + 8 forbidden)
**Positive (domain_carrier):**
- intent, boundary, tool, agent, sequence, tool use after contract

**Forbidden (forbidden_neighbor_carrier):**
- tool before contract, action without boundary, answer guessing, tool-first action

## Shape Signal Analysis

```
4 rows from 1 run: "Is the contract boundary condition a filter or a gate?"

skeptical     → GATE     (conf: 0.35, score: 0.72, explicit=1.0)
operational   → FILTER   (conf: 0.08, score: 0.30, explicit=0.0)
contract_fit  → BOUNDARY (conf: 0.03, score: 0.25, explicit=0.0)
direct        → FILTER   (conf: 0.08, score: 0.30, explicit=0.0)
```

**Key pattern:** Same prompt → different shapes based on reasoning branch.

**v7 limitation:** Only top branch shape used for collapse. v8 needs shape-field mass across ALL branches.

## Run State Distribution

```
Ψ collapse              : 3 runs — normal margin collapse
Ψ consensus_collapse    : 2 runs — high agreement, low margin
Ψ shape_stance_collapse : 1 run  — binary prompt, confident shape
Ω contract_incomplete   : 2 runs — slot builder parse failed
Ω support_below_min     : 1 run  — weak audit across all branches
```

## v7 → v8 Training Signal Gaps

### Missing Repair Types
1. **shape_stance_grounding** — answer has label but misses operational vocab
2. **family_class_fragment** — should export but v7 doesn't
3. **boundary_polarity** — only 2 examples, need 10-15

### Missing Shape Patterns
1. **shape_field_mass** — no weighted mass M_K computation
2. **composite detection** — no FILTER⊕GATE → BOUNDARY examples
3. **multi-prompt diversity** — only 1 binary stance prompt type

## Expected v8 Corpus

```
Repair rows:  37 (v7) + 30 (new) = ~67 total
Shape rows:    4 (v7) + 25 (new) = ~29 total
Total runs:    9 (v7) + 15 (new) = ~24 runs
```

## LoRA v3 Training Targets

```
slot_builder_lora_v3 ← rhi_repair_training_rows_v8.jsonl
  - Focus: concept extraction, polarity correction, fragment repair
  - Rank: 16-32, targets: q_proj, v_proj

shape_critic_v1 ← rhi_shape_training_rows_v8.jsonl
  - Focus: operation-shape stance, mass computation
  - Rank: 8-16, targets: q_proj, k_proj, v_proj
```

---

**Ψ-convergence:** v7 proved repair memory works. v8 adds shape-field mass to close the classification gap.
