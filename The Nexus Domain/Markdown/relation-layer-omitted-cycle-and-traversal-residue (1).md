# Two species of invariant harmonic residue

Written 2026-10-04. Supersedes `claude/relation-layer-odd-cycle-blind-spot.md`, whose central
claim is refuted here. Follows `claude/relation-layer-k4-refutation.md`, which stands unchanged.

Notebook: `two_species_residue.ipynb` — 18 cells, executed from scratch, zero errors, exact
rational arithmetic throughout, two independent engines.

## The claim that died

The earlier mechanism doc asserted the §19 survivor was an **odd-cycle blind spot** of a
4-cycle-only predicate, and posed as the next falsifiable question whether any
ε_harm(𝒦₃₄) > 0 exists. Both halves resolved, and not in that doc's favour.

**Refuted.** For C_n with n even, at K = 2 and 3, the arena is **bipartite** — no odd cycle of
any length exists in it — and yet ε_harm(𝒦₄) = 1, first detected at even length n. Parity is
not the operative property. **Omission from the declared cell family** is.

| substrate | K | arena bipartite | odd arena cycles | ε_harm(𝒦₄) | L_closure |
|---|---|---|---|---|---|
| C₆ | 2 | yes | none | 1 | 6 |
| C₈ | 2 | yes | none | 1 | 8 |
| C₁₀ | 2 | yes | none | 1 | 10 |
| C₁₂ | 2 | yes | none | 1 | 12 |
| C₆ | 3 | yes | none | 1 | 6 |
| C₈ | 3 | yes | none | 1 | 8 |

**Answered, affirmatively.** ε_harm(𝒦₃₄) > 0 exists. The witness is the cycle graph. Both
arena 3-cycle types require a base triangle (verified computationally), so on a triangle-free
base 𝒦₃₄ = 𝒦₄ exactly, and C_n is triangle-free.

## The operative variable: rank access, not cell count

Not "triangles see what squares miss." Sharper: **triangles read the residue at full rank; the
entire square vocabulary reads half of it.** For any declared family 𝓡, the datum that matters
is rank E_𝓡 where E_𝓡 : ℋ¹_G(𝒦_disj) → C²_G(𝓡) records circulation — not |𝓡|.

| family | cells | rank d₁ | rank E on ℋ¹_G(𝒦_disj), dim 2 |
|---|---|---|---|
| 3-cycle, spectator (token parked, other walks a base triangle) | 180 | 10 | **2** |
| 3-cycle, rotation (3 base edges, no parked token) | 20 | 2 | **2** |
| 3-cycle, all | 200 | 12 | **2** |
| 4-cycle, spectator (token parked, other walks a base 4-cycle) | 528 | 8 | 1 |
| 4-cycle, commuting (2 base edges, independent) = 𝒦_disj | 291 | 13 | 0 |
| 4-cycle, rotation (4 base edges, no parked token) | 264 | 7 | 1 |
| 4-cycle, all | 1083 | 14 | **1** |
| 5-cycle, all | 5688 | 15 | 2 |

**1083 relations supply one independent constraint on the residue; 20 supply two.** The three
square shapes do not contribute partial pieces that combine: spectator and rotation squares have
the *same image*, verified directly as the line spanned by (1, −1/2) in the chosen basis, equal
to the image of the whole 1083-cell family. The minimal complete reader is 20 rotation triangles,
one per base triangle, of a shape Definition 1.3 excludes by demanding four distinct arena
vertices.

That is the rank deficiency named in the refutation certificate, now localized:
rank E_{𝒦₄} = 1 < 2 = dim ℋ¹_G(𝒦_disj). Not a shortage of cells, of shapes, of orbits, or a
parity effect.

## Detection is not closure

The families are **not nested**, and the earlier doc got L_closure wrong by conflating the two.
On the witness, triangles *alone* leave 3 of the 15 open and squares *alone* leave 1; only the
union closes it. Triangles have full rank access to the 𝒦_disj residue *and* fail to close the
rest of the ε = 15 space. So L_closure = 4, not 3.

| | 12v witness | C₇ (ℤ₇) | C₉ (ℤ₉) | C₁₀ (ℤ₁₀) |
|---|---|---|---|---|
| base triangles | 20 | 0 | 0 | 0 |
| ε = dim C¹_G − rank d₀ | 15 | 3 | 4 | 4 |
| ε_harm(𝒦_disj) | 2 | 1 | 1 | 1 |
| ε_harm(𝒦₃) triangles only | 3 | 3 | 4 | 4 |
| ε_harm(𝒦₄) squares only | 1 | 1 | 1 | 1 |
| ε_harm(𝒦₃₄) both | **0** | **1** | **1** | **1** |
| L_closure | **4** | **7** | **9** | **10** |

## The traversal class, identified rather than likened

Token exchange *suggests* the Möbius half-twist. Suggestion is not identification, so the
chain was made checkable rather than the sentence softened.

**Step 1 is a definition, not an analogy.** At trivial G,
ε_harm = dim C¹ − rank d₀ − rank d₁ = dim ker d₁ − dim im d₀, which is simplicial H¹ of the
2-complex over ℚ. And 𝒦_disj — vertices = K-subsets, edges = single token moves, 2-cells =
pairs of base edges with disjoint closed supports — is exactly the cell structure of Abrams'
discrete configuration space UD^K(X). So
ε_harm(𝒦_disj | G trivial) = dim H¹(UD^K(X); ℚ) by definition.

**Step 2 is a cited theorem with a checked hypothesis.** Abrams' Theorem A, as stated by
Prue–Scrimshaw: for a graph with at least n vertices, 𝒞ⁿ(G) deformation retracts onto 𝒟ⁿ(G) if
**(A′)** each path connecting distinct essential vertices has length ≥ n+1, and **(B′)** each
homotopically essential path connecting a vertex to itself has length ≥ n+1. (Prue–Scrimshaw
improve (A′) to n−1 via discrete Morse theory; (B′) unchanged.)

For C_n every vertex has degree 2, so there are **no essential vertices**, (A′) is vacuous and
the improvement is irrelevant. The only homotopically essential loop is the whole cycle, length
n, so **(B′) reduces to n ≥ K+1**.

**Step 3 is the measurement, including the boundary.** ε_harm(𝒦_disj | trivial G) = 1 on every
admissible (n, K) for n = 3…10, K = 2…n−1 — 33 rows — and **0 at K = n**, where every vertex is
occupied, no token can move, the discrete model collapses to a point, and (B′) fails while
UConf_n(S¹) is still ≃ S¹. The hypothesis is sharp here, so this is a test the identification
could have failed and did not.

**Step 4 is the equivariant degree, solved exactly.** For the spanning class h, solving
g*h = λh + d₀f as an exact linear system gives **λ = +1 for every rotation and λ = −1 for every
reflection**, across C₅–C₉ at K = 2, 3 — 20 rows, all consistent. Hence H¹ invariants are rank 1
under ℤ_n and **0 under the full dihedral group**. The dihedral column is therefore not an
observation; it is a rank-1 space carrying a −1 action. The group matters as much as the cell
vocabulary: same substrate, same cells, rank 1 under ℤ_n and 0 under D_2n.

**What is cited vs. run, kept apart.** The homotopy equivalence UD^K ≃ UConf_K is Abrams'
theorem, used with its hypothesis verified, not reproved. The descent of the retraction from
ordered to unordered configurations is the standard free-quotient argument. UConf_K(S¹) ≃ S¹ is
classical. Contributed here: the measured rank across the whole admissible range, the sharpness
at the boundary, and the exact equivariant degree. **An explicit chain-level isomorphism is
still not written down.**

## The two regimes

Two experimentally populated regimes, not an exhaustive classification.

| | Vocabulary residue | Traversal residue |
|---|---|---|
| representative | 12-vertex §19 witness | C_n |
| L_closure | 4 | n |
| obstruction | incomplete rank access of a declared family | global traversal unreadable below length n |
| repair | admit the omitted bounded-length family | admit a substrate-scale relation |
| uniform finite vocabulary | succeeds | cannot succeed uniformly over n |

L_closure — the shortest relation depth that separates every surviving invariant circulation
class — separates them and is computable. Bounded L_closure says the flatness was apparent and a
longer reader dissolves it. L_closure tracking the substrate says it was genuine: there is no
shorter address.

## Cross-checks that passed

- **Independent recovery of 𝒦_disj.** Classifying all 1083 arena 4-cycles by move-multiset
  yields exactly 291 commuting squares with rank d₁ = 13 — matching `cells_disj` by a route that
  never enumerates base-edge pairs.
- **Arena 3-cycle count formula.** Predicted 20·(12−3) spectator + 20 rotation = 200;
  enumerated 200.
- **im d₀ has zero circulation on every arena cycle** of length 3, 4, 5. PASS.
- **Triangle-free ⟹ zero arena 3-cycles.** Verified on C₅, C₆, C₇, C₉ at K = 2 and C₆, C₈ at
  K = 3, so the 𝒦₃₄ = 𝒦₄ collapse is not assumed.
- **Abrams boundary.** 33 admissible rows at 1, every K = n row at 0, zero disagreements.
- **Equivariant degree.** 20 rows, exact solve, all consistent, all ±1 as predicted.
- **Companion engine.** 24 rows of (NV, NE, dim C¹_G, rank d₀, ε, #4-cells, rank d₁, ε_harm)
  agree exactly between the orbit/reversibility engine and the projector engine, which never
  classifies an orbit and never applies a reversibility test. 0 disagreements.

## Status

- **Established**: ε_harm(𝒦₃₄) > 0 exists, with an explicit infinite family. L_closure = n for
  C_n in the tested range. The odd-cycle reading is false. rank E_△ = 2 > 1 = rank E_□ on the
  witness, with the two nonzero square types sharing one image. The Abrams identification holds
  across its hypothesis and fails at its boundary. The equivariant degree is ±1 as computed.
- **Not a theorem**: that every harmonic residue is one of exactly these two species; that
  vocabulary residue has a uniform L_closure bound; an explicit chain-level isomorphism to the
  configuration-space generator.
- **Definitional caveat, unchanged and still load-bearing**: arena 3-cells are *not* 2-cells
  under §1.3 as written. Admitting them extends the complex to mixed-size cells — a legitimate
  generalization, not a third predicate inside the existing family, and any writeup must say so.
- **Supersedes nothing in the refutation**: §19 Open Problem 1 remains refuted on the evidence
  already certified, independent of this mechanism.

## The next question, sharply posed — the bounded-closure problem

> Give structural conditions on a family (X, K, G) under which every invariant harmonic residue
> is annihilated by a relation vocabulary of uniformly bounded cycle length — equivalently, a
> uniform L with ε_harm(𝒦_{≤L}) = 0 throughout the family.

C_n shows the obstruction is real, with sup_n L_closure(C_n, K) = ∞, so any bounded-closure
theorem must exclude or quotient out the configuration-space traversal component. Note the care
point: H₁(A_K(X); ℚ) = 0 does not automatically give H¹_G(𝒦_{≤L}) = 0 at bounded L, since the
declared system need not span all null-homologous cycles at a uniformly bounded local scale.

## Sources

- Abrams' theorem and the improved subdivision bound: Prue & Scrimshaw, *Abrams's stable
  equivalence for graph braid groups*, https://arxiv.org/abs/0909.5511
- Background on discretized graph configuration spaces: Abrams & Ghrist, *Finding topology in a
  factory: configuration spaces*, https://arxiv.org/html/math/0009118v1
- Later work on the stabilization bound: *Abrams' stabilization theorem for no-k-equal
  configuration spaces on graphs*, https://arxiv.org/abs/2407.07854

## Not established

Nothing physical. ε_harm is dim ℋ¹_G under a declared predicate, per §18. "Reader" and
"residue" here are names for a rank computation, not claims about physical observers.
