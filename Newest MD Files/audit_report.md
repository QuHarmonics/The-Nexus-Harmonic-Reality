# Audit Report: SHA-256 Phase Lock + Twin-Prime W=210

## Status heading

```
Ψ SHA-256:  signal DOES NOT survive rigorous audit
Ω Twin primes: signal IS present with correct observable
```

---

## 1. SHA-256 Quantizer Competition

Panel tested: 15°, 18°, 20°, 22.5°, 24°, 30°, random

| Step  | obs_err | null_mean |    z    |   p     | %below | Direction      |
|------:|--------:|----------:|--------:|--------:|-------:|----------------|
|  15°  | 0.06489 |  0.06545  |  -2.317 |  0.0205 |  +0.8% | ← phases closer to grid |
|  18°  | 0.07958 |  0.07853  |  +3.912 |  0.0001 |  -1.3% | phases further           |
| **20° (H=π/9)** | **0.08775** | **0.08721** | **+1.796** | **0.0724** | **-0.6%** | **phases further, not significant** |
| 22.5° | 0.09699 |  0.09815  |  -3.310 |  0.0009 |  +1.2% | ← phases closer to grid |
|  24°  | 0.10627 |  0.10470  |  +4.112 | <0.0001 |  -1.5% | phases further           |
|  30°  | 0.13309 |  0.13085  |  +5.072 | <0.0001 |  -1.7% | phases further           |

**H=π/9 does not win.** The observable (arctan2 of normalized state vector) shows
phases are marginally *further* from the 20° grid than random expectation (z=+1.80),
not closer. 15° and 22.5° actually show genuine phase attraction (negative z).

---

## 2. Null Ensemble Audit at H=π/9

| Ensemble                    | obs_err | null_mean |   z    |   p     | %below |
|-----------------------------|--------:|----------:|-------:|--------:|-------:|
| Real: random inputs         | 0.08775 |  0.08726  | +1.510 |  0.1309 | -0.6%  |
| Real: prefix-structured     | 0.08975 |  0.08725  | +7.181 | <0.0001 | -2.9%  |
| Surr: shuffle rounds        | 0.08840 |  0.08725  | +2.619 |  0.0088 | -1.3%  |
| Surr: shuffle per-round     | 0.08840 |  0.08722  | +2.488 |  0.0128 | -1.4%  |

**Signal does not survive.** The shuffled surrogates behave identically to real
SHA data under the H=π/9 quantizer. The "49% below random" from the prior run
was an artifact of the earlier observable/methodology — it did not replicate
under the controlled audit.

---

## 3. Observable Stability + Round Localization

| Observable                      |   z    |   p     | verdict        |
|---------------------------------|-------:|--------:|----------------|
| Primary (arctan2 of norm state) | +1.510 |  0.1309 | not significant |
| Diff (arctan2 of state diffs)   | -0.596 |  0.5512 | not significant |
| Autocorr lag-1 mean             | -0.438 |   —     | anti-correlated |

Round localization: effect (weak, ~z=1.8) is concentrated in r0–15 (early
rounds, p=0.078), near zero in mid and late rounds. Consistent with structure
from initial padding rather than SHA's internal dynamics.

**The phase-lock finding does not generalize across observable definitions.**
It is not robust.

---

## 4. SHA-256 Verdict

```
The original "49% below random" result does not survive:
  - quantizer competition   (H=π/9 is not the best axis)
  - null surrogates         (shuffled data looks the same)
  - observable variation    (effect vanishes on state-diff observable)
  - round localization      (weak signal only in early rounds)

Effect sizes: ~0.6–1.5%, not the claimed ~49%.

Most likely explanation: the prior observable confounded input structure
with SHA dynamics. The early-round (r0–15) weak signal may reflect
padding/block-boundary regularities, not H-quantization of internal state.

Current status: Ω  SHA-256 phase lock at H=π/9 is not confirmed.
```

---

## 5. Twin-Prime W=210 Subtype Entropy

### Subtype structure
- W=210 = 2×3×5×7: **48 coprime residues**
- Valid twin-prime subtypes (r, r+2 both coprime to 210): **14 pairs**

### Signal: entropy × twin-center density

| Window  | r(entropy, twin_frac) | p-value    | t-test p | Direction |
|---------|-----------------------|-----------|----------|-----------|
| W×1=210 |      **r = 0.343**    | 2.1 × 10⁻¹⁵ | 0.0000  | ✓ twins in HIGH entropy windows |
| W×2=420 |      **r = 0.256**    | 4.7 × 10⁻⁹  | 0.0001  | ✓ twins in HIGH entropy windows |
| W×3=630 |      **r = 0.286**    | 6.5 × 10⁻¹¹ | 0.0000  | ✓ twins in HIGH entropy windows |

Direction is consistent across all window sizes.  
Twin centers are systematically overrepresented in windows where subtype
occupancy entropy is above median.

### Fourier: period-210 dominance

| Period  | Z-score vs neighbors |
|---------|---------------------|
| **210.1** | **z = 50.84** ← dominant |
| 209.9   | z = 24.09  |
| 230.9   | z =  8.99  |
| 689.7   | z =  8.27  |

Period-210 is the single dominant spectral peak in twin-center density.
Not ambiguous.

### Center spacing structure

- All twin-center gaps are divisible by **6** (100% of 11,593 gaps).  
- Modal gap: **30** (6.5%), followed by 42, 12, 60, 90.  
- Top gaps are all divisors/multiples of 30 = W/7.  
- 29.7% of gaps are divisible by 30.

```
Twin prime signal summary:
  ✓ Twins over-represented in high-entropy windows: r=0.34, p=2×10⁻¹⁵
  ✓ Period-210 dominates the Fourier spectrum: z=50
  ✓ All center gaps divisible by 6 (forced by wheel structure)
  ✓ Signal robust across W×1, W×2, W×3 windows

Current status: Ψ  W=210 subtype entropy signal is real and significant.
```

---

## 6. Overall State

```
SHA-256:     Ω  Phase lock at H=π/9 not confirmed under rigorous controls.
                Effect was ~0.6%, not ~49%. Does not survive surrogates.
                Do not invest further until the prior observable is audited
                for the source of the discrepancy.

Twin primes: Ψ  Subtype entropy signal confirmed.
                Twins cluster in high-entropy windows, period-210 Fourier
                peak is z=50, spacings are all divisible by 6.
                This is the live signal. Next: check whether the SPECIFIC
                14 valid subtypes show unequal occupancy (which subtypes
                carry the overrepresentation?), and whether the entropy
                signature is dominated by a handful of subtype slots or
                is uniformly distributed.

Transformer: Ω  Internal activation measurement still unexecuted.
                Output-level compression proxies are too downstream.
                Skip unless actual residual stream access is available.
```
