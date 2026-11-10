# NEXUS P33–P35 — Saturation, relabelling, and the reader-relative cost

**Dean A. Kulik · QuHarmonics Research Group · ORCID 0009-0003-3128-8828**  
Independent derivations / executable audits, 6 November 2026.  
Ledger vocabulary: **STANDS** for proven identities; **RUNS** for pre-sealed executions that landed; **DEAD END** for the sealed false clause; **OPEN** for missing computational constraints. Original manuscript unchanged.

## Starting question

In a saturated contact field, every admissible route is present. Does that make every route equivalent? The answer splits by **which interface is held fixed**. A word-facing contract is weaker than a contact-facing contract, and both are weaker than a bound cost model for a concrete reader.

## P33 — All complete rings under one word-facing operator form a single conjugacy orbit

Let \(X_n=\{0,1\}^n\), \(N=2^n\), \(m=N/2\), \(n\ge2\). Let \(J\) reverse a word, \(C\) complement it, and \(P\) reverse nonpalindromes or complement palindromes. \(P\) is a fixed-point-free involution, hence has \(m\) paired orbits \(\{a_i,P(a_i)\}\).

A complete oriented ring is a single \(N\)-cycle \(T\). Requiring \(PTP=T^{-1}\) forces the reflection to have no vertex fixed points and exactly two fixed edges opposite each other. Choose one representative \(a_i\) from each facing pair, in any order, and form

\[
R=(a_1,\dots,a_m,P(a_m),\dots,P(a_1)).
\]

Every compatible ring has this form after a cyclic rotation, and the reverse order gives the opposite travel direction.

The centralizer of \(P\) in the symmetric group is \(C_2\wr S_m\), of size \(2^m m!\). For any two compatible rings \(R_a,R_b\), the map \(Q(a_i)=b_i,\ Q(Pa_i)=P b_i\) commutes with \(P\) and satisfies \(QT_aQ^{-1}=T_b\). Its inverse uses the opposite matching. The stabilizer of one complete cycle is \(\{I,T^m\}\): a relabelling that commutes with a full cycle is a rotation \(T^k\); to commute also with its reflection requires \(T^k=T^{-k}\), forcing \(k=0,m\). By orbit–stabilizer:

\[
\boxed{\#\text{directed compatible rings}=2^{m-1}m!,\qquad
\#\text{unoriented compatible rings}=2^{m-2}m!}\quad(m\ge2).
\]

At LEN 2: 4 oriented, 2 unoriented. LEN 3: 192 oriented, 96 unoriented. LEN 4: 5,160,960 oriented, 2,580,480 unoriented. There are always **two** reflection-fixed axis edges; an ordering convention decides which one is named the center seam and which one the closure.

**RUNS P33:** exhaustively enumerated all compatible full permutations at LEN 2–3 independently of the half-chain generator and checked conjugation, inverse, and exact two-axis law. The SHA-256 seal for P33 precedes execution: `060041d1c8523f25d2628ce98fa4534ce8035c193abfbb9bafbcccf50bc1ce20`.

## P34 — The contact interface reduces the permitted relabellings

The same complete rings are **not** interchangeable if the canonical binary contact encoding \(u\mid v\) and its fixed facing \(P_{2n}\) are held in place. At LEN 3, all 192 word-facing-compatible oriented rings have contact exception counts 6 or 8 (112 and 80 rings respectively), despite satisfying the identical \(PTP=T^{-1}\) law. The lexicographically constructed native ring has 8; other valid full rings have 6. At LEN 4, even elementary rearrangements of the first half produce different contact defect counts.

Consider a relabelling \(Q\) preserving the *individual* native operations: \(QJ=JQ\), \(QC=CQ\). Then \(Q\) preserves the palindrome locus, both branches of \(P\), and the contact-facing operation:

\[
\boxed{(Q\times Q)P_{2n}=P_{2n}(Q\times Q).}
\]

Therefore if \(T'=QTQ^{-1}\), the count of contacts in \(\Gamma_T\) whose image under \(P_{2n}\) is absent from \(\Gamma_T\) is **invariant** under \(Q\). The proof is a bijection of the transition graphs by \(Q\times Q\). The inverse is \(Q^{-1}\times Q^{-1}\).

The group \(H_n=C(J)\cap C(C)\) is obtained by decomposing \(\langle C,J\rangle\)-orbits into three types: \(u=p_n/2\) palindrome complement-pairs, \(v=a_n/2\) anti-palindrome pairs (\(a_n=2^{n/2}\) for even \(n\), otherwise 0), and \(g=(2^n-p_n-a_n)/4\) generic four-word orbits. Equivariant maps may permute orbits only within the same type; on each orbit there are 2, 2, or 4 possible shifts. Hence

\[
\boxed{|H_n|=2^u u!\,2^v v!\,4^g g!.}
\]

\[
\begin{array}{c|r|r}
 n & |C(P)| & |H_n|\\\hline
 2 & 8 & 4\\
 3 & 384 & 32\\
 4 & 10{,}321{,}920 & 2{,}048
\end{array}
\]

The 192 directed rings at LEN 3 split into **8** \(H_3\)-orbits: there are 3 orbits of size 16 and 2 of size 32 with defect 6, and 1 of size 16 and 2 of size 32 with defect 8. (Totals: \(3(16)+2(32)=112\), and \(16+2(32)=80\).)

**STANDS:** functorial contact identity and group-order formula. **RUNS P34:** independently enumerate \(H_3\) from all 8! bijections, generate all 2,048 members of \(H_4\) from the orbit types and test the pointwise contact identity on 524,288 inputs; verify the invariant facing-defect counts. Seal SHA-256: `4a8ea1193687251c43bd132f62e65136531197dfb9fde07e57718f12dce96d68`.

**Consequence:** All complete compatible rings are equivalent *before* the contact reader is fixed. Once a contact encoding and its interface are held fixed, an individual relabelling may cease to preserve the relevant contract. What changes is relative alignment, not the inventory of available routes.

## P35 — The exact reader-order effect for mirror equality constraints

The paper's mirror-pair equality family supplies the same distinction in Boolean complexity without randomized data. Let

\[
E_m(x)=\bigwedge_{i=0}^{m-1}(x_i=x_{m+i}).
\]

Given a variable read order \(\pi\), at cut \(k\) let \(c_\pi(k)\) count pairs with exactly one endpoint read. Each crossing pair contributes one independent outstanding binary obligation. The number of distinct **nonzero** residual Boolean functions is exactly \(2^{c_\pi(k)}\). Add one zero residual if at least one pair has been fully read and can already be violated.

\[
\boxed{W(E_m,\pi,k)=2^{c_\pi(k)}+[\text{at least one fully read pair}].}
\]

For \(m\ge2\), the pair-adjacent order \((0,m,1,m+1,\dots)\) has maximum width **3**; the split order \((0,1,\dots,m-1,m,\dots,2m-1)\) has maximum width \(2^m\). For the same complete constraint field, the two readers therefore exhibit very different costs.

Every order is the mirror order under some variable permutation, but to preserve width that permutation must also act on the **formula**: \(W(E_m,\pi,k)=W(QE_m,Q\pi,k)\). Acting only on the reader generally changes width. For an exchangeable *random formula ensemble*, simultaneous relabelling leaves the ensemble distribution unchanged; this implies equality of width distributions across fixed, formula-independent read orders, **not** equality of costs on each individual formula.

**RUNS (corrected audit):** all 24 orders at 4 variables; all 720 at 6; all 40,320 at 8. For the 4- and 6-variable cases, each cut width was also reconstructed from the full residual truth tables.

**DEAD END / SEALED FAILURE:** P35.2 originally predicted width 2 for the pair-adjacent order. The first run failed. That missed the zero residual from an already-violated completed pair. The corrected value is 3 for \(m\ge2\), and the original seal was not changed. Seal SHA-256: `80e13583a323c03211bf3c4fd9caa22a29790ce1ae593fbb92a463ecc44cc263`.

The exact empirical distributions of maximum width (including zero):

- \(m=2\): width 3 for 8 orders, width 4 for 16.
- \(m=3\): width 3 for 48 orders, width 4 for 96, width 5 for 288, width 8 for 288.
- \(m=4\): width 3 for 384 orders, width 4 for 768, width 5 for 9216, width 8 for 6912, width 9 for 13824, width 16 for 9216.

## What this changes in the full landscape

The result is **not** that one arbitrary ordering is the correct reality. It is that route selection is a choice of *reading frame*. A full saturated relation may admit many conjugate complete continuations. An external readout or additional interface fixes a smaller equivalence group, separating routes that were identical under the coarser law.

For native rings: \(C(P)\) acts transitively, whereas \(C(J)\cap C(C)\) need not. For the paired-equality compiler: simultaneous formula-reader relabelling is free, whereas reordering one fixed formula changes the number of outstanding obligations. The pattern is the same relative-constraint geometry.

**OPEN / next provider:** characterize the **restricted family of inexpensive, contact-preserving relabellings** from the actual bit-level compiler verbs, including their cost and inverse, rather than assuming any of the algebraically existing \(Q\)'s can be discovered or implemented at constant cost. This is the shared link to the 3-SAT reader-order problem and the retained-step's readable reversor.

All calculations and corrections are in the companion three independent scripts, three pre-execution seals and four run/correction logs.
