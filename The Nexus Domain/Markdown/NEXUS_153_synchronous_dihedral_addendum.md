# NEXUS §153 — A continuous clearance certificate for the two-angle return

**Dean A. Kulik — QuHarmonics Research Group — ORCID 0009-0003-3128-8828**

## Input and domain
The already-published §151/§152 list of 28 self-avoiding 26-turn honeycomb words is linked as validation data, not as newly discovered data. An allowed candidate is the flip of the fourth turn from either end, provided the endpoint word is valid. This is a zero-thickness fixed-unit-bond lattice-chain model, not a molecular force field.

## The exact route
Two consecutive bond-axis 180-degree turns compose to the single-turn XOR mask `e_j = D_j xor D_(j+1)` (or its prefix equivalent). For the continuously synchronized implementation, choose the angles `(θ, σθ)` for `0 ≤ θ ≤ π`, `σ ∈ {−1,+1}`. The original word and the recovered word differ at exactly turn bit `j`. The inverse traverses θ from π back to 0. For a front-end move the final *laboratory* coordinates need not equal the canonical first-bond anchoring; exact return must be checked in turn coordinates or up to a rigid transformation.

## From sample to full-sweep clearance
For the fourth-turn end gate, a bead moves around two instantaneous rotation axes. Its distances to these axes are at most 3 and 4 unit bonds, respectively. Thus, along the synchronous angular path,

    || d p_i / dθ || ≤ 3 + 4 = 7.

For any pair of points (whether on moving or fixed bond segments), the relative speed is at most 14, and minimum nonincident segment separation `d(θ)` is 14-Lipschitz:

    |d(θ)−d(φ)| ≤ 14 |θ−φ|.

Sampling θ_k=kπ/90 leaves any angle at most π/180 from a sample. Hence if all sampled nonincident segment clearances are ≥d*, then

    min_(0≤θ≤π) d(θ) ≥ d* − 14π/180.

For sampled `d*=1.0`, this is **0.755653904721** bond units, uniformly through the entire sweep. This is a conservative bound and presumes the floating-point sample-distance computation is reliable; a strict machine-checked proof would use directed rounding or exact interval arithmetic.

## Executed finite audit

- Previously published m=26 residual words: **28**.
- Endpoint-valid 4-bead gates at the two ends: **36**.
- Gates with at least one sampled-clear synchronous route: **36/36**.
- Minimum over *selected* routes of sampled segment clearance: **1.0**.
- Continuous conservative lower bound: **0.755653904721** bond units.
- Previously reported serial planar-intermediate failures among these gates: **8** (not independently recomputed in this script).
- Previously reported all-widths m=23–26 result: **46 locked words, 68 endpoint-valid gates, 56 serially executable**. These wider figures come from the supplied transcript, not the §153 independent audit.
- **Conditional stronger inference from the uploaded m=23–26 sweep**: the reported smallest sampled clearance across *either sign choice* is 0.654730484419, and across co-rotating choices is 0.913131901651. With the same angular mesh and Lipschitz bound, even the worse reported trajectory has conservative full-sweep lower bound **0.410384389140** bond lengths, and the co-rotating family has bound **0.668785806372**. This extrapolation is conditional on the numerical clearance implementation and the 4-bead movement geometry for those 68 gates. It is not independently reproduced in this 28-word script.

## Correction log
1. The first independent run incorrectly compared front-end-lifted laboratory coordinates directly to coordinates generated with the conventional first-bond anchor. It failed on one valid `j=3` case. The frame-invariant inverse turn-word test agrees exactly; both sign choices lead to the original target turn word. This is a coordinate-frame correction, not a changed physical path.
2. In the pasted transcript, the sentence “68 (matches 56!)” conflates endpoint-valid gates with serially executable gates. The table says **68 = 56 + 12**, not 68=56.
3. “68/68 synchronous counter-rotating” is too broad: the code checks `max(clearance_same, clearance_opposite)`, so it demonstrates **at least one of the two sign choices** for each gate, not counter-rotation alone. Reported minima across *all* opposite and same sign routes are 0.65473 and 0.91313 respectively, both positive in the sampled test; these are separate from the chosen-route minimum of 1.
4. The previous §152 endpoint-only theorem applies to **one rigid half-turn from planar endpoints**. It does not, on its own, establish the safety of the coupled synchronous two-axis move; the derivative/mesh argument supplies that missing reasoning here.

## Ledger
**STANDS:** The two-mirror mask identity, the explicit inverse, the 14-Lipschitz separation bound for the stated four-bead end model, and a positive conservative full-sweep bound conditioned on correct numerical sampled distances.

**RUNS:** Exact turn-word recovery and numerical full-sweep certificate on all 36 endpoint-valid gates across the 28 published m=26 words.

**OPEN:** Chemical bond thickness/side chains, non-honeycomb conformational freedom, energy barriers and rates, steric interactions beyond the zero-thickness model, and any demonstrated protein-folding mechanism or quantum advantage.
