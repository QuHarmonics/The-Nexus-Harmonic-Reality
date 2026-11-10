# NEXUS §159 — The end-window return and the full-chain reader

**Dean A. Kulik, QuHarmonics Research Group — ORCID 0009-0003-3128-8828**

## Scope and provenance

This section audits the user-supplied 46-word residual lock catalogue at turn widths 23–26. Its initial data, exchange definitions, and reported 20 numerical motions were already exposed in the uploaded pasted transcript before this independent check. Thus this is **retrospective ownership/reproduction**, not a blind predictive landing. The published papers are untouched.

## The typed hole

The previous report showed a 3D return for isolated 12-/14-cycle windows. The missing readout was the *complete-chain embedding*: a lawful exchange endpoint must admit a continuous 3D motion whose moving bonds do not collide with any stationary bond. The source words and opposite arcs are fixed. No candidate word search is needed.

For each word `x` and arc length `k=6` (12-cycle) or `k=7` (14-cycle), `exchange(x,k)` specifies a legal alternative honeycomb arc with the same two endpoint vertices. Its way home is the reverse arc exchange, while the continuous way home is the reverse geometric trajectory.

## Independent discrete census

| Turn width | Residual locks in catalogue | With a 12-cycle exchange | With a 14-cycle exchange | Distinct locks reached by either |
|---|---:|---:|---:|---:|
| 23 | 4 | 0 | 0 | 0 |
| 24 | 4 | 0 | 0 | 0 |
| 25 | 10 | 0 | 0 | 0 |
| 26 | 28 | 4 | 12 | **12** |

At width 26 there are exactly **20 exchange instances**, belonging to **12 distinct source words**. These comprise **8 rigid** chord-axis 180-degree returns and **12 nonrigid** arc replacements. Every instance is at an *end* window: `i=0`, `20`, or `21`. Consequently none tests the fully interior two-fixed-exterior interface.

## Subtract the available return

Eight of the twelve source words possess an **exact** rigid-body half-turn return. For each such replacement, all internal arc vertices coincide with the rigidly rotated start vertices and all exterior vertices are fixed. In the zero-thickness planar-endpoint setting the half-turn clearance identity gives the minimum entire-sweep separation from the two endpoints. Full-chain endpoint clearance is one bond length in all eight.

The remaining four sources have no rigid 12-/14-cycle return in the measured catalogue. They form two complement pairs:

| Independent representative | `C`-partner |
|---|---|
| `00001111011010110110111100` | `11110000100101001001000011` |
| `00111101101101011011110000` | `11000010010010100100001111` |

Complement is a **proper 3D half-turn of the complete framed chain**. It preserves all bond distances, and maps the route of either representative onto that of its partner. Therefore only two geometrically independent numerical pucker cases remain.

## Continuation replay and bridge

The two representative returns were rerun independently with **analytic constraint Jacobians**. All constrained waypoints preserve squared unit lengths and 120-degree bond angles to the printed residuals; the fixed opposite exterior was not moved.

| Reproduced measurement | First pair representative | Second pair representative |
|---|---:|---:|
| End-to-target Euclidean norm | 9.941e-8 | 9.978e-8 |
| Largest constraint residual in continuation | 7.772e-15 | 8.238e-14 |
| Minimum sampled clearance across **every** nonadjacent bond pair in full chain | 1.000000 | 1.000000 |
| Continuation step count | 579 | 484 |
| Largest single-bead move per continuation step | 0.02027 | 0.01776 |
| Projected source-to-seed bridge waypoints | 200 | 200 |
| Largest single-bead move per bridge step | 0.000856 | 0.000691 |
| Largest bridge residual | 2.98e-13 | 2.89e-13 |
| Minimum sampled bridge clearance | 1.000000 | 1.000000 |

The bridge begins at the **exact** planar start; its first projected nonplanar point lies only 0.001278 and 0.001132 away (Euclidean norm over all moving coordinates). Thus the earlier jumps of 0.255 and 0.222 between start and perturbation seed have now been resolved into many individually checked, close constrained snapshots.

### A separate whole-interpolation clearance bound — not a constrained-chain proof

Let `c` be the minimum full-chain separation among nonadjacent bond segments at every sampled frame, and let `h` be the largest displacement of **any single bead** between consecutive frames. Under straight-line interpolation of each bead's coordinates, any point on a bond moves by at most `h`; hence the distance between any two bonds changes by at most `2h`. Consequently the **piecewise-linear positional interpolant** has minimum clearance at least `c − 2h`, over its *entire* continuous sweep, not merely its samples.

For the two reproduced puckers, the lower bounds are approximately `0.959451` and `0.964478` bond lengths; for their source-to-seed bridges they are `0.998288` and `0.998618`. These positive bounds certify nonintersection of that explicit *unconstrained positional interpolation*. They do **not** certify that unit bond lengths and 120-degree valence angles remain exact between snapshots (linear interpolation generally perturbs them). The exact-constraint continuous return therefore remains OPEN.

The uploaded 20-route trace also contains four **low-clearance alternative** puckering paths with sampled minima `0.1547`, `0.0342`, `0.1061`, `0.000322`. All four corresponding source words independently possess *rigid* alternative routes with exact whole-sweep clearance. These low-clearance alternatives cannot be used as collision-free certificates.

A geometric interpolation between sampled configurations can be shown collision-free under a displacement bound, but *linear interpolation generally violates bond-length and angle constraints*. Positivity at finitely many exact-constraint snapshots plus short steps therefore remains numerical evidence, not a mathematically certified continuous solution curve in the exact configuration manifold.

## The Omega islands

`m=8`: `00111100 → 11000011` is a full complement (mask `11111111`), a rigid half-turn; it joins the two four-word islands but does not connect them to the 208-word component. `m=12`: `001111000010 → 110000110010` complements only the first eight turn bits and contains hexagon windows `0110` at index 5 and `1001` at index 7, furnishing new local exits. This mechanism explains the different connectivity effect reported in §158, without claiming a 3D route for all other words at higher widths.

## Ledger status

- **STANDS:** Arc-swap inverse; rigid chord-axis half-turn identity and full-sweep endpoint-clearance theorem; complement as proper 3D spatial rotation. The reduction from four nonrigid-only words to two complement pairs is exact.
- **RUNS (prior-exposed checks, rerun for ownership):** 46 catalogue words, 20 exchanges over 12 words at m=26, eight rigid identities, two nonrigid numerical witnesses, and their 200-waypoint start bridges. These are retrospective executions, not new prediction landings.
- **OPEN:** Proof of a connected exact-constraint path between the projected numerical waypoints and the exact target for both nonrigid representatives; robust formal segment-clearance bounds on that path; any *fully interior* fixed-two-exterior embedding theorem; general widths beyond the catalogue; finite steric thickness and dynamical rates.

**Way home:** reverse each rigid half-turn, reverse each numerically traced pucker and its start bridge (approximate until full continuity is certified), and reverse the discrete arc swap. The complementary partner returns by conjugating the same route with `C`.
