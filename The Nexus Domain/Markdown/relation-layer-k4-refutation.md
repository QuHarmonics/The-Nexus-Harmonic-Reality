# §19 Open Problem 1 — REFUTED, two independent engines

Written 2026-10-04. Companion notebook: `k4_counterexample.ipynb` (13 cells, executed, 0 errors).
Supersedes the search status in `relation-layer-k4-search.md`.

*The Relation Layer* §19: "Prove or refute: for 𝒦₄, at most two vertex orbits implies ε_harm = 0."

**Answer: refute.**

## Witness

    |V| = 12   |E| = 30   K = 2
    0,1 0,2 0,4 0,5 0,6 0,7 0,9 1,2 1,3 1,5 1,7 1,8 1,10 2,3 2,4 2,8 2,9 2,11
    3,4 3,5 3,6 3,9 3,10 4,5 4,7 4,10 4,11 5,6 5,8 5,11

    |Aut(X)| = 24      vertex orbits {0,1,2,3,4,5} and {6,7,8,9,10,11}  (exactly two)
    degree sequence 3^6 7^6
    arena: 66 vertices, 300 edges;  |𝒦_disj| = 291, |𝒦₄| = 1083

| quantity | 𝒦_disj | 𝒦₄ |
|---|---|---|
| dim C¹_G | 22 | 22 |
| rank d₀ | 7 | 7 |
| rank d₁ | 13 | 14 |
| ε | 15 | 15 |
| **ε_harm** | **2** | **1** |

## Why 112/112 and the extended 784 missed it

Every 𝒦_disj-nonzero case in both populations had **dim ℋ¹_G(𝒦_disj) = 1**. At dimension 1 the
spanning condition degenerates: "E has full column rank" collapses to "some λ(c) ≠ 0", which a
single added cell always satisfied. The intermediate outcome 0 < rank E < r is structurally
impossible there. The earlier evidence was a rank-1 calibration regime, not a test of the
conjecture's content.

Here dim ℋ¹_G(𝒦_disj) = 2 and **rank E = 1**: the added all-4-cycle relations kill one harmonic
direction and leave the other.

## Two independent engines

| quantity | engine 1 (orbit basis) | engine 2 (group averaging) |
|---|---|---|
| dim C¹_G | 22 | 22 |
| rank d₀ | 7 | 7 |
| rank d₁(𝒦_disj) | 13 | 13 |
| rank d₁(𝒦₄) | 14 | 14 |
| ε_harm(𝒦_disj) | 2 | 2 |
| ε_harm(𝒦₄) | 1 | 1 |
| cells 𝒦_disj / 𝒦₄ | 291 / 1083 | 291 / 1083 |

Engine 1 reduces to an orbit basis and explicitly zeroes reversible orbits per Lemma 1.2 / §1.4.
Engine 2 contains **no orbit enumeration, no canonical cell forms, and no reversibility rule**: the
invariant subspaces are the image of P = (1/|G|)Σ_g T_g on the full cochain spaces, so reversible
directions are annihilated automatically and never named. It also rebuilds the arena, both
predicates, and Aut(X) from scratch. Engine 2 independently finds 8 arena-vertex orbits with
rank d₀ = 7, consistent with a connected quotient.

This rules out the specific logic that could have fabricated the result. **Both engines are mine** —
this is not cross-author replication, and a rerun on the companion engine remains the publication
gate.

## Certificate (engine 1)

- Aut closed under composition: True
- Lemma 1.2: 44 oriented − 22 unoriented orbits = 22 = dim C¹_G
- 4-cycle count cross-check: Σ over diagonals C(codeg,2) = 2166, halved (each C₄ seen from both
  diagonals) = 1083 = enumerated
- Lemma 1.3: 𝒦_disj (291) ⊆ 𝒦₄ (1083): True
- cell orbits partition the declared cell set exactly, both predicates
- Lemma 1.4: max |d₁d₀| = 0 exactly, both predicates
- rank d₁ agrees over ℚ, mod 1000003, mod 999983, both predicates
- ε_harm by rank formula = ε_harm by nullspace dimension, both predicates
- explicit survivor h, primitive integral, with d₁(𝒦₄)h = 0 and ⟨h, d₀f⟩ = 0 exactly over ℚ:

      h = [-7529, 8433, -6200, 7917, -6191, -6625, -7141, 9807, -6155, 7963, -9419,
            6589, 6580, 7901, -7999, 6588, -6208, -6579, -5267, 9791, -6217, 7999]

## What the refutation does and does not touch

- **Refuted**: ≤2 vertex orbits ⟹ ε_harm(𝒦₄) = 0. Also the full-column-rank form of the spanning
  conjecture.
- **Untouched**: Theorem 10.3 monotonicity — 1 ≤ 2 holds. Theorem 10.1's certificate is correctly
  *silent* here: ε = 15 = dim C²_G(𝒦_disj), not strictly greater, so this is a genuine rank
  deficiency in d̄₁ and not a counting shortage. rank d₁ rises by only 1 (13 → 14) while two
  harmonic directions were present — a linear dependence among the added relations, not a shortage
  of relation coordinates.
- **Strengthened**: Corollary 12.1. Neither declared predicate forces vanishing on a two-orbit
  substrate; the relation layer matters under both.

## Scope

Not isolated. In the 12-vertex 6+6 block-rotation family at K=2, **96 of 264** cases with
ε_harm(𝒦_disj) ≥ 2 have ε_harm(𝒦₄) > 0. The counterexamples sit at |Aut| = 24; the |Aut| = 6 cases
with ε_harm(𝒦_disj) = 3 and 4 all vanished under 𝒦₄. So neither "more symmetry helps" nor "less
symmetry helps" survives — orbit count and |Aut| are screening variables, not mechanisms.

## Next theorem-shaped question

Which two-orbit substrates have added-cell evaluation map E : ℋ¹_G(𝒦_disj) → ΔC²_G of deficient
rank? Candidate routes: characterize the linear dependencies among rows of E; decompose
ℋ¹_G(𝒦_disj) under the order-24 group and identify which summand the all-4-cycle relations fail to
see; compare the |Aut|=24 failing family against the |Aut|=6 vanishing family at the level of E's
rank profile rather than group order.

## Dead ends (from the prior search, still dead)

Intrinsic cell shape; orbit size (one-sided only); primitive gcd / rank-1 Smith form (held in 8 of
120 cases, coincidence). The surviving normalization-independent constraint from the rank-1
population — nonzero |λ| ratios always {1} or {1,2} — is untested above rank 1.

## Not established

Nothing physical. ε_harm is dim ℋ¹_G under a declared predicate, per §18.
