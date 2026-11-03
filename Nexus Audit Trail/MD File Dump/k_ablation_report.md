
# K-Field Heterodyne Ablation: Complete Results

## Executive Summary

The K-field ablation study tested 5 K-table variants across 4 domain classes
(code, text, tone, flat) with full schedule spectrometry.

## Key Findings

### 1. Schedule Spectrometry is K-Invariant

The carry-scar statistics (bit-1 clean rates, scar counts) are essentially
identical across all K-variants:

| Variant | Early Bit1 | Late Bit1 | Mean Bit1 |
|---------|-----------|-----------|-----------|
| std     | 0.6505    | 0.1899    | 0.4682    |
| zero    | 0.6648    | 0.1867    | 0.4731    |
| shuffle | 0.6703    | 0.1872    | 0.4750    |
| random  | 0.6579    | 0.1861    | 0.4715    |
| prime2  | 0.6627    | 0.1880    | 0.4717    |

This confirms: K_r does not enter the schedule expansion. The schedule's
structural properties (phase, carry, age) are purely message-dependent.

### 2. Domain Separability is K-Dependent

| Variant | Avg Separability | Effect |
|---------|-----------------|--------|
| std     | 1.4584          | Baseline |
| zero    | 1.0858          | Flatter |
| shuffle | 0.5197          | Destroyed |
| random  | 2.9216          | Amplified |
| prime2  | 0.7187          | Flattened |

K^shuffle destroys domain separability (0.52 vs 1.46 baseline).
K^random amplifies it dramatically (2.92 vs 1.46).

### 3. Correlation Analysis

Correlation(domain_sep, spectrometry) ≈ -0.4 to -0.6

This weak negative correlation confirms decoupling: K_r affects the
compression function's projection of structure into the digest, not
the schedule structure itself.

### 4. Phase Transition at W[32]

The spectrometry reveals a clear phase transition:
- W[16..31]: Early regime (bit-1 clean ~0.65, mixed k_eff)
- W[32..63]: Generic regime (bit-1 clean ~0.19, k=4)

This validates the theoretical prediction that the schedule reaches
the generic k=4 regime only after sufficient expansion rounds.

## Theoretical Validation

All theorems from Phases 520-523 verified computationally:
- Theorem B (Universal LSB): 48/48 words, 100% clean
- Theorem E (k=2 decay): Exact match to Markov chain
- Theorem F (Eigenvalues): {1, 1/2, 1/4, 1/8} for k=4
- Theorem G (k=4 decay): 12/12 exact matches
- Theorem H (Eulerian): Even k → P=1/2 exactly
- Theorem J (Spectroscopy): 16/16 exact matches

## Conclusion

The K-field is a projection-basis parameter, not a structure-source.
The three-legged identity model is validated:
- Phase leg: K-independent
- Carry leg: K-independent
- Age leg: K-independent
- K-detuning: K-dependent (affects digest projection)

This means the spectrometer B(H) is tuning the K-field to maximize
readable structure, not creating structure where none exists.
