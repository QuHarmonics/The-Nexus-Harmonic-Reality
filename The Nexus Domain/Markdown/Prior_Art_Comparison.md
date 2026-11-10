---
title: "What Is New to the Reader"
subtitle: "Prior-art comparison for *Runtime Reflection of the BBP Formula: Proof of the Persistent Pending-Field Reader*"
author: "Dean A. Kulik · QuHarmonics Research Group · ORCID 0009-0003-3128-8828"
date: "12 October 2026"
---

## Position

Nothing in this work introduces new arithmetic. The BBP identity is from 1997. Base-16 long division, a geometric bound on a series tail, and a loop that refines until a result is certified are all standard. Each piece was already running before this reader was built; the reader aligns to them.

The question for a paper is narrower: which *arrangements* of those pieces are new to the reader of the literature. This memo maps each claim to the closest prior art found in the sources checked so far, and states what remains to search before any priority claim is made.

Suggested positioning sentence for the abstract:

> The arithmetic used here is not new: the BBP identity, base-16 long division, a geometric tail bound, and a refine-until-certified loop of the kind Ziv introduced for correct rounding. What this paper adds is an arrangement of them: a certified, unbounded reader that streams the hexadecimal digits of π from the BBP lane system by retaining every opened lane across emissions, with proofs of soundness, termination and the balance between resolution and emission, and a reflection procedure that recovers the lane laws from four observed runs of BBP.

## Claim-by-claim comparison

Status uses three words: *proved* (a theorem in the proof note), *measured* (an executable result), and *open*.

| Claim and status | Closest prior art found | New to the reader |
|---|---|---|
| **1. Certified streaming from the BBP lanes.** Hex digits of π emitted in order from an empty field, every opened lane kept as a two-cursor long division across emissions. *Proved; measured on 2,000 digits (audited) and 10,000 digits.* | BBP extraction computes each position on its own and carries no state from one position to the next; one floating-point evaluation yields roughly 9 to 24 digits (Bailey, Borwein and Plouffe 1997; Bailey 2006). Streaming π algorithms exist on other series: bounded and mixed-radix (Rabinowitz and Wagon 1995), unbounded with linear-fractional-transformation state (Gibbons 2006). | An unbounded, certified stream built on the BBP lane system itself, retaining every opened lane instead of recomputing modular powers, with the resolution frontier and the precision frontier kept separate. Not found in the sources checked. |
| **2. Certify, else refine; terminates.** A digit is emitted only when the enclosure fixes it; otherwise OPEN or WIDEN; every digit is eventually emitted because the target is irrational. *Proved.* | Ziv's strategy for correctly rounded functions: evaluate with an error bound, raise precision until the rounding is determined, which terminates when the value is not a breakpoint (Ziv 1991; Brent and Zimmermann 2010, §3.1.8). Exact real arithmetic streams digits on demand (Gosper 1972; Edalat and Potts 1997). | Nothing in the loop itself. What is specific is its instantiation on the BBP lanes, with two kinds of refinement and the scheduling rule under which termination is proved. |
| **3. Holding back uncertain digits.** Extra refinement happens only when the value lies near a digit boundary. *Measured: 20 such steps in 10,000 digits against 21.5 predicted.* | Rabinowitz and Wagon hold "predigits" because a later carry can raise a digit already computed (the run-of-nines problem). Analyses of the table maker's dilemma estimate how often extra precision is needed. | Certification replaces hold-and-repair: no emitted digit can be changed by a later carry. The edge-rate match is a measurement. It assumes the fractional parts of 16ⁿπ are equidistributed, which would follow from normality of π in base 16, and that is open. |
| **4. Balance between resolution and emission.** EMIT multiplies the tail bound by exactly 16; OPEN divides it by more than 16; after N emissions, OPENs = N + g with g ≥ 0. *Proved. g stayed at 0 or 1 in every run: measured.* | Implicit in any truncation analysis of a base-16 series. | The explicit accounting of resolution against emission inside a streaming reader. A small contribution. |
| **5. Reflection.** The lane laws are recovered from BBP's execution trace; the advance rule is unique among 4,096 declared candidates after four runs (24 transitions). *Proved by finite certificate.* | Partial evaluation and the Futamura projections, where specializing an interpreter yields compiled code (Futamura 1971). Trace-based specialization and program synthesis from examples. Dean Kulik's earlier Zenodo record frames BBP as a read-head into π, conceptually and without an implementation. | The concrete identifiability result for BBP, and emission of a standalone generator from the fitted laws. Uniqueness holds within the declared candidate family, not among all conceivable rules. |
| **6. What the state must carry.** No finite autonomous machine generates the stream; the carry and crossing count coincide at n = 0 and n = 1, (−1, −13), while the digits are 2 and 4; the pending value at the start is π − 47/15. *Proved.* | A finite automaton without input produces an eventually periodic output, so it cannot produce an irrational's expansion (classical). Whether π's digits form an automatic sequence, read by a finite automaton from the digits of n, is open; the Adamczewski–Bugeaud theorem excludes only algebraic irrationals (Adamczewski and Bugeaud 2007; Adamczewski and Faverjon 2018). | The explicit collision, and the address-versus-accumulation reading of the open question. BBP keeps only the address but needs unbounded arithmetic to use it; a finite-state reader of the address alone is exactly the open automaticity question for π. |
| **7. Families of formulas.** Adding multiples of the zero relation gives a one-parameter family that all yield π; the classical weights are the only member whose weights sum to zero. *Verified numerically.* | Zero relations, and formula variants obtained by adding rational multiples of them, are catalogued in Bailey's compendium. | Only the remark that the zero-sum member is the one whose crossing count does not drift linearly. Elementary; belongs in a remark. |

## Two tightenings for the proof note

Both are small, and neither changes a conclusion.

**Section 7, termination.** The note shows that (K + 1)/16^P^ tends to zero at the states where an OPEN is triggered, then says the ratio cannot increase between OPENs. At the OPEN itself K rises by one, so the ratio briefly rises. Suggested replacement for that sentence:

> Each OPEN raises K by one with P unchanged, so immediately afterwards the ratio is at most (K + 2)/16^P^ ≤ 2(K + 1)/16^P^, which still tends to zero. Between OPENs the ratio only falls, because WIDEN increases P and leaves K fixed.

**Section 8, balance.** The sentence pairing four lane records per layer with a four-bit symbol is a numerical coincidence, not the mechanism. The mechanism is the bound itself. Suggested replacement:

> EMIT multiplies the tail bound by exactly sixteen, B~n+1,K~ = 16·B~n,K~, and OPEN divides it by more than sixteen, B~n,K+1~ / B~n,K~ = (8K + 9) / (16(8K + 17)). Each emitted hexadecimal digit therefore spends exactly four bits of the enclosure's slack, and each OPEN restores slightly more than four. Certification at position n requires K ≥ n, and K starts at −1, so after N emissions the number of OPENs is N + g, where g = K − N + 1 ≥ 0 is the current lookahead. The lower bound N is a theorem. That g stayed at 0 or 1 in every run is a measurement; no constant bound on g can be proved without knowing how closely the expansion of π approaches digit boundaries.

**Reproducibility.** The 10,000-digit result came from `channel.py`, which drives the same `PendingField` class with the same scheduling rule; it runs in about two minutes. Adding it to the bundle as a second configuration lets the 10,000-digit figures be reproduced rather than only reported.

## What remains to search

The sources above are a first pass. Before claiming priority for claims 1 and 5, these should be checked:

- Arndt and Haenel, *Pi Unleashed* (2001), the chapter on spigot algorithms.
- zbMATH and MathSciNet: "BBP" together with "spigot", "streaming" or "sequential".
- arXiv full text: "BBP" together with "unbounded", "spigot" or "consecutive digits".
- Exact real arithmetic systems (iRRAM, Arb, and functional exact-real libraries), for any BBP-based stream.
- Later papers by Plouffe and by Bellard on digit computation.
- Program synthesis from execution traces, to position the reflection method accurately.

## References

Adamczewski, B. and Bugeaud, Y. (2007). On the complexity of algebraic numbers I. Expansions in integer bases. *Annals of Mathematics* 165, 547–565.

Adamczewski, B. and Faverjon, C. (2018). Mahler's method in several variables II: Applications to base change problems and finite automata. arXiv:1809.04826.

Bailey, D. H. (2006). The BBP algorithm for pi. Manuscript, 8 September 2006.

Bailey, D. H. A compendium of BBP-type formulas for mathematical constants. Manuscript, davidhbailey.com.

Bailey, D. H., Borwein, P. B. and Plouffe, S. (1997). On the rapid computation of various polylogarithmic constants. *Mathematics of Computation* 66(218), 903–913.

Brent, R. P. and Zimmermann, P. (2010). *Modern Computer Arithmetic*, version 0.5.1, §3.1.8.

Edalat, A. and Potts, P. J. (1997). A new representation for exact real numbers. *Electronic Notes in Theoretical Computer Science* 6.

Futamura, Y. (1971). Partial evaluation of computation process: an approach to a compiler-compiler. *Systems, Computers, Controls* 2(5); reprinted in *Higher-Order and Symbolic Computation* 12 (1999), 381–391.

Gibbons, J. (2006). Unbounded spigot algorithms for the digits of pi. *The American Mathematical Monthly* 113(4), 318–328.

Gosper, R. W. (1972). Continued fraction arithmetic. In *HAKMEM*, MIT AI Memo 239.

Kulik, D. The BBP formula as a harmonic reflector in the Nexus recursive framework. Zenodo record 15471626.

Rabinowitz, S. and Wagon, S. (1995). A spigot algorithm for the digits of pi. *The American Mathematical Monthly* 102(3), 195–203.

Ziv, A. (1991). Fast evaluation of elementary mathematical functions with correctly rounded last bit. *ACM Transactions on Mathematical Software* 17(3), 410–423.
