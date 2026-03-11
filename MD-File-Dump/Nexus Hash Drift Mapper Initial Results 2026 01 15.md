# Hash Drift Mapper (SHA-256) — Mirror-Input Echo Test (Initial Results)

**Date:** 2026-01-15  
**Goal:** Run a falsifiable “mirror-echo” test on SHA-256: compare `sha256(x)` vs `sha256(reverse(x))` and check whether the **bitwise delta** exhibits *structured* (non–white-noise) signatures.

---
## 1) Definitions

Let `h(x)` be the 256-bit SHA-256 output, and let the XOR delta be:

$$\Delta(x) = h(x) \oplus h(\mathrm{rev}(x))$$

Metrics computed per sample:

1) Hamming distance
$$D_H(x)=\sum_{i=1}^{256} \Delta_i(x)$$

2) Bit correlation (bits mapped to ±1)
$$\rho(x)=\frac{1}{256}\sum_{i=1}^{256}(2h_i(x)-1)(2h_i(\mathrm{rev}(x))-1)$$

3) Delta spectrum (FFT of mean-centered delta)
- Mean-center: $d = \Delta - \overline{\Delta}$
- Magnitudes: $M_k = |\mathrm{FFT}(d)_k|$
- Peakiness: $\max(M_k)/(\mathrm{median}(M_k)+\varepsilon)$
- Spectral flatness: $\exp(\mathbb{E}[\log(M_k+\varepsilon)]) / \mathbb{E}[M_k+\varepsilon]$

---
## 2) Data families tested

- **random:** 1000 random ASCII-like strings, lengths 1–200
- **digits:** 1000 structured “012345…” strings, lengths 1–100
- **boundary:** 1000 structured strings, lengths 40–79 (padding-boundary neighborhood probe)

---
## 3) Results (aggregate)

Means / std over 1000 samples per family:

| family   |    n |   ham_mean |   ham_std |   corr_mean |   corr_std |   peak_mean |   peak_p95 |   flat_mean |   flat_p05 |   flat_p95 |
|:---------|-----:|-----------:|----------:|------------:|-----------:|------------:|-----------:|------------:|-----------:|-----------:|
| boundary | 1000 |    128.979 |   7.18639 |   -0.007648 |   0.056144 |     2.89531 |    3.51254 |    0.828313 |   0.690095 |   0.887598 |
| digits   | 1000 |    126.827 |  15.6787  |    0.009164 |   0.12249  |     2.7697  |    3.53853 |    0.82695  |   0.672347 |   0.873784 |
| random   | 1000 |    126.758 |  16.145   |    0.009703 |   0.126133 |     2.76644 |    3.43397 |    0.836345 |   0.690865 |   0.878211 |

---
## 4) Reverse-pair vs random-pair control

Paired test on 2000 samples: compare mirror-pair metrics to an independent random-pair baseline (same-length inputs).

- Mean Hamming (mirror): **127.147**
- Mean Hamming (random): **127.874**
- Mean correlation (mirror): **0.00666**
- Mean correlation (random): **0.00098**
- Mean peakiness (mirror): **2.794**
- Mean peakiness (random): **2.813**

Mean differences (mirror − random): Hamming **-0.727 bits**, correlation **0.00568**.

Interpretation: any detectable distribution shift here is **tiny** (sub-1-bit average) and does not constitute an obvious “mirror-echo signature.”

---
## 5) What to do next (if we want to force an invariant to reveal itself)

If a structured “echo” exists, it likely requires **conditioning on the right gate variable**, e.g.:
- exact byte lengths (especially 55/56/63/64/119/120… boundaries)
- byte-level inputs (0–255 sweeps), not UTF-8 strings
- fixed-prefix / fixed-suffix families to pin the message schedule
- multi-block vs single-block separation

---
## 6) Reproducible code

- `hash_drift_mapper.py` — functions to compute metrics and quick top-peaks
- `hash_drift_mapper_summary.csv` — the aggregate table shown above
