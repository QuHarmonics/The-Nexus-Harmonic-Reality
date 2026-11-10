# NEXUS §160 — The planar singularity and the closure reader

**Dean A. Kulik — QuHarmonics Research Group — ORCID 0009-0003-3128-8828**

## Provenance and scope

Derived from the two previously reported §159 nonrigid, full-chain end-window witnesses. This addendum does not modify the published papers or §159. It identifies the analytical conditions that must be proved before the numerical puckering trajectories can be promoted to exact continuous returns. Both computations below are retrospective, using the exposed source words. The two predictions were SHA-256 sealed in their respective execution scripts before each numerical/symbolic evaluation.

## Exact domain contract

The seven-bond window consists of eight beads `p_i,...,p_{i+7}` and six moving interior beads `p_{i+1},...,p_{i+6}`. Both window endpoints are fixed. Only one endpoint has an adjacent fixed exterior bond because the other endpoint is a physical chain terminus. The six interior valence angles and one flanking angle are fixed at 120 degrees; there is no bond-angle constraint at the free end terminus.

In ordinary Cartesian moving coordinates `X∈R^18`, define fourteen **quadratic** constraints:

- Seven bond constraints: `F_b(X) = ||p_{b+1}-p_b||² − 1 = 0` for `b=i,...,i+6`.
- Seven valence constraints: `F_j(X) = (p_{j-1}−p_j)·(p_{j+1}−p_j)+1/2 = 0` at the six internal vertices and the one flanking vertex.

The exterior bead positions are constants. The exact way home is to reverse an admissible path inside `F^-1(0)` and read back the starting framed word.

## Exact planar-Jacobian result

The Jacobian is `J = DF(X_0)` of shape `14×18`. At either flat honeycomb endpoint every derivative with respect to an out-of-plane coordinate is identically zero. The 12 in-plane columns have exact rank 12, so

`rank J = 12`, `nullity J = 6`, `dim ker J^T = 2`.

This was calculated over the rationals in the lattice basis with Gram matrix `[[1,1/2,0],[1/2,1,0],[0,0,1]]` for both:

- `00001111011010110110111100`, window `i=0`;
- `00111101101101011011110000`, window `i=20`.

At a **regular** nonplanar point, if `rank J=14`, the implicit-function theorem supplies a local `18−14=4` dimensional manifold. The planar point is *not regular*; that theorem cannot be invoked there directly. In particular, the six-dimensional planar tangent space is not proof of a six-dimensional local solution manifold.

## The first missing link is at second order

Let `z=(z_1,...,z_6)` be a candidate initial out-of-plane displacement. Write an exact constrained path near the source as `X(t)=X_0+t Z+t²Y+O(t³)`, where `Z` inserts `z` only into the six height coordinates. Expansion of the quadratic constraints gives the necessary equation

`JY + q(z) = 0`,

where `q(z)` has seven entries `(z_{b+1}−z_b)²` for bond constraints and seven entries `(z_{j-1}−z_j)(z_{j+1}−z_j)` for angle constraints. Set all fixed-bead heights to zero.

Since `dim ker J^T=2`, the necessary **branch compatibility conditions** are

`ell_1^T q(z)=0` and `ell_2^T q(z)=0`.

The two exact rational quadratic forms for each representative are printed by `NEXUS_160_planar_branch_quadratic.py`. They are independent second-order necessary conditions; they do not by themselves prove a real nontrivial branch. A constrained continuation from an arbitrary z-kick is not justified without this interface or an equivalent validated singular-branch argument.

## Correct torsional interface

There are seven angular placement controls for the seven-bond end arc when rooted at its **one fixed flanking exterior bond**: one initial azimuth for the first generated bead and one each for the next six generated beads. They can be parameterized as `theta ∈ T^7`; this fixes all seven lengths and seven prescribed bond angles by forward kinematics. The opposite window endpoint imposes *three more equations*:

`E(theta) = p_terminal(theta) − p_terminal_fixed = 0 ∈ R^3`.

A regular solution of these three equations gives a `7−3=4` dimensional admissible family. But naive torsion interpolation `theta(t)=(1−t)theta_start+t theta_target` preserves local lengths and angles **only**; it generally fails `E(theta(t))=0` and moves the fixed exterior endpoint. Therefore interpolating torsions is not already a fixed-exterior certificate.

**Correction to the quoted proposal:** it refers to a “6-bead chain” and six internal dihedrals, which omits the actual eight-bead arc and its flanking-axis azimuth. The seven-variable closure formulation above counts all angular controls and all fixed-exterior conditions.

## Second-derivative bound must be redefined

For an **internal** bond connecting two movable bead coordinates, the Hessian of `||q−p||²−1` is

`[[2 I_3, −2 I_3], [−2 I_3, 2 I_3]]`,

whose spectral norm equals **4**, not 2. Thus the proposed universal `M=2` bound is false in ordinary Cartesian coordinates even for one component of `F`. A vector-valued second-derivative bound, in a named norm and local chart, must be computed explicitly; norm conversions cannot be skipped.

## What a valid manifold certificate must supply

1. An *exactly identified* nontrivial branch through **each** singular planar endpoint. The second-order conditions above are a necessary entrance test, not the whole proof.
2. Overlapping regular charts on the nonplanar route, with a nonsingular `14×14` selected Jacobian minor and interval bounds on its inverse and derivative.
3. Interval-Newton/Krawczyk inclusions that establish an exact constrained solution in each chart and certify overlap/continuation to the target branch; no claims based solely on residuals at snapshots.
4. Whole-chain, nonincident segment distance enclosures. If every bead on a certified curve segment stays within `h` of the sample and the sampled bond clearance is `c`, then the true segment clearance is at least `c−2h`.
5. The reversed curve must return to the original exact endpoint; the complement-pair route is obtained by conjugation with the global proper half-turn.

The prior numerical evidence is strong: the two §159 traces reach endpoint distance below `1e−7`, residuals below `1e−13`, and sampled whole-chain clearance 1. But §159's `0.959451` and `0.964478` bounds rigorously describe *piecewise-linear positional interpolants*, which need not lie on the exact constraint manifold.

## Ledger status

- **STANDS:** 14 quadratic constraints in 18 moving coordinates; two exact left-null conditions on second-order out-of-plane branches; internal bond-constraint Hessian norm 4; torsion closure is an independent three-coordinate endpoint condition.
- **RUNS (retrospective):** exact rank 12 and nullity 6 for both planar representatives; two exact rational branch-compatibility quadratic forms for each.
- **OPEN:** existence and certification of the connecting nonplanar fixed-exterior branch, a validated continuation enclosing the existing numerical witnesses, and positive clearance over the *constraint-preserving* continuum.

No random kicks, arbitrary new arc words, long loops, or plotting were used in these checks.
