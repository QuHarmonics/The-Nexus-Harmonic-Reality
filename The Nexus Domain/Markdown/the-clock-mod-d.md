# The period, the components, and the clock mod d

Written 2026-10-04. Follows `claude/c1-is-the-abrams-hypothesis.md`. Two results, one of them a
lemma with a one-line proof that also serves as an independent check on the period computation.

## 1. Terminology correction: which cover has which deck group

Earlier phrasing said "the cover has deck group ℤ" without saying which construction. Corrected:

- The **skew-product** cover on V × ℤ, with (v,m) → (w, m + h(e)), **decomposes into d connected
  components** when Per(h) = dℤ.
- Restricting to one component gives the **connected cyclic cover** associated with ker φ_h, whose
  deck group is naturally dℤ ≅ ℤ.

Verified by BFS on the skew product (window ±3d), counting how many of (0,0), (0,1), …, (0,d−1)
lie in the component of (0,0), and confirming (0,d) does:

| substrate | group | d | components | (0,d) ~ (0,0) |
|---|---|---|---|---|
| C₅ K=2 | ℤ₅ | 5 | 5 | yes |
| C₅ K=2 | 1 | 5 | 5 | yes |
| C₆ K=2 | ℤ₆ | 6 | 6 | yes |
| C₇ K=2 | ℤ₇ | 7 | 7 | yes |
| C₇ K=2 | 1 | 7 | 7 | yes |
| C₈ K=2 | ℤ₈ | 8 | 8 | yes |
| 12v witness | 1 | 9 | 9 | yes |

Components = d on every row.

## 2. The period depends on the group, and the two witness figures are both right

A confusion worth recording because it looked like a contradiction. The witness's period is
**22587 under Aut(X)** (|Aut| = 24) and **9 under the trivial group**. Neither is an error; they
are periods of different cochains on different spaces. An invariant cochain assigns one value to a
whole G-orbit of edges, so a loop closing the generator must cross whole orbits and picks up a
correspondingly larger period.

So Per(h) is a function of (X, K, G, 𝒦), not of the substrate alone. Any statement of a period
must name the group.

## 3. Lemma: h mod d is exact — a single-valued clock always exists

**Lemma.** Let Per(h) = dℤ with d > 0 on a connected arena. Then h mod d is exact: there is
U : V → ℤ/d with U(w) − U(v) ≡ h(v→w) (mod d) on every oriented edge.

*Proof.* Every closed loop has circulation in dℤ, hence ≡ 0 mod d. A ℤ/d-valued cochain whose
periods all vanish is exact on a connected graph: fix U(v₀) = 0 and define U(v) by the circulation
along any path, which is path-independent mod d. ∎

Verified by BFS-propagating U and then checking **every** edge independently — exact on every row
above, including the witness under both groups.

| substrate | group | d | h mod d exact | image of U |
|---|---|---|---|---|
| C₅…C₈ | ℤ_n and 1 | n | yes | all n values |
| 12v witness | Aut | 22587 | yes | 24 values |
| 12v witness | 1 | 9 | yes | 9 values |

The witness-under-Aut row is the odd one: the clock takes only 24 of its 22587 available residues.
24 is also |Aut(X)|. **Recorded as an observed coincidence, not a claim** — 24 does not divide
22587, the arena has 7 vertex orbits rather than 24, and no mechanism has been checked.

### This also pins the period exactly

The lemma gives a mutual verification that resolves §2 rigorously. The computed d is a gcd of
observed periods, so d_true | d. The clock being exact at d means d divides every period, so
d | d_true. Hence **d = d_true**. The clock check is therefore not a decoration; it independently
confirms the period computation, and a wrong d would have produced an inconsistent U.

## 4. What this says about the "shaped absence"

The sharpest statement so far, and it is now a theorem rather than a picture:

> The hidden potential is not absent. It is present as an ordinary single-valued potential **mod
> d**. What is missing is exactly the lift of that clock from ℤ/d back to ℤ.

So the absence has a size, and the size is computable: the residual class is the obstruction to
lifting a ℤ/d-valued function to a ℤ-valued one. Two base paths v → w always land on sheets
differing by an element of dℤ — the attainable displacement set is D_h(v,w) = c(v,w) + dℤ, a
one-line consequence of the fact that two such paths differ by a loop — and c(v,w) mod d is
exactly U(w) − U(v). The base arena collapses d classes of history into one visible endpoint, and
d is the number.

That is the precise content of "a merge may be a quotient-induced halt of distinction rather than
a union": the merge is genuine iff the clock values agree, which they always do, and the lift
values differ, which is what the base cannot see.

## 5. What was deliberately not folded in

A large body of framing material arrived with this: the interface-first inversion
(food-interface before metabolism, machine schemas across chemistry, thermodynamics, nuclear
reactors, computation, ecology, institutions), the shared-library-and-local-shapes picture, the
need-as-trajectory-functional proposal, and the defense of structural metaphor.

None of it is in this file, for a stated reason: restating one pattern across seven domains is
cataloguing, and cataloguing is not the work. The inversion may well be right, but a framing that
fits everything predicts nothing until it produces a domain-specific measurable that separates a
working implementation from a failing one. The one genuinely computational item in that batch —
the false-merge test — is §4 above, and it reduced to a lemma.

The need-functional proposal (𝔑 = (A, 𝒦, G, h, ℓ, ℱ, ℛ, Π)) is a reasonable shape for a later
paper. It is not started here because nothing in it has been run.
