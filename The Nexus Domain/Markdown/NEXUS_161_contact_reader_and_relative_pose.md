# NEXUS §161 — The contact reader is not a six-DOF clamp

**Dean A. Kulik — QuHarmonics Research Group — ORCID 0009-0003-3128-8828**

## Purpose and scope

The §160 POV-to-overhead instruction is the serial product `G_b = G_a g_{a+1}...g_b` in `SE(3)`. A new H–H contact is a relationship in that existing spatial field. Before assigning it the type of a rigid `SE(3)` loop closure, read the exact constraint that a pair of interacting beads supplies. This note uses a pre-existing m=10 HP witness, not a new candidate search. It does not alter any published paper.

## 1. Three distinct types of contact

**Observed HP contact:** Two nonconsecutive H beads occupy neighboring honeycomb sites. This is a property of a discrete configuration; in the HP energy model it is an energetic contribution, not a mechanically immutable bond. A conformational move can make or break such a contact.

**Hard point-distance contact (idealized bar):** Two bead centers satisfy `F_ab(φ) = ||p_b(φ) − p_a(φ)||² − d_ab² = 0` at every instant. This is one scalar equation. At a regular point with a nonzero independent Jacobian row it removes one continuous degree of freedom. It is not an orientation constraint.

**Rigid dock:** The complete relative pose is fixed, `G_a(φ)^{-1} G_b(φ) = H_* ∈ SE(3)`. This is generically six scalar conditions (three translations and three orientations), not implied by a single point contact. It requires additional independent constraints or an explicit mechanical docking assumption.

For a single first contact joining two originally separate chain components, the graph gains an edge but no cycle. An intrachain contact or a second independent connection between already-connected components adds a graph cycle. Neither fact by itself imposes six independent holonomic constraints.

## 2. Contact Jacobian and reader

For a torsion φ_j about a unit bond axis `u_j` through `o_j`, with a fixed upstream bead a and a downstream bead b,

`∂p_b/∂φ_j = u_j × (p_b − o_j)`.

Therefore the one-contact Jacobian entry is exactly

`∂F_ab/∂φ_j = 2 (p_b − p_a)·[u_j × (p_b − o_j)]`.

An arbitrary fixed-distance contact produces **one row** in the torsion Jacobian. Several contacts lower the generic dimension by the *rank of their combined rows*, not necessarily by their number. At a planar configuration with all relevant rotation axes lying in the plane, the infinitesimal out-of-plane motion makes this first derivative zero; second-order compatibility may still obstruct a path.

## 3. A pre-existing HP witness, derived and executed

Published test word: `1000010010`, with sequence `HHPHPPHHPPHP` and the H–H contact between beads 1 and 6. In Cartesian coordinates, with the first bond east:

- `p_1 = (1,0,0)`;
- `p_2 = (3/2,−√3/2,0)` and `p_3 = (5/2,−√3/2,0)`;
- `p_6 = (3/2,√3/2,0)`.

Hold beads 0..3 fixed and rotate the suffix 4..11 by angle θ around the existing covalent bond p_2→p_3. All covalent bond lengths and all valence angles are preserved identically. The transformed contact bead is

`p_6(θ) = (3/2, −√3/2 + √3 cosθ, √3 sinθ)`.

Subtraction gives the exact relation

`||p_6(θ) − p_1||² = 4 − 3cosθ`.

At θ=0 the squared contact distance equals 1; at θ=π/3 it equals 5/2. The first derivative is `3sinθ`, hence zero at the flat configuration, whereas the second derivative equals 3. If an exact unit-distance bar is imposed, *this one-torsion trajectory* cannot move off θ=0 without violating that bar. If the H–H attraction is a soft energy, the motion is kinematically allowed but changes the energy. In either case, reversing θ returns exactly to the original chain.

The executed audit prints three θ samples, numerical errors below `4e−16`, and the recovered geometry. The analytic identity holds for the entire sweep independent of those samples.

## 4. Strictly interior loop geometry and contact rank

For a strictly interior k-bond exchange arc, hold both exterior parts fixed and move k−1 internal beads: `3(k−1)` Cartesian coordinates. Preserve k unit lengths and k+1 bond angles: `2k+1` scalar equations. **If those constraints have full row rank at a regular solution**, the dimension is

`dim M_k = 3(k−1) − (2k+1) = k−4`.

Thus k=5, 6, 7 have generic dimensions 1, 2, 3, reproducing the earlier §158 dimension ledger. Adding r independent hard-contact equations yields local dimension `k−4−r` if the combined Jacobian remains regular and the resulting set is nonempty. An intrachain graph cycle need not be a *fixed relative SE(3) pose*. The boundary-angle and endpoint-position constraints already have their own closure type; substituting six independent frame conditions would overconstrain this particular model.

At flat honeycomb endpoints the Jacobian can lose rank, so neither generic dimension counting nor an infinitesimal tangent-nullspace certificate proves a connecting branch. For actual 6R/7R/8R interior exchanges, one must identify source and target on one regular/validated singular branch and check collision clearance throughout.

## 5. Compiler type ledger

| WHAT | WHERE / readout | Disposition |
|---|---|---|
| Local step and torsion stream | Running product G_0 g_1 ... g_k | STANDS |
| Contact observed in an HP lattice configuration | Boolean adjacency / HP energy | STANDS, not a hard constraint |
| Idealized persistent H–H contact | Scalar equation F_ab=0 and its Jacobian row | STANDS |
| H–H separation under the published one-torsion m10 witness | `4−3cosθ` | RUNS; exact geometric derivation |
| Generic interior-loop DOF for k=5,6,7 | `1,2,3` under full regular rank | STANDS conditionally |
| Exact rigid dock between frames | Full pose equation in SE(3) | Different constraint type |
| Continuous collision-free strictly interior nonrigid 10-/12-/14-cycle exchange | Verified fixed-exterior manifold branch + clearance bound | OPEN |
| General multichain assembly with soft contacts | Potential energy and transition dynamics | OPEN |

**Way home:** reverse the torsion trajectory and release/restore the designated contact constraint; no global frame has to be redefined. The new hole is not an unknown bit mask, but **which constraint row the physical contact actually writes**.

## 6. Prediction seal and correction log

Pre-execution analytic prediction seal SHA-256: `c0b34365fab0da4c3ce697a80bc7a3cb02b7f265ababa8ae7c1347e7f58ea8ff`. This was sealed after the published witness was known and before running the finite test; it is not a blind discovery. First execution used exact floating-point equality for an irrational-coordinate unit distance and halted. The assertion was corrected to a `1e−12` numerical tolerance; the sealed prediction was not changed.
