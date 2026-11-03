# Five Open Holes: Source-Grounded Audit and Next Binding Step

**Date:** 2026-10-20  
**Scope:** Review of the two pasted compendium texts and the NotebookLM relation-layer note. This is an audit of the claims in those files, not a claim that all proposed results have been executed.

## Decision

**Bind Hole 1 first: the closed-form Walsh spectrum of latitude in ring coordinates (CNT-03).**

It is the best first target because it is a finite, exact, discrete problem and depends on already established components: the partner involution, corrected rank, the full block reader, the palindrome carrier, and the Walsh parity split. Its proposed block decomposition is mathematically plausible as a finite-sum identity, but the submitted text does not yet demonstrate that its inner reversal-ordered character sums have a closed evaluator of the stated complexity or reproduce every coefficient. That is a bounded proof-and-test task.

## What the submitted material actually contains

The expanded pasted text begins with the claim that all five open holes are being bound, but the file ends part-way through Hole 2C. It includes partial candidate work for Hole 1 and Hole 2, not solutions for Hole 3 (wide SHA-256 ROBDD schedule-tail pruning), Hole 4 (the all-width carry-seam functor), or Hole 5 (interpreting the constant second derivative as mass versus acceleration). Those three cannot be reclassified as resolved from this material.

The NotebookLM note supplies a separate deficiency-module template, \(D=A/W\), with character evaluation for a cyclic reader subgroup and examples on a 12-vertex witness arena. It does not specify a map from that witness arena, its automorphism group, or its module quotient to the nested-ring state space. It is therefore a potentially useful organizational method, not proof that any ring open hole has closed.

## Hole 1 — ring-coordinate latitude spectrum

### What stands

The source material already establishes the parity split:
- even Walsh degrees read the Walsh-even body;
- odd Walsh degrees read the palindrome carrier;
- the carrier has a degree-one expression in half-word coordinates;
- the exact ring address is given by the corrected rank/block reader.

For the carrier, transporting the half-word singleton characters through the explicit palindrome placement is an exact representation. For the body, splitting canonical non-palindromes into high-half blocks \(K\), with the reversal-ordered within-block index, gives a natural finite sum indexed by \(K\).

### What is not yet closed

The proposed expression for \(W[z_+](s)\) still contains the reversal-ordered sums \(\mathcal C_{K,\ell}\). Calling these “standard geometric/dyadic interval sums” and assigning them \(O(\operatorname{wt}(K))\) bit steps is not a proof of that evaluator. The evaluator must state its bit order, address mask conventions, block boundary convention, treatment of the center swap, and the special handling of palindrome entries. Then it must be compared coefficient-by-coefficient against direct Walsh transforms at small widths and the recorded coefficients through width 20.

The quadratic continuum argument explains a plausible reason for degree-two concentration, but it does not by itself prove the measured \(47\%\to33\%\) values or a closed all-\(n\) coefficient formula. Keep those values as measured observations unless derived exactly.

**Status:** parity decomposition — RUNS from the existing ledger; finite block-sum candidate — STANDS as a proposed identity pending explicit evaluator and coefficient audit; closed all-\(n\) spectrum — OPEN.

## Hole 2 — radial profile language

### Link 2A: \(A(q_D)\) as interval unions

The interval expression is an exact way to describe the preimage of a finite output prefix, provided the radial reader \(b_L(u)\), address convention, and half-open endpoint convention are fixed. As written, however, it is also close to a direct expansion of the definition: it still quantifies over every address and slice. To count as a useful seam-block result, each union must be reduced to the \(K\)-block and reversal-order indices with explicit bounds, including the center swap and palindrome-containing blocks.

**Status:** interval preimage decomposition — STANDS as a set identity under the stated reader definition; efficient block-union reduction — OPEN.

### Link 2B: Myhill–Nerode distinguishability

The proposed argument contains a promising observation: a front-half output can expose a bit of \(\tau(u)=1-\sqrt{1-2u}\), and equal binary suffixes of two angle cylinders can make \(\{2^L u\}\) agree at a shared future depth. But the pasted proof does not yet establish the required automata statement.

For Myhill–Nerode, the object must first be defined as a language of finite words. For every pair of distinct prefixes \(p_a,p_b\), the proof must then construct **one same finite suffix** \(v\) such that exactly one of \(p_av\) and \(p_bv\) is in that language (or the relevant right-quotient test differs). Showing that two angle intervals can have different \(\tau\)-bits is not enough unless the intervals are uniform at that digit and the same suffix forces the radial reader to observe that digit across the two states. The dependence \(k_L=\lfloor L\{2^L u\}\rfloor\) must be handled uniformly, not pointwise.

The stated entropy-deficit explanation is qualitative. It does not derive the numerical \(0.0113\) bits/ring or prove the asymptotic growth law.

**Status:** candidate mechanism — STANDS as a route to investigate; non-regularity proof — OPEN; entropy asymptotic — OPEN.

### Link 2C: \(D\equiv2\pmod3\) witness

The excerpt derives the seam offset
\[
q_L=2^{L-p}+\left\lfloor \frac23\,2^{L-D+1}\right\rfloor.
\]
For the range where the second term is zero, this does give a raw power-of-two offset. It does **not** alone identify the seam word's popcount: the known seam law depends on both the triangular block \(K\) and reversal-ranked intra-block index \(r\). In particular, the exact seam law has low-deficit special offsets \(q=K(K-1)/2\) when \(K=2^t\); these are triangular offsets, not arbitrary powers of two. The excerpt stops before it completes the generated-word identities or handles the carry at the end of the \(L\)-range.

**Status:** offset arithmetic — STANDS for its stated range; required target-word identities and all residue classes — OPEN.

## Hole 3 — SHA-256 ROBDD schedule-tail pruning

The provided excerpt names an implementation target (`cofactor_inverse_bdd.py`) but supplies no pruning invariant, cofactor-preservation proof, node-count benchmark, or multi-byte run. A bijection/relabeling of schedule coordinates cannot by itself reduce the number of valid preimages. A viable claim must show that the constraints prune impossible regions while preserving every valid message and must compare node counts on the same variable ordering.

**Status:** OPEN; route-code relabeling remains non-inversion.

## Hole 4 — all-\(n\) adder carry-seam functor

The supplied materials mention a 22-edge-orbit family, a 12-vertex witness arena, and a proposed relation between Myhill–Nerode cut states and a cohomology rank. They do not provide the all-\(n\) induction or a natural map between those objects. The relation-layer machinery becomes relevant only after defining the domain/codomain modules, the group action, and the map on generators and relations, then proving the required square commutes.

**Status:** OPEN.

## Hole 5 — interpreting \(u''(t)=-1\)

From \(u=t-\tfrac12t^2\), the calculus identity \(u''(t)=-1\) is exact. The identity alone cannot determine which component should be called “mass” and which “acceleration.” That split needs independent definitions of the variables, dimensions/units, and a governing physical model. Assigning those labels from the second derivative alone would be underdetermined.

**Status:** calculus identity — STANDS; physical factor interpretation — PULL / OPEN.

## Relation-layer method: safe integration rule

The quotient \(D=A/W\) can be a useful way to catalog unresolved relations, but only after each ring problem defines:
1. the ambient relation module \(A\);
2. the submodule \(W\) generated by already-proved ring identities;
3. the relevant automorphism group \(G\) and its action;
4. the readout subgroup \(H\), if a character/Fourier calculation is to be used;
5. the actual quotient class whose vanishing or non-vanishing closes the claim.

The NotebookLM note’s numerical example (12 vertices, dimension 235, 22 edge orbits) must not be imported as if it already described the ring. A bridge map and compatibility proof are necessary.

## Updated decision ledger

| Hole | Status after this source audit |
|---|---|
| 1. Ring-coordinate latitude spectrum | OPEN; candidate finite block formula needs a tested evaluator |
| 2A. Prefix support \(A(q_D)\) | Set identity STANDS; compact block reduction OPEN |
| 2B. Myhill–Nerode infinite distinguishability | OPEN; common-suffix proof missing |
| 2C. \(D\equiv2\bmod3\) target word | OPEN; offset arithmetic partial only |
| 3. SHA-256 ROBDD pruning | OPEN |
| 4. All-\(n\) carry-seam functor | OPEN |
| 5. Mass/acceleration interpretation | PULL / OPEN |
| Physical quantum claims | PULL; finite combinatorial identities do not alone prove physical quantum mechanics |

**Next action:** derive and implement the exact \(\mathcal C_{K,\ell}\) evaluator for Hole 1, with a pre-run prediction and a direct-transform comparison. Do not describe the five-hole binder as fully closed until each hole has its own proof, source artifact, and audit scope.
