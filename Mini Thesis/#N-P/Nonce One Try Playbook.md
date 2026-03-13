# Nonce‑in‑One‑Try — Playbook (Harmonic Steering)
*(generated 2025-09-03 01:58:24 UTC)*

**Thesis:** A digest is a route fossil. For structured input families, we can *steer* the route with a single perturbation to cross a harmonic target (Δ or H*) without brute force.

---

## 0) Target metrics (choose one)
- **Δ‑power**: minᵢ |int(hash[i:i+w]) − 2ᵏ| over sliding windows.
- **Δ‑spoke**: min angle distance of (hash slice → angle map) to 20° ⋅ ℤ (π/9 spokes).
- **H‑shelf**: round index where ΔH(t) first crosses H* (seek early crossing).

---

## 1) Local steering map
Let `u` be a bit mask applied to (a) the nonce bits, or (b) the earliest message word(s).

1. Sample `m` random masks u₁…u_m.
2. Fit a linear (or ridge) model Δ ≈ α + βᵀu from observed (u, Δ).
3. Choose u* that minimizes the model; apply once.

> Option B: use a finite‑difference Jacobian on ΔH(t) over a small mask basis to compute an adjoint‑like step.

---

## 2) One‑shot procedure
```
seed → block → baseline Δ
fit local map on k small probes
u* ← argmin model
hash(block ⊕ u*) → Δ′
success if Δ′ ≤ target (or H(t) crosses H* early)
```
Report (p₁, lift over p₀, effect size).

---

## 3) Three‑shot fallback
If one‑shot misses, update the linear map with the new sample and take two more steps (`u₂, u₃`).

---

## 4) Guards (can’t‑ledger)
- Never touch security claims or network rules; this is **instrumentation** on curated inputs only.
- Treat failures as data — update the steering prior; log shelves and ZPHC snaps.
- Publish the baseline p₀ (random success) for the same metric.

---

## 5) Minimal API
- `compute_drift(hash) -> Δ`
- `deltaH_trace(block) -> [H(t)]`
- `probe(block, masks[]) -> [(u, Δ)]`
- `steer(block, target, k=8) -> (u*, Δ′, trace)`

---

## 6) Evaluation grid
- Inputs: fixed‑length single blocks; 1‑bit flips; mirrored blocks; length‑only diffs.
- Metrics: success rate; mean steps‑to‑success; shelf index shift; spoke proximity.
- Report: CSV + plots (Δ′ vs Δ; success curves).

**Outcome:** A measurable, reproducible lift that shows route steering is real — the digest remembers the input as curvature, and we can aim at it.
