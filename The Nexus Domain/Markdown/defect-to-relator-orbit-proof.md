# §93 continuation: the defect-to-relator-orbit calculation

## Result

For the three-cell witness, the six-letter relation

\[
R=(CT^2)^2=1
\]

closes the entire five-dimensional loop defect left by \(C^3=1\) and \(u^2=1\), where \(u=C^{-1}T\). The result can be stated in two complementary forms: an algebraic proof of the resulting group order, and an exact chain-rank certificate showing how the relation orbit fills the specific \(H_1\) defect.

## Algebraic identity

Since \(T=Cu\) and \(C^3=1\),

\[
CT^2=C(Cu)(Cu)=C^{-1}uCu.
\]

Put \(v=C^{-1}uC\). Since \(u^2=v^2=1\),

\[
(CT^2)^2=(vu)^2=1 \iff vu=uv.
\]

Thus the hexagon is precisely the neighboring-lamp commutation relation in the \(C,T\) alphabet. Conjugating it by \(C\) supplies the other cyclic neighboring pairs. Together with \(u^2=1\), all three conjugate lamp flips commute, so there are at most \(3\cdot 2^3=24\) elements. The ordinary three-lamp action realizes all 24 head/tape configurations. Hence the presented group has exactly 24 elements and is \(C_2\wr C_3\cong C_2\times A_4\).

## Exact chain-rank certificate

Represent the 24 states as \((h,b)\), where \(h\in\mathbb Z/3\mathbb Z\) is the head location and \(b\in\mathbb F_2^3\) is the tape. Let \(C\) advance the head and let \(T\) flip the bit under the head, then advance. The graph has 24 vertices and 48 oriented move edges. It is connected, so its cycle space has dimension

\[
48-(24-1)=25.
\]

Using signed edge chains and exact rational row rank, the boundary ranks are:

| Relation faces | Distinct faces | Boundary rank |
|---|---:|---:|
| \(C^3\) triangles | 8 | 8 |
| \(u^2\) squares | 12 | 12 |
| Both families together | 20 | 20 |
| \((CT^2)^2\) hexagons | 12 | 12 |
| All three families together | 32 total distinct faces | 25 |

Therefore the first two families leave \(25-20=5\) independent cycles, and the hexagon orbit adds rank \(25-20=5\) modulo the prior boundaries. The residual defect is completely killed.

This is stronger than a rank-only result. The audit also extracts a \(25\times25\) minor of determinant \(-1\). With rows ordered as the 24 triangle starts, then 24 square starts, then 24 hexagon starts, the selected zero-based row indices are

```text
0,1,2,3,4,5,6,7, 24,25,26,27,32,34,36,38,40,41,44,45, 48,49,56,58,64
```

With edge columns ordered as \((x,C),(x,T)\) for each state index \(x=0,\ldots,23\), the selected zero-based edge-column indices are

```text
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14, 16,18,20,22,24,26,32,34,36,38
```

The determinant is exactly \(-1\). These 25 face boundaries form a primitive rank-25 sublattice of the integral edge-chain group. Since they lie in the rank-25 integral cycle kernel, they form an integral basis of that kernel. This gives an independently checkable unimodular certificate for complete closure.

The word \(q=CT^2\) is a head-fixed double flip and \(q^2=1\). Since \(R=q^2\) has period three as the word \(CTTCTT\), starting the same face at \(q(x)\) gives the same face. Its stabilizer is \(H=\langle q\rangle\) of order two, so its face orbit has \(|G|/|H|=12\) faces and carries the permutation module \(\operatorname{Ind}_H^G\mathbf1\) in the ledger's face convention.

## The static/dynamic bridge on this witness

This graph is not an arbitrary 24-vertex drawing. Let

\[
F=F(C,u),\qquad P_0=\langle C,u\mid C^3,u^2\rangle\cong C_3*C_2,
\]

and let \(\phi:P_0\twoheadrightarrow G=C_2\wr C_3\) be the transition action on the 24 head/tape states. Because \(C\) has order three, \(u\) has order two, and their conjugates generate all three lamp flips, this map is onto and \(|G|=24\). Let \(L=\ker\phi\). Then \(L\) has index 24 in \(C_3*C_2\).

The subgroup \(L\) is torsion-free: every finite-order element of \(C_3*C_2\) is conjugate into one of its finite factors, and the map is injective on each factor. By the subgroup theorem for free products, a torsion-free subgroup is free. Using \(\chi(C_3*C_2)=1/3+1/2-1=-1/6\) and multiplying Euler characteristic by index,

\[
\chi(L)=24(-1/6)=-4=1-\operatorname{rank}(L),
\qquad\boxed{L\cong F_5}.
\]

So the five-dimensional loop defect is not only a numerical remainder. It is the abelianization of the exact free kernel left by the first two stored relations:

\[
D\cong L_{\mathrm{ab}}\otimes\mathbb Q
\cong\mathbb Q^5
\cong 2^-\oplus3a.
\]

This is the bridge the two presentations were missing. The transition system determines \(G\) and its word kernel; the partial presentation determines which part of that kernel has already been declared. The graph's 25 cycles are the rank-25 free kernel of the unpresented two-generator action. Attaching the triangle and square orbits leaves the rank-5 kernel \(L\). The chain calculation sees its abelianization; the free-product calculation identifies the full group kernel.

Finally, the algebraic proof above shows \(P_0/\langle\!\langle R\rangle\!\rangle\cong G\). Therefore \(R\) normally generates all of \(L\), not merely its abelianization. The hexagon closes the exact group-level gap; the unimodular chain certificate independently shows how its finite face orbit kills the five homological directions.

A reader then performs a separate quotient. If \(\pi:X\to Y\) is a readout and

\[
x\sim_\pi y\iff\forall g\in G,\quad \pi(gx)=\pi(gy),
\]

the continuation equivalence is \(G\)-invariant. Because the action on the 24 configurations is regular, the address space is a transitive quotient \(X/\!\sim_\pi\cong G/H_\pi\) for the stabilizer subgroup \(H_\pi\) of the address of the base state. A state-separating reader gives \(H_\pi=1\) and retains 24 addresses; a coarser reader may merge them. This address quotient is not the five-dimensional residual. The residual measures the missing relations in the partial presentation; the reader quotient measures which already-defined states remain distinguishable under future observations.

## What the symmetry calculation proves

Over the complex numbers, Frobenius reciprocity gives

\[
\operatorname{mult}_{V_\chi}(\mathbb C[G/H])=\dim(V_\chi^H).
\]

The ledger's \(2^-\) is a rational two-dimensional type whose complexification is the conjugate pair of one-dimensional characters of order three, twisted by the central sign. Because a double flip lies in \(V_4\), both complex characters are trivial on \(H\); each occurs once, together giving one rational \(2^-\) channel. In \(3a\), a nonidentity double flip has eigenvalues \(1,-1,-1\), so its fixed space is one-dimensional and that channel also occurs once. Thus the 12-dimensional face-orbit module contains the full defect type \(2^-\oplus3a\), of dimensions \(2+3=5\).

The criterion proves eligibility, not closure. For the actual relator, the standard Fox-derivative convention \(\partial(uv)=\partial u+u\partial v\), with \(q=CT^2\) and \(R=q^2\), gives

\[
\frac{\partial R}{\partial C}=1+q,\qquad
\frac{\partial R}{\partial T}=(1+q)(C+CT).
\]

The factor \(1+q\) is the algebraic source of the stabilizer filter: on an irreducible channel it annihilates any component with no \(q\)-fixed vector, while it acts as twice the identity on the \(q\)-fixed component. That predicts which channels the hexagon boundary can touch. The exact edge-boundary rank calculation supplies the remaining sufficiency certificate: the induced boundary map has rank five, the full dimension of the defect, so its projections jointly cover both components.

## General form of the missing-line criterion

Let \(D=Z_1(\Gamma^{(1)};\mathbb Q)/B_{\mathrm{stored}}\) be the residual loop module of the graph 1-skeleton after quotienting by the stored face boundaries, and let \(F_H=\mathbb Q[G/H]\) be a candidate relation-face orbit. Its actual boundary induces a \(G\)-equivariant map

\[
\bar\partial_R:F_H\longrightarrow D.
\]

The candidate closes the defect exactly when \(\bar\partial_R\) is surjective. The representation condition

\[
\dim(V_\chi^H)>0
\quad\text{for every complex constituent }V_\chi\text{ of }D
\]

is necessary, but not sufficient by itself. If a constituent occurs with multiplicity greater than one, the induced map must have full rank on its multiplicity space as well. In this witness the target channels each occur once, and the unimodular boundary certificate proves the map reaches both of them jointly.

For a relator of the form \(R=q^m\), the Fox derivatives contain the norm factor \(N_q=1+q+\cdots+q^{m-1}\): \(\partial R/\partial x=N_q(\partial q/\partial x)\). When the represented action satisfies \(q^m=1\), this norm operator is \(m\) times the projection onto the \(q\)-fixed subspace. Thus the stabilizer filter is not a post-hoc description: it is present in the boundary operator algebra itself. For this witness, \(m=2\) and \(N_q=1+q\). This provides a precise finite theorem behind the phrase “the hole names the third line.”

## Scope

This proves the defect/relator claim for the specified 24-state witness and the defined move alphabet. It does not prove that every relation deficit in every field can be completed by a relator orbit chosen solely from its representation profile. That broader selection principle requires a general theorem that includes both the stabilizer eligibility condition and a nonzero/surjective boundary-map condition.

The accompanying `defect_relator_orbit_audit.py` reconstructs the stated action and checks all boundary ranks with exact rational arithmetic.
