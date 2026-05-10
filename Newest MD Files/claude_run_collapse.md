# Claude Run Set Collapse

## Aggregate
- runs: 5
- mean hamming: 129.6/256 (50.6%)
- hamming spread: σ = 11.64 bits
- mean energy ratio INV/STD: 0.9826
- mean absolute energy drift from 1.0: 0.0620
- XOR popcount: 122/256 (Δ from random = -6)
- XOR z-score vs random 50/50: -0.750
- dP correlation K_std vs K_inv: 0.011945

## Read
- Additive inversion is exact at the constant layer.
- Digest outputs do **not** cancel; they stay near half-bit separation overall.
- Energy stays relatively close on average, so the inverse carrier perturbs topology without collapsing it.
- Correlation is near zero, which reads as decorrelation rather than mirror inversion.

## Per-run ranking for next passes
1. K_phase_shifted: hamming=113/256, ratio=0.9914, zones STD 4/8 REAL 4/8 IMAG -> INV 5/8 REAL 3/8 IMAG
2. K_INV_as_msg: hamming=124/256, ratio=1.0306, zones STD 6/8 REAL 2/8 IMAG -> INV 6/8 REAL 2/8 IMAG
3. H_constants: hamming=126/256, ratio=0.8480, zones STD 6/8 REAL 2/8 IMAG -> INV 5/8 REAL 3/8 IMAG
4. K_constants_half: hamming=139/256, ratio=1.0808, zones STD 6/8 REAL 2/8 IMAG -> INV 4/8 REAL 4/8 IMAG
5. K_constants_full: hamming=146/256, ratio=0.9621, zones STD 5/8 REAL 3/8 IMAG -> INV 4/8 REAL 4/8 IMAG

## Suggested next targets
- K_phase_shifted is the strongest candidate: lowest hamming (113) and near-unit energy ratio (0.9914).
- K_INV_as_msg is second-best structurally: low hamming (124) with modest energy drift (1.0306).
- H_constants is weaker on energy preservation despite decent separation.

## Bottom line
The inverse constants are behaving like a valid anti-carrier at the injection layer, but not yet as a digest-space canceller. The best current signal is a near-energy-preserving decorrelation, strongest on the phase-shifted input.