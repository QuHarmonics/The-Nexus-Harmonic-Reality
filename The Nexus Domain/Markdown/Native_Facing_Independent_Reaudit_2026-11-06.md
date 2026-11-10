# Independent re-audit of *Native Facing* (53 pages)

**Source:** *Native Facing.docx*, Dean A. Kulik, QuHarmonics Research Group, ORCID 0009-0003-3128-8828.  
**Audit date:** 2026-11-06.  
**Scope:** Mathematical contracts, code verification coverage, selected independent enumerations, published observational context, and document rendering. **The original manuscript was not modified.** This is a post-source audit, **not a sealed new prediction**.

## Verdict

The native ring/facing program contains reproducible mathematical results. Its full-paper statement **“every theorem, dimension, spectrum, cycle count, and table cell has been exhaustively verified” is not supported by the five-section master script**. The script runs successfully, but it tests subsets, sometimes much smaller than its PASS labels imply. A separate program reproduces the 8,704-class retained quotient, and the full AGL catalog program reproduces 5/11/25 classes at LEN 2/3/4.

There are **two definite mathematical/terminological corrections**, a **non-uniqueness theorem gap**, several **scope corrections** for physics and computational complexity, and **one serious DOCX rendering failure**.

## Reproduced independently

1. **Facing and center law:** for 1 ≤ n ≤ 12, P_n is a fixed-point-free involution commuting with bit reversal and complement; the odd-center response agrees with the palindrome selector. See `nf_reaudit/independent_check.py` and its log.
2. **Transition-table facing criterion:** exhaustive enumeration of all 2!, 4!, and 8! bijections gives native programs 2, 6, 188. Separately, facing yields a *valid total table* for 2, 12, and 15,952 of those bijections, respectively; being a total faced table is distinct from being *the same* program. The valid faced function is J f^{-1} J.
3. **Signed cyclic-shift group:** independently computed |G_n| = n·2^n and directed generator diameter 2n−2 with {C,σ,τ} at 2 ≤ n ≤ 10; with {σ,τ}, diameter 2n−1. These computations are algebraic, not observational fits.
4. **Affine conjugacy catalog:** ran the separate complete `catalog4.py` (not invoked by the master script). LEN 2: 5 classes among 24 maps; LEN 3: 11 among 1,344; LEN 4: 25 among 322,560. Inverse-twin pairs 0, 1, 3.
5. **Retained quotient:** re-executed `NEXUS_Locked_Return_Map.py` (not invoked by the master script): 8,704 quotient classes; long period list [15,47,49,66,106,217,806,1130,1974,2593], with the indicated section-return checks and exact inverses.
6. **Mirror-pair reader dependence:** independent residual-function analysis for the equality constraints x_i=x_{n-1-i} finds midpoint frontier width 2^{n/2} in left-to-right variable order and nonzero width 2 in mirror-aligned order at n=4,6,8,10,12. This is a result about those exact constraint families, not an asymptotic theorem for arbitrary random 3-SAT.
7. **Master verification re-run:** all five advertised PASS lines reproduce. This proves its stated assertions executed, not that every claim in the manuscript was checked.

## Exact corrections

### R1 — Klein group at n=1 (Section 1.1)

The manuscript says J_n and C_n generate a Klein four-group at **every** n. At n=1, J_1=I and the generated group has only {I,C_1}, of order **2**. A four-element Klein group occurs for n≥2.

### R2 — Nonuniqueness of the palindrome fallback (Section 1.1)

The statement that bitwise complement is the **unique** distinction on the palindrome locus commuting with reversal is false under the written constraints.

At LEN 3, define a different permutation Q by these four exchanges:

- 000 ↔ 010
- 111 ↔ 101
- 001 ↔ 100
- 011 ↔ 110

This Q is fixed-point-free, involutive, commutes with J_3 **and** C_3, and agrees with J_3 on all nonpalindromic words. Yet Q(000)=010, while native P_3(000)=111. Thus the listed group properties alone do not uniquely select native facing. The additional contract “on the palindrome locus, select the root bitwise complement” does select P_n. That is the missing dependency and should be explicit. Q was executed as a counterexample.

### R3 — Signed cyclic shifts are not the full hyperoctahedral group (Section 4.1)

The theorem correctly gives the group G_n=(Z_2)^n ⋊ Z_n, order **n·2^n**. Calling it the **full hyperoctahedral wreath product** is incorrect for n≥3. The full signed permutation group is (Z_2)^n ⋊ S_n, order **n!·2^n**. For n=3, these orders are 24 versus 48. Rename G_n the cyclic signed-shift / cyclic-base wreath group, a subgroup of the hyperoctahedral group.

### R4 — Equation-extraction false alarm, resolved (Section 4.1)

The DOCX's actual OMML markup **correctly says** J_n(1)=2^{n−1} ≠ 2^n−1=inc_n^{-1}(0). A plain-text extraction flattened these distinct superscript structures to the same string and initially suggested a proof error. **This is not a defect in the mathematics or source markup.** It was an audit interpretation error, corrected by inspecting the equation tree. The calculation showing increment non-nativity stands.

### R5 — Inversion versus contact-local native facing (Section 3.3)

For every reversible F, ordinary transition-graph reversal gives the exact inverse without any seam or additional state:

(s,F(s)) ↦ (F(s),s).

The theorem's nontrivial question is whether **conditional P_{2n}** on each concatenated contact represents J_n F^{-1}J_n as a total function. This holds precisely when the self-reading set is complement-closed. Failing that condition proves an obstruction to **this native contact-facing encoding**, not to computation being reversible or to an extra reader being logically mandatory.

### R6 — `RUNS` and theorem coverage (Appendix)

The master script's labels are wider than its assertions:

- Section 1: directly checks P identities, selected center entropies, ring successor exceptions, and one hard-coded comb arithmetic point, not an observational posterior or horizon quantization.
- Section 2: checks **overlap-contact** paths for L=2..6,k=2..5 and selector pullback, not every k or the entire §181 block model. Also, its local variables `emergent` and `lone` do not correspond clearly to the manuscript's semantic labels: `emergent` increments on a palindromic whole, which includes the actual *lone-seam* case.
- Section 3: computes cycle rank and some necklace/defect counts, but does not run BIND, prove the full closed-route invariant subspace, or audit all seam providers.
- Section 4: enumerates native programs at n≤3 and a principal clock address property. It does **not** invoke `catalog4.py`, the complete native instruction audit, or any Cayley BFS.
- Section 5: checks the parity toggle and nine-move cylinder. It does **not** compute the 8,704-class quotient, the 29-depth twisted Burnside identity, the full algebraic degree table, or the 3-SAT notebook.

Do not call all claims “verified by master.” Link each to the relevant actual audit, including existing independent scripts where available.

### R7 — Answer memory and assignment certificates (Section 5.3)

A Boolean satisfiability **decision result** is one bit. But a general satisfying **assignment certificate** specifies n variable values (n bits before any compression), not O(1) bits. Keep the decision answer separate from a certificate or a local bit of a certificate. The verified mirror-pair BDD width law applies to those constructed pair-equality constraints. Empirical slopes ~0.28n and ~0.29n for critical random 3-SAT require separate data and scope; they are not consequences of P_n alone. The accompanying 3-SAT notebook has FULL=False and explicitly skips its extended runs in that execution.

### R8 — Physical binding and GW250114 (Sections 1.3–1.4)

The Bell-paired palindrome register has the exact entropy tent S(k)=min(k,n−k) **for the specified state**. The Bekenstein–Hawking conversion ΔA=4ℓ_P² ln 2 follows **if** a physical horizon-area transition corresponds to an increase of one binary entropy bit. The current ring algebra proves count doubling under LEN extension; identifying physical horizon transitions with LEN increments is a separate binding hypothesis.

The GW250114 comb numerical offsets are arithmetic evaluations of a **conditional Foit–Kleban emission-line model**, using a selected remnant spin, model tone, and quoted measurement precision. The published LVK result finds the fundamental Kerr QNM within approximately 2% precision, but it is not a black-hole area-spectrum model comparison. Foit and Kleban explicitly condition their ringdown test on quantized emission/absorption frequencies controlling the observed initial ringdown. Therefore “8π excluded at 10.89σ” is **a conditional residual within that model**, not a directly published 10.89σ exclusion by the detectors. The existing datum does not establish the one-bit horizon step.

External source checks: LVK [official summary](https://ligo.org/science-summaries/GW250114_TGR/), [spectroscopy paper](https://arxiv.org/abs/2509.08099), [Foit–Kleban hypothesis](https://arxiv.org/abs/1611.07009), and [2026 independent RingCWB analysis](https://arxiv.org/abs/2610.09503).

### R9 — DOCX rendering failure (whole document)

The file has **1,424 native OMML (`m:oMath`) objects**. They contain the mathematical content in XML. However the LibreOffice-based DOCX rendering displays the formula objects as **blank spaces**. This affects inline symbols and displayed equations throughout all 53 rendered pages, notably page 2. The manuscript is not publication-ready **in that renderer**. This does not establish whether Microsoft Word's renderer has the same problem. Test in Microsoft Word or regenerate equation objects through a compatible conversion and visually verify a distribution PDF before release.

## Overall disposition

**STANDS in the defined algebra:** native P facing and palindrome selector identities, exact center law, de Bruijn cycle dimension, native program criterion and counts, signed cyclic-shift subgroup, affine conjugacy counts and twin behavior, explicit retained-state reversibility and the separately audited 8,704 quotient.

**Needs correction:** uniqueness of P from only group properties, Klein group at LEN 1, hyperoctahedral naming, scope of the master PASS claims, and presentation of inverse-as-graph versus P-facing table.

**OPEN as physical correspondence:** the deduction from a one-bit LEN extension to a discrete physical horizon area jump and any statistically meaningful model comparison of discrete combs to a measured QNM posterior.

**Source code and evidence:** `/mnt/data/nf_reaudit/independent_check.py`, `/mnt/data/nf_reaudit/independent_check.log`, `/mnt/data/nf_reaudit/catalog4.log`; the original and supplied `Native_Facing_Master_Verify_Extracted.py` were not modified. The original `Native Facing.docx` is unchanged.
