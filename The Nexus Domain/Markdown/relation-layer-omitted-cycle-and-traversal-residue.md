# Two species of invariant harmonic residue

Written 2026-10-04. Supersedes `claude/relation-layer-odd-cycle-blind-spot.md`, whose central
claim is refuted here. Follows `claude/relation-layer-k4-refutation.md`, which stands unchanged.

Notebook: `two_species_residue.ipynb` — 16 cells, executed from scratch, zero errors, exact
rational arithmetic throughout, two independent engines.

## The claim that died

Last round's mechanism doc asserted the §19 survivor was an **odd-cycle blind spot** of a
4-cycle-only predicate, and posed as the next falsifiable question whether any
ε_harm(𝒦₃₄) > 0 exists. Both halves resolved, and not in that doc's favour.

**Refuted.** For C_n with n even, at K = 2 and 3, the arena is **bipartite** — it contains no
odd cycle of any length — and yet ε_harm(𝒦₄) = 1. The class is first detected at length n,
which is even. Parity was never the operative property. **Omission from the declared cell
family** is.

| substrate | K | arena bipartite | odd arena cycles | ε_harm(𝒦₄) | L_closure |
|---|---|---|---|---|---|
| C₆ | 2 | yes | none | 1 | 6 |
| C₈ | 2 | yes | none | 1 | 8 |
| C₁₀ | 2 | yes | none | 1 | 10 |
| C₁₂ | 2 | yes | none | 1 | 12 |
| C₆ | 3 | yes | none | 1 | 6 |
| C₈ | 3 | yes | none | 1 | 8 |

**Answered, affirmatively.** ε_harm(𝒦₃₄) > 0 exists. The witness is the cycle graph, the
simplest nontrivial graph there is. Both arena 3-cycle types require a base triangle
(verified computationally), so on a triangle-free base 𝒦₃₄ = 𝒦₄ exactly, and C_n is
triangle-free.

## The dichotomy that replaces it

**Vocabulary residue.** L_closure bounded. The declared cell family was missing a cycle
shape the substrate has. Admit the shape and the class evaporates; the substrate never
moved. The §19 witness is this: L_closure = 4.

**Traversal residue.** L_closure tracks the substrate size. No fixed vocabulary 𝒦_{≤L}
reads it once the substrate exceeds L. It is H¹ of the configuration space itself. C_n is
this: L_closure = n, unbounded.

L_closure — the shortest relation depth that separates every surviving invariant
circulation class — separates the two, and is computable. This is the apparent-vs-genuine
flatness distinction, measured rather than asserted.

| | 12v witness | C₇ (ℤ₇) | C₉ (ℤ₉) | C₁₀ (ℤ₁₀) |
|---|---|---|---|---|
| base triangles | 20 | 0 | 0 | 0 |
| ε = dim C¹_G − rank d₀ | 15 | 3 | 4 | 4 |
| ε_harm(𝒦_disj) | 2 | 1 | 1 | 1 |
| ε_harm(𝒦₃) triangles only | 3 | 3 | 4 | 4 |
| ε_harm(𝒦₄) squares only | 1 | 1 | 1 | 1 |
| ε_harm(𝒦₃₄) both | **0** | **1** | **1** | **1** |
| L_closure | **4** | **7** | **9** | **10** |

The families are **not nested**, and the earlier doc got L_closure wrong by conflating
detection with closure. On the witness, triangles *alone* leave 3 of the 15 open and squares
*alone* leave 1; only the union closes it. So L_closure = 4, not 3.

## What the C_n class is

The surviving class is the **exchange of two indistinguishable tokens**. Verified by
tracking token labels around the generator: for C₅…C₈ at K = 2 the shortest
nonzero-circulation loop has length n and returns the configuration to its start with the
two token labels swapped.

UConf₂(S¹) is an open Möbius band, H¹ = ℤ, and the class is its half-twist. For general K,
UConf_K(S¹) ≃ S¹, which is why ε_harm = 1 at every K rather than growing — confirmed at
K = 2, 3, 4.

L_closure = n is a clean step function: ε_harm(𝒦_{≤L}) = 1 flat from L = 4 through L = n−1,
then 0 at L = n. Verified n = 5…10 at K = 2 and n = 6, 7 at K = 3.

**The group matters too, not only the cell vocabulary.** Trivial G and the rotation subgroup
ℤ_n both carry the class. The **full dihedral group destroys it** — a reflection reverses the
generator's orientation and sends it into a reversible orbit, so C¹_G never contains it.
Every full-dihedral row across n = 5…12, K = 2, 3 gives ε_harm = 0.

## The witness's mechanism, correctly stated

Not "triangles see what squares miss." Sharper:

**Triangles read the residue at full rank; the entire square vocabulary reads half of it.**

Rank of each family's circulation map on the 2-dimensional ℋ¹_G(𝒦_disj):

| family | cells | rank d₁ | rank on ℋ¹_G(𝒦_disj) |
|---|---|---|---|
| 3-cycle, spectator (token parked, other walks a base triangle) | 180 | 10 | **2** |
| 3-cycle, rotation (3 base edges, no parked token) | 20 | 2 | **2** |
| 3-cycle, all | 200 | 12 | **2** |
| 4-cycle, spectator (token parked, other walks a base 4-cycle) | 528 | 8 | 1 |
| 4-cycle, commuting (2 base edges, independent) = 𝒦_disj | 291 | 13 | 0 |
| 4-cycle, rotation (4 base edges, no parked token) | 264 | 7 | 1 |
| 4-cycle, all | 1083 | 14 | **1** |
| 5-cycle, all | 5688 | 15 | 2 |

Three structurally distinct square shapes; two of them are nonzero readers; the union still
reads **rank 1**. They see the same line. Meanwhile **20 rotation triangles**, one per base
triangle, read rank 2 — the whole residue. The minimal complete reader is 20 cells of a shape
Definition 1.3 excludes, since it demands four distinct arena vertices.

That is the rank deficiency named in the refutation certificate, now localized.

## Cross-checks that passed

- **Independent recovery of 𝒦_disj.** Classifying all 1083 arena 4-cycles by move-multiset
  yields exactly 291 commuting squares with rank d₁ = 13 — matching `cells_disj` by a route
  that never enumerates base-edge pairs.
- **Arena 3-cycle count formula.** Predicted 20·(12−3) spectator + 20 rotation = 200;
  enumerated 200.
- **im d₀ has zero circulation on every arena cycle** of length 3, 4, 5. PASS.
- **Triangle-free ⟹ zero arena 3-cycles.** Verified on C₅, C₆, C₇, C₉ at K = 2 and C₆, C₈ at
  K = 3, so the 𝒦₃₄ = 𝒦₄ collapse is not assumed.
- **Companion engine.** 24 rows of (NV, NE, dim C¹_G, rank d₀, ε, #4-cells, rank d₁, ε_harm)
  agree exactly between the orbit/reversibility engine and the projector engine, which never
  classifies an orbit and never applies a reversibility test. 0 disagreements.

## Status, stated carefully

- **Established**: ε_harm(𝒦₃₄) > 0 exists, with an explicit infinite family. L_closure = n for
  C_n. The odd-cycle reading is false. The witness's residue is triangle-complete and
  square-rank-deficient. Both engines agree on all of it.
- **Not a theorem**: that every harmonic residue is one of exactly these two species, or that
  vocabulary residue has a uniform L_closure bound. The dichotomy is a measured distinction
  with two populated sides, not a classification theorem.
- **Definitional caveat, unchanged and still load-bearing**: arena 3-cells are *not* 2-cells
  under §1.3 as written. Admitting them extends the complex to mixed-size cells. That is a
  legitimate generalization, not a third predicate inside the existing family, and any
  writeup must say so.
- **Supersedes nothing in the refutation**: §19 Open Problem 1 remains refuted on the
  evidence already certified, independent of this mechanism.

## The next question, sharply posed

The old axis (which two-orbit substrates fail) was wrong, and so was its replacement (odd
cycles). The live question:

> Is L_closure bounded whenever the arena is simply connected — i.e. is all vocabulary
> residue closed at some universal depth, with everything beyond that depth accounted for by
> configuration-space topology?

The topological side is now known to be real and unbounded. Whether the vocabulary side
admits a uniform bound is open, and it is a question about token arenas generally, not about
the one witness.

## Not established

Nothing physical. ε_harm is dim ℋ¹_G under a declared predicate, per §18. "Reader" and
"residue" here are names for a rank computation, not claims about physical observers.
