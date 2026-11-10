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

## Addendum, 4 November 2026: step versus journey (seal predictions9 `6d92d1331db91dd35a0d1b95c455096bd635a16cf7b1d183a4108b5be7bb373e`)

- H1 RUNS: one tick has algebraic degree 4 in the lab frame, the Toffoli frame Ψ(b, c, d) = (b, b ⊕ c, d ⊕ bc) and the co-moving (T4-relative) frame.
- H2 ELSEWHERE: the largest output degree of F^t climbs about two per tick, not to 15 by t = 3. Lab and Toffoli: 4, 6, 8, 10, 11, 12 for t = 1–6, 14 at t = 8, 15 from t = 12 on. Co-moving: 4, 7, 9, 10, 11, 12, 13 at t = 8, 14 (its ceiling) from t = 12 on.
- H3 RUNS: the seed's 1,612-cycle has degree 16 in the Toffoli frame, identical to the lab frame. The Toffoli frame halves a step's affine pieces (8 → 4) and changes no degree.
- H4 RUNS: in the co-moving frame the seed's orbit closes at 806 (the H_1001 drift vanishes) with degree 14, the ceiling for an even set on 15 bits.
- Reading: a tick is cheap and the journey is algebraically maximal in every frame tried. The route is easy to walk and hard to skip.
- The C = s slice (independent audit) was read without a seal; its vacuum clock, 3,123 on the quotient, is measured.

## Addendum, 4 November 2026: rung 2 return map (seal predictions11 `fdc1f65dd42d4c10410784da994054c1c9f8c63ef1617fccae614a2e1a16824c`)

Section S = rung 2 (e_R-locked R) with w = 0; M0 = first return of F to S.
- S1 RUNS: |S| = 1,024 (256 co-moving); every state returns; M0 is a permutation and commutes with the translations. Every cycle of R meets S.
- S2 RUNS: M0 is not affine. Its largest output degree is 9 in lab coordinates (a random permutation of 10 bits: 9), 8 in Toffoli coordinates, and 7 co-moving (the ceiling on 8 bits). The section map is as nonlinear as a random permutation of the section; the w = 0 section does not carry the clock law.
- S3 RUNS: summing tau over each M0-cycle gives the F-cycle length. Long families: 30, 94, 98, 212, 434 with 6, 18, 16, 44, 90 section hits, four cycles each. Short cycles in R (2, 4, 6, 12) hit S exactly twice each.
- Return times take 13 values, 1–14; tau = 10 never occurs (observed, OPEN).
- S4 RUNS: the lag between visits to the same partner pair takes 7–20 distinct values per family, so the route word is not a fixed-lag recurrence. The mean lag is exactly 4 on every cycle (STANDS: each pair's gaps sum to the cycle length, Kac).
- Next: per-plane time reversal. The Fibonacci matrix M = [[1,1],[1,0]] satisfies S M S = M^{-1} with S the carry-cell swap, so the swap reverses a plane's write wherever that plane's constant κ is fixed (planes 0 and 1 always; plane 2 only where 1 ⊕ ℓ(x) is constant, which it is on rung 1).

## Addendum, 5 November 2026: interface versus values (seal predictions12 `9e7a7300ad4ce33a5f10a76bca183a3fc041481a1a8bf39db42802d92e6d0ed6`)

Machines on reader + carry + four paired cells (2^18 states): A1 the ring (3-bit codes), A2 the ring built with a scrambled operation table, A3 A1's run written in 4-bit words, B a J-pair partner rule, C a random reversible map, D B's outputs remapped to copy A1's value histogram. Value reader: histogram of values read. Motion reader: revisit lags read through same/different only, orbit lengths, places used.
- Value distance to A1: A2 0.026, A3 0.504, B 0.033, C 0.022, D 0.011. Motion distance: A2 0, A3 0, B 0.024, C 0.098, D 0.024.
- W1 RUNS: the three ring implementations differ by values and are identical by motion (same orbit lengths).
- W2: C RUNS (0.098; 10 of its 17 orbits odd, against 0 of 5,624 for the ring). B lands ELSEWHERE: B is the ring under other labels. Its orbit-length spectrum equals the ring's, and four XOR-respecting relabelings carry the ring's partner and mate maps exactly onto B's. The 0.024 is start noise (same machine, other starts: 0.012 and 0.049; starts carried across: 0.013).
- W3: the value reader ranks D (0.011) and the random map C (0.022) closer to the ring than the ring's own second program A2 (0.026). D is the ring too (it is B), so its motion distance is noise.
- W4 RUNS: on all 128 closed walks of A1, the average return lag equals the number of places the walk uses, exactly (Kac). Every ring orbit is even.
- W5 ELSEWHERE: the value-pair distance 0.080 between A1 and B separates two implementations of one interface.
- Correction: the earlier unsealed slice table (I three locks, J one, A two, A0 none) counted coordinate planes. The J rule at h = u is the ring relabeled and has the same two locks. The lockable directions are the linear functionals vanishing on the toggle word: two for every nonzero toggle. A0 and I admit no XOR-respecting relabeling onto the ring.

## Addendum, 5 November 2026: NOT at the Planck floor, landed on a horizon (seal predictions13 `52e37183273b9977ed7a968a96f80a5a5b0d05e127e25a025af5b299d602e64b`, 05:32 UTC)

Contract: a distinction's price rises as the distinction gets finer, and the price bends the field that has to read it. The two gradients run opposite and touch at one scale: x ≥ ħc/E and x ≥ 2GE/c⁴ meet at x* = √(2ħG/c³) = √2 ℓ_P, the form of Mead's 1964 limit. The contract fixes the form (two opposite gradients, one residue); the field supplies ħ, G, c. A horizon is a closed surface with every patch at the floor, so its smallest change is one NOT. With the field's exchange rates (S = A/4ℓ_P², first law) the sealed claims were P13.1, α = 4 ln 2 (equal binary area steps), and P13.2, lines ω_N = κ α N/(8π) + 2Ω_H.
- P13.3 STANDS: no published ringdown analysis excludes α = 4 ln 2. Laghi, Carullo, Veitch, Del Pozzo (CQG 2021, events to 1 October 2019): α = 15.6 +20.5/−13.3, log odds 0.1 ± 0.6; GW150914 alone is uninformative. The LVK GW250114 spectroscopy paper does not test quantization.
- Comb check on GW250114, RUNS (our computation on published 90% intervals, exact Kerr tones from the qnm package; remnant χ_f = 0.68 ± 0.01; measured 220 tone 0.02 ± 0.02 above Kerr). Binary comb: line spacing 4.45% of the tone; nearest line N = 6 at +1.60%, 0.33σ from the measurement (Kerr itself sits 1.65σ away). Every spin in the posterior keeps a line inside the band, so at 2% precision the binary comb cannot fail: a pass, not a confirmation. 4 ln 3: line N = 4 at +3.11%, 0.91σ. 8π: no line within 15%, nearest N = 1 at +15.2%, 10.9σ; excluded in the Foit–Kleban emission-line model.
- Laghi et al.'s best fit 15.6 lands ELSEWHERE: it is the α whose first line (N = 1) falls on the Kerr tone of a spin-0.68 remnant (N* = 1.00). The value is set by where the detected remnants sit, not by the horizon.
- P13.4 STANDS (retrodiction, known to the sealer): the Fermilab Holometer excluded Hogan's pixel-noise model; LHAASO GRB 221009A gives E_QG,1 > 10 E_Pl and E_QG,2 > 6 × 10⁻⁸ E_Pl (95%). Wherever tested, the floor behaves as a bound, not a grid. A grid whose corrections start at second order is not excluded by timing.
- OPEN: binary versus ternary. The strongest objection to the binary reading is Motl's 2002 proof that highly damped Schwarzschild tones approach T_H ln 3 (Hod's 4 ln 3). Separating 4 ln 2 from 4 ln 3 needs the 220 tone below about 1% on one remnant, or a population with spread spins, since each spin slides the comb against Kerr. Laghi et al. estimate about 20 GW150914-like events at design sensitivity.
