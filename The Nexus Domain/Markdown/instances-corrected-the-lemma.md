# The instances corrected the lemma

Written 2026-10-04. Amends `claude/relation-layer-paper-and-theorem.md` §6 and the paper
`Kulik_RelationLayer_RankAccess_ClosureDepth.docx`. Written after Dean's objection that
instantiation is not cataloguing — which this file confirms empirically, because the instances
broke a clause the abstraction had stated too narrowly.

## 1. Lemma 6.2 was stated too narrowly

**Paper version.** For C_n with n ≥ 5, every arena 4-cycle is a commuting square, so
𝒦₄ = 𝒦_disj.

**Actual clause, found by instantiating.** Running the contract over 20 graphs showed the
condition is neither "cycle graph" nor "girth ≥ 5":

> **𝒦₄ = 𝒦_disj ⟺ X contains no 4-cycle subgraph.**

Verified at K = 2 and K = 3 over C₄–C₇, K₃, K₄, K₅, bull, butterfly, paw, K₃,₃, Q₃, Petersen,
P₅, K₁,₄, tree Y, the 12-vertex witness, two-triangles-plus-edge, C₅-plus-chord, Heawood.
**0 mismatches.**

The instances that forced the correction:

| instance | has 4-cycle | 𝒦₄ = 𝒦_disj | what it showed |
|---|---|---|---|
| C₄ | yes | no | the n ≥ 5 bound is sharp |
| K₄, K₅, K₃,₃, Q₃, C₅+chord | yes | no | the clause fails outside C_n too |
| **bull, butterfly, paw** | no | **yes** | holds with a **triangle** present — so not girth |
| **Petersen, Heawood** | no | **yes** | holds far from cycle graphs |
| **P₅, K₁,₄, tree Y** | no | **yes** | holds on trees, which have no cycles at all |

The published proof needs no change — it already turns on whether a token can wind a closed walk
of length 4, which requires a 4-cycle. A triangle only supplies a closed walk of length 3, which
cannot produce four distinct arena vertices. Only the hypothesis line was wrong.

## 2. The collapse of all predicates needs girth ≥ 5, and the bull proves it

No triangle ⟹ 𝒦₃ = ∅ (already proved). No 4-cycle ⟹ 𝒦₄ = 𝒦_disj (above). Together:

> girth(X) ≥ 5 ⟹ 𝒦₃, 𝒦₄, 𝒦₃,₄ and 𝒦_disj all coincide.

The **bull** is the control that shows both conditions are needed: no 4-cycle, so 𝒦₄ = 𝒦_disj,
but it has a triangle, and there ε_harm(𝒦_disj) = 3 while ε_harm(𝒦₃,₄) = 0. One condition is not
enough.

## 3. New numbers, and a reversal about Prue–Scrimshaw

At trivial G the collapsed quantity is dim H¹(UD^K(X); ℚ) by the paper's §8.1–8.2. Measured:

| X | girth | K | arena | ε_harm(𝒦_disj) = ε_harm(𝒦₃,₄) |
|---|---|---|---|---|
| C₅, C₇ | 5, 7 | 2, 3 | — | 1 |
| **Petersen** | 5 | 2 | 45v 120e | **6** |
| **Petersen** | 5 | 3 | 120v 420e | **6** |
| **Heawood** | 6 | 2 | 91v 252e | **8** |
| **tree Y** | ∞ | 2 | 21v 30e | **2** |
| **tree Y** | ∞ | 3 | 35v 60e | **4** |

**The reversal.** The paper says of Prue–Scrimshaw's improvement of Abrams (A′) from K+1 to K−1:
"the improvement is therefore irrelevant in this case." True for C_n, which has no essential
vertices. **False for every substrate above**, where it is load-bearing. Checked per graph:

| X | K | min essential-vertex path | Abrams (A′) ≥ K+1 | Prue–Scrimshaw ≥ K−1 | (B′) | applies |
|---|---|---|---|---|---|---|
| Petersen | 2 | 1 | **fails** | holds | holds | **yes, via PS only** |
| Petersen | 3 | 1 | fails | fails | holds | no |
| Heawood | 2 | 1 | **fails** | holds | holds | **yes, via PS only** |
| Heawood | 3 | 1 | fails | fails | holds | no |
| tree Y | 2 | 1 | **fails** | holds | vacuous | **yes, via PS only** |
| tree Y | 3 | 1 | fails | fails | vacuous | no |

So the topological reading is licensed at K = 2 and **not** at K = 3:

- **dim H¹(UConf₂(Petersen); ℚ) = 6**, **dim H¹(UConf₂(Heawood); ℚ) = 8**,
  **dim H¹(UConf₂(tree Y); ℚ) = 2** — via Abrams with the Prue–Scrimshaw bound.
- Petersen and Heawood at K = 3, and tree Y at K = 3 (value 4): **discrete configuration space
  only**. No topological claim; the hypothesis fails even under the improved bound.

## 4. Other instance findings

- **A second separation witness.** The **bull** gives I_h = 3 and L_closure = 4, independently of
  the 12-vertex witness. The separation of traversal cost from closure depth is not a quirk of one
  graph.
- **A tree carries a residual class.** Tree Y has no base cycle at all, yet its arena does (tokens
  commute), and ε_harm = 2 at K = 2. Arena topology is not inherited from base topology.
- **The clock lemma held on every instance** where d was computable, as it must.
- **Caveat on d.** The period is computed as a gcd over cycles up to a length bound. For C₇ and C₈
  with the bound at 6, d came back 0 — correctly, since their shortest detecting cycle has length
  7. A reported period must state the bound, and the clock check (§3 of `the-clock-mod-d.md`) is
  what confirms it.

## 5. The methodological point, conceded

The prior file dismissed a batch of cross-domain restatements as cataloguing. That was right about
prose restatement and wrong as a general principle. Instantiation is a test: an interface with no
implementations is vacuous, and an implementation that violates the contract is what tells you the
contract was mis-specified. In this session the instances have now done that four times — C₄ for
the sharpness bound, the witness and the bull for I_h ≠ L_closure, bipartite C₆/C₈ for the
odd-cycle refutation, and now Petersen, the bull and the trees for the 4-cycle clause.

The distinction worth keeping is narrower than "instances versus abstraction": a restatement in a
new vocabulary adds nothing; an instantiation that can fail the contract is evidence.
