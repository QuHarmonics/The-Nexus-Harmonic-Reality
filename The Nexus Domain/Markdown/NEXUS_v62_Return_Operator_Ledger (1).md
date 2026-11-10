# NEXUS v6.2 — the return operator: ledger

Dean A. Kulik · QuHarmonics Research Group · ORCID 0009-0003-3128-8828 · 3 November 2026

Object: F, the 17-bit fixed-charge step (phi = A, h = u, C = u); G16 = V4 × T4; quotient Q on 8,704 classes. The gap: the first meeting T(s) = min{t > 0 : F^t(s) ∈ G·s}; for the vacuum seed, T = 806 with owner H_1001.

v6.2 independent run: exit 0, every assertion passes. Burnside count STANDS: fixed points 131,072 (I), 4,096 (J), 2,048 (A), 2,048 (A0), 0 for every element with a translation; orbits 256 × 4 + 640 × 8 + 7,808 × 16 = 8,704 classes.

Seals: predictions7 `a4f2e0b6987580c60f18fd4a1995e0589d18dc43746591d5fd6ded76af466a6a`; predictions8 `d3b252d184c16dc6e2d4f3bc7eb9767dae8c5506b6239415bedbd135815f1328`.

- Q5 twisted Burnside, STANDS (proof: each s with F^t s ∈ G·s is counted |Stab s| times) and RUNS: #classes fixed by Q^t = (1/16) Σ_g #{s : F^t s = g·s}, 0 mismatches at 19 depths (1 to 5,186). The return operator is the v6.2 Burnside sum with F^t inserted.
- Q1–Q4 RUNS: the only charge of F of degree ≤ 3 in the key bits (Q∘F ⊕ Q constant) is the e_R ledger (key bits 1, 7, 10, 13, 15; c = 1); for F² it is the ledger with c = 0. The ledger is the character χ(g) = g & 1, so the algebra binds exactly one bit of the clock: T ≡ χ(owner) mod 2. BOUND: parity.
- Q6: the seed's 1,612-cycle has algebraic degree 16, the maximum for an even set, RUNS. Its family and the long part have degree 14, ELSEWHERE: owned by the symmetry (cycle 16, V4 closure 15, G16 closure 14; random even G16-invariant sets land at 14 or 15). Affine re-addressing preserves degree, so no affine change of coordinates lowers the cycle below 16.
- measured: the seed's route word (806 moves x) has letter counts 89, 132, 114, 66, 107, 114, 108, 76 for x = 0..7; the 89 zero moves are the zero-displacement hits. Factor complexity 8, 64, 327, 562, 689 against 8, 64, 382, 720, 797 for the same letters shuffled; zlib 351 vs 387 bytes. The route cylinder shrinks 16,384 → 2,048, 256, 32, 32, 4, 4, 4, 4, 1: nine moves pin the state.

Binding: the magnitude of T is UNBOUND in these coordinates. F is affine on each of its 8 pieces (fixed p), so F^t is affine on each route cylinder and the twisted fixed set is a rank computation there; the cylinder is named by a near-incompressible address. OPEN, missing link named: a nonlinear coordinate change in which the seed's cycle has low degree (equivalently fewer affine pieces), or a reversor that turns T into the distance between two boundary sets.

## Addendum, 4 November 2026: the channel lock and the plane ladder

- The step on every state: with x = D[p] ⊕ w and κ = 7 if ell(x) = 0 else 3 (codes), (w, D[p]) → (w ⊕ D[p] ⊕ κ, w ⊕ κ), then p ← p ⊕ x. On each code bit plane this is the affine map (w, d) → (w ⊕ d ⊕ κ_i, w ⊕ κ_i), linear part [[1,1],[1,0]] (order 3 over GF(2)). κ_0 = κ_1 = 1 always; κ_2 = 1 ⊕ ell(x). STANDS, checked on all 131,072 states.
- Channel lock (independent audit), RUNS in the full sector: on plane i ∈ {0, 1} the map with κ = 1 fixes (w_i, d_i) = (0, 1), so {w_i = 0, every cell bit i = 1} is F-invariant. |R| = |L| = 4,096, |R ∩ L| = 128; indicator degree 5 (R ⊕ L) and 10 (both-locked, unlocked). Each channel's 32 states split 1 + 31 under the four triad maps, so the split is complete.
- Ladder: both planes locked → cycles 2 and 6 only; one plane locked (affine hull exactly the 12-dimensional lock) → 30, 94, 98, 212, 434 (quotient 15, 47, 49, 106, 217); nothing locked (affine hull all 17 dimensions) → 132, 1612, 2260, 3948, 5186 (quotient 66, 806, 1130, 1974, 2593). The 30-cycle's own hull is 8-dimensional and not invariant: no nested lock.
- Correction to the first section: the degree ≤ 3 scan was right as stated, but invariant structure begins at degree 5, where the lock lives. The statement about the seed stands: its cycle's affine hull is the whole space, so no invariant affine subspace short of everything contains it.
- The audit's S3 (every long cycle meets w = u) lands ELSEWHERE for 15, 47, 49, 106, 217: owner, the lock (e_R(w) = 0 forbids w = u).
