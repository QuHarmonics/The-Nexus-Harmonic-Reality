# The harmonic sector is the odd-cycle blind spot of a 4-cycle-only predicate

Written 2026-10-04. Follows `claude/relation-layer-k4-refutation.md`. This is the mechanism the
three earlier dead ends were circling.

## What the survivor actually is

The §19 counterexample's surviving harmonic class was deconstructed by locating the shortest arena
cycle with nonzero circulation. It is a **3-cycle**:

    [0,1] -> [1,9] -> [1,2] -> [0,1]        circulation = -22587

One token sits at vertex 1; the other walks 0 → 9 → 2 → 0. All three steps are base edges, so
**{0, 2, 9} is a triangle in the base graph.**

Both declared predicates are 4-cycles only. §1.3: "a cyclic sequence (A, B, C, D) of four distinct
arena vertices." Neither 𝒦_disj nor 𝒦₄ contains a single 3-cell. A class carried by base-graph
triangles is therefore invisible to both **by construction, not by accident**.

## Measured

| substrate | K | 𝒦_disj | 𝒦₄ | 𝒦₄ + arena 3-cells | base triangles |
|---|---|---|---|---|---|
| the 12-vertex witness | 2 | 2 | 1 | **0** | 20 |
| §12 counterexample (8v) | 2 | 1 | 0 | **0** | 12 |
| **bull** (Thm 8.1 minimal witness) | 2 | 1 | 1 | **0** | 1 |
| Q₃ (bipartite) | 3 | 0 | 0 | **0** | 0 |

The bull is the decisive row. Theorem 8.1 names it the minimal graph with ε_harm ≠ 0 under *both*
predicates — |V| = 5, |Aut| = 2, ε = 2, ε_harm = 1 at K = 2 and 3. It is a triangle with two
pendants, and arena 3-cells close it.

Q₃ is the control from the other side: bipartite, zero triangles, zero harmonic sector under both
predicates.

## The reframe

§19 asked whether two vertex orbits forces ε_harm(𝒦₄) = 0. The orbit count was never the variable.
The 4-cycle-only relation family has a systematic blind spot at odd cycles, and in every case
tested the harmonic sector *is* that blind spot.

The 12-vertex witness is then not a pathological graph. It has 20 base triangles arranged so the
4-cycle relations reach only one of its two harmonic directions. Structure of the witness:

- the degree-7 part {0,…,5} is exactly the octahedron K(2,2,2) — K₆ minus the perfect matching
  (0,3), (1,4), (2,5)
- {6,…,11} is an independent set of degree-3 vertices
- each degree-3 vertex attaches to three octahedron vertices, and in all six cases those three
  **include an antipodal pair** — 6→{0,3,5}, 7→{0,1,4}, 8→{1,2,5}, 9→{0,2,3}, 10→{1,3,4}, 11→{2,4,5}

## Status, stated carefully

- **Established**: the surviving class has nonzero circulation on an arena 3-cycle coming from a base
  triangle; adding arena 3-cells drives ε_harm to 0 in all four cases tested, including the bull.
- **Not a theorem**: four cases. The clean 0,0,0,0 is suggestive. Theorem 10.3 monotonicity
  guarantees the direction of the change, not that it reaches zero.
- **Definitional caveat**: arena 3-cells are *not* 2-cells under §1.3 as written, which requires four
  distinct arena vertices. Admitting them extends the complex to cells of mixed size. That is a
  legitimate generalization but a change to Definition 1.3, not a new predicate inside it. Any
  writeup must say so rather than presenting 𝒦₃₄ as a third predicate of the existing family.
- **Supersedes nothing**: the §19 refutation stands independently of this mechanism.

## The next theorem-shaped question

Not "which two-orbit substrates fail" — that was the wrong axis. Instead:

> Is ℋ¹_G under any 4-cycle-only predicate always carried by the odd-cycle part of the arena's
> cycle space? Equivalently: does admitting arena 3-cells force ε_harm = 0 for every substrate,
> or only for substrates whose harmonic sector happens to be triangle-supported?

A counterexample would be a substrate with ε_harm(𝒦₄ + 3-cells) > 0 — a class invisible to all
cycles of length 3 and 4. Candidates: high-girth graphs where the shortest circulating cycle is
length 5 or more. Q₃-like bipartite substrates are the natural place to look, since they have no
triangles at all and so cannot be closed this way.

## Dead ends this explains

The three killed discriminators — intrinsic cell shape, orbit size, primitive gcd / rank-1 Smith
form — were all searching for a property of the *added 4-cycles*. The discriminator was never in the
4-cycles. It was in what no 4-cycle can reach.

## Not established

Nothing physical. ε_harm is dim ℋ¹_G under a declared predicate, per §18.
