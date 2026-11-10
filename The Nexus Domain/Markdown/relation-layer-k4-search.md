# 𝒦₄ two-orbit conjecture — independent engine, 6× larger verified pool, mechanism still open

Written 2026-10-04. Target: *The Relation Layer* §19 open problem — "Prove or refute: for 𝒦₄, at
most two vertex orbits implies ε_harm = 0."

## Engine

Rebuilt from §1.1–1.5 alone, sharing no code with the companion notebooks. Exact rational ranks
(Fraction Gaussian elimination), no floating point.

**Calibration before use — every published anchor reproduces:**

| check | paper | this engine |
|---|---|---|
| Q₃, K=3 cell counts | 𝒦_disj 168, 𝒦₄ 306 | 168, 306 |
| paw (ε, dim C²_G, ε_harm) | 0, 0, 0 | 0, 0, 0 |
| bull | 2, 1, 1 | 2, 1, 1 |
| bull ε_harm, both predicates, K=2 and 3 | 1 in all four | 1 in all four |
| wheel W₆ at K=3 | 3, 3, 0 | 3, 3, 0 |
| connected graphs on 6 vertices | 112 | 112 |
| §12 counterexample \|Aut\|, orbits, degrees | 8, {0,2,5,6}/{1,3,4,7}, 4⁴5⁴ | identical |
| §12 rank table, K=2 𝒦_disj | dim C¹=14, r₀=6, r₁=7, ε=8, ε_harm=1 | identical |
| §12 rank table, K=2 𝒦₄ | 14, 6, 8, 8, 0 | identical |
| §12 rank table, K=3 𝒦_disj | 32, 9, 22, 23, 1 | identical |
| §12 rank table, K=3 𝒦₄ | 32, 9, 23, 23, 0 | identical |

Note: the Theorem 10.1 table's W₆ row is at K=3, not K=2. At K=2 the same graph gives ε=1, which
is the value §14 quotes. Both are correct; the table mixes K.

## Search

Monotonicity (Thm 10.3 + Lemma 1.3) gives ε_harm(𝒦₄) ≤ ε_harm(𝒦_disj), so every 𝒦₄
counterexample is first a 𝒦_disj counterexample. Screen on 𝒦_disj, test survivors under 𝒦₄.

- **6 vertices, exhaustive.** 112 connected graphs → 23 with ≤2 vertex orbits → 46 cases at K=2,3.
  Zero nonzero under either predicate. Consistent with the paper's 86/86 stage.
- **8 vertices, group-invariant generator.** Graphs invariant under ⟨2×4-block rotation⟩,
  ⟨rotation + block swap⟩, ⟨8-cycle⟩; filtered to ≤2 Aut-orbits; K = 2, 3, 4.
  **672 two-orbit cases. 120 with ε_harm(𝒦_disj) > 0. Zero with ε_harm(𝒦₄) > 0.**

So the 𝒦₄ vanishing statement now survives roughly 784 cases (the paper's 112 plus these 672), and
the population of 𝒦_disj counterexamples it has to beat rose from 8 to 128. Still a finite verified
range, not a theorem.

Every one of the 120 new 𝒦_disj counterexamples has ε_harm = 1 exactly. Two distinct regimes
appear: at K=2, ε=5 > dim C²_G(𝒦_disj)=4, so Theorem 10.1's counting certificate applies; at K=3
(ε=17, dim C²=25) and K=4 (ε=22, dim C²=34) it does not, and the deficit is a genuine rank
shortfall in d̄₁.

## Mechanism hunt — attempted and failed

On the §12 counterexample at K=2 there are 30 G-orbits of 4-cycles in 𝒦₄ ∖ 𝒦_disj.
**12 of the 30 individually suffice to kill the harmonic class**; 18 do not.

First classification attempt failed. Killers and non-killers have *identical* values for the two
coarse invariants tried: distinct base edges per cell (4 for both) and base-vertex support size
(4 for both). Orbit size does not separate them either — both groups contain orbits of size 8.
So the separating invariant is finer than the base-edge multiset, and is not yet identified.

That is the open edge: a proof of the 𝒦₄ conjecture needs the structure the paper says it needs
("it cannot follow from vertex-orbit count alone"), and the discriminator between killer and
non-killer extra cells is the concrete form of that structure.

## Next

1. Finer classification of the 12 killer orbits: which token moves at each step (one token
   traversing a base 4-cycle vs two tokens alternating), and the induced 4-edge subgraph type
   (4-cycle vs triangle-plus-pendant).
2. Push the search to 9 and 10 vertices with the same generator.
3. If the killer family turns out to be canonically present whenever ≤2 vertex orbits, that is the
   theorem.

## Not established

- The 𝒦₄ conjecture. 784 verified cases is not a proof, and the 86/86 that preceded the 𝒦_disj
  counterexample is the standing reminder.
- Nothing physical. ε_harm is dim ℋ¹_G under a declared predicate, per §18.
