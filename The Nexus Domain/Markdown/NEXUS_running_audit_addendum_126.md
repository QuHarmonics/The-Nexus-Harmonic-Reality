# NEXUS Running Audit Addendum §126 — ASK THE RINGS: the WP5 lockstep link

**Date:** 17 October 2026  
**Upstream path:** §121 rational-ring decompile → §123 difference compiler → §124 BBP/SHA execution → §126 joint-orbit reconstruction.  
**Executable:** `nexus_ask_the_rings_lockstep.py`  
**Pre-run prediction SHA-256:** `b706f2ac615ca016ad985c7e513cc73d2e20139d1583d47ddeaed8db13ea8c8e`

## Correction to the starting point

The prior §125 `ASK THE RINGS` run enumerated de Bruijn transitions on low-dimensional SHA slices and compared ordered endpoint pairs with endpoint-XOR readouts. That is a valid side-projection experiment, but it was not the unresolved ring link in WP5 §121 and did not advance the stated build order. This addendum returns to WP5's actual lane transformation: each rational ring is split by CRT into a reader ring and a field ring, then the phase relationship between those two rings is retained.

The compiler-side BBP/SHA link is already recorded in §124. This run does not recalculate or reopen it.

## The exact joint orbit

For an eligible WP5 partial lane, let `d = 8k+j`, let `o` be the odd part of `d`, and let `y_t = a·16^t mod o` be the original rational-ring orbit. Set

\[
 h=\operatorname{ord}_{o}(16),\quad
 \epsilon=16^{h/2}\bmod o,\quad
 o_1=\gcd(\epsilon-1,o),\quad o_2=o/o_1.
\]

The `o1` parent is the **reader ring** and the `o2` parent is the **field ring**. With the respective CRT inverses, the two normalized coordinates at the same original phase are

\[
 \alpha_t=\frac{y_t(o_2^{-1}\bmod o_1)\bmod o_1}{o_1},\qquad
 \beta_t=\frac{y_t(o_1^{-1}\bmod o_2)\bmod o_2}{o_2}.
\]

Write `h1 = ord_o1(16)`, `h2 = ord_o2(16)`, and `g = gcd(h1,h2)`. The paired orbit is

\[
 J=\{(\alpha_{t\bmod h_1},\beta_{t\bmod h_2}):0\le t<\operatorname{lcm}(h_1,h_2)\}.
\]

Its period is exactly `lcm(h1,h2)`. In phase coordinates, the reachable pairs are exactly those satisfying `i ≡ j (mod g)`. There are `h1*h2/g` such pairs. If `g=1`, that is the full Cartesian product and the independent-ring factorization is justified. If `g>1`, the actual orbit is a phase-constrained subset; replacing it with the full product changes the owner of the average.

The exact lane lean is read along the synchronized joint route:

\[
 L_J=\frac{1}{|J|}\sum_{(\alpha,\beta)\in J}
 \left(\alpha-\mathbf 1[\beta<\alpha]\right)=\mu-\frac12.
\]

This is not a generic lane-wise Boolean/Toffoli analogy. It is WP5's rational-ring CRT decompile, using the same original lane orbit and preserving which reader-ring phase is paired with which field-ring phase.

## Execution results

All **10/10** run invariants passed using exact rational arithmetic. Reconstructing the original WP5 eligibility filter recovered the recorded population: 804 eligible partial lanes; 75 balanced; 692 independent-period lanes, of which 66 balanced; 112 lockstep lanes overall; and exactly 9 balanced lockstep lanes.

For all 804 eligible lanes, the mean from the reconstructed synchronized CRT route equals the original rational-ring `mu - 1/2` exactly. The joint-orbit period matches `lcm(h1,h2)` for all 804, and every reachable phase pair satisfies the modulo-`g` relation.

For the nine balanced lockstep cases, the joint route gives exact lean `0` in **9/9**. The hypothetical full Cartesian-product average disagrees with the true joint-route average in **5/9** cases. In the other four it happens also to be zero, but that coincidence does not restore the missing phase relation.

| k | j | a | d | odd modulus `o` | reader `o1` | field `o2` | `h1` | `h2` | `g` | joint period | Cartesian lean | joint lean |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 313 | 5 | 1 | 2509 | 2509 | 13 | 193 | 3 | 24 | 3 | 24 | 1/36 | 0 |
| 630 | 4 | 4 | 5044 | 1261 | 13 | 97 | 3 | 12 | 3 | 12 | 0 | 0 |
| 703 | 5 | 1 | 5629 | 5629 | 13 | 433 | 3 | 18 | 3 | 18 | -1/18 | 0 |
| 757 | 6 | 8 | 6062 | 3031 | 7 | 433 | 3 | 18 | 3 | 18 | 1/27 | 0 |
| 824 | 4 | 4 | 6596 | 1649 | 17 | 97 | 2 | 12 | 2 | 12 | 0 | 0 |
| 1009 | 6 | 8 | 8078 | 4039 | 7 | 577 | 3 | 36 | 3 | 36 | -1/27 | 0 |
| 1297 | 1 | 1 | 10377 | 10377 | 9 | 1153 | 3 | 72 | 3 | 72 | 1/108 | 0 |
| 1634 | 1 | 1 | 13073 | 13073 | 17 | 769 | 2 | 96 | 2 | 96 | 0 | 0 |
| 1640 | 4 | 4 | 13124 | 3281 | 17 | 193 | 2 | 24 | 2 | 24 | 0 | 0 |

The per-step `y`, `alpha`, `beta`, phase indices, and exact lean term for every one of these nine full joint orbits are in `NEXUS_ASK_THE_RINGS_lockstep_results.json`.

## Ledger

| Claim | Status |
|---|---|
| WP5 lane eligibility is reproduced at `k ≤ 2000` | RUNS, 804/804 |
| Joint period is `lcm(h1,h2)` and phase pairs obey `i ≡ j (mod gcd(h1,h2))` | RUNS, all 804 eligible lanes |
| Joint CRT route returns the original rational-ring lean exactly | RUNS, 804/804 |
| The 692 coprime-period lanes reduce to the independent Cartesian-product result | RUNS, 692/692 |
| The nine balanced lockstep lanes have exact joint lean zero | RUNS, 9/9 |
| Full-product substitution changes the lean in five of the nine balanced lockstep cases | RUNS, 5/9 |
| General density law for balanced partial lanes | OPEN; this finite link does not solve it |
| Digest-only SHA inverse / minimum root observer | OPEN; unaffected by this run |

## Artifacts

- `nexus_ask_the_rings_lockstep.py` — executable exact reconstruction.
- `NEXUS_ASK_THE_RINGS_lockstep_results.json` — every lockstep route and exact phase/lean term, plus all 804 lane checks.
- `NEXUS_ASK_THE_RINGS_lockstep_run.md` — run report and nine-case table.
- `NEXUS_ASK_THE_RINGS_lockstep_prediction_2026-10-17.txt` and `.sha256` — pre-run seal.
- `wp5_checks.py`, the WP5 manuscript and the §§121/124 source records are included in the bundle for lineage.
