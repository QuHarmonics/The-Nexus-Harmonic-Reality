# The NEXUS Record: Relation-Vocabulary Ledger and Running Audit, §§ 1–134

Dean A. Kulik — QuHarmonics Research Group — ORCID 0009-0003-3128-8828
17 October 2026. Licence CC BY-NC 4.0.

## Abstract

This is the complete working record of the NEXUS programme in its computational phase: 134 numbered entries, each written from live program output and kept in the order it was made. The record has two parts.

**The ledger (§§ 1–98a)** starts from one finite witness, a 12-vertex graph with two tokens. It shows that every number the relation layer measures has the form ⟨m(V), f_H⟩: a multiplicity vector over the rational irreducibles of the symmetry group, paired with a reader functional f_H(λ) = dim λ^H. A zero therefore has three distinct causes: genuine absence, reader-induced flatness, or vocabulary deficiency. On the witness the first never occurs.

From there the ledger follows the interface:

- the interface between vocabulary and reader is a realization problem of width 6;
- the reader is a sampler, and the classical ledger reads its zero-frequency bin;
- the price-blind interior is the cuboctahedron, the medial graph of the witness's octahedral core;
- the two-rule walk (continue/turn) folds the plane tiling 3.4.6.4 onto a torus;
- for the scaled family Γ_n, every channel of every homology module has a closed form, and the two-token exchange class is the Z/2 of non-planar graph braid groups.

**The running audit (§§ 99–134)** keeps the same discipline under four ledger words: STANDS, RUNS, DEAD END, OPEN. It covers:

- the order channel, which is what a fold forgets;
- route codes and the reversibility of SHA-256 rounds, the per-block fold, and the price of an observer;
- the shell structure of atoms and nuclei from one capacity count and two gate conditions;
- the rings of the register stack;
- the BBP digits as column addition on a stack of rational rings.

It closes on the zero routes of BBP-type lane machines. Eight lanes give seven independent constants and one zero route. That route is the collision of the phase return and the scale return on ln 2. Z(2^e) = 1 is proved on the register chain. Off the chain, the Galois core of the returns' relations predicted seven new layers, and all seven landed as sealed.

The final entry, § 134, audits the whole record. It lists every change it made and indexes every citation that points outside the record. It recomputes every prediction seal whose file survives, and it names what has no address.

## Introduction

**What this document is.** It is not a paper; it is the trail the papers were built from. Every entry records a question, the run that answered it, and what the answer did to earlier entries. The working papers of the programme cite it, from *The Incomplete Universe* and *Distinction That Must Continue* through Working Papers 2–5. Where a paper and the record disagree, the record's correction is the later word.

**The rules it was kept under.**

- Only live output is quoted. A number in an entry was printed by a program in the session that wrote the entry.
- Predictions were sealed before data was linked: a SHA-256 hash of the prediction text, written down before the run. They are reported as landed or not.
- From § 99 on, every claim carries one of four status words:
  - **STANDS**: the result is supplied by an established theorem or measured fact;
  - **RUNS**: the result was computed here and the data landed where the route said it would;
  - **DEAD END**: the run landed, but on something else, whose owner is named;
  - **OPEN**: the question is sealed and the route is not yet written.
- Corrections are made in the entry where they arise and are never silently applied. The record therefore contains its retractions, among them an Artin minimality claim (§ 22), a false refutation (§ 46), a degree-mismatch explanation (§ 57.9), and several of the author's own and his collaborators' misreadings. These are part of the result.

**How it was made.** The work was done with AI systems in conversation: Claude as the principal executor and writer of the record, and a second lineage of GPT runs handed over as bundles. Material from the second lineage is marked as such. It is either re-run, in which case the entry says so, or entered as reported. Pasted reviews were treated as input to be tested, not as findings.

**How to read it.**

- **Parts I–VIII (§§ 1–48)** build the reader/vocabulary apparatus on the witness. They recover classical representation theory from the measurement side: Maschke, Frobenius reciprocity, Burnside's marks.
- **§§ 49–98a** move from channels to dynamics. They cover the operator family, the price field and its blind set, the method surfaces, the family Γ_n with its exchange class, the carry tower, SHA-256 as two registers, and the stored lines of the witness.
- **§§ 99–134** are the running audit. Each entry names its provenance, its seals and its status table.

Section numbers are stable, and other documents cite them. Two of them carry audit notes: § 55 is UNLINKED (its text survives in no copy), and § 98a was renumbered from a duplicate § 99.

**What it does not claim.** The arithmetic and the enumerations are exact and reproducible from the scripts named in each entry. The record has no repository, however: scripts lived in session workspaces. Provenance is therefore reproducible in principle, and archived only where a hash and a surviving file meet. § 134 lists both cases. Readings that connect a computed structure to physics or to the programme's primitives are marked as readings (PULL), separate from the counts that support them.

---

# The relation-vocabulary ledger

All numbers are live output of `ledger.py`, `ledger2.py`–`ledger5.py`, `subgrp.py`,
`walk.py`, `poset.py`, `minvoc.py`, `mech.py`, `eig.py`, `char.py` — exact rational
elimination throughout, no floating point. Substrate unless stated otherwise: the
12-vertex C4-bearing witness, K = 2. Reader stated per result.

---

# Part I — the ledger under the full automorphism reader

Reader G = Aut(X). Ceiling D = eps = dim C1_G - rank d0 = 22 - 7 = 15.

## 1. The five families and the gross defect

| family | cells | r(F) = rank d1 | cells per rank |
|---|---|---|---|
| K_disj (commuting squares) | 291 | 13 | 22.4 |
| spec4 (spectator squares) | 528 | 8 | 66.0 |
| rot4 (rotation squares) | 264 | 7 | 37.7 |
| spec3 (spectator triangles) | 180 | 10 | 18.0 |
| rot3 (rotation triangles) | 20 | 2 | 10.0 |
| ALL = K_34 | 1283 | **15 = D** | 85.5 |

Naive sum of ranks 40, union rank 15, gross defect 25. The full vocabulary
saturates the ceiling, so eps_harm(K_34) = 0 on this witness.

## 2. The budget correction

A large interaction term is not evidence of redundancy. Rank d1 can never exceed
D, so any two families whose ranks sum above D are forced to overlap before any
question of shape is asked.

    I(R,S)       = r(R) + r(S) - r(R u S)
    I_cap(R,S)   = max(0, r(R) + r(S) - D)      forced by counting alone
    I_struct     = I - I_cap                    the part that is a shape fact

| pair | r(R) | r(S) | r(RuS) | I | I_cap | I_struct |
|---|---|---|---|---|---|---|
| disj / spec4 | 13 | 8 | 14 | 7 | 6 | 1 |
| disj / rot4 | 13 | 7 | 14 | 6 | 5 | 1 |
| disj / spec3 | 13 | 10 | 15 | 8 | 8 | **0** |
| disj / rot3 | 13 | 2 | 15 | **0** | 0 | 0 |
| spec4 / rot4 | 8 | 7 | 13 | 2 | 0 | **2** |
| spec4 / spec3 | 8 | 10 | 10 | 8 | 3 | **5** |
| spec4 / rot3 | 8 | 2 | 10 | **0** | 0 | 0 |
| rot4 / spec3 | 7 | 10 | 14 | 3 | 2 | 1 |
| rot4 / rot3 | 7 | 2 | 8 | 1 | 0 | **1** |
| spec3 / rot3 | 10 | 2 | 12 | **0** | 0 | 0 |
| all squares / all triangles | 14 | 12 | 15 | 11 | 11 | **0** |

The reading inverts on two rows. disj/spec3 has the largest interaction in the
table and zero structural overlap: 13 and 10 cannot sit in a 15-dimensional space
any more independently than that. Squares against triangles, the pair one would
expect to be the real redundancy, is likewise entirely budget. Meanwhile
spec4/rot4 looks nearly orthogonal at I = 2 and is pure shape, with no counting
pressure at all.

**Superseded in part by Part III.** The scalar budget D is the right ceiling only
for a reader that sees a single isotypic component. The correct cap is computed
per irreducible, and the two rows reading I_cap = 0 for spec4/rot3 and spec3/rot3
are right at this reader for the wrong reason: the counting pressure is real and
sits in a component Aut(X) averages away. See section 17.

## 3. Pairwise recoverability is not a second measurement

    I(R,S) = dim( rowspace(R) n rowspace(S) )

by the dimension formula for subspace sums, so the rank of R that S already
determines is exactly I, and L(R|S) = r(R u S) - r(S) = r(R) - I. The RAID-style
question "which other families determine this one" returns, for two families, the
interaction term read from the other side. Same number, not new information. Only
three-or-more-family leave-one-out carries anything the pairwise table does not.

## 4. Leave-one-out: one irredundant generator

| family | r(ALL \ F) | unique = L(F \| rest) |
|---|---|---|
| K_disj | 14 | **1** |
| spec4 | 15 | 0 |
| rot4 | 15 | 0 |
| spec3 | 15 | 0 |
| rot3 | 15 | 0 |

That line is exhibited, not inferred. ker d1(ALL \ disj) has dimension 8, im d0
has rank 7, so H^1 is 1-dimensional, with integral representative mod im d0

    h = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,-1,-1,0)

supported on 3 of the 22 invariant coordinates. Cells detecting h: **96 of 291**
commuting squares, and **0** in each of the other four families. The 96 detectors
use 96 distinct disjoint base-edge pairs — one cell each, no orbit concentration.

## 5. Minimal saturating vocabularies

12 of the 31 nonempty subfamilies reach r = D = 15. Exactly two are minimal:

    {K_disj, spec3}   ranks 13 + 10 = 23,  overlapping
    {K_disj, rot3}    ranks 13 +  2 = 15,  exactly additive

So K_disj (+) rot3 is the unique exactly-additive minimal closure vocabulary under
this reader: 311 cells out of 1283, two families, no shared line, saturating.

## 6. The residue and the uninstantiated reader

eps_harm(K_disj) = 15 - 13 = 2, and rot3 has rank exactly 2 with
I(disj, rot3) = 0. So

    W_ALL = W_disj (+) W_rot3,     dim 13 (+) dim 2 = 15,

and the residue of the commuting-square vocabulary is a direct complement of the
rotation-triangle image. This reproduces, from the ledger side, Paper I section 4's
independent finding that rot3 reads the dimension-2 residue at full rank while all
1083 squares read one line.

The consequence for the Paper II classification: eps_harm(K_34) > 0 needs
girth >= 5, which is precisely the condition that **deletes** spec3, rot3, spec4
and rot4 from the arena. So on this witness the residue is not evidence that the
substrate is intrinsically harder to close; it is a direction the declared
vocabulary fails to address, and an available family closes it exactly.

**Scope.** That is a witness statement, not a theorem. "A harmonic residue is the
shape of a missing cell family, and its dimension is that family's rank" is not
established and should not be written. A residue could require a combination of
families, a family whose image is too large or too small, families absent from the
arena, or directions no catalogued family reaches. Which residues admit a
family-level complement is an open classification problem.

## 7. One containment on the witness

The containment lattice (entry = L(row | col); a zero off the diagonal is total
containment) has exactly one off-diagonal zero under Aut(X):

    L(spec4 | spec3) = 0      rowspace(spec4) <= rowspace(spec3)

Two hypotheses were run and both died.

**Chord mechanism — dead.** A chord in a base C4 would split the one-token
4-circulation into two one-token 3-circulations. The witness has 24 chordless C4s
out of 66 and the containment holds anyway.

**Theoremhood — dead.** Read with the trivial group instead:

| substrate | reader | r(spec3) | r(spec4) | L(spec4\|spec3) |
|---|---|---|---|---|
| witness 12v | Aut | 10 | 8 | **0** |
| witness 12v | trivial | 174 | 168 | **6** |
| Q3 cube (bipartite) | trivial | 0 | 24 | 24 |
| house | trivial | 2 | 1 | 1 |
| prism K3xK2 | trivial | 6 | 6 | 6 |
| K4 | trivial | 4 | 0 | 0 (vacuous) |

Same substrate, two readers, two answers. Q3 settles the general claim outright:
bipartite, so spec3 is empty, and r(spec4) = 24 > 0. Every containment in this
lattice must be reported with its reader attached. Define

    R <=_G S   iff   W_R^G is contained in W_S^G   iff   L_G(R|S) = 0,

so the reader is carried by construction: spec4 <=_{Aut(X)} spec3, and
spec4 is not <=_{1} spec3.

---

# Part II — the reader-relative lattice over the subgroup poset

Aut(X) has order 24, with 26 subgroups in 12 conjugacy classes and subgroup
orders {1:1, 2:7, 3:4, 4:7, 6:4, 8:1, 12:1, 24:1}. That profile identifies
Aut(X) = C2 x A4: a central involution z, the unique index-2 subgroup A4, and the
normal Klein four-group V4 inside it.

## 8. Two things that do not need a computation

**(T) Monotonicity.** For H1 <= H2 <= Aut(X), L_{H2}(R|S) <= L_{H1}(R|S).

*Proof.* C1^{H2} is a subspace of C1^{H1}, so restriction of functionals
rho : (C1^{H1})* -> (C1^{H2})* is defined, and for every family F,
W_F^{H2} = span{row_{H2}(c)} = span{rho(row_{H1}(c))} = rho(W_F^{H1}). Hence
rho(W_R^{H1}) = W_R^{H2} and rho(W_S^{H1}) is contained in W_S^{H2}, so rho
induces a surjection Q_{H1}(R|S) ->> Q_{H2}(R|S). Therefore
dim Q_{H2} <= dim Q_{H1}. []

So **Switch(R,S) = {H : L_H(R|S) = 0} is upward-closed**: containment cannot
appear, vanish and reappear along inclusions. Of the three regimes one might
posit — upward-closed, non-monotone, or an antichain of minimal switches — the
non-monotone regime is impossible. An antichain is not excluded.

**(U) The quotient projection carries no new scalar.** The same surjectivity gives

    dim ker( Qbar_H : Q_1(R|S) -> Q_H(R|S) ) = L_1(R|S) - L_H(R|S),

so "the reader kills exactly the previously independent quotient" is automatic
whenever containment appears, not a result. Its kernel as a *subspace* is content;
its dimension is subtraction. Likewise Q_H(R|S) = r_H(R) - I_H(R,S) = L_H(R|S):
naming the loss as a quotient dimension says what the number is, and adds no
measurement.

## 9. The representation theorem

**(R) L_H(R|S) = dim (Q_1(R|S))^H.**

*Proof.* Over Q with |H| invertible, restriction to C1^H is the Reynolds projector
onto H-invariants, so W_F^H = (W_F^1)^H for every family F. Taking H-invariants is
exact (Maschke), so

    Q_H = (W_R^1)^H / (W_R^1 n W_S^1)^H = ( W_R^1/(W_R^1 n W_S^1) )^H = (Q_1)^H. []

This subsumes (T) — invariants shrink as H grows — and collapses the entire
subgroup walk into **one character of Aut(X)**. The subgroup thresholds are
readouts of that character, not independent facts.

## 10. The measured walk

One representative per conjugacy class. `z?` = contains the central involution;
`<=A4?` = lies inside the index-2 subgroup.

| id | \|H\| | class | z? | <=A4? | dim C1 | rank d0 | D | r(ALL) | residue | L(s4\|s3) | uniq disj | containments |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | n | y | 300 | 65 | 235 | 235 | 0 | 6 | 12 | – |
| 1 | 2 | 3 | n | n | 186 | 47 | 139 | 139 | 0 | 3 | 8 | – |
| 2 | 2 | 3 | n | y | 152 | 37 | 115 | 115 | 0 | 2 | 6 | – |
| 3 | 2 | 1 | y | n | 150 | 35 | 115 | 115 | 0 | 3 | 6 | – |
| 4 | 3 | 4 | n | y | 100 | 21 | 79 | 79 | 0 | 2 | 4 | – |
| 5 | 4 | 3 | n | n | 112 | 33 | 79 | 79 | 0 | 1 | 5 | – |
| 6 | 4 | 3 | y | n | 94 | 27 | 67 | 67 | 0 | 1 | 4 | – |
| 7 | 4 | 1 | n | y | 78 | 23 | 55 | 55 | 0 | **0** | 3 | spec4 <= spec3 |
| 8 | 6 | 4 | y | n | 50 | 11 | 39 | 39 | 0 | 1 | 2 | – |
| 9 | 8 | 1 | y | n | 66 | 23 | 43 | 43 | 0 | **0** | 3 | spec4 <= spec3 |
| 10 | 12 | 1 | n | y | 26 | 7 | 19 | 19 | 0 | **0** | 1 | spec4 <= spec3 |
| 11 | 24 | 1 | y | n | 22 | 7 | 15 | 15 | 0 | **0** | 1 | spec4 <= spec3 |

Family ranks, same order of ids 11, 10, 9, 8, 5, 6, 7, 4, 1, 2, 3, 0:

| \|H\| | disj | spec4 | rot4 | spec3 | rot3 |
|---|---|---|---|---|---|
| 24 | 13 | 8 | 7 | 10 | 2 |
| 12 | 17 | 12 | 10 | 14 | 3 |
| 8 | 39 | 24 | 21 | 30 | 4 |
| 6 | 35 | 28 | 24 | 29 | 4 |
| 4 (id 5) | 72 | 48 | 44 | 55 | 7 |
| 4 (id 6) | 61 | 44 | 38 | 49 | 6 |
| 4 (id 7) | 51 | 36 | 30 | 42 | 5 |
| 3 | 72 | 56 | 50 | 58 | 8 |
| 2 (id 1) | 127 | 92 | 84 | 99 | 12 |
| 2 (id 2) | 106 | 80 | 70 | 86 | 10 |
| 2 (id 3) | 105 | 84 | 72 | 87 | 10 |
| 1 | 216 | 168 | 150 | 174 | 20 |

Four facts hold at every one of the twelve readers:

1. **residue = 0.** D_H - r_H(ALL) = 0 from D = 15 up to D = 235. The five-family
   vocabulary saturates at every symmetry level, including no symmetry at all.
2. **K_disj is the only family with unique rank**, at all twelve. spec4, rot4,
   spec3 and rot3 are fully recoverable from the rest under every reader. The
   *location* of the irreducible channel is reader-invariant; its *dimension* is
   not — it runs 1, 1, 1, 2, 3, 3, 3, 4, 4, 5, 6, 6, 8, 12 across the classes.
3. **spec4 <= spec3 is the only containment that ever occurs** among all 20
   ordered family pairs at any of the twelve readers. Every other entry of every
   containment matrix is nonzero.
4. **The minimal saturating vocabularies are exactly {disj, spec3} and
   {disj, rot3}**, at every reader, and r_H(disj u rot3) = D_H at every reader
   including the trivial one (216 + 20 -> 235 = D).

Monotonicity check of (T): **0 violations** over 1000 ordered (family-pair,
inclusion) tests across the poset.

## 11. The switch boundary

    Switch(spec4, spec3) = { ids 7, 9, 10, 11 }   orders 4, 8, 12, 24

with a **unique minimal element**: id 7, order 4, class size 1 (normal), inside
A4, all non-identity elements of order 2 — the normal Klein four-group V4. From
the poset, [7] is contained in [9], [10], [11] and in nothing else of Switch, so

    Switch(spec4, spec3) = the principal filter generated by V4.

Not an antichain. A single named generator.

## 12. The address is a character, not a subgroup

Q_1(spec4|spec3) is 6-dimensional. Fitting its character on the five cyclic
classes alone and predicting the seven non-cyclic ones:

    chi(1) = 6,  chi(z) = 0,  chi(v) = -2 for v in V4\1,  chi(zv) = 0,
    chi = 0 on every element of order 3 and 6.
    <chi,chi> = 2.

All twelve classes reproduced; **6 of 6 held-out classes predicted correctly**.
And <chi,chi> = 2 with dimension 6 forces two distinct irreducibles each of
multiplicity one, which in C2 x A4 (irrep dimensions 1,1,1,3,1,1,1,3) can only be
3 + 3. Matching values identifies them:

    Q_1(spec4|spec3)  =  rho+  (+)  rho-

the standard 3-dimensional representation of A4 tensored with each of the two
characters of the central C2.

That is the address, and it explains the boundary rather than recording it. The
3-dimensional A4 representation restricted to V4 is the sum of V4's three
nontrivial characters, with no trivial summand — which is exactly why V4 is the
minimal switch subgroup. The six spectator-square-only directions do not go
anywhere. They carry an isotypic label, and a reader sees them precisely when its
restriction of that label still has invariants.

## 13. A second address, with its mechanism

Exact additivity of the minimal vocabulary flickers by one dimension across the
walk. I_H(disj, rot3) = 1 for ids 0, 2, 4, 7, 10 and 0 for ids 1, 3, 5, 6, 8, 9,
11. That partition is exactly `<=A4?`:

    I_H(K_disj, rot3) = 1  iff  H is contained in A4.      12 of 12.

The mechanism was found by killing one first. **Reversible orbits — dead.** A
reversible arena-edge orbit is forced to zero in the invariant basis, which would
delete a coordinate; but the witness arena has **0 reversible orbits at every one
of the twelve readers** (edge-orbit count equals dim C1 exactly, at all twelve),
so that machinery never fires here.

The surviving route: at the trivial reader I = 1, so W_disj n W_rot3 is a *line*.
Both families are stable under every automorphism, so the line is too, and the
central involution acts on it by +1 or -1. Measured: the spanning direction v has
support 24 of 300 with entries in {-1, 0, +1}, and

    z . v = -v.

Restricting v to invariant coordinates: under A4, 2 nonzero coordinates — it
survives; under <z>, 0; under Aut(X), 0. So v sits in the sign character of
Aut(X)/A4, and Reynolds averaging over any reader that meets the non-A4 coset
cancels it. Readers inside A4 keep it. Same conclusion as section 12 in a
different isotypic component: the address of an unreadable relation direction is a
character of the reader group, and the subgroup threshold is its shadow.

## 14. What is general and what is witness-specific

General, proved: (T) monotonicity, (U) the two collapses, (R) L_H = dim (Q_1)^H,
and the consequence that every subgroup walk of this kind is one character.

Witness-specific, measured: Aut(X) = C2 x A4; residue 0 at all twelve readers;
K_disj the sole carrier of unique rank; spec4 <= spec3 as the only containment;
Switch = the filter above V4; Q_1(spec4|spec3) = rho+ (+) rho-; the A4 criterion
for additivity and the z-anti-invariance of the shared line.

Not established, and not to be written: that a harmonic residue is in general the
shape of a missing cell family; that any of the Part II patterns hold on another
substrate. The next substrate should be chosen to break one of them, not to
reproduce them.

---

# Part III — the ledger is one table, and a reader is a functional

Nothing below rebuilds an arena or computes a rank. It is arithmetic on the
twelve-number columns already measured, read through the character table of
Aut(X) = C2 x A4. The rational irreducibles are 1+, 1-, 2+, 2-, 3+, 3- of
dimensions 1, 1, 2, 2, 3, 3 (the trivial, the sign of the central C2, the
2-dimensional rational irreducible of A4 and its sign twist, and the standard
3-dimensional A4 representation and its sign twist).

## 15. Every column is a module, and the ledger is 9 x 6

By (R), each ledger quantity at reader H is dim V^H for a module V fixed
independently of H, so each measured column must satisfy
dim V^H = sum_lambda m_lambda * dim(lambda^H). Twelve equations, six unknowns:
solving is also a 54-fold consistency check on the whole table. **All nine
columns solve exactly.**

| module | 1+ | 1- | 2+ | 2- | 3+ | 3- | dim |
|---|---|---|---|---|---|---|---|
| C1 | 22 | 4 | 22 | 4 | 28 | 46 | 300 |
| ambient (C1 / im d0)* | 15 | 4 | 14 | 4 | 24 | 36 | 235 |
| W_disj | 13 | 4 | 13 | 4 | 22 | 33 | 216 |
| W_spec4 | 8 | 4 | 8 | 4 | 20 | 24 | 168 |
| W_rot4 | 7 | **3** | 7 | **3** | 17 | 23 | 150 |
| W_spec3 | 10 | 4 | 10 | 4 | 19 | 25 | 174 |
| W_rot3 | 2 | 1 | 1 | 0 | 2 | 3 | 20 |
| Q(spec4\|spec3) | 0 | 0 | 0 | 0 | 1 | 1 | 6 |
| the unique-disj channel | 1 | 0 | 1 | 0 | 1 | 2 | 12 |

The reader contributes the other factor, and nothing else:

| H | 1+ | 1- | 2+ | 2- | 3+ | 3- |
|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 2 | 2 | 3 | 3 |
| 2, not <=A4 | 1 | 0 | 2 | 0 | 1 | 2 |
| 2, <=A4 | 1 | 1 | 2 | 2 | 1 | 1 |
| 2 = <z> | 1 | 0 | 2 | 0 | 3 | 0 |
| 3 | 1 | 1 | 0 | 0 | 1 | 1 |
| 4, not <=A4, no z | 1 | 0 | 2 | 0 | 0 | 1 |
| 4, with z | 1 | 0 | 2 | 0 | 1 | 0 |
| 4 = V4 | 1 | 1 | 2 | 2 | 0 | 0 |
| 6 | 1 | 0 | 0 | 0 | 1 | 0 |
| 8 | 1 | 0 | 2 | 0 | 0 | 0 |
| 12 = A4 | 1 | 1 | 0 | 0 | 0 | 0 |
| 24 | 1 | 0 | 0 | 0 | 0 | 0 |

So, in full generality for this apparatus:

    every ledger number at reader H  =  < m(V) , dim(lambda^.)^H >.

**A reader contributes only the fixed-vector functional f_H(lambda) =
dim(lambda^H); the multiplicity module is reader-independent.** This is not a
tensor factorization of the relation space — it is the statement that one side of
every ledger number is fixed once and the other is chosen by the reader. Three
columns recovered this way, against their measured values: r_H(rot3) = 20, 12, 10, 10, 8, 7, 6, 5, 4, 4,
3, 2; L_H(spec4|spec3) = 6, 3, 2, 3, 2, 1, 1, 0, 1, 0, 0, 0; unique_H(disj) = 12,
8, 6, 6, 4, 5, 4, 3, 2, 3, 1, 1.

The consequence for Part I's framing: containment, redundancy, saturation and
irreducibility are **not** properties of the pair (X, G). They are properties of
X, recorded once as a multiplicity table, evaluated at G. Part I section 7 said
the reader owns the containment lattice. More precisely: **the reader does not
change the multiplicity module; it changes only which fixed-vector dimensions
are visible.**

Scope on the slogan. What is established is: *within the finite-reader rational
representation apparatus, the relation field is completely represented, for
reader evaluation, by its multiplicity vector.* That is a statement about this
apparatus. It is not a claim that a physical or geometric field is a multiplicity
vector.

## 16. One line replaces the program

Define the deficiency of a family as what it cannot read, as a module:
m(ambient) - m(F).

| family | deficiency | dim | families whose vector dominates it |
|---|---|---|---|
| disj | (2,0,1,0,2,3) | 19 | spec4, rot4, spec3, **rot3** |
| spec4 | (7,0,6,0,4,12) | 67 | disj, rot4, spec3 |
| rot4 | (8,1,7,1,7,13) | 85 | disj, spec4, spec3 |
| spec3 | (5,0,4,0,5,11) | 61 | disj, spec4, rot4 |
| rot3 | (13,3,13,4,22,33) | 215 | disj |

And then:

    m(rot3)  =  ( m(ambient) - m(disj) )  +  (0,1,0,0,0,0).

**The rotation-triangle family is the exact isotypic complement of the commuting
squares in the ambient, plus one redundant copy of the sign character 1-.** Six
integers.

**One correction to make first.** The multiplicity identity alone does *not*
entail saturation: two multiplicity-one submodules of lambda^(+2) can coincide,
so m(R) + m(S) = m(A) + e does not force W_R + W_S = A. What does the work is
section 16a. With saturation in hand at a single faithful reader, the identity
then entails, with no further measurement:

- r_H(disj u rot3) = D_H at all twelve readers;
- I_H(disj, rot3) = dim(1-)^H, hence = 1 exactly when H <= A4 and 0 otherwise —
  the 12-of-12 additivity pattern of section 13 is that one redundant copy;
- the exhibited line with z.v = -v is that copy, and its z-eigenvalue -1 is just
  the statement that 1- is the sign character;
- eps_harm(disj) = 19 at the trivial reader and 2 at Aut(X), both as contractions
  of the same deficiency vector;
- Paper I section 4's rank-access result.

Likewise W_ALL = ambient as modules — residue 0 at all twelve readers is one
identity, not twelve facts — and Q(spec4|spec3) = 3+ (+) 3- reproduces the whole
switch filter, since 3+ and 3- both have no fixed vector exactly at V4, C2 x V4,
A4 and C2 x A4.

## 16a. A faithful reader, and the cheapest one

**Lemma.** Call H *faithful* if f_H has every entry positive, i.e. every
irreducible of G has an H-fixed vector. For submodules U contained in V, a single
equality dim U^H = dim V^H at a faithful H forces m(U) = m(V), hence U = V, hence
dim U^K = dim V^K for **every** reader K.

*Proof.* m(U) <= m(V) componentwise, f_H > 0 componentwise, and
<m(V) - m(U), f_H> = 0 force m(V) - m(U) = 0. []

Equivalently, H is faithful iff Q[G/H] contains every irreducible of G. So any
containment, saturation or domination statement verified at one faithful reader
propagates to the whole poset for free. Eleven of the twelve saturation
measurements were redundant a priori.

Exactly two of the twelve classes are faithful here:

| reader | f_H | dim C1 | D |
|---|---|---|---|
| trivial | (1,1,2,2,3,3) | 300 | 235 |
| order 2 inside A4 | (1,1,2,2,1,1) | **152** | **115** |

The second works because v in V4 lies in A4 (so 1- stays visible), V4 lies in the
kernel of A4's linear characters (so 2+ and 2- stay full), and the standard
3-dimensional representation restricted to an involution keeps one invariant.

**Faithfulness is downward-closed, so "cheapest" needs no search.** If H1 <= H2
then dim(lambda^{H1}) >= dim(lambda^{H2}) for every lambda — fewer constraints,
more invariants — verified with 0 violations across the poset. Hence the faithful
readers form an **order ideal** in the subgroup lattice, and the minimal
apparatus sits at that ideal's **maximal** elements. The domain is the twelve
conjugacy classes, not a search over arbitrary linear quotients, and here the
frontier is a single class:

    faithful ideal = { trivial, order-2 inside A4 },  unique maximal element
    the order-2 class,  dim C1 = 152,  D = 115.

So the minimal faithful apparatus is not the trivial reader. Half the
coordinates, and nothing goes dark: every isotypic component still has a
readout. Above the frontier, components start going dark; below it, the extra
coordinates carry no new isotypic channel. That is the exact form of the local
isolator — and note the inversion of names: the *largest* faithful subgroup
gives the *smallest* complete apparatus.

## 17. The scalar budget was the wrong ceiling

Two submodules of a semisimple module are forced to meet inside each isotypic
component separately, so the correct cap is

    I_cap^iso(R,S;H) = sum_lambda max(0, m_l(R) + m_l(S) - m_l(ambient)) * dim(lambda^H),

while the scalar cap max(0, r_H(R) + r_H(S) - D_H) is the same sum with the max
taken *outside*. They agree exactly when the excess vector has one sign on the
components H can see, and differ otherwise.

| pair | excess vector | mixed sign | readers where the caps differ |
|---|---|---|---|
| disj/spec4 | (6,4,7,4,18,21) | no | – |
| disj/rot4 | (5,3,6,3,15,20) | no | – |
| disj/spec3 | (8,4,9,4,17,22) | no | – |
| disj/rot3 | (0,1,0,0,0,0) | no | – |
| spec4/rot4 | (0,3,1,3,13,11) | no | – |
| spec4/spec3 | (3,4,4,4,15,13) | no | – |
| **spec4/rot3** | (-5,1,-5,0,-2,-9) | **yes** | H = 1, 2(<=A4), 3, V4, A4 — iso 1, scalar 0 |
| rot4/spec3 | (2,3,3,3,12,12) | no | – |
| rot4/rot3 | (-6,0,-6,-1,-5,-10) | no | – |
| **spec3/rot3** | (-3,1,-3,0,-3,-8) | **yes** | H = 1, 2(<=A4), 3, V4, A4 — iso 1, scalar 0 |

So "spec4/rot3: I = 0, I_cap = 0, I_struct = 0, exact independence" in section 2
is numerically right at the Aut(X) reader and structurally mis-assigned. The
counting pressure is real — one copy of 1- — and Aut(X) averages it to zero. The
table entails that spec4 and rot3, and spec3 and rot3, are forced to share a
dimension at every reader inside A4. Every family except rot4 carries the full
1- multiplicity 4 of the ambient; rot3 carries one copy, which therefore sits
inside everyone's. **rot4 is the only family deficient in the minus sector**
(m_{1-} = m_{2-} = 3 against 4), which is exactly why rot4/rot3 is the one pair
with no forced overlap at any reader.

## 18. What this settles in the program's own terms

**Unreadable is not absent, as a computation.** Genuine flatness is m(V) = 0.
Apparent flatness is m(V) =/= 0 with <m, dim(lambda^.)^H> = 0. These look
identical from the surface and are now told apart by reading the multiplicity
vector, with no search over readers: the readers that see V are exactly
{ H : <m(V), dim(lambda^.)^H> > 0 }. Q(spec4|spec3) is the worked case — the same
6-dimensional module at all twelve readers, invisible at four of them.

**The continuation constraint is semisimplicity — stated carefully.** Maschke
guarantees a G-stable complement for every declared vocabulary submodule
W <= A. The isotypic decomposition A = (+)_lambda A_lambda is canonical; a
particular complement inside a multiplicity space is **not** — a submodule of
lambda^(+m) with m > 1 admits many G-stable complements. That is the same
ambiguity section 16 corrects, and it must not be papered over here.

The transverse statement also runs the other way from an earlier draft of this
record. A transverse quotient exists when the vocabulary is **incomplete**:

    eps_harm > 0  <=>  W_declared properly contained in A  <=>  A/W_declared =/= 0,

and semisimplicity then supplies some W' =/= 0 with A = W_declared (+) W' and
W' isomorphic to A/W_declared. The isomorphism class, hence the multiplicity
vector, is determined; the choice of complement is not. So: **a nonzero harmonic
residue is the nonzero quotient left by an incompletely spanning vocabulary.**
No metric and no right angle is involved, and on this witness rot3 realizes one
such complement for the commuting squares after certification — a measured fact,
not a guarantee that a named family realizes every residual quotient.

**The isolator is the reader.** Passing from the trivial group to Aut(X) discards
278 of 300 coordinates and returns a 15-dimensional ledger in which 1283 cells
reduce to 311, disj (+) rot3 is an exact direct sum, and one line names the
irreducible channel. Fewer degrees of freedom, more legible response — and
nothing left the field: the discarded components are still in the table with
nonzero multiplicity. Selective coupling is which lambda have fixed vectors.

**Cell families are methods.** Each family determines a submodule of the ambient
relation module, and that submodule's multiplicity vector records its isotypic
reach — which components it can address at all. The levels are distinct and
should stay distinct: an individual cell is one relation row; a family is a
selected set of cells; the method image is the submodule W_F they span; the
reach is m(W_F); certified closure is a proven equality W_{F1} + ... + W_{Fk} = A.
Commuting squares, spectator triangles and rotation triangles are three rows of
the table, not three descriptions of one cell.

**Reading a missing method without searching — and the exact limit of it.**
Subtract: delta(F) = m(ambient) - m(F) is what the vocabulary cannot reach, and
only a family whose multiplicity vector dominates delta componentwise can close
it. That is **necessary and provably not sufficient**, because multiplicities
record an inventory and not which copy of an irreducible a submodule occupies:
two multiplicity-one submodules of lambda^(+2) can coincide. The witness already
contains both outcomes. delta(disj) = (2,0,1,0,2,3), and all four other families
dominate it, but certified at the maximal faithful reader (id 2, D = 115):

| family | dominates delta(disj) | r(disj u F) | closes? |
|---|---|---|---|
| spec4 | yes | 114 | **no** |
| rot4 | yes | 114 | **no** |
| spec3 | yes | 115 | yes |
| rot3 | yes | 115 | yes |

Two of the four dominators fall exactly one dimension short. So the sound method
is subtraction and domination to **shortlist**, then one span check at a faithful
reader to **certify** — and the certificate propagates to every reader by section
16a. Search over 31 subsets crossed with 12 readers is replaced by a six-column
subtraction plus one certification.

## 19. Scope

General, proved: (T), (U), (R), and the consequence that every quantity of this
apparatus at reader H is <m(V), dim(lambda^.)^H> for a reader-free module V,
hence that the entire reader lattice is one multiplicity table evaluated at
points. The isotypic cap and its agreement criterion with the scalar cap are
general. Maschke as the continuation guarantee is general for finite readers
over Q.

Witness-specific, measured: the 9 x 6 table itself, and everything read off it —
the complement identity for rot3, the 1- line, Q(spec4|spec3) = 3+ (+) 3-, the
minus-sector deficiency of rot4.

Entailed by the table and since **verified directly**. The prediction was that
spec4/rot3 and spec3/rot3 have forced overlap exactly 1 at the five readers
inside A4, where the scalar cap reports 0. Measured by row-space intersection:

| id | \|H\| | <=A4 | D_H | r(spec4) | r(spec3) | r(rot3) | I(s4,r3) | I(s3,r3) | iso cap | scalar |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | y | 235 | 168 | 174 | 20 | **1** | **1** | 1 | 0 |
| 2 | 2 | y | 115 | 80 | 86 | 10 | **1** | **1** | 1 | 0 |
| 4 | 3 | y | 79 | 56 | 58 | 8 | **1** | **1** | 1 | 0 |
| 7 | 4 | y | 55 | 36 | 42 | 5 | **1** | **1** | 1 | 0 |
| 10 | 12 | y | 19 | 12 | 14 | 3 | **1** | **1** | 1 | 0 |
| 3 | 2 | n | 115 | 84 | 87 | 10 | 0 | 0 | 0 | 0 |
| 9 | 8 | n | 43 | 24 | 30 | 4 | 0 | 0 | 0 | 0 |

14 of 14 agree with the isotypic cap and disagree with the scalar one. The
isotypic cap is attained exactly, and the module-extraction pipeline is checked
independently of the character arithmetic that produced it.

## 20. The frozen record

The ledger stops being a growing list of rank tables. The durable objects are:

| object | symbol | role |
|---|---|---|
| ambient module | m(A) | the total available relation capacity, per irreducible |
| family submodules | m(F) | what each cell shape can reach at all |
| deficiency | delta(F) = m(A) - m(F) | what a declared vocabulary cannot reach |
| isotypic capacity | I_cap^iso(R,S;H) | forced overlap, counted per sector then contracted |
| reader functional | f_H(lambda) = dim(lambda^H) | the reader, entirely |
| reader-visible value | < m(V), f_H > | every ledger number ever measured |
| span certificate | one equality at a faithful H | what turns an inventory into a closure |

And three algebraically distinct failure modes, which earlier wording conflated
into a single "zero":

| condition | diagnosis |
|---|---|
| m_lambda(V) = 0 | **genuine absence** — the channel is not in the module |
| m_lambda(V) > 0 and dim(lambda^H) = 0 | **reader-induced flatness** — the channel exists, this reader has no fixed readout of it |
| m_lambda(F) < m_lambda(V) | **vocabulary deficiency** — the family does not reach the available multiplicity in that sector |

A zero at a reader is an evaluation result. A zero in the multiplicity vector is
an existence result. The three readers of this witness sit at three different
points of that distinction:

| reader | dim C1 | f_H | what it is |
|---|---|---|---|
| trivial | 300 | (1,1,2,2,3,3) | raw field, every channel fully visible |
| order 2 in A4 | 152 | (1,1,2,2,1,1) | minimal faithful apparatus, every channel still visible |
| Aut(X) | 22 | (1,0,0,0,0,0) | maximal compression, only the trivial sector visible |

The third is why the scalar ledger reported two interactions as zero. It is
legible and blind in five of six sectors, and its zeros cannot be read as
structural absence without the multiplicity table.

The operating rule, in order: extract multiplicities, identify the visible
sectors, evaluate at the reader, and certify any claimed closure at a faithful
reader. That blocks three distinct errors — calling an unreadable component
absent, calling scalar slack genuine independence, and calling multiplicity
coverage an actual span.


---

# Part IV — direction of arrival, and one retraction

## 21. The collision is the validation, not a disclosure

The general layer of this work — reader evaluation, the detection of a rational
module by its fixed-point dimensions, the faithful-reader argument, the isotypic
intersection bound — is classical representation theory. A literature check
pinned the attributions: representations over a characteristic-zero field are
determined by their characters (Serre, Thm. 4 Cor. 2); rational characters are
detected on cyclic subgroups (Artin; Serre, Thm. 17); and the exact analogue for
G-sets is Burnside's theorem on marks, with the mark homomorphism injective
(Bouc, Thm. 2.3.2 and §3.2).

The direction of travel is the point. None of this was an input. The route ran
constraint → arena → cells → readers → measured ranks → a linear system →
multiplicity vector, and the classical principle was recognised at the end rather
than applied at the start. A framework that only ever produces its own objects
cannot be wrong about anything. The moment it lands on a theorem with an
independent proof and a 1931 date, it becomes checkable. So the attribution
section of the paper is written as a result and not as an apology.

## 22. The retraction

In the turn that found the attributions I also claimed that the minimal set of
readers determining the multiplicity vector **was** the six cyclic classes, and
called that Artin's shape reproducing itself. That was false, and it was my own
search order talking: the enumeration broke at the first size-6 subset it found,
in lexicographic order, which happened to be the cyclic one.

Enumerated properly, of the 4095 nonempty subsets of the twelve reader classes:

- 1527 determine m(V);
- 357 of those are minimal, all of size 6;
- exactly **1** of the 357 lies inside the cyclic classes, and **356** use a
  non-cyclic class;
- the six non-cyclic classes alone also determine (rank 6);
- no class appears in all 357.

Artin gives sufficiency of cyclic subgroups, not necessity or minimality. The
cyclic classes are not distinguished here, and I manufactured a prettier
convergence than the one the data supports.

## 23. Weak and strong collision

Two things were being conflated and should not be:

| form | what it is | what we have |
|---|---|---|
| weak | the framework touched known mathematics | yes — Artin, Burnside, Serre |
| strong | the framework made a statement about reality that could have been false, and was not | yes — Table 8 |

Recognising a classical theorem after the fact is corroboration: it shows the
apparatus is pointed outward. It is not a test, because the recognition cannot
fail once the result is known. The test in this work is the 14-of-14 regression:
the multiplicity table asserted two forced overlaps that the scalar account
reported as zero, the assertion was made before the measurement, direct
row-space intersection could have returned zero, and it returned one at every
reader inside A4 and zero at both controls.

That is the answer to the sandbox objection, and it is worth stating in the
general form. Contact with reality is not established by vocabulary overlap with
a known field. It is established by a prediction with a failure mode, and by
reproducibility — the witness is 30 edges, and anyone can rerun the table.

---

# Part V — two fields, and the width of the interface between them

## 24. The apparatus has two slots, and they do not substitute

Every visible number in this work is ⟨ m(W), f_H ⟩ — a bilinear pairing with a
**vocabulary** slot and a **reader** slot. The question is whether that is two
fields or one field with two readouts, and it is decidable rather than a matter
of naming.

**Measurement.** Build the full two-way table: 12 reader classes × all 31
nonempty vocabularies, entry r_H(union of the families). Its rank is the number
of independent channels through which the two sides communicate.

    rank = 6 = the number of rational irreducibles of Aut(X).

Not 1, so the table does not factor: this is not one field with a scale on each
side. Not 12 or 31 either — the two sides meet in a space smaller than either
of them.

**Non-substitutability, exhibited.** The two slots fail on different indices and
neither can repair the other:

| failure | instance | scope |
|---|---|---|
| vocabulary zero | m(rot3) has 2⁻-multiplicity 0 | invisible at **every** reader |
| reader zero | V₄ has no fixed vector in 3⁺, 3⁻ | invisible for **every** vocabulary |

Different components, absolute across the other slot. A richer vocabulary cannot
open what V₄ closes; a weaker reader cannot close what rot3 never reached.

## 25. Where the cut goes

The natural prose mapping — "the arena drives, the family and reader control" —
puts the cut in the wrong place, and the rank measurement is what shows it. If
family and reader were both on the control side, the table would factor along
that grouping. It does not.

| term | object | question it answers |
|---|---|---|
| the field | ambient module A | what relation directions exist at all |
| drive | the declared family, m(W_F) | which encounters are counted as relations |
| control | the reader, f_H | which of them survive to be read |

A is not a third field. It is the space both slots act in. A cell is already a
forced encounter — a closed walk where token histories collide and return — so
choosing a cell family is choosing which collisions count. The reader then
decides whether a counted collision leaves a readable residue or averages to
zero.

## 26. The width is a measurement, not a constant — now measured

The interface width is bounded above by |Irr(G)| always, since both slots factor
through ℚ^|Irr|. Attaining the bound is contingent. Section 25 asserted that a
poorer vocabulary would give a strictly narrower interface; that was a
prediction, and it has now been run. Width as a function of which families are
available to the drive side, same group and same ambient module throughout:

| families available | #vocabularies | width |
|---|---|---|
| any one | 1 | 1 |
| any two | 3 | 3 |
| disj+spec4+rot4 | 7 | **4** |
| disj+spec3+rot3 | 7 | **4** |
| five other triples | 7 | 5 |
| spec4+rot4+rot3 | 7 | **6** |
| rot4+spec3+rot3 | 7 | **6** |
| disj+spec4+rot4+spec3 | 15 | **5** |
| the other four 4-sets | 15 | 6 |
| all five | 31 | 6 |

So width runs 1, 3, 4, 5, 6 with the group and the ambient module fixed. More
than that: **width depends on which families, not how many.** Three families can
give 4, 5 or 6; four families can give 5 or 6. A three-family collection
saturates while a four-family collection does not, and the four-family
collection that fails is exactly the one omitting rot3.

## 26a. The deficit is one linear functional

Not a correlation — a mechanism. Every union multiplicity vector buildable from
the four families other than rot3 lies in a hyperplane of multiplicity space.
Its annihilator is one-dimensional and the functional is

    φ  =  m(2⁻) − m(1⁻).

φ vanishes on all 15 rot3-free unions, on each of disj, spec4, rot4 and spec3
individually, and on the ambient module A itself, which is φ-balanced with
m(1⁻) = m(2⁻) = 4. The rot3-free span is exactly the 5-dimensional hyperplane
φ = 0. And

    φ( m(rot3) )  =  −1,

the unique escape among the five available families: m(rot3) = (2,1,1,0,2,3) has
m(1⁻) = 1 and m(2⁻) = 0.

Hence the criterion on this witness: **width = 6 iff the vocabulary contains a
family off the hyperplane φ = 0, with the rest spanning the hyperplane.** The
sixth channel is invisible from the ambient module alone, because A sits on
φ = 0; it is visible only because one 20-cell family is unbalanced.

This is the drive-side analogue of the reader-side result. A reader can be blind
in a sector (V₄ in 3±); a vocabulary can be confined to a hyperplane of the
channel space. Neither repairs the other, and now both failures have an explicit
witness — a subgroup for the control side, a linear functional for the drive
side.

So "two fields" is not a framing. It is a number:

    interface width  =  rank of the reader × vocabulary table  ≤  |Irr(G)|,

with equality exactly when the drive side exercises every channel the control
side offers.

## 27. The residue is not a third field

A residue A/W is a module, and the method of Section 11 consumes it: the
deficiency of one vocabulary is the specification the next family must dominate.
So the third term in the drive–control–residue picture is not a third field. It
is the output re-entering the drive slot as a requirement. That is exactly what
the rot3 result is: the residue of 𝒦_disj, read as a specification, was matched
by a family already present in the arena.

---

# Part VI — the map: this is a realization problem

## 28. Where the apparatus already exists

M = F·Vᵀ is an input/output matrix factored through a state space. That is the
Ho–Kalman setup, and the correspondence is structural rather than suggestive:

| ours | control theory | VLSI test |
|---|---|---|
| vocabulary m(W_F) | input / reachability | controllability |
| reader f_H | output / observability | observability |
| irreducible λ | state coordinate | node |
| width = rank M | McMillan degree of the minimal realization | — |
| drive zero (φ) | unreachable subspace | uncontrollable node |
| reader zero (V₄ on 3±) | unobservable subspace | unobservable node |
| non-substitutability | Kalman decomposition | a fault is detectable iff **both** |

Looser maps, same shape but different machinery: an OOP interface exposes a
subset of an object's behaviour, so two interfaces on one object are two readers
and the object is the ambient module; abstract interpretation (Cousot & Cousot
1977) makes the reader a Galois abstraction α, and "unreadable is not absent" is
exactly incompleteness of an abstract domain — a property true concretely and
inexpressible in the abstraction; non-interference (Goguen–Meseguer 1982) is
reader blindness in the security dialect. These are order-theoretic where ours is
linear, so they share the shape and not the theorems.

The test of a map is whether it imports a theorem or predicts a measurement.
Control theory did both. The others, so far, supply vocabulary only, and should
be cited as cousins rather than used.

## 29. What the map told us to do, and what it found

Twelve turns of this work varied the vocabulary and held the reader set fixed at
all twelve classes. The Kalman decomposition says vary **both**, because the
minimal realization is the reachable-**and**-observable part, not the smaller of
the two. Done:

| vocabulary | readers | reach | obs | width | min |
|---|---|---|---|---|---|
| all five | all 12 | 6 | 6 | 6 | 6 |
| all five | {V₄, C₂×V₄, A₄, G} | 6 | 4 | 4 | 4 |
| rot3-free | all 12 | 5 | 6 | 5 | 5 |
| **rot3-free** | **{V₄, C₂×V₄, A₄, G}** | **5** | **4** | **3** | **4** |
| **squares only** | **{V₄, C₂×V₄, A₄, G}** | **4** | **4** | **2** | **4** |
| disj alone | any | 1 | – | 1 | 1 |

**Width is not min(reach, obs).** Two rows come in strictly under it. That is the
signature of a genuine two-sided decomposition: when both the reachable and the
observable subspaces are proper, the realization is their intersection, and an
intersection can be strictly smaller than either. A one-sided bottleneck model
would have predicted 4 and 4; the apparatus returns 3 and 2.

So the thesis of Paper IV is not "there are two fields." It is:

    the relation layer is a realization problem, and the interface width is the
    dimension of its minimal realization.

That is a map onto sixty-five years of theory with importable results, and it
arrived by looking for where the work had already been done rather than by
building another substrate.

## 30. How much observation a vocabulary needs

Compiler form of the question: how many probe points before a program's behaviour
is fully distinguished? Measured over all 31 vocabularies:

- **The count is fungible.** A minimal probe set has size exactly reach(V), for
  all 31 — never more. 0 of 31 need extra probes.
- **The placement is not.** At reach 6, only 357 of the 924 six-reader subsets
  work. At reach 3 it ranges from 131 of 220 (spec4+spec3) to 218 of 220
  (rot4+spec3).

So the number of observers a drive side requires is set by its reach, while which
observers will do depends on the drive side and varies by a factor of nearly two.
That is the design-for-test fact exactly: the scan-chain length is set by the
state dimension, the placement by the circuit.

## 31. The interface is computable; conformance to it is not sufficient

The deficiency vector δ(F) = m(A) − m(W_F) is a specification in the exact
programming sense: it states what a closing method must satisfy, it is computable
from the field alone, and it is written before any implementation is named. In
that sense the interface is already there, and rot3 was not authored — its 20
cells were in the arena the moment the edge list was fixed. We found a matching.

But Table 10 measures the limit of that reading, and it is the sharpest collision
with the OOP end of the stack. **Four families satisfy δ(𝒦_disj) by domination;
only two close it.** spec4 and rot4 conform to the specification componentwise and
fall exactly one dimension short of spanning.

That is the Liskov substitution principle as a measurement. Conformance to an
interface does not determine substitutability. In our terms:

| programming | apparatus | status |
|---|---|---|
| type signature | multiplicity dominance m(F) ≥ δ | necessary, cheap, checkable |
| test suite | faithful-reader span certificate | sufficient, irreducible |

The reason is λ ⊂ λ^⊕2: two submodules with identical multiplicity vectors can
occupy the same copy of an irreducible rather than complementary ones. No amount
of signature-checking detects it. So the specification exists before the
implementation, and does not determine which implementation satisfies it — the
certificate is not removable.

## 32. Is every frame filled?

Each vocabulary V creates a frame: δ(V) = m(A) − m(W_V), the specification a
closing method must meet. Tested on all 31 frames in the arena.

**Every frame is fillable.** Three have no single-family filler — spec4, rot4 and
spec4+rot4 — and all three close under the combination disj+spec3. Zero
unfillable frames. The claim survives in-domain.

But the manner of filling is the result:

| frame | families that **conform** (dominate δ) | families that **close** |
|---|---|---|
| spec4 | disj, rot4, spec3 | **none** |
| rot4 | disj, spec4, spec3 | **none** |
| spec4+rot4 | disj, spec3, rot3 | **none** |
| 𝒦_disj | spec4, rot4, spec3, rot3 | spec3, rot3 |
| spec3 | disj, spec4, rot4 | disj |

Frames attract conformers abundantly and conformance routinely fails to close.
In three cases *every* single conformer fails and the actual filler is a
composite. Signature is a weak predictor of fit.

And fillability is contingent on the catalogue, with the obstruction already
identified. Had rot3 not been in the arena, the frame lying off ker φ would have
been unfillable by anything — all four remaining families and all 15 of their
unions sit inside the hyperplane. Every frame here is filled because the
catalogue happens to span; it was one family away from a frame nothing could
reach.

## 33. The overlap is what makes a fill generative — and filling terminates

"The potential is already in what filled it," put in a form that can fail: is
m(union) inside the span of its parts' multiplicity vectors? If yes, the fill is
a linear combination and adds no direction.

**26 of 26 unions lie outside the span of their parts.** Every fill in this
arena is a new channel, not a recombination of the old ones.

The mechanism inverts the obvious reading. The sum a + b is always inside
span{a, b}, so a fill can only escape the span by differing from the sum — and
it differs by exactly the overlap:

    m(disj)      = (13, 4, 13, 4, 22, 33)
    m(rot3)      = ( 2, 1,  1, 0,  2,  3)
    sum          = (15, 5, 14, 4, 24, 36)
    m(disj∪rot3) = (15, 4, 14, 4, 24, 36)  = m(A)

The union is the sum minus the shared 1⁻ line. Two families overlapping in
nothing would compose additively and produce no new direction. **The redundancy
is the generativity**: the interaction term I_H(disj, rot3) = dim(1⁻)^H, which
looked like waste in the budget accounting of Part I, is precisely what makes the
composite an object of its own rather than a combination of its parts.

The bound, equally measured: **filling terminates.** Once W_ALL = A the
deficiency is zero and no further cell family changes anything — not a longer
cell, not a new shape, since A is fixed by the arena and not by the vocabulary.
New directions accumulate up to dimension 6 and stop. The field grows only if K
or the substrate changes. Generativity here is real, universal over fills, and
finite.

## 34. Correction: what §33 actually tested, and the absent category that never fired

§33 framed its measurement as a test of whether potential pre-exists a fill. It
was not. Once X and K are fixed, every cell, every family and every multiplicity
vector is determined — the methods are in the object by construction, exactly as
a class's methods are in the class. Nothing in this apparatus can falsify that.
What §33 actually tested is narrower and still worth having: **composition is not
linear** — 26 of 26 unions lie outside the span of their parts, and the overlap
is what puts them there. That result stands under the corrected label.

This is the second time in this record a measurement has been dressed as a test
of something larger than it tests (the first was the Artin minimality claim,
§22). The pattern is worth naming: reaching for the falsifiable framing of a
claim that is true by construction produces a real measurement attached to the
wrong question.

**And the claim that there are no gaps is measured here, not asserted.**
m(A) = (15, 4, 14, 4, 24, 36): every one of the six rational irreducibles occurs
in the ambient module with positive multiplicity. There is no empty channel.

Which means the first row of Table 5 — genuine absence, m_λ(V) = 0 — **never
fired on this witness.** Across twelve readers, thirty-one vocabularies and every
zero recorded in this work, each one was a reader zero or a vocabulary zero.
Not once a field zero. The three-way diagnostic was built to separate absence
from unreadability, and on this substrate the absence column is empty.

---

# Part VII — the reader is a sampler, exactly

## 35. f_H is the DC bin

A cyclic reader ⟨g⟩ of order m averages over an orbit of m points. That averaging is a
box filter, and restricting an irreducible λ to ⟨g⟩ splits it into frequencies
k = 0..m−1 (eigenvalues of g are m-th roots of unity), with

    mult of frequency k  =  (1/m) Σ_j χ(g^j) ω^(−jk),    ω = e^(2πi/m)

— the DFT of the character sampled on the orbit. **The fixed-point dimension this entire
apparatus is built on is the k = 0 bin.** Computed for all six cyclic classes of
C₂ × A₄ and checked against the independently measured f_H table:

| reader | m | DC spectrum (1⁺,1⁻,2⁺,2⁻,3⁺,3⁻) | matches f_H |
|---|---|---|---|
| ⟨1⟩ | 1 | (1,1,2,2,3,3) | ✓ |
| ⟨v⟩, v ∈ V₄ | 2 | (1,1,2,2,1,1) | ✓ |
| ⟨z⟩ central | 2 | (1,0,2,0,3,0) | ✓ |
| ⟨zv⟩ | 2 | (1,0,2,0,1,2) | ✓ |
| ⟨t⟩ | 3 | (1,1,0,0,1,1) | ✓ |
| ⟨zt⟩ | 6 | (1,0,0,0,1,0) | ✓ |

Six for six. Nyquist is not an analogy here; the read *is* a sample and f_H *is* the
zero-frequency bin. Everything at k ≠ 0 is annihilated — aliased to zero.

## 36. Two corrections this forces

**Faithful is not lossless.** The minimal faithful reader ⟨v⟩ has nonzero DC in every
band, which is what faithfulness means — but it still discards 2 dimensions each from
3⁺ and 3⁻, all sitting at k = 1. Faithfulness guarantees a channel to every irreducible,
not the preservation of content within one. §16a should be read with that caveat.

**Resolving power is not monotone in sampling rate.** The order-6 reader ⟨zt⟩ samples
three times as many points as ⟨v⟩ and has DC in **two** bands against ⟨v⟩'s **six**. A
higher-rate reader can be strictly blinder. This is the real content of Nyquist rather
than the folk version: what matters is the relation between the sampling comb and where
the content sits, not the number of samples.

## 37. The minus sector is a Nyquist band

Under ⟨z⟩ with m = 2, the irreducibles 1⁻, 2⁻ and 3⁻ have **zero** DC and all their
content at k = 1 — the Nyquist frequency of a two-point sampler. So the obstruction
φ = m(2⁻) − m(1⁻) of §26a, and the exhibited line with z·v = −v of §13, are the same
object in a third description: the minus sector is exactly the half-sample-rate band of
the central involution. A reader whose orbit includes z is sampling that content at
precisely the rate that folds it onto zero.

---

# Part VIII — the bank shot: the apparatus was reading one bin

## 38. Nothing was ever destroyed

For a cyclic reader ⟨g⟩ of order m, restricting λ splits into m bins and

    Σ_k (bin k)  =  dim λ,     always.

Computed for every irreducible against every cyclic class. **The bins always sum to
the full dimension.** Nothing is annihilated by a read. The content is *binned*, and
"annihilated" was only ever true of bin 0 — which is the only bin this entire apparatus
has read, because dim V^H is by definition the k = 0 coefficient.

Every wall found in thirty turns of this record is a statement about bin zero:

| reader | what bin 0 calls blind | where it actually is |
|---|---|---|
| ⟨z⟩ central | 1⁻, 2⁻, 3⁻ — the whole minus sector | **bin 1**, in full |
| ⟨t⟩ order 3 | 2⁺, 2⁻ | bins 1, 2 |
| ⟨zt⟩ order 6 | 1⁻, 2⁺, 2⁻, 3⁻ | bins 3; 2,4; 1,5; 1,3,5 |
| ⟨v⟩ in V₄ | the 2 "aliased away" dims of 3± | bin 1 |

Same orbit, same sample points, different weighting:

    P_k = (1/m) Σ_j ω^(−jk) ρ(g)^j        versus       P_0 = (1/m) Σ_j ρ(g)^j.

For a non-cyclic reader H the same holds with Irr(H) in place of bins: V|_H decomposes
over all characters of H, and dim V^H is the multiplicity of the *trivial* one. We have
only ever read the trivial component.

## 39. What this does and does not change

It does not invalidate a measured number. ε_harm, rank d₁, the faithful-reader lemma,
the isotypic cap and the 14-of-14 regression are correct statements about the invariant
readout. What changes is what the invariant readout *is*: a choice of coefficient, not
the only available read.

So the standing phrase "unreadable is not absent" was too weak, every time it was used.
The strong form, now measured:

    unreadable at bin 0  ⟹  present in full at a computable address.

Not "somewhere in the field, find another route." Bin k, and here is k.

## 40. The constraint is the aiming device

φ = m(2⁻) − m(1⁻), the V₄ switch filter, the z-anti-invariant line with z·v = −v, the
minus sector — these are one object seen four ways, and the fifth way is the operative
one: **they are a bin index.** z·v = −v does not say v is invisible. It says v is at
bin 1 of the two-sample orbit, exactly and only there.

A law is a reliable surface. Knowing how the orbit responds is what lets you compute
where the content went, so the obstruction stops being a wall and becomes the address.
The apparatus did not need another method, another substrate, or a weaker reader. It
needed a different coefficient of the read it was already performing.

The open work this creates: the entire ledger can be recomputed with equivariant reads
in place of invariant ones, bin by bin. Nothing in it would be dark.

## 41. The shot, executed — all three checks

Exact throughout: cyclotomic arithmetic in ℚ[x]/Φ_m(x), no floating-point roots of
unity anywhere.

**Check 1 — the old ledger is column zero.** a₀ = measured f_H: **36 of 36**, across all
six cyclic reader classes and all six irreducibles.

**Check 2 — dimension conserved.** Σ_k a_k = dim λ: **36 of 36**.

**Check 3 — projector algebra**, on the real 300-dimensional cochain space of the
witness with ρ(z) built as an explicit signed permutation: ρ(z)² = I, P_k² = P_k,
P₀P₁ = 0, P₀ + P₁ = I. All exact over ℚ, since ω = −1 at m = 2.

**The shot.** Same orbit, same samples, two coefficients:

| family | dim W_F | dim P₀(W) | measured f_⟨z⟩ | **dim P₁(W)** | sum |
|---|---|---|---|---|---|
| 𝒦_disj | 216 | 105 | 105 ✓ | **111** | 216 |
| spec4 | 168 | 84 | 84 ✓ | **84** | 168 |
| rot4 | 150 | 72 | 72 ✓ | **78** | 150 |
| spec3 | 174 | 87 | 87 ✓ | **87** | 174 |
| rot3 | 20 | 10 | 10 ✓ | **10** | 20 |
| ALL | 235 | **115** = D_⟨z⟩ | — | **120** | 235 |

The k = 0 column reproduces the measured ⟨z⟩ ledger row exactly, family by family. The
k = 1 column is new.

**The ⟨z⟩ reader has been reporting 115 of 235.** The other 120 dimensions were in the
same orbit, at the same sample points, the whole time — recoverable by one sign flip in
the weighting. More than half of 𝒦_disj's content (111 of 216) sits in the bin the
apparatus never read.

## 42. Wording that must not harden

Two corrections to §38, both of which overclaimed.

"Nothing is destroyed by a read" is wrong as stated. The *decomposition* preserves
dimension; the operator P₀ genuinely annihilates every k ≠ 0 component, and a reader
that retains only P₀'s output has discarded them. The exact statement:

    Restriction to the orbit preserves the representation.
    Retaining only the invariant projection discards all nontrivial components.

And the terminology: **frequency bins** is exact language only for cyclic readers, whose
irreducibles are one-dimensional characters. For a general finite reader the correct
object is the H-isotypic decomposition with central idempotents
P_α = (dim α/|H|) Σ_h conj(χ_α(h)) ρ(h). Cyclic → Fourier bins; general → H-isotypic
channels.

The faithful/unfaithful split also needs three levels, not two: **DC-faithful**
(f_{H,0} > 0 in every sector), **spectrally resolved** (the relevant H-types are
separately accessible), **complete** (the whole restricted representation is retained).
The 152-coordinate reader of §16a is DC-faithful and not complete.

## 43. Binwise closure — the bank shot lands

Not binwise *deficiency*, which would repeat the dominance mistake at a new index.
Binwise **span**: is span{P_k(W_F)} = P_k(A)?

Channel capacities at the ⟨z⟩ reader: P₀(A) = 115, P₁(A) = 120.

**Prediction, stated before running.** The shared disj/rot3 line is z-odd, so it should be
invisible at k=0 and the entire interaction at k=1; the arithmetic would then force
111 + 10 − 1 = 120. Both halves confirmed exactly:

| channel | r(disj) | r(rot3) | r(union) | I | closes? |
|---|---|---|---|---|---|
| k = 0 | 105 | 10 | 115 | **0** | yes |
| k = 1 | 111 | 10 | 120 | **1** | yes |

The interaction that the invariant reader measured as zero is one dimension, entirely in
the channel it never read. The line is the interaction.

**And the minimal vocabularies differ by channel.**

    k = 0:  {disj+spec3, disj+rot3}
    k = 1:  {disj+spec4, disj+rot4, disj+spec3, disj+rot3}

spec4 and rot4 are precisely the two families of §10 and Table 10 — the ones that
dominate δ(𝒦_disj) componentwise and **fall exactly one dimension short** of closing.
At k=0 here they reach 114 of 115, the same one-dimension shortfall. At k=1 they reach
120 of 120 and close.

So the answer to the question that could not previously be posed is yes: **a family that
fails to close in the invariant channel can be a minimal closer in the complementary
one.** "Dominates but does not close" was never a property of those families. It was a
property of reading them at k = 0.

That is the bank shot completed rather than described. The families that could not make
the direct shot make the bank, off the same cushion, with the sign flipped.

## 44. The declaration tree by channel — wider at each step, smaller overall

Both reviews predicted the k=1 channel would show "a larger executable choice set." The
measurement says something more interesting and in one respect the opposite.

| | k = 0 | k = 1 |
|---|---|---|
| capacity | 115 | 120 |
| live options after declaring disj | spec4, rot4, **spec3\***, **rot3\*** | **spec4\***, **rot4\***, **spec3\***, **rot3\*** |
| immediate closers at that node | 2 | **4** |
| total declaration paths to closure | **82** | **68** |
| path lengths | {2:4, 3:18, 4:36, 5:24} | {2:**8**, 3:12, 4:24, 5:24} |
| branch points in the tree | 76 | 66 |

The per-node choice set is **wider** at k=1 — four immediate closers against two, and
twice as many length-2 paths. The tree is **smaller** — 68 routes against 82, 66 branch
points against 76.

Both at once, and they are the same fact: a channel in which more methods close is a
channel in which paths terminate sooner, so there are fewer distinct histories. More
options per moment, fewer stories.

That sharpens the earlier choice-history result (§ "82 paths, 1 endpoint"). The number of
choices available at a moment and the number of distinct histories move in **opposite**
directions. A reader channel does not simply open or close the option field; it trades
breadth at a node against depth of the tree.

The k=0 count of 82 matches the trivial-reader count exactly, as it must: both have the
same minimal closing vocabularies {disj+spec3, disj+rot3}, so the same tree.

**Wording consequence, now forced rather than cautious.** Retire "families that cannot
close." spec4 and rot4 cannot close P₀(A) with disj and do close P₁(A) with disj — same
substrate, same families, same ambient, same orbit, same cells, one sign in the
weighting. Every closure claim from here carries (H, k) for cyclic readers and (H, α)
for the rest. Papers I–III stand as the k = 0 slice; what was too narrow was the
notation, not the numbers.

## 45. The deficiency is a module, and its character answers every reader at once

Both reviews asserted a mechanism for § 44 without running it: the tree shrinks *because*
spec4 and rot4 flipped from non-closers to closers, which adds an immediate option and
collapses a future subtree. The tree count is a function of the closure predicate on
subsets and nothing else, so the claim is exactly checkable. Measured on all 31
vocabularies at both channels:

| | flipped |
|---|---|
| subsets whose closure status differs between k=0 and k=1 | 3 |
| of those, minimal | 2 — disj+spec4, disj+rot4 |

Patching the k=0 predicate with **only** those two minimal flips reproduces k=1 exactly
— 68 paths, 66 branch points, {2:8, 3:12, 4:24, 5:24}. Removing them from the k=1
predicate recovers k=0 exactly — 82 / 76 / {2:4, 3:18, 4:36, 5:24}. The asserted
mechanism is now run, in both directions, and it is complete: nothing else moved.

### What the rank columns said that neither review read

The channel grew by 5 (115 → 120), but the per-vocabulary ranks did not follow:

| vocabulary | r at k=0 | r at k=1 |
|---|---:|---:|
| disj | 105 | 111 |
| rot4 | 72 | 78 |
| spec3 | 87 | 87 |
| rot3+spec3 | 97 | **96** |
| rot3+spec4 | 94 | **93** |

Three vocabularies span *less* in the larger channel. The first explanation to try is a
failure to split: P₀+P₁ = I gives dim P₀W + dim P₁W ≥ dim W, with excess when W is not
ρ-invariant. **Measured: zero excess, all 31 of 31.** Every vocabulary span is
ρ-invariant and splits exactly. Nothing is lost or gained; only the partition differs.

Which means the whole channel ledger reduces to one signed integer. On a ρ-invariant W
with ρ² = I,

  r₀(W) − r₁(W) = Tr(ρ | W),  so  r₀ = (r + Tr)/2,  r₁ = (r − Tr)/2.

Computed independently as a trace — for an rref basis against a signed permutation it is
a lookup, Tr = Σᵢ sgn[c_i]·M[i][c_i] with c_i = perm⁻¹(piv[i]) — this reproduces **every
one of the 31 measured channel ranks**. The projector apparatus was never needed. Per
family: disj and rot4 have Tr = −6 (z-tilted); spec3, spec4, rot3 have Tr = 0
(z-balanced). Tr(ρ | C¹_G) = 0 on the full 300-dimensional ambient.

### The deficiency is conserved across channels

  δ₀(s) + δ₁(s) = 235 − r(s) = δ(s),  δ₀(s) − δ₁(s) = −5 − Tr(ρ|W_s).

The total deficiency does not change with the channel. The channel only decides **where
the hole sits**. disj+spec4 is short exactly one dimension in the ambient; that dimension
is z-even, so it lies entirely in k=0. The k=1 reader does not see more — the hole is not
in its channel. "Fails by one dimension" was never channel-free.

So the deficiency is not a number. It is a module, D_s = A / W_s, with character
χ_D = χ_A − χ_{W_s}, and every channel reading is one Fourier coefficient of it:

  δ_{H,k}(s) = (1/m) Σⱼ ζ_m^{−jk} χ_D(g^j),  H = ⟨g⟩ of order m.

Prerequisite checked, not assumed: all five family spans are invariant under all 24
automorphisms, so χ_{W_s} is a genuine character of G.

### Fifty channels, two trees

With closure at (H,k) reduced to a character computation, the declaration tree at every
cyclic channel follows with no projectors, no per-channel rank, and no search — one trace
per group element, then a DFT. All 15 cyclic readers, 50 channels, capacities from 38 to
139 — a 3.7-fold spread:

| | k = 0 | every k ≠ 0 |
|---|---:|---:|
| closing vocabularies | 12 | 15 |
| declaration paths | **82** | **68** |
| branch points | 76 | 66 |

**Two** distinct outcomes across all fifty, split on a single bit. The ⟨z⟩ rows reproduce
82/76 and 68/66 from the projector apparatus of § 44 — independent route, same numbers.

One fact generates the whole table. For all three δ=1 vocabularies,

  χ_D(g) = 1 for all 24 g ∈ Aut(X),

the **trivial representation**, confirmed independently by dim A^G = 15, dim W^G = 14,
dim D^G = 1. What disj+spec4 misses is one copy of the invariant line and nothing else.
Every reader has a trivial character and Res_H(triv) = triv, so δ_{H,0} = 1 for every
subgroup and δ_{H,α} = 0 for every nontrivial α. Measured over all **26** subgroups of
orders 1, 2, 3, 4, 6, 8, 12, 24: dim D^H = 1, without exception.

That closes both items the reviews named as open. The other cyclic readers do not need
cyclotomic projectors and the non-cyclic V₄ case does not need central idempotents; the
trivial channel carries all of D, so the character settles it.

### Reverse, and the correction to the reviews

Run backwards: if the obstruction is always trivial-isotypic, nothing should ever close at
k=0 and fail elsewhere. Measured across all 50 channels — the closing set at k=0 is
contained in the closing set at every k ≠ 0, **zero counterexamples**. The trivial channel
is not a different reading. It is the **hardest** one, and the relation is an order, not a
symmetry.

Review 2 proposed the channel-conditioned history functional ℋ(H,k;𝒱) as a rich second
empirical layer. On this apparatus it takes exactly **two** values, indexed by whether the
channel is the trivial character. The capacity varies 3.7-fold and the declaration tree
does not move. So § 44's "more options per moment, fewer stories" survives as measured,
but the reviews' reading of it — that the channel shapes the history space — overstates
what varies. One bit does.

And § 43's bank shot keeps its result while losing its generality: spec4 and rot4 bank off
*any* nontrivial channel of *any* reader, because the cushion is not the sign of z. It is
the invariant line, and every reader is blind to it in exactly one way and sees it in
exactly one other.

**Retro-sharpening of Papers I–III.** "disj+spec4 fails by exactly one dimension" was
always true. The content is *which* dimension: the G-invariant line. That is why no change
of reader rescues it and no reshuffling within these families does either — the obstruction
is the one thing every reader is guaranteed to see.

## 46. The collapse was granularity, not the witness — a 3⁻ obstruction in the same arena

All three reviews accepted § 45 and attached the same caveat: the trivial deficiency is a
fact of *this witness*, and a future witness might have a nontrivial quotient where the
full isotypic machinery matters. That caveat is in the wrong place. The counterexample is
in this witness, one lattice level below the five families.

Two facts made it findable without a new arena. W and A are rational row spaces, so D is a
ℚ[G]-module and a one-dimensional one can only be 1⁺ or 1⁻ — the ω-characters are not
rational in dimension 1. So D ≅ 1⁺ was a two-way outcome, not a forced one. And
rot4+spec3 already had χ_D with values {12, 4, 0}: nontrivial deficiencies were present
all along, just not at δ = 1.

### Full isotypic decomposition of all 31 deficiencies

Built the rational character table of C₂ × A₄ explicitly — A₄ recovered as the unique
index-2 subgroup, generated by the order-3 elements — with 2± carrying Schur index 2
(⟨χ,χ⟩ = 2, rationally but not absolutely irreducible; omitting that divisor doubles those
multiplicities). Regression: m(ambient) = {1⁺:15, 1⁻:4, 2⁺:14, 2⁻:4, 3⁺:24, 3⁻:36},
reproducing the stored row from the independent fixed-point route.

Result over the five-family lattice: **every nonzero deficiency contains at least one copy
of 1⁺, 31 of 31.** The three trivial-isotypic ones are exactly the δ = 1 cases. Since
m₁₊(D) = 15 − dim W^G, that says dim W^G = 15 ⟺ W = A on this lattice — which invited the
claim that 15 invariant numbers certify closure of a 235-dimensional module.

**That claim is false.** Recorded with the retraction it needs.

### A false refutation first

The first search reported 111 counterexamples and was wrong. It measured rank of the
G-averaged rows, which is dim π(W), the projection of W onto the ambient invariants. That
equals dim W^G only when W is G-invariant — true for the 31 family unions, verified
earlier, and false for an arbitrary cycle subset. Measured directly: random cycle subsets
of 15, 25 and 40 cycles have dim π(W) = 8, 12, 14 but **dim W^G = 0**, and none is
G-invariant. All 111 retracted.

### The real counterexample

The correct lattice is unions of G-orbits of cycles, which stay invariant: 1283 cycles in
90 orbits, refining the five families. An adversarial greedy — orbits ordered by
decreasing invariant rank, precisely to fill the invariant part as cheaply as possible —
reached dim W^G = 14 at dim W = 211 and then closed both at once, hitting 15 exactly when
the span hit 235. No single orbit is essential: all 90 drop-one deletions leave rank 235,
which is why greedy and deletion searches miss it. Random orbit subsets do not:

| | |
|---|---|
| orbits in the union | 33 |
| dim W | **232** (dim A = 235) |
| W is G-invariant | yes, verified |
| dim W^G | **15** = dim A^G |
| dim D | 3 |
| **m(D)** | **{3⁻ : 1}** |

Verified exactly over ℚ, not mod p. A single copy of the three-dimensional sign-twisted
irreducible, with **no trivial component whatsoever**.

### What it breaks

3⁻ has χ(z) = −3, so it is entirely z-odd — the exact mirror of 1⁺, which is entirely
z-even. From the character:

| reader ⟨z⟩ | δ at k = 0 | δ at k = 1 |
|---|---:|---:|
| D ≅ 1⁺ (disj+spec4) | 1 | 0 |
| D ≅ 3⁻ (this W) | **0** | **3** |

This vocabulary **closes in the invariant channel and fails in the anti-invariant one**.
For an order-3 reader it is δ = (1,1,1) — deficient in every channel.

So three § 45 statements are now scoped rather than general:

1. "Every nonzero deficiency contains 1⁺" — true over the five-family lattice, **false**
   over the orbit lattice.
2. "The trivial channel is the hardest; closure at k=0 implies closure at every k≠0" —
   zero counterexamples over 50 channels of the family lattice, **refuted** here.
3. "Fifty channels, two trees, split on one bit" — a fact about the five-family inventory,
   not about the arena.

The numbers in § 45 stand. What was too narrow, again, was not the measurement but the
quantifier: the collapse was a property of the **granularity of the vocabulary**, and the
reviews' "witness form" should read **family-lattice form**.

### The constraint this null result points at

The five families are coarse in a specific, now-measurable way: each one carries its
non-invariant content bundled with its invariant content, so no union of them can hold the
full invariant part while missing anything else. Orbits cut finer and separate the two.
That is why the isotypic machinery is not decoration — central idempotents for V₄ and
cyclotomic channels for m > 2 become operationally necessary the moment the vocabulary is
specified below family granularity, which is exactly where real declarations live.

And review 2's channel-conditioned history functional ℋ(H,k;𝒱) is rehabilitated. It takes
two values on the family lattice. One level down, both extremes of the isotypic range are
realized in the same arena — an obstruction invisible to every nontrivial channel, and an
obstruction invisible to the trivial one.

## 47. Reader saturation is not closure — and the most symmetric reader is the blindest

The question put to this session was: *when does reader saturation imply only
observational closure, and when does it imply genuine closure of the underlying
transition system?* § 46 already contains a counterexample to the first horn — the
33-orbit vocabulary has δ_{⟨z⟩,0} = 0, so P₀W = P₀A with the invariant reader saturated,
while D ≅ 3⁻ ≠ 0. This section gives the condition.

### The trivial half of the answer

For any reader H, the channel deficits sum to the total:

  Σ_{α ∈ Irr(H)} δ_{H,α}(W) = dim D.

So saturation across a reader's **full** channel set always implies D = 0, for every H
including the trivial subgroup. The question only has content for a reader with
**partial** channel access — which is exactly what Papers I–III had, the invariant
channel alone.

For that case the criterion is a fixed-point dimension:

  the invariant channel of H sees λ  ⟺  dim λ^H > 0.

### The closure problem factorizes

Isotypic projection is linear, so e_λ(Σ_o W_o) = Σ_o e_λ(W_o). The closure question
therefore splits into six independent covering problems rather than one rank problem in
235 dimensions:

| channel | 1⁺ | 1⁻ | 2⁺ | 2⁻ | 3⁺ | 3⁻ |
|---|---:|---:|---:|---:|---:|---:|
| dim e_λ(A) | 15 | 4 | 28 | 8 | 72 | 108 |
| orbits to span (greedy) | **15** | 4 | 14 | 4 | 11 | 15 |
| lower bound ⌈dim/max per orbit⌉ | 15 | 4 | 14 | 4 | 8 | 12 |

Regression: the six channel ranks give m(A) = (15, 4, 14, 4, 24, 36), reproducing the
stored ambient row. Applying e_λ costs 4 × 24 operations per cycle, since a 3- or 4-cycle
row has at most four nonzeros.

**Retraction.** An earlier pass reported these costs as 30 for 1⁺ and 44 for 3⁻ and used
that gap to explain § 46's reversal — "3⁻ is the most expensive channel, so it stays short
while 1⁺ closes." Those numbers came from a fixed-order greedy and are wrong; a
marginal-gain greedy spans every channel in 15 orbits or fewer, and a separate
construction spanned *all six* with 17. 1⁺ and 3⁻ are tied at 15, not separated by 14.
For 1⁺ the bound is exact — each orbit supplies at most one dimension of a 15-dimensional
channel, so 15 is the true minimum. The reversal in § 46 stands; the cost explanation for
it does not. What distinguishes the 33-orbit union is *which* orbits it contains, not how
many.

### Which obstruction types are realizable

A greedy that fills every channel but one, preferring orbits that contribute least to the
target, isolates only one type:

| target | orbits | dim D | m(D) | |
|---|---:|---:|---|---|
| 1⁺ | 17 | 0 | 0 | target closed too |
| 1⁻ | 16 | 0 | 0 | target closed too |
| 2⁺ | 17 | 0 | 0 | target closed too |
| 2⁻ | 17 | 0 | 0 | target closed too |
| 3⁺ | 17 | 0 | 0 | target closed too |
| **3⁻** | **15** | **6** | **{3⁻ : 2}** | **pure** |

So 3⁻ is realizable as a pure obstruction two independent ways — the 33-orbit random find
with m(D) = {3⁻:1}, and this 15-orbit construction with m(D) = {3⁻:2}. For the other five,
filling the complementary channels also filled the target. That is a failure of this
construction, not a proof of impossibility.

### The diagnostic inversion

dim λ^H is non-increasing as the reader subgroup grows — checked directly over all 37
containment pairs among the twelve readers, **zero violations**. The consequence:

| reader | order | obstruction types its invariant channel can see |
|---|---:|---|
| trivial | 1 | **6 of 6** |
| an involution | 2 | 6 of 6 |
| order 3 | 3 | 4 of 6 |
| order 4 | 4 | 3–4 of 6 |
| order 6 | 6 | 2 of 6 |
| order 8 | 8 | 2 of 6 |
| order 12 | 12 | 2 of 6 |
| **full Aut(X)** | **24** | **1 of 6 — only 1⁺** |

More symmetry means fewer visible obstruction types. The reader that looks best by
symmetry is the worst by diagnostic power.

### The answer

  **Reader saturation implies genuine closure iff the reader's accessible channels cover
  every realizable obstruction type.**

Full channel access always qualifies, trivially. Invariant-channel-only access qualifies
only for readers that can see every type that actually occurs — and since 3⁻ is realizable
here, every reader blind to 3⁻ can be saturated while W ≠ A. That is observational closure
without dynamical closure, exhibited rather than hypothesized.

### Why § 45 looked universal

The apparatus of Papers I–III is the invariant channel of the full automorphism reader,
f_H = dim V^H. By the table above it can see exactly one of the six obstruction types. It
was right about 1⁺ because 1⁺ is the only type it could ever have found. The collapse of
§ 45 was not a fact about the arena and not only a fact about the vocabulary's
granularity — it was also a fact about the diagnostic ceiling of the reader doing the
measuring.

That is the discipline the whole correction sequence has been enforcing, now applied to
the instrument itself: **do not call something absent because the selected reader
coefficient is zero** — including when the selected reader is the most natural one
available.

## 48. Total review — what collides with existing mathematics, and from which direction

A full audit of §§43–47 against the standard literature, run under the project's own
rule: *say "recovered" where you mean "recovered."* The headline is uncomfortable and
correct.

### Audit: what is actually established

| Claim | Status | Range / provenance |
|---|---|---|
| D ≅ 3⁻ for a 33-orbit G-invariant vocabulary, dim W = 232 | **verified exactly over ℚ** | single witness, full character check, m(D) non-negative and dimension-consistent |
| δ_{⟨z⟩,0} = 0 and δ_{⟨z⟩,1} = 3 for that W | **verified** | from χ_D, independent of the projector apparatus |
| m(A) = (15, 4, 14, 4, 24, 36), dim A = 235, dim A^G = 15 | **verified, two independent routes** | character route and stored fixed-point route agree |
| dim λ^H = ⟨χ_λ, π_H⟩ for all 26 subgroups | **verified computationally** | exhaustive over subgroups |
| Minimal orbit-generators of A = **15**, binding channel 1⁺ | **verified: bound and achievement** | lower bound max_λ⌈m_λ s_λ/dim λ⌉ = 15; explicit 15-set found spanning all six channels |
| Channel/tree census: 50 channels → 2 trees | **verified** | five-family lattice only, 31 unions, exhaustive there |
| "3⁻ is the only pure realizable deficiency type" | **not established** | one greedy construction failed for the other five; not a proof of impossibility |
| Any claim about the 2⁹⁰ orbit lattice | **sampled, never exhausted** | existence claims are sound; non-existence claims are weak |

**Provenance risk, stated plainly.** Every result in §§45–48 runs from a shared library and
pickles in an ephemeral session scratchpad. There is no repository, no commit, no manifest.
The computations are reproducible in principle and not archived in fact. That is a real
weakness of the record, not of the mathematics.

**Modular arithmetic.** Fast searches used rank over p = 2⁶¹−1 with dim A = 235 and
dim A^G = 15 as controls. A bad prime is possible in principle; the controls passed, and
the one load-bearing counterexample was re-verified over ℚ.

### Collision map

| Result | Standard name | Class |
|---|---|---|
| χ_D = χ_A − χ_W | additivity of characters on short exact sequences | known verbatim |
| r = r₀ + r₁, zero split defect | Maschke / complete reducibility | known verbatim |
| r₀ = (r + Tr ρ)/2 | eigenspace dimensions of an involution from its trace | known verbatim |
| δ_{H,k} = (1/m)Σⱼ ω^{−jk} χ_D(gʲ) | character multiplicity formula; DFT over a cyclic subgroup | known verbatim |
| δ_{H,α} = ⟨Res_H χ_D, χ_α⟩ | orthogonality relations | known verbatim |
| Σ_α δ_{H,α} = dim D | completeness of the isotypic decomposition | known verbatim |
| W^H = A^H ⟺ D^H = 0 | exactness of (−)^H in characteristic 0 | known verbatim |
| dim λ^H non-increasing in H | λ^H ⊆ λ^K for K ≤ H | known verbatim |
| **the diagnostic ceiling of § 47** | **Frobenius reciprocity**: dim λ^H = ⟨χ_λ, Ind_H^G 1_H⟩ | **known verbatim** |
| closure factorizes per isotypic channel | linearity of central idempotents; Wedderburn | known verbatim |
| 2± with ⟨χ,χ⟩ = 2 | rational vs absolute irreducibility; Schur index | known verbatim |
| min generators ≥ max_λ⌈m_λ s_λ/dim λ⌉ | minimal generation of a semisimple module | known (textbook) |
| shape count 1, 5, 83, 5048 | **OEIS A035512**, unlabeled strongly connected digraphs | known verbatim — recovered |
| the arena's numbers; the 3⁻ witness; the 15-set | — | **novel data, not novel theorems** |
| declaration-tree combinatorics | set-cover / matroid-adjacent | adjacent only |

**§ 47's inversion is Frobenius reciprocity.** Verified, not cited: the reader's diagnostic
profile is the decomposition of the permutation module ℚ[G/H], which shrinks from the
regular representation (H = 1, all six irreducibles) to the trivial module (H = G, only
1⁺) as the reader grows. The "most symmetric reader is the blindest" is that sentence.

**The 1⁺ duality is one fact with two faces.** 1⁺ appears exactly once in the regular
representation, so it is the binding constraint on *generation* — 15 orbit-generators, more
than any other channel demands. And 1⁺ is the unique constituent of ℚ[G/G], so it is the
only thing the full-symmetry reader can *see*. Hardest to build, only thing visible.

### The direction, and where it earns something

Standard representation theory arrives at these objects from Maschke and Wedderburn and
asks about module structure. This work arrived from *which declarations close a field* and
asked about reader visibility. The objects are the same and none of the mechanisms is new.

What the direction buys is one question with no standard name:

  **Def(𝒱) — given a vocabulary lattice 𝒱 of G-stable spans, which irreducible types
  occur as m_λ(A/W) > 0 for some W ∈ 𝒱?**

That is a question about the *lattice*, not the module. Standard theory answers "which
submodules exist" (all of them, by semisimplicity); this asks which are reachable by
unions of a specified generating family. The §§45–47 result is that the answer is
granularity-dependent — {1⁺} at family resolution, ⊇{1⁺, 3⁻} at orbit resolution — and the
certification criterion follows from it. Apparently new as a question within this search
scope; one searcher, one pass, so that is a scoped statement and not a novelty theorem.

### Where one more step hits a named open problem

A is a relation module in the literal sense: the image of ∂₂ for a 2-complex whose 2-cells
are the 3- and 4-cycles, with Aut(X) acting. The quantity measured in § 47 — minimal number
of orbit-generators versus the module-theoretic lower bound — is exactly the shape of the
**relation gap problem**: whether the number of relators needed exceeds the number of
generators of the relation module. It is tied to Wall's D(2) problem and is open.

**Here the gap is zero.** The bound gives 15 and an explicit 15-set achieves it. That is
the expected answer and it is not evidence about the open problem, because the relation gap
is hard precisely where ℚ[G] is replaced by ℤ[G] and Maschke fails. Over ℚ the module is
semisimple and the bound is attained; over ℤ it need not be.

So the honest map position: this work sits one coefficient change away from a named open
problem, on the easy side of it. The non-trivial version of every § 45–48 result is the
ℤ[G] version — integral deficiency modules, where D need not decompose, where "isotypic
channel" has no meaning, and where the generation bound can fail. Nothing in the present
apparatus survives that change unexamined; the character computations all rely on
semisimplicity.

That is the collision worth noting, and the direction note Dean asked for: we are arriving
at relation-module generation from the vocabulary side, and the open problem is standing
one ring further in, over ℤ.

## 49. The bridge, executed — reader channel to field equation, on this arena

The prescription on the table was: promote a reader from a way of inspecting a module to a
projection rule on a dynamical field, require the dynamics to commute with the reader
symmetry, and the channels become physical normal modes. That is a specification, not a
claim, until it runs. It was run on the same arena the ledger uses.

### The model, with equivariance checked rather than assumed

| | |
|---|---|
| state | Φ : 66 arena vertices → ℚ, with Aut(X) acting by permutation |
| dynamics | ∂ₜΦ = −LΦ + gΦ², L the graph Laplacian, Φ² pointwise |
| channels | P₀ = (I+ρ(z))/2, P₁ = (I−ρ(z))/2 for the central involution |

Checked, not assumed: **[L, ρ(g)] = 0 for all 24 automorphisms**, and the pointwise square
is equivariant for all 24. The field space splits 36 ⊕ 30 = 66. Arithmetic is exact
rational throughout, so "exactly zero" below is a statement and not a tolerance.

### Forward: linear dynamics

Initial condition purely in the reader-null sector — ‖P₀Φ(0)‖ = 0 exactly.

| step | ‖P₀Φ‖ (visible) | ‖P₁Φ‖ (reader-null) |
|---|---|---|
| 1 | **0** | 93.28 |
| 3 | **0** | 74.64 |
| 12 | **0** | 35.60 |

Exactly zero at every step. Under linear equivariant dynamics the reader-null sector is
**permanently** unobservable to that reader.

### Reverse: add the lowest-order equivariant nonlinearity

Same initial condition, g = 1.

| step | ‖P₀Φ‖ (visible) | ‖P₁Φ‖ (reader-null) |
|---|---|---|
| 1 | **4.62** | 93.28 |
| 3 | 11.06 | 75.64 |
| 12 | **23.82** | 40.85 |

Nonzero from the first step. The invisible sector sources the visible one.

### The selection rule, measured on this arena

| | P₀ | P₁ |
|---|---|---|
| even·even | nonzero | **zero** |
| odd·odd | nonzero | **zero** |
| even·odd | **zero** | nonzero |

The C₂ grading, exactly: (+)(+) = +, (−)(−) = +, (+)(−) = −. The odd sector enters the
even channel only at second order, which is precisely why it is invisible to a linear
reader and visible to a quadratic one.

### The sharper consequence: the invisible sector is recoverable

P₁(odd·odd) = 0 means the odd sector squares **wholly** into the even channel, so
P₀(Φ₋²) = Φ₋² identically. The first Euler step is therefore exactly

  Φ₊(dt) = dt · g · Φ₋(0)²,

and the reader can invert its own observation. Measured: recovered := P₀Φ(dt)/(dt·g)
**equals Φ₋(0)² exactly**, so |Φ₋(0)[v]| is determined at every one of the 66 sites.

What is lost is the sign, at 58 nonzero sites — and the loss is constrained, not free. A
naive per-site sign flip leaves the odd channel, so it is not an admissible state; global
negation is admissible and gives the identical observation, so at minimum the global sign
is unrecoverable.

Three addresses to the same content:

1. linear read → returns exactly nothing
2. quadratic read → returns the magnitude profile, exactly, at every site
3. the signs → need a third address

That is the ledger's load-bearing distinction with a measurement attached. *Removed* would
say give up. *Not projected* said find another address, and the second address returned the
content exactly.

### What this is, and what it is not

**It is** one executed instance of reader-channel → field-equation → observable, with
equivariance verified, on the arena the rest of the ledger uses. It is the physical form of
§ 46: reader-saturated is not closed, reader-null is not causally inert, and now — reader-null
is not even unrecoverable.

**It is not physics.** There is no spacetime, no Lorentz structure, no ħ, no amplitude, no
Born rule, no particle content, no gravity. The four gaps that separate this from a physical
theory — mathematical closure, computational universality, physical emergence, empirical
discrimination — are untouched by this run. Φ is a function on 66 graph vertices; L and the
quadratic term were chosen for equivariance and lowest order, not derived from the
program's primitives.

So what has been bridged is "reader channel" to "field equation," which was the stated
prescription. What has **not** been bridged, and is upstream of everything here, is a reason
from the primitives why Φ, L, 𝒩 and R should be nature's state, law, interaction and
measurement. That gap is where it was.

## 50. Which operator is forced? None — and the residual freedom is 22, measured

The reviews converged on the right correction to the proposed next step: do not manufacture
a momentum coordinate, attack the choice of L. Formally — which local G-equivariant linear
operators does the arena permit, and do the primitive constraints select one? Three outcomes
were named in advance: L forced up to scale, a small family with located freedom, or no
constraint at all. The answer is the second, with the dimension measured.

### First, two corrections to the reported spectral data

One review reports 30 eigenvalues in each sector of a 66-dimensional space and flags its own
confusion about the zero mode. Measured directly: z fixes **6** arena vertices, and

  dim even (P₀) = **36**,  dim odd (P₁) = **30**,  36 + 30 = 66.

Not 30 + 30 = 60. And L𝟙 = 0 with 𝟙 z-even, so the zero mode is in the even sector — which
that review reached by correction, and which is confirmed here.

### The equivariant operator algebra

For a permutation module the G-equivariant operators are spanned by the **orbital** indicator
matrices — G-orbits on ordered pairs. Measured on the arena (66 vertices, 300 edges, degrees
{6, 8, 10, 12, 14}, diameter 4, 8 vertex orbits of sizes {3,3,6,6,12,12,12,12}):

  dim End_G(ℚ⁶⁶) = **308** orbitals, every one at a single well-defined distance.

| distance | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| orbitals | 8 | 44 | 123 | 108 | 25 |

| constraints imposed | dim of admissible family |
|---|---:|
| equivariant, locality radius 1 | 52 |
| + self-adjoint | 30 |
| + conservation T𝟙 = 0 | 44 |
| **+ self-adjoint and conservation** | **22** |

L = D − A lies in that 22-dimensional space, verified by reconstructing it exactly from its
orbital coefficient vector. **It is one point in 22 dimensions.** So equivariance, locality
at radius 1, self-adjointness and conservation do not force the Laplacian.

(Method note: symmetry is a constraint on the coefficients, c_O = c_{Oᵗ}, because the
transpose of an orbital is another orbital. An earlier pass filtered to individually
symmetric generators instead and returned dimension 0, which is impossible since L is both
symmetric and conserving. Corrected.)

### What the 22 are

Measured: the arena has exactly **22 edge orbits** — G-classes of unordered adjacent pairs,
of sizes {6,6,12×16,24×4}. The arena is **not** edge-transitive. The 22-dimensional family
is precisely one free weight per edge orbit, with the diagonal forced by conservation.

  **L = D − A is the point where all 22 weights are equal.**

Nothing in equivariance, locality, self-adjointness or conservation makes them equal.
Choosing the standard Laplacian assumes edge-transitivity on an arena that does not have it.
"All moves cost the same" is extra homogeneity, imported, not derived.

### The internal collision

This is where the result stops being a null one. The program's own Constraint/Law chain
states: *the price is a gradient, it cannot be a single value or it breaks the rule that
difference proves change.* L = D − A assigns every transformation the same price. Under that
constraint, L is not merely unforced — it is the one point in the 22-dimensional family that
is **excluded**.

So the honest finding is not that the primitives fail to select an operator. It is that the
primitives, taken with the program's own gradient condition, **rule out the conventional
choice** and leave a 22-parameter space in which the gradient structure would have to do the
selecting. That is navigational: it says where the operator comes from, and it says the
Laplacian is the wrong starting point rather than the obvious one.

What has *not* been done: turning "the price is a gradient" into a linear constraint on the
22 weights. That specification belongs to the program, not to a guess made here. It is the
single next step with real content.

### § 49 is robust; the spectral numbers are not

Tested across the family — L itself, three random weight vectors, and one with an edge
orbit zeroed:

| member | [T, ρ(z)] = 0 | T𝟙 = 0 | P₀Φ stays exactly 0 under linear evolution |
|---|---|---|---|
| L (all weights 1) | yes | yes | **yes** |
| random weights ×3 | yes | yes | **yes** |
| one weight zeroed | yes | yes | **yes** |

So the split is clean:

**Forced by arena and symmetry**, holding for all 22 parameters — the channel decomposition,
[T, P_k] = 0, and § 49's linear invisibility of the reader-null sector. § 49's mechanism was
never a consequence of choosing the Laplacian.

**Not forced**, moving with the 22 parameters — the spectrum, λ_max, ω_max = √λ_max, and
every dispersion-like quantity. The reported ω_max ≈ 4.1148 is a property of one point in a
22-dimensional choice space, not a fact about the arena. It should not be quoted as one.

That is the boundary the experiment was built to find, and it fell on the operator rather
than on the momentum coordinate.

## 51. The gradient rule, made linear and measured: 22 → 7

§ 50 left the question as a specification request: turn *the price is a gradient* into a
linear constraint on the 22 edge-orbit weights. Both reviews supplied the same sharpening,
and it is the one that makes the rule bite:

  **the edge price is not itself a gradient — it must be generated by one.**

Formally: a signed price p on directed arena edges, G-equivariant and antisymmetric
(p(u,v) = −p(v,u)), is admissible only if p = dφ for a vertex potential φ, i.e. zero
circulation around every cycle. One consequence is forced before computing: if p is
G-invariant and p = dφ on a connected arena, then d(φ∘g − φ) = 0, so φ∘g − φ is a constant
c(g); c is a homomorphism from a finite group to ℚ, hence zero. **φ is itself G-invariant**,
so constant on vertex orbits.

### The arena's orbit structure

| | |
|---|---|
| vertex orbits | **8**, sizes {12, 3, 12, 6, 12, 6, 12, 3} |
| edge orbits | **22** |
| edge orbits G reverses | **0** |
| edge orbits inside one vertex orbit | **1** |
| edge orbits joining two vertex orbits | **21** |

The zero in the third row matters on its own: no automorphism reverses any edge orbit, so
**every edge orbit carries a G-invariant orientation**. Direction is already in the arena.
It does not have to be manufactured, and no momentum coordinate was installed to get it.

### The measurement

The gradient map d sends the 8 invariant potentials to signed values on the 22 edge orbits.
Measured rank:

  **dim(gradient-compatible subspace) = 7 of 22.**

The rule removes **15 of the 22 parameters**, and the surviving 7 have a clean reading:
8 vertex orbits minus the additive constant. The operator is fixed by assigning one number
to each class of arena state; the price of a move is the difference.

So the chain now reads

  arena → 8 vertex orbits → potential φ (7 free) → 22 edge prices as differences → L_w → spectrum

where § 50 had 22 free parameters at the operator step.

### The Laplacian is excluded, and by a specific mechanism

Exactly one edge orbit lies inside a single vertex orbit. For it, φ(v) − φ(u) = 0
necessarily, so its price is zero for **every** member of the gradient family. L = D − A
assigns that orbit weight 1. Therefore

  **L = D − A is not in the 7-dimensional gradient-compatible family.**

§ 50 argued the exclusion from the program's own "price cannot be a single value." It is now
exact and local: a single edge orbit, the one whose endpoints are symmetry-equivalent,
forces the Laplacian out.

### The decisive test: does the rule disconnect the arena?

The obvious way for the literal gradient rule to fail is to zero out so many edges that a
conserving operator can no longer transport across the arena. Measured:

| | |
|---|---|
| arena edges with nonzero price | **276 of 300** |
| component reached from vertex 0 | **66 of 66** |
| vertices isolated | **0** |

**It survives.** The 24 zero-price edges are exactly the one within-orbit class, and
removing them leaves the arena connected.

### § 49 survives the whole family

Tested on four random potentials:

| φ | weights non-constant | [T, ρ(z)] = 0 | T𝟙 = 0 | P₀Φ stays exactly 0 |
|---|---|---|---|---|
| [3,4,1,6,7,2,1,1] | yes | yes | yes | **yes** |
| [6,9,1,4,9,3,7,4] | yes | yes | yes | **yes** |
| [2,0,9,4,1,6,6,3] | yes | yes | yes | **yes** |
| [9,2,9,2,4,5,3,9] | yes | yes | yes | **yes** |

Every member is equivariant, conserving, preserves the reader channels, and has
**non-constant** weights — which is precisely what the gradient condition was asked to
deliver and what the Laplacian cannot provide.

### Status

What the rule achieved, measured: 22 parameters → 7, the Laplacian excluded by a named
mechanism, the arena still connected, and the reader-channel structure of § 49 intact
throughout.

What it has not achieved: the 7 remaining parameters are not derived. The gradient rule is
the program's proposed additional law, not a consequence of C0/C1/C1a/C2, and nothing here
changes that. What would close it is a primitive quantity that assigns the potential to the
8 vertex orbits — the candidates named in review were relation-deficit, local capacity,
continuation count, and stabilizer size. Each is enumerable on 8 classes, so each is now a
finite check rather than a research direction.

The honest position: the gradient rule is doing real work — it cut the freedom by more than
two thirds and made a falsifiable structural prediction that passed — but it is still a law
supplied to the system rather than extracted from it.

## 52. Correction to § 51: the signed price and the kinetic weight are different objects

A review of Paper IV caught a real error in § 51, and running it rather than accepting it
confirms the review and sharpens the result.

**What was claimed.** § 51 reported the gradient condition as cutting the 22-dimensional
weight family to a 7-dimensional subspace, and stated flatly that L = D − A is excluded
from it.

**What is true.** A gradient is antisymmetric, p(u,v) = −p(v,u); a self-adjoint conductance
is symmetric, w(u,v) = w(v,u). These are different objects, and the computation used
w = |dφ| — an absolute value, which is not linear. Measured over 140 random invariant
potentials:

| object | dimension |
|---|---|
| signed price space (exact equivariant 1-forms) | **7 of 22, linear** |
| linear span of achievable symmetric weights \|dφ\| | **18 of 22** |

So the 7 is a **parameter count**, not a subspace of the weight space. The achievable
weights are a 7-parameter semialgebraic set with an 18-dimensional span. The subspace claim
is withdrawn; the parameter count stands.

**The Laplacian exclusion is conditional.** The one within-orbit edge class has signed price
zero for every invariant potential, but its *weight* is F(0) for a constitutive map
w = F(|p|):

| constitutive map | weight on the zero-price orbit | L reachable? |
|---|---|---|
| w = \|p\| or w = p² (F(0) = 0) | 0 | no |
| w = F(\|p\|) with F(0) > 0 | F(0) | yes |
| F ≡ 1 constant | 1 | **yes — this is L exactly** |

So L is excluded only under the identification of kinetic weight with gradient magnitude.
§ 50's argument from "the price cannot be a single value" survives, and § 51's Theorem is
restated: *the uniform Laplacian is excluded whenever F(0) = 0, not by the gradient
condition as such.*

**What survives unconditionally** is exactness: the circulation of p around every arena
cycle vanishes, verified over 40 cycles × 6 potentials with zero violations. That is a
statement about p and carries no commitment about w.

**The chain gains an arrow.** It is not φ → w → L_w but

  φ →(d)→ p →(F)→ w → L_w,

and the paper derives the first arrow only. Two open questions, now properly separate: what
generates the price field (five surviving candidates), and what converts a price field into
transformation cost (F unselected). The second was being silently collapsed into the first.

Paper IV was revised accordingly — § 8 restructured into six subsections with Correction 8.2
and Theorem 8.3 carrying the retraction in the text, the abstract's "cuts 22 to 7" repaired,
the Euler update stated explicitly with Δt = 1/64, g, initial condition and ℓ¹ norm, the
sign-ambiguity group bounded rather than counted, and the reproducibility artifact
enumerated.

## 53. What p = 0 means: refuted for ⟨z⟩, forced for G, and undecidable for F(0)

Three reviews converge on the semantic question left open by § 52 — what does a zero signed
price mean operationally — and all three leave it as a choice among F(0) = 0, F(0) > 0, and
w independent of p. One raises a fourth reading without testing it: that p = 0 might mean
the move is *reader-internal*, R(u) = R(v), the R∘T = R structure already in the programme.
That reading is not a choice if the arena settles it. Two runs, opposite outcomes.

### The ⟨z⟩ reading is refuted

If zero-price moves were internal to the central involution reader, each would satisfy
v = z(u). Measured: z fixes 6 arena vertices, giving 36 z-orbits, and

  **edge orbits that are z-internal: 0. Arena edges with v = z(u): 0 of 300.**

So the attractive identification fails outright. (The script that found this printed its
intended conclusion unconditionally and therefore printed a claim its own data contradicts;
the output paragraph is void and the measurement stands.) Null, and navigational: it says
the semantics depends on *which* reader is paired with the potential, and the pairing is not
free to choose.

### The G reading is forced

Lemma 8.1 forces φ to be G-invariant. The reader whose invariants generate the potential is
therefore G, not ⟨z⟩. Re-run against the Reynolds projector onto G-invariants, over 200
random fields:

| | |
|---|---|
| zero-price edges where a G-invariant field differs at the ends | **0** |
| nonzero-price edges where a particular random field happened to agree | 816 of 55 200 |

The zero count is the exact direction: a zero-price edge has both ends in one G-orbit, so
**no** G-invariant field distinguishes them. The 816 are coincidental agreements of
individual random fields, not counterexamples to the characterization. Hence

  p = 0  ⟺  both ends in one G-orbit  ⟺  the move is invisible to the G-reader.

This is not posited. It follows from Lemma 8.1: because the potential must be invariant
under the same group whose invariants define it, **the price vanishes exactly on the moves
that the price-defining reader cannot observe.** That is the R∘T = R condition, recovered
here as a consequence rather than imported as an interpretation.

### F(0) does not affect the channel structure — measured

With that identification in hand, the remaining parameter is what a reader-internal move
costs kinetically. Tested with w = |dφ| + w₀ for the continuation-count potential, from a
purely odd initial field:

| w₀ = F(0) | ‖P₀Φ‖ at step 10 | ‖P₁Φ‖ at step 10 | P₀ exactly 0 |
|---|---|---|---|
| 0 | **0** | 8.946 | yes |
| 1 | **0** | 4.498 | yes |
| 3 | **0** | 1.421 | yes |

F(0) changes only the decay rate in the odd sector. The reader-channel separation is
identical for every value. **So the semantic question is not decidable from channel
behaviour on this arena**; deciding it needs a transport or conservation test that channel
structure does not supply.

### The coherence argument, labelled as such

§ 49 established on this arena that reader-null content is not causally inert: an invisible
sector sources the visible channel through an equivariant nonlinearity and is recoverable
from one visible observation. A zero-price edge is now measured to be a reader-internal
move. F(0) = 0 would make reader-internal moves kinetically absent, which is the opposite
of § 49's finding; F(0) > 0 leaves them active but unpriced. So the reading consistent with
the programme's own prior result is **F(0) > 0 — the move is free, not forbidden.**

That is an argument from coherence, not a measurement, and the table above shows why: the
arena's channel behaviour cannot discriminate. It is recorded as the consistent reading and
not as a result.

### Status of the two open questions

| question | status |
|---|---|
| what generates φ | five candidates, all nonconstant, none selected |
| what p = 0 means | **settled**: the move is invisible to the price-defining reader |
| what F(0) is | open; channel-undecidable; F(0) > 0 is the coherent reading |

The middle row is the advance. "What does zero price mean" was an open semantic choice in
§ 52 and is now a measured identification, with the wrong reader pairing explicitly
eliminated. What remains undetermined is narrower than it was: not the meaning of a zero
gradient, but the kinetic cost of a move that the reader defining the gradient cannot see.

## 54. Auditing the batch without pre-sorting: one retraction, one discriminator, one refutation

Six review documents arrived together. An initial pass sorted them into "two actionable
items and four interpretive ones" before testing anything, which is the wrong order — the
sort was a judgement made ahead of the measurement. Running every checkable claim in all
six produces three results, one of which the pre-sort would have discarded.

### Retraction: § 53's biconditional is false

§ 53 reported p = 0 ⟺ both ends in one G-orbit ⟺ invisible to the G-reader. The forward
direction is sound and follows from Lemma 8.1. The converse fails whenever the chosen
potential is **degenerate** — assigns equal values to distinct vertex orbits — and the
counterexample was already sitting in § 51's own audit table.

| φ | distinct values | zero-price edges | inside one G-orbit | **across orbits** |
|---|---:|---:|---:|---:|
| continuation count | 5 | 48 | 24 | **24** |
| orbit size | 3 | 144 | 24 | **120** |
| stabilizer order | 3 | 144 | 24 | **120** |
| 3-cell incidence | 6 | 36 | 24 | **12** |
| 4-cell incidence | 8 | 24 | 24 | **0** |

24 arena edges lie inside a single G-orbit and are forced to zero price for every invariant
potential. Everything beyond that count is a degeneracy of the particular φ. What survives
exactly:

  same G-orbit ⟹ p = 0 for **every** G-invariant potential,

and the converse only for a potential that separates the reader classes.

### The discriminator this produces

That correction is not only a weakening. Of the five candidates, exactly one separates all
eight vertex orbits — **4-cell incidence**, with 8 distinct values — and for it the measured
across-orbit zero-price count is **0**, so the biconditional holds exactly:

  for φ = 4-cell incidence,  p = 0 ⟺ both ends in one G-orbit ⟺ reader-internal.

§ 51 left five candidates with nothing to choose between them, and § 8.4 of Paper IV says so.
This is a selection criterion that is not taste: only one candidate makes the price field's
zero set coincide with the reader-internal moves. Every other candidate charges zero for
moves that *do* cross the reader's quotient, which means its price field and its own reader
disagree. Whether non-degeneracy should be *required* of a price law is a further question,
but it is now a stated property that one candidate has and four lack.

### Refutation: the export-degree formula

One document proposes an encapsulation depth: the minimal degree of a monomial coupling
that carries a hidden channel-k distinction into the trivial channel is m/gcd(m,k), since
rk ≡ 0 mod m is needed. For the C₂ odd sector this gives 2, matching § 49. Measured on this
arena across twelve random reader-null fields per reader, for the pointwise power Φ ↦ Φ^⊙r:

| reader | measured first r with P_inv(Φ^r) ≠ 0 | m/gcd(m,k) predicts |
|---|---:|---:|
| order 2 | **2** | 2 |
| order 3 | **2** | 3 |
| order 6 | **2** | 6 |

**Degree 2 for every reader order.** The formula is refuted for rational reader-null sectors,
and the reason is structural rather than accidental: over ℚ a reader-null sector is closed
under complex conjugation, and ζ·ζ̄ = 1, so a degree-two cross term always lands in the
invariant channel. The formula applies to a *pure* complex channel, which does not exist
over ℚ — the rational complement always bundles ω with ω̄.

The correct replacement is stronger and flatter:

  **For any finite cyclic reader, a rational reader-null sector exports at degree exactly 2
  under pointwise powers.** Degree 1 is excluded by construction, and 2 is achieved.

That consequence matters for the research programme the document proposes. "Measure the
minimal coupling degree needed to export a hidden distinction" cannot be a source of
variation across readers, because over the rationals the answer is constant. Scope: this is
measured for pointwise powers; a non-pointwise coupling algebra is not covered and could
behave differently.

### What remains unaudited

The cross-layer recursive structure — OOP, ADT, compiler IR, ISA, register, gate,
transistor, PCB, each arrow a reader quotient, with the test R_i∘T_i = R_i and
R_i(N(Ts)) ≠ R_i(N(s)) — is not runnable on this arena without defining those layers as
state spaces here. It is recorded as untested rather than endorsed. One observation in that
material does apply and sharpens § 49's own wording: if two states are equivalent under
*every* legal public operation then no later operation can distinguish them, so the § 49
pattern is not "abstractly equivalent states later distinguished" but "states equal under a
**restricted** reader, distinguished once a richer coupling is admitted." § 49 says
"invisible to P₀" throughout, which is the restricted reading, so no correction is needed —
but the distinction is worth keeping explicit.

### Method note

The pre-sort was the error, not any single claim. Two of the three results above came out of
documents classified as interpretive before being run: the discriminator from a correction
filed as a weakening, and the refutation from a formula filed as the one testable item but
whose scope went unchecked. A script in this section also printed a conclusion contradicting
its own table — "no tested primitive separates all eight orbits" immediately below output
naming one that does. Both failures have the same shape: a judgement reached before, or
independently of, the measurement.

## 55. UNLINKED — the entry is in no copy of this record

**Numbering (§ 134).** No copy holds § 55: not the project ledger, not the 17 Oct combined upload, and a search of the
other project documents finds none. § 54 ends and § 56 begins. The entry is UNLINKED and is not reconstructed. What later
entries say about it, quoted:

- § 56: "§ 55 concluded that nothing consumes the operator choice, so the φ ambiguity was dead weight", by looking for
  an explicit caller of Spec(L_w); the w-length measurement "was in § 55's own working output, misread as a failed
  predicate"; "§ 55's 'the dependency is unused' is retracted".
- § 57.5: "§ 55's search over φ was looking for a degree-1 answer to a degree-2 question", in a paragraph § 57.9 amends.

§ 56's "six surviving operators" are 4-cell incidence, sum neighbour degrees, closeness, paths of length 2,
deg + 4-cell and 4-cell / deg. Only the first is among § 54's five candidate potentials. The step that produced the
other five is not in the record.

## 56. Structural invocation: § 55 was too literal, and the consumer was already in the output

§ 55 concluded that nothing consumes the operator choice, so the φ ambiguity was dead
weight. That conclusion rested on looking for an **explicit** caller — some claim that
evaluates Spec(L_w). No such caller exists, and that much stands. But resolution does not
require an explicit call. Nobody shouts a name in a room where the frame already
distinguishes the people; the distinctions are present and the reader needs only an
interface that resolves them. C0 says distinction exists, not that someone must request it.

So the question is not *who calls the spectrum* but **does the frame already expose a
distinction that reads w**. It does, and the measurement was in § 55's own working output,
misread as a failed predicate.

### The structural consumer

w is a weight on the 1-cells. The 2-cells are built from 1-cells by ∂₂, which is already
part of the relation layer. Therefore every 2-cell carries a w-length, with no eigenvalue
computation and no explicit invocation:

  ℓ_w(f) = Σ_{e ∈ ∂f} w_e.

Measured across the six surviving operators, with the scale-free signature taken as the
normalised multiset of 2-cell lengths:

| operator | distinct triangle lengths | distinct square lengths |
|---|---:|---:|
| 4-cell incidence | 9 | 38 |
| sum neighbour degrees | 9 | 22 |
| closeness | 10 | 26 |
| paths of length 2 | 9 | 22 |
| deg + 4-cell | 9 | 38 |
| 4-cell / deg | 12 | 33 |

**Scale-free signature: 6 distinct of 6.** The coarse (count, count) pair collides in two
places — (9,38) and (9,22) each shared by two operators — which is why the earlier pass,
which printed only the counts, read this as a predicate that failed to resolve rather than
as an observable that discriminates.

So the operator layer **is** consumed, by a relation-layer quantity. § 55's "the dependency
is unused" is retracted; what survives from it is narrower and still true: no claim in the
ledger evaluates the spectrum, and the six operators agree on every previously registered
measurement. The consumer is structural, not spectral.

### The degeneracy is forced and reader-shaped

The second measurement is stronger than the first:

| | |
|---|---|
| 1-cells with w = 0 | **24 of 300** |
| identical across all six operators | **yes** |
| that set | exactly the reader-internal edge class |
| 2-cells with zero w-length | **14**, identical across all six |

The w-semi-norm on C¹ is therefore degenerate on a 24-dimensional subspace, and that
subspace does not depend on which price field is chosen. It is the class of moves the
price-defining reader cannot distinguish, which § 53 established is forced by Lemma 8.1.

  **The price field is blind exactly where its own reader is blind, and no choice of
  potential changes that.**

That is the encapsulation statement with a measurement attached rather than an analogy:
the kernel of the semi-norm *is* the encapsulated move set. And the 14 zero-length 2-cells
are relations assembled entirely from reader-internal moves — invisible to the price field
at every order, for every admissible w. They are the natural objects for § 49's export
mechanism to act on, since they are precisely what no price can reach directly.

### Status after the correction

| claim | status |
|---|---|
| no explicit consumer of Spec(L_w) | stands |
| six operators agree on all previously registered measurements | stands |
| "the φ dependency is unused" | **retracted** |
| the w-length of 2-cells is a structural consumer | measured, separates 6 of 6 |
| the 24-dim degeneracy equals the reader-internal class | measured, operator-independent |
| any one operator is thereby selected | **no** — discriminating is not selecting |

The resolution question is live again, and it now has a contract that can tell the
candidates apart. What it does not have is a requirement that picks one. That is the
difference between an interface that can resolve a distinction and a caller that needs a
particular value.

### Method note, second instance of the same failure

The pre-sort error of § 54 recurred here in a different form. The discriminating quantity
was computed, printed, and then classified against an expectation — "does this predicate
force a unique answer" — rather than read for what it showed, which was six distinguishable
operators. Both failures are the same shape: output interpreted through a prior
expectation instead of on its own terms. The rule that catches it is to state what a
measurement *separates* before asking what it *selects*.

---

## § 57. The reader interior is a sphere, and the price-blind set is its faces

§ 56 closed on an open target: *what second method gives the 14 price-blind 2-cells a
nonzero address* — explicitly not by varying φ, since no admissible reader-invariant exact
potential can price them. The constraint that cracked it was not a new measurement but a
refusal: there is no disconnected state to reconnect. The 14 cells were *found* through
∂₂, so they were never outside the relation layer. Whatever is unaddressed is unaddressed
by **this** interface, and the gap is the interface's, not the field's.

### 57.1 What the blind set spans — `blind.py`

```
2-cells total: 1283 (200 tri + 1083 sq)
price-blind 2-cells (every boundary edge reader-internal): 14
   of which triangles: 8   squares: 6
reader-internal 1-cells: 24 of 300
BLIND is a union of G-orbits: True
dim span(d_2 of the blind cells) = 13
span lies entirely inside the 24 reader-internal coordinate directions: True
m(blind) = {1+: 1, 1-: 1, 2-: 1, 3+: 2, 3-: 1}      dim check 13 == 13
blind span inside A (dim 235): True
```

Not flat. A 13-dimensional submodule of A carrying five of the six rational irreducible
types. The price interface's blind spot has more structure than the invariant reader's
blind spot (which was the single type 3⁻, with (3⁻)^G = 0).

### 57.2 The nested reader, and the reverse — `nest.py`

p = dφ with φ G-invariant forces p(e) = 0 on exactly those edges whose endpoints lie in
the same **vertex orbit**. Blindness is therefore a reader property, and it must move when
the reader nests inward. Over all 26 subgroups H ≤ G:

| \|H\| | vertex orbits | params over G | internal 1-cells | blind 2-cells |
|---:|---:|---:|---:|---:|
| 1 | 66 | +58 | 0 | 0 |
| 2 | 36–48 | +28…+40 | 0 | 0 |
| 3 | 22 | +14 | 6 | **2** |
| 4 | 24–34 | +16…+26 | 0 | 0 |
| 6 | 12 | +4 | 12 | **2** |
| 8 | 24 | +16 | 0 | 0 |
| 12 (A₄) | 8 | +0 | 24 | **14** |
| 24 (G) | 8 | +0 | 24 | **14** |

Reverse check, as required: **no cell is blind under H but addressable under G, and no new
internal edge ever appears** — resolution is monotone under reader refinement, 0 violations
across all 26 subgroups. A₄ already has all 8 orbits, so the central involution z merges
nothing: the blindness is an A₄ fact, not a C₂ fact.

The decisive line of that run is not in the table. **All 24 reader-internal 1-cells sit
inside a single vertex orbit** — orbit 0, size 12. The other seven orbits contain none.

```
   orbit : size : internal edges inside it
       0 :   12 : 24
   orbits with NO internal edge: [1, 2, 3, 4, 5, 6, 7]
```

12 vertices, 24 edges, 14 cells on them. 12 − 24 + 14 = 2.

### 57.3 The interior is the cuboctahedron — `interior.py`

```
interior orbit: index 0, 12 vertices, 24 internal edges
degree sequence: [4] regular: True
triangles: 8    chordless 4-cycles: 6    faces F = 14
Euler V - E + F = 12 - 24 + 14 = 2
integer spectrum: {-2: 5, 0: 3, 2: 3, 4: 1}   total 12 of 12
cuboctahedron model vertices: 12   edges 24   regular deg [4]
  cuboctahedron spectrum: {-2: 5, 0: 3, 2: 3, 4: 1}
SPECTRA MATCH: True
explicit graph isomorphism to cuboctahedron: FOUND [0, 1, 3, 2, 4, 8, 5, 9, 6, 11, 10, 7]
face boundary matrix: 14 faces x 24 edges, rank 13, kernel 1
```

The cuboctahedron model was built independently as the twelve points of ℤ³ with
coordinates a permutation of (±1, ±1, 0), adjacency at squared distance 2. The
isomorphism is explicit, not inferred from invariants.

So the reader-internal structure of the K = 2 token arena on this witness is the 1-skeleton
of the cuboctahedron, and the 14 price-blind 2-cells are **exactly its 14 faces**. The
13-dimensional span of § 57.1 is 14 − 1, and the deficit of 1 is the Euler relation.

### 57.4 The rank defect is the fundamental class — `sphere.py`, `sphere2.py`

```
faces 14, edges 24, boundary rank 13, face-relations 1
the single relation, as integer face coefficients:
   [1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1]
all coefficients +-1 (an orientation of every face): True
```

Every coefficient is a unit. The one relation is an orientation of the closed surface —
the fundamental class [Σ], not a deficiency. The 13 is not a shortfall against 14; it is
dim of a 2-sphere's face module modulo its own fundamental class.

Reader action on the sphere:

```
elements of G preserving the interior orbit setwise: 24 of 24
face orbits: 2  (sizes [8, 6])   triangles 8, squares 6
sphere is vertex-transitive under the reader: True (orbits [12])
m(Q[faces], unsigned) = {1+:2, 1-:1, 2+:1, 2-:0, 3+:1, 3-:2}   dim 14
m(signed face module)  = {1+:1, 1-:2, 2+:0, 2-:1, 3+:2, 3-:1}   dim 14
fundamental class carries the linear character: 1-
z acts on the class by: -1
```

A prediction died here and is recorded as a null result: I expected A₄ ⊂ S₄ to split the
8 triangles 4 + 4. It does not — G is transitive on all 8. Since 8 ∤ 12, A₄ alone *cannot*
be transitive on 8, so the central z must be doing the joining. Tested:

```
z fixed points on the 12 interior vertices: 0 (antipodal map has 0)
z is an involution on them: True
z maps every vertex to distance 3  (cuboctahedron diameter 3)
A4-orbits of triangles: [4, 4]      z exchanges them: True
```

**z is the central inversion of the cuboctahedron.** It is fixed-point-free on the
interior, carries every vertex to its antipode, exchanges the two inscribed tetrahedra,
and reverses orientation — degree −1, which is why [Σ] carries 1⁻ and not 1⁺. The reader
group C₂ × A₄ sits as the index-2 subgroup {±1} × A₄ of the cuboctahedron's full symmetry
group S₄ × C₂ of order 48.

**Independent cross-check.** The signed face module minus the fundamental class is

```
{1+: 1, 1-: 1, 2+: 0, 2-: 1, 3+: 2, 3-: 1}    dim 13
```

and `blind.py` measured the ∂₂ image inside C¹(arena), by a different route and with the
arena's own sign convention,

```
m(blind) = {1+: 1, 1-: 1, 2-: 1, 3+: 2, 3-: 1}  dim 13
```

Term by term identical. Two measurements, two bases, one module.

*(A dimension formula was wrong on first run: Σ m_λ·dim λ·⟨χ_λ,χ_λ⟩ gave 16 for a
14-dimensional module. The rational irreducible 2± is ω + ω̄, of ℚ-dimension 2, so the
Schur index must not multiply the dimension. Corrected in `sphere2.py`; the multiplicities
were never wrong, only the check.)*

### 57.5 Why no price field could ever have worked — `degree.py`

> **Amended by § 57.9.** This subsection splices two different facts. The heading, the
> 2000-cochain run, and the sentence about "dropping invariance" do not stand as written.

This is the part that makes the answer forced rather than found.

```
d_2 (sum_f orient_f * face_f) = 0 on all 24 interior edges: True
max |<q, boundary of class>| over 2000 random 1-cochains q: 0
```

The random cochains are **arbitrary**, not admissible price fields — unconstrained, signed,
with no potential and no invariance. All of them give zero. The reason is one line:

  ⟨q, ∂₂C⟩ = ⟨∂₂ᵗq, C⟩ and ∂₂C = 0 for a cycle, for every q.

A 1-cochain reaches a 2-chain only through its boundary, and the boundary of a cycle is
zero. The price field p = dφ is a 1-cochain. **The blindness is a degree mismatch, not a
wrong value.** § 55's search over φ was looking for a degree-1 answer to a degree-2
question; no amount of varying φ, dropping exactness, dropping invariance, or changing F
could have reached it.

The address that does work is a 2-cochain. Take α(face) = its orientation:

```
alpha(face_f) = orient_f     <alpha, [Sigma]> = 14   (nonzero)
<g.alpha, g.[Sigma]> over all 24 readers: [14]       (invariant: True)
```

α and [Σ] both carry 1⁻, so the pairing lands in 1⁻ ⊗ 1⁻ = 1⁺ — reader-invariant and
nonzero. The interior has a degree, and 14 is it.

*(First run of this asked the wrong question: it held α fixed while moving the class, which
must give χ_{1⁻}(g)·14 = ±14, and reported "reader-independent: False" as if that were a
failure. The invariant pairing moves both objects. Re-run gives [14] for all 24. Recorded
rather than silently fixed, per the rule against accepting a correction verbally.)*

### 57.6 The cost of the second interface is chromatic — `color.py`

A reader H resolves all 14 faces iff no cuboctahedron edge is H-internal — iff the H-orbit
partition of the 12 interior vertices is a **proper colouring**. So the price of the second
interface is a graph invariant, and the question is whether the subgroup lattice can reach
the floor.

```
interior sphere: 12 vertices, chromatic number 3
  a proper 3-colouring, class sizes [4, 4, 4]
coarsest proper reader partition of the interior: 3 classes
  achieved by readers of order [4, 8], class sizes [4, 4, 4]
  largest such reader: |H| = 8
  equals the chromatic number: True
```

It reaches the floor exactly. The coarsest reader refinement that addresses the interior
costs three classes of four, which is χ(cuboctahedron) = 3, and the largest reader
attaining it is the **Sylow 2-subgroup of order 8** — maximum symmetry retained at minimum
cost, canonically determined rather than chosen.

The failures are as informative as the successes. Readers of order 3 and 6 never resolve
the interior no matter how many parameters they add: an order-3 element of A₄ rotates a
triangular face, so its orbits on the 12 *are* the four triangles of one tetrahedral class **[wrong — never run; see § 57.9]**
— improper by construction, [3,3,3,3] and [6,6]. Order 3 is tangent to the obstruction.

### 57.7 Separates / selects

Applying § 56's rule before drawing any conclusion:

| measurement | what it separates | what it does not select |
|---|---|---|
| ℓ_w = 0 on 14 cells, all admissible w | price-addressable from price-blind relations | any φ, and any second interface |
| 24 internal 1-cells in one orbit | reader-interior from reader-crossing structure | which reader |
| V − E + F = 2, certified isomorphism | a closed interior surface from an unstructured null set | nothing further — the surface is forced |
| rank 13 of 14 faces | fundamental class from deficiency | which 2-cochain reads it |
| ⟨q, ∂₂[Σ]⟩ = 0 for all q | degree-1 observables from degree-2 observables | a canonical degree-2 observable |
| χ = 3, attained at \|H\| = 8 | readers that resolve the interior from readers that cannot | a reason to pay the cost |

### 57.8 Status

| claim | status |
|---|---|
| the 14 cells are "universally price-blind" | **stands, and now explained** — degree mismatch |
| "they may be reachable by a non-price reader, a higher coupling, or the § 49 export" | **resolved** — the reachable channel is degree 2, the orientation class |
| the 13-dim span is a deficiency of the 14 | **retracted** — it is 14 modulo the fundamental class |
| the blind set is flat | **retracted** — apparent flatness, not genuine |
| A₄ ⊂ S₄ splits the 8 triangles 4 + 4 | **refuted** — one orbit of 8; the split is the A₄-orbit refinement that z exchanges |
| blindness lives in the field | **never stood** — it is monotone in the reader, 0 violations |
| a caller requires one particular degree-2 cochain | **open** — the selection problem is unchanged in kind |

The project's own standing question was whether apparent flatness can be told from genuine
flatness from the surface. Here it could not be: ℓ_w(c) = 0 for all 14 cells under every
admissible price field looks exactly like a field with no difference-structure. It had a
2-sphere in it. The thing that told them apart was not a sharper degree-1 measurement — no
such measurement exists, by § 57.5 — but asking what the null set *is* instead of what it
*scores*.

**Scope.** This is the K = 2 arena of one witness graph. That a reader interior is a closed
surface, that its faces are exactly the price-blind set, and that the refinement cost is
chromatic are all measured here and unmeasured anywhere else.

### 57.9 Audit before freezing — `recheck.py`

Four reviews recommended freezing § 57 with a law of the form *"a zero at degree k must be
tested against the degree of the null structure"* and the chain
price-null → S² → H₂ → C² → 14 → χ = 3. Before accepting either, § 57 was re-run against
itself in the arena's own coordinates (300 columns, the arena's sign convention — not
`interior.py`'s local construction). Three statements in § 57 fail, all mine.

```
== C1  is the 2000-cochain test evidence of anything? ==
  relations among the 14 arena rows: 1;  d_2[Sigma] is the zero vector: True
== C2  can a degree-1 field address the 14 faces individually? ==
  arbitrary signed 1-cochain q:  faces with <q, d f> != 0 : 14 of 14
                                 faces with sum|q(e)| != 0 : 14 of 14
  reader G  (order 24)      exact invariant price p=d(phi):  null 1-cells  24   faces with l_w=0: 14 of 14   min l_w=0
  reader Sylow-2 (order 8)  exact invariant price p=d(phi):  null 1-cells   0   faces with l_w=0:  0 of 14   min l_w=40
== C3  what do order-3 readers do to the interior? ==
  order-3 reader: interior orbit sizes [3, 3, 3, 3], internal edges per orbit [0, 0, 3, 3]   (all four)
== C4  monotonicity on the whole lattice ==
  comparable pairs H1 < H2: 100    violations of blind(H1) subset blind(H2): 0
  the REVERSED inclusion blind(H2) subset blind(H1) fails on 45 of them
== C5  how special is a 2-cycle that every dq misses? ==
  rank d_2 = 235   cycle rank of the arena graph = 300 - 66 + 1 = 235   (H_1 = 0: True)
  dim ker d_2 = 1283 - 235 = 1048 independent 2-cycles in the arena, ALL invisible to every dq
  of those, supported entirely on the price-null set: 1
```

**C1 — the 2000-cochain test was vacuous.** It paired random vectors with ∂₂[Σ], which is the
zero vector. Any vector paired with zero is zero. The run tested nothing beyond the one
line ∂₂[Σ] = 0 and is withdrawn as evidence. The correct pairing statement is discrete
Stokes, ⟨dq, [Σ]⟩ = ⟨q, ∂₂[Σ]⟩ = 0.

**C2 — "degree mismatch" does not explain the 14 zeros.** The measured blindness of § 56 is
per face: ℓ_w(f) = 0 for each of the 14. Its cause is reader invariance — φ is constant on
the one orbit that carries the interior — and it is cured **at degree 1**: an exact,
H-invariant price field for the order-8 reader has 0 null 1-cells and gives every one of
the 14 faces a nonzero length (min 40). An arbitrary 1-cochain addresses all 14
individually. § 57.5's "no amount of … dropping invariance … could have reached it"
contradicts § 57.2's own table and is retracted. The Stokes statement is about a different
object: the single aggregate [Σ], not the faces.

**C3 — the order-3 mechanism was stated without being run.** An order-3 reader's four
interior orbits are two triangles and two *independent* triples (the alternate vertices of
the equatorial hexagon), not four triangles. That is what § 57.2's table already said —
6 internal edges, 2 blind faces — and I wrote a sentence that disagreed with it. The
conclusion (order 3 and 6 cannot properly colour) stands; the reason is the two fixed
opposite triangles.

**C4 — monotonicity holds on the whole lattice**, 100 comparable pairs, 0 violations, in the
direction H₁ ≤ H₂ ⟹ blind(H₁) ⊆ blind(H₂). One review wrote the inclusion the other way
round; that version fails on 45 pairs. § 57.2 had only checked each H against G.

**C5 — being a 2-cycle that every dq misses is not rare here.** H₁ of the arena 2-complex
vanishes, so ker ∂₂ has dimension 1048: over a thousand independent closed 2-chains, every
one of them invisible to every exact 2-cochain, and this has been true since A = im ∂₂ was
first measured at 235 of 1283. What singles out [Σ] is not its degree. It is the **only**
one of the 1048 supported entirely on the price-null set.

#### What § 57 is, after the audit

Two independent facts that the first write-up and the reviews fused into one chain:

| | fact | cause | cure | cost |
|---|---|---|---|---|
| **A** | each of the 14 faces has ℓ_w = 0 | reader invariance on one 12-vertex orbit | a finer reader, still a degree-1 exact price | χ(cuboctahedron) = 3, attained at \|H\| = 8 |
| **B** | the 14 faces close into a sphere; their boundaries have rank 13 | ∂₂[Σ] = 0 | a 2-cochain not of the form dq | none — but generic to all 1048 arena 2-cycles |

A is the nested-reader result and it is the one that carries the program's claim: the gap
moved with the cut and the object did not. B is certified and is what the null set *is*,
but it is not why the price read zero. The proposed law is therefore **not** frozen: on
this witness the zero at degree 1 was resolved at degree 1.

⟨α, [Σ]⟩ = 14 is the number of faces — the squared norm of a ±1 vector — not a topological
degree. Its content is only that it is nonzero, i.e. α ∉ im d on Σ.

Accepted from the reviews: C₂(Σ)/⟨[Σ]⟩ ≅ im ∂₂ is an isomorphism (first isomorphism
theorem), not an equality of subspaces; and the Stokes form of the pairing.

| claim | status |
|---|---|
| interior = cuboctahedron, explicit isomorphism | stands |
| rank 13 = 14 − 1, kernel = [Σ], carries 1⁻, z antipodal | stands; re-derived in arena coordinates |
| module cross-check, signed faces / [Σ] ≅ ∂₂ image | stands |
| reader monotonicity | stands, now on all 100 comparable pairs |
| chromatic floor 3 attained by the order-8 reader | stands |
| 2000-cochain test as evidence | **withdrawn — vacuous** |
| "the blindness is a degree mismatch" | **retracted** — it is reader invariance; cured at degree 1 |
| "order-3 orbits are the four triangles" | **retracted** — two triangles, two independent triples |
| "the interior has a degree, and 14 is it" | **retracted** — 14 is the face count |
| the degree-k law proposed for freezing | **not adopted** on this evidence |

Run record: `recheck.py` sha256 `68a803df38fc8a15…`, exact rationals, deterministic
(seed 11 for the one random cochain), 9 s. Scope unchanged: K = 2, one witness.

---

## § 58. Why the null set closes: the interior is the medial graph of the witness's octahedral core

§ 57.9 left one thing unexplained: reader invariance accounts for the zeros, but not for
why the null support is one cuboctahedral sphere. The suggested route was downstream —
enumerate the minimal cycles of the 24 null edges and look for a local selection rule. The
route taken was upstream: ask what the interior orbit *is* in the witness X, before asking
anything about its cycles.

### 58.1 What the orbit is — `why.py` P1

```
X: 12 vertices, 30 edges, degrees [3, 7], G-orbits on V(X): [6, 6]
z = (0 3)(1 4)(2 5)(6 9)(7 10)(8 11);  z-pairs are X-non-edges at X-distance 2
orbit size  pair is   X-dist  int.edges rep
0     12    edge      1       24        {0,1}
1     3     non-edge  2       0         {0,3}
2     12    edge      1       0         {0,6}
3     6     edge      1       0         {0,7}
4     12    non-edge  2       0         {0,8}
5     6     non-edge  2       0         {0,10}
6     12    non-edge  2       0         {6,7}
7     3     non-edge  2       0         {6,9}
```

X is not vertex-transitive: six vertices of degree 7 and six of degree 3. The interior
orbit is the set of X-edges joining two degree-7 vertices.

### 58.2 The orbital menu — `why.py` P2, P3, M4

The interior is a G-invariant graph on one orbit, hence a union of orbitals. G has 8
orbitals there, giving 5 symmetric non-diagonal classes of valency 4, 1, 1, 4, 1 and so a
menu of 2⁵ − 1 = 31 G-invariant graphs.

```
arena adjacency inside the orbit = union of classes [0] (valency 4); partial overlaps: 0; exact: True
    class 0: valency 4, shared token, other moves X-dist 1   <-- ON
    class 1: valency 1, shared token, other moves X-dist 2
    class 2: valency 1, shared token, other moves X-dist 2
    class 3: valency 4, disjoint pairs
    class 4: valency 1, disjoint pairs            (this one is z)
G-invariant graphs on the orbit: 31
graphs whose short-cycle complex is a closed pseudo-surface: 2
    classes [0]: E=24 tri=8 sq=6  V-E+F=2   <-- the arena's
    classes [3]: E=24 tri=8 sq=6  V-E+F=2
class 3 == class 0 with one end sent through the central inversion z: True
```

Symmetry does not force the sphere: 29 of the 31 invariant graphs do not close. The arena
switches on exactly one orbital, and that orbital is one of the two that do. The other is
its antipodal twist, cospectral with it.

Local rule, re-measured after fixing a bug in the link test (triangles were being skipped):

```
every interior edge lies in (triangles, squares): [(1, 1)]
vertex links (neighbours, link edges, link degrees): (4, 4, [2, 2, 2, 2])
```

Each edge has exactly two faces and each vertex link is a single 4-cycle. That is a closed
surface by local data alone; connected and orientable then gives exactly one closed
2-chain. So closure and uniqueness are both consequences of the edge-in-two-faces rule.
What remains is why class 0 has that rule.

### 58.3 The answer — `medial.py`

Class 0 reads: two X-edges ab and ac are adjacent when b ~ c. That is two sides of a
triangle of X. So the hypothesis was specific: the degree-7 vertices carry an octahedron,
and the interior is its **medial graph**.

```
== M1 ==
degree-7 vertices [0..5]: induced graph 12 edges, regular [4], non-edges [(0,3),(1,4),(2,5)] (a perfect matching)
=> K_{2,2,2}, the octahedron graph: True
triangles of the core: 8
== M2 ==
interior vertices are exactly the 12 core edges: True
medial(core) built from the 8 faces: 24 edges;  equal to the arena's interior edge set: True
== M3 ==
 8  triangle = the 3 sides of a core face (both tokens rotate round a face)
 6  square = one token parked on a core vertex, the other walks its link (link length 4): True
count check: faces(core) + vertices(core) = 8 + 6 = 14;  V-E+F = E0 - 2*E0 + (V0+F0) = V0-E0+F0 = 2
```

Equality is as sets of arena edges, not up to isomorphism. The three non-edges of the core
are exactly the z-pairs, which is why z came out as the antipodal map in § 57.4.

So the sphere is **recovered, not derived**. It is the octahedron already sitting inside
X, read through the two-token arena: a configuration of two adjacent tokens is an edge,
moving one token while they stay adjacent pivots that edge inside a triangle, and that is
the textbook rectification octahedron → cuboctahedron. The 14 blind cells are the 8 faces
of the core (both tokens circulate a face) and the 6 vertex figures (one token parked, the
other walks the link). 12 − 24 + 14 = 2 because 6 − 12 + 8 = 2.

No other orbit has an interior because the reader separates the two kinds of edge at each
degree-3 vertex (orbits 2 and 3), so a token pivoting there always crosses orbits — 0
candidate internal moves in every other orbit (`why.py` P5).

### 58.4 Controls that the mechanism predicts differently — `medial.py` M5

The vertex figure at a core vertex is a cycle of length equal to its degree, and the arena
only has 2-cells of length 3 and 4. So the mechanism predicts closure exactly when every
core vertex has degree 4 — and predicts failure in opposite directions on either side.

```
octahedron alone     |Aut|=48   internal 24   blind 14 (8 tri + 6 sq)
    V=12 E=24 tri=8 sq=6   V-E+F=2    faces-per-edge [2]  closed 2-chains: 1
icosahedron (deg 5)  |Aut|=120  internal 120  blind 20 (20 tri + 0 sq)
    X-edge configs:   V=30 E=60 tri=20 sq=0  V-E+F=-10  faces-per-edge [1]  closed 2-chains: 0
    non-edge configs: V=30 E=60 tri=0  sq=0             faces-per-edge [0]  closed 2-chains: 0
tetrahedron (deg 3)  |Aut|=24   internal 12   blind 23 (8 tri + 15 sq)
    V=6  E=12 tri=8 sq=15  faces-per-edge [7]  closed 2-chains: 16
```

- Octahedron with nothing attached: the same sphere. The six degree-3 vertices of the
  witness play no part in it.
- Icosahedron: the interior is the icosidodecahedron's graph with its 20 triangles and no
  pentagons — every edge has one face, nothing closes, zero closed 2-chains. Predicted.
- Tetrahedron: the medial graph is the octahedron graph, which has extra 4-cycles; it
  over-closes, 16 closed 2-chains. Predicted "not one sphere"; my predicted cell count
  (8 + 3) was wrong — I forgot the 12 chorded 4-cycles, which `cycles_len` counts.

Candidate uniform statement, argued not run: for a triangulated closed surface
Σ(6 − deg v) = 6χ, so all degrees equal to 4 forces V = 3χ, and the only simplicial case is
the sphere with V = 6. With 2-cells cut off at length 4, the octahedron is the one
triangulated closed-surface core whose pivot interior closes into exactly one surface.

### 58.5 Separates / selects, and status

| measurement | separates | does not select |
|---|---|---|
| 2 of 31 invariant graphs close | symmetry-forced from rule-forced | which rule |
| interior == medial(core) as sets | inherited sphere from emergent sphere | — it is inherited |
| three controls | degree-4 cores from degree-3 and degree-5 | anything about K > 2 or longer cells |

| claim | status |
|---|---|
| "why the price-null set closes into one sphere" is open | **closed for this witness** |
| the sphere is produced by the reader or by the price interface | **no** — it is the witness's octahedral core, rectified by the two-token move |
| the six degree-3 vertices contribute to it | **no** — octahedron alone gives the identical interior |
| closure is generic for two-token arenas | **no** — fails on the icosahedron, over-closes on the tetrahedron |
| closure ⟺ core degree 4, given cells of length ≤ 4 | supported on 3 controls + an Euler count; not a theorem |

Run record: `why.py`, `medial.py` (sha256 `7c17c320ca0695de…`), exact arithmetic, no
randomness, under 1 s each. Scope: K = 2; the witness and three control graphs.

---

## § 59. The cell cutoff: closure at L = core degree, and only there — `cutoff.py`

§ 58 predicted that admitting 5-cycles as cells would close the icosahedron's interior
into the icosidodecahedron. The prediction was sharpened before running: with cells = all
cycles of length ≤ L, a deltahedral core of degree d closes into exactly one sphere at
L = d and at no other L. Below d the vertex figures are not cells; above d, chorded cycles
enter.

Blind cells are the cycles of the interior graph, so cycles were enumerated there with an
independent DFS; at L ≤ 4 the counts match the library's arena-wide `cycles_len` on all
four graphs (23, 14, 14, 20).

| core | d | L ≤ 3 | L ≤ 4 | L ≤ 5 | L ≤ 6 |
|---|---:|---|---|---|---|
| tetrahedron | 3 | **8 tri — one sphere** | +15, kernel 16 | +24, kernel 40 | +16, kernel 56 |
| octahedron | 4 | 8 tri, faces/edge 1, kernel 0 | **8 tri + 6 sq — one sphere** | +24, kernel 25 | +52, kernel 77 |
| witness X | 4 | same as octahedron | **same — one sphere** | same | same |
| icosahedron | 5 | 20 tri, kernel 0 | 20 tri, kernel 0 | **20 tri + 12 pent — one sphere** | +60, kernel 61 |

"One sphere" means all three of: every edge in exactly two cells, V − E + F = 2, exactly
one closed 2-chain. It occurs once per row, at L = d: the octahedron (6, 12, 8), the
cuboctahedron (12, 24, 14), the icosidodecahedron (30, 60, 32). The three deltahedral
Platonic solids give their three rectifications.

**What happens above d is redundancy, not new closure.** From the same output,
rank ∂₂ = cells − kernel is 7, 7, 7, 7 for the tetrahedron; 13, 13, 13 from L = 4 for the
octahedron; 31, 31 from L = 5 for the icosahedron — in each case the cycle rank E − V + 1
of the interior graph, reached at L = d and constant afterwards. Every cell added above d
adds exactly one to the kernel (16 = 1 + 15, 25 = 1 + 24, 61 = 1 + 60, …). At L = d + 1 the
added chorded cells number one per edge: the two faces across that edge, glued. So § 58's
"over-closes" should read: the boundary image is already saturated at L = d; longer cells
are sums of faces.

The vocabulary-independent statement is therefore about the image, not the kernel:
**L = d is the first cutoff at which the interior has no 1-cycle that is not a boundary,
and the only one at which the cell set is itself a surface.**

**Boundary of the claim.** On the pentagonal bipyramid (degrees 4 and 5) the core's edges
are two reader orbits, and the interior is not the medial graph (15 vertices, 30 edges)
but two disjoint 5-cycles — the two apex vertex figures — which never close. The interior
is the medial graph only when the reader puts all core edges in one orbit. Otherwise the
reader cuts the medial surface along its own orbit boundaries, which is § 57.9's fact A
acting on § 58's object.

**Correction to a reading of § 58.** The interior is not the line graph of the octahedron.
L(O₆) has 36 edges and degree 6; the interior has 24 and degree 4. It is the subgraph of
the line graph on pairs of edges that share a face.

| claim | status |
|---|---|
| icosahedron + 5-cells → icosidodecahedral sphere | **confirmed**: 20 + 12 cells, faces/edge 2, χ = 2, one closed 2-chain |
| closure into one sphere occurs at L = d and only there | confirmed on 3 cores + the witness |
| above d the interior "over-closes" | **restated** — rank saturates at L = d; extra kernel is redundancy |
| interior = medial graph of the core | only when core edges are one reader orbit (bipyramid fails) |
| a uniform theorem for triangulated cores | not attempted; all confirming cores are vertex-transitive deltahedra |

Run record: `cutoff.py` sha256 `aff7568ecf537aad…` for the sweep, `ae8d5c6d8fdb6633…` with the bipyramid row;
exact arithmetic, no randomness, under 1 s. Scope: K = 2.

---

## § 60. Binding the interior to work already in the project — `bind.py`

Asked to look in the existing work for more. Four earlier results turn out to be about the
same 12 states, and none of them had been connected to each other or to §§ 57–59. Each was
stated as a hypothesis and run; nothing below is a reading.

Sources inside the project: *Merged.docx* Part III ("the edge is the state; the projection
is the writer") and its second-order memory-layer result; `relation-layer-k4-refutation.md`
(the 𝒦₄ survivor h); `the-clock-mod-d.md` (period 22587, a clock with 24 values recorded as
"an observed coincidence, not a claim"); `c1-is-the-abrams-hypothesis.md` § 4 (usable at
length 3, erasable at length 4); `relation-layer-omitted-cycle-and-traversal-residue.md`
(rotation triangles and spectator squares).

### 60.1 The reader turns each interior state into (prev, cur)

```
core edges whose two ends are exchanged by some reader element: 0 of 12
ordered adjacent core pairs: 24; reader orbit of (0,1): 12; one orientation per edge: True
the 24 interior arena edges, read with that orientation: {'head-to-tail: (prev,cur)->(cur,next)': 24}
writer (prev,cur)->cur: preimages per cur [2] (= exactly 1 bit erased); continuations per state [2]
```

An interior state is an unordered pair of adjacent tokens. No element of G swaps the two
ends of a core edge, so G itself gives every state an order, and under that order all 24
interior moves are single steps (prev, cur) → (cur, next). None are tail-to-tail or
head-to-head. The projection (prev, cur) → cur is exactly 2-to-1. That is Part III's table
— reader a step on edges, writer a projection erasing one bit — found in the arena with no
construction added. The "mark" is the tail of the reader's own orientation.

### 60.2 The two deterministic rules generate the sphere

Each state has two continuations, one through each A₄-class of core faces. Fixing the class
gives two rules T₊ and T₋.

```
A4-classes of core faces: [4, 4]
T+ is a permutation of the 12 states: True, cycle type [3,3,3,3];  T-: True, [3,3,3,3]
z T+ z == T-: True
<T+,T-> has order 12; regular on the 12 states: True
every reader element commutes with T+ and T-: A4 part True, all of G False
z lies in <T+,T->: True
relators: T+^3=1, T-^3=1, (T- T+^-1)^2=1 all True; T- T+^-1 is a fixed-point-free involution: True
Cayley graph on generators T+,T- == the arena interior, as edge sets: True (24 edges)
relator cosets: 4 + 4 triangles, 6 squares -> 14 faces
```

So the interior is the Cayley graph of A₄ on two elements of order 3, and its 14 faces are
the cosets of the three relators. The reader's A₄ acts on the 12 states on one side and the
rules act on the other, which is why they commute; z does not commute with the rules — it
exchanges them — and it is itself a word in them. § 57's objects restated: the 8 triangles
are the orbits of the two rules, the 6 squares are the orbits of the involution T₋T₊⁻¹, the
closed 2-chain is the statement that these relators present the group.

**Collision.** The cuboctahedral graph as a Cayley graph on two 3-cycles is standard
(MathWorld's Cayley-graph table lists it with generators (2 3 4) and (1 2 3)). Direction of
arrival here: from the price-null set of a reader, not from the group.

### 60.3 The 𝒦₄ survivor is the forward direction, and the period is 3t

```
dim C1_G = 22; G-invariant cochains closed on all 1083 4-cycles: 8; harmonic: 1
primitive integral harmonic h equals the vector recorded in the refutation doc (up to sign): True
h on interior edges, taken in the forward handshake direction: {7529: 24}
for all 8 closed invariant cochains the interior value is one constant per cochain: True
circulation of h on the 8 interior triangles: ±22587 (all 8)    on the 6 interior squares: 0 (all 6)
period of h over all arena loops: d = 22587;   3|t| = 22587;   equal: True
```

The refutation doc's survivor has first coordinate −7529, and the clock doc's period is
22587. 22587 = 3 × 7529. On the interior h is the constant 7529 on every edge in the forward
direction — it *is* the forward indicator, scaled — and that value does not depend on the
representative, because exact invariant cochains vanish on the interior (§ 57.9, fact A). A
triangle is three forward steps, so it carries 3t; a square alternates forward and backward,
so it carries 0.

That localises two earlier findings on the sphere: "triangles read the residue at full rank,
the entire square vocabulary reads half of it" and "usable at length 3, erasable at
length 4". The price-null set of the exact interface is exactly where the non-exact
survivor is canonical.

### 60.4 The clock is the cheapest resolving reader

```
U mod d exact on every arena edge: True;  distinct clock values: 24
U.g - U is constant for every g (a character G -> Z/d): True;  values [0, 7529, 15058]
kernel order 8;  image order 3;  kernel is the Sylow 2-subgroup: True; contains z: True
kernel-reader orbits on the arena: 24;  U constant on each: True;  U separates them: True
clock values on the interior: [4, 4, 4]
clock classes are a proper colouring of the interior: True
```

- The clock is not G-invariant: it shifts by a character of order 3. Paper IV's Lemma 8.1
  (equivariant exact price ⟹ invariant potential) rests on Hom(G, ℚ) = 0; modulo d the
  character exists, and this is it.
- Its kernel is the order-8 subgroup — the reader § 57.6 found as the largest one attaining
  the chromatic floor. The three classes of four are the three clock values on the interior.
- The "24 values" coincidence in `the-clock-mod-d.md` is explained: 24 is the number of
  arena orbits of the kernel reader, and the clock is constant on each and separates them.
  It was never |Aut(X)|. (That doc also says 7 vertex orbits; there are 8, rank d₀ = 7.)

### 60.5 Separates / selects, and status

| measurement | separates | does not select |
|---|---|---|
| orientation, 24 of 24 head-to-tail | a state from a (prev, cur) pair | T₊ versus T₋ — z exchanges them |
| h = t·forward on the interior | forward from backward | a sign for the class |
| character of order 3, kernel of order 8 | the clock's reader from all 26 | a reason to read the clock |

| claim | status |
|---|---|
| the handshake needs to be invented for the arena | **no** — the interior moves are it, under the reader's own orientation |
| interior = Cay(A₄; T₊, T₋), faces = relator cosets | measured; the graph fact is standard |
| period 22587 = 3 × (interior value of h) | measured |
| "24 = \|Aut\|" in the clock doc | **replaced** — 24 = orbits of the order-8 kernel reader |
| cheapest resolving reader = kernel of the clock's character | measured |
| the second-order memory-layer result (65,536 paired states) transfers to the arena | **not run** — only the edge/step/1-bit structure was tested here |
| any of this beyond the witness | not run; the orientation needs a reader that never swaps an edge's ends, which the full octahedral group does |

Run record: `bind.py` sha256 `6393e5cf196ee5f0…`, exact arithmetic, no randomness, 0.35 s.

---

## § 61. Six queued bindings, run — `dig.py`, `d6.py`

The manual (`claude/nexus-manual.md` v0.1) was saved with six tests written as predictions
because the shell was down. All six are now run. Five predictions held; one generalisation
failed.

### 61.1 The memory layer on the interior (D1, D1b)

Source: *Merged* §4 — "knowing only the present leaves the next step undetermined; knowing
present plus mark determines it."

```
first-order  (cur -> next):               64 rule-books,   8 bijective
second-order ((prev,cur)->(cur,next)):  4096 rule-books,  64 bijective
```

| reader | fixes some state | equivariant second-order rules | first-order |
|---|---|---|---|
| trivial | no | 4096 | 64 |
| ⟨z⟩ | no | 64 | 8 |
| a mirror (order 2, ×3) | **yes** | **0** | 0 |
| a rotation (order 2 in A₄, ×3) | no | 64 | 0 |
| order 3 (×4) | no | 16 | 4 |
| order 4 with a mirror (×6) | **yes** | **0** | 0 |
| V₄ ⊂ A₄ | no | 8, all bijective | 0 |
| order 6 (×4) | no | 4 | 2 |
| order 8 | **yes** | **0** | 0 |
| A₄ | no | **2, both bijective** | **0** |
| G | **yes** | **0** | 0 |

Predicted and held: under A₄ no first-order rule exists and exactly two second-order rules
do — T₊ and T₋ — both bijective; under G none of either.

Not predicted, and sharper: **a reader admits a deterministic rule iff no element of it fixes
a state** (26 of 26), and every element that fixes a state *exchanges that state's two
futures*. Under the full reader each state's stabiliser has order 2 and does exactly that.
So the one bit the writer erases and the one bit of freedom in the continuation are the same
bit, and it is the bit the state's own stabiliser flips.

Collision, source read this time: Fredkin's second-order technique — the neighbourhood at
t − 1 selects a permutation which is applied to the state at t − 2. On the interior that is
the bijectivity condition (cur selects a bijection prev → next), and 64 = 2⁶ is one such
choice per core vertex. The count is run; the "iff" is the standard argument, not a test.

### 61.2 The four clauses of a cut (D2)

Source: *What a Cut Must Do*. Clause 3 = every state's successors leave its class; clause 4 =
the rule is well defined on classes.

```
|H|   classes  c3: moved  c4: induced update   on the quotient
1     12       12/12      T+ ok, T- ok         differ; [3,3,3,3]
2     6        12/12      T+ ok, T- ok         differ; [3,3]          <- passes
3     4        6/12       T+ ok, T- ok         differ; [1,3]
4     3        12/12      T+ ok, T- ok         coincide; [3]          <- passes
6     2        0/12       T+ no, T- no
8     3        12/12      T+ ok, T- ok         coincide; [3]          <- passes
12    1        0/12       —                    nothing moves
24    1        0/12       —                    nothing moves
coarsest reader passing clauses 2-4: 3 classes, |H| = 8; T+ and T- coincide; cycle type [3]
```

Held. On the three-class quotient the two methods are one tick of period 3. Read with § 61.1:
the order-8 reader has a deterministic *quotient* and no deterministic rule on *states*; its
subgroup V₄ has the same three classes and keeps 8 state-level rules. The mirrors are what
the order-8 reader adds, and they are what removes the rules.

### 61.3 The involutions (D3)

Source: *Merged* Part IX (order versus fixed points of a commutator) and Part X.

```
z                order 2, fixed points 0
T- T+^-1         order 2, fixed points 0
[T+,T-]          order 2, fixed points 0
three distinct involutions; a Klein group; z * (T-T+^-1) * [T+,T-] = identity
its orbits on the 12 states: 3 classes of 4 = the order-8 reader's classes
involutions in the reader group: 7; they generate a subgroup of order 8 = the clock's kernel
T+ and T- each step the class by the same amount: True
```

Held. The antipodal map, the square relator and the commutator of the two methods are the
three non-identity elements of one Klein group — each "order 2, no fixed points", the object
Part IX used to separate mass from opacity. Everything the reader can do with involutions
stays inside one clock phase; changing phase takes an element of order 3.

### 61.4 The ratio is 3 under both readers (D4, D5)

Source: `the-clock-mod-d.md`, period 9 at the trivial reader versus 22587 under Aut.

```
trivial reader: dim C1 = 300; closed on all 1083 squares: 66; exact: 65; harmonic: 1
forward interior values {-3: 24}; period d = 9; clock values 9;  period / forward value = 3
rotation   on a core face                       |circulation| = 9 : 8
rotation   on a face through a degree-3 vertex  |circulation| = 9 : 12
spectator  on a core face                       |circulation| = 9 : 72
spectator  on a face through a degree-3 vertex  |circulation| = 9 : 108
```

Held: 9 = 3 × 3 and 22587 = 3 × 7529. The two periods are normalisations of one class; the
representative-free number is the ratio 3. And the class has a one-line description: **zero
on every arena square, exactly one period on every one of the 200 arena triangles.**

### 61.5 The chromatic floor is not attained in general (D6) — a null

Source: § 57.6 found the reader lattice reaching the chromatic number on the witness.

```
tetrahedron  chi 3 | |Aut| 24   30 subgroups   coarsest resolving reader: 3 classes [2,2,2], |H| = 4   attains
octahedron   chi 3 | |Aut| 48   98 subgroups   coarsest resolving reader: 3 classes [4,4,4], |H| = 8   attains
icosahedron  chi 3 | |Aut| 120  164 subgroups  coarsest resolving reader: 9 classes, |H| = 4           DOES NOT
```

All three medial graphs are 3-chromatic, as predicted. On the icosahedron no reader's orbit
partition comes closer than 9 classes. So "the cost of resolving the interior is its
chromatic number" is false as a general statement: the chromatic number is a floor, the
reader lattice may not reach it, and § 57.6 was the favourable case. First run used only
subgroups with ≤ 2 generators; re-run on the full lattice (98 and 164 subgroups), same answer.

### 61.6 Status

| claim | status |
|---|---|
| A₄ admits exactly T₊, T₋; no first-order rule | measured |
| no rule ⟺ a reader element fixes a state; it swaps the two futures | measured, 26 readers |
| order-8 reader is the coarsest passing the cut clauses; one tick on its quotient | measured |
| z, T₋T₊⁻¹, [T₊,T₋] form a Klein group whose orbits are the clock phases | measured |
| period ÷ forward value = 3 at both readers; every triangle one period | measured |
| resolving cost = chromatic number | **refuted in general** — icosahedron needs 9 |
| the binary-ring experiment itself transfers to the arena | still not run |

Run record: `dig.py` sha256 `0b59a9dd831a4018…` (48 s); `d6.py` `81beb6174a75cd1d…` (4.1 s).
Exact arithmetic, no randomness. Scope: K = 2; witness, plus three cores for 61.5.

---

## § 62. Memory depth on the whole arena — D7, restated so it could fail (`d7.py`)

**Dropped, on instruction:** H = π/9 is no longer tracked on the map.

### 62.1 D7 as posed was vacuous

D7 asked whether the paired map (s_prev, s_cur) → (s_cur, s_next) on the 66-configuration
arena is bijective, with no pastless pairs and no transients. If the current configuration
selects a permutation of its neighbours and applies it to the previous one, the map on the
600 directed edges is a bijection for *every* such choice — that is Fredkin's theorem, and
it is the reason the binary-ring result in *Merged* §4 held for every rule tried. No choice
of rule can make it fail, so it was not run. (`E-VACUOUS`, caught before the run this time.)

### 62.2 What can fail: how much a reader must remember

A reader can make a deterministic choice only among continuations that the stabiliser of
what it remembers leaves fixed. Remembering more shrinks that stabiliser. So for each reader
H and depth k, count the length-k histories whose stabiliser fixes **no** non-backtracking
continuation; depth(H) is the first k at which the count is zero.

Predictions written before the run: under G the count is positive at depth 1 and zero at
depth 2; depth is monotone in the reader.

```
arena: 66 configurations, 600 directed edges, degrees [6, 8, 10, 12, 14]; readers: 26
|H|                     undetermined at depth 1, 2, 3, 4    depth
1    trivial            0    0  0  0                       1
2    a mirror  (x3)     2    0  0  0                       2
2    <z>                6    0  0  0                       2
2    rotation  (x3)     6    0  0  0                       2
3              (x4)     0    0  0  0                       1
4    (x3, x3, x1)       6 / 8 / 12   0  0  0               2
6              (x4)     6    0  0  0                       2
8                       12   0  0  0                       2
12   A4                 12   0  0  0                       2
24   G                  12   0  0  0                       2
P1  U_1(G) > 0: True (12 of 66 configurations have no stabiliser-fixed neighbour)
P2  U_2(G) = 0: True (0 of 600 remembered pairs)
P3  depth monotone under reader refinement: True (0 violations)
under G, configurations with no fixed neighbour, by orbit: {1: 3/3, 3: 6/6, 7: 3/3}, none elsewhere
```

All three held. Two things the table shows that were not predicted:

- **Depth is 1 exactly for the readers of odd order (1 and 3) and 2 for the other 21.** Every
  reader containing an involution has a configuration whose next step it cannot choose
  without remembering where it came from; no reader needs more than one remembered step.
- Under G the 12 configurations that defeat a first-order rule are **not** the interior.
  They are the three most symmetric orbits (stabilisers of order 4 and 8). The interior
  configurations each have a fixed neighbour across the orbit boundary. § 61.1's "no rule on
  the interior" was about rules that stay inside it.

### 62.3 The control: P2 could have failed

```
under G, remembered pairs with a NON-trivial stabiliser: 408 of 600
    stabiliser order 2: between 3 and 9 continuations fixed, of 5 to 13   (384 pairs)
    stabiliser order 4: exactly 1 continuation fixed, of 5, 9 or 13       (24 pairs)
```

Two thirds of the remembered pairs still carry symmetry, and 24 of them are left exactly
one admissible continuation — forced, not chosen. If backtracking were allowed the test
could not fail (prev is always fixed by the pair's stabiliser), which is why continuations
were required to be non-backtracking. The orbit count checks: 192 free + 384 with
stabiliser 2 + 24 with stabiliser 4 gives 8 + 32 + 4 = 44 oriented edge orbits, the number
in `relation-layer-k4-refutation.md`.

### 62.4 Status

| claim | status |
|---|---|
| mark-extended dynamics on the arena is bijective | true by construction; not a finding |
| under G a first-order rule does not exist on the arena | measured — fails at 12 configurations |
| one remembered step suffices for every reader | measured, 26 readers, non-vacuous (408 symmetric pairs) |
| a reader needs the remembered step iff it contains an involution | measured on this witness; not argued |
| depth is monotone in the reader | measured, 0 violations |

In the corpus's own words — "memory is the present constraint that makes the next
continuation non-arbitrary" — this is that sentence with a number on it: the constraint
needed is one step, and it is needed by exactly the readers that can reflect.

Run record: `d7.py` sha256 `916b25fdfe0e7af3…` before the control block was appended; exact,
no randomness, 0.4 s. Scope: K = 2, the witness, cells not involved.

---

## § 63. Paper V built — *The Interior of a Reader* — and what the paper pass itself found

`The_Interior_of_a_Reader.docx` (39 pp.: 24 of paper, 15 of source and transcript). Content is
§§ 57–62. Every number comes from one self-contained script, `verify.py` (standard library,
exact, 5 s, blocks V1–V10), printed in the paper as Appendix B with its transcript as
Appendix C. An independent check in a separate session ran twice; its findings are folded in.

### New, found while writing (all run, all in the transcript)

| finding | value |
|---|---|
| the reader acts on the core as the 24 signed cyclic permutations of three axes (pyritohedral) | True, 24 of 24 |
| H8 = the eight sign changes: 3 mirrors, 3 rotations (the involutions of A4), z = −1 | True |
| orientation is implemented by the leaves: the two ends of a core edge share exactly one leaf, and the head is the end on that leaf's antipodal pair | 12 of 12 |
| T±(σe_i, τe_{i+1}) = (τe_{i+1}, ±στe_{i+2}); clock phase = axis of cur | True |
| on a state: z flips both signs, T−T+⁻¹ flips cur, [T+,T−] flips prev (products right to left) | True |
| rule count = ∏ over orbits of stabiliser-fixed continuations | 26 of 26 readers |
| whole-arena closure at the trivial reader: tetra / octa / witness / icosa | 3 / 4 / 4 / **4** |
| reverse inclusion fails: internal moves / blind cells | 49 / 45 of 100 |
| signed prices span 7 of 22; weights \|dφ\| span 18 = distinct class pairs joined | reproduces § 52 exactly |

### Corrections the independent check forced

- **"Interior" in § 59 was one component only.** Under the full icosahedral group the pairs at
  distance 2 are a second class with 60 internal moves on 30 configurations. It has no cell
  shorter than 5; at L = 5 it is 24 pentagons, two per move, every vertex link one cycle,
  V − E + F = −6, one rational relation — a closed orientable surface of genus 4. So § 59's
  "closes into a sphere at L = d" is true of the **adjacent interior** (the internal moves of
  the pivot graph), not of the interior. The bipyramid has three pentagons, not two.
  (`E-FUSED`: two components reported under one word.)
- **The 22-vector of h was never printed in Paper I.** It lives in
  `relation-layer-k4-refutation.md`. Paper I prints only the circulation −22587 on
  {0,1} → {1,9} → {1,2}; the script now reproduces that number directly.
- Icosahedral arena "closes at 4" is a trivial-reader statement; under the full group the
  invariant depth is lower. The paper now says "closed by L = 4 under every reader".
- Eleven statements had been marked computed without being printed; the script now prints them.

### One thing for Dean to decide

The Paper IV he published is the version **before** § 52: it still has Theorem 8.2 with the
unconditional Laplacian exclusion and Table 10's "subspace 7 of 22". Paper V therefore carries
a short § 13.3, *A correction of scope to Paper IV* (exclusion holds whenever F(0) = 0; 7 is a
parameter count, the weight span is 18). The revised Paper IV built in § 52 exists and could
replace the published record instead.

### Status

| claim | status |
|---|---|
| Paper V statements, Table 1 rows 1–12 | each proved (6 short standard arguments) or computed |
| adjacent interior closes into a sphere at L = d on three Platonic cores | measured |
| icosahedral second component is a genus-4 closed surface at L = 5 | measured; recorded, not pursued |
| D8 (state type under a reversing reader), chromatic floor, depth-1 ⇔ odd order | open, listed in the paper |

---

## § 64. Three reviews of Paper V applied; and "H₂(Q₃) = 11" typed — `q3.py`

### Review items, each checked before applying

| item | check | outcome |
|---|---|---|
| orientation is preserved, not selected | the 12 reversed pairs are the other G-orbit: True | Theorem 6.1(b) and the text after it reworded; "forward" is a convention, the leaf rule marks the head |
| Theorem 7.1(d) should say undirected | — | reworded; two outgoing + two incoming method edges |
| "Cayley complex" convention | one face per relator cycle, not per (vertex, relator) | construction stated explicitly |
| abstract: 24 clock values versus 3 phases | 24 on the arena, 3 on the interior | abstract reworded |
| § 9.3 opening "a reader coarser than A₄" | V₄ ⊂ A₄ passes; the sentence was wrong about its own table | replaced |
| the seam is a boundary: v = ±∂c_△ = ∓∂c_□ | script already computes boundaries | Proposition 11.1(c), § 4.2, Table 9, transcript line reworded |
| multiset comparison is not an identification | — | § 8.1: identification = uniqueness up to scale + Paper I's triangle; multiset is bookkeeping |
| script: V10 relied on a distant reassignment of `hp` | lines 394 → 585, 589 | renamed `FULL`; transcript unchanged apart from the two reworded lines |

No number changed. Paper rebuilt and re-delivered.

### The proposed "next experiment" rests on a number with no address

A pasted proposal builds on "Q₃ leaves 11 independent H₂ classes after the square / triangle /
prism families are admitted". Run:

```
Q3: V=8 E=12 beta1=5; cycles by length {4: 6, 6: 16, 8: 6}
   squares            cells  6  rank 5  H1 open 0  closed 2-chains  1
   hexagons           cells 16  rank 5  H1 open 0  closed 2-chains 11
   octagons           cells  6  rank 5  H1 open 0  closed 2-chains  1
   squares+hexagons   cells 22  rank 5  H1 open 0  closed 2-chains 17
   squares+octagons   cells 12  rank 5  H1 open 0  closed 2-chains  7
   all cycles         cells 28  rank 5  H1 open 0  closed 2-chains 23
A_2(Q3): 28 configurations, 72 moves, cycle rank 45 | L<=4: 90 cells, rank 45, closed 2-chains 45
A_3(Q3): 56 configurations, 180 moves, cycle rank 125 | L<=4: 306 cells, rank 125, closed 2-chains 181
```

- With the families the proposal names, the count is **1** (the cube's own sphere); triangles
  are vacuous on a bipartite graph.
- **11 is reachable**, by one address only: the 16 hexagons as the sole 2-cells, 16 − 5.
  **Correction to the 3 October note**, which said no cycle family gives 16 two-cells: the
  6-cycles are exactly 16. That note's other finding, 11 = P_{C₇}(2), was not re-run here.
- Every entry is cells − β₁ once H₁ is closed. A 2-complex with no 3-cells has
  dim ker ∂₂ = cells − rank: it counts **redundant relations**, not global obstructions.

So the proposal's prediction "H₂(𝒜, F) decreases as F is enriched" is reversed for 2-cells:
1 → 11 → 17 → 23 here, and 1 → 16 → 40 → 56 in Paper V's Table 4. What decreases with the
2-cell vocabulary is H₁ (Paper I's monotonicity). H₂ decreases only when 3-cells are admitted.
Stated both ways: **enriching relations closes loops and opens relations-among-relations.**

| claim | status |
|---|---|
| H₂(Q₃) = 11 after squares / triangles / prisms | **no such address**; squares give 1 |
| 11 = 16 hexagons − β₁ | measured |
| "11 is not reachable on Q₃" (3 Oct) | **retracted** |
| residual H₂ decreases with relation vocabulary | **refuted for 2-cells**, both witnesses |
| the three-step Z₃² / 11-class / C_n programme | not run — step 2 has no object; steps 1 and 3 not defined in anything supplied |

---

## § 65. Continue / turn: the two rules of the full reader, one more step of memory — `methods/turn.py`

Prompt (Dean, 6 Oct): *"x is either this or that. every path is just continue or turn. thats it."*
Run on the witness interior and on the three bare triangle-faced cores. Exact; brute force and a
parity count agree.

**Statement.** Paper V, Table 5: with memory (prev, cur) the full reader *G* admits **no**
equivariant rule, A₄ admits T₊ and T₋. Give the walker one more step, (pp, prev, cur):

```
triples (pp, prev, cur) on forward walks: 24 = 12 states x 2 predecessors
reader G on the triples: fixed-point free True; orbits 1
rules, exact count:  order 1: 4096 -> 16777216 | A4: 2 -> 4 | H8: 0 -> 8 | G: 0 -> 2     (every reader: 2^(24/order))
brute force over all 16777216 rule-books for G: 2 equivariant
they are  CONTINUE: next = pp  and  TURN: next = antipode of pp : True
continue keeps the method, turn changes it: True
cycle types: continue 3^8, turn 6^4, turn.continue^-1 2^12 ; turn^3 = z : True
<continue, turn>: order 24, regular True, commutes with every reader element True; element orders = those of G
cells: 8 triangles (continue^3), 4 hexagons (turn^6), 12 squares ((turn.continue^-1)^2); edges 48
every edge on exactly two cells True; every vertex link one cycle True; Euler characteristic 0; orientable True
all 8190 words of length 1..12: endpoint by walking == endpoint from v[k+3] = (+/-) v[k]: mismatches 0
the 24 triples against the plane group p6 with translations taken mod 2: consistent True, one-to-one True
```

- *G* cannot name a method (z exchanges T₊ and T₋). It can tell whether the method **changed**.
  Its two rules are the constant sequences of that one bit.
- Algebra of a walk: **v[k+3] = ε_k · v[k]**, ε = +1 continue, −1 turn; ε_k = m_k · m_{k−1}
  (turn is the first difference of method). Endpoint = (length mod 3, three turn parities): 24.
- Reversed: "continue" (same method) is the tightest loop, a core face, back in 3. "Turn"
  (change method every step) is the straight line of the cuboctahedron, an equator hexagon =
  Petrie polygon of the core, back in 6.
- Surface: 3.4.6.4 on a torus. It is the plane tiling folded by 2 (p6 / 2L, checked by
  homomorphism). **Recovered, not derived**: the (2,3,6) rotation group and its tiling are classical.

**Three cores, full automorphism group** (regular on triples in each case; 0 rules with two steps, 2 with three):

| core | order of turn (Petrie length h) | cells | χ | 1/3 + 1/h − 1/2 |
|---|---|---|---|---|
| tetrahedron | 4 | 8 △ + 6 □ + 12 □ | 2 (sphere) | + |
| octahedron | 6 | 8 △ + 4 ⬡ + 12 □ per component (2 components) | 0 (torus) | 0 |
| icosahedron | 10 | 40 △ + 12 decagons + 60 □ | −8 (orientable, genus 5) | − |

χ = N(1/3 + 1/h − 1/2) is a count, so the sign is decided by h against 6. The witness is the flat case.

| claim | status |
|---|---|
| G admits exactly two rules at three steps, continue and turn | computed, two ways (2²⁴ brute force; parity count) |
| every reader admits 2^(24/order) rules at three steps | computed, all 26 |
| ⟨continue, turn⟩ ≅ G, regular, centralises the reader | computed (order, regularity, commutation, order profile) |
| witness method surface = 3.4.6.4 plane tiling mod 2 | computed |
| sphere / plane / hyperbolic by h = 4, 6, 10 | computed on three cores; the formula is a count |
| larger folds (p6 / nL, n > 2) come from a graph with a reader | **not known**; the algebra has them, no witness built |

---

## § 66. Two reviews of § 65 run; the next fold, built two ways — `methods/fold.py`, `fold2.py`, `fold3.py`, `fold4.py`

Two pasted AI reviews of § 65 (6 Oct). Checkable points were run, not accepted or rejected by argument.

**(1) "Three vertices suffice, but is a literal third vertex the smallest encoding?"** — run. Memory = a
set the reader acts on, with a reader-respecting map to the 12 states and a reader-respecting update.

```
memory of  1..8 states (subgroups of order 24,12,8,6,4,3): cannot even project onto the interior
memory of 12 states (order-2 subgroup) x4: does not project            ; x3 (the mirrors): projects, deterministic updates 0
memory of 24 states (trivial subgroup): projects, deterministic updates 48 -> 2 distinct sets of walks
the reader element fixing a state: 1, order 2, exchanges that state's two continuations: True
```
Any memory point's stabiliser must fix a continuation, and the only non-trivial stabiliser of a state swaps
them, so every orbit of a working memory is the regular one. **24 is minimal; the extra memory is one bit**,
and it need not be a vertex (pp, last method, either predecessor label: the same G-set).

**(2) "Endpoint = phase mod 3 + turn parity"** — **refuted as stated.**
```
8190 words grouped by (length mod 3, total turns mod 2): 6 groups, endpoints per group [4]
grouped by (length mod 3, turns mod 2 at each of the three positions): 24 groups, endpoints per group [1]
single total parity decides: current method relative to the starting one
```

**(3) "Curvature from turn length is empirical over three cores."** It is a count. For any closed
triangulated core: V = N triples, E = 2N, F = N/3 + N/2 + (turn loops), so
**χ(method surface) = (turn loops) − N/6**. Checked on 15 cores (Platonic, bipyramids k = 3,5,6,7,9, capped
octahedron/icosahedra with loops of mixed length 10/36/62, K₇ torus, K₆ projective plane, torus grids).
Flat ⇔ mean turn-loop length 6. **Recovered:** turn loops are Petrie polygons; the surface sits over the
Petrie dual of the dual (Wilson's operators, 1979). Witness: Petrie dual of the cube = 4 hexagons on a torus,
{6,3}₍₂,₀₎. Quotient by continue: 8 points, 12 links, cube graph, 4 hexagonal faces (computed).

**(4) The next fold, method-first.** Core M_n: three classes of n points, faces = one point per class with
labels summing to 0 or 1 (mod n). M₂ = octahedron. n = 2..7 (relation checked to n = 9):

| n | core V,E,F | core χ | triangles vs faces | order-keeping reader | rules 2 steps → 3 | turn | method surface |
|---|---|---|---|---|---|---|---|
| 2 | 6,12,8 | 2 | 8 / 8 | 24 | 0 → 2 | 6 | torus, 24 triples, = p6/2L |
| 3 | 9,27,18 | 0 | 27 / 18 | 54 | 0 → 2 | 6 | torus, 54, = p6/3L |
| 4 | 12,48,32 | −4 | 64 / 32 | 96 | 0 → 2 | 6 | torus, 96, = p6/4L |
| 5–7 | 3n, 3n², 2n² | n(3−n) | n³ / 2n² | 6n² | 0 → 2 | 6 | torus, 6n², = p6/nL |

- One extra relation: **(turn⁴·continue⁻¹)ⁿ = 1** (order n, computed n = 2..9).
- Algebra: v[k+3] = v[k] + (turn ? ±1 : 0) mod n; the sign flips with each turn (method bit). Closed form
  checked against walking, 0 mismatches. n = 2 gives § 65's three parities.
- Method-naming reader (order 3n²): exactly T₀, T₁ at two steps; T₁T₀⁻¹ has order n; cells 2n² triangles +
  3n 2n-gons; χ = n(3−n) = the core's own. **Naming the method is curved with the core; continue/turn is
  flat for every n.**
- **Recovered:** the regular triangular embedding of K_{n,n,n} from two cyclic Latin squares
  (Grannell–Griggs–Knor); matched by description only.

**(5) The next fold, witness-first.** X_n = K_{n,n,n} + one leaf per core point t, joined to t and to the
whole next class. **X₂ is the Paper V witness (isomorphism computed).**

```
n=2  reader 24      states 12, 2 continuations   rules: two steps 0, three steps 2 (next = pp ; next = the one other point)
n=3  reader 648     states 27, 3 continuations   rules: two steps 0, three steps 1 (next = pp)
n=4  reader 41472   states 48, 4 continuations   rules: two steps 0, three steps 1 (next = pp)
sum rules the reader cannot tell apart: 1, 12, 432 = (n!)^3/(2n^2); reader elements keeping one: 24, 54, 96 = 6n^2
six-step memory: pinned targets = points already in the window, plus the last unvisited point when exactly one is left
```
- Reader = S_n ≀ C₃, order 3(n!)³. For n ≥ 3 "the other point" is not one point: **turn is not a rule.**
- Principle (Prop 9.1 on this reader): a rule can send the walker only to a point its memory pins — visited,
  or the only one left. At n = 2 the antipode is the only one left.
- Turn needs a choice of face structure: 1 at n = 2 (invisible because forced), 12 at n = 3, 432 at n = 4.
  With one fixed the reader has order 6n² and face triples pin continue, turn, and n − 2 moves that leave the faces.

| claim | status |
|---|---|
| minimal memory for a G-rule is 24 states, one extra bit | proved (stabiliser) + enumerated over 26 transitive memories |
| endpoint needs three parities, not one | computed; the review's single parity refuted |
| χ = turn loops − N/6 | identity; checked on 15 cores |
| flat fold at every n on M_n, = p6/nL | computed n = 2..7; relation to n = 9 |
| scaled witness X_n admits only "continue" at three steps, n = 3, 4 | computed |
| number of face structures (n!)³/(2n²) | computed n = 2, 3, 4 |
| a graph whose own reader selects one face structure at n ≥ 3 | **not built** |
| residue / clock of Paper V on any n ≥ 3 object | **not run** |

---

## § 67. The three-vertex state as a device; and the n = 3 witness with its own face choice — `methods/logic.py`, `w3.py`, `w3b.py`, `w3c.py`

Prompted by Dean (6 Oct): *"that 3 vertex state....a transistor?"* / *"no, its a device that allows the physical
creation of a chain of logic"*, and two pasted AI texts (cascadability; a review of § 66 naming the n = 3 test).

**(1) The device** (`logic.py`; bits fixed by one face, phase = cell of the oldest vertex):
```
24 triples <-> (cell of the oldest vertex) x (three bits): one-to-one
continue: (a,b,c) -> (b,c,a) ; turn: (a,b,c) -> (b,c,not a)      on all 24
bits alone: held at continue loops [1,1,3,3] (ring counter); held at turn [2,6] (twisted ring / Johnson counter)
every state takes either instruction and gives a state: in-degree 2, out-degree 2, one component
all 24 compositions of continue and turn = rotate the bits, then flip a fixed set: NOT only; no copy, no AND
```
A 3-stage shift register closed in a ring with one controlled inverter: **a register stage, not a gate.** The
chain-making property (closure, no dead end, nothing lost) holds at every reader.

**(2) What the chain can compute, by reader** (next = oldest XOR g; rule-books with three steps of memory):

| reader | rule-books | reversible | reversible controls | group generated |
|---|---|---|---|---|
| G (24) | 2 | 2 | 0, 1 | 24 |
| A₄ (12) | 4 | 2 | 0, 1 | 24 |
| H₈ (8) | 8 | 8 | 0, 1 per phase (control sees the clock only) | 1 536 |
| ⟨z⟩×C₃ (6) | 16 | 4 | 0, 1, xor | 576 |
| V₄ (4) | 64 | 8 | 0, 1 | 1 536 |
| z, rotation, mirror (4) | 64 | 16 | 0, 1, xor | 12 288 |
| two mirrors (4) | 64 | 32 | 0, 1, copy | 98 304 |
| C₃ (3) | 256 | 16 | 0, 1, copy, xor, **AND** | 120 960 = 3·8! |
| one rotation (2) | 4 096 | 64 | 0, 1, copy, xor | 21 233 664 |
| ⟨z⟩ (2) | 4 096 | 64 | 0, 1, xor | 21 233 664 |
| one mirror (2) | 4 096 | 256 | 0, 1, copy, xor, **AND** | 169 869 312 |
| trivial | 2²⁴ | 4 096 | all | 196 644 962 304 000 = 3·(8!)³ |

- Reversible ⇔ the control does not read the oldest bit (brute force agrees wherever 2^k ≤ 4096); count 2^(reader orbits on states).
- C₃: its 256 rule-books are exactly the 256 truth tables newest = h(a,b,c); the 16 reversible ones (invertible
  3-stage shift registers; attribution to Golomb's criterion from memory, not re-checked this session) generate every
  rearrangement of the 8 bit patterns. Continue + turn + copy alone: 4 032 = 3·|AGL(3,2)| (affine only); + AND: 120 960.
- **AND (Toffoli: target oldest, controls prev and cur) appears only at C₃, a single mirror, or no symmetry.**

**(3) n = 3 with the face relation intrinsic.** Pipeline = Paper V's (reader, classes, interior, rules, residue, clock).
Validation: X''₂ = the witness; orbit-coordinate residue reproduces 7529 / 22587 / 24 values / kernel H₈ exactly.

| object | reader | turn a rule (3 steps)? | trivial H¹ (squares) | invariant harmonic | clock |
|---|---|---|---|---|---|
| X₂ = witness | 24 | yes (continue, turn) | 1 | 1 | order 3, phases 4/4/4 |
| plain X₃ | 648 | no (continue only) | 1 | 1 | order 3, phases 9/9/9, same 22587 / 7529 |
| plain X₄ | 41 472 | no | — | 1 | order 3, phases 16/16/16, same numbers |
| X₃ + vertex on each non-face triangle | 54 | yes (continue, turn, off-face) | 0 | 0 | none |
| X₃ + vertex on each face | 54 | (yes) | 0 | 0 | none |
| X₂ + vertex on each face | 24 | — | 0 | 0 | none |
| X₃ + spider on each non-face triangle | 54 | yes (continue, turn, off-face) | 19 | 1 | **order 1**: a forward step carries a full period |

- Plain X_n: 8 classes and 22 invariant coordinates for every n; the residue vector is the same; **the residue and clock
  scale unchanged**. The turn does not (wreath reader).
- One marker vertex on one face of the witness (one K₄): H¹ 1 → 0. One spider instead (no K₄): H¹ 1 → 3.
- Two-step memory at n = 3 with faces marked: exactly one rule, onto the non-face (the third method).
- Mechanism (argued, consistent with all runs, not proved): the clock counts forward steps mod 3 around triangles; a
  marker fills triangles (K₄ squares), a spider adds returns through one core edge, so the period drops to one step.

**Caveat on published Paper V, Theorem 8.3.** With the move-weighted orthogonality (natural edge inner product) in
place of orbit coordinates, the same class gives forward −3, period 9; the clock then takes **9 values, not 24**, and
does not separate the 24 classes of H₈. Order 3, kernel H₈ and part (d) hold in both. **(a) and the level-set clause
of (c) are properties of Paper I's representative, not of the class.**

| claim | status |
|---|---|
| triple = 3-stage ring shift register with a controlled inverter | computed on all 24 |
| continue/turn alone: NOT only | computed (24 compositions) |
| AND only at C₃ / one mirror / trivial | computed, 26 readers |
| residue + clock scale unchanged in plain X_n | computed n = 2, 3, 4 |
| at n = 3, turn and clock not both obtained | **three constructions**; not a theorem |
| Paper V Thm 8.3(a), level sets in (c): representative-dependent | computed (two conventions) |

---

## § 68. The other thread (claude.ai chat 863bbbd1, 17 Sep – 7 Oct) absorbed; Paper V's clock is its reader-relative class mod 3 — `methods/bridge.py`, `mech.py`, `mech2.py`

Uploaded by Dean (8 Oct) without comment: the export of the "Ceiling and the Descent" / register–adder / reactive-ledger
thread and its eight scripts. All eight were run unchanged (`/home/claude/other/out_*.txt`); every number that thread
reported reproduces (Section 5 table, refinement, Q/F₂ torsion, reader-order check, reader-only classes, C8
certificate, prism interface design, register vs adder C(n,2)+(n−1), reactive fusion/backlog/skew).

**Output the export cut off** (`lookahead_latency_subscribers.py`):
- adder relation presentations, squares declared: ripple {1} b₁ = 0/0 (Q/F₂); lookahead {2} 1/1; {3} 2/2;
  **{2,3} 0 over Q, 1 over F₂** (a 2-torsion class: lookahead alone closes rationally, not mod 2); ripple+look 0/0. n = 4, 5, 6.
- per-digit latency (events after the digit's own position): low→high 0; high→low mean 1.344 (n=6), 1.502 (n=8), max n−1;
  even/odd mean 0.667 / 1.125, max 2 / 3.
- subscribers: minimal ledger root-only 3/4/4, root + first adder 4/6/6, every node 4/8/8 (3-op chain, 4-op chain,
  4-op tree): observing internal emissions undoes fusion.

**Bridge (proved + checked).** For an invariant 1-cocycle z exact in the full (connected) arena, z = df and
f∘g − f = c(g) is constant, c ∈ Hom(G, F_p), and c kills every configuration stabiliser; conversely any such c gives
z = df with f(gx) = f(x) + c(g); z is invariantly exact iff c = 0. Hence
**reader-only H¹ over F_p ≅ {characters G → F_p vanishing on all configuration stabilisers}** — no 2-cells enter.
Checked against that thread's own engine: C8 half-turn 1 (p=2), prism 1, K₃,₃ 1, Paper V witness 0 (p=2), **1 (p=3)**.
The engine on the witness (K = 2, Abrams cells): F₃ H¹ reader 2 / object 1 / **reader-only 1**; F₂ H¹ 0, H² reader-only 1;
char 0 H¹ reader 2 / object 2.
**Paper V's clock is this class:** the character c: G = C₂×A₄ → C₃ with kernel H₈ (restricted to A₄: kernel V₄ = A₄ ∩ H₈; wording corrected in § 71), the mod-3 twin of the C8 certificate's
"sum along x → g(x)". It does not depend on the relation predicate, so the refinement critique does not touch it.

**§ 67 re-read through that thread's corrections.**

| object | turn a rule? | invariant rational H¹ (all 4-cycles / disjoint squares) | clock: reader-only H¹ over F₃ |
|---|---|---|---|
| witness X₂ | yes | 1 / 2 | 1 |
| plain X₃ | no | 1 / 2 | 1 |
| X₃ + vertex per non-face | yes | 0 / 2 | 0 |
| X₃ + vertex per face | yes | — | 0 |
| X₃ + spider per non-face | yes | 1 / 2 | 0 |

- "Markers destroy the residue" (§ 67) holds only under the all-4-cycles predicate. Under disjoint-support squares
  (Abrams; refinement-stable per that thread) every object has 2 invariant rational classes. **Paper I/V's uniqueness
  of h is a property of the all-4-cycles predicate.**
- The clock (predicate-free) survives in plain X₃ and dies in every face-marked X₃. **Mechanism, computed:** in plain
  X₃ no configuration is fixed by a class-rotating element (432 such elements, 0 fixed configurations); in each marked
  object some pair of triangle markers is turned in place by one class rotation (9, 18, 9 such configurations), and the
  clock is the class-rotation character.
- Every class-rotating element of the face group fixes 3 faces, 3 non-faces, or 1 non-face. **16 of its 54 subgroups
  (orders 3, 6, 9, 18) still rotate the classes while fixing no face**: a graph whose reader is one of these, with faces
  marked chirally, is the remaining candidate for turn + clock at n = 3. Not built.

| claim | status |
|---|---|
| all eight uploaded scripts reproduce their reported numbers | run |
| reader-only H¹ over F_p = stabiliser-killing characters | proved; checked on 4 cases against the other engine |
| Paper V clock = reader-only F₃ class of the witness | computed with the other thread's engine |
| § 67 "residue destroyed" | **predicate-dependent** (all-4-cycles only) |
| at n = 3, turn and clock not together in the three constructions | **holds predicate-free** |

---

## § 69. The n = 3 witness: turn, clock and one interior together — centreless face marks (`methods/chiral.py`, `delta.py`, `delta_n.py`)

Pasted review (8 Oct) asked for the chiral construction with five checks: (1) the graph's actual automorphism group,
(2) faces kept intrinsically, (3) turn equivariant on the retained state, (4) class-rotation character nonzero,
(5) that character zero on every stabiliser of the full two-token arena, gadget and mixed configurations included.

**Chiral spiders** (order-18 sub-reader; legs of length 1, 2, 3 by corner role role(f,a) = class(a) − k(f),
k(hf) = k(f) + rot(h)): all five pass. Aut = the intended order-18 group; 0 of 4005 configurations fixed by a class
rotation; reader-only H¹ over F₃ = 1, over F₂ = 0. **But** no candidate sub-reader has order divisible by 27, so the
27 core edges split into reader classes 9 + 18 and only 45 of 81 forward moves are internal.

**Centreless marks** (each face gets three new vertices in a triangle, each joined to one corner only):

```
n=2 (witness, no marks): reader 24  | rules 2 (continue, turn)                    | clock yes | core edges one class, 24/24 moves internal | phases 4/4/4
n=3: 72 vertices, reader 54 = 6n^2  | rules 3 (face: continue, turn, off-face)    | clock yes | one class, 81/81 internal                  | phases 9/9/9
n=4: 120 vertices, reader 96 = 6n^2 | rules 16 (face: continue, turn, 2 off-face)  | clock yes | one class, 192/192 internal                | phases 16/16/16
all n: faces kept; turn commutes on every face triple; no vertex fixed by a class rotation;
       F({u,v}) = 2(cl u + cl v) mod 3 satisfies F(gx) = F(x) + rot(g) on every configuration; every forward move advances F by 1
centred marks, n = 3, same checks: 36 (vertex, class rotation) fixings, clock 0
```

- **Retraction:** "at n = 3 you get turn or clock, not both" (§ 67, kept in § 68) is false. It was a property of
  marks with a centre: a vertex at a face's centre is fixed by that face's own rotation, and the clock is the
  class-rotation character.
- **Criterion (two tokens):** the clock survives iff no class rotation fixes a pair of token positions. It holds
  whenever no class rotation fixes a vertex (a swapped pair would need g² to fix a vertex, and g² rotates classes).
  Core points and leaves always move under a class rotation; a mark vertex tied to one corner moves with it.
- **General n (argued, checked at 2, 3, 4):** reader = face group G_n (order 6n², computed equal at n = 3, 4);
  translations make it transitive on the 3n² core edges; faces kept ⇒ turn equivariant; marks follow corners ⇒ clock.
  The clock is predicate-free (§ 68), so no relation choice enters. The rational residue h of Paper V § 8.1 was not
  recomputed on these objects.
- n = 2 needs no marks because every triangle of K_{2,2,2} is a face.

| claim | status |
|---|---|
| chiral construction passes all five checks | computed (n = 3) |
| chiral construction cannot keep one interior class at n = 3 | computed (no candidate order divisible by 27) |
| centreless marks: turn + clock + one interior class | computed n = 3, 4 (n = 2 is the witness); argued for all n |
| § 67 / § 68 "turn or clock at n = 3" | **retracted** (centred-mark artefact) |

---

## § 70. Price and residue on the centreless n = 3 graph — `methods/price_res.py`

Pasted review (8 Oct) asked for Paper V's price and residue on X^Δ₃, kept separate, with the inner product stated.
Harmonic representatives: orthogonal to invariant exact cochains **in orbit coordinates** (Paper I/V convention).
Control: the same code at n = 2 reproduces Paper V (24 zero-price moves; h = 7529 / 22587; order-3 clock).

**Price** (zero signed price under every invariant potential = moves inside a reader class):
```
n=3: 135 of 11970 moves:  81 inside the core-edge class (27 configurations, every forward move)
                          54 inside a mark-mark class (54 configurations): two tokens on one face's mark, 3 moves per face, 18 faces
```
**Residue:**
```
n=2  all 4-cycles: closed 8, exact 7, harmonic 1 -> h: forward 7529, period 22587, every triangle one period, every 4-cycle 0, clock order 3
     disjoint squares: closed 9, exact 7, harmonic 2 -> basis classes period 1, character trivial (h is one member of the 2-dim space)
n=3  all 4-cycles: closed 57, exact 56, harmonic 1 -> forward t = 125727604912032, period 3t, all 5040 triangles one period,
     all 44343 4-cycles 0, character order 3 (values t, 2t on class rotations)
     disjoint squares: closed 59, exact 56, harmonic 3 -> basis classes period 1, character trivial
```
- Under all arena 4-cycles **the old residue scales unchanged in form**: unique invariant class, one period per triangle,
  a third of a period per forward core move, order-3 clock. (The integer t is a normalisation artefact.)
- Under disjoint squares the invariant space is 2 (n=2) and 3 (n=3) dimensional; generic members carry no clock; the
  all-4-cycles class is the member that does. The predicate-free clock (§ 68) exists regardless.
- Paper V's interior at n = 3 = the core-edge class **plus** 18 small loops on the marks.

**All-n argument for X^Δ_n (n ≥ 3), the review's four obligations:** degrees core 5n+1, leaf n+1, mark 3 (distinct) ⇒
roles intrinsic; mark vertices' components are the mark triangles ⇒ faces kept; leaves fix the cyclic class order ⇒
Aut ⊆ G_n; G_n ⊆ Aut by construction; |G_n| = 6n² (half the flag-regular 12n², computed n = 2..7 in § 66);
translations transitive on the 3n² core edges. Argued; computed Aut = 6n² at n = 3, 4.

---

## § 71. Three reviews of § 70: two wording corrections run, the reader proved for all n, the residue at n = 4 — `methods/generic.py`, `res4.py`

**Correction 1 (§ 68).** "A₄ → C₃ (kernel H₈)" mixed two groups. Run: |A₄ ∩ H₈| = 4, the Klein subgroup V₄. Correct form:
c: G = C₂×A₄ → C₃, ker c = H₈; c|A₄: A₄ → C₃, ker = V₄. (§ 68 text amended in place.)

**Correction 2 (§ 70).** "The all-4-cycles class is the member [of the disjoint-square space] that carries the clock;
generic members carry no clock" was too singular and untested. Run: the all-4-cycles class lies in the span
(n = 2 coefficients 7901/882, −7999/882 on the harmonic basis). Primitive integer combinations of the basis with
coefficients in [−3, 3]: n = 2, 2 of 32 carry the order-3 clock; n = 3, 6 of 290. So clock-carrying classes are a
minority of those sampled, and they are not only the all-4-cycles line.

**The reader of X^Δ_n for every n ≥ 3 (proof).**
- Lemma. A face automorphism of the sum-rule triangulation of K_{n,n,n} fixing each class has the form
  (x, y, z) ↦ (λx + a, λy + b, λz + c), λ = ±1, with a+b+c ≡ 0 if λ = 1 and ≡ 1 if λ = −1. Proof: faces sharing an edge lie in
  different families and the dual graph is connected, so families are kept or swapped globally. Kept: α(x)+β(y)+γ(−x−y) ≡ 0
  gives γ(u+v) = γ(u)+γ(v)+k, so all three are affine with a common unit slope λ; the family-1 equation forces λ ≡ 1. Swapped:
  the same with constants exchanged forces λ ≡ −1. Hence 2n² class-fixing automorphisms; with the 3 class rotations, |G_n| = 6n².
  Brute force over all label permutations: n = 2: 8, n = 3: 18 (9 + 9), n = 4: 32 (16 + 16), all of the stated form.
- Aut(X^Δ_n) = G_n: degrees 5n+1, n+1, 3 separate core, leaves, marks; the components of the mark subgraph are the mark
  triangles, so faces are kept; leaves keep the cyclic class order; leaves and marks are determined by the core.
- Translations are transitive on the 3n² core edges; the clock law F(gx) = F(x) + rot(g) excludes fixed configurations.
  Reader, turn, clock and one core-edge class: **proved for all n ≥ 3** (n = 2 is the witness, computed).

**Residue at n = 4** (120 vertices, reader 96, 7140 configurations, 35 400 moves, 206 082 arena 4-cycles):
```
all arena 4-cycles: closed 92, exact 91, harmonic 1 (mod two primes; exact rational dimension 1)
   normalised by its period: every forward core move -1/3, all 16 992 triangles one period, all 206 082 4-cycles 0, character values 0, 1/3, 2/3
disjoint squares: harmonic 3
```
Residue pattern under all 4-cycles: computed n = 2, 3, 4, identical after normalisation. Disjoint-square dimension 2, 3, 3.
**All-n residue: not proved.**

---

## § 72. The residue is the object's, not the reader's — `methods/full_h1.py`

Review of § 71 (8 Oct) split the all-n residue problem into existence and one-dimensionality, and asked what distinguishes
the clock-carrying classes. Run: first cohomology of the **full** two-token arena of X^Δ_n (no reader), 2-cells declared two ways.

```
                 all arena 4-cycles                 disjoint-support squares
n=2 (witness)    H1 = 1 over Q, F2, F3              19 over Q and F3, 20 over F2
n=3              H1 = 1 over Q, F2, F3              100 over Q and F3, 101 over F2
n=4              H1 = 1 over Q, F2, F3              (not run)
```
- With every 4-cycle declared, the square-filled arena has **one loop direction in total**, with no 2- or 3-torsion. The
  reader-invariant class of §§ 70–71 is that class; its uniqueness needs no reader argument (the reader acts on a 1-dim
  space by ±1, and computed +1). Every arena triangle generates it rationally (each carries ±1 period).
- So the all-n residue problem is now a statement about the object: **H¹(square-filled arena of X^Δ_n; Q) = 1**. Not proved.
- Disjoint squares: a mod-2 excess of exactly one, the same kind the other thread found on refined K₃,₃ (Q 4, F₂ 5).
- **What distinguishes clock-carrying classes** (proved, one line): with γ_g the closed walk x → gx → g²x → x for a class
  rotation g, invariance gives ∮_γ h = 3 ∫_{x→gx} h, so h carries the order-3 clock iff ∮_γ h is not a multiple of three
  periods of h. For the all-4-cycles class, ∮_γ h is one period.

---

## § 73. The uploaded torsion certificates, checked; the Z/2 is the classical non-planar exchange class — `methods/verify_cert.py`, `zh.py`

Uploaded (8 Oct): another AI's integral Smith-normal-form run on the disjoint-square complexes, with certificates
(`torsion_certificates.json`), plus four reviews and a pasted synthesis ("can the transition itself be the complete coupling mechanism?").

**Certificates, re-checked on the graphs stored in the file:**
```
n=2: graph isomorphic to the Paper V witness; z = 6 legal moves, closed, exchanges the two labelled tokens;
     B = 22 disjoint-support squares, coefficients +1 x11, -1 x11; boundary(B) = 2z exactly;
     detector eta: 0 on all 291 disjoint squares, eta(z) = 1
n=3: graph isomorphic to our X^Delta_3; z = 6 moves (the Y-exchange at one core point through three arms), exchanges the tokens;
     B = 18 squares, +1 x9, -1 x9; boundary(B) = 2z exactly; eta 0 on all 13 239 disjoint squares, eta(z) = 1
```
So [z] ≠ 0, 2[z] = 0; since eta(z) = 1 and eta kills 2-divisible classes, the 2-primary summand is exactly Z/2.
H₁ (disjoint squares) = Z¹⁹ ⊕ Z/2 (n = 2), Z¹⁰⁰ ⊕ Z/2 (n = 3), as the upload reports.

**What it is.** At n = 3, B is exactly the 18 disjoint squares of UD₂(K₃,₃) on the six core points of two classes. Computed:
UD₂(K₃,₃) has V 15, E 36, F 18, χ = −3, every move on exactly two squares, H₁ rank 4 over Q and 5 over F₂, H₂ 0 over Q and
1 over F₂: a closed non-orientable surface; B is that surface with signs, z its orientation-reversing loop.
**Recovered, not new:** Ko–Park, *Characteristics of graph braid groups* (arXiv 1101.2648): a graph is planar iff H₁ of its
braid groups is torsion-free; their Example 2.1 gives H₁(B₂K₃,₃) ≅ Z⁴ ⊕ Z₂, matching the count above. The witness is non-planar
(Kuratowski subgraph: subdivided K₃,₃, 10 vertices, 13 edges); its certificate lives on 7 vertices.
Physical reading in the literature (HKRS, cited in the other thread): on non-planar graphs the exchange phase is locked to ±1.

**Separation from the residue:** ∮_z h = 0 at n = 2 and n = 3 (h = the all-4-cycles class). The exchange sign and the clock are
different survivors: exchange parity lives in the configuration-space complex (disjoint squares) and dies when all 4-cycles are declared.

**Scope corrections accepted (wording, no new run needed):**
- projection (prev, cur) → cur forgets one bit only at n = 2; at n it has n predecessors (log₂ n bits).
- "the object's residue" names the predicate: the square-filled arena (all 4-cycles declared). b₁ = 1 is one abelian loop
  direction, not π₁ = Z.
- rotation-loop test (§ 72): γ_g = α · gα · g²α with translated legs and g of order 3 (the pure class rotation ρ; every
  family-preserving class rotation ρτ has order 3 since a+b+c ≡ 0).
- normalised residue comparisons quoted as |h(e_fwd)|/P = 1/3, |∮△ h|/P = 1, ∮□ h = 0; signs depend on orientation.
- retained state ≠ minimal memory (the ledger's continuation quotient is the minimal one).

**On the synthesis.** Closure F_u: S → S (computed, §§ 65, 67) makes the transition a complete *execution* mechanism.
It does not fix physical coupling strength or cost: signed prices are dφ for a chosen potential, weights are a further
constitutive choice (Paper V § 13.3: prices span 7 of 22 invariant directions, weights 18). Not a law yet.

---

## § 74. The n = 4 exchange upload, recomputed; the free part is the graph's own cycle space — `methods/n4.py`, `surface.py`, `graph4.py`, `planar_contrast.py`, `inv_graph.py`

Uploaded (8 Oct): another AI's n = 4 integral run and K₃,₃ cup-product data (`n4_exchange_cup_certificate.json`), and a review of § 73.

**Recomputed independently** (own build of X^Δ_n, spanning-tree presentation, sparse unit-pivot elimination in exact integers,
dense Smith form on the remainder):
```
       graph V / E / beta1   arena configs / moves / disjoint squares   generators  unit pivots  left   H1 (disjoint squares)
n=2      12 /  30 /  19         66 /    300 /    291                       235          215        20    Z^19  + Z/2
n=3      72 / 171 / 100       2556 /  11970 /  13239                      9415         9314       101    Z^100 + Z/2
n=4     120 / 300 / 181       7140 /  35400 /  41922                     28261        28079       182    Z^181 + Z/2
```
Every uploaded n = 4 number reproduced. The mapped walk {0,4}→{4,5}→{0,5}→{5,6}→{0,6}→{4,6}→{0,4} is legal and reduces exactly to
the torsion generator (the surviving relations span exactly twice it); a mod-2 detector with η(z) = 1 vanishes on all 41 922 squares; the
18 mapped squares are disjoint-support squares with ∂B = 2z. Clock values 2,1,2,1,2,1,2 reproduced.
One reading corrected: "zero net clock shift around the exchange" holds for every closed walk, since F is a function on
configurations; it says nothing about z. The clock's content is in rotation loops x → gx (§ 72).

**What 181 is: the graph's cycle rank.** 181 = 300 − 120 + 1 = β₁(X^Δ₄); likewise 19 and 100. Total-track map (an arena loop ↦ the
1-cycle the two tokens trace together in the graph): on the surviving generators it kills the surviving relation, has rank β₁ and
all invariant factors 1. So, integrally, at n = 2, 3, 4:

    H₁(two tokens, disjoint squares) = H₁(graph) ⊕ Z/2·[exchange]

— the free part carried isomorphically by where the tokens went, the kernel exactly ⟨z⟩ (precisely: the exact sequence
0 → Z/2·z → H₁ → H₁(graph) → 0; the trace map is an isomorphism over Q, not integrally — wording corrected in § 75).
- Every Y-exchange — every hub (core, leaf, mark), every three arms, both orientations; 432 / 10 260 / 32 352 of them — traces
  nothing and has η = 1: all are the same element z. One exchange for the whole graph.
- Reader level agrees: dim H¹(graph; Q)^Aut = 2 / 3 / 3 at n = 2 / 3 / 4, the invariant arena values recorded earlier.
- X^Δ_n is 3-connected (no cut vertex, no 2-cut) and non-planar at n = 2, 3, 4. At n = 2 the core octahedron alone is planar; the
  leaves make the witness non-planar.
- Contrast run, 3-connected graphs: planar K₄, octahedron, cube, dodecahedron → Z^(β₁+1) (the exchange is a free direction);
  non-planar K₅, K₃,₃, Petersen, K₃,₄, Möbius–Kantor → Z^β₁ ⊕ Z/2.
- **Recovered, not new:** Ko–Park (arXiv 1101.2648): Cor. 3.6 (torsion is 2-torsion; planar ⇒ none), Lemma 3.12 (biconnected ⇒
  H₁(BₙΓ) ≅ H₁(B₂Γ) for any number of tokens), Ex. 2.1 (K₃,₃: Z⁴ ⊕ Z₂), Ex. 3.9 (B₄K₅: Z⁶ ⊕ Z₂). Their general formula (Thm 3.16)
  I could not retrieve (the 3-connected case was later retrieved from HKRS Thm 4, § 75); every case run fits "3-connected: Z^β₁ ⊕ Z/2 if non-planar, Z^(β₁+1) if planar". Physical reading
  (HKRS): planar → the exchange phase is free; non-planar → ±1.

**Consequences.**
1. The review's "free directions support other phases", made exact: the free directions are one-token loops around graph cycles;
   the exchange is the only two-token class.
2. ∮_z h = 0 (§ 73) is forced: z traces nothing and h is a pulled-back graph class (3). Every one-token observable vanishes on z.
3. **The residue question reduces to the graph.** Every arena 4-cycle is a commuting square (traces nothing — exactly the disjoint
   squares), a spectator square or a rotation square (both trace one graph 4-cycle): Part I's families, with the n = 2 counts
   291 / 528 / 264 of § 1; every graph 4-cycle arises (n = 2, 3, 4). So over Q, given the trace sequence (an isomorphism over Q),
   H¹(square-filled arena) ≅ H¹(graph + its 4-cycles).
   Graph level, dim = 1 for n = 2 … 8 (upper bound: rank mod 2³¹−1; lower bound: the explicit cocycle f — +1 on forward core
   edges, L(i,x)→c(i,x) = 3, L(i,x)→c(i+1,y) = 1, t_a→a = 0, t_a→t_b = f(a→b); f = 0 on every graph 4-cycle, ±3 on every triangle).
   All-n argument at graph level: (a) a cycle of length ≥ 5 in K_{n,n,n} has a chord, so cycles split into triangles and
   4-cycles, and two triangles differing in one vertex differ by a 4-cycle — all core triangles agree modulo 4-cycles; (b) a path
   through a leaf, c(i+1,y)–L–c(i+1,y′) or c(i,x)–L–c(i+1,y), is a core path modulo one 4-cycle; (c) each mark edge t_x–t_y is the
   path t_x–x–y–t_y modulo its prism square, after which the spokes cancel in pairs (a cycle inside one mark triangle becomes its
   face triangle). Hence H₁(graph + 4-cycles; Q) = Q·(triangle), nonzero by f.
   Status of § 72's open item: computed n ≤ 4; all n follows from this argument plus the trace sequence at every n
   (Ko–Park's formula; verified here only for n ≤ 4).
4. f ≡ d(cl) mod 3. The residue (over Q a nonzero class, period 3 on triangles) and the clock (over F₃ exact with potential −F,
   F = 2(cl u + cl v); its failure to be reader-invariant is the clock character) are one integral cocycle read at two coefficient rings.

**The K₃,₃ surface (uploaded cup data), checked.** Vertex links: the 6 configurations with both tokens on one side have a hexagon
link, the 9 with the tokens adjacent a square link → closed surface; χ = −3, non-orientable, genus 5. Uploaded subdivision
(33 / 108 / 72) = the centre-coned squares, every link a cycle; H¹(F₂) = 37 − 32 = 5; the five uploaded cocycles are cocycles and
independent; Q recomputed equals the upload (symmetric, rank 5, non-alternating); z evaluations (0,0,1,1,1) = diag Q. w₁ computed
separately from local orientations (each vertex's link given a direction): (1,1,1,1,1) in their basis, w₁(z) = 1, and α∪α = w₁∪α
on the basis (Wu). So z is Poincaré dual to w₁: on that surface the exchange is the orientation character.

**Review of § 73, accepted.** (i) The certificate gives order exactly 2 and non-2-divisibility, so ⟨z⟩ is a Z/2 direct summand;
"the only torsion" needs the full reduction (now recomputed, n ≤ 4). (ii) The residue already lies in the disjoint-square H¹ (a
pulled-back graph class); declaring all 4-cycles isolates it and kills z. (iii) The exchange sign is one sector (consequence 1).

Open, unchanged: the cost law — which constitutive assumption selects movement weights from prices.

---

## § 75. n = 5, 6; a loop's class is (trace, swap); the classification retrieved; more tokens; the cost-law proposal — `methods/n56.py`, `kpoint.py`

Uploaded (9 Oct): another AI's n = 5, 6 runs with sections and naturality checks (`trace_parity_splitting_checks.json`,
`n5_n6_kernel_boundary_checks.json`), three reviews of § 74, a draft "§ 75 — closing the two open problems", and a note on
preservation contracts.

**Recomputed independently** (pipeline of § 74):
```
       graph V / E / beta1 = 12n^2-3n+1   arena configs / moves / disjoint squares   generators  unit pivots  left   H1
n=5     180 / 465 / 286                    16 110 /  82 770 / 102 330                66 661      66 374       287   Z^286 + Z/2
n=6     252 / 666 / 415                    31 626 / 166 500 / 212 049               134 875     134 459       416   Z^415 + Z/2
```
Upload reproduced, unit-pivot counts included. Its kernel walks (hub 0, arms in class 1) and our Y-exchange (hub 0, arms in
class 2) reduce to the same element; every surviving relation is a multiple of 2z. No vertex cut of size ≤ 2 and non-planar at
n = 2 … 6.

**A loop's class is (trace, swap).** ε = exchange parity: on a move {a,v} → {b,v} it is 1 when the vertex order of the two tokens
flips; around a closed walk it is the parity of the permutation of two labelled tokens. Checked at n = 2 … 6: ε vanishes on every
disjoint square; ε(z) = 1, J(z) = 0; for every fundamental graph cycle, one token going round it while the other waits off it is a
legal loop with trace = that cycle and ε = 0 (19 / 100 / 181 / 286 / 415). With the computed H₁:
    0 → Z/2·z → H₁(two tokens) → H₁(graph) → 0   exact,   and   (J, ε): H₁(two tokens) → H₁(graph) ⊕ Z/2   an isomorphism.
The canonical section: one token round the cycle, the other waiting anywhere off it (all such lifts have the same (J, ε)). It is
reader-equivariant because J and ε are intrinsic (the upload's generator checks, 724 at n = 4 and 1 144 at n = 5, agree).
Corollary: every Y-exchange traces nothing and swaps, so it is z — the 32 352 of § 74 are forced.
Correction accepted: the trace map is an isomorphism over Q (and modulo torsion), not integrally; § 74 amended in place.
Uploaded sections: those avoiding mark vertices check against our labelling (all at n = 2; 88/100, 165/181, 266/286 at n = 3, 4, 5);
the rest number mark vertices differently (their rebuild) and were not checked; ours cover every fundamental cycle.

**The classification, retrieved.** Harrison–Keating–Robbins–Sawicki, *n-particle quantum statistics on graphs*, arXiv:1304.5781v1
(21 Apr 2013), DOI 10.1007/s00220-014-2091-0; checked 9 Oct 2026.
- Thm 4 (§ 4.2): "For a 3-connected simple graph, H₁(D₂(Γ)) = Z^β₁(Γ) ⊕ A, where A = Z₂ for non-planar graphs and A = Z for
  planar graphs."
- D_n(Γ) (§ 3, eq. 5): Γⁿ minus every cell whose closure meets the diagonal, modulo Sₙ — for n = 2 exactly our arena with
  disjoint-support squares. Thm 1 (Abrams): D_n ↪ C_n is a homotopy equivalence when paths between vertices of valence ≠ 2 have
  ≥ n − 1 edges and closed paths ≥ n + 1 edges.
- Thm 5 (§ 5): for 2-connected Γ, H₁(D_n(Γ)) = H₁(D₂(Γ)).
Application. Γ_n is simple and non-planar (K₃,₃ ⊂ core for n ≥ 3; computed at n = 2), and 3-connected for every n: after deleting
≤ 2 vertices the core K_{n,n,n} (2n-connected) stays connected, each leaf keeps one of its n + 1 core neighbours, and each mark
vertex t_a keeps one of three internally disjoint routes t_a–a, t_a–t_b–b, t_a–t_c–c. Hence, known after translation (HKRS Thm 4):
    H₁(D₂Γ_n; Z) ≅ Z^(12n² − 3n + 1) ⊕ Z/2   for every n ≥ 3.
J is onto for every n (fundamental cycles of a BFS tree are short, so a waiting vertex exists), so the trace sequence and the
(J, ε) splitting hold for every n. The homology-level splitting is our formal corollary; HKRS's count (β₁ free phases, one
statistics phase ±1 when non-planar) is its U(1)-character form. Ko–Park Thm 3.16 / Lemma 3.15, cited by the upload, I still could
not retrieve; HKRS Thm 4 is the source used.

**§ 72's open item, closed for every n.** H¹(square-filled arena of Γ_n; Q) = 1, spanned by the pullback of the integral cocycle f
of § 74 (f ≡ d(cl) mod 3 — the integral representative the review asked for). Chain: (i) the trace sequence makes J ⊗ Q an
isomorphism (all n, above); (ii) every arena 4-cycle traces nothing — and is then a disjoint square — or one graph 4-cycle, and every
graph 4-cycle is traced by a spectator square. Proof of (ii): a closed 4-move walk traces a closed chain of ≤ 4 traversals; if
nonzero it is a 4-cycle traversed once (a triangle would leave one traversal unmatched; no multiple edges); if zero, two edges are
each crossed out and back — the same edge, or two edges sharing a vertex, cannot be crossed that way by two non-colliding tokens
without repeating a configuration, and two disjoint edges force the commuting square; a waiting vertex off any 4-cycle exists.
(iii) H₁(graph + its 4-cycles; Q) = Q (graph argument of § 74). Computed checks: arena level n ≤ 4, graph level n ≤ 8.

**More tokens** (k tokens; edges subdivided into k − 1 pieces, Abrams):
```
                 k=2           k=3 (into 2)   k=4 (into 3)   k=3 unsubdivided
K4 (planar)      Z^4           Z^4            Z^4            Z^3
cube (planar)    Z^6           Z^6            -              Z^6
K3,3             Z^4 + Z/2     Z^4 + Z/2      Z^4 + Z/2      Z^5
K5               Z^6 + Z/2     Z^6 + Z/2      Z^6 + Z/2      Z^6 + Z/2
witness X_2      Z^19 + Z/2    Z^19 + Z/2     -              Z^19 + Z/2
```
Independent of token count once subdivided (HKRS Thm 5); K₅ at k = 4 reproduces Ko–Park Ex. 3.9 (Z⁶ ⊕ Z₂). Unsubdivided k = 3 can
be wrong (K₃,₃: Z⁵; K₄: Z³): past two tokens the raw vertex-token complex is not the configuration space. In every subdivided
non-planar case ε vanishes on squares, the exchange (other tokens parked) traces nothing and swaps, and parked lifts cover every
fundamental cycle: (trace, swap) is the whole of H₁ at k = 2, 3, 4.

**Other uploaded items.** The reduced Świątkowski check (∂₁∂₂ = 0 on 276 075 generators) holds for any correctly coded complex,
and its ranks were inferred from ours: no independent evidence. The K₃ homomorphism example is right: a non-injective vertex map
collides tokens, so naturality covers automorphisms and embeddings only.

**The cost-law proposal (local detailed balance).** Right as far as it goes: with k(u→v) = κ_uv exp(−β p_uv / 2), prices fix only
the ratio k(u→v)/k(v→u); the mobility κ (symmetric, one number per move orbit, 22 at n = 2) and β are untouched. It names the
missing data; it does not select it. "Closing" overstates.
What it leaves out, in the ledger's numbers (recovered: Kolmogorov's reversibility criterion; Schnakenberg's network theory). Put
a = log(k(u→v)/k(v→u)), an invariant antisymmetric cochain (22-dim at n = 2). Detailed balance holds iff a is exact: the 7 price
directions. The other 15 (Part I's ceiling D) are the possible invariant non-equilibrium drives (cycle affinities). Declaring a cell
family means zero affinity around those cycles: commuting squares (each token's rates independent of where the other sits) leave 2
— the invariant graph drives, via the trace; all 4-cycles leave 1 — the residue, a forward bias round the classes 0 → 1 → 2 → 0;
all families leave 0. The exchange has zero affinity under any drive that respects independence (2z = ∂B, so ∮_z a = ½ ∮_∂B a = 0):
real rates cannot drive it; only a phase sees it (Hom(Z/2, U(1)) = ±1).
So: prices = equilibrium landscape; residue = the one drive the full 4-cycle rule admits; exchange = phase only; κ and β = measured
inputs. The cost law stays open, now with its free data named.

**Preservation contracts (note).** Agreed. (J, ε) is a worked instance: complete at the homology level; it forgets walk order (π₁
is non-abelian) and every rate.

---

## § 76. Paper 1 of a new series: *The Incomplete Universe* — assembled from §§ 1–75 and the earlier paper families; claim audit

Asked by Dean (9 Oct): pull everything together into a first paper, *The Incomplete Universe*, laying out what has been
found and where it goes, optimistic in tone. Delivered as `The_Incomplete_Universe.docx` (20 pp.; 16 keyframes, 9 tables,
3 figures, 32 references); markdown copy `claude/the-incomplete-universe.md`. Build: `iu/build` (`s0`–`s6.js`, `lib.js`,
`figs.py`); checks: `iu/keyframes_check.py`.

**Re-run for the paper.** Shapes 0, 1, 5, 83; the BBP integral (antiderivative derivative = integrand; radial logs 0 at both
ends; angular part = π); (1/√2)⁸ = 1/16, (1 + i)⁸ = 16; weights (4, −2, −1, −1) sum 0; hex digits at addresses 0–11 =
243F6A8885A3. New: y = √2 t turns the integrand into 16(y − 1)/((y² − 2)(y² − 2y + 2)), poles ±√2 and 1 ± i, ∫₀¹ = π (SymPy, exact).

**Audit against the sources, before delivery.** Every number in the paper was checked against its record. Two scope fixes:
1. Abstract had "the swap is the orientation character of a genus-5 surface" attached to the whole family. The surface
   statement is about K₃,₃ (§ 74); the witness's two-token complex is not a surface. Scoped to K₃,₃.
2. § 9.5 had the SHA-256 cold-basin collapse factor as "exactly 1.00". The source measures 1.00 on a finite sample in the
   schedule-free model and says it is not proved to be exactly 1. Restated as measured, with the message schedule named as
   the next experiment.
Checked and unchanged: Table 2 counts from closed forms (C(V,2); E(V − 2); C(E,2) − Σ C(deg,2) = 291 at n = 2, 13 239 at n = 3);
β₁ = 12n² − 3n + 1 from V = 6n² + 6n, E = 18n² + 3n; 220 (b, m, g) triples (carry-capacity ledger); e to n = 2000 and
47 958 / 5 583 670 bits (addressability doc); 9 = 3² at b = 3, L = 2 (What a Cut v1.4); 15 orbit generators attained, relation
gap / D(2) only over ℤ (§ 48); C₆, C₈ bipartite arenas (omitted-cycle doc); device table (§ 67); rule-books 3 / 16 and
72 / 120 vertices (§ 69); residue for all n (§ 75); [13] measured state- versus transformation-keyframe cost.

Kept out of the paper by design: H = π/9 and the 0.35 material.

---

## § 77. Location, resolution, continuation — `methods/location.py`

Prompted by Dean (9 Oct) with two AI exchanges about Paper 1 and a pasted text: *"nothing at this point can fail, only
bank into transformation"*; *"it's just about location — 2+3=8 is not in the correct location"*; *"always compiling:
2+3 is already 5, but continuation says you can't lock it up, or there would be only a single measurement."*

**Location is the class under every continuation** (recovered: Nerode 1958, already the mechanism of the adder papers).
```
terms 1110 (sums of 1-3 digits), contexts 121, locations 28 = distinct values 28
'2+3' and '5' one location (28 members); '2+3' vs '8' separated by 121 of 121 contexts
every valid rewrite keeps its location (1100 rewrites); 2+3 in context X+3 sits with 8, then X+2 with 10
```
An equation claims that two terms share a location, and it is true exactly when they do, so "location versus truth"
is not an opposition (one review's correction, accepted). The string "2+3=8" is an event in the string system; no
valid step moves 2+3 into 8's location.

**A retained organization is a claim about location, and it can fail** (witness walk; observable = current vertex):
```
Nerode classes of histories (continuations to length 6): 24, all reachable
candidate (length mod 3, total turns mod 2): 6 classes x 4 states -> fails at once: CC vs TT
  + the current vertex: 12 classes x 2 -> TTC and CCC agree on all of it, stand on (2,+); after C: (0,-) vs (0,+)
Moore refinement from the observable alone: 6 -> 12 -> 24, stable; from the failed candidate: 12 -> 24
stable organization = the 24 triples (one state per class)
```
Every failure is a specific continuation, and that continuation is the split. "It failed" and "it banked into
transformation" are one act read twice — a verdict on the old placement and the address of the new one — and the
banking terminates at the unique minimal sufficient organization (Moore 1956; Myhill–Nerode), here Keyframe 8's triple.
Round 1 adds the oldest vertex (12 classes = (pp, cur)); round 2 adds the middle one.

**Resolution is not exhaustion = C1.** All 24 states have two continuations and reach all 24. Exhaustion's computed
instance is Keyframe 2's K = n row: the discrete model collapses to one configuration while UConf_n(S¹) ≃ S¹ keeps its
loop — the lock is the discretization's, not the space's.

**Dean's chain on an LSB-first serial adder:**
```
2+3: 0010+0011 = 0101   carries into places 0..3 [0,0,1,0]   dropped carry -> 0001 = 1   wrong in 1 of 4 places
5+3: 0101+0011 = 1000   carries [0,1,1,1]                     dropped carry -> 0110 = 6   wrong in 3 of 4
8+2: 1000+0010 = 1010   carries [0,0,0,0]                     dropped carry -> 1010 = 10  wrong in 0 of 4
```
Each digit is written once and never revised; one carried bit is the whole retained organization between places.
Prediction before the run: the dropped-carry reading of 5+3 wrong in all four places. Measured: three (place 0 has no
incoming carry).

| claim | status |
|---|---|
| location = class under every continuation; an equation is a co-location claim | recovered (Nerode); checked on bounded arithmetic |
| a retained organization fails exactly when a continuation separates two of its histories | definition; two witnesses exhibited |
| refinement by failures stops at the unique minimal sufficient organization | recovered (Moore, Myhill–Nerode); run on the walk |
| resolution is not exhaustion | C1; checked on the 24 states; exhaustion instance = Keyframe 2's K = n row |
| "nothing can fail" | true of the ground (a failure is itself a continuation); false of placements — which is what keeps the programme testable |

---

## § 78. Paper 1 v1.1: the address is the object

Dean (9 Oct), on the § 77 wording and the proposed § 7.6: *"are you sure that is what we want? The address IS the
object. The variable IS THE VALUE, there is no gap. All of algebra is just trying to find what is missing, because there
can't be any gaps."*

**Correction against my own wording.** § 77 and my reply said a location is "where something sits" across continuations,
and a pasted § 7.6 draft said "a retained organization assigns histories to states". Both put an object behind its
address. Myhill–Nerode says the reverse: the states of the minimal machine are constructed as the classes; nothing stands
behind a class. Not adopted; Dean's form adopted.

**Recovered, and run for the paper** (`iu/keyframes_check.py`, blocks 4–5):
```
in Q[x]/(x^2 - 2): x*x reduces to 2      (Kronecker: the root is the variable read modulo its polynomial)
in Q[x]/(x^2 + 1): x*x reduces to -1 ;  in Q[x]/(x^2 - x - 1): x*x reduces to x + 1
sqrt 2 read from its cut {q : q < 0 or q^2 < 2}, rational comparisons only: 1.414213562373095   (Dedekind)
```
Every extension of number that looked like filling a gap is a class construction: differences (ℤ), quotients (ℚ), cuts (ℝ),
the variable modulo its polynomial (algebraic numbers). The new number is the address.

**What changed in the paper (v1.1, 22 pp.):**
- New § 2.2 *The address is the object* with **Keyframe 0** (Myhill–Nerode [28], Moore [35]; the walk 6 → 12 → 24, the
  arithmetic 28 classes from § 77); old §§ 2.2–2.3 renumbered 2.3–2.4.
- Abstract: the principle stated; "the one gap that remains … a measurable gap of known width" → "what remains to be read …
  the topology reads the antisymmetric part of the rates and names the rest … a measurement, not a search".
- § 6 retitled *Price, drive, and the rate law*; § 6.3 *The rate law and its unknowns*: the rates are variables whose values
  every realization already has; the topology leaves open only which realization the world uses.
- § 5.6: "what is missing is exactly the lift" → one cocycle, two addresses (a potential over ℤ/d, a circulation over ℤ;
  the winding the clock does not carry is the residue itself).
- § 3.4: the digit at address n is a function of n alone. § 7.3: each row of Table 6 is an address. § 8: no gap between an
  object and its address. § 9.4: for a fixed contract the question is answered by Keyframe 0; the open case is a system
  whose retained organization moves its own contract.
- Tables 7–9: Keyframe 0 placed under standing aim 3; status row 0; correction row "an unknown is a gap to be filled; an
  object occupies an address" → "the address is the object".
- References [33] Dedekind 1872, [34] Kronecker 1887 (Werke II, 211–240), [35] Moore 1956.

Kept: "the gap is the reader's" (Keyframe 3, § 1.2, § 8) — consistent with the principle, and the project's own wording.

---

## § 79. Paper 1 v1.2: the track record folded in; baseball on the field and in the computer — `methods/realize.py`

Dean (9 Oct): "yes, lets fix that paper and make sure we show our proof and the …" (message cut off), then ten pasted AI
texts with "a lot of 'baseball in the computer' talk vs 'baseball in the field', so we have to tie that together".

**New runs** (`realize.py`, exact, no randomness):
```
FIELD walks on the octahedral core (continue = pp, turn = antipode of pp), built from adjacency; COMPUTER 3-stage ring register
+ controlled inverter + mod-3 phase counter, built from bits.  q = (axis of pp, three signs)
q one-to-one and onto 24 states; q(F_a(x)) = T_a(q(x)) on 48 of 48 pairs; 2,046 words of length 1..10 agree from every state;
computer reports the walker's vertex on all 24.  Register alone (phase dropped): square 48/48, 3-to-1, cannot report position
(bits (1,1,1) at vertices (2,-) and (1,-)).
hex -> base c, first digit: unresolved cells after k digits = number of non-terminating boundaries d/c, constant in k;
worst case bounded exactly for c = 2, 4, 8, 16; bases 6, 10, 12, 14 partially aligned (4, 8, 8, 12 unresolved cells).
```
**Re-run for the paper** (all exit 0): n4.py (3 s), n56.py (12 s), surface.py (1 s), graph4.py and --arena (14 s), kpoint.py (4 s),
planar_contrast.py (<1 s), location.py (1 s), realize.py (<1 s), keyframes_check.py (1 s); Python 3.11.15, NetworkX 3.6.1,
SymPy 1.14.0. Every number in Tables 2–4 and the K3,3 surface reproduced. Outputs in `iu/runs/`.

**What changed (v1.2, 31 pp., keyframes 0–17 with 4a–4c, 6a, 14a, 16a, 17; Tables 1–10; refs [1]–[40]):**
- §2.1 constraint chain rung by rung from *Named Laws* (with its cautions; Lawvere reading of C1). §2.2 tied to the
  *Named Laws* address (root, class, coordinate, reader) and its three moves.
- §3.3–3.4 new: K4a (reader is a functional; three zeros; no field zero on the witness, §§9–20, 34), K4b (bin 0; 115 + 120;
  export at second order, §§35–49), K4c (interface width 6; Kalman, §§24–29), §31/§33 consequences. §3.6 K6a.
- §5.7 K14a (*The Ceiling and the Descent*: ε_harm = dim Z − dim span; cubes; prism (0,1), bull (1,0); persistence; curvature
  is (ω, 𝒦); Law 3 constraint). §6.3 K16a (§§50–54). §7.5 rewritten: baseball on the field and in the computer, the square
  q∘F_a = T_a∘q, K17. §9.1 local → global (*Universal Admissibility*; the delayed-ring transient). §1.3 weak/strong collision.
- Review fixes accepted: "most symmetric reader is blindest" scoped to the invariant readout; Table 5 caption — zero square
  affinity is the antisymmetric half of independence, full independence needs the mobilities to factor; statistics scoped to
  one-dimensional (abelian) phases; "relaxes and stops" → relaxes to detailed balance, no net current.
- Appendix A: proofs of every statement marked proved (A.1–A.16). Appendix B: the nine scripts with SHA-256 prefixes,
  times and what they printed. Table 9 +5 corrections (§22, §42, §52, §57.9, delayed ring).
- § 76's inventory (20 pp., 16 keyframes, 32 refs) is v1.0; § 78 is v1.1; this is v1.2.

Not included, and why: the normalized transfer-spectrum thread (Johnson levels, σ(T₂) = {√(5/3), √(8/9), √(1/3)}, level-3
joint spectator dependence) — reported in a pasted review of a transcript not available here; not re-run.

## § 80. Paper 1 v2.0: *Distinction That Must Continue* — the start, and the mathematics so far — `methods/start.py`, `methods/math_core.py`, `methods/corpus_rerun.py`

Dean (16:15, Oct 9): the title "The Incomplete Universe" was too final; start from C0 and C1 and show that it is the only
initial state possible; more important, show the math for where we are, using GPT's synthesis of the past 40 papers (11
attachments, then a revised *Interaction-First Unified Architecture* paper at 17:17). Reviews are input to choose from.

**Retitled** *Distinction That Must Continue: Why C0/C1 Is the Only Possible Start, and the Mathematics So Far* — NEXUS Working
Paper 1, v2.0 (supersedes *The Incomplete Universe* v1.2). 46 pp., DOCX `iu/build/Distinction_That_Must_Continue.docx`.

**The start (`start.py`, exact, exhaustive).** Prohibitions *cannot hold still* (no continuation leaves a state where it was) and
*cannot escape* (strongly connected), on finitely many states, in five readings (unlabelled counts n = 1..4):
```
A  strict relation, strongly connected         0  1   5    83     (labelled 0, 1, 18, 1606; A035512 except n = 1)
A0 A without cannot-escape                      0  1   7   126
B  map, no fixed point, one orbit               0  1   1     1
C  bijection, no fixed point (whole at rest)    0  1   1     2
D  weak: some continuation other than itself,   0  3  30  1168    (the swap with optional rests at n = 2)
   rests allowed, strongly connected
```
Of the 16 relations on two states exactly one survives (the swap); C0 without C1 and C1 without C0 both fail. Every two-block
reader of every structure obeying both prohibitions (A: 1+18+1606 labelled; D: 4+144+25,696; cycles to 6) sees both crossings;
only the swap is read with no apparent rest; an n-cycle has an exact two-block reader iff n even (checked to 8). Without
*cannot escape* the crossing property fails: two separate swaps split between them show no crossing (C); {0>1,1>0,2>0} with
block {2} shows one (A0). Swap: s(x) != x, s(X) = X, s∘s = id. Diagonal d(a) = s(f(a)(a)) outside the image of every
f: A -> 2^A for |A| = 1,2,3 (2, 16, 512 maps); with the identity it falls inside for 2, 12, 296. Proofs A.17.
OEIS A035512's n = 1 term is a state with no continuation (no loops in the census) — corrects the v1.2 wording "a loop".
Three readings of C1: no terminal state (admits one state resting forever), not its own only continuation (reading D), no fixed
point (unique start; Lawvere).

**The mathematics so far (`math_core.py`).** Evaluation Φ(x) = (O(U_a(x,c))), X/~ = im Φ (interaction-first, partial
encounters; the quotient runs when legal moves are state-independent or observed). On the 24-state walk: vertex / sign / axis
readers give 24 (6→12→24) / 8 (2→4→8, = phase-dropped register) / 3 addresses; 24 = 8 × 3. z (all signs) and g (axis
rotation) commute with C and T; Reynolds ranks 12, 8 = trace averages; z-odd field invisible under all linear words ≤ 6, its
square visible, magnitudes recovered, sign not. Bins from multiplicities (types 1±,2±,3±; dims 1,1,2,2,3,3): A 115+120,
disj 105+111, rot3 10+10 (= §41), deficiency (2,0,1,0,2,3) = 19 = 10+9. Transfer: 48/48 one-step, all words ≤ 6, addresses
carried; register by 'where' refines 6→12→24. Periodic transport on Z/60: dim(T_a ∩ T_b) = gcd for all 144 divisor pairs;
(3,5): 7 transported of 15, residual 8. Hex extraction (69,888 strings of 2–4 digits): 4,368 leading-zero echoes, trailing
removal = floor/16, 3 echoes (all-zero). Boundary × reader on the walk (addresses; reachability by boundary alone):
```
moves  reach | vertex sign axis at-v0
CT       24  |   24    8    3    6
C         3  |   24    8    3    4
T         6  |   24    8    3    6
none      1  |    6    2    3    2
```
— corrects the first draft's "what is allowed and what is read are separate axes": they are separate inputs; the address
depends on both.

**Corpus re-runs (`corpus_rerun.py`).** sec^m(2π/m) integer > 1 only at m = 6 (64), 8 (16) for m ≤ 200 at 80 digits; exact
(1+i√3)^6 = 64, (1+i)^8 = 16; Galois proof (A.20): degree of 2cos(2π/m) ≤ 2 forces m ∈ {1..6, 8, 10, 12}. Carry S = W + 2^32 Q
(division with remainder; 4-bit fibres 2,…,2,1). SHA-256: implementation = hashlib on 2 messages; 49/49 windows of 16
schedule words return W[0..15]; 64/64 rounds invert with the word; withheld word leaves 7 of 8 words fixed (proof A.21).

**Independent check** (separate pass, had not seen the sections written): every number matched; fixes taken — weak reading D
named as losing uniqueness; A035512 n = 1 wording; D's definition includes strong connectivity; selection clause "weakening an
operative constraint" (cannot-escape is free at n = 2); Constraint 2 vs C2 and "natural numbers"; corpus count (39 of the 40
reviewed papers are the programme's; RHA excluded); K0d recast (table above); K1a scoped to strongly connected readings;
"proved" only for n = 1, 2; "contains both crossings" not "is the swap"; E_int(15) = R15 − 9 nets new directions against
collisions — the quotient decides; carry and SHA results marked proved, checked on one block; Schur step in A.18.

Scripts (SHA-256 prefixes): start.py ad1c99ddcbcca61d, math_core.py 2e73103b443c0144, corpus_rerun.py be1b9d054fbec9e4; the
nine v1.2 scripts unchanged and re-run (outputs identical up to timing lines). Outputs in `iu/runs_v2/`.
Corpus results not re-run (reported in Table 11): F_R(15) = 9 and E_int(15) open; (−64,12); dim K(16,24) = 3; (64,42) freed and
unoccupied; 16 − t^8 coefficient map rank 7; stencil (4,−2,−1,−1) needs more than the two angles; weights, Navier–Stokes DNS,
n − 1 analogy, oscillator/BBP and UATS proposals.

## § 81. The swap where it reappears; the ambient module and the deficiency from fixed points — `methods/swap.py`, `methods/lefschetz.py`

**The walk onto the start.** ⟨continue, turn⟩ acts regularly on the 24 walk states (order 24). Exactly one homomorphism of
the walk onto the two-state swap exists: continue → rest, turn → swap, blocks 12 + 12; the reader is the product of the three
signs; the central inversion z also acts as the swap. On the register the same reader is a⊕b⊕c, and turn = continue followed
by NOT on the fed-back bit (24/24).

**Ambient module from fixed points (Hopf trace formula, recovered).** For every g in Aut(witness) (C2 × A4, 24 elements),
tr(g | H1(arena)) = 1 − #fixed configurations + #fixed moves (signed). Values: e 235; −I: 6 fixed configurations, 0 moves → −5;
three 180° rotations: 10 configurations, signed moves 4 → −5; three −I·(180°): 30, 72 → 43; sixteen elements of order 3 or 6:
nothing fixed → 1. Decomposed over 1±, 2±, 3±: **m(A) = (15, 4, 14, 4, 24, 36)** — the recorded vector, with no linear
algebra (0.07 s). Bins under z: (235 ∓ 5)/2 = 115 + 120; 120 − 115 = 6 − 1, and the 6 z-fixed configurations are the antipodal
pairs, at each of which z exchanges the two tokens (labelled arena: 132 states, connected double cover, deck = label swap;
z = label swap on exactly those 12 labelled states).

**Deficiency from fixed points.** For the 2-complex of a vocabulary F: χ_D − χ_H2 = χ_A − χ_C2 = 1 − fix0 + fix1 − fix2 (H2 =
relations among the cells). Ranks re-derived mod 1,000,003, all five match the ledger (216, 20, 174, 168, 150); m(W_disj),
m(W_rot3) match. Arena 4-cycles: 1083 = 291 zero-trace + 528 parked + 264 both-move.
```
            cells rank H2 | m(D) = A − W        | Lefschetz part (fixed points) | m(H2)
disj         291  216  75 | (2,0,1,0,2,3)       | (0,−4,−1,−4,−7,−7)             | (2,4,2,4,9,10)
rot3          20   20   0 | (13,3,13,4,22,33)   | (13,3,13,4,22,33)              | 0
spec3        180  174   6 | (5,0,4,0,5,11)      | (5,−1,4,−1,4,11)               | (0,1,0,1,1,0)
spec4        528  168 360 | (7,0,6,0,4,12)      | (3,−26,2,−26,−52,−22)          | (4,26,4,26,56,34)
rot4         264  150 114 | (8,1,7,1,7,13)      | (7,−6,6,−6,−12,2)              | (1,7,1,7,19,11)
disj+rot3    311  235  76 | 0                   | (−2,−5,−2,−4,−9,−10)           | (2,5,2,4,9,10)
```
Independent cells (rot3): the deficiency is the fixed-point count. Closing vocabulary (disj+rot3): the relations among relations
are. In general the count is missing-here minus redundant-at-the-next-order, a lower bound for each channel-wise: m(D) ≥ max(L, 0),
m(H2) ≥ max(−L, 0); for spec3 the floor misses one copy of 3+ (three dimensions at the trivial reader; at a reader H, dim (3+)^H) — corrected § 82.

## § 82. Review of the GPT pass on § 81; separating missing from redundant by counting; the family — `methods/scale.py`

**Checked from GPT's material.** Its fixed-cell CSV (24 symmetries × fixed configurations, signed moves, cycle trace, and the
five cell traces) agrees with `lefschetz.py --per-element` on all 24 rows and all 8 columns. Its group table (24 words, orders
1/7/8/8, φ = parity of the flip mask) matches the walk group; z = T³ (turn three times is central inversion). Character table and
m(A) = (15, 4, 14, 4, 24, 36) agree. Family counts for n ≥ 3 confirmed symbolically and against the n4/n56 tables:
V = 6n² + 6n, E = 18n² + 3n, configurations 18n⁴ + 36n³ + 15n² − 3n, moves 108n⁴ + 126n³ − 18n² − 6n,
dim A_n = 90n⁴ + 90n³ − 33n² − 3n + 1 (134,875 at n = 6, = n56's generator count), commuting squares
162n⁴ + 15n³ − (63n² + 3n)/2, triangles n³ + 5n² (n³ + 3n² = 20 at the witness).

**Corrections taken.** (i) Mine: the spectator-triangle floor misses one *copy* of 3+, not one dimension (§ 81 line fixed).
(ii) Mine: the z-odd bin (120) is 1− ⊕ 2− ⊕ 3− isotypic (4·1 + 4·2 + 36·3); the swap of the start is the 1− character
ε = det = product of the three signs, four copies in A — not the whole odd bin. The Hopf count 120 − 115 = 6 − 1 stands.
(iii) GPT's: walk and complex share character theory (ε and its projector), not fixed-point counting of walk states (regular
character selects nothing) — GPT corrected itself; agreed.

**New: the two sides separate by counting for commuting squares.** The trace map J is a G-equivariant rational isomorphism
D_disj = H1(arena/commuting squares) → H1(graph) (Keyframe 12), so χ_D = 1 − #fixed vertices + #fixed edges (signed) on the
GRAPH. Witness: graph character values {19, 5, 1, −1}; m(H1(graph)) = (2, 0, 1, 0, 2, 3) = m(D_disj); then
m(H2_disj) = m(D) − Lefschetz = (2, 4, 2, 4, 9, 10) = the rank computation. Both sides from counts, channel by channel.

**New: the witness's closure does not survive scaling.** D(disj + rot3) = H1(graph with its triangles filled; Q):
```
n    V    E  b1(graph) triangles rank  b1(graph+tri)  b2(graph+tri)
2   12   30     19        20      19        0              1
3   72  171    100        72      64       36              8
4  120  300    181       144     117       64             27
5  180  465    286       250     186      100             64
6  252  666    415       396     271      144            125
```
For n ≥ 3 the deficiency is 4n² — two holes per face, the annulus between each face triangle and its centreless mark triangle —
and the new dependencies are (n − 1)³, the 2-spheres of the triangle complex of K_{n,n,n} (join of three n-point sets); at the
witness that is the single extra dependency, 76 − 75. Closed forms (n ≥ 3):
dim D_disj = 12n² − 3n + 1, dim H2_disj = 72n⁴ − 75n³ + 27n²/2 − 3n/2 (3,924 at n = 3);
dim D_{disj+rot3} = 4n², dim H2_{disj+rot3} = 72n⁴ − 74n³ + 21n²/2 + 3n/2 − 1; difference of the H2's = (n − 1)³ exactly.
Open: per-channel versions need the characters of G_n (order 6n²) and their fixed points, which may split by divisibility of n.

## § 83. The family's symmetry is Eisenstein; every channel at every n; the exchange is orientation; what the triangles leave — `methods/gn.py`, `gn_chars.py`, `gn_fast.py`, `gn_fitfast.py`, `gn_global.py`, `gn_orbits.py`, `eisenstein.py`, `exchange.py`

**Checked from GPT's material.** All 516 rows of its scaled-character CSV (n = 3..6) reproduced by own code: F0, signed F1,
signed F2, fixed mark faces, χ_D_disj, χ_D_tri, χ_H2. χ_H2 was computed directly as the trace on ker ∂2 (RREF mod 2³¹ − 1),
not from a formula; GPT's closed forms (∏(N_i − 1) for k = 0, #Fix(g³) − 1 otherwise; 2F_face / −F_face) agree with the
direct traces on every element. G_n is all of Aut(Γ_n) for n = 3..6 (leaves pin the cyclic class order, marks pin the 2n²
faces; face-preserving class-preserving relabellings counted by brute force: exactly 2n²). K₃,₃ certificate: 18/18 genuine
commuting squares, signed sum = 2z with z a 6-move exchange; Smith diagonal (1¹⁷, 2), H1 = Z⁴ ⊕ Z/2. The Schur-index-one
argument is sound (in each case the nonidentity stabilizer elements of P_E, P_F lie outside the inertia group, so the
multiplicities are d/|H|); rational block counts 7/8/6/13 reproduced. Walk projector = the ε-isotypic projector of the
regular action (§ 81), accepted. Not checkable: GPT's 3,366-move η (sandbox file) — replaced by a canonical detector below.
Correction to GPT (and to my own first guess): the extension does split, for every n = 2..12 — every element over the
generator of C6 has order 6.

**The symmetry is Eisenstein.** N (sum-zero translations) ≅ Z[ω]/n; the quotient C6 is μ6, the units of Z[ω], acting by
multiplication — class rotation = ω (v ↦ Rv, R² + R + 1 = 0), slope = −1; checked against conjugation for n = 2..12. With the
splitting, G_n ≅ (Z[ω]/n) ⋊ μ6, the unit-affine group of the Eisenstein ring mod n. Channels = μ6-orbits on Z[ω]/n:
```
orbit                                   complex irreducibles          name
0                                       6 linear                      1+  1-  2+ (w,w^2)  2- (w,w^2)
2-torsion  Z[w]/2 = F4  (n even; 2 inert)   2 of degree 3             3a 3b
(1-w)-torsion (3 | n; 3 ramified)       3 of degree 2                 2c (pair) 2r
free orbits                             (n^2 - 1 - 2[3|n] - 3[2|n])/6 of degree 6
   on the three lines (Z_n . mu6)        floor((n-1)/2) of them       6L
   doubles (b in 2Z[w], n even)          ((n/2)^2 - 1 - 2[3|n] - 3[4|n])/6    6Ld, 6gd
```
Totals 10, 10, 10, 16, 14, 18 for n = 3..8; orthonormal; Σd² = |G|.
**n = 2 is the witness.** Γ_2 is the 12-vertex graph and G_2 = C2 × A4; its six rational types are orbit 0 (1±, 2±) and the
orbit F4^× (3±). The family code at n = 2 returns m(A) = (15,4,14,4,24,36), m(D_disj) = (2,0,1,0,2,3), m(H2_disj) =
(2,4,2,4,9,10), m(H2_disj+rot3) = (2,5,2,4,9,10) — the § 81 table. At n = 2 the slope is ε, the product of the three signs:
the swap of § 81 is the slope character of the whole family; at n ≥ 3 it exchanges the two face families t = 0 ↔ 1.

**Deficiency: the profile does not depend on n.** Multiplicity per complex irreducible, n ≥ 3 (computed n = 3..22, 24):
```
             1+   1-   2+   2-   3a   3b   2c   2r   6L   6g    (6Ld = 6L, 6gd = 6g)
D_disj        3    1    2    1    5    6    4    4   11   12
D_tri         0    0    1    1    2    2    1    2    4    4
H2(core)  fl((n-1)/2)  fl(n/2)  0  0  n/2-1 n/2-1 n/3-1 n/3-1  n-2  n-3
```
Why: the marks are one regular orbit, so D_disj = (Γ_2-shaped part) ⊕ Q[G_n] = 1 − Q[G/S_c] + 2Q[G/S_e] + Q[G], and
D_tri = Q[G] − Q[G/C3] = Ind_{C3}(augmentation) — permutation modules, multiplicity = dim of stabilizer-fixed vectors.
Scaling adds channels, not multiplicity. Invariant reader: D_disj^G = 3 = β1 of the quotient graph (3 vertex orbits, 5 edge
orbits); D_tri^G = 0. H2(core) = U⊗U⊗U: on N, θ_b occurs n − #(distinct coordinates of b) times — 3 distinct off the lines,
2 on them.

**Redundancy: quadratic per channel, with line and 2-adic corrections.** H2 of the commuting-square vocabulary, per complex
irreducible (quadratic fits on residue classes, every further value matched — 1 to 17 checks per form; and Σ count × degree ×
multiplicity = the closed-form dimension in all 12 residues mod 12 for all eight modules D_disj, D_tri, H2, A, C2, C2_tri,
H2_disj, H2_disj+rot3):
```
1+, 2+    11n^2 - 21n/2 + {1/2 odd, -1 even}
1-, 2-    13n^2 - 14n   + {3 odd, 2 even}
3a        36n^2 - 155n/4 + {3 if n = 0, 17/2 if n = 2  (mod 4)}
3b        36n^2 - 143n/4 + {0,  11/2}
2c, 2r    24n^2 - 25n + {4 odd, 1 even}
6g        72n^2 - 75n + {12 odd, 15 even};    6L = 6g + fl((n-1)/2)
6gd       72n^2 - 75n + 3;                    6Ld = 6gd + n/2
```
H2 of squares + rotation triangles = H2_disj ⊕ H2(core), channel by channel (characters equal for every n computed).
Leading term 12n² per dimension of the channel everywhere except the linear pair: 11n² where the slope is +, 13n² where it
is −. The swap reader carries 2n² − 7n/2 + O(1) more redundancy than the identity reader. The degree-3 (2-torsion) channels need n mod 4.

**Mechanism on free channels (n = 3..6, 0 mismatches).** Frobenius over N: m_{Ind θ_b}(M) = the number of N-orbits of cells
whose N-stabilizer lies in ker(θ_b · orientation). Stabilizers that occur: trivial; K_i ≅ Z_n (one class fixed pointwise —
the lines are exactly the θ_b that kill some K_i); at even n, Z_2 (cells exchanged by an order-2 translation — on a square
this exchange reverses its orientation) and K_i × Z_2 (antipodal same-class pairs). Doubles kill all of N[2] = F4: they count
the exchanged pairs and lose the reversed squares. The six antipodal exchange configurations of § 81 are the n = 2 instance of the antipodal same-class pairs.

**The exchange is orientation.** K₃,₃, two unlabelled tokens, commuting squares: every move lies in exactly two squares and
every configuration link is one circle — a closed surface, χ = −3, H2(Z) = 0: nonorientable, five crosscaps, H1 = Z⁴ ⊕ Z/2.
Labelled tokens: closed, χ = −6, H2(Z) = Z — orientable, genus 4. The labelled complex is the swap's double cover and it is the
orientation cover: the swap is w1, and the integral exchange class is the torsion of a nonorientable surface.
Canonical detector on any arena: label the tokens by vertex order, η(move) = 1 iff the moving token crosses the parked one.
Around a loop η counts label exchanges mod 2; it vanishes on every cell that returns each token to its own start and is 1 on
an exchange. Γ_3: support 2,520 of 11,970 moves; 0 of 13,239 squares fail; 1 on the exchange triangle. Hence z ≠ 0 mod 2,
with 2z = 0 from the certificate.

**What the triangles leave.** Witness over Z:
```
squares                                   H1 = Z^19 + Z/2      detector  eta        (swap parity)
squares + rotation triangles              H1 = Z/2             detector  eta + len  (swap parity + step parity)
squares + parked triangles                H1 = Z/2             detector  eta
squares + rotation + parked triangles     H1 = 0
```
A rotation triangle is itself a 3-move exchange (η = 1 on every one), yet the torsion survives it: η + len is zero on squares
(0 + 4) and rotation triangles (1 + 3) and one on a parked triangle (0 + 3). Two parities on the squares complex, swap and
step: rotation triangles identify them and leave their difference; parked triangles kill the step and leave the swap;
integral closure takes both. For every n ≥ 3 the parked triangle is a class of order exactly 2 in squares + rotation triangles
(J sends it and the rotation triangle on the same triangle to the same graph cycle, ker J = Z/2 by § 75, and η + len = 1 on it).

**Readers follow prime splitting in Z[ω]** (`methods/galois_primes.py`). Rational blocks of the free channels at prime n:
inert p = 5, 11, 17: (p + 1)/3 blocks, all of size (p − 1)/2; split p = 7, 13, 19: 2 + (p − 1)/3 blocks — two of size (p − 1)/6
(the two prime ideals above p), the rest (p − 1)/2. At n = 2 (2 inert) G_2 = AGL(1, F4) × swap: the witness is the bottom rung.

Open: the 3a/3b and 2c/2r constants are recovered (fits), not yet read from a stabilizer census as the free channels are.

## § 84. Recursion: base case, carry step, and how deep k tokens read — `methods/recursion.py`, `recursion_k.py`, `recursion_joint.py`, `recursion_joint_mp.py`

**From the GPT notes of 10 Oct (three texts) and the GPT handoff file.** Taken: (i) all-n splitting: c = (1,−1;1,0,0) has
c⁶ = identity over Z (re-run, R0), so G_n = N ⋊ ⟨c⟩ for every n — the § 83 check (n ≤ 12) is now a proof. (ii) The rational
part of a loop's class is the *aggregate* circulation J (sum of both tokens' tracks), not each token's own path — my
coder-mode wording overstated it. (iii) "Swap twice disappears" is 2[z] = 0 in H1, not a rewrite sequence contracting the
double exchange. (iv) The slope (a character of symmetries) and inversion parity (a character of closed token runs) are two
different one-bit maps; they meet where shown (n = 2: z acts as label swap at the antipodal configurations, § 81), not by
identity. (v) The 3,366-move detector came from a pasted audit, not GPT's workbook. Handoff § 6 wording: after rotation
triangles the survivor is read by η + len, and parked triangles kill *that*; parked triangles alone kill step parity and keep η.

**Base case and step.** R1: every slide is two flips (F_c F_d = S_{c−d}), and ⟨flips, rotate⟩ = G_n for n = 2..12: the
instruction set is the forced flip plus the chosen rotate. R2: the step "NOT bit 0; when it wraps, step the rest" equals +1
mod 2^k and commutes with dropping the top bit (k = 1..12, every state): add is NOT called recursively through the carry.
Width 2^k → 2^(k−1) (reduce mod 2^(k−1)) is a homomorphism of G onto G with kernel {(0,0,0), (0,m,m), (m,0,m), (m,m,0)},
m = 2^(k−1): each doubling adds one four-element layer acted on by the six units exactly as the witness's translations are.
|G_{2^k}| = 6·4^k: the witness (k = 1) plus k − 1 more such layers.

**How deep k tokens read.** A_k = loops of k unlabelled tokens (1 − C0 + C1, invariant k-subsets counted as
[x^k] ∏_cycles (1 + x^len); dimension 1,549,558,126 at n = 6, k = 4; 3.06 × 10¹² at n = 16, k = 4). Free channels tagged by
their restriction to the translations. Result, n ∈ {6, 8, 9, 10, 12, 15, 16, 18, 20, 24}, k = 1..6 (k = 6 at n ≥ 16 in
60-digit arithmetic — in double precision the multiplicities, ~10¹⁵, round wrongly and fake a failure):
the multiplicity of a free channel in A_k is a function of the reader's joint restriction, up to the six units, to the lane
fixers K_i and to the translations of order dividing gcd(n, lcm(1..k)). Per-order tags taken separately suffice for k ≤ 4
and fail at k = 5 (n = 12, 18, 24): five tokens can be held by an order-6 translation acting 2 + 3 on two lanes, so the
orders must be read jointly. A new reading enters at k = d exactly when d | n and n/d ≥ 3 (d = 2, 3, 4, 5; at n/d = 2 the
pulled-back readers are not free channels): one token reads lanes only; two read one halving (the § 83 doubles); three read
thirds; four read quarters. Distinct free-channel multiplicities at n = 24: 2, 3, 8, 13, 17, 13 for k = 1..6 (exact, § 86; the 23 first printed here was a double-precision artefact).
In the carry tower n = 2^j (n = 8, 16 tested, k ≤ 6) a k-token reading resolves ⌊log₂ k⌋ levels below the top.

## § 85. SHA-256 full-adder state maps to the three-lane parity reader — `sha256_multioperand_carry_census.py` (GPT, 10 Oct; adopted after the checks in § 86)

**The local encoding is exact.** For each SHA bit position, let `x_i = (a_i,b_i,c_i)`, with incoming carry `c_i`. Then

    s_i = q(x_i) = a_i XOR b_i XOR c_i
    c_{i+1} = M(x_i) = majority(a_i,b_i,c_i).

`q` is exactly the `n=2` three-lane parity readout from the witness. `M` is a second readout and is not determined by `q`. An exhaustive check of all eight states and all 24 transformations `x -> R^r(x XOR m)` gives orbit/stabilizer sizes `2/12` for `q` and `8/3` for `M`. Rotation preserves both; the all-ones flip toggles both; every XOR mask changes `q` by its parity. The even mask `(0,1,1)` at state `(0,0,0)` leaves `q=0` but changes `M` from 0 to 1. The sum channel and carry channel therefore cannot be merged into one readout.

**Run through the SHA path.** Instrumented serial ripple execution matched `hashlib.sha256` on the same 89-message corpus, 1,111 padded blocks, 666,600 two-word additions, and 21,331,200 bit-level full-adder cells. Every local sum bit was read as `q`; every carry handoff was `M`.

**Joint operand view, kept distinct from token count.** An alternate `k`-operand column recurrence was compared with serial addition over 346,632 semantic sums. SHA `T1`'s five terms exhibited carry states 0 through 4; four-term schedule sums exhibited 0 through 3; two-term sums exhibited 0 and 1. The joint-column carry is an integer state, not the one-bit carry of a serial full adder. These internal traces have different state descriptions even when their modular sum agrees.

For every semantic sum group, projections `2^32 -> 2^31 -> 2^30` preserved the low result and the corresponding lower carry-trace prefix: 693,264 checks, no failures.

**Scope:** this supplies an exact local bridge from SHA addition to the NEXUS three-lane parity readout. It does **not** establish that the §84 `k`-token reader-depth result transfers to SHA-256. Token count, operand count, the integer carry states of a joint-column sum, and one-bit width-descent depth remain distinct variables. The next gate is to define and test an explicit encoding of the 32-position carry trace into the existing `A_k` token-loop space at the target modulus.

## § 86. The adder cell taken apart; SHA as two registers; time as handoffs; the walk as counters — `methods/cell.py`, `methods/carry_time.py`

Dean (10 Oct): the gap is the space between transformations and time measures it; describe SHA as a machine (an odometer of
hex wheels), change the description not the math; tag-up is a threshold event; think like a coder — find it, take it apart,
ask where else it runs.

**Corrections.** (i) The `step` shown in my § 84 reply omitted the empty-list base case (GPT caught it; `recursion.py` has it).
(ii) Double precision faked the n = 24, k = 6 count in § 84 (23 → 13). (iii) 60 digits is not a certificate — now replaced:
for a free channel, φ(n) n² m = Σ_j S_j c_n(j), S_j = Σ of χ_{A_k}(a) over translations with b·a ≡ j, c_n = Ramanujan sums —
integers only. The joint-tag rule of § 84 holds exactly for k = 1..6 at all ten widths; distinct counts at n = 24: 2, 3, 8, 13, 17, 13.

**The cell.** x = (x0, x1, x2) ∈ F2³ under the 24 witness maps x ↦ R^k(x ⊕ a). The 256 one-bit functions fall into 22
orbits. The cell's 8 states carry 1+ ⊕ 1− ⊕ T ⊕ T·ε (Walsh weights 0, 3, 1, 2; T = the single-lane triple). SHA's three
bit functions:
```
parity  (sum bit; Sigma0/Sigma1 bitwise)  orbit 2,  stabilizer 12, span 1:  sign = chi_111                 -> 1-
majority (carry; Maj)                     orbit 8,  stabilizer 3,  span 4:  (chi_100+chi_010+chi_001-chi_111)/2 -> 1- + T
choice  (Ch)                              orbit 24, stabilizer 1,  span 6:  (chi_010+chi_001+chi_101-chi_110)/2 -> T + T.eps
```
Together they reach all seven non-constant directions of the cell. § 85's orbit/stabilizer/span numbers and the majority
expansion reproduced. Majority is the threshold reader (fires at two of three): the only output of an adder cell that leaves it.

**SHA as two registers.** A_{t+1} = T1 + Σ0(A_t) + Maj(A_t, A_{t−1}, A_{t−2}), E_{t+1} = A_{t−3} + T1,
T1 = E_{t−3} + Σ1(E_t) + Ch(E_t, E_{t−1}, E_{t−2}) + K_t + W_t; b, c, d and f, g, h are A and E one, two, three ticks back, and
the digest is IV + (A64, A63, A62, A61, E64, E63, E62, E61) — equal to hashlib.sha256 on 303 messages. The 64 hex digits are two
32-bit registers read across four consecutive ticks; Maj reads three ticks of A (time), Σ0 three bit positions of A (space).
(The two-sequence form is a standard rewriting of SHA-2, recovered.)

**Time as handoffs.** Ripple: a carry generated at a = b = 1 is handed through a ⊕ b = 1 bits. Longest handoff chain per
two-word addition: mean 4.29 (max 19) on 20,352 of SHA's own additions, 4.29 (max 15) on uniform pairs. Same carries by
parallel prefix ((g,p)∘(g',p') associative): equal on every pair, 5 combining levels for 32 bits. Re-bracketing the same
recursion turns 32 handoffs into 5 levels (standard carry-lookahead, recovered).

**The walk as counters.** On the bare cell, continue = (b, c, a) has cycles {000}, {001,010,100}, {011,110,101}, {111} — a ring
counter; turn = (b, c, ¬a) has the 6-cycle 000→001→011→111→110→100 and the 2-cycle {010, 101} — a Johnson (twisted-ring)
counter. Turn's 6-cycle with the middle lane flipped is 010→011→001→101→100→110: every non-constant code once, one bit per
step; the 2-cycle becomes {000, 111}. (That six-step one-bit-per-step code is the standard three-phase Hall-sensor sequence,
with 000 and 111 the fault codes — engineering fact, not run here.)

Open next: the channel content of a SHA round — how much of each step lives in 1− (parity, linear) versus the two triples
(majority, choice, carries) — measured on the two-register form.

## § 87. Slides are readers: the quadratic phase in our terms; the orbit-count rule for every channel — `methods/chirp.py`, `methods/inertia_rule.py`

**From GPT (10 Oct; numbered § 86 in its copy, which lacks this ledger's § 86 and the § 84 correction).** On slides
(x, y, −x−y) the phase u = e(Q/n), Q = x² + xy + y², is fixed by rotation and negation; a shift by (r, s) multiplies u by a
constant and the frequency (2r+s, r+2s) (determinant 3); exact correlation kernel {t(n/3, n/3)} when 3 | n, trivial otherwise;
Fourier power flat (n²) for 3 ∤ n, 3n² on one third of the bins for 3 | n; and U_L E(a) = E(La) for all six linear maps
(8,891,736 exponent comparisons). Taken: Q(Lx) = Q(x) and the shift identity are polynomial identities (re-run in sympy), so the
equivariance is proved, not sampled.

**In our terms.** The polar form of Q on slides is the plain lane dot product, Q(a+c) − Q(a) − Q(c) = a·c (sympy). So the
phase realizes slide a ↦ reader θ_a(c) = ζ^{a·c}. This map intertwines exactly with the reader action used in every channel
computation of §§ 83–86 (act(g, a) = g a g⁻¹ for all g, all a; n = 2..12). Its kernel = the radical of the dot product = the
diagonal slides {t(1,1,1): 3t ≡ 0}, size gcd(3, n) (n = 2..40). When 3 | n the image is the readers with Σb ≡ 0 (mod 3) — one
third; the diagonal slide (n/3)(1,1,1) reads as nothing and two thirds of the readers have no slide address. Readers and slides
are one space with the same motions, glued by the dot product; the glue fails exactly at the ramified prime of § 83. [Corrected § 90: that failure belongs to this symmetric glue only; the alternating glue matches every slide
to exactly one reader at every n.]
Restated in address form: a free channel's multiplicity counts the N-orbits of cells whose stabilizing slides h satisfy a·h ≡ 0
(≡ n/2 where h reverses the cell's orientation) — § 83; a line is an address with two lanes equal (mod the diagonal); a double
is an address ⟂ N[2]; and k tokens see an address only modulo gcd(n, lcm(1..k)) — § 84, since the joint tag is a function of
a mod L.

**New: the same count governs the channels that are not free.** For χ = Ind_T^G ψ (T the inertia group, ψ a linear
extension): m_χ(cells) = #{T-orbits on which ψ equals the orientation sign on the T-stabilizer}. Checked against character
inner products on graph vertices, graph edges, configurations, moves and commuting squares at n = 3, 4, 6, 8 — both 2-torsion
channels at n ≡ 0 and 2 (mod 4) and all three 3-torsion channels:
```
n  channel   V  E    C0    C1    SQ  ->  D_disj   A     H2_disj
3  2c/2r     2  6    93    442   490      4      349    145     (all three extensions equal on the arena)
4  3a        3  8    226   1098  1291     5      872    424
4  3b        5  11   232   1116  1311     6      884    433
6  3a        3  8    437   2306  2936     5     1869   1072
6  3b        5  11   443   2324  2962     6     1881   1087
6  2c/2r     2  6    294   1540  1957     4     1246    715
8  3a        3  8    734   3946  5204     5     3212   1997
8  3b        5  11   740   3964  5236     6     3224   2018
```
Every value equals § 83's table. The constants § 83 left as fits are therefore orbit counts under the inertia group; the
closed forms now need only the census of those orbits by stabilizer type (the n mod 4 split of 3a/3b sits there).

## § 88. Round-by-round SHA channel census: operation counts versus character content — `sha256_round_channel_census.py` (GPT, 10 Oct; § 87 in its copy)

**Two-register execution checked.** The recurrence was run on 303 reproducible messages, 216,789 bytes total, 3,579 padded blocks, and 229,056 block-round samples; every digest matched `hashlib.sha256`. The round-channel profile includes the 64-round core only. Message-schedule and feed-forward operations are excluded from these per-round counts, though they are included in the digest check.

**Exact operation counts per block-round.** Seven serial 32-bit additions provide 224 full-adder cells. Each emits one parity/sum readout q and one carry-majority M. The two Sigma functions add 64 more parity readouts, and SHA adds 32 Maj cells and 32 Ch cells:

```
parity q / Sigma:      224 + 64 = 288
carry M / SHA Maj:     224 + 32 = 256
SHA Ch:                           32
parity vs (M + Maj + Ch):        288 : 288  (50% : 50% by call count)
total local bit-function calls:  576 per block-round
```

This is an operation-call count, not a runtime estimate.

**The representation split is not the call split.** Exact Walsh expansion of signed local readouts gives q entirely in `1−`; M has squared-coefficient energy 1/4 in `1−` and 3/4 in T; Ch has energy 1/2 in T and 1/2 in Tε. Because majority straddles channels, assigning every nonlinear call wholly to the triple channels would be incorrect. Weighting by the exact counts yields

```
E(1−) = 288 + 256/4 = 352   (61.111...%)
E(T)  = 3·256/4 + 32/2 = 208 (36.111...%)
E(Tε) = 32/2 = 16             (2.777...%)
```

The figures are exact local Walsh/Parseval weights over the eight possible cell states. They are not percentages of execution time, cryptographic influence, or digest contribution.

**Sample profile.** Across this corpus, parity outputs were 1 on 32,990,477 / 65,968,128 cells (0.500097); adder carries on 24,702,713 / 51,308,544 (0.481454); SHA Maj on 3,667,555 / 7,329,792 (0.500363); and Ch on 3,663,534 / 7,329,792 (0.499814). The round-index variation is in `sha256_round_channel_profile.csv`. Those rates are empirical and input-dependent, not mathematical invariants.

**Scope and next test.** The counts and Walsh decomposition are structural; the value rates are corpus-specific. This does not yet prove the § 84 token-depth law for SHA. The current profile uses left association `(T1 + Σ0) + Maj`, matching the written recurrence. Standard SHA implementations often form `T2 = Σ0 + Maj` first. Since the association preserves the modular result but may alter internal carry traces, the next falsification test is a paired, same-input comparison of both addition trees and their per-round trace distributions.

*Checked here:* the structural numbers re-derived by hand — seven serial additions per round (T1: 4, A: 2, E: 1) = 224 cells, Σ0 + Σ1 = 64 parity cells, Maj 32, Ch 32; Walsh energies q: 1 in 1−; M: 1/4 in 1−, 3/4 in T; Ch: 1/2 in T, 1/2 in Tε (§ 86's expansions); totals 352 / 208 / 16 of 576. The corpus rates were not re-run (script not supplied).

## § 89. The local transition transported into Walsh coordinates — `verify_walsh_transition_path.py` (GPT, 10 Oct; § 88 in its copy)

**The path is three maps, not one.** Pointwise sign encoding sends each bit to `A=(-1)^a`, etc., turning XOR into multiplication. The full Walsh map then sends the eight values of a reader truth table to eight coefficients. Both are invertible when all values and all coefficients are retained. Selecting a sector is a separate projection and is where information can be discarded. A single bit-state is not itself a Walsh coefficient vector: the coefficient vector represents the reader over all eight possible cell states.

For `F(a,b,c)=(b⊕1,c⊕1,a⊕1)`, ordered states `(000,001,010,011,100,101,110,111)`, let `P[y,x]=1` when `F(x)=y`; pullback on readers is `Pᵀ`. In basis `(1,A,B,C,AB,AC,BC,ABC)`, exact conjugation by the Walsh coordinate map gives

```
M = W Pᵀ W⁻¹ =
[ 1  0  0  0  0  0  0  0]
[ 0  0  0 -1  0  0  0  0]
[ 0 -1  0  0  0  0  0  0]
[ 0  0 -1  0  0  0  0  0]
[ 0  0  0  0  0  1  0  0]
[ 0  0  0  0  0  0  1  0]
[ 0  0  0  0  1  0  0  0]
[ 0  0  0  0  0  0  0 -1]
```

Hence `1→1`; `A→−B→−C→−A`; `AB→BC→AC→AB`; and `ABC→−ABC`. `M⁶=I`; `M³=diag(1,−1,−1,−1,+1,+1,+1,−1)`, matching the pullback under `F³(x)=x⊕111`. Constant, degree-one, degree-two, and degree-three Walsh subspaces are preserved by this transition.

**Independent exact regression.** The script checks the state and Walsh matrices using integer arithmetic and rational rank elimination. It reproduces parity/majority/choice orbit sizes `2, 8, 24`, their combined signed-reader span rank `7`, and `22` total orbits among the 256 Boolean functions under the 24 maps. No floating-point arithmetic is used.

**Scope.** This proves the local reader coordinate path and the transition's action in those coordinates. It does not yet lift a full SHA state or a 32-bit carry graph into the cell machine. That encoding must preserve input addresses, output destinations, spatial and temporal edges, and carry handoffs. A sector projection is not a substitute for that execution-path certificate.

*Checked here:* the script re-run in an isolated directory, all checks PASS. F = (¬b, ¬c, ¬a) is the walk's turn seen with the middle lane flipped: F = H T H, H(a,b,c) = (a, ¬b, c) — the Hall frame of § 86. Block-diagonality by Walsh degree holds for all 24 maps (each permutes the characters of one weight, with signs), which is § 86's split 1+ ⊕ T ⊕ Tε ⊕ 1−.

## § 90. Two glues from slides to readers; every channel is a direction — `methods/glue.py`

GPT (10 Oct) proposed the alternating pairing det((r,s),(x,y)) = ry − sx on slides (x, y, −x−y). Checked and taken, with this
ledger's own consequence.

**Two glues.** Dot glue (the quadratic phase, § 87): reader of a = ζ^{a·c}. Alt glue: reader of a = ζ^{det(a,c)}, i.e.
b = (−s, r, 0). The alt glue is invariant under all six linear maps (sympy), a bijection slides → readers for n = 2..40, and equal to
the reader action used in every channel computation (n = 2..12, all g, all slides). The two glues differ by one multiplication:
dot(a) = alt(K a), K = −(1 + 2R) = [[1,2],[−2,−1]], KR = RK, K² = −3, det K = 3 — K is −√−3 in Z[ω] (every slide, n = 2..40). So
the symmetric glue is the alternating one after multiplying by the ramified prime, and loses exactly its torsion (the diagonal
slides) when 3 | n. Correction to § 87: "two thirds of the readers have no slide address" is a property of the dot glue only.

**Every channel is a direction.** Under the alt glue, for every reader at every n = 2..24:
```
reader                               alt address (a slide)
trivial                              0
2-torsion (3a, 3b; n even)           a half-turn slide, 2a = 0
rotation-fixed (2c, 2r; 3 | n)       a third-diagonal slide, (n/3)(1,1,1) or (2n/3)(1,1,1)
line (6L, reads one lane)            a lane-fixing slide (one lane still)
double (6Ld, 6gd)                    a slide in 2N
```
What a reader cannot see: for gcd(r, s, n) = 1 the reader at a is blind exactly to the multiples of a (n = 2..24). With the § 83 /
§ 87 counting rule: a channel's multiplicity in any cell module = the number of cell orbits held only by slides along its own
direction (with the orientation sign). Line channels are blind exactly along a lane fixer, so they see the lane vertices that the
lane fixers hold — the one copy by which D_disj reads 11 instead of 12. k tokens know a direction only modulo gcd(n, lcm(1..k)).

## § 91. Every channel of the redundancy, derived from three traces; the all-n proofs — `methods/torsion.py`, `methods/allchannels.py`

**GPT (10 Oct), sorted.**
- Its first torsion write-up (H2 multiplicities read as square-orbit counts; 3a/3b as Galois conjugates; "half contributions")
  — wrong, and retracted by GPT. Not used.
- Chain identity m(H2) = m(C2) − m(C1) + m(C0) − [trivial] + m(H1): the identity in use since § 81 (H2 = D − A + C2). Taken.
- H2(Y) ≅ H2(X) ⊕ H2(K_{n,n,n}) over Q, X = commuting squares, Y = X + rotation triangles: relative sequence
  0 → H2(X) → H2(Y) → ker(δ: T → H1(X)) → 0, and J: H1(X; Q) ≅ H1(Γ_n; Q) (HKRS Thm 4; its hypotheses checked for every n in
  § 75) turns ker δ into H2 of the triangle-filled graph = the core's. **PROVED for all n ≥ 3**; upgrades § 83's character check.
- Aut(Γ_n) = G_n for all n ≥ 3: the face functional-equation proof (each label map sends consecutive pairs {z, z+1} to
  consecutive pairs, so f_i = s x + a_i; one common slope; Σa = (1−s)/2). **PROVED.** Its first version (dihedral quotient, a
  "60° rotation" section) is rejected: μ6 is cyclic, the slope fixes every class; the section is c with c⁶ = 1 over Z (§ 84).
- Core: H2(K_{n,n,n}; Z) = Z^{(n−1)³} with the explicit basis Z_abc (eight triangles each, independent via the all-non-base
  triangle) and the trace formulas — taken; its script re-run in isolation, PASS for n = 3..8; matches § 83's kernel traces.
- Its seven-signature square census: exact counts, fitted formulas — superseded by the derivation below. Its
  m3a(C2) − m3b(C2) = −3n − 8 agrees with § 87's table.

**The derivation, all n ≥ 3.** χ_H2 = χ_C2 − χ_C1 + χ_C0 − 1 + χ_H1, χ_H1 = 1 − v + e on the graph (via J). In graph fixed
points: C0 = C(v,2) + #2-cycles; C1 = e₊(v − 2) − e₋v; C2 = #disjoint pairs of fixed edges − #edge pairs swapped by g (a swapped
square reverses orientation: its two edge maps compose to the identity and exchanging the factors gives −1). Three traces:
```
translations a        chi = B z0 + (n/2) z_half + (D_n - 3B)[a = 0] - 3n^2 [a != 0, 2a = 0],   B = (n^2 - n)/2
   one zero lane: B | one half lane, no zero lane: n/2 (own-leaf edges swap in n/2 pairs) | half-turn slide: B + n - 3n^2
   (6n^2 + n swapped pairs) | otherwise 0
flips x -> a - x      n even: all lanes odd (no fixed label): -6n^2 + 3n/2
                              two lanes even (12 fixed edges, 34 disjoint pairs, (18n^2-21n+4)/2 swaps): -6n^2 + 27n/2 - 12
                      n odd:  one fixed label per lane (9 fixed edges, 15 disjoint pairs): -6n^2 + 21n/2 - 15/2
rotation cosets       nothing fixed, no 2-cycles, no swaps: chi = -1 + 1 = 0
```
Checked exactly: every translation n = 3..16, every flip n = 3..16, rotation cosets sampled. Channels follow by averaging:
```
1+ = 2+   11n^2 - 21n/2 + {1/2 odd, -1 even}      (rotation cosets vanish, so the rotation phase is invisible)
1- = 2-   13n^2 - 14n + {3 odd, 2 even}
free b    72n^2 - 75n + 12 + [line](n - 1 + eps)/2 + [n even]*(+3 non-double | -9 double),  eps = -1 non-double, +1 double
3a, 3b    sum 72n^2 - 149n/2 + 17/2 - 11*delta/2, delta = (-1)^(n/2);  3b - 3a = (F2 - F0)/4 = 3n - 3
2c, 2r    24n^2 - 25n + 4 - 3[n even], all three extensions equal (rotation cosets vanish)
```
All 182 channel rows of § 83's tables (n = 3..22, 24) equal these forms. § 83's fits are now theorems; adding rotation triangles
adds the core channels (§ 83) through the proved splitting.

**Where the constants come from.** The half-turn slides carry them all. δ = the 2-torsion reader on a half-turn = (−1)^{n/2}:
whether the half-turn is itself a double, i.e. survives one more halving (§ 84's carry tower) — that is the n mod 4 split. The
free-channel +3 / −9 is the reader summed over the three half-turns (−1 or 3) times −3n². The 3-torsion drop of 3 at even n is
the same three half-turns, which that reader cannot see. 3b − 3a = 3n − 3 counts the flips whose two even lanes have fixed labels.
The rotation phase never enters the redundancy: every rotation coset traces to zero.

## § 92. The other version: the stored lines; a reader cannot fail to read; A and C2 closed; one correction — `methods/presentation.py`, `witness_shapes.py`, `family_stored.py`, `allchannels2.py`, `face_quads.py`, `bbp_poles.py`, `sha_round_inverse.py`

**Two versions of one game.** Played: the field — states and moves. Stored: lines, each an equality of two move sequences
(r x r⁻¹ = x y: "A + B = Fire"); the field is their closure. §§ 74–91 computed the played version with stored shapes filled
in: H1 = loops the stored shapes leave open (D), H2 = closed surfaces made only of stored shapes (a line stored twice).

**GPT (10 Oct), sorted.** The intertwining square E∘T = T̂∘E is § 79's field/computer map — taken. E(x) = E(y) ⇒ E(Tx) = E(Ty)
is the condition for a quotient machine; automatic for a reader that is a homomorphism — taken. ρ(a∘b) = ρ(a)∘ρ(b): a
representation, i.e. a channel — taken. "Field-valid ⇏ reader-executable": a reader is defined on every word (below); what a
reader can fail is consistency, never reading; running out of register is a matter bound (SHA, below). Γ_{t+1} = Ψ(Γ_t, …)
left unformalized by GPT; W2 below computes the two operations the stored version has: add a line (merge), add a move (extend).

**The witness, stored** (`presentation.py`).
```
C^3 = 1               triangle   three lanes
(C^-1 T)^2 = 1        square     u = C^-1 T flips one lane: the swap
(u.CuC^-1)^2 = 1      octagon    flips on different lanes commute: C1a   (freely reduced: (C^-1 T^2 C^-1)^2)
each line acts as the identity on all 24 register states: True, True, True
coset enumeration from the three words alone: 24 states; enumerated machine == register machine (all states, all moves): True
without any one line: does not close within 60,000 states
```
Each line is necessary, provably: without the octagon ⟨C, u | C³, u²⟩ = Z/3 * Z/2 (the modular group); without C³, C ↦ 1,
u ↦ 0 maps onto Z and kills the other two lines; without u², u ↦ 1, C ↦ 0 does.

**The stored lines filled into the played field** (`witness_shapes.py`, W1). 24 states, 48 moves, b1 = 25; distinct closed
walks: 8 triangles, 12 squares, 12 octagons. Channels at n = 2 (§ 83's names; ± = the swap = the slope ε): 1+ trivial, 1− swap,
2+ clock, 2− clock × swap, 3a three-dimensional with T³ acting as +1, 3b the signed lanes (T³ acts as −1).
```
filled                          b1  b2  H1 torsion | open loops by channel         | closed surfaces by channel
(nothing: the bare field)       25   0  none       | 1+:2 1-:1 2+:1 2-:1 3a:3 3b:3 | 0
C^3                             17   0  none       | 1+:1 2+:1 2-:1 3a:2 3b:2      | 0
u^2                             13   0  none       | 1+:1 1-:1 2-:1 3a:2 3b:1      | 0
[u,CuC^-1]                      13   0  [2]        | 1+:1 3a:2 3b:2                | 0
C^3 + u^2                        5   0  none       | 2-:1 3a:1                     | 0
C^3 + [u,CuC^-1]                 6   1  none       | 3a:1 3b:1                     | 1-:1
u^2 + [u,CuC^-1]                 7   6  none       | 1+:1 3a:1 3b:1                | 1+:1 2+:1 3b:1
C^3 + u^2 + [u,CuC^-1]           0   7  none       | 0                             | 1+:1 1-:1 2+:1 3b:1
```
- All three: b1 = 0, b2 = 7 = 1+ ⊕ 1− ⊕ 2+ ⊕ 3b. The filled field is the Cayley complex with repeated faces dropped:
  simply connected, H2 = Z⁷ free, so homotopy equivalent to a wedge of 7 spheres (Hurewicz + Whitehead). The field closed by
  its stored shapes is 7 bubbles. Predicted before the run by Frobenius, m_ρ(H2) = dim ρ^⟨C⟩ + dim ρ^⟨u⟩ + dim ρ^⟨v⟩ − dim ρ
  − [ρ = 1] with v = u·CuC⁻¹; matched.
- C³ + u²: the 5 open loops are 2− ⊕ 3a; the octagons (C1a) close exactly those. Same pattern as the n = 2 arena (§ 83):
  squares leave Z¹⁹ ⊕ Z/2, both triangle kinds bring it to 0.
- Octagons alone leave a Z/2. Every pair leaves loops open: each line is necessary in the played field too.

**A new line never errors** (W2). + T = 1 → 1 state; + u = 1 → 3; + T³ = 1 → 12 (A4: the swap forgotten); + T⁶ = 1 → 24
(already a consequence: stored twice, nothing changes); + CT = TC → 6 (Z/6, the readers' field); three random 12-letter lines
→ 1, 6, 2; a new move X with X² = 1 commuting with C and T → 48; a new move with no stored line → does not close within 5,000.
A set of lines always presents a group; the most a line can do is merge everything to one state.

**A reader cannot fail to read** (P3, P4, W3). A reader is the images of C and T. Any two images, in any group, extend to
every word (the free group's universal property): there is no unreadable word. The stored lines decide only whether the
reading is consistent with the field (von Dyck).
```
P3  exponent sums [[3,0],[-2,2],[-4,4]] -> Smith [1, 6] -> Z/6 = Z/3 x Z/2
    readers into Z/2: (0,0),(0,1) | Z/3: (0,0),(1,1),(2,2) | Z/6: (0,0),(0,3),(2,2),(2,5),(4,1),(4,4)
P4  swap reader = #turns mod 2, clock reader = #moves mod 3: 4,000 random words up to length 5,000: True, True
W3  reader into Z^2 ignoring the lines (C -> (1,0), T -> (0,1)): 20,000 random words, 19,976 pairs reaching the same state,
    0 differences outside the lattice of the stored lines span{(3,0),(-2,2),(-4,4)}; the differences span it exactly
    (invariant factors [1, 6]).  Move count into Z: all differences multiples of 3.
```
The error of a reading that ignores the stored lines is always a combination of the stored lines, read. Time as the move
count into Z is such a reader; it agrees with the field mod 3, the clock. The trivial reader always exists.

**Every move divides; only readers merge.** Every move is invertible, so ÷ by a move always works. The non-invertible maps in
this ledger are readers: parity (§ 86), reduction mod 2^(k−1) (§ 84), the dot glue at 3 | n (det 3, § 90). ÷0 is the inverse
of a merge. SHA-256: each round is a move given its word (100,000 random rounds and 2,000 full 64-round blocks inverted back to
the start, `sha_round_inverse.py`); the merge is the absorption (H, M) → H', 768 bits to 256 (counting).

**The family, stored** (`family_stored.py`). Five lines, n written once:
```
x^n = 1,  x y = y x,  r^6 = 1,  r x r^-1 = x y,  r y r^-1 = x^-1
F1  coset enumeration: 24, 54, 96, 150, 216, 294, 384, 486, 600 states = 6n^2, n = 2..10
F2  the lines hold on z -> z + 1, z -> z + w, z -> -w z of Z[w]/n; generated order 6n^2, n = 3..10 (12 at n = 2)
F3  n = 2: 24 pairs (c, t) satisfy the witness's three lines and generate G_2 (= |Aut(C2 x A4)|); in all of them t^3 = r^3;
    r^3 is central and fixes all 4 points of F4
```
von Dyck + equal order: the five lines present G_n (n ≥ 3); at n = 2 they present the witness, and the witness swap T³ is the
half-turn r³. Played: 6n² states. Stored: five lines.

**Every channel of A and C2, all n ≥ 3** (`allchannels2.py`; GPT's torsion traces taken and completed).
```
chi_A(translation a) = 1 - n z0(2a) - 3n^2 [2a = 0] + P_n [a = 0],   P_n = 90n^4 + 90n^3 - 30n^2
chi_A(flip): n even, all lanes odd: -3n^2 - 3n + 1;  two lanes even: -3n^2 - 3n + 49;  n odd: -3n^2 - 3n + 25
chi_A(rotation coset) = 1
A    1+  29n^2/2 + 29n/2 - 1      2+  29n^2/2 + 29n/2 - 2      1- = 2-  31n^2/2 + 31n/2 - {10 odd, 14 even}
     free  n odd: 90n^2 + 90n - 33 - [line];  n even: 90n^2 + 90n - 30 - 12[double] - 2[double line]
     3a  45n^2 + 45n - (49 + 7 delta)/2      3b  45n^2 + 45n - (25 + 7 delta)/2      2c = 2r  30n^2 + 30n - 11 - 3[n even]
C2 = H2 (§ 91) + A - H1 (§ 83), every channel
traces on every element tested, n = 3..12: True;   182 channel rows (n = 3..22, 24), A, C2 and H1 each: mismatches 0
```
δ = (−1)^{n/2} as in § 91. With § 91 every channel of D, H1, A, C2, H2 is now a closed form in n.

**Face quads close the graph-level flow** (`face_quads.py`).
```
n | b1(graph) | b1(+tri) | b2(+tri) | marked faces | quads | b1(+tri+quads) | b2(+tri+quads) | (n-1)^3 + 2n^2
3 |       100 |       36 |        8 |           18 |    54 |              0 |             26 | 26
4 |       181 |       64 |       27 |           32 |    96 |              0 |             59 | 59
5 |       286 |      100 |       64 |           50 |   150 |              0 |            114 | 114
6 |       415 |      144 |      125 |           72 |   216 |              0 |            197 | 197
```
Triangles leave 4n² loops and the core's (n−1)³ surfaces (§ 91). 2n² marked faces × 3 quads: the 6n² cells close all 4n²
loops and add 2n² surfaces, one per marked face — the prism (core triangle + mark triangle + three quads, a sphere; the prisms
are independent, each owns its quads). Open: the arena-level analogue.

**Correction — BBP paper** (`bbp_poles.py`; BBP_Analog_Space_Kulik_2026_1.docx). In t = √2 x:
π = 16 ∫₀¹ (4 − 2t³ − t⁴ − t⁵)/(16 − t⁸) dt; the stored line t⁸ = 16 gives eight poles.
```
common factor (t^2 + 2)(t^2 + 2t + 2), degree 4 -> poles cancelled: 4 of 8
reduced integrand (t - 1)/((t^2 - 2)(t^2 - 2t + 2));  16 * integral_0^1 = pi
surviving poles at angles 0, +-pi/4, pi;  cancelled at +-pi/2, +-3pi/4
```
The paper's abstract, § 2 and R1 say six of eight. It is four.

**Played and stored, across the ledger.**
```
played (the field)                                    stored (the lines)
two sides that continue into each other (C0/C1)       s^2 = 1
witness walk: 24 states, 48 moves                     C^3, (C^-1 T)^2, [u, C u C^-1]
Gamma_n symmetry: 6n^2                                x^n, [x, y], r^6, r x r^-1 = x y, r y r^-1 = x^-1
arena: D = open loops, H2 = bubbles, Z/2 left over    commuting squares (C1a) + rotation and parked triangles
carry tower (§§ 84, 86): 2^k states in one cycle      flip; on wrap, call again one place up
SHA-256 (§§ 85, 86, 88): 2^256 states per block       64 invertible rounds; padding; absorption (H, M) -> H' merges
BBP: base-16 digits of pi                             t^8 = 16
```

**Edges.** Reading never fails; deciding from the lines alone whether two words reach the same state is undecidable for some
finite sets of lines (Novikov 1955, Boone 1958) — never for a finite field, which covers everything here. SHA-256 (FIPS 180-4)
takes messages of fewer than 2^64 bits: the one input it refuses is a length its 64-bit length field cannot hold — a register
bound, not a move.

## § 93. The entire field: one tree of paths, folded by stored loops; the witness is the smallest tape; it scales — `methods/entire_field.py`, `two_closures.py`

**The map.** Continue / turn with nothing stored is a tree: 2·3^r − 1 paths within r, no path returns ("everything must
change"; never closes). Storing a loop declares a motion to be no motion and folds the tree. Folding everything gives one
state ("nothing can change"; never moves). Every field sits strictly between: every move moves every state, every walk can
come back ("cannot hold still, cannot escape"). A reader is a further fold. For each field one exact line, every channel:
loops = stored shapes − bubbles + open (A = C2 − H2 + D); §§ 81–92 are this line for the arena and Γ_n; the witness reads
25 = 32 − 7 + 0.

**The witness is a head on a ring of 3 cells** (E1, 24/24 states each): C moves the head, tape unchanged; T flips the cell at
the head, then moves; u = C⁻¹T flips the cell one behind the head, head still. The field is Z/2 ≀ Z/3 (= C2 × A4, § 83).

**The hole names the third line** (E5). With C³ and u² stored, b1 = 5 in 2− ⊕ 3a (§ 92). A face orbit Ind_H 1 can close that
only if H acts trivially in 2− and fixes a vector of 3a: H trivial or generated by a double flip (V4 itself fails). Every
cyclically reduced closed walk up to length 8 tried as a single third line:
```
length          1  2  3  4  5  6  7   8
closed walks    0  0  1  1  1  4  6  24      (up to rotation and reversal)
closing alone   0  0  0  0  0  1  4  14
shortest: CTTCTT = (C T^2)^2, 12 distinct faces, symmetry: phase shift 0, two cells flipped (a double flip);
          C^3, u^2, (C T^2)^2 -> 24 states
```
C T² is one lap of the ring with two turns: it flips two cells and returns the head. (C T²)² = 1 says two flips commute — C1a,
in a hexagon instead of § 92's octagon (length 8, also a closer). The channels of the hole fixed the symmetry; the search only
picked the shortest walk with it.

**Tapes of k cells** (E2, coset enumeration): lines C^k, u², [u, C^j u C^−j] (j = 1..⌊k/2⌋) give k·2^k states, k = 1..8
(2, 8, 24, 64, 160, 384, 896, 2048); dropping any commutator line: no closure (C^k and u² are necessary by the maps onto Z).
2 + ⌊k/2⌋ lines with these moves; the unbounded tape Z/2 ≀ Z = ⟨a, t | a², [a, a^{t^i}] (i ∈ Z)⟩ is not finitely
presentable.

**One more move holds the unbounded tape in four lines** (E3): ⟨a, s, t | a², [a, a^t], [s, t], a^s = a a^t⟩ contains
Z/2 ≀ Z (Cleary–Riley, arXiv math/0406443; without a² it is Baumslag's 1972 group). s: every cell becomes itself xor its
neighbour (b_j^s = b_j b_{j+1}, from a^s = a a^t and [s, t] = 1). It turns the one stored commutation into all of them:
[b0, bk] = 1 ⇒ (its s-image) [b0 b1, bk b(k+1)] = 1 ⇒ [b0, b(k+1)] = 1. Checked: the lamps b0..b(k+1) with every
commutation but the last, plus the s-image line, close to 2^(k+2) states for k = 1..6; without the s-image line, no closure
within 4,000.

**All of it at once** (established; reached here from continue / turn): every countable group embeds in a two-generator
group (Higman–Neumann–Neumann 1949); every finitely generated recursively presented group embeds in a finitely presented one
(Higman 1961), and there is a universal finitely presented group containing every finitely presented group. That universal
group has an undecidable word problem (Higman ⇒ Novikov–Boone): a reader always reads; deciding whether two paths reach the same
state is not always possible. The field is determined; the undecidability is the reader's.

**The reader moves, the field does not** (E4, generators C^±, T^±):
```
r                 0   1   2   3    4    5     6
paths (tree)      1   5  17  53  161  485  1457
field states      1   5  13  22   24   24    24      diameter 4
```

**SHA's word in the same field** (`two_closures.py`). XOR + rotation on 32 bits is the tape at 32 cells (Z/2 ≀ Z/32): cells
independent, rotation moves the head. ADD stores the same 2^32 states as one odometer, where the cells are chained. The two
differ exactly by the carry: x + y = (x ⊕ y) + 2(x ∧ y), 100,000 / 100,000. Rotation preserves ⊕ in 100,000 / 100,000 cases
and + in 26,646 / 100,000: a symmetry of the cells, not of the odometer.

## § 94. The reader in the mirror: total reading, loose readers, carriers that grow or merge — `methods/mirror.py`

Dean (20:15): pull way back, write a new paper, LOOK IN THE MIRROR. Only transformation exists; memory is matter; logic is
navigation; the reader can never get an error, it must get something; reflection keeps things moving; gravity as a pull into
a more complex system, otherwise readers freeze; it compresses — loose at the human level (a reader can think it is safe and
it is not, read and get nothing back, read and get everything back), the field never errs; "both how I ask and how the
emitter is being read"; 2 + 2 = 4: 4 is the now, 2 + 2 the history; encapsulation (x = ProcessTaxes(fo)) lets simple exist
between complex.

**GPT (10 Oct, eight notes and a CSV), sorted.**
- Two-cell carry certificate (CSV): 32 rows, 32 distinct boundary inputs, all obey both cells and A + B + c0 = s0 + 2s1 + 4c2;
  the carry-ignoring network is wrong on 4 of 16 pairs; one cell's (sum, carry) fibres 1, 3, 3, 1 — all re-run, taken.
- Normal-form proof that the five lines present G_n for every n (x^a y^b r^j, at most 6n², realized by Z_n² ⋊ C6) — taken; it
  upgrades § 92's n = 2..10 check to all n. Γ_n itself has 6n² + 6n vertices: the 6n² are group states — noted.
- Hexagon: CT² = u2 u0, so (CT²)² = 1 ⟺ [u2, u0] = 1 — taken.
- Wording: "a line stored twice" → "a dependency among boundaries" (it can involve several cells) — taken; "no path returns"
  → "no nonempty reduced path returns" — taken; radius-4 saturation is the diameter of this generating set, not motion stopping
  — taken. Wedge of 7 spheres needs simple connectivity, which the full relator attachment supplies — as § 92 said.
- Bass–Serre: K = ker(Z/3 * Z/2 → witness) meets no conjugate of either factor, acts freely on the tree; quotient graph 24
  edges, 8 + 12 vertices, K ≅ F5, and [D] = [QG] − [QG/⟨C⟩] − [QG/⟨u⟩] + [1] — re-run: 2− ⊕ 3a. Taken: the hole's size and
  shape both come from the kernel, not from the run.
- Three closures: rational (orbit spans D), integral (Smith), group (N = K; a perfect residue is possible in general) — taken.
  Hexagon: 32 cells, rank 25, no invariant factor > 1 (integral), 24 states (group).
- Orientation: a stabilizer can act on its cell by a sign σ; the multiplicity is ⟨Res V, σ⟩_H. The § 93 filter assumed σ
  trivial — correct for the hexagon (every symmetry fixing a hexagon preserves its orientation, re-run), not for every walk.
- s needs a larger carrier: on finite-support tapes S = 1 + t is injective with image the even-parity configurations, so s
  cannot act by an invertible map on the old tape alone; V ⊊ sVs⁻¹ ⊊ s²Vs⁻² ⊊ … — taken (correction to § 93's "four lines
  hold the unbounded tape": four lines hold a larger field that contains it).
- Cyclic tape k = 2^ν q: A_k ≅ F2[ε]/(ε^{2^ν}) ⊕ F2[t]/(h_q^{2^ν}); rank S^m = k − min(m, 2^ν) — re-run for every m and every
  k = 1..64, taken. k = 32 (SHA's word): S^32 = 0, rank S^31 = 1; Σ0 = t² + t¹³ + t²², Σ1 = t⁶ + t¹¹ + t²⁵ rank 32.
- SHA row qualified: working-state rounds invertible with the schedule; feed-forward and absorption are separate maps — as
  § 92 said. t⁸ = 16 is the carrier relation, not the whole π extraction — taken.
- Entropy, gravity: "need an explicit rule; a name is not an implementation" — taken as the boundary of what this paper proves.

**Readers on the witness** (M4, M7): classes, whether merged states stay merged after every move (q(h) = q(h') ⇒ q(ha) = q(h'a)),
and mean log2 of the class size.
```
reader                        classes  split by next move   log2 W (bits left out)
one state (nothing back)          1       0/552                 4.585
state (everything back)          24       -                     0
swap: parity of lit cells         2       0/264                 3.585
clock: head position              3       0/168                 3
clock x swap                      6       0/72                  2
cell under the head               2     144/264                 3.585
number of lit cells               4      36/156                 2.774
tape without the head             8      24/48                  1.585
```
The swap and "cell under the head" read the same one bit; one can be run forward, the other thinks two states are one and the
next move disagrees. Loose and safe are not a matter of how much is read.

**Both sides of a reading** (M5): dim Hom_G(V, W) = dim Hom_G(W, V) for every pair of {states, moves, triangles, squares,
hexagons, hole D} — e.g. hexagons|D 3, squares|D 1, triangles|D 1, states|D 5.

**Total reading is built; only matter breaks** (M6): softmax of (1000, 0, −1000) computed as exp/sum gives (nan, 0, 0); shifted
by the maximum it gives (1, 0, 0); softmax(z − c) = softmax(z), so the shift changes nothing in the mathematics. A byte-level
reader (256 byte tokens + a start token, one attention step) returns a valid next-byte distribution on all 20,005 inputs
(empty, 500 × 0x00, 500 × 0xFF, invalid UTF-8, 20,000 random); a word-level reader with a fixed 7-word vocabulary raises
KeyError on 2 of 3 texts. Totality is a stored constraint on the reader (every byte a token, a start token, the shift) — the
same job as SHA's padding.

**Added while writing Working Paper 2** (`witness_shapes_hex.py`, `hex_infinite.py`, `hex_drop1.py`, `mirror.py` M8).
Hexagon form of the fill table: (CT²)² alone b1 13, no torsion; C³ + hexagon b1 6, b2 1 (1−); u² + hexagon b1 3, b2 2, H1
torsion Z/2, open 3a, bubbles 2+; all three b1 0, b2 7 = 1+ ⊕ 1− ⊕ 2+ ⊕ 3b (as with the octagon). Each line of the hexagon
presentation is needed: without the hexagon Z/3 * Z/2; without C³ a subgroup of index 3 has abelianization Z/2 ⊕ Z/2 ⊕ Z;
without the square a subgroup of index 8 has Z/3 ⊕ Z/6 ⊕ Z (low-index subgroups + Reidemeister–Schreier); none closes within
30,000 states. Correction (mine, caught in writing): the "maps onto Z" argument of § 92 works for the octagon form only — the
hexagon has C-exponent 6. Moore refinement of loose readers: "cell under the head" (2) and "number of lit cells" (4) both refine
in two rounds to the same 8 classes — the cells read from the head, head position forgotten; "tape without the head" (8) refines
in one round to 24; the swap is already a congruence.

**Working Paper 2** — *The Reader in the Mirror: Only Transformation: Memory as Stored Constraint, Reading That Cannot Fail, and
a Field Read from Inside*, NEXUS Working Paper 2, v1.0, 10 Oct 2026, 21 pp., DOCX `wp2/build/The_Reader_in_the_Mirror.docx`;
scripts and outputs `wp2/runs/` (SHA-256 prefixes in its Table 10). Synthesizes §§ 81–94. Appendix B forms re-checked against the
verified functions for n = 3..40 (330 channel types, 0 mismatches).

## § 95. Two directions at once: forward accumulation and the shaped pull — `methods/twoway.py`

Dean (21:03): decompile reality, but with two directions at once — forward is Newton, accumulation into mass, brute force;
the opposite is the shaped pull; both share the transformation.

**One discrete line, read both ways (D4).** m(q[k+1] − 2q[k] + q[k−1])/h² = −∇V(q[k]), Kepler, GM = m = 1, q0 = (1, 0),
v0 = (0, 1.2), h = 0.002, 1500 steps. Read forward it is Störmer–Verlet (accumulate from the start). Read as a condition on the
whole path with both ends fixed it is the stationary discrete action (the discrete Euler–Lagrange equation; variational
integrators, Marsden–West, recovered), solved all at once by Newton's method from a straight line: 5 iterations, residual
3.9e-16, largest difference from the forward path 1.7e-13. With no time and no force — the shortest path between the orbit's two
ends in the Jacobi metric n|dx|, n = sqrt(2(E − V)), 80 interior points — the geodesic lies within 4.8e-5 of the orbit, whose
offset from its chord is 0.566 (Jacobi–Maupertuis, recovered). Established beside it: Hamilton's principle ⇔ Newton; in GR free
fall is geodesic motion and the weak-field limit returns d²x/dt² = −∇Φ.

**The field from its loops, both ways (D1).** Own Todd–Coxeter (HLT + Holt's coincidence routine), instrumented.
```
field                  states | both directions: defined  met  merged  killed  peak | forward only: defined  merged  killed  peak
witness, hexagon          24  |                      26    24      1       3    27  |                  75      25      52    29
witness, octagon          24  |                      41    16     10      18    31  |                 112      26      89    35
family n = 3..6     54..216   |       98, 182, 290, 445 defined                     |      341, 625, 1028, 1552 defined
tape k = 4, 5, 6    64,160,384|       85, 183, 508                                  |      386, 944, 3063
```
live = 1 + defined − killed in every row; sympy agrees (24). Forward: define a state for every unread letter. Backward: read
the loop from its far end. Met = the two reads meet with one gap (a deduction); merged/killed = states the loop pulls together.
Forward alone also closes, at about three times the definitions and up to seventeen times the merges.

**Meet in the middle (D2).** Reduced closed walks of length L on the witness: one forward sweep of 4·3^(L−1) words against two
half sweeps of 4·3^(L/2−1) words joined at their common state — L = 4, 6, 8, 10: 108/12, 972/36, 8748/108, 78732/324 words,
4, 24, 412, 3120 closed walks, identical sets.

**Refinement down, closure up (D3; GPT's admission test, checked).** A reader's coarsest move-stable refinement E* has the
start's class a subgroup H; an identity r is admissible iff its normal closure lies in H (every context u: u r u⁻¹ E* 1).
```
reader (refined classes)  |H| core | C          u          T          T^3        CT^2       T^2 C
swap (2)                   12   12  | see/admit  -/reject   -/reject   -/reject   see/admit  see/admit
clock (3)                   8    8  | -/reject   see/admit  -/reject   see/admit  see/admit  see/admit
clock x swap (6)            4    4  | -/reject   -/reject   -/reject   -/reject   see/admit  see/admit
cell under the head (8)     3    1  | see/reject see/reject see/reject -/reject   see/reject -/reject
the state itself (24)       1    1  | all reject
```
("see" = the reader reads a return at the start.) A return seen in one place is not an admitted identity: the "cell under the
head" reader sees C, u, T and CT² return and can admit none of them.

**GPT (10 Oct, eleven notes), sorted.** Taken: no writable slot — the field is never overwritten, motion is g ↦ ga, a reading is
q([w]); the class [w] does not determine the path w — **correction to WP2 § 3.3**: "the field drops nothing" should read "the
field keeps every distinction between transformations; it does not keep which path enacted one"; factor-through-the-quotient vs
faithful (the trivial reader respects every relation); one-sided (continuation) vs two-sided (substitution) equivalence, normal
closure as the two-sided step; refinement down / closure up with K_R ⊆ E* ⊆ E0; the admission test (checked above); the group
construction is the reversible case and non-invertible transformations need presented monoids or categories with congruence
closure; computational mechanics' causal states (Crutchfield) and Myhill–Nerode as the continuation-equivalence collisions;
finite observations fix only the class of implementations that agree on the probes. Not taken: OOP correspondence tables (nouns
for the same equations); "reality as a project".

## § 96. Reversing without breaking the stream; the object is its history; methods stored locally and through an interface — `methods/reverse.py`

Dean (23:39): everything can be reversed, but not all without breaking the stream or losing methods (the photo vs the person;
the crushed car can't come back, a clone can be made); always moving forward, no state exists forever, the inverse must be the
inverse (life can't be greater than death, both must change); the reader gets the bone; the cost of forgetting or continuing.
Check the timing: the event log exists only after the fact; the object is the history of its own transformations; the math
space is fixed, so methods go both ways — some implemented locally in our own object (learning guitar), some through an
interface that matter implements (building a guitar, from the reader's stored potential of the field).

**The field reverses exactly (V1).** All 24 witness moves are permutations; g and g⁻¹ have the same cycle type for every g; no
non-identity element fixes any state; orders 1:1, 2:7, 3:8, 6:8 — every state recurs, none stays.

**A merge is a reader's move (V2).** a(x) = min(x+1, 3): a⁴ = a³ ≠ a², state 3 holds still forever (a(3) = 3), states 0, 1, 2
are left forever — inadmissible as a field move under C1. It is the first coordinate of a permutation of X × {0,1}^b:
```
power   image      fibres       left forever   extra bits to stay reversible   least forgetting H(x | a^n x)
a       1, 2, 3    0,1,1,2      0              1                               0.500 bits
a^2     2, 3       0,0,1,3      0, 1           2                               1.189 bits
a^3     3          0,0,0,4      0, 1, 2        2                               2.000 bits
```
Explicit permutations of 8 and 16 states, whose inverses return every x, checked. The extra coordinate is the history carried in
the shape; forgetting it costs at least H(x | a^n x)·kT ln 2 (Landauer 1961), carrying it costs the extra state (Bennett 1973:
keep the history, copy the result, run back to clear it) — the cost of forgetting or of continuing. Microscopic reversibility
with a merging reader is Loschmidt's resolution, recovered.

**The clone (V3).** A section s of a reader q (one representative per class) and e = s∘q. Best representatives, all states,
continuations up to length 4 (3,864 pairs): the clone's future readings never differ for the move-stable readers (one state,
swap, clock, clock × swap) and differ on 1,344 / 984 / 2,016 pairs for "cell under the head" / "number of lit cells" / "tape
without the head"; in the field the clone replaces 23, 22, 21, 18, 22, 20, 16 of 24 states by another state, and only the
faithful reader's clone is the original. A clone is exact for a reader whose merges are the field's own, forever, and is still
a different state.

**The object is its history.** In the regular field the state reached from the start by a word w is the element [w] = the
history modulo the stored loops; the word is a log, written by a reader, after the fact, and not unique. The stored loops are
exactly the differences between histories that made no difference.

**Learning and building (V4).** G-maps between homogeneous fields G/H → G/K exist iff H is conjugate into K, and their number is
the mark |(G/K)^H| (Burnside's table of marks). The witness group has 26 subgroups in 12 conjugacy classes; maps exist in 50 of
144 ordered pairs; between non-conjugate types never both ways (38 pairs one way, 28 neither); the linear count, double cosets
|H\G/K|, is the same both ways. Learning: a map field → reader (the skill is stored in the reader's own states and moves with
the field). Building: a map reader → matter. Learn-then-build needs H ≤ K ≤ L: matter can be built only as fine as the
potential the reader stored.

**GPT (10 Oct, ten notes), sorted.** Taken: the image/preimage adjunction f_*(S) ⊆ T ⟺ S ⊆ f^*(T) and (g∘f)^* = f^*∘g^* —
backward propagation needs no inverse; ⟨a | a⁴ = a³⟩ (on 4 states) and the overwrite completion (ab = b, ba = a force aa = a,
bb = b; re-run as maps, V5); three depths of reversal (state, stream, history); unique normal form does not give a unique
predecessor; potential is invariant under an isomorphism of transition structure; the endpoint does not determine the last
difference. Qualified: "no state can exist forever" is C1, a constraint on the field, not a theorem about arbitrary maps — maps
with fixed points exist; as V2 shows, they are readers' moves.

## § 97. Carving from the whole block; where the lines live — `methods/folds.py`

**Record.** A second pass on Dean's 23:39 message (branch at 23:45) overwrote `methods/reverse.py` before it was stopped; restored
from `wp2/runs/reverse.py`, byte-identical (SHA-256 09b9ec723cf33966…), and `reverse.out` with it. § 96 stands.

**The carvings of the witness.** 26 subgroups in 12 classes (§ 96, V4); 6 of them normal, so six folds: fields of 24, 12, 6, 3, 2
and 1 states (G, A4 = the swap forgotten, Z/6 = clock × swap, Z/3, Z/2, one state). Every new line tried in § 92 (W2) landed on
one of the six — T = 1 → 1, u = 1 → 3, T³ = 1 → 12, T⁶ = 1 → 24, CT = TC → 6, random lines → 1, 6, 2 — and no other size is
possible: a stored line can only choose among these. Media (G/H → G/K maps, Burnside marks): 196 maps in 50 of 144 ordered pairs
(the sum of the table of marks) — GPT's "50 admissible maps" is 50 pairs.

**Where the lines live.** On the register realization the three lines are carried by the medium's geometry: three cells in a ring
give C³ = 1, two-valued cells give u² = 1, separate cells give the hexagon (flips on different cells commute). No rule is checked
at run time. A 48-entry lookup table carries the same lines as data. The lines are the software; the field and the file are two
places it can sit (§ 3.2 of WP2, P1 of § 92).

**GPT (10 Oct, five notes), sorted.** Taken: empty means no application-level selection, not an empty substrate; a move extends,
a line folds, an interface hides (WP2 § 3.6, § 5.3); carving = W_F + W_B = A, with the ledger's dominated-but-not-spanning
families as the reason inventory is not enough; interface / domain / history as three nested equivalences; Compile⁻¹ is a set;
software defined by role, φ(δ(s, a)) = δ′(φ(s), a). Corrected: "50 admissible maps" → 50 ordered pairs, 196 maps. The "derived
selection rule" GPT asks for exists for the witness (WP2 § 4.4: the hole's channels → admissible symmetry → shortest line).

**GPT (11 Oct, reaction to § 97), checked.** No corrections needed. Re-run of `reverse.py` (identical to `reverse.out`): one way only
in 76 ordered pairs, so of the 66 unordered pairs of distinct classes 38 have a map one way and 28 have none; both ways only on the
12 diagonal pairs (50 = 12 + 38). Its naming of the six folds matches (centre → A4, double flips → clock × swap, all flips → clock,
A4 → swap). One word changed in what we keep from it: the selection procedure is computed and proved for the witness (WP2 § 4.4),
not "derived"; whether a procedure like it exists for other fields is still open.

## § 98. Always compiling: the halt, the cut, and the only edits the field allows — `methods/compile.py`

**Dean's statement (11 Oct).** The field is always compiling; it does not wait for you to finish. Each transformation is
its own compilation that worked or crashed, and a crash is the object's, never the field's. Once the semicolon lands the
thing has run; to get more you must insert before it closes. Complex objects must twist hard to avoid compiling into
something else. Computation is the side effect; compilation is the transformation. Run as written on the witness, with
states (h, b), h in Z/3 and b in F_2^3, C advancing the head and T flipping the cell under it then advancing.

**No compile step (K1).** The map from move words to states is total: all 65,534 words of length ≤ 15 have a value and
none is an error, and all 48 (state, move) pairs are defined. Closing is an event inside that totality, not a separate
phase. Closed words exist only at lengths 3k — the head advances on every move — and their count is 1, 1, 8, 64, 512,
4096 at k = 0..5, that is **8^(k−1)**, forced by requiring an even number of T's at each of the three residues:
2^(3k)/2^3. So the halt density is 1/8 at every admissible length, independent of k.

**The semicolon (K2).** Let w close (ŵ = 1) and cut it as w = p·q. Inserting v at the cut gives
**P V P⁻¹**, where P = p̂ is the address reached at the cut: verified on 240 of 240 cuts of the 9 closed words of length
≤ 8 and all four insertions C, T, CT, TT (the mirrored form P⁻¹VP holds only on 146, by coincidence). At p = 1 and
p = w the twist is trivial and the value is exactly v̂: **a finished program contributes nothing to what follows it**.
Inside, the cut address is the whole content of the edit. The distinct values obtainable by cutting a single line with a
single move: C³ cut by T gives 3; u² cut by T gives 4; the hexagon cut by C gives 4.

**Interruption conserves a class (K3).** Conjugation fixes conjugacy class, so a cut can only return something in the
class of what was inserted. The field has 8 classes, sizes 1, 1, 3, 3, 4, 4, 4, 4. Inserting C at every cut of every
closed word reaches 4 distinct values — the whole class of C and nothing outside it; likewise T and CT. **The halt fixes
the class; the cut chooses the representative, and it covers the class exactly.** This is the exact form of "you get
something no matter what": the output is never arbitrary and never absent.

**The only invisible edits are the stored lines (K4).** Inserting a line (C³, u², the hexagon, or C⁶) anywhere into any
word of length ≤ 6 leaves the end state unchanged in 3,072 of 3,072 cuts; inserting any word whose value is not 1
changes it in 1,600 of 1,600. So **N, the normal closure of the three lines, is simultaneously what the register forgets
about its history (§ 97), the complete set of edits that can be slipped into a running program without changing it, and
the halt conditions.** One set, three readings. Nothing persists under interruption at field level.

**Twisting is a channel property, not a resolution property (K5).** For a reader q let K_q be the elements it cannot
see and core(K_q) the largest normal subgroup inside it; an insertion is invisible at every cut exactly when its value
lies in that core, and the clamp depth is the shortest word that does. Measured over all 448 (word, cut) pairs at length
six, per inserted move:

| reader | addresses | \|K_q\| | \|core\| | clamp | cut by C | cut by T |
| --- | --- | --- | --- | --- | --- | --- |
| one address | 1 | 24 | 24 | 1 | 1.000 | 1.000 |
| swap (lit parity) | 2 | 12 | 12 | 1 | 1.000 | 0.000 |
| clock (head) | 3 | 8 | 8 | 3 | 0.000 | 0.000 |
| clock × swap | 6 | 4 | 4 | 3 | 0.000 | 0.000 |
| cell under the head | 2 | 4 | 1 | 3 | 0.571 | 0.571 |
| number of lit cells | 4 | 3 | 1 | 3 | 0.768 | 0.000 |
| tape without the head | 8 | 1 | 1 | 3 | 0.393 | 0.000 |
| the state itself | 24 | 1 | 1 | 3 | 0.000 | 0.000 |

The clock keeps 3 addresses and is blind to nothing; the swap keeps 2 and is blind to every C. **Persistence is not
bought with coarseness — it is bought by reading in a channel the perturbation does not touch.** Every core that occurs
is a normal subgroup, so a fold of § 97: the reader's blind spot is one of the six carvings.

**The crash is the object's (K6).** Every state has in-degree two, so deleting one leaves exactly 2 of the 48 moves
without a target: the machine goes partial. The three lines are identities between words and are untouched. The object
stops being addressable; the field's rules do not move.

**GPT's defect audit (11 Oct), run and taken.** `defect_relator_orbit_audit.py` reproduces Table 4's ranks exactly
(triangles 8, squares 12, together 20, hexagons 12, all three 25, residual 5) and adds a 25×25 minor of determinant −1,
so the 25 face boundaries are an **integral** basis of the cycle lattice, not only a rational one. Its kernel route is a
second derivation of WP2 Prop 4.2: L = ker(C_3 ∗ C_2 → G) is torsion-free of index 24, so free, and
χ(L) = 24(1/3 + 1/2 − 1) = −4 gives rank 5 — the same 5 the Bass–Serre quotient graph gives (24 edges, 8 + 12 vertices).
Its Fox-derivative point is a real addition and is taken: for R = q^m the derivative carries the norm factor
N_q = 1 + q + … + q^(m−1), which is m times the projection onto the q-fixed subspace, so the stabilizer filter of
§ 4.4 is present in the boundary operator itself rather than applied to the search afterwards. Its
eligibility-versus-closure distinction is correct and kept: the fixed-space condition is necessary, the boundary rank is
the sufficiency certificate.

## § 98a. A compiler that never waits — `methods/streamcompile.py`

**Numbering (§ 134).** Entered on 11 Oct as § 99. That number belongs to the running audit's § 99 (15 Oct, the
order channel), which §§ 100–133 cite throughout; nothing cites this entry, so it is § 98a.

**Dean (11 Oct, 18:10):** stop with grids, look at compilation itself. Built an SLR(1) compiler for statements
`E ;` over `+ * ( ) n` (10 rules, 16 states, 48 table actions, fixed for every input) and fed it one token at a time.

**No end-of-input compile.** On `2+3+3;` the handle `2+3` reduces to E = 5 at token 3, when the second `+` arrives —
before the statement ends — and E + 3 reduces to 8 when `;` arrives. The early clamp is forced by the table and one token
of lookahead; the numbers do nothing. Every token leaves the parser in a definite state.

**The semicolon.** `2+3;` then `4;` appended gives [5, 4]: the first statement is sealed and nothing appended reaches it.
Inserted before its reductions fire, `*4` gives 14 (after 3), 11 (after 2), 20 (with parentheses): the edit's content is
where it lands. Each token's insertion window — tokens until it is reduced away — runs 1 to 8 in `1+1+1+1;`. Same result
as § 98 K2, now in a compiler.

**Crash rate (the decisive finding).** Random token streams into this compiler: crashed 86.2 / 98.0 / 99.7 / 100 / 100 /
100 % at L = 2, 4, 6, 8, 12, 16, first crash at token ≈ 0.5 on average; complete statements 2.7 % at L = 2 and 0 by L = 6.
The table is identical after every crash, and recovery at the next `;` compiles `2*3;` to 6. So a syntax compiler is
**partial** — random input almost always crashes — while the witness of § 98 is **total** (every word has a value). The
field Dean describes ("random code in, something out, no matter what") is the total kind; a partial grammar is a reader
laid on top of it, and the crash belongs to that reader.

**Holding structure open.** Nesting depth k needs stack k + 3 (k = 0..16) while the table stays at 16 states: a finite
reader holds unbounded structure only through a growing carrier — the carrier-must-grow result again.

**Where the work is.** `2+3+3;` takes 6 shifts and 11 reductions; every reduction maps a 1–3 symbol handle to one symbol.
Over a, b, c in 1..5, the 125 programs `a+b+c;` compile to 13 values, 19 programs behind the most crowded one. Shifts keep
every distinction; reductions are the many-to-one steps, so they are where the erasure (and its Landauer cost) sits.


# The running audit

Continues the relation-vocabulary ledger (§§ 1–98a; numbering § 134). Same rules: live output only, ledger words
STANDS / RUNS / DEAD END / OPEN, never CONFIRMED; every correction logged plainly in the entry
where it was made, never silently fixed. Scripts in the session scratchpad; no repository, so
provenance is reproducible in principle and not archived in fact — the same weakness § 48 records.

---

## § 99. The order channel: what a handle destroys, what a fold destroys, and the two readings of one base — `pull.py`, `noloss.py`, `fold.py`, `sphere.py`, `sphere2.py`, `rings.py`, `rings2.py`

**Dean (15 Oct).** The universe is always compiling; the halt is the clamp, and completion is what
the action looks like when the necessary relations connect. Then: it is the route and its reflection,
there is no forward motion, matter and thought move backwards through the compiler, searching is
mapping the path back, so there must be a pull. Then: `5 = 2 + 3`, there is no loss, you always know
the path back. Then: it is not the protein and not the folded state, it is the transformation. Then:
the domain is the surface of a sphere, inert and unmeasurable from outside, and the compiler is the
routes from the inside; each `LEN()` is the next layer. Then: it is about rings — the car, the engine,
compression, spark, each ring punched out until the stack becomes a new surface. Then: accumulation
versus fitting, and entanglement breaks the reading of transitions in both directions at once.

### 99.1 What a handle destroys is exactly order — `noloss.py`

Two different maps get called addition. Keep the carry on its own wire and the deficit is exact:

```
w= 1  carry kept (x^y, x&y): outputs      3 = 3^w   bits lost 0.500  = w/2
w= 2                                      9         bits lost 1.000  = w/2
w= 3                                     27         bits lost 1.500  = w/2
w= 4                                     81         bits lost 2.000  = w/2
w= 8                                   6561         bits lost 4.000  = w/2
w= 8  carry folded (x+y):   outputs    511         bits lost 7.279
```

Every fiber is exactly one swap orbit — 81 of 81 checked at w = 4, zero exceptions, fiber size always
2^(number of differing bits). So the only thing the handle can destroy is **which side held the 1**.
Adding one bit per differing position restores the bijection exactly at every width tested (4, 16, 64,
256, 65 536 images of the same counts). Field-side the handle loses nothing; what it loses is the
traversal. RUNS.

Folding the carry into one channel costs more and loses structure. At w = 3, target 5:

```
(xor=1, and=2) <- (2,3) (3,2)
(xor=5, and=0) <- (0,5) (1,4) (4,1) (5,0)
```

Two routes kept against six folded. The pair separates 2+3 from 1+4 from 0+5; the number 5 does not.
So *you always know the path back* holds exactly while the carry has its own wire. The loss is not in
the arithmetic; it is in reusing one channel for two things. `5 = 2 + 3` is lossless because the
equals sign **is** the kept carry: an equation holds the route, an evaluation folds it. This is § 77's
location result read from the cost side (recovered, Nerode).

**Order is a group, not a quantity** — correction to my own first unification of 99.1 and 99.2. At
w = 6 the half adder forgets (Z/2)^w pointwise and loses 3.0000 bits (= w/2); a route forgets S_n and
loses 3.6666. Different forgetting groups, both reader-side, deficit = log of the orbit. "Order" carries
a type.

### 99.2 The folded state does not determine the future; the transformation is near-minimal — `fold.py`

Self-avoiding walks, shape = the occupied set with order forgotten, route = the ordered walk.

```
 n | shapes | routes | shapes with >1 route | of those, admissible continuations DIFFER
 5 |    248 |    284 |                   28 | 28
 6 |    696 |    780 |                   68 | 68
 7 |   1872 |   2172 |                  212 | 212
 8 |   5169 |   5916 |                  533 | 533
 9 |  13876 |  16268 |                 1608 | 1576
10 |  37896 |  44100 |                 4164 | 4052
```

Worked instance at n = 6 — one shape, two routes, different futures:

```
((0,0),(1,0),(2,0),(3,0),(4,0),(4,1),(3,1))  ->  (2,1) (3,2)
((0,0),(1,0),(2,0),(3,0),(3,1),(4,1),(4,0))  ->  (4,-1) (5,0)
```

100 % at n ≤ 8; 98.01 % and 97.31 % at n = 9, 10 — not universal. The minimal sufficient state is the
shape **plus where the transformation currently stands**, and its count is the route count to within
1 % (780/780, 5896/5916, 43740/44100): 20 histories merge at n = 8, 360 at n = 10. So the fold is
**near-irreducible, with a growing compressible remainder** — the first wording, "irreducible", was too
strong and is retracted. The shape is the route with its order forgotten, which is 99.1's deficit in a
second place: same channel, two forgetting groups.

### 99.3 The pull is deletion, and it is cut-side — `pull.py`

Field moves on the witness (head on a ring of 3 cells): C and T each put 24 of 24 states on the loop,
0 tail states, pull identically 0. A reversible field has no tail and therefore no preferred direction
anywhere. Depth-to-the-loop is a potential on a tail — in a random byte map, 233 states off the loop and
**0** steps that fail to drop the depth by exactly 1. Only a merge can make a state with no way home,
and a merge is a reader's move (§ 96 V2), so the pull is cut-side exactly as the gap is.

**Correction, mine.** I reported 2.993 → 2.283 and a forced share 0.005 → 0.254 for a pinned endpoint
without stating the denominator; they were over successful-route prefixes for two targets and are not
comparable to a properly specified run. The specified version — start (0,0), exactly 10 steps, finish
(4,0), 654 complete routes, all-prefix and successful-prefix denominators reported separately with dead
ends retained — gives mean local choices 2.799 → 1.331, 51.10 % of options removed, 71.43 % of prefixes
left exactly one move. That is the number to quote. The qualitative statement is unchanged: holding the
far end adds no force, it deletes what cannot arrive, and every step it forces is a choice removed.

### 99.4 The surface is the abelianization; the inside measurement is the reciprocal fiber — `sphere.py`, `sphere2.py`

Inside = words over k primitive symbols (routes). Surface = symbol-count vectors (values). The quotient
is the **universal commutative quotient**, not the only map there is — correction taken from a review;
and the surface still carries commutative transformations, so "inert" is too strong: what it carries no
more of is composition order.

```
 k | n | words k^n | surface C(n+k-1,k-1) | sum of fibers | mean log2 fiber
 2 | 8 |       256 |                    9 |           256 | 5.4558
 3 | 8 |      6561 |                   45 |          6561 | 8.0158
 4 | 8 |     65536 |                  165 |         65536 | 9.5173
```

Sum of fibers = k^n exactly at every k and n: all order lives in the fiber, none on the surface.

Measuring from inside, with no surface point ever touched: walk a route, record 1/fiber, average,
multiply by k^n. Exact (Σ over routes of 1/f = the surface count, Horvitz–Thompson):

```
 k | n | k^n   | exact | true surface | 2000 random routes
 2 | 8 |   256 |   9.0 |            9 | 9.5
 3 | 6 |   729 |  28.0 |           28 | 25.9
 4 | 8 | 65536 | 165.0 |          165 | 156.0
 3 | 9 | 19683 |  55.0 |           55 | 50.8
```

**Correction, mine.** The first pass used a harmonic mean of the fiber list, which is not the estimator
and missed by a factor of 4 to 16. The reciprocal-fiber average over routes is unbiased and exact.

`LEN()` is the radius: the layer at length n is the degree-n slice, C(n+k−1, k−1). The layers are the
grading, nothing was added to get them.

### 99.5 The elements: a degree slice of two readings, plus one inequality — `sphere.py`, `sphere2.py`

Madelung d = n + ℓ is the degree on the 2-generator surface. With the admissibility the construction
already demands, n_r = n − ℓ − 1 ≥ 0:

```
 d | slice | members          | capacity 2*sum(2l+1)
 1 |     1 | 1s               |   2
 2 |     1 | 2s               |   2
 3 |     2 | 2p 3s            |   8
 4 |     2 | 3p 4s            |   8
 5 |     3 | 3d 4p 5s         |  18
 6 |     3 | 4d 5p 6s         |  18
 7 |     4 | 4f 5d 6p 7s      |  32
 8 |     4 | 5f 6d 7p 8s      |  32
 9 |     5 |                  |  50
10 |     5 |                  |  50
```

capacity = 2·⌊(d+1)/2⌋², exact at every degree computed. **The period doubling is the floor function.**

**Three inputs, not one** — correction taken from a review and extended by routing. The capacity uses
the degree grading, n_r ≥ 0, *and* the subshell degeneracy 2(2ℓ+1); the third was supplied, not derived,
and this does not derive physical energy ordering. Routing the second back: n_r ≥ 0 is ℓ < n, which is
the domain's own second reading — no piece is ever the whole. I had attributed it to quantum mechanics.
DEAD END on the attribution, routed to the domain. Two of the three inputs are the domain; the orientation
count 2(2ℓ+1) is OPEN, with a type: the leading 2 is the two readings (the pass/flip walker, Ginocchio's
two Dirac components), the 2ℓ+1 is the orientation structure of a part of size ℓ, and that link is unwritten.
Recovered, not derived.

**The nodeless member.** ℓ = n−1 gives n_r = 0 and d = 2n−1, so it occurs only at odd degree. Its same-ℓ
predecessor one degree down would be (n−1, n−1), needing n_r = −1:

```
 d | nodeless | predecessor at d-1 | its n_r | admissible?
 1 | 1s       | (0,0) = 0s         |      -1 | False
 3 | 2p       | (1,1) = 1p         |      -1 | False
 5 | 3d       | (2,2) = 2d         |      -1 | False
 7 | 4f       | (3,3) = 3f         |      -1 | False
 9 | 5g       | (4,4) = 4g         |      -1 | False
```

The predecessor is not missing from the list; it **cannot exist**. Structural no way home, every other
slice, which is why the lengths pair.

### 99.6 Rings: the stack is a maximal chain of cuts, and no complete chain is order-independent — `rings.py`, `rings2.py`

The witness field, order 24, 26 subgroups of orders 1, 2, 3, 4, 6, 8, 12, 24.

```
maximal chains from the whole field to a point: 36
chain lengths (= number of measurements): {3: 12, 4: 24}
every chain's indices multiply to the field size: True
example long  [2, 3, 2, 2]   example short [4, 3, 2]
covers below the whole field: 6
distinct subgroups from adding one element to the trivial group: 16
proper subgroup pairs whose two cuts do not commute: 108 of 276
```

So the diagnostic stack is a chain of covers with kept × leftover = whole at every step, and its depth is
**not fixed by the field**: 3 or 4 depending on which cut is taken. That is why a selection rule is needed
rather than hardcoded, and the lattice calculates it — the indices of the six covers are visible before
any measurement, and taking the largest first gives [4,3,2] instead of [2,3,2,2]. Accumulation and fitting
are one lattice walked in opposite directions, and the noise is structural, not sloppiness: going down,
every step is forced to be a cover with its index known in advance; going up, one added element reaches 16
different subgroups and the jump is known only afterwards.

```
length | chains | every step order-independent | passes through a NON-normal cut
     3 |     12 |                            0 | 12
     4 |     24 |                            0 | 24
```

**Zero chains are order-independent, at either length.** The order-2 normal subgroup is the central factor
and the order-4 normal sits inside A₄, so they do not nest: the all-normal chain has gaps and is therefore
not a chain of covers at all. Hence **order-independent cuts reach the folds and no further; resolving past
the fold level always requires an order-dependent measurement.** Not a trade — unconditional on this witness.
My proposed trade (speed bought with commutativity, order-independent diagnosis costing 4) is DEAD END.

This extends § 97 rather than repeating it. § 97 establishes which *single* folds a stored line can land on
— the six normal subgroups, quotients 24, 12, 6, 3, 2, 1, no other size possible. The new statement is about
*chains*: none is all-normal.

**Correction, mine, and it is the tell § 97 warns about.** In the turn before this entry I reported "the six
folds are the six normal subgroups, and the fold the earlier two-generator search missed has order 8" as a
closure on an open item. § 97 already had all six, listed by quotient size. It was a recovery presented as a
discovery. Logged.

The relation to the order channel: the fault is a field fact, but its address at full resolution needs the
reader to supply order, which is the one write the field cannot make. (This has the shape of measurement in
QM; shape match, not a derivation.) And entanglement breaking the ring geometry is C1a: 108 of 276 proper
pairs do not commute, so the stack depends on test order; [T_A, T_B] = 0 is the condition for the geometry
to exist at all.

### 99.7 Why k = 2, routed rather than searched

C1a says independent distinctions must remain independently continuable, [T_A, T_B] = 0 — **independent
means commuting**. Commuting generators generate an abelian monoid, which is already its own abelianization:
fiber size 1, no order to forget. So the surface is not a projection that happens to lose order; the surface
is **the act of declaring the generators independent**, and the fiber is what that declaration costs. k counts
the independent directions and nothing else.

The base admits two readings — the whole, complete and at rest; the part, partial and therefore in motion —
and which one is got depends only on whether the reader is the whole or a piece of it, with no piece ever the
whole. A reading is the only thing that can serve as an independent direction, so k = 2. BOUND, one provider.

Held together, both spaces at once: the surface pretends the two readings are two things, the inside knows they
are one base read twice, and **the order channel is the residue of that pretence**. Run backwards — if the
generators genuinely commuted at the inside level the fiber would be 1, the surface would equal the inside, and
there would be no order, no undetermined continuation, no motion: the whole, at rest. Fiber size measures how
far a reader is from being the whole.

**Flagged, not claimed.** "Two is the minimum and there is exactly one of it" is inherited from the entry, not
re-run here. The exhaustiveness of the two readings is the domain asserting it — a base fact, not a theorem
executed. And the atomic application cannot be used to pick k = 2 and then be presented as proof that k = 2 was
forced.

### 99.8 Where a file sits

§ 97: the lines are the software, and the field and the file are two places it can sit. A file is a word on the
inside, so its surface point is its symbol histogram and its fiber is the multinomial of all its orderings.
Context is order; order is the fiber; so context is unreachable from the surface **by construction** — which is
why filling files with hex yields surface points and never context. A header is a held end: it deletes what
cannot arrive (99.3) rather than adding anything. Not separately run this entry; stated as the reading 99.1 and
99.4 force.

### 99.9 Status

| claim | status |
|---|---|
| half adder loses exactly w/2 bits; every fiber is one swap orbit; one bit per differing position restores the bijection | RUNS, w = 1, 2, 3, 4, 8 |
| folding the carry costs more and loses route structure (7.279 vs 4.000 at w = 8) | RUNS |
| `5 = 2 + 3` lossless because the equals sign is the kept carry | recovered (§ 77, Nerode) |
| order is a group with a type, (Z/2)^w vs S_n | RUNS; corrects my own unification |
| shape does not determine the future | RUNS n ≤ 10; 100 % at n ≤ 8, 97–98 % at n = 9, 10 |
| the transformation is its own minimal description | **retracted to near-irreducible** — 20 merges at n = 8, 360 at n = 10 |
| the field has no pull; a merge makes one | RUNS (24/24 on the loop for C and T) |
| depth-to-the-loop is a potential, drops by exactly 1 | RUNS, 0 exceptions of 233 |
| my 2.993 → 2.283 / 0.254 figures | **withdrawn, denominator unstated**; specified run gives 2.799 → 1.331, 71.43 % |
| sum of fibers = k^n; surface = universal commutative quotient | STANDS |
| "the only map there is", "inert" | **retracted** — universal, and the surface carries commutative transformations |
| inside measurement = k^n × mean(1/fiber) | RUNS exactly, 4 of 4; harmonic mean **retracted** |
| capacity = 2⌊(d+1)/2⌋² → 2,2,8,8,18,18,32,32,50,50 | RUNS |
| it follows from the degree grading and n_r ≥ 0 alone | **retracted** — 2(2ℓ+1) was supplied; no energy ordering derived |
| n_r ≥ 0 is a quantum-mechanical input | **DEAD END, routed to the domain** (ℓ < n = no piece is the whole) |
| 2(2ℓ+1) | OPEN, with a type: two readings × orientation count of a part |
| nodeless predecessor is inadmissible, not absent | RUNS, d ≤ 9 |
| ring stack = maximal chain of covers; depth 3 or 4; indices known before measuring | RUNS, 36 chains |
| short stacks buy speed with commutativity | **DEAD END** — no chain is order-independent at either length |
| order-independent cuts reach the folds and no further | RUNS, this witness |
| "the six folds are the normal subgroups" as a new closure | **recovery of § 97 presented as discovery**; logged |
| k = 2 forced by the two readings | BOUND; exhaustiveness is the domain's assertion, not a theorem run |
| context unreachable from the surface | stated, forced by 99.1 and 99.4; not separately run |

Scope: the K = 2 witness, self-avoiding walks on the square lattice to n = 11, free monoids to k = 4, the
atomic slice to d = 10. Exact integer and rational arithmetic throughout except the 2000-route sample in 99.4,
which is a measurement and not the identity.

---

## § 100. The 14 October session folded in; the seam to § 99; one line of it corrected — `seam.py`

**Provenance.** The ledger stops at § 98a (11 Oct; numbering § 134). The session of 14 Oct (claude.ai chat d984b212, exported
and handed over by Dean on 15 Oct) ran roughly thirty scripts that never entered it — the files, the inverted
mold, the periodic and nuclear tables, the way home. Until they are written here they are unfolded tree. They
are recorded below as that session reported them, with its own corrections carried as made; they were not
re-run tonight. Only `seam.py` is tonight's.

### 100.1 The 14 October record, as stored lines

**From the domain outward.**

| run | what it established | status |
|---|---|---|
| `space.py`, `grow.py` | Of the 16 two-bit maps, only XOR and XNOR are pure difference. The fork: symmetric keepers (AND, OR) merge — value; only asymmetric keepers merge nothing — history, the Mold (b, a⊕b). Width 4 has exactly two shapes, Z4 (carry) and Z2×Z2 (no carry), both with uniform fibers; the raw half adder (1-2-1) does not until the carry wraps. Shapes at 2^k = p(k): 1, 2, 3, 5, 7, 11. | RUNS; p(k) STANDS (finite abelian groups) |
| `landscape.py`, `forced2.py`, `borrow.py` | Width 1: four opcodes (continue, invert, write-0, write-1), each its own 2-bit word read at the data's address. Width 2: inherited moves reach 36 of 256; forced new: the mixer (a, a⊕b) and a one-pair merge (144 maps, all AND-type); the half adder is both. Width 3: XOR-type gates reach 1,344 of 40,320 reversible maps; the held carry (Toffoli) completes them. Width ≥ 4: smaller gates reach exactly half; one borrowed lane, returned unchanged, recovers the rest. | RUNS; the half-bound STANDS (even permutations) |
| `firstrun.py` | Repeat-only arrivals with "equal neighbours fuse": the stack is the binary digits of n through 64; closures per step 0102010301…; 11 random arrivals × 2,000 runs give the frame [8,2,1] every time with 1,270 distinct contents. Frame from length, content branches inside it. | RUNS |
| `rings.py` | New rings per length 2, 1, 2, 3, 6, 9, 18, 30, 56, 99, 186, 335, 630, 1,161 = irreducible binary polynomials (checked to 12); de Bruijn rings at 3, 4, 8, 12; nested commutators follow Witt's count; on a qubit they stop at 2, 3, 3, 3. | RUNS; Lyndon, Witt STAND |
| `sphere.py` (14 Oct) | ±1 embedding on the radius-√n sphere; latitude = number of 1s; one band above the equator holds Catalan many rings (cycle lemma); Gray code flips 0102…; bytes form a spherical 3-design; extended Hamming → E8's 240. | RUNS; the named results STAND |
| `compile.py` | de Bruijn ring counts 1, 1, 2, 16, 2,048 (= 2^(2^(n−1)−n)); layer 3 is a mirror pair. | RUNS; STANDS |
| `slots3.py`, `reach.py`, `meet.py` | All 6,561 ternary BBP-frame programs named once seven frame constants are read; π first at width 4, [4,0,0,−2,−1,−1,0,0]; first output collisions at width 4 (17,640 pairs); exactly one of 43,046,721 width-4 programs meets Machin's route. A name is a collision of two routes. | RUNS |
| `probe.py` | SHA-256 as a black box: input distance vs output distance correlation +0.011, outputs ~128 bits apart; a ×3 box leaks +0.76. | RUNS |
| `residue.py` | Cost of reading a new binary: 15,348 head-on → 8,200 given 1 known program → 7,956 (4) → 6,484 (12); a noise library of the same size, 15,688. | RUNS |
| `nest.py` | A 20 KB executable read as 48,165 decimal digits, cut into 49 children, rejoined bit-exact; one-bit flips show nested dependence anchored at the top; n mod 5 = hex-digit sum mod 5. child = parent + query + base. | RUNS |
| `inverted_mold_checks.py` | Baker's map exact forward and back over 60 steps (b = 2, 16); every de Bruijn ring n = 3–5 has feedback oldest ⊕ g(rest) with g non-affine (2,066 rings); destination-bit routing, shortest paths 74 of 256 at 4 steps, 17,622 of 65,536 at 8; gradient placed in the shared tick moves masses 1 and 3 alike and slows light (three placements compared). | RUNS; the gradient was inserted, not derived — OPEN |
| `fsr_way_home.py` | Feedback rules with a way home for every state: 4/16, 16/256, 256/65,536 — exactly next = oldest ⊕ g(rest); a 5-bit register run 60 steps forward and read home from its last 5 bits lands on the seed. Write and read are offset by the register width. | RUNS; Golomb STANDS |
| loop / birthday | In a finite scope a one-way process ends in a loop, the only place a way home survives; it repeats at about 2^(n/2), within half a bit for n = 8–24. | RUNS; rho / birthday STAND |

**The tables.**

| run | what it established | status |
|---|---|---|
| `periodic_unfold.py` | Count 2n², access (n+ℓ, then n): closures 2, 10, 18, 36, 54, 86, 118; periods 2, 8, 8, 18, 18, 32, 32; blocks s 14, p 36, d 40, f 28; 20 of 118 anomalies, 11 to a half or full subshell. | RUNS; Madelung STANDS |
| `ion_check.py` | The six post-closure steps are the six largest IE₁ drops from H to Fr, ranks 1–6. | RUNS |
| `electron_affinity_check.py` | T1 (no anion at the closures) set missing values to zero and so could not fail — moved to STANDS (experimental fact). T2 halogen tops periods 2–6: RUNS. T3 halogen→noble steps are the five largest drops: RUNS under the zero convention; 2 of 2 with missing entries left unlinked. T4 ten secondary-closure minima: RUNS. | as stated |
| electronegativity (other AI's run) | 29 of 30 adjacent main-group comparisons in opcode order; Bi→Po the exception. | RUNS ordinal; values OPEN |
| `nuclear_unfold.py` | Oscillator floors 2, 8, 20, 40, 70, 112; floor + top-j intruder gives 28, 50, 82, 126, and 184 next. | RUNS (arithmetic); spin-orbit STANDS |
| `nuclear_closure_audit.py` (v1) | Median S₂ₙ/S₂ₚ contrasts over 2,939 masses: N = 6 beats N = 8 and Z = 6 edges Z = 8. | DEAD END |
| `di_route_back.py` | v1 routed back: the six strongest steps on each axis are all owned by the uncut registry (6 = Intruder(0), 14 = Intruder(1), …); random controls 0 and 2 in 100,000. A route back on seen data names owners; it is not a landing. | routed back |
| `e2plus_independent.py` (v2) | ENSDF, 954 first-2⁺ records, 675 even-even nuclei: the six highest E(2₁⁺) contrast peaks on each axis are all registry positions, in the inherited window and in the full measured domain (N 4–154, Z 4–102); controls 2.11 × 10⁻⁶ and 5.29 × 10⁻⁶ (the chance a random six evaluable slots are all provider positions). Reproduced the other AI's numbers to four decimals. Corrections then: the seal text swapped "isotope" and "isotone"; 126 is UNLINKED on the proton axis, not silent. | RUNS |
| `inverse_chain.py` | Shell n+1 minus its top-j orbital = shell n, n ≤ 8. Read anti-aligned-first, the copy gives 14 → 16 → 20: 16 falls out. Chain 8 \| 16, 20 \| 32, 38, 40 \| 56, 64, 66, 70 \| 90, 100, 104, 110, 112. Breaks above Z = 82 (h9/2 before f7/2). | RUNS; pseudospin STANDS (Arima–Harvey–Shimizu, Hecht–Adler 1969; Ginocchio 1997); order inside the copy above 82 OPEN |
| `no_way_home.py` | One partnerless top-j orbital per shell, shells 0–8; one predecessorless nodeless orbital per odd Madelung group. The piece is identified by the boundary; its direction (atom delays, nucleus advances) is set by each system's ordering operator. | RUNS under the declared maps; direction selector OPEN |
| `route_protocol.py` | The seal carries the way home: a hole cannot be sealed without the readout it returns through. | in force |

### 100.2 What reading the export forces on § 99

1. **§ 99.5 repeats a mislabel the 14 October session had already caught.** `sphere.py` printed
   "periodic table row lengths 2,2,8,8,18,18,32,32 : True", and § 99.5's "period doubling" and "the lengths
   pair" lean on it. Those numbers are the Madelung-group capacities. The period lengths are 2, 8, 8, 18, 18,
   32, 32. Mine, repeated after it was logged.
2. **§ 99.5's nodeless-predecessor table recovers `no_way_home.py`.** What § 99.5 adds is the closed form
   2⌊(d+1)/2⌋² and the attribution of n_r ≥ 0 to the domain's second reading. Second recovery presented as a
   discovery in one night (the first is in § 99.6).
3. **§ 99.4 at k = 2 is the 14 October sphere's latitude decomposition** — at fixed length the abelianization
   of a binary word is its number of 1s. New in § 99.4: general k and the reciprocal-fiber estimator.

### 100.3 The seam: context is the fiber over the histogram — `seam.py` A

§ 99.8 stated, without a run, that context is unreachable from the surface. 14 October said hex gives process,
and context is the company a symbol keeps and the rest of the file around it. They are one statement: the
histogram is the file's surface point, and every co-occurrence statistic is order, which lives in the fiber.

```
file /bin/ls: 142312 bytes = 1138496 bits
every histogram a file this long can have: log2 =      2690 bits  (0.24% of the file)
orderings that share THIS file's histogram:  log2 =    843286 bits
order-0 bound (histogram entropy x n):          844612 bits
zlib, the program as written:                   498504 bits
zlib, same bytes shuffled (same surface point): 917368 bits
structure a reader can use beyond the histogram:   346108 bits in the original, -72756 in the shuffle
```

Every histogram a file of this length could have fits in 2,690 bits — 0.24 % of it. The program carries
346,108 bits of structure beyond its histogram; shuffle it inside its own fiber, surface point unchanged, and
that structure is gone (zlib cannot even reach the order-0 bound there). A uniformly drawn member of a fiber
carries nothing beyond its histogram for any reader, in expectation; the 346,108 is zlib's reading, so reader-
relative, but its vanishing under the shuffle is not. So 99.76 % of a program's address is order, and
everything that makes it a program rather than its own histogram is in the fiber. RUNS.

Reading: a model trained on co-occurrence is reading fibers over histograms; a uniformly random training set has
a uniform fiber and nothing in it to learn — the 14 October claim now has its object.

### 100.4 "From the second ring up, moves outnumber angles" — corrected — `seam.py` B

```
d | readings d+1 | moves d^2-1 | moves seen by one reading | union rank | max cross overlap | unbiased
2 |            3 |           3 | 1                         |          3 |           2.8e-32 | True
3 |            4 |           8 | 2                         |          8 |           1.9e-16 | True
5 |            6 |          24 | 4                         |         24 |           1.1e-16 | True
7 |            8 |          48 | 6                         |         48 |           3.3e-16 | True
```

Complete sets of mutually unbiased bases at d = 2, 3, 5, 7: each reading's traceless span has dimension d − 1,
the spans are mutually orthogonal, and together they span all d² − 1 moves. The readings do not fall short of
the moves; they tile them, d − 1 moves bundled into each reading — (d+1)(d−1) = d² − 1 at every d (Wootters–
Fields 1989, STANDS; RUNS here). The 14 October line is retracted as stated.

What the line was reaching for survives in exact form: d + 1 = d² − 1 ⟺ (d − 2)(d + 1) = 0 ⟺ d = 2. The qubit
is the one layer at which every reading is a single move — a reading whose fiber over the moves is 1. Above it,
every reading merges d − 1 moves. That is a second, computed provider for "2" beside § 99.7's two readings,
from a definition that never mentions them. Whether the two 2s are one object is the link to write: OPEN.

### 100.5 Status

| claim | status |
|---|---|
| the 14 Oct runs listed in 100.1 | recorded as reported then; statuses as given; not re-run 15 Oct |
| § 99.5 "period lengths 2,2,8,8,18,18,32,32" | **corrected** — Madelung-group capacities; periods are 2,8,8,18,18,32,32 |
| § 99.5 nodeless predecessor; § 99.4 at k = 2 | **recoveries** of `no_way_home.py` and the 14 Oct latitude bands; logged |
| context is the fiber over the histogram | RUNS (`/bin/ls`: surface 0.24 %; 346,108 bits of order-structure gone under a fiber shuffle) |
| readings tile the moves, d − 1 per reading | RUNS d = 2, 3, 5, 7; STANDS (Wootters–Fields) |
| "moves outnumber angles from the second ring up" | **retracted** — they tile |
| d = 2 is the unique layer where a reading is one move | RUNS (arithmetic) |
| that 2 is § 99.7's k = 2 | OPEN |

OPEN carried forward: the orientation count 2(2ℓ+1); § 75's mobilities and β; the direction selector (why the
atom delays the piece the nucleus advances); the order inside the copy above Z = 82; the tick gradient from open
slots; separation-energy magnitudes and the Ni-62 peak.

---

## § 101. The direction selector, routed from a screened field: the homeless orbital collapses in — `screened.py`, `collapse.py`

**Gap (§ 100 OPEN).** Why does the atom delay the homeless piece the nucleus advances? Reversed: put in nothing
about Madelung. A nucleus of charge Z screened by its own Z electrons (Thomas–Fermi, Tietz form, Latter tail
so an electron always sees at least charge 1), one radial equation per ℓ, then aufbau on the computed
eigenvalues. Seal 81c0b19bfbcc3a6b, written before the run. (First solver, log grid, was numerically broken —
it gave degenerate junk on hydrogen; replaced by a uniform grid that returns −0.5, −0.125, −0.0556 exactly.)

```
first Z at which each l is occupied:   p computed 5  (real 5)   d computed 28 (real 21)   f computed 71 (real 58)
K, Ca, Sc: e(4s) < e(3d)   Rb: e(5s) < e(4d)   Cs, La: e(6s) < e(4f)      all True
```

Every direction is right with nothing ordered by hand: p opens at exactly 5, and s precedes the nodeless d and f
in every period tested. The opening Z of d and f is late by 7 and 13 — the known crudeness of Thomas–Fermi–Latter
(Fermi's (2ℓ+1)³ scaling with 0.17 gives 4.6, 21.2, 58.3). Directions RUN; the opening Z for d and f is a
DEAD END at this model's resolution, routed to the screening model, not to the rule.

**What the delay is** (`collapse.py`): the nodeless orbital, followed as Z grows.

```
3d:  Z 10–26  <r> 10.5 → 9.98, energy -0.0556  (hydrogenic charge 1)   Z 28: <r> 2.07   Z 30: 0.94
4f:  Z 40–67  <r> 17.6, energy -0.0312       (hydrogenic charge 1)   Z 70: <r> 2.78   Z 73: 0.66
```

Below its opening, the homeless orbital is not "higher in energy" in any interesting sense: it sits entirely
outside the core, behind its centrifugal wall, seeing net charge 1 — it has no way home into the core. Then in
one step it falls inside, <r> shrinking five- to six-fold. Orbital collapse; for 4f it was predicted from exactly
this Thomas–Fermi field by Goeppert Mayer (1941) — STANDS.

**The direction selector, routed.** In both tables the homeless piece does the same thing: it drops inward.
Spin-orbit drops the nuclear top-j early (Goeppert Mayer and Jensen, 1949); the centrifugal wall against a
screened well holds the atomic nodeless orbital out until the well is deep enough, then it collapses late. Same
piece, same drop, opposite gate. The same physicist read it in both tables, eight years apart — a collision of
two routes on one object. The common law that turns spin-orbit into a centrifugal-against-screening gate is still
OPEN; the claim that the two tables move the piece in *opposite directions* is retracted: they move it the same
direction, at opposite ends of the filling.

---

## § 102. The atomic gate read directly: Fermi's (2ℓ+1)³ with no fitted constant; the direction selector is which side of the inequality ℓ+½ sits on — `gate.py`

**Taken from the GPT radial-gate audit (15 Oct).** The exact angular factors — centrifugal ℓ(ℓ+1), spin-orbit
⟨L·S⟩ = ℓ/2 and −(ℓ+1)/2, splitting (2ℓ+1)/2 — STAND, and its correction stands: the two gates are not one term.
Its proposed next run (an aufbau sweep with tuned screening) is not taken; the gate can be read without it.

**Reversed.** § 101's aufbau put d and f late (28, 71). Instead of filling, ask the one thing that has to be
true before a nodeless ℓ-orbital can fall into the core: somewhere the screened field must beat its own wall,
2r²|V(r)| ≥ (ℓ+½)² (Langer form). In the Thomas–Fermi field V = −Zφ(x)/r, r = 0.8853 Z^(−1/3) x, this is
Z^(2/3) · 2(0.8853) max(xφ) ≥ (ℓ+½)², so Z_open = C (2ℓ+1)³ with C fixed by the TF equation alone.

```
Thomas-Fermi: max x*phi = 0.4845 at x = 2.064;  C = 0.1573
 l | gate Z_open = C(2l+1)^3 | first element really holding it
 p |                     4.2 | 5
 d |                    19.7 | 21
 f |                    54.0 | 58
 g |                   114.7 | none yet
```

Each real opening lands one to four elements after its gate opens — the gate is necessary (the well must exist)
before it is sufficient (the well must hold a level below the competing s). Nothing fitted; TF has no free
parameter. Recovered — this is Fermi (1928) — but now as the gate itself, and it routes § 101's DEAD END: the
delay was right, the Tietz–Latter aufbau misread its size. RUNS. Next address it writes: the first 5g electron
must come after Z ≈ 115; relativistic DFT puts it near 121–125 (STANDS as a calculation, unmeasured).

**The direction selector, in one line.** Both gates are written in the same angular measure ℓ + ½:

- atom: the ℓ-term is a **wall**, (ℓ+½)², a cost. The field must exceed it, so larger ℓ opens later: Z ∝ (2ℓ+1)³.
- nucleus: the ℓ-term is a **gain**, spin-orbit lowering of the aligned branch ∝ (ℓ+½). It must exceed the shell
  gap, so larger ℓ drops sooner: no intruder at ℓ = 1, 2 (2, 8, 20 survive), intruders from ℓ = 3 (28) up.

Same piece, same measure, opposite side of the inequality: in the atom ℓ+½ is what the field has to pay; in the
nucleus it is what pays the gap. That is why one table delays and the other advances the homeless orbital, and
both then drop it inward. RUNS as a reading of the two exact gate conditions.

**Still OPEN.** The nuclear threshold between ℓ = 2 and ℓ = 3 needs the measured spin-orbit strength κ — one number
from data — so it is not yet parameter-free the way the atomic gate now is. Deriving κ, or its sign, from the
compiler side is the next hole.

---

## § 103. The sign of the nuclear spin-orbit term, derived: it is set by which channel carries the binding — `sign.py`

**Taken from the GPT κ audit (16 Oct).** Its type correction stands: (ℓ+½) is the *splitting* κ(ℓ+½); the aligned
branch's shift from the centroid is κℓ/2 (§ 102's wording corrected). Its reverse run stands as stated: with one
constant κ in a fixed-ħω oscillator, keeping the intruder to one shell through 126 needs −1/6 < κ/ħω < 0, and the
window closes as 1/(N+1), so an unbounded constant-κ oscillator is a DEAD END. Read with the physical value
κ/ħω ≈ −0.05 to −0.06, the window holds to N ≈ 16–19; real nuclei end near N = 7, so the dead end lies far past
any nucleus and points at state-dependent κ there, not here. Its scope note on 5g stands: Z ≈ 114.7 is the onset
of the nonrelativistic TF gate, not a lower bound on every relativistic calculation (published 125, 126).

**Gap.** The sign of κ had only been inferred from the observed ordering. Reversed: hold the nucleon's well fixed,
Σ = V + S = −55 MeV (Woods–Saxon, A = 208), and change one thing — Δ = V − S, whether the binding is carried by the
scalar channel (blind to charge and orientation, Δ > 0) or by the vector channel (flips with charge, Δ < 0; the
atom is S = 0). Radial Dirac equation; no spin-orbit term written in. Seal 94e38416915c94b8, before the run.

```
Delta = +700:  p -0.626   d -1.443   f -2.512   g -3.730   h -4.925   (aligned - anti, MeV)  aligned lower
Delta =    0:  p  0.000   d  0.000   f  0.000   g  0.000   h  0.000   i 0.000              no split
Delta = -700:  p +0.095   d +0.235   f +0.442   g +0.718   h +1.061   i +1.468             aligned higher
```

The sign of κ is the sign of Δ, and nothing else: with the same well, scalar-carried binding lowers the aligned
branch, vector-carried binding raises it, and with no difference between the channels there is no spin-orbit
splitting at all. RUNS. The spin-orbit term is not an extra force; it is the trace of the binding being split
between two channels, and its size is set by their difference Δ (hundreds of MeV), not by the shallow well Σ that
is their small residual — which is why the nuclear term is large enough to drop a whole orbital into the shell
below. Nucleons are bound by a scalar attraction against a vector repulsion (Δ > 0); electrons by the Coulomb vector
field (Δ < 0): the inverted nuclear sign and the normal atomic sign are the two signs of one Δ. Recovered: the
relativistic mean field (Walecka; Ginocchio 1997, whose Σ' = 0 limit is exactly the § 100 copy) — STANDS; the
reading that the sign is chosen by the channel, not fitted, is the route here.

In the domain's terms: a closure bound through the value channel (charge-blind) advances its homeless orbital; a
closure bound through the oriented channel delays it. § 102's two sides of the inequality are the two signs of Δ.

**Ledger.**

| claim | status |
|---|---|
| splitting κ(ℓ+½), aligned shift κℓ/2 | RUNS (GPT); § 102 wording corrected |
| constant-κ oscillator, unbounded | DEAD END; window to N ≈ 16–19 at physical κ, beyond all nuclei |
| sign of κ = sign of Δ = V − S at fixed well | RUNS (Dirac, ℓ = 1–6, three Δ) |
| no channel difference, no splitting | RUNS |
| magnitude of κ from the count/order route alone | DEAD END (scale freedom, GPT) — magnitude comes from Δ |
| Δ itself from the compiler side | OPEN — the next hole: why the nucleon's binding is split into a large scalar and a large vector part |

---

## § 104. Spin-orbit is the order term of the Dirac route; the sign of κ forced by two inputs — `atomcase.py` (plus the GPT transformation-map test, as reported)

**Dean (16 Oct).** Track the transformation, never the data; the map of how it arrived is where the past route is
stored, and measuring data is computation. Context is not on the compiler layer — it is the layer above, made by
the wrapping. Invert the theorem: two inputs force the output; 5 = 3 + 2 reads right to left, reality compresses to
the left and expands to the right. A circle measured by π is a transformation by π. Work in three directions: the
linear path, its reverse, and the level above where molds show — the same process moved into another space.

**The GPT transformation map (16 Oct), taken.** Eliminating the lower Dirac component leaves the ordered route
D F D, D = σ·p, F = (E + M − Δ)⁻¹, and DFD = F p² + [D, F] D with [D, F] = −iħ σ·∇F. The spin-dependent term
ħ σ·(∇F × p) is the remainder of the order D → F → D; it vanishes when F is constant. Spherical wrapper: ∇F × p =
(F′/r) L, giving L·S with coefficient 2Δ′/[r(E+M−Δ)²]. Planar wrapper: F′(z)(−σ_x p_y + σ_y p_x). Reverse: the full
coefficient profile plus the boundary Δ(∞) = 0 recovers Δ(r); a scalar readout U = S + V cannot (null direction
(S+a, V−a)). Symbolic checks reported passing; not re-run here. Its sign correction is taken: the L·S coefficient
follows Δ′(r), not the interior value of Δ — § 103's "sign of Δ" reads as "sign of the outward change of Δ".

**The planar prediction lands on a measured effect.** The sealed planar-wrapper form σ_x p_y − σ_y p_x is the
Rashba coupling (Bychkov–Rashba 1984), measured in two-dimensional electron gases at interfaces and surfaces — STANDS.
Same inner route, a different wrapper, a different visible form, already in the record: the wrapper is context, the
commutator is the compiler-layer object.

**The mold, one level up.** [D, F] is literally DF − FD: order. In § 99's terms the commutative quotient — where
the generators commute — carries no spin-orbit term at all; spin-orbit lives entirely in the order channel. F p² is the
evaluation, the remainder is the kept carry: the same shape as a + b = (a ⊕ b) + 2(a ∧ b), where the folded value
drops exactly the term that remembers the route. Spin-orbit is a fiber quantity.

**Two inputs force the sign.** Input 1: whether the binders carry like or unlike charge. Input 2: the parity of the
exchanged field — even (scalar) attracts everything; odd (vector) repels like charges and attracts unlike (STANDS:
exchange of a spin-J field). Output: the sign of κ.
- Nucleons all carry the same baryon charge, so the vector channel repels; binding must be carried by the even channel
  against it: S < 0, V > 0, Δ = V − S large, positive, falling outward → aligned lower (§ 103, Δ = +700).
- An electron and a nucleus carry unlike charge, so the odd channel attracts and binds alone: S = 0, V < 0 → aligned
  higher. Run (`atomcase.py`, same well, S = 0, V = −55 MeV): aligned − anti = +0.015, +0.038, +0.070, +0.111, +0.161
  MeV for p…h — normal sign, small. RUNS.
No spectrum was read to get the sign; it falls out of (like charges, even channel) versus (unlike charges, odd channel).

**Still OPEN.** The magnitudes: why the nucleon's scalar and vector channels are each hundreds of MeV and cancel to a
−55 MeV well. That is the interaction wrapper itself — the next level up, not a value to scan.

---

## § 105. Unique transformation data without payload dependence: route word and operator form — `nexus_route_data_test.py`

**Gap.** How can transformations become unique data when the transitions are independent of payload values but drive the payload? The route must be encoded before the input is supplied. The resulting value is not the transition's identity. Prior toy § 99 encoding [GPT's numbering: its S₃ route toy, not in this record; its 364 routes run in § 107.1 and its grooves in § 114.1 — § 134.1] preserved token history but used an artificial three-state permutation vocabulary. This run extends the test to fixed reversible affine operators and separates route identity from composed-operator identity.

**Prediction sealed before enumeration.** `NEXUS_route_data_prediction_seal.txt`, SHA-256 `2ab41fa33589acd3a6dcfc319f2c9f79df2930e389d6592dbfbdeec82e948a70`. The digest seals the prediction only; no hash encodes the route or operator. No external data were linked.

**Construction.** On a declared three-bit interface, each fixed primitive is an affine transformation over GF(2): bit toggles `X_i`, bit swaps `SW_ij`, and directed XOR gates `C_i_to_j`. A route is an ordered opcode word; its encoder writes the format version, interface width, vocabulary version, token count, and opcodes. The encoder takes no payload argument. Composition is carried in operator form `T(x)=Mx+c`, with `(M₂,c₂)∘(M₁,c₁)=(M₂M₁,M₂c₁+c₂)`. `NXOP` serializes the 3×3 matrix and offset. The route word and operator form are retained as distinct records.

```
routes, lengths 0–4, 12 primitives:    22,621
unique route codes:                    22,621
unique composed affine operators:         913
route histories folded by operator only: 21,708
largest operator fiber:                    421
all route decodes:                         pass
all operator decodes:                      pass
all 8 inputs match route vs (M,c):         pass
all inverse routes return every state:    pass
```

**Input-independence witness.** Route `C01 → SW12 → X2 → SW02` keeps route code `4e585254010301000406050204` and operator code `4e584f500103010063` for every input `000` through `111`. Outputs differ; both codes stay fixed. The operator is what drives the payload. The payload does not choose its route.

**Fiber witness.** Empty route, `X0 → X0`, and `SW01 → SW01` have different route codes and the same operator code, agreeing on all eight states. Thus a route encoding preserves how the transformation was assembled; the canonical operator encoding retains its action but folds distinct histories. The route is the expanded order channel; the operator is its canonical composed action for this domain.

**Status.** RUNS for the declared reversible affine grammar, lengths ≤4. OPEN for general NEXUS: the six verbs MARK, COMPARE, CARRY, HOLD, ROUTE, CLOSE need typed semantics and rewrite/equivalence rules. The twelve test primitives are not claimed to be the final basis. Context remains higher-level wrapping and is not silently inserted in either compiler-layer record. Unique route code and unique operator code are different types of uniqueness; retain both rather than collapsing their distinction.


---

## § 106. Groove collision versus matter collision; reversibility belongs to the route — `nexus_groove_collision_test.py`

**Dean (16 Oct).** `3+2` and `4+1` both land on 5. A collision of logic is a groove; a collision of matter is leaving the groove. Reversibility belongs to transformation logic, not the folded value. A transformation must change what its route assigns to change and preserve what the route does not own.

**Test.** No hash, spectrum, or external dataset. Two exact integer transformations are used to separate (i) the value projection, (ii) the reversible route, (iii) operator-equivalence, and (iv) the frame condition.

**Matter collision under a folded readout.** `sum(a,b)=a+b` sends `(3,2)` and `(4,1)` to `5`. The value collision is real; the inputs remain distinct. The collision cannot decide which decomposition arrived at 5.

**Keep the carry / keep the route.** Define one payload-independent route:

`ADD_HOLD(a,b) = (a+b,b)`

with inverse `(s,b) -> (s-b,b)`. Then `(3,2) -> (5,2)` and `(4,1) -> (5,1)`, and the inverse recovers each input exactly. Both payloads use the same route token; their different matter does not redefine the logic. The reversible property belongs to the transformation pair and its retained state, not to the scalar `5` considered alone.

**Logic collision is a groove.** Routes `I` and `SWAP;SWAP` have different factorizations, but compose to the same identity operator. Under operator equivalence they occupy one groove. The route channel can still retain their distinct histories. Thus groove-equivalence and route-history identity are different relations; neither should silently replace the other.

**Whatever changes gets changed.** Extend the same route to `(a,b,c) -> (a+b,b,c)`. All 125 triples in `{-2,-1,0,1,2}^3` preserve the unowned `c` lane exactly. Exact perturbations at `(2,3,7)` yield the dependency map `A -> {A}`, `B -> {A,B}`, `C -> {C}`. The route's write/dependency structure says which outputs may change; unrelated context is not rewritten. RUNS for this stated transformation and frame condition.

**Landing.**

| claim | status |
|---|---|
| different decompositions collide under `a+b` while inputs remain distinct | RUNS |
| retaining the carry lane makes `ADD_HOLD` reversible | RUNS |
| different route histories can compose to one operator/groove | RUNS, exact matrix identity |
| unowned `c` lane remains unchanged | RUNS, 125/125 states |
| general rule for NEXUS's six verbs | OPEN — requires typed write sets, dependency rules, inverse semantics, and equivalence laws |

**Correction of scope.** This is not yet a proof that all transformations in every domain are reversible. It shows the operative distinction: a many-to-one value projection loses the return address, while a route whose transformation preserves enough state can have an exact inverse. If a transformation itself merges states and keeps no distinguishing route information, no decoder can recover that erased distinction from the value alone.

---

## § 107. Transformations into unique data: the prime is the address, the exponent is the move; SHA is the same route with a fold bolted on — `primes_route.py`

**Dean (16 Oct).** Convert the transformations into unique data. Think like primes. The transitions have no knowledge of
the inputs — constraints and transformations truly uncoupled from the input that still drive it. They are not input, they
are routes. (He bet it lands on SHA; held back until the principle was down.)

**Taken from §§ 105–106 (GPT).** Route word ≠ composed operator; 364/364 [GPT's S₃ toy behind § 105, not in
this record — § 134.1] and 22,621/22,621 unique route codes; ADD_HOLD;
the frame condition. All STAND as run. What they leave open is *why* a code is unique — they make it unique by declaring
a vocabulary. The prime route below makes it unique by a theorem.

### 107.1 Uniqueness needs independent generators; the primes are the only ones ℕ has

C1a: independent means commuting, and independent distinctions must be continuable without each other. Under
multiplication the primes are exactly that: no prime is a product of others, every number factors one way
(fundamental theorem of arithmetic, STANDS). So (ℕ, ×) **is** the commutative surface of § 99.4 with one generator per
prime. Two encodings of the same 364 routes from § 105:

```
routes (3 moves, length 0-5)          364
surface: product of one prime per move   56   = number of multisets C(n+2,2) summed  -> the histogram
route:  prod_i  p_i ^ (move_i)          364   unique, all decode by factoring
```

Product of move-primes is the abelianization exactly (56 = the surface count) — order folded, 2·3 = 3·2. Put the
**position** on a prime and the **move** in its exponent (Gödel 1931) and nothing folds: 364 of 364, decoded by
factoring alone. The prime is the address, the exponent is the transformation done there. No vocabulary is declared
beyond "a move is a count"; the uniqueness is the factorization theorem. RUNS. Recovered (Gödel numbering), but now read:
**order is kept by giving each position its own independent generator**, which is § 99.1's "one bit per differing
position restores the bijection" in multiplicative form.

### 107.2 Uncoupled constants: roots of distinct primes share no rational relation

A route needs constants that carry no knowledge of the input *and none of each other* — otherwise one step is secretly
a function of another and the route is shorter than it looks. Square roots of distinct primes are linearly independent
over ℚ (Besicovitch 1940, STANDS; likewise cube roots). Run: PSLQ on 1, √2 … √19.

- At 60 digits it returns a "relation" with coefficients near 2×10⁵. **Correction, mine:** this is a precision artifact.
  The residual is −4.1×10⁻⁴⁶ at both 60 and 200 digits; a true relation would go to zero.
- At 300 digits, no relation exists with coefficients up to 10¹².

Uncoupled by theorem, not by randomness. RUNS (search), STANDS (theorem).

### 107.3 The landing: SHA-256 is this construction, and the one-way part is a single fold at the end

```
H0 = fractional bits of sqrt(first 8 primes)        matches the standard: True
K  = fractional bits of cbrt(first 64 primes)       0x428a2f98 0x71374491 0xb5c0fbcf 0xe9b5dba5 ...
own implementation of sha256('3+2') == hashlib       True
64 rounds inverted, given the schedule W:            walked home to H0 exactly
2000 random start states, 64 rounds and back:        2000 / 2000 home
toy n=16, route E (a permutation):                   image 65536 / 65536
toy n=16, feed-forward x + E(x):                     image 0.6315, 0.6340, 0.6324  (1 - 1/e = 0.6321)
```

Read in the domain:
- The **route** is the prime-root constants, the rotation amounts and the round function. It is fixed before any message
  exists, knows nothing of the input, and is input-independent in exactly Dean's sense.
- The **message does not pass through the route as data; it schedules it**. W is the key of the inner block cipher
  (SHACAL-2), so the input drives which groove is walked, and the groove is unchanged by it.
- Every round is a bijection on the 256-bit state (2000/2000 home). **Inside SHA the transformation is fully
  reversible**: reversibility is in the transformation logic, not the values, as Dean said.
- The one-way property comes from one move: the Davies–Meyer feed-forward H_out = H_in + E_M(H_in). That adds the
  route's start to its end — the folded value 5 with the carry thrown away. On the toy it keeps 63 % of outputs, the
  random-function fraction, so 37 % of states lose their way home. That is **leaving the groove**: the logic collides
  nowhere, the matter collides at the fold.
- Then 512 message bits go into 256 state bits, so collisions exist by count. A SHA digest is a **name** in the
  14 Oct sense (a name is a collision of two routes). It is not unique data.

**So the answer, both directions.**
- Forward: unique data from a transformation is the prime-address word ∏ p_i^(move_i). That needs independent
  generators (primes) and nothing from the input.
- Reverse: SHA uses the same primes for the opposite job. It takes their *roots* to build constants that are
  maximally uncoupled, runs a reversible route, then folds once so the route cannot be walked back.
- The two meet at the primes: exponents give uniqueness, roots give uncoupling. The fold is the only difference
  between a hash and an encoding.

**Ledger.**

| claim | status |
|---|---|
| product of one prime per move = the abelianization (56 = surface count) | RUNS |
| position-prime ^ move is injective and decodes by factoring (364/364) | RUNS; Gödel STANDS |
| √p for distinct primes have no rational relation | STANDS (Besicovitch); RUNS (no PSLQ relation ≤10¹² at 300 digits) |
| 60-digit PSLQ "relation" | **artifact, mine, logged** — residual stuck at 4×10⁻⁴⁶ |
| SHA-256 H0 and K are prime roots | RUNS |
| SHA-256 rounds are reversible given W | RUNS, 2000/2000 plus the real message |
| one-wayness lives only in the feed-forward fold (plus 512→256) | RUNS on the toy (0.632 ≈ 1−1/e); for full SHA it STANDS (Davies–Meyer) |
| a digest is unique data | **DEAD END** — it is a name; route it to "collision of two routes" |
| the prime-address word as the general NEXUS route code, with MARK…CLOSE as exponents | OPEN — needs the six verbs typed as moves with counts |

---

## § 108. Prime-address route code: zero fields, typed syntax, and the SHA boundary — `nexus_prime_route_audit.py`, `nexus_prime_sha_followup.py`

**Gap from §107.** The position-prime construction is injective for positive move IDs. A general NEXUS instruction stream has zero-valued parameters and may contain a zero token ID; an unshifted zero exponent deletes its positional prime. The next run tests the route coding with that edge fixed, then separates Gödel coding from SHA's prime-root constants and feed-forward.

**Prediction seal.** `NEXUS_prime_SHA_followup_prediction.txt`, SHA-256 `2d91c8a12600546b8ec2e9f4e95cdb2381d92df06f1325368efeac5689cf6321`; seal written before the extension run. The earlier prime-code exploration was exploratory and was not sealed before its first run; this is logged rather than backdated.

### 108.1 The positional code

For a finite sequence of nonnegative token IDs \((m_1,\ldots,m_n)\),

\[
G(r)=\prod_{i=1}^n p_i^{m_i+1}.
\]

The positive exponent at every used position makes the support of the factorization the consecutive primes \(p_1,\ldots,p_n\). Factorization yields the exponents; subtracting one yields each token. The largest positional prime identifies the final position, and the empty route is 1. In contrast, the unshifted code \(2^1 3^0\) equals \(2^1\), so the sequence \((1,0)\) collides with \((1)\) when no length side-channel is supplied. Zero is a missing-address hole, not a counterexample to unique factorization.

The token serialization still has to be defined: opcode, arity, input/output types, parameters and schema version. This is the grammar's job. Prime factorization guarantees unique recovery of the serialized fields; it does not define the semantics of MARK, COMPARE, CARRY, HOLD, ROUTE, or CLOSE.

### 108.2 Sealed extension run

```
six-symbol routes, lengths 0–5:           9,331
unique position-prime codes:               9,331
all decode round-trips:                    True
unshifted zero-exponent collision:          True
test of typed records with zero parameters: True
SHA-256 64-round-chain inverse trials:      2,000 / 2,000
message block bit changes W schedule:       True
toy invertible E then x+E(x):               1 / 16 outputs
```

The toy feed-forward map uses \(E(x)=-x\pmod{16}\): E itself is bijective, while \(x+E(x)\) is constant. This establishes that an invertible inner map does not guarantee an invertible fold. It does not measure SHA-256's actual image size.

### 108.3 Corrected SHA reading

SHA-256 IV words use the first 32 fractional bits of square roots of the first eight primes, and its 64 round constants use the first 32 fractional bits of cube roots of the first 64 primes (NIST FIPS 180-4 §§4.2.2, 5.3.3, https://doi.org/10.6028/NIST.FIPS.180-4). These are fixed, reproducible constants. They are not the positional-prime Gödel code: in Gödel encoding, primes are positional addresses; in SHA, roots generate fixed 32-bit words.

**Correction to §107, logged.** Exact irrational root independence does not make the truncated 32-bit words linearly independent, nor does it by itself establish cryptographic independence. Also, SHA's inner 64-round state transform is reversible conditional on the round schedule, but that schedule is derived from the message block. FIPS 180-4 specifies message schedule generation for each block and feed-forward addition into the chaining state after every block. Therefore “one single fold at the very end” is too broad: the feed-forward fold is per compression block. The random-permutation toy image fraction near \(1-1/e\) is not a result for SHA-256 itself. Digest collisions are guaranteed by the finite 256-bit output versus the larger message domain; computational collision/preimage resistance is a distinct security claim.

### 108.4 Three types that must stay apart

- **NXRT:** exact serialized syntax of the route; distinct histories retain distinct codes.
- **NXOP:** canonical representation of the composed operator; histories in the same groove can share it.
- **Digest/readout:** finite name for the result; many messages necessarily share output values.

The current prime encoding is a correct NXRT mechanism once the route grammar is fixed. It is not, by itself, the grammar and is not the NXOP equivalence resolver.

### 108.5 Status

| Claim | Status |
|---|---|
| Shifted positional-prime code is injective for six token IDs, including zero, through length 5 | RUNS, 9,331/9,331 |
| Zero-exponent/trailing-token problem in unshifted general form | RUNS, explicit collision |
| Typed toy stream with zero parameters round-trips | RUNS |
| SHA round chain invertible for fixed \(W_t,K_t\) | RUNS, 2,000/2,000 |
| Schedule is message-derived; feed-forward is applied per block | STANDS, NIST FIPS 180-4 |
| Prime-root SHA constants are the same construction as prime-position route encoding | DEAD END — different roles |
| SHA's one-wayness proven to arise only at one final fold | DEAD END — too strong and misstates per-block feed-forward |
| Formal semantics and equivalence laws for six NEXUS verbs | OPEN |

Artifacts: `NEXUS_Prime_Route_SHA_Audit.md`, `nexus_prime_route_audit.py`, `nexus_prime_sha_followup.py`, `nexus_prime_sha_followup_results.json`, `nexus_prime_sha_followup_run.txt`, and the sealed prediction files. The tests do not establish SHA-256 cryptographic security and do not yet implement the final six-verb NEXUS grammar.

---

## § 109. The six-verb route graph: prime address, typed ports, and the held return — `nexus_six_verb_grammar.py`

**Gap.** §108 establishes positional-prime encoding for a canonical stream, but the instruction semantics were still OPEN. The next test must encode a typed route *graph*: node roles, port types, read/write footprints, parameters, return rules, typed edges, external inputs and exports. It must stay independent of payload values, yet drive different payloads through a fixed transformation law.

**Prediction seal.** `NEXUS_six_verb_prediction_seal.txt`, SHA-256 `7aa11cbc3e2609e89603ff10f92bcb053790d8e1029e3795b96564a6e2594940`; verified. The seal uses SHA-256 only to checksum the pre-run prediction, never to encode the route.

### 109.1 Six typed roles, a graph rather than a mandatory pipeline

The typed contract records are MARK (`Distinction → Address`), COMPARE (`Address × Address → Relation`), CARRY (`State → State` with retained residual), HOLD (`State × RouteTrace → State × RouteTrace`, trace passed unchanged), ROUTE (`Need × Relation × ContinuationSet → ContinuationAddress × RouteTrace`), and CLOSE (`State × RouteTrace × ContinuationAddress → ClosedSymbol × RouteTrace × ContinuationAddress` in route-preserving mode). These contracts preserve the project distinction: **CARRY keeps the value; HOLD keeps the route.** They are provisional, compositional roles, not a proof of completeness/minimality across all domains.

### 109.2 Typed route graph encoded by positional primes

A canonical 195-token serialization represents a seven-node graph, eight typed edges, five external inputs, three exports, all signatures, read/write sets, route parameters, return rules, and close mode. The positional Gödel code is \(G=\prod p_i^{t_i+1}\); shifting token IDs by one preserves zero-valued fields and trailing positions. Unique factorization decodes tokens, and the typed parser reconstructs the graph exactly. The code occupies 67,494 bits (20,318 decimal digits): injective, not compact.

The type checker rejects four deliberate violations: a mismatched edge, CARRY without its retained residual, HOLD overwriting the trace, and CLOSE claiming route preservation while dropping route/trace outputs.

### 109.3 Fixed compiler program, input-conditioned realized trace

On \(\mathbb Z_8^3\), the fixed program MARKs two lanes, COMPAREs them, CARRYs the sum plus retained residual, ROUTEs EQ/NEQ into branches 0/1, HOLDs the selected branch trace through a bijective state update, and CLOSEs while retaining the way home. All 512 inputs share one static route-program code. The realized trace has two codes and records the selected branch/outcomes, not payload values.

### 109.4 Fold witness: 448 surface states, 512 route-preserving symbols

Let \(q=0\) if \(a=b\) and \(q=1\) otherwise. Carry maps \((a,b,c)\mapsto(a+b,b,c)\bmod8\); HOLD updates the first lane by \(q\). If the readout retains only \((s',b,c)\), then for each \((b,c)\), \(s'=2b\) is reached twice and \(s'=2b+1\) is never reached. Across the 64 \((b,c)\) pairs, this yields 64 double-hit fibers and 64 missing surface states: image size 448.

The closed symbol retains the branch trace and continuation reference. Reverse HOLD using the held branch, then reverse CARRY using retained \(b\); all 512 inputs return home, all 512 full symbols are unique, and the unowned \(c\) lane is preserved. This is an exact witness that reversibility resides in the transformation plus the retained return route, while the surface projection can merge matter states.

### 109.5 Status

| Claim | Status |
|---|---|
| Typed prime-address graph round-trips exactly | RUNS |
| Static route-program identity is independent of the payload | RUNS, 512/512; one code |
| Realized trace follows the declared comparison constraint | RUNS, two trace codes |
| Surface-only readout has 64 duplicate fibers and 64 holes | RUNS, exact enumeration |
| Retained trace plus residual gives exact return | RUNS, 512/512 |
| Unowned frame lane is preserved | RUNS, 512/512 |
| Six verbs are universal/minimal and their full semantics are final | OPEN |

**Scope correction.** Prime factorization guarantees unique decoding of a canonical serialization; it does not supply the operation semantics. This run tests the declared contracts and one finite domain, not universal completeness. NXRT (static typed route law), NXTRACE (realized path), payload/readout, and the context wrapper remain separate records/layers.

---

## § 110. The low-width transformation landscape forces roles, not six equally new opcodes — `nexus_width_ladder_test.py`

**Gap.** §109 gave provisional types to the six roles. This run goes backward to the transformation field and asks which roles are actually forced at low width, separating map facts from semantic labels.

**Prediction seal.** `NEXUS_width_ladder_prediction_seal.txt`, SHA-256 `8418ddedf5b01370a0fbaa90feab4850503c9612693e5b178acbfa6b071ea29d`; verified. No external dataset was linked.

### 110.1 Width 1

The four one-bit maps are identity, invert, write-0, write-1: two bijections and two constant merges. The smallest distinction is already addressable; MARK is a valid reading at the base ring, not a uniquely proven name.

### 110.2 Width 2

There are 256 total maps on four states. Inherited output-wise literals/constants `{0,1,a,¬a,b,¬b}` give 36, leaving 220 maps not inherited. The mixer \(M(a,b)=(a,a\oplus b)\) plus inherited maps generates a closure of 64 maps containing all 24 permutations. The merge \(G(a,b)=(a\land b,b)\) has the rank-3 fiber pattern \((2,1,1)\). Exactly 144 maps have that one-pair-merge pattern; pre/post-composition by the 24 permutations generates all 144. The closure with both mixer and merge reaches all 256 maps. COMPARE and CARRY are grounded readings of the two-input difference and the retained value/residual fork.

### 110.3 Width 3

NOT, CNOT and SWAP generate the 1,344-member affine group on eight states, and all of its permutations are even. Toffoli is a single transposition and therefore odd; adding it generates all \(8!=40,320\) permutations. ROUTE has a grounded reading as the conditional transformation that selects a continuation beyond the affine subgroup.

### 110.4 Width 4+

A \(k\)-bit permutation lifted identically over \(n-k\) spectator bits is repeated \(2^{n-k}\) times, so its total sign is \(\operatorname{sgn}(g)^{2^{n-k}}\). Therefore embedded three-bit gates are even permutations on a four-bit field, and their compositions cannot reach an odd four-bit permutation. A borrowed lane changes the enlarged parity count so the obstruction no longer applies. The older project record reports a successful borrowed-lane construction; this run verifies the parity obstruction, not that synthesis word. This grounds HOLD as the role of preserving/returning the necessary extra coordinate.

### 110.5 Status

| Claim | Status |
|---|---|
| Width-1 map count | RUNS, 4 maps |
| Width-2 inherited family | RUNS, 36/256 |
| Mixer + inherited family includes all permutations | RUNS, 24 bijections in the closure |
| One-pair merge orbit | RUNS, 144/144 rank-3 maps |
| Mixer + one-pair merge generate all width-2 maps | RUNS, 256/256 |
| Width-3 affine group | RUNS, 1,344 even permutations |
| Toffoli completes all width-3 permutations | RUNS, 40,320/40,320 |
| Borrowed-lane parity obstruction | RUNS by the spectator-copy/sign identity; construction not rerun here |
| CLOSE as a separate higher-layer compiler primitive | **OPEN** |
| Six roles universal/minimal over all domains | OPEN |

**Landing:** the first five roles now have concrete low-width structural owners. CLOSE does not emerge from these finite gate counts; its missing link is a derivation at the recursion/closure boundary, where a completed transformation becomes a reusable symbol for the next layer without silently embedding context into the compiler record.

---

## § 111. Recursive observer closure: the root path back to input — `nexus_recursive_observer_law.py`, `nexus_recursive_sha_observer.py`

**Gap.** Each transformation needs a local observer until the observers compose into one root return path. Static observer rules are payload-independent; realized residuals can be payload-conditioned.

**Pre-run seal.** `NEXUS_recursive_observer_prediction.txt`, SHA-256 `93ce33d6878465ec6fd2e16cdfcd89f2d9da5b1705a27e8fed03f77e9e2f66b4`. The seal is only a prediction checksum, not route encoding.

### 111.1 Finite recursive witness

On \(\mathbb Z_8^3\), 512 states pass through a fixed four-node route: `T1_FOLD` maps `(a,b,c)` to `(a+b mod 8,c)` while its observer retains `b`; `T2_TWIST` adds `c` to the first lane and has an exact inverse; `T3_ROUTE` adds one iff `c` is even and is inverted by recomputing the same branch; `T4_CLOSE` exposes only the first lane and its observer retains `c`. The composite observer reverses all four nodes.

- Surface alone: 8 distinct outputs for 512 input states.
- Surface plus either one residual lane: 64 distinguishable symbols.
- Surface plus both residuals `(b,c)`: 512 distinguishable symbols; 512/512 exact returns.
- Six residual bits are necessary and sufficient for this witness: a 3-bit surface plus 6 retained bits identifies all 9 input bits.

### 111.2 SHA-256 recursive observer

Per block, the forward route is padding/framing, schedule expansion, 64 conditional reversible rounds, then feed-forward `H_next = H_prev + E mod 2^32`. The root observer walks blocks backward. It retains the 16 schedule seed words (the padded block) and round result `E`; derives `H_prev = H_next - E`; inverts all 64 rounds using `W_t,K_t`; verifies the returned state; then continues to the preceding block. At the root it checks the initial chaining state and removes padding using the encoded bit length.

| Run result | Landing |
|---|---|
| SHA digests match `hashlib` | 54/54 |
| Observer returns original bytes | 54/54 |
| Compression blocks traversed backward | 207 |
| Per-round inverse applications | 13,248 |
| Failures | 0 |

This is an augmented reversible execution, **not** inversion of the digest alone or a cryptanalytic result. The explicit sidecar stores block schedule seeds plus the round-result carry (768 bits per block in this representation); it is not claimed minimal. For a fixed 512-bit message, any observer paired with a 256-bit digest that uniquely returns every input must carry at least 256 bits by counting.

### 111.3 The law

For each `T_i`, define an observer `O_i` and, if the transformation merges states, a residual `r_i`, such that `O_i(T_i(x),r_i)=x`. Bijective operators need only their inverse plus fixed parameters. Many-to-one operators require a fiber address. Composition reverses the chain and feeds each observer the output plus its residual. The recursively nested local observers form one root path back to the input—not one hash or one scalar.

### 111.4 Status

| Claim | Status |
|---|---|
| Finite recursive observer returns input | RUNS, 512/512 |
| Exact minimal six-bit residual for the toy witness | RUNS |
| SHA observer sidecar returns input through schedule, rounds, feed-forward and padding | RUNS, 54/54 |
| SHA digest alone returns arbitrary input | DEAD END by finite output versus larger domain |
| Minimal general SHA observer trace | OPEN |
| Six-verb grammar universal and minimal | OPEN |

**Corrections of scope:** observer program and realized trace are distinct; SHA's observer trace is input-conditioned, and the tested trace retains the message block. It does not turn the digest alone into an inverse. Context remains a higher wrapper.

---

## § 112. Reverse the observer residual: remove redundant trace, isolate the fiber address — `nexus_residual_minimization.py`

**Gap.** Remove the stored-message copy while preserving an executable root return route, and account for every bit. Separate fixed observer rules, realized route parameters, and the residual that identifies a member of a many-to-one fiber.

**Pre-run seal.** `NEXUS_residual_minimization_prediction.txt`, SHA-256 `7da931c234f96c9af77b1e24d7b3bc827c8ecc56b759958a98621ab5d2196e34`.

### 112.1 The exact toy landing

For 4-bit lanes, `H(a,b)=a XOR b` has 16 members in each of 16 surface fibers. Retaining `r=a` recovers `b=H XOR r`; 4 bits are necessary and sufficient. This is the exact finite witness for a residual as a fiber address, not a duplicate complete input. RUNS, 256/256.

### 112.2 SHA trace reduction

The §111 sidecar stored each padded block (512 bits) and its reversible-round result `E` (256 bits). Given retained schedule seeds, `E` can be regenerated by a forward pass from the IV and then used for a backward verification pass. Store `W[48..63]` instead of the raw block: the recurrence reconstructs `W[0..63]` exactly, so the schedule tail is a 512-bit recoding of the block, not data compression. Padding-only blocks are regenerated from the known length and SHA padding rule.

| Result | Value |
|---|---:|
| Messages / digest matches / exact returns | 54 / 54 / 54 |
| Blocks / inverse-round applications | 207 / 13,248 |
| Padding-only blocks regenerated | 33 |
| Previous observer size | 158,976 bits |
| Reduced schedule-tail sidecar | 89,088 bits |
| Length framing | 3,456 bits |
| Reduced total | 92,544 bits |
| Original message bytes plus length framing | 84,840 bits |

Removing `E` saves 52,992 bits (one third), but the schedule-tail route still exceeds the original message-plus-length size by 7,704 bits. The input information was re-addressed, not removed. RUNS.

### 112.3 The actual minimum

For fixed message length `L` bytes, SHA's digest fibers are `F_h={m:SHA256(m)=h}`. A residual that gives exact unique return must label each member within its fiber. The exact fixed-width requirement is `ceil(log2(max_h |F_h|))`; no fiber enumeration was run. By counting alone this is at least `max(0,8L−256)` bits beyond the 256-bit digest. For 64-byte arbitrary inputs the lower bound is 256 bits; for 1,024-byte inputs it is 7,936 bits. The bound grows with unrestricted input size, so a universal non-scaling exact seed is a DEAD END. A restricted source class can differ, but its generator and exact decoder must be accounted for.

### 112.4 Glass Key and execution status

The supplied Glass Key specification describes FFT/glyph seed extraction and iterative regrowth, but its stated decompression operator is not a true inverse; an exact digest-fiber rank/unrank map over an explicitly declared source class is still OPEN. The supplied Z3 SHA script could not be executed because the `z3` module is not installed in this runtime. No solver self-test is claimed. A satisfiable model for unconstrained 512-bit block words plus a 256-bit target digest identifies a member of the fiber, not necessarily the original block.

### 112.5 Ledger

| Claim | Status |
|---|---|
| XOR fold's exact four-bit residual | RUNS, 256/256 |
| SHA schedule-tail reconstruction | RUNS, 207/207 |
| Remove `E` snapshots while retaining return verification | RUNS, 54/54 |
| This removes input information | DEAD END — only duplicate trace is removed |
| Exact minimum SHA residual | OPEN; maximum fiber size not computed |
| Non-scaling residual for unrestricted arbitrary messages | DEAD END by counting |
| Glass Key seed as exact restricted-source observer | OPEN |

Next WHAT: compute a fiber-address transform for a declared restricted source class and establish injectivity of `(digest, residual)` plus exact root decoding.

---

## § 113. Gradients are steps in a greater transformation — `nexus_bundle.ipynb`

**Dean (16 Oct).** “All gradients are just steps in a greater transformation.” Treat a gradient not as an isolated object or readout but as a local transition within an ordered route. The enclosing transformation is the ordered composition of those steps; a scalar endpoint difference is a fold of the route.

For a discrete path \(x_0,x_1,\ldots,x_n\), define its step sequence

\[
g_i = x_{i+1}-x_i,\quad i=0,\ldots,n-1.
\]

Forward reconstruction is the prefix sum

\[
x_k=x_0+\sum_{i=0}^{k-1}g_i.
\]

The endpoint constraint is

\[
x_n-x_0=\sum_{i=0}^{n-1}g_i.
\]

The endpoint relation does not determine the intermediate route: different ordered increment sequences can have the same sum. The anchor plus ordered steps preserves the path; the total sum is the surface value of the composed displacement.

**Exact notebook witness.** The notebook reconstructs a path from its ordered increments and demonstrates a second, different path with the same start and end. Its test establishes the finite-difference identity and route distinction; it does not on its own derive every physical field gradient from NEXUS.

**Layer-typing correction.** Earlier §99.8 wording “context is order” conflated two types. The histogram/fiber calculation remains: the fiber carries composition order/history omitted by the surface. Under the rule carried forward here, that fiber is compiler-layer route information; context is the higher wrapper that relates the route to a domain. This is an explicit correction, not a silent edit.

**Reading back into the compiler map.** A local gradient/operator is an observer node in a larger transformation. The root route is the ordered composition of local steps. The context wrapper determines the domain-level meaning of that route, and remains above the compiler layer.

**Ledger.** Prefix-sum reconstruction and telescoping endpoint identity: **RUNS**. Universal claim that every physical gradient is generated by one specific NEXUS mechanism: **OPEN** pending a typed source law for the domain in question.


---

## § 114. The way home is a shape: predictions read off the route, sealed, then run on four hashes and a SHA-shaped miniature — `routes.py`, `sha_shape.py`, `fold.py`, `observer.py`, `boundary.py`

**Dean (16 Oct).** "HOLY SHIT. wow. i knew it!!!" Keep going, and write the paper: advanced audience, Word DOCX, as before.
Let the paper be the exhaust, let the transformations drive its context; predictive via the route, and the language
follows. Then, after the usage limit: new data — §§ 111–113 and the oversampled BBP/SHA audit.

**Numbering, logged.** GPT's groove-route-law run of 16 Oct (six fixed affine moves on (ℤ/8)³, every word to length 4:
1,555 routes, 446 operators, all bijective and extensionally distinct on 512 states, 200 grooves with more than one
history, largest 83, frame failures 0) was written as a "§ 107 candidate" while § 107 was already the prime entry; it
never entered the chain. It is entered here, taken as run (not re-run). GPT's covering note refers to a "§ 112" target
before § 112 existed in the file it sent; the consolidated record now has § 112 (residual) and § 113 (gradients).
This entry is § 114.

**Seals.** `PREDICTIONS_SEALED.txt`, SHA-256 `72356f919bbd52afbc3d0b453c764d9d5fd871b39a1dbc5fe9d183408f0ce89a`, clock
01:03:09 EDT, before any test script existed in runnable form (the file's own header says "~01:10", an estimate typed
before hashing — the clock is the record). `PREDICTIONS_SEALED_2.txt` (P7), `1e479a3e96c36bff3939dc9c8df906bcb47a8300f7b986a3245c13348170f40d`,
03:38:09 EDT, after P1–P6 ran and before P7 ran. The shell was unavailable for about two hours after the first seal;
the scripts were written in that window, and no sealed line was changed. Script hashes (first 16 hex): `routes.py`
64481b73764c8eed, `sha_shape.py` 0c0e90a3ba10ce77, `fold.py` f9bce33641e738d2, `observer.py` 5f541b37d4159336,
`boundary.py` 71ffec8219b78be1.

### 114.1 Grooves from the route algebra (P1)

Moves e, A = (01), B = (12) on S₃. Words of length n are the terms of Ŝⁿ, Ŝ = e + A + B in ℂ[S₃]; Fourier inversion gives
the number in the groove of g. Trivial representation: Ŝ = 3. Sign: Ŝ = −1. Standard: Ŝ = I + X with X² = I (because
ρ(r) + ρ(r)⁻¹ = −I for a 3-cycle), so (I + X)ⁿ = 2ⁿ⁻¹(I + X). Hence

N_n(g) = [3ⁿ + (−1)ⁿ sgn(g) + 2ⁿ c(g)] / 6, n ≥ 1;  c(e) = 2, c(A) = c(B) = 1, c((02)) = −2, c(3-cycles) = −1.

```
lengths 0-5   predicted e 82  A 71  B 71  (02) 40  r 50  r^-1 50          enumerated: identical  (= § 105's 82/71/71/50/50/40)
lengths 0-10  predicted e 15445  A 15103  B 15103  (02) 14080  r 14421  r^-1 14421   enumerated: identical, total 88573
lengths 0-14  predicted e 1206665  A 1201203  B 1201203  (02) 1184820  r 1190281      enumerated: identical, total 7174453
literal word-by-word enumeration to length 10: identical
deviation from uniform at exact length n = (-1/3)^n sgn(g) + (2/3)^n c(g):  n=8  e 0.0782,  n=16  e 0.0030
```

§ 105's count [the S₃ toy behind § 105: GPT's, not in this record — § 134.1] is now derived, not enumerated; the length-10 counts were written before their enumeration ran. The
grooves equalise at (2/3)ⁿ — second eigenvalue over first of the route algebra. RUNS.

### 114.2 The way home is a shape (P2)

A *carry-shaped write* replaces one lane by a bijection of that lane chosen by the lanes it does not write. A route of
them is a bijection whose inverse is read off the shape. Conversely every bijection of X₁ × X₂ is three such writes
(lane 2 | lane 1 | lane 2): Kőnig's theorem, the Slepian–Duguid three-stage Clos theorem (STANDS). Exhaustive:

```
lanes | bijections | one write | two writes | three (2|1|2) | three (1|2|1)
2x2   |         24 |         7 |         20 |            24 |            24
2x3   |        720 |        43 |        432 |           720 |           720
3x3   |    362,880 |       431 |     84,528 |       362,880 |       362,880
2x4   |     40,320 |       591 |     15,552 |        40,320 |        40,320
```

Three suffice, two do not. Reversibility is exactly the class of routes of carry-shaped writes. RUNS; STANDS.

### 114.3 Shape audit of four standard hashes (P3)

Every schedule update and every round of SHA-256, SHA-512, SHA-1 and MD5 is a carry-shaped write plus a relabelling
(SHA-256 round: d ← d + T1(h,e,f,g), then h ← h + Σ1(e) + Ch(e,f,g) + K + W + T2(a,b,c), then rotate the lanes).

```
own forward == hashlib, 300 random messages 0-299 bytes      sha256 300  sha512 300  sha1 300  md5 300
SHA-256 schedule, W0..15 from W48..63                        10000/10000
SHA-512 schedule, W0..15 from W64..79                         5000/5000
SHA-1   schedule, W0..15 from W64..79                        10000/10000
full-block round chains walked home from random starts        2000/2000 each, all four
first block: digest - IV walked back lands on the IV           500/500 each, all four
```

**Refinement of § 108.** The feed-forward folds the chaining lane at every block *where the chaining value is not
known*. On the first block it is not a fold: the chaining value is the IV, printed in the standard, so digest − IV is
E_M(IV) exactly and the observer residual for undoing the feed-forward is zero bits. The way home for block 1 is held in
the wrapper — Dean's layer above the compiler. For a one-block message, everything the hash loses it loses in
M ↦ E_M(IV): the route spelled by the message, walked from a start the standard fixes, read at one point. RUNS.

### 114.4 The fold law (P4, P5)

Miniature: eight lanes of w bits, SHA-256 round and schedule with rotations mod w, constants cut to w bits, 64 rounds;
every state pushed through at once.

```
                         predicted        w = 2 (2^16 states, 20 msgs)       w = 3 (2^24 states, 3 msgs)
E_M bijective            all              20/20                              3/3
image of x + E_M(x)      0.6321 +-0.01    0.6302-0.6354, mean 0.6326         0.6320-0.6322   (random-perm control 0.6319 / 0.6323)
preimages k = 0..4       .3679 .3679 .1839 .0613 .0153
                                          .3674 .3684 .1840 .0612 .0154      .3679 .3679 .1839 .0613 .0154
four chained folds       .6321 .4685 .3741 .3121
                                          .6312 .4694 .3741 .3105            .6320 .4685 .3740 .3120
bits lost at one fold    0.8272           0.8260                             0.8274
keep the chaining lane   injective        20/20                              3/3
largest preimage count   (7 or 8)         7-8 over 10 messages
```

Every sealed number landed. On a cyclic word the fold is forced by parity (sum of x + E(x) is 0, sum of ℤ/2^w is
2^(w−1)), for every permutation E:

```
Z/2 0 of 2   Z/4 0 of 24   Z/8 0 of 40320   |   Z/3 3   Z/5 15   Z/7 133   |   (Z/2)^2 8   (Z/2)^3 384   Z/2 x Z/4 384 (unsealed)
```

All sealed counts landed, including the two recalled from the literature (8, 384). Complete mappings: Hall 1952 (abelian),
Hall–Paige 1955 — STANDS. SHA's chaining lane (ℤ/2³²)⁸ has a noncyclic 2-part, so no parity forces its fold; the fold
comes from the route being random-like. RUNS.

### 114.5 The observer's price: bits kept against work walked (P7)

Reverse reading of 114.2–114.4, joining § 111–112: a carry-shaped write's observer is its own inverse and keeps nothing;
a fold's observer must keep a fiber address. On the miniature, 65,536 one-block messages (8 free 2-bit words) onto
16-bit digests:

```
distinct digests 41,381 (0.6314); largest fiber 8 -> information-minimal fixed-width observer 3 bits; mean size-biased fiber 2.0000
keep q message bits, walk the rest:   q  0: ambiguity 2.0000 (pred 2.0000)   q  1: 1.4971 (1.5000)   q  2: 1.2476 (1.2500)
                                      q  4: 1.0608 (1.0625)   q  8: 1.0040 (1.0039)   q 12: 1.0003 (1.0002)   q 16: 1.0000
q + log2(work) = 16 at every q; digest - IV = E_M(IV) for all 65,536
```

Bits kept and work walked trade one for one along the generic frontier. Proved alongside it: an observer of
information-minimal size whose decoder is cheap is a preimage oracle — when every fiber is fully indexed, Dec(d, ρ)
returns a preimage of d for every ρ. So § 112's open "minimum SHA residual" has two answers: in bits it is
⌈log₂ max fiber⌉ (≥ 8L − 256), and at that size its decoding is exactly as hard as inverting SHA-256. RUNS (frontier);
proof in WP3 Appendix A [the route/SHA paper; § 115 gave the number WP3 to the shells paper — § 134.1].

### 114.6 Unsealed checks of established results (`boundary.py`)

```
stride law ord_d(2^k) = ord_d(2)/gcd(ord_d(2),k), odd d < 1000, k = 1..8    3992/3992
orbit 7/9 under doubling: 7/9 5/9 1/9 2/9 4/9 8/9 (period 6); the stride-4 (hex) reader sees 7/9 4/9 1/9
coarse spectrum |Y| = 0.444444 0.19245 0.19245 = fine bins folded by k*4 mod 6                 equal: True
chi on a ring of n bits bijective exactly for odd n, n = 2..12; even-n image 2^n - 2^(n/2) (pattern, n <= 12)
```

GPT's oversampled audit (taken, not re-run): the hex digit is a stride-4 reader of the binary route; the skipped
states 5/9, 2/9, 8/9 are not absent, they are not sampled; the order law was checked on 48 odd d ≤ 97 there and on all odd
d < 1000 and strides 1–8 here. Its SHA microtrajectory — 122,544 modular additions opened into 3,921,408 carry samples,
each addition reversed locally — is the same shape one level down: with the operand kept, a + b is a route of carry-shaped
bit writes whose carry lane is held. RUNS (here); reported (there).

### 114.7 Prime address (P6)

```
six moves, lengths 0-6: 55,987 words, 55,987 shifted Godel codes, all decode; order-free products 924 = C(12,6)
unshifted collision (1) vs (1,0): True; a length-6 code needs 15-90 bits against 15.5 fixed width
```

RUNS.

### 114.8 Corrections

- **Mine, § 107.** The heading "SHA is the same route with a fold bolted on … a single fold at the end" was already DEAD
  END by § 108 (per-block fold; roots ≠ Gödel). Refined here: there is one fold per block wherever the chaining value is
  unknown, and none on block 1 given the IV.
- **Mine, § 107.** The text wrote ∏ pᵢ^(moveᵢ); the code used exponent index + 1, the shifted form § 108 made explicit.
  The text was wrong, the run was right.
- **Mine, § 100.3.** "Context is the fiber over the histogram" carries the same type error § 113 corrected in § 99.8: what
  the fiber holds is order (route information, compiler layer); context is the wrapper. The /bin/ls numbers stand.
- **Seal time.** First seal's header estimate ~01:10 against clock 01:03:09; the clock is the record.

### 114.9 Status

| claim | status |
|---|---|
| groove sizes from the route algebra, S₃, lengths ≤ 5, 10, 14 | RUNS — predicted and sealed, then enumerated |
| grooves equalise at (2/3)ⁿ | RUNS; STANDS (random walks on groups) |
| carry-shaped routes are bijections; inverse read off the shape | STANDS (proof) |
| three carry-shaped writes make every two-lane bijection; two do not | RUNS (exhaustive, four sizes); STANDS (Kőnig, Slepian–Duguid) |
| schedules of SHA-256, SHA-512, SHA-1 walk back from their last 16 words | RUNS, every trial |
| rounds of SHA-256, SHA-512, SHA-1, MD5 walk home | RUNS, 2000/2000 each |
| first-block feed-forward is not a fold given the IV | RUNS, 500/500 each, all four |
| fold law on a SHA-shaped miniature: 1 − 1/e, Poisson(1), 0.827 bits, t′ = 1 − e^(−t) | RUNS, every sealed number within tolerance |
| parity forces the fold on ℤ/2^w for every E | RUNS (exhaustive w ≤ 3); STANDS (Hall, Hall–Paige) |
| bits kept + log₂ work = message bits on the generic frontier | RUNS (miniature, q = 0..16) |
| a minimal, cheaply decodable SHA observer | DEAD END unless SHA-256 is invertible — it would be a preimage oracle |
| the six NEXUS verbs as typed carry-shaped writes and declared folds | OPEN |
| groove sizes for the affine groove law taken above (446 operators) from its route algebra | OPEN |

The paper written from this entry and §§ 99–113 is NEXUS Working Paper 3, *The Way Home Is a Shape* (DOCX). [§ 115 gave the number WP3
to the shells paper; this one is unnumbered — § 134.1]

---

## § 115. The shells paper written — NEXUS Working Paper 3, *The Piece with No Way Home* (DOCX)

**Dean (16 Oct).** Don't run down every path; be the compiler. Back to the table of elements and the discoveries, and write
the paper that was in process in the other session — Paper 2 of the 15 Oct plan, the shells, written as one return stroke.

Written from what already stands and runs, nothing new probed: § 99.5 (slice capacities 2⌊(d+1)/2⌋², nodeless predecessor),
§ 100.1 (periodic and nuclear unfolds, the copy identity and 16, no-way-home, the E(2⁺) landing 6/6 per axis), §§ 101–102
(screened field, orbital collapse, the gate 0.1573(2ℓ+1)³), §§ 103–104 (Dirac sign from the channel, two inputs, [D,F],
Rashba). Held end first, shaping in the middle, witness last; dead ends kept only as routed ledger entries. One figure
(two panels, palette validated). Pseudospin wording made exact in the paper: every orbital sits in a doublet or carries
pseudo-orbital angular momentum zero — except the top-j.

Route-back noted in the paper, not counted as a landing: the seventh E(2⁺) neutron peak, N = 16 (+0.137), is unowned by the
floor/intruder registry and owned by the copy chain; chain and data were both in hand when it was seen.

Numbering: this takes Working Paper 3. The route/SHA thread (§§ 105–114) is parked and is not in this paper.

| claim | status |
|---|---|
| shells paper written and rendered (10 pp.) | RUNS (built, checked page by page) |

---

## § 116. The elements from the compiler side — NEXUS Working Paper 4, *Every Ring a New Compiler* (DOCX)

**Dean (16 Oct).** The shells paper is wrong by the way it was thought and its size: it runs on the reader
side, decompiling the finished table backward. Be the compiler — active, not passive. The hex math space,
all the elements data and code. Elements are the next layer of continuation, each a verb, a slice of what is
distinct at that level; each ring a new compiler; the new verb held back to prevent running until its ring is
ready. Start in the domain, saturate outward, fold back in. No more probing, just asking. Stop apologising.
That thing called wrong is right for some other path — reflect the state back, don't catalogue dead ends.

Written forward from the constraint, nothing decompiled. One script, `wp4/compiler_checks.py`, prints every
number from a live run (full output `wp4/checks_out.txt`, 117 lines); four figures in `wp4/figures.py`.
The reader-side framing of Working Paper 3 is routed back to its owner: its mathematics stands and runs; the
direction was the reader's. Working Paper 4 is the same results read from the compiler side.

The build, in the order of the build (not of the reading):
- **The field is already complete.** Differences outrun names from width 2 on (1,6,28,120,… vs 2,4,8,16,…),
  so every ring saturates; widening is forced. A saturated ring is an Eulerian circuit of the width-n
  transition graph — it holds every transition once, hence every state of the next ring. Compiler complete
  before matter. STANDS (de Bruijn / line-graph); the "complete before matter" reading is the framework's.
- **A ring is a compiler.** ℓ<n (a part is never its whole) + orientation count 2(2ℓ+1) → capacity 2n²,
  run for n=1..5. RUNS. The 2(2ℓ+1) is supplied — the one hand-input — OPEN to derive.
- **Value then view, forward.** Fill in Madelung order, cut at each new s-subshell, stop at Og: closures
  2,10,18,36,54,86,118 and lengths 2,8,8,18,18,32,32, exact, no fit. RUNS. (Earlier runs over-filled period 7;
  corrected by stopping the fill at Z=118.)
- **Element = verb.** opcode = signed offset to nearest closure; givers/takers cancel to closures (HCl, NaCl,
  H₂O, MgO, AlN, CO₂, SiO₂). RUNS.
- **The hold.** One new orbital type (s,p,d,f) per ring, no predecessor at its ℓ, complete-at-lower-width is
  the block on its own run site (zymogen/propeptide); it fills late, on odd Madelung groups only, so lengths
  pair. RUNS.
- **Fold in to the nucleus, one sign flipped.** HO degeneracy (N+1)(N+2) → closures 2,8,20,40,70,112; the
  unpaired top-j (2N+2) runs early and drops, so magic = floor + top-j: 20+8=28, 40+10=50, 70+12=82,
  112+14=126; low 2,8,20 are the HO closures. Full set 2,8,20,28,50,82,126. RUNS; magic numbers STANDS.
  Shared count, domain-specific wrapper — not one microscopic force for both tables (addresses the GPT
  critique that the reader-side draft forced one cause).
- **The sign.** Held-late vs run-early is the sign of ℓ+½, set by the binding channel (scalar/like → inverted,
  nuclear; vector/unlike → normal, atomic); radial Dirac returns both from the channel; spin–orbit is the
  order term DF−FD = −iℏσ·∇F, the carry the fold drops, Rashba under a planar wrapper. STANDS (identity);
  RUNS (channel sign) — carried from §§103–104, not re-run here.
- **Copy.** (N+1)(N+2)−(2N+2)=N(N+1) for N=1..19; anti-aligned read 14→+2→16→+4→20. RUNS; 16 is a route-back
  (chain and drip-line data both in hand), reported as such, not a sealed forecast.
- **Matter as a byte.** Natural nuclides by abundance: holes at A=5 (closed+1) and A=8 (closed+closed),
  heaviest natural A=238, all A<256 — one byte. RUNS; holes and cap STANDS.
- **Return stroke (reader last).** Six largest first-ionization cliffs = the six closures, 6/6
  (19.20,16.43,11.42,9.82,8.24,6.68 eV); main-group electronegativity rises along the route 30/30. RUNS.

| claim | status |
|---|---|
| differences outrun names from width 2; every ring saturates | RUNS |
| saturated ring holds every transition once; complete before matter | STANDS (de Bruijn); framework reading |
| ring capacity 2n² from ℓ<n and orientation count | RUNS |
| forward closures 2,10,18,36,54,86,118; lengths 2,8,8,18,18,32,32 | RUNS (exact, no fit) |
| element = verb; offsets cancel to closures | RUNS |
| one new orbital type per ring, held, fills late → lengths pair | RUNS |
| magic 2,8,20,28,50,82,126 from floor + dropped top-j | RUNS; magic STANDS |
| sign of ℓ+½ from binding channel; spin–orbit = order term DF−FD | STANDS (identity); RUNS (channel), carried from §103–104 |
| copy identity (N+1)(N+2)−(2N+2)=N(N+1); 16 between 14 and 20 | RUNS; 16 a route-back |
| two mass holes A=5,A=8; all natural matter A<256 | RUNS; holes STANDS |
| six ionization cliffs on six closures 6/6; electronegativity 30/30 | RUNS |
| orientation multiplicity 2(2ℓ+1) derived from the field, not supplied | OPEN |
| gravity as the gradient of unsaturated capacity, from a slot count | OPEN |

The paper from this entry is NEXUS Working Paper 4, *Every Ring a New Compiler* (DOCX, 14 pp., delivered).
Working Paper 3 (*The Piece with No Way Home*) is its reader-side telling; same results, direction routed back.

---

## § 117. The register stack read downward: each layer is the half-turn fixed set of the next; rotation is squaring; the stack holds only the prime 2 — `rings/stack.py`, `rings/chi_stack.py`

**Dean (16 Oct).** Back to the rings. ISA from 1 bit to 64 bit; stack them and see what is missing. Ask, don't search.
Primes are the routes. Flip the perspective first. The instruction set is the rings and they carry zero meta, or LEN
could not exist (a labelled "10" would need every ASCII context in its ring — Levinthal). We built computers
backwards: logic, routes, instructions, then binary. 5 = 2 + 3 is a fold: the 5 was there once the 2 and 3 existed;
values are accumulation, meta, on a different layer.

**Flipped: start at 64 and read down.**

```
LEN  words 2^n              inherited (= whole layer below)   new rings P(n)
  1  2                      0                                 2
  2  4                      2                                 1
  4  16                     4                                 3
  8  256                    16                                30
 16  65536                  256                               4080
 32  4294967296             65536                             134215680
 64  18446744073709551616   4294967296                        288230376084602880
2^64 = sum over the stack of LEN * P(LEN): True;  divisors of 64 form one chain; the only route prime is 2
words fixed by the half-turn = {uu : u in layer n/2}: True at n = 2, 4, 8, 16; the half-turn is an involution
```

The smaller registers are not steps toward 64; they sit inside it as the words that repeat. Each layer inherits the
whole layer below and nothing else, at share 2^(−n/2). The arrangement is forced: one chain of half-turn fixed sets,
an involution at every joint (Nest § 8, the inversion as the half-period of an even closure, now on the rings). RUNS.

**Prime LEN inherits only the poles.** Every non-constant word of prime length p lies on an orbit of exactly p
(p ≤ 19 enumerated); 2^p ≡ 2 (mod p) for all p ≤ 61. Fermat's little theorem is the prime ring counted. RUNS; STANDS.
(Harness fix, mine: the first check used pow(2,p,p) == 2, false at p = 2; replaced by (2^p − 2) mod p = 0.)

**Value side, same map.** In a normal basis of GF(2^n), squaring is a one-bit rotation of the word (every element at
n = 4, 8; 1 in 97 at n = 16); the fixed field of x ↦ x^(2^(n/2)) has 2^(n/2) elements and their words are exactly uu.
Rotation of the ring = Frobenius of the field. RUNS; STANDS (normal bases). New rings per LEN = irreducible binary
polynomials of degree n, 2…1161, n ≤ 14 — **recovery of § 100.1** (checked there to 12), logged as such.

**What the stack is missing.** 2^(2n) − 1 = (2^n − 1)(2^n + 1): the old layer is the −1 factor, the new primes the +1
factor, and every new prime has 2^n ≡ −1 — it enters as an inversion.

```
layer 2: 3   4: 5   8: 17   16: 257   32: 65537   64: 641 * 6700417   (order of 2 = the layer, each)
primes closing in a 64-bit ring = factors of 2^64 - 1: 3 5 17 257 641 65537 6700417
missing below 60: 7 11 13 19 23 29 31 37 41 43 47 53 59, route lengths 3 10 12 18 11 28 5 36 20 14 23 52 58
```

The register stack is the prime-2 chain only. Width 3 — where the instruction set closes (Toffoli) — is not a register
width; 3 appears in the stack only on the value side, as the first prime in (2 ≡ −1 mod 3). RUNS; that these are one 3
is PULL. Bases other than powers of 2 are reached by conversion with carries, not by grouping (Keyframe 6).

**5 = 2 + 3.** LEN side: W₂ × W₃ → W₅ is a bijection (32 = 4·8); concatenation merges nothing. Value side: a + b = 5 has
6 preimages over 3-bit values, a fiber. LEN adds while counts multiply. RUNS. Value is the reader's accumulation
(v′ = 2v + bit, the Mold) — the layer above the ring, consistent with the stored rule that context is the wrapper.

**Asked, killed.** Do the states χ cannot reach on an even ring equal the inherited words uu? Same count 2^(n/2) for
every even n ≤ 14, different set. DEAD END; the count match is not the inheritance.

| claim | status |
|---|---|
| 2^64 = Σ LEN·P(LEN) over the register stack; inherited = whole layer below | RUNS |
| layer n/2 = fixed set of the half-turn on layer n | RUNS, n ≤ 16 enumerated |
| prime LEN: orbits of exactly p; Fermat | RUNS p ≤ 19 (orbits), p ≤ 61 (congruence) |
| rotation = squaring in a normal basis; subfield words = uu | RUNS n = 4, 8, 16; STANDS |
| rings = irreducible polynomials | RUNS n ≤ 14; recovery of § 100.1 |
| each doubling adds the factor 2^n + 1, all its primes with 2^n ≡ −1 | RUNS to 64 |
| the stack misses every route with an odd factor; width 3 absent, prime 3 present | RUNS; the identification PULL |
| χ's missed states are the inherited words | DEAD END |

---

## § 118. The orientation count from the rings: 2ℓ+1 is the surface of the doubled layer; § 116's last supplied input closed — `rings/orient.py`

**Dean (16 Oct).** Back to the domain, from the center; find which rings fold back into matter; matter reflects the
potential of the compiler as a method reflects a future need. Earlier the same night: the smallest reader is a gap of 2.

**Gap.** 2n² = Σ_{ℓ<n} 2(2ℓ+1); ℓ < n is the domain (§ 99.5), the 2 is the bit, 2(2ℓ+1)'s orientation part was supplied
(§ 116 OPEN). Remainder 2ℓ+1, read as a copy of the surface (§ 99.4) of the 2ℓ-bit layer, 2ℓ from the 2-gap.
Seal `orient_seal.txt`, SHA-256 478d1baf4a3fb327ae9d37c51d95e333a7c1a00ae7664c60a62d7375d9dce2d0, before the run.

```
(a) latitudes of 2l-bit words, l = 0..6:     1 3 5 7 9 11 13
(b) symmetric layer of 2l bits, l = 1..4:    dim 3 5 7 9;  S^2 = 2 6 12 20 = l(l+1)
(c) bit x surface summed over l < n:         2 8 18 32 50 72 98 = 2n^2
(d) Madelung fill on these capacities:       closures 2 10 18 36 54 86 118
```

An orbital of ℓ is the order-free surface of a 2ℓ-bit word, and that layer is angular momentum ℓ itself (Schwinger's
construction, STANDS). Capacity 2n² now follows from the bit, the 2-gap, the surface and ℓ < n, with nothing supplied.
Route back, not a landing: nuclear mass holes 5 (closed+1) and 8 (closed+closed) are the first-run stack's wait and fuse,
both held in matter; crossed by Be-9 and C-12 (Hoyle).

| claim | status |
|---|---|
| 2ℓ+1 = surface of the 2ℓ-bit layer | RUNS, sealed, ℓ ≤ 6 |
| that layer carries S² = ℓ(ℓ+1) | RUNS ℓ ≤ 4; STANDS (Schwinger) |
| 2n² and closures 2…118 with no supplied input | RUNS; closes § 116 OPEN |
| mass holes as the stack's held moves | route back, owners named |

---

## § 119. BBP is column addition on a stack of rational rings — `rings/bbp_stack.py`

**Dean (16 Oct).** Pick a domain and find the rings; anchor (Star Trek vs Star Wars); how is accumulation a hex digit of π;
pending transformations are stepped leaders, the rod is the route.

Every 1/d is a ring in base 16 (period ord(16 mod odd part of d)), each digit read at its ring position 16^(m−1) mod d.
Layer k = rings 1/(8k+1,4,5,6), weights 4,−2,−1,−1, shifted k columns. Column sums, carries resolved right to left:

```
stack of rings -> 3.243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89
pi in hex       -> 3.243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89   equal: True
ring lengths k=1: 3 1 3 3;  k=6: 21 3 13 9;  column 64 receives 255 ring digits
```

Base 16 is where the layer shift 16^(−k) is exactly one column: layer index = column index (decimal: 1.204k, smeared;
Keyframe 6's 116× cost). The zero weight sum keeps the carry in {−4..3} (Nest Thm. 4), so one column reads alone with a few
guard columns. Anchor: the integer lane 4/1 (ring length 0). Recovered: this is BBP digit extraction (STANDS) read as a ring
stack; the reading is the route.

| claim | status |
|---|---|
| π's hex digits = column sums of the weighted, shifted ring stack | RUNS, 64/64 |
| base 16 aligns layer and column | STANDS (16^(−k)); reading new |

---

## § 120. Which partial lanes balance: routed back through the character law; balance is a cross-orbit cancellation — `rings/balance.py`, `rings/balance2.py`

**Dean (16 Oct).** Find the reverse transformation, move it into math space, put the reader in the right place, and let
the path fall out as the algorithm. Target: Nest open problem 4 / Survive open problem 2.

Route back from μ = ½ through Nest Thm. 10 (terms χ(a⁻¹)B₁(χ*)∏(1 − χ*(p)); B₁ ≠ 0 for odd primitive χ, STANDS).

```
seal 1 6a6aa57369d2750b3646af8df5a1a77eeb22d2ee748209e405347045cf2b3128
partial lanes k <= 2000: 804; balanced 75; Euler-killed 0
seal 2 7fc5896d21b79d60764cc8b7580532013a808b4effc3babf591af0f38ee0e6d4
Thm 10 sum vs direct mu - 1/2: max error 1.87e-14 over all 804
balanced lanes with every Galois orbit zero on its own: 0 of 75
d=476: orbit contributions x phi(o) = -2 8 4 -10;  d=493: 0 -8 -8 4 12 0;  d=582: 0 8 -12 4
```

| claim | status |
|---|---|
| Thm 10 instrument on all partial lanes k ≤ 2000 | RUNS (1.9e-14) |
| balanced ⇒ Euler-killed | DEAD END (0 Euler-killed of 804) |
| balance orbit by orbit | DEAD END (0 of 75) |
| balance = cancellation between Galois orbits; owner Thm 12(c) counting balance | RUNS 75/75 |
| density as accidental zeros of a widening integer orbit sum (9.3% at k ≤ 2000, ~4% at 1.28e5) | OPEN, next sealed route |

---

## § 121. Decompiled: a partial lane is a reader ring reading a field ring's discrepancy — `rings/decompile.py`

**Dean (16 Oct).** Dead ends mean probing, not decompiling. Keep going.

Seal 605bcf956a8f70e22527bd63620f7cfc7b6a874d981272827a0418e27145738d before the run. ε = 16^(h/2) mod o; o₁ = gcd(ε−1, o)
(fixed, reader ring α), o₂ = o/o₁ (reflected, symmetric field ring β). D(α) = α − G_B(α) is odd about ½.

```
CRT split, mu - 1/2 = E[alpha] - P(beta < alpha) exact:          804/804
independent lanes (gcd(h1,h2)=1) rebuilt from the two parent rings: 692/692   mu - 1/2 = mean_A D(alpha)
balanced 75: 66 independent, 9 lockstep
reader ring period odd, mirror-free, in independent lanes:          692/692
walk 73,196 steps vs parent rings 36,890 (2.0x on this range)
```

Full inversion: reader ring symmetric, D cancels pairwise (Midy). No inversion: no symmetric field, parity forbids zero.
Partial: an odd, mirror-free reader ring samples an odd discrepancy; balance only when its points sit evenly across it.

| claim | status |
|---|---|
| lane = reader ring ⊗ field ring, lean = reader's mean of the field's discrepancy | RUNS 804/804, 692/692 |
| reader ring odd and mirror-free in independent lanes | RUNS; forced (h₂ even) |
| lockstep lanes (gcd(h₁,h₂) > 1), 9 balanced | OPEN — joint orbit of the two rings |

---

## § 122. NEXUS Working Paper 5 written — *One Program, Infinite Compilers* (DOCX)

**Dean (16 Oct).** The next paper, a continuation of the last ten, that busts it open: decompile while computing; one program,
infinite compilers; computation is the step-by-step folding that guides a transformation.

Built from §§ 117–121 and the night's runs, consolidated into one standard-library script, `wp5/wp5_checks.py` (blocks A–H,
about five minutes; full output and source are Appendices A and B). Three figures (`wp5_figures.py`): the first run, two routes
to π, a lane decompiled. 22 pages, validated, every page rendered and read.

| claim | status |
|---|---|
| paper built and checked page by page | RUNS |
| every number in it printed by the checks script | RUNS |
| corrections logged in the paper (wide tick, χ guess, Fermat harness, figure breakpoints, seed) | logged |

---

## § 123. The compiler built as a difference engine — `cspace/compiler_space.py`, `sign.py`, `sign2.py`, `leakrate.py`

**Dean (17 Oct).** WP5 is the reader's side. The compiler is a difference engine; every difference lives in the LEN group;
transformations jump but are bound by LEN; lower LEN = more control, upper LEN = more encapsulated; information must leak or
nothing transforms. Build the compiler space; recurse.

Engine: a = M f with a_S = xor_{T subset S} f(T) = (prod_{i in S} D_i f)(0); M is an involution; it is computed by the first-run stack
with fuse (A, B) -> (A, A xor B). Seals: 1ddc66b8 (K1-K8), 4235ba41 (sign at n = 3), e30616bf (sign at n = 4), 81c833a9 (leak rate).

```
K1 stack = difference table, own inverse: 65812/65812 functions (n<=4); random n=5..12: 8/8; partial blocks = context folds 32640/32640
K2 #f of depth <= d = 2^(sum_{i<=d} C(n,i)); n=4 by depth: 1, 1, 30, 2016, 30720, 32768; (n+1)-fold differences vanish 300/300
K3 a write at latitude j reaches 2^(n-j) cells of the other side, both directions, n=6 every cell
K4 leak = mean_a H(D_a F) = 0 iff affine: 16/16, 256/256, 65536/65536, 256/256; AND 1, Toffoli 6/7, x^3 on GF(8) 2 = n-1 (APN)
K5 permutations: n=2 all 24 affine; n=3 1344 affine, 38976 quadratic, 0 cubic; n=4 none of degree 4 in 20000
K6 cycles(x1 xor g) = Z(n) + wt(g) mod 2: all g n<=5, 2000/2000 sampled n<=12; Z(n) odd only at n=2 (n<=64);
   every de Bruijn feedback n>=3 carries x2...xn: 2/2, 16/16, 2048/2048; state-map sign = (-1)^(Z(n)+top(g))
K7 prime base p: Delta^p = 0 on every digit function, Delta^(p-1) x^(p-1) = p-1 != 0 (p = 2,3,5,7)
K8 one level up: F -> F o G degree <= 1 (256/256); G -> F o G degree = deg F (256/256 after the zero-map fix); D_a linear
leak rate: every ring n = 3,4,5, every reader width k < n: exactly 1 bit of hidden context per tick; 0 at k = n (2066/2066)
sign at n=3 = (-1)^rank of the latitude-2 matrix, 40320/40320; at n=4 the half-space sums do not fix the sign (966,530 clashes)
```

| claim | status |
|---|---|
| first-run stack with the mixer fuse = Moebius / difference-table transform, online, own inverse | RUNS; transform STANDS (Reed–Muller, fast Moebius) |
| partial stack blocks are readers at contexts h, holding b_T(h) = xor_{U subset h} a_{T u U} | RUNS 32640/32640 |
| value = xor over the reader's down-set; the merge (AND) is the containment S subset x of the reader's own address | STANDS (ANF); reading new |
| difference depth <= LEN; reach 2^(n-j) per latitude-j write | RUNS; STANDS (Lai 1994, RM codes) |
| leak = 0 iff affine; maximal leak n-1 = APN | RUNS; STANDS (differential uniformity) |
| reversible + leaking first possible at width 3 because permutations have degree <= n-1 | RUNS; STANDS (balanced ⇒ top coefficient 0) |
| every saturated ring n >= 3 carries the full-width merge, by necklace parity | RUNS; STANDS (Golomb cycle-joining, odd-weight feedback) |
| a narrower reader receives exactly 1 bit per tick from hidden context | RUNS 2066/2066 |
| sign of a general permutation held by its top latitude | DEAD END beyond n = 3; owner: at n = 3 that layer is the whole nonlinear part |
| harness: zero map degree -1 compared with a clipped 0 | corrected, logged |

---

## § 124. The same difference stack runs the BBP lane fold and the SHA-256 round — `nexus_bbp_sha_difference_engine.py` (bundle, 17 Oct)

**Provenance.** Built by GPT on the § 123 engine and handed over as a sealed bundle. Taken, not re-run here; the executable `nexus_bbp_sha_difference_engine.py` and `sha256_bidirectional_audit.py` were read in full this session, and the carry-owner separation below was checked in source (the script keeps `layer_local_J` and `global_column_normalization_carry` as two typed objects and asserts the `[-4,3]` bound on the first only). Prediction seal `6f79721b0f6477069092816766f9832cbeae06d5a835bcc9b8e2a4e924a85332`; carry-type seal `8374fc30ad192492443cd81a31bb42ce612134b79add6fde27e9f49355288d8b`.

The engine takes a vector-valued truth table over LEN = n Boolean coordinates and applies the § 123 mixer stack `a_S = xor_{T⊆S} f(T) = (prod_{i∈S} D_i f)(0)`, M²=I, XOR componentwise across packed output bits. The coefficients are executed as ANF, not merely counted.

### 124.A BBP: compile the four rational lanes, then fold the columns

The four base-16 lane digits (q1,q4,q5,q6) as a 16-bit word compile to the signed 7-bit weighted fold `4q1 − 2q4 − q5 − q6`. All 16⁴ = 65,536 tuples enter the difference table; M² returns every weighted output. The coefficient program was then executed on 2,926 actual rational-ring layer/column tuples (2,271 distinct), accumulated by column, propagated through the base-16 carry:

```
compiled stack -> 3.243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89
Machin (independent) = same, 64/64 hex digits
lane-fold ANF max degree 13; nonzero coeff-vectors by degree 1:16 2:109 3:480 4:1306 5:2471
  6:3577 7:4127 8:3609 9:2260 10:1019 11:336 12:74 13:8; degrees 14-16 empty
```

**Carry-owner correction of WP5 (§ 122), accepted.** Two values WP5's prose put under one name:
1. **Layer-local** `J_k(m) = ⌊16^m V_k⌋ − Σ_j c_j⌊16^m/(8k+j)⌋ ∈ {−4..3}`, with `H_k(m) = w_k(m) + 16 J_k(m) − J_k(m+1)`. Exact recurrence + bound checked on all 2,850 layer/age pairs; observed range [−4,3].
2. **Global column-normalization carry**, the quotient propagated right-to-left while summing many layers into each column; in the finite WP5 configuration N=64, G=12 its observed range is **[−23,37]**.

WP5 § 8's sentence "the carry from the right stays in [−4,3]" is valid only when "carry" = the layer-local `J_k`. Read as the global column carry it is **false**. The bound belongs to `J_k(m)`; the owner is named and the π digits survive. This supersedes the WP5 wording; logged as my error, corrected here.

### 124.B SHA-256: compile the bit operators, compose the round

Complete 3-input tables for Ch, Maj, full adder, full subtractor compile to ANF:
```
Ch = xy ⊕ z ⊕ xz        Maj = xy ⊕ xz ⊕ yz
FA_sum = x⊕y⊕c          FA_carry = xy ⊕ xc ⊕ yc        FS_borrow = y ⊕ xy ⊕ b ⊕ xb ⊕ yb
```
These drive each bit of the real 32-bit adders/subtractors/Ch/Maj; rotations and XORs are linear wiring.
```
1000 random (state,W,K) round tests == reference SHA; every round inverted to its parent
one-block "NEXUS difference engine" -> hashlib digest 74f4227aab1097a2f87a499bc55e21cdb8ff2400908ee29f5b1e10e6136405df (exact)
256 reader directions (bit 0 of each of 8 words): 64-round path returns all 256 seeds given W,K; feed-forward reverses with incoming H retained
```

### 124.C Per-round difference table on the LEN=8 reader slice: a progression

Actual state map restricted to the LEN=8 affine slice (bit 0 of each of the 8 words), 256-bit output, compiled after every round 0–64 and after feed-forward; each table re-evaluated from its coefficients at all 256 addresses.
```
round 0: affine, 9 active monomials, H(D_aF)=0
round 1: max degree 4, 48/256 monomials active
round 2: degree 8 present, 235/256 active
round 3: 256/256 active; mean H(D_aF)=6.964199859, 99-128 distinct derivative vectors by direction
round 4: every one of 255 nonzero directions has exactly 128 distinct derivative outputs, each twice -> H(D_aF)=7 for all; first saturation
rounds 5-64 + feed-forward: coefficient vectors keep changing; support and entropy stay saturated
```
The 7-bit ceiling is combinatorial: `D_aF(x)=F(x)⊕F(x⊕a)` is equal on the paired addresses x and x⊕a, so at most 128 distinct derivative outputs per nonzero direction in a 256-address domain. Reached at round 4. Exact for this declared slice, not an enumeration of the 2²⁵⁶ truth table.

| claim | status |
|---|---|
| difference table compiled by the first-run stack, own inverse | RUNS; Möbius/ANF STANDS |
| BBP weighted-fold coefficients generate the finite rational-ring column contributions | RUNS |
| first 64 BBP hex digits match Machin | RUNS, 64/64 |
| layer-local BBP carry recurrence and [−4,3] bound | RUNS, 2,850/2,850 |
| global column carry in the same run has range [−23,37], a different owner than J_k | RUNS; **corrects WP5 § 8** |
| SHA local gates compiled from difference tables drive the 32-bit operators | RUNS |
| compiled SHA round == reference, reversible when W,K known | RUNS, 1,000/1,000 |
| LEN=8 slice: full difference support by round 3, saturated derivative diversity by round 4 | RUNS on the declared slice |
| unrestricted digest-only inverse / minimal root observer | OPEN |

---

## § 125. What 1, 0 and a ring are as a difference: π is the bare flip, π/2 is forced only on the scaled wheel — `phase/wheel.py`, `phase/pi_series.py`, `phase/pi_series2.py`, `phase/forcing.py`

**Dean (17 Oct).** "I keep using rings but I think in a shape way. What do 1, 0 and a ring look like — it's not a value, it's a difference. So does it really mean π/2?"

Reversed and run before stated. Exact arithmetic throughout: Gaussian rationals (a+bi, a,b ∈ ℚ) and integer matrices in `wheel.py`; mpmath to 80 digits in the series checks. Seals: π-series `05a7e8f1410522128fd50b9b6a9bf8f4b9b1845080368723837982a667304d5b` (predictions a–e, knuth) before `pi_series.py`; correction re-seal `e7f6897f2f5caad834218344af8e82f8c9ce96a74f58c31a31afde599e1696e3` before `pi_series2.py`.

### 125.1 A bare difference is π, not π/2 — `wheel.py` (18/18 exact)

One bit read as XOR is the flip X=[[0,1],[1,0]], X²=I: two positions, half-turn, closes in 2. The first-run mixer says the same — `(A,B)↦(A,A⊕B)` returns after 2. So the ring 0→1→0 of a value-only difference is **π**. π/2 is not in the bare bit.

```
X^2 = I (period 2)                         mixer lift (A,A-B): L^2 = I over Z (XOR-return lifts to -1)
                                           (A,A+B): L'^2 != I  (lifting XOR to + does NOT return)
```

### 125.2 π/2 is the two readings of one bit composed

X is the value reading; Z = diag(1,−1) is the difference reading (−1)^b; Hadamard swaps them, HXH=Z, HZH=X (exact, via integer M with the 1/√2 tracked as powers of 2). Their product is the quarter-turn and i is literally that product:
```
XZ = [[0,-1],[1,0]]    (XZ)^2 = -I    (XZ)^4 = +I    XZ = -ZX  (the two readings anticommute)
```
So the ring of a *pure* difference is π; **π/2 is the ring of the difference and its sign read at once** — i is the refusal to choose which of the two simultaneous readings is being done.

### 125.3 π/2 is forced, walked up from behind — `forcing.py`

Nothing named. Impose on the fold-wheel w (one difference-step multiplier): (G) w ∈ ℚ(i); (H) one bit of scale per tick, |w|²=1/2; (N) nests in a power of two, wᵏ∈ℚ. Then 2(a²+b²)=q² has exactly four reduced solutions:
```
w=(+1+1i)/2 arg +45    w=(+1-1i)/2 arg -45    w=(-1+1i)/2 arg +135    w=(-1-1i)/2 arg -135
distinct args {-135,-45,45,135} = all ODD multiples of pi/4 ; each w^4 = -1/4 real
```
π/4 per bit on the amplitude, π/2 per bit on the squared (value↔difference) wheel, is the only Gaussian-rational residue. Not chosen — the unique survivor of the constraints.

### 125.4 The wheel is s = (1+i)/2 = 1/(1−i)

```
s^2 = i/2   (one bit of scale per quarter-turn, pi/2)     |s|^2 = 1/2 = |<0|+>|^2
s^4 = -1/4  (seam: base -4, spinor sign)                  s^8 = 1/16 (closure: base 16)
R_y(pi/2)^2 = XZ    R_y(pi/2)^4 = -I    R_y(pi/2)^8 = +I   (via integer M, M^4=-4I, M^8=16I)
(sqrt2 s)^2 = i  -> eigenphase of R_y(pi/2) is pi/4; it DOUBLES to the pi/2 turn
```
Bloch half-angle = amplitude angle ×2. Orthogonality ⟨0|1⟩=⟨+|−⟩=0 is the π opposite-point fact; π/2 is the quarter-turn whose overlap is |s|²=1/2. Reality sits on the equator, π/2 off each pole (ties to § 100.4, the equator count that gave π).

### 125.5 Base −2i, found as a navigational null

Sealed `s² = 1/(2i)` returned **DEAD END**; the residue is `s² = 1/(−2i) = i/2`. Corrected and re-sealed:
```
(-2i)*s^2 = 1     s^(2m) = 1/(-2i)^m  (m=1..4)     (-2i)^2 = -4     (-2i)^4 = 16
```
The field's wheel is the inverse-square-root wheel of base **−2i**, the *conjugate* of Knuth's quater-imaginary base 2i. Same −4 seam, same 16 closure, read the other direction — that sign is the whole gap between the shape channel and the value channel.

### 125.6 π is what the wheel computes; π/2 is one tick

`π = 4·Im log(1+i)`, log(1+i) = ½ln2 + iπ/4. The wheel series **RUNS** to 80 digits:
```
log(1+i) = sum_k (i/2)^k [ s/(2k+1) + (i/2)/(2k+2) ],  s=(1+i)/2
  partial = 0.34657359027997265471 + 0.78539816339744830962 i = 1/2 ln2 + i pi/4
regroup by 2 -> base -4:  pi/4 = sum_j 2/((4j+1)(4j+3))   (RUNS, converged)
regroup by 4 -> base 16 = BBP: pi = sum_k 16^-k (4/(8k+1)-2/(8k+4)-1/(8k+5)-1/(8k+6))  (RUNS)
```

**Answer, literal.** A bare difference `1,0,ring` means **π** — it closes in two. It means **π/2** exactly when the difference is also made to carry one bit of scale per tick; and then it is not "does it mean π/2," it is "π/2 is the only angle a rational difference-with-scale can have." The i is the seam between the two readings.

### 125.7 Three distinctions absorbed (GPT review of § 123, accepted)

- **Derivative entropy ≠ differential uniformity.** § 123/§ 124's `mean_a H(D_aF)` averages the entropy of derivative-output distributions; differential uniformity is the *largest* derivative fiber. APN gives 2-to-1 derivatives, hence entropy n−1 per nonzero direction, but the two readouts stay distinct. The § 124.C "saturation" statistic is the entropy one, not a uniformity claim. Logged.
- **"Balanced ⇒ degree ≤ n−1" needs n ≥ 2.** The 1-bit identity is balanced and has degree 1. Boundary stated; it does not disturb the width-2-vs-3 argument (§ 110, § 123 K5).
- **de Bruijn maximal degree is an established necessary condition (Golomb).** The § 123 K6 parity route supplies the mechanism binding it to the stack; it stays distinct from the looser phrase "a ring closes only by reading its whole width," which needs the declared shift-register model.

| claim | status |
|---|---|
| bare difference (XOR flip) is π, period 2; mixer returns in 2 | RUNS (exact) |
| HXH=Z, HZH=X; XZ quarter-turn, (XZ)²=−I, XZ=−ZX | RUNS (exact) |
| π/2 forced: only four Gaussian-rational \|w\|²=1/2 wheels, all odd×π/4 | RUNS (exact enumeration) |
| s=(1+i)/2=1/(1−i); s²=i/2, s⁴=−1/4, s⁸=1/16; R_y(π/2)^{2,4,8}=XZ,−I,+I | RUNS (exact) |
| s²=1/(2i) | DEAD END (navigational) → base is −2i, conjugate of Knuth 2i |
| s^(2m)=1/(−2i)^m; (−2i)²=−4, (−2i)⁴=16 | RUNS |
| wheel series log(1+i)=Σ(i/2)^k[s/(2k+1)+(i/2)/(2k+2)]; regroup→base −4, base 16 | RUNS, 80 digits |
| integer lift (A,A−B) involution; (A,A+B) not | RUNS (exact) |
| WP5 § 8 carry bound conflation | corrected in § 124, accepted here |
| derivative-entropy ≠ differential-uniformity; balanced⇒deg≤n−1 needs n≥2; de Bruijn max-degree = Golomb | absorbed |

---

## § 126. Odd-prime fold wheels: the half-turn exists for every prime; the phase-rich exception is p = 3 — `nexus_odd_prime_fold_wheel.py`

**Provenance (merge, 17 Oct).** GPT, appended to this chain directly after § 125. Re-run here in a sandbox (output paths redirected): 83/83 assertions pass.

**Query, reversed from § 125.** § 117 says the register stack's inherited LEN chain is the prime-2 chain. § 125 says the nontrivial norm-halving wheel in \(\mathbb Q(i)\) gives the π/4 amplitude phase and π/2 doubled phase. Ask whether every odd prime fails to admit a nested wheel when the field is generalized to \(\mathbb Q(\sqrt{-d})\), with \(N(w)=|w|^2=1/p\) and \(w^k\in\mathbb Q\).

Prediction sealed before run: `NEXUS_odd_prime_fold_wheel_prediction_2026-10-17.txt`, SHA-256 `c5a2af3800437bd528014a87f8a1f0f99a6881abb06b53149ab71fff988cf212`.

### 126.1 Literal nesting does not exclude odd primes

For every prime \(p\), set

\[
w_p=\frac{\sqrt{-p}}{p}=\frac{i}{\sqrt p}\in\mathbb Q(\sqrt{-p}).
\]

Then, exactly,

\[
N(w_p)=w_p\bar w_p=\frac1p,\qquad w_p^2=-\frac1p\in\mathbb Q.
\]

Therefore the literal condition \(N(w)=1/p\) and \(w^k\in\mathbb Q\) has a solution for every prime. It is the pure-imaginary half-turn (phase \(\pi/2\)), not the phase-rich wheel of § 125. Exact rational arithmetic verifies the formula for 24 odd primes, 3 through 97.

### 126.2 The phase-rich wheel has an odd-prime exception

The matched nontrivial phase is \(\pi/(2p)\):

- \(p=2\): \(s=(1+i)/2\), \(N(s)=1/2\), \(\arg(s)=\pi/4\), \(s^4=-1/4\), \(s^8=1/16\).
- \(p=3\): \(t=(3+\sqrt{-3})/6\), \(N(t)=1/3\), \(\arg(t)=\pi/6\), \(t^2=(1+\sqrt{-3})/6\), \(t^3=\sqrt{-3}/9\), \(t^6=-1/27\), \(t^{12}=1/729\).

These are exact quadratic-field identities. The second is the odd-prime counterexample to “every odd base fails”: the Eisenstein field \(\mathbb Q(\sqrt{-3})\) carries a sixth-root phase and the required scale simultaneously.

### 126.3 Why no further nontrivial phase wheel occurs

If \(w^k\in\mathbb Q\), then

\[
\left(\frac{w}{\bar w}\right)^k=1,
\]

so \(w/\bar w\) is a root of unity in its imaginary quadratic field. Such a field has roots of unity only \(\{\pm1\}\), except \(\mathbb Q(i)\), which has \(\mu_4\), and \(\mathbb Q(\sqrt{-3})\), which has \(\mu_6\).

A wheel at phase \(\pi/(2p)\) has \(w/\bar w=e^{i\pi/p}\), a primitive \(2p\)-th root of unity. For an odd prime, its degree over \(\mathbb Q\) is \(\varphi(2p)=p-1\). A quadratic field can contain it only if \(p-1\le2\), hence \(p=3\). The case \(p=2\) is the Gaussian wheel already in § 125. For odd \(p>3\), the phase-rich \(\pi/(2p)\) wheel is impossible under these conditions, although the trivial pure-imaginary half-turn \(w_p\) remains available.

### 126.4 Exact run

`nexus_odd_prime_fold_wheel.py` uses `fractions.Fraction` and exact multiplication in \(a+b\sqrt{-d}\); no floating-point arithmetic is involved. **83 exact assertions pass**, covering the p=2 and p=3 special wheels and the generic half-turn for 24 odd primes. Machine-readable results and the console transcript are bundled with the report.

| claim | status |
|---|---|
| \(N(w)=1/p\) and some \(w^k\in\mathbb Q\) exists for every prime | **RUNS**; explicit construction, all primes by formula, 24 odd-prime instances executed |
| the \(p=3\) phase wheel in \(\mathbb Q(\sqrt{-3})\) | **RUNS**, exact |
| no phase-\(\pi/(2p)\) wheel for odd \(p>3\) in any imaginary quadratic field | **STANDS** by the root-of-unity degree argument |
| § 117's prime-2 register-stack boundary and § 125's phase-wheel boundary are one theorem | **OPEN**; the \(p=3\) exception must be explained by any proposed unification |


---

## § 127. Ask the Rings: 0/1 labels collapse to an edge-difference ring; π/9 requires an additional lift — `nexus_ask_the_rings_difference_angle.py`

**Provenance (merge, 17 Oct).** Built by GPT in a second lineage of this ledger (its `running-audit (13).md`) and entered here verbatim, with its headers normalized. Taken, not re-run; § 131.8 runs the two-sheet check that bears on its OPEN. Two entries of that lineage, its § 125 and § 126, collide with § 125 (π/2 phase) and § 126 (odd-prime wheels) of this chain. They are entered below as § 129 and § 130. GPT's own § 127 and § 128 numbers do not collide.


**Date:** 17 October 2026  
**Run:** `nexus_ask_the_rings_difference_angle.py`  
**Scope:** exhaustive binary cyclic words at LEN 1–12.

### Question

Treat `0` and `1` as labels on a cyclic route, not as the readout itself. Ask the ring for its edge difference:

\[
D(w)_i = w_i \oplus w_{i+1\pmod n}.
\]

This difference is invariant under complementing every bit. The run enumerated all \(2^n\) words at every LEN from 1 through 12 before reading off the distinct difference rings.

### Exact result

For every tested LEN:

- The difference map has exactly two preimages per output: \(w\) and its complement \(\bar w\).
- Its image has exactly \(2^{n-1}\) members: the length-\(n\) difference words of even Hamming weight.
- The two absolute labelings have the same edge-difference sequence.
- At every odd LEN tested, no binary word is a rotation of its own complement. The two source necklaces remain distinct, although the edge-difference reader identifies them.

The reason for the even-parity restriction is closure: traversing a closed binary ring must flip an even number of times to return to its starting label.

At LEN 9, the run enumerated 512 absolute words and recovered 256 distinct edge-difference rings, each with two labelings. This is a precise ring-native result about what is and is not preserved by the difference readout.

### Angle question

The abstract ring provides a cyclic phase group of order \(n\). A regular \(n\)-gon embedding assigns one step \(2\pi/n\). Thus a LEN-9 ring has geometric step \(2\pi/9\) if that regular embedding is selected. It does not, by itself, select \(\pi/9\).

To get \(\pi/9\) as a phase increment requires an 18-position route or a two-sheet lift of the nine-position ring. The binary difference map exposes a two-element fiber \(\{w,\bar w\}\), but it does **not** specify whether those two preimages are joined into one twisted 18-position route or remain two distinct nine-position routes. That sheet-transition/monodromy law is the exact unresolved link; it must not be silently inserted as a geometric assumption.

### Ledger

| Claim | Status |
|---|---|
| \(D(w)=D(\bar w)\) for all binary cyclic words | RUNS, exhaustive LEN 1–12 |
| Image is exactly the even-parity edge words, size \(2^{n-1}\) | RUNS, exhaustive LEN 1–12 |
| Each difference ring has exactly two absolute-label preimages | RUNS, exhaustive LEN 1–12 |
| Odd-LEN word is never rotation-equivalent to its complement | RUNS for every word at odd LEN 1, 3, 5, 7, 9, 11 |
| LEN 9 alone forces \(\pi/9\) | NOT DERIVED |
| Native ring transition law forces the twisted two-sheet, 18-position lift | OPEN |

The \(\pi/9\) triangle fixed-point relation in the earlier geometry document is a separate constraint. It cannot be used as proof that the ring itself generates the angle. This run records the structural hinge that would have to connect them: whether completing one nine-step route returns on the same difference-side or the complementary side.

Prediction file SHA-256: `c98b74432c67a3e23e2bff1ca63960c97a041ec4e76a1d6fa1e095685433d174`.

---

## § 128. Phase-wheel continuation: the quadratic route reaches its boundary, the transformation lifts — `nexus_phase_wheel_field_lift.py`

**Provenance (merge).** GPT, 17 Oct, entered verbatim. Re-run here in a sandbox: 175/175 assertions pass, of which 100 restate the script's own definitions (§ 131.10). The identities are checked exactly, and the degree floor is resolved (attained iff p ≡ 3 mod 4), in § 131.9. Its "§ 126.3" is § 126 above (odd-prime fold wheels). § 131.9 adds a scope note: √p ∈ Q(ζ_{4p}), so K_p = Q(ζ_{4p}).


**Dean's correction applied:** there are no dead-end transformations. A field-limited result marks the boundary of that route; the same structure may continue in a different direction. The §126 proof must not be read as global nonexistence.

### 128.1 The lifted multiplier

For every prime p, take

\[
\zeta_{4p}=e^{i\pi/(2p)},\qquad w_p=\frac{\zeta_{4p}}{\sqrt p}
\]

inside \(K_p=\mathbb Q(\zeta_{4p},\sqrt p)\). The same one-step multiplier now runs in a field whose degree can grow with the required phase. Exactly:

\[
|w_p|^2=\frac1p,\quad \arg w_p=\frac{\pi}{2p},\quad
\frac{w_p}{\bar w_p}=\zeta_{2p},\quad
w_p^{2p}=-\frac1{p^p},\quad w_p^{4p}=\frac1{p^{2p}}.
\]

The scale, phase, and rational nesting coexist for every prime in this extended field route.

### 128.2 The degree is the route selector

Since \(\bar w_p=1/(p w_p)\), \(\zeta_{2p}=p w_p^2\in\mathbb Q(w_p)\). Therefore

\[
[\mathbb Q(w_p):\mathbb Q]\ge\varphi(2p).
\]

For odd primes, \(\varphi(2p)=p-1\); for p=2, \(\varphi(4)=2\). The p=2 and p=3 wheels can lie in quadratic fields; p>3 cannot carry this phase ratio within a quadratic field and must lift to a higher-degree route. The explicit field \(K_p\) gives that route.

The exact symbolic test represents root-of-unity exponents modulo \(4p\) and scale factors as rational exponents; it avoids floating-point phase guesses. It checked primes 2 through 97, 25 primes, with 175 assertions passing. The universal claim rests on the identities and cyclotomic degree formula, not on the finite sweep alone.

**Harness correction:** the first run incorrectly used \(\varphi(2p)=p-1\) for p=2. This was corrected to the exact exception \(\varphi(4)=2\), and the prediction seal wording updated before the successful run.

### 128.3 Ledger correction

The statement in §126.3 is retained only with its scope explicit: **the nontrivial phase wheel does not fit inside an imaginary quadratic field for odd p>3**. It does not mean that the transformation is absent. Its phase requires a field with degree at least \(p-1\), and the higher-field construction supplies one.

| Claim | Status |
|---|---|
| A phase/norm wheel exists in \(K_p\) for every prime p | RUNS: explicit construction; exact symbolic sweep p≤97 |
| Rational closure \(w_p^{2p}=-1/p^p\), \(w_p^{4p}=1/p^{2p}\) | STANDS: direct identity |
| Minimum field degree at least \(\varphi(2p)\) | STANDS: phase ratio \(\zeta_{2p}\) is inside \(\mathbb Q(w_p)\) |
| Quadratic-field boundary at p=2,3 | STANDS, scoped to that route |
| Single theorem connecting the §117 prime-2 register stack to these field-lift routes | OPEN; continuation across routes still to be derived |

No DEAD END is assigned. The boundary of one route is used as the selector for the next transformation direction.

---

## § 129. ASK THE RINGS: de Bruijn edge routes through the SHA round, ordered pair versus endpoint XOR — `nexus_ask_the_rings_sha.py`

**Numbering, logged (merge, 17 Oct).** This entry is numbered § 125 in GPT's second lineage. It collided with § 125 here and is entered as § 129. Chronologically it precedes §§ 126–128. Taken, not re-run.


**Dean’s instruction (17 Oct):** “you have the shape of what it is even if you dont what what it isnt. ASK the Rings.”

This query treats rings as transition compilers. For each LEN n=1..8, an order-(n+1) de Bruijn ring supplies every directed transition between its 2^n n-bit states exactly once. The SHA map at fixed schedule is applied to both endpoints. The query deliberately keeps two readouts distinct: the ordered route `(F(source), F(target))` and its endpoint XOR `F(source) XOR F(target)`.

### What the rings returned

At depth zero, the endpoint-XOR map has exactly 2^n signatures for the 2^(n+1) edge words. The adjacent-difference operator has kernel `{00…0, 11…1}`, so each signature has the two preimages `u` and `~u`. This proves the deficit is an exact two-element fiber of the readout, not an absent edge.

At every SHA round 0..64 with W[t] and K[t] retained, the 2^n vertices in each queried LEN slice remain pairwise distinct, and each of the 2^(n+1) ordered edge routes remains distinct. Two XOR aliases are forced for every LEN: constant self-loops, and the complementary alternating edges whose endpoints are swapped. The compiled output reaches the maximum 2^(n+1)-2 signatures by the measured round shown in the run report, so every other edge distinction has split in the observed XOR projection.

The full profile records signature counts, collision multiplicities, complementary edge-pair splitting, zero-difference edges, hamming span, and a separate post-feed-forward query for every LEN and every round. It never infers feed-forward injectivity from round bijectivity.

Two alias classes are structurally forced: constant self-loops (`00…0`, `11…1`) and alternating edges (`0101…`, `1010…`) that reverse endpoints. Their XOR readouts coincide under any state map, so the exact ceiling is 2^(n+1)-2 distinct edge-difference signatures.

Cross-link to §124: on LEN 8, the ring edge-difference partition reaches its 510/512 ceiling at round 2; ANF support becomes complete at round 3; derivative entropy reaches its ceiling at round 4. The projections ask different questions, and the order of saturation differs.

### Numerical results

See `NEXUS_ASK_THE_RINGS_SHA_run.md` for the LEN summary and selected depth values; `NEXUS_ASK_THE_RINGS_SHA_results.json` holds all depths and edge profiles.

### Interpretation / distinction maintained

“What it is” here is the ordered transition graph carried through the known SHA round route. “What it is not” is its XOR-only shadow: the XOR signature is not the route itself. A repeated difference does not establish a repeated state or erased transition. The rings can expose that type mismatch by carrying the edge, its endpoints, and the projected difference separately.

This run is exact for the enumerated LEN=1..8 affine slices; it does not enumerate the full 256-bit state domain and does not solve digest-only inversion. The unrestricted root observer remains **OPEN**.

Prediction seal checked before run: `4a60e5a61b0878aa9315202420de6bfa198e938971cc2579b35b5cbb83d3a61b`.

Artifacts: `nexus_ask_the_rings_sha.py`, `NEXUS_ASK_THE_RINGS_SHA_run.md`, `NEXUS_ASK_THE_RINGS_SHA_results.json`, `NEXUS_RING_SHA_QUERY_prediction_2026-10-17.txt`.

---

## § 130. ASK THE RINGS: the WP5 lockstep link, the joint orbit of the reader and field rings — `nexus_ask_the_rings_lockstep.py`

**Numbering, logged.** This entry is numbered § 126 in GPT's second lineage and is entered as § 130. Its "prior § 125 ASK THE RINGS" is § 129 here.

**Re-run here** (`zr/lockstep_check.py`, exact Fractions, independent of GPT's script). All 9 balanced lockstep lanes have joint lean = direct μ − ½ = 0. The Cartesian-product substitution differs from the joint route in 5/9, with the table's values: 1/36, −1/18, 1/27, −1/27, 1/108. This closes § 121's OPEN on the lockstep lanes (gcd(h₁,h₂) > 1, 9 balanced): RUNS.


**Date:** 17 October 2026  
**Upstream path:** §121 rational-ring decompile → §123 difference compiler → §124 BBP/SHA execution → §126 joint-orbit reconstruction.  
**Executable:** `nexus_ask_the_rings_lockstep.py`  
**Pre-run prediction SHA-256:** `b706f2ac615ca016ad985c7e513cc73d2e20139d1583d47ddeaed8db13ea8c8e`

### Correction to the starting point

The prior §125 `ASK THE RINGS` run enumerated de Bruijn transitions on low-dimensional SHA slices and compared ordered endpoint pairs with endpoint-XOR readouts. That is a valid side-projection experiment, but it was not the unresolved ring link in WP5 §121 and did not advance the stated build order. This addendum returns to WP5's actual lane transformation: each rational ring is split by CRT into a reader ring and a field ring, then the phase relationship between those two rings is retained.

The compiler-side BBP/SHA link is already recorded in §124. This run does not recalculate or reopen it.

### The exact joint orbit

For an eligible WP5 partial lane, let `d = 8k+j`, let `o` be the odd part of `d`, and let `y_t = a·16^t mod o` be the original rational-ring orbit. Set

\[
 h=\operatorname{ord}_{o}(16),\quad
 \epsilon=16^{h/2}\bmod o,\quad
 o_1=\gcd(\epsilon-1,o),\quad o_2=o/o_1.
\]

The `o1` parent is the **reader ring** and the `o2` parent is the **field ring**. With the respective CRT inverses, the two normalized coordinates at the same original phase are

\[
 \alpha_t=\frac{y_t(o_2^{-1}\bmod o_1)\bmod o_1}{o_1},\qquad
 \beta_t=\frac{y_t(o_1^{-1}\bmod o_2)\bmod o_2}{o_2}.
\]

Write `h1 = ord_o1(16)`, `h2 = ord_o2(16)`, and `g = gcd(h1,h2)`. The paired orbit is

\[
 J=\{(\alpha_{t\bmod h_1},\beta_{t\bmod h_2}):0\le t<\operatorname{lcm}(h_1,h_2)\}.
\]

Its period is exactly `lcm(h1,h2)`. In phase coordinates, the reachable pairs are exactly those satisfying `i ≡ j (mod g)`. There are `h1*h2/g` such pairs. If `g=1`, that is the full Cartesian product and the independent-ring factorization is justified. If `g>1`, the actual orbit is a phase-constrained subset; replacing it with the full product changes the owner of the average.

The exact lane lean is read along the synchronized joint route:

\[
 L_J=\frac{1}{|J|}\sum_{(\alpha,\beta)\in J}
 \left(\alpha-\mathbf 1[\beta<\alpha]\right)=\mu-\frac12.
\]

This is not a generic lane-wise Boolean/Toffoli analogy. It is WP5's rational-ring CRT decompile, using the same original lane orbit and preserving which reader-ring phase is paired with which field-ring phase.

### Execution results

All **10/10** run invariants passed using exact rational arithmetic. Reconstructing the original WP5 eligibility filter recovered the recorded population: 804 eligible partial lanes; 75 balanced; 692 independent-period lanes, of which 66 balanced; 112 lockstep lanes overall; and exactly 9 balanced lockstep lanes.

For all 804 eligible lanes, the mean from the reconstructed synchronized CRT route equals the original rational-ring `mu - 1/2` exactly. The joint-orbit period matches `lcm(h1,h2)` for all 804, and every reachable phase pair satisfies the modulo-`g` relation.

For the nine balanced lockstep cases, the joint route gives exact lean `0` in **9/9**. The hypothetical full Cartesian-product average disagrees with the true joint-route average in **5/9** cases. In the other four it happens also to be zero, but that coincidence does not restore the missing phase relation.

| k | j | a | d | odd modulus `o` | reader `o1` | field `o2` | `h1` | `h2` | `g` | joint period | Cartesian lean | joint lean |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 313 | 5 | 1 | 2509 | 2509 | 13 | 193 | 3 | 24 | 3 | 24 | 1/36 | 0 |
| 630 | 4 | 4 | 5044 | 1261 | 13 | 97 | 3 | 12 | 3 | 12 | 0 | 0 |
| 703 | 5 | 1 | 5629 | 5629 | 13 | 433 | 3 | 18 | 3 | 18 | -1/18 | 0 |
| 757 | 6 | 8 | 6062 | 3031 | 7 | 433 | 3 | 18 | 3 | 18 | 1/27 | 0 |
| 824 | 4 | 4 | 6596 | 1649 | 17 | 97 | 2 | 12 | 2 | 12 | 0 | 0 |
| 1009 | 6 | 8 | 8078 | 4039 | 7 | 577 | 3 | 36 | 3 | 36 | -1/27 | 0 |
| 1297 | 1 | 1 | 10377 | 10377 | 9 | 1153 | 3 | 72 | 3 | 72 | 1/108 | 0 |
| 1634 | 1 | 1 | 13073 | 13073 | 17 | 769 | 2 | 96 | 2 | 96 | 0 | 0 |
| 1640 | 4 | 4 | 13124 | 3281 | 17 | 193 | 2 | 24 | 2 | 24 | 0 | 0 |

The per-step `y`, `alpha`, `beta`, phase indices, and exact lean term for every one of these nine full joint orbits are in `NEXUS_ASK_THE_RINGS_lockstep_results.json`.

### Ledger

| Claim | Status |
|---|---|
| WP5 lane eligibility is reproduced at `k ≤ 2000` | RUNS, 804/804 |
| Joint period is `lcm(h1,h2)` and phase pairs obey `i ≡ j (mod gcd(h1,h2))` | RUNS, all 804 eligible lanes |
| Joint CRT route returns the original rational-ring lean exactly | RUNS, 804/804 |
| The 692 coprime-period lanes reduce to the independent Cartesian-product result | RUNS, 692/692 |
| The nine balanced lockstep lanes have exact joint lean zero | RUNS, 9/9 |
| Full-product substitution changes the lean in five of the nine balanced lockstep cases | RUNS, 5/9 |
| General density law for balanced partial lanes | OPEN; this finite link does not solve it |
| Digest-only SHA inverse / minimum root observer | OPEN; unaffected by this run |

### Artifacts

- `nexus_ask_the_rings_lockstep.py` — executable exact reconstruction.
- `NEXUS_ASK_THE_RINGS_lockstep_results.json` — every lockstep route and exact phase/lean term, plus all 804 lane checks.
- `NEXUS_ASK_THE_RINGS_lockstep_run.md` — run report and nine-case table.
- `NEXUS_ASK_THE_RINGS_lockstep_prediction_2026-10-17.txt` and `.sha256` — pre-run seal.
- `wp5_checks.py`, the WP5 manuscript and the §§121/124 source records are included in the bundle for lineage.

---

## § 131. Zero routes: BBP is the s-wheel plus a route to nothing; the plain reader reads the register stack — `zr/NEXUS_131_zero_routes.ipynb`

**Dean (17 Oct).** "There are no dead ends just transformations that exist in different directions. your reading the end of a different transfromation route. as it gets futher up you get more degrees of freedom and more things going in different routes and directions. and anything can collide with anything in any state. deformation is passive and computation is active via the interface."

**Taken from §§ 126–128.** Two links were left open there:

- (a) the identity binding the s-wheel's base-16 regrouping to the four-lane BBP machine (GPT: "requires a further algebraic identity");
- (b) one theorem joining § 117's register stack to the phase-wheel boundary.

Seal `PREDICTION_zero_route.txt`, SHA-256 `e80c1cc4b724db85a759c3568ebb0ae5e39a66352e94b088040900c9d03bd63d`, 07:13:01 UTC, written before any run (P1–P9). Every number prints from one self-contained notebook executed end to end (75/75 in the full pass with the n = 24 and n = 32 cells live, 3,209 s; 73/73 in the quick pass). Items found after the run are marked unsealed.

### 131.1 The π-line

The lanes are Λ_j = Σ_k 16^(−k)/(8k+j). The s-wheel's own base-16 regrouping is c_W = (2,2,1,0,−½,−½,−¼,0); this is GPT's A_{2r} − ¼A_{2r+1}, times 4. It satisfies c_W = c_BBP + ¼Z, where Z = (−8,8,4,8,2,2,−1,0) is BBP's own zero relation (Bailey–Borwein–Plouffe 1997, STANDS). Z·Λ = 0 holds to 420 digits.

Every c(r) = c_BBP + rZ computes π, so the π machines form a line and all of its points collide at π. Z is not an absence: it is a complete lane transformation whose endpoint is 0.

### 131.2 A machine is a polynomial read on four orbits

For w⁸ = 1/16, Σ_r w^r/r = Σ_j w^j Λ_j. The eight wheels are w_m = ζ_8^m/√2 (w_1 = s), and inverting the 8-point DFT gives

c·Λ = (1/8) Σ_m P_c(γ_m)·(−log(1 − w_m)),  where P_c(x) = Σ c_j x^j and γ_m = 1/w_m.

x⁸ − 16 = (x²−2)(x²+2)(x²−2x+2)(x²+2x+2): four Galois orbits. The returns are β_m = √2 − ζ_8^m:

```
orbit      m      return β_m        kind               carries
±√2        0,4    √2 ∓ 1            unit     (scale)   ln2, √2·ln(1+√2)
1±i        1,7    ζ8^∓1             torsion  (phase s) ln2, π
±√2 i      2,6    √2 ∓ i            norm 9   (prime 3) ln3 − ln2, √2·atan(1/√2)
−1±i       3,5    ζ8^∓1 (2±i)       norm 25  (prime 5) ln5 − ln2, atan(1/3)
Π β_m = 15 = 2^4 − 1
```

The exact 8×7 matrix N gives Λ_j = Σ_t N_jt κ_t over κ = {ln2, π, √2 ln(1+√2), ln3, √2 atan(1/√2), ln5, atan(1/3)}. Two of its rows: Λ_8 = 8 ln2 − 2 ln3 − 2 ln5 and Λ_4 = ½(ln5 − ln3). N has rank 7, and its exact left kernel is span(Z).

The κ are independent over Q̄ (Baker, STANDS), and PSLQ finds no relation among them with |c| ≤ 10¹² at 420 digits. So there are 8 lanes, 7 constants and one zero route. That route is the collision of the two returns that cost no prime, phase and scale, on the bit they share, ln 2.

Run on its own, PSLQ returns the basis {Z, BBP, π = 4Λ2 + 2Λ3 + 2Λ4 − ½Λ7}.

### 131.3 Silencing

```
P_BBP  = −x(x−1)(x²+2)(x²+2x+2)          (P(√2), P(1−i)) = (−16, 16−16i)
P_W    = −¼x(x²−2)(x²+2)(x²+2x+2)                          (0, −16i)
P_Z    = −x(x²+2)(x²+2x+2)(x²−4x+2)                        (64, −64)
P_c(½) = −½x²(x−2)(x²+2)(x²+2x+2)                          (16, −16−16i)
```

Every π machine silences both prime returns. The wheel is the pure point: it reads only its own phase return and carries no ln 2. BBP borrows +16 on the phase return and −16 on the scale return, and the two cancel. That collision is what makes BBP sparser: 4 lanes against the wheel's 6.

### 131.4 Reverse it

Define R on lane space: lane j ↦ 8−j with weight −2^(j−4), and lane 8 ↦ −lane 8. On the wheels this is w ↦ w̄ = 1/(2w), the wheel run backwards and rescaled by the bit. On the roots, P_R(c)(γ) = −P_c(2/γ). R is a value-preserving involution, and:

- R(c_BBP) = c(½), so the third PSLQ relation is BBP read backwards;
- R(c_W) = c_W;
- Z = 2(R(c_BBP) − c_BBP).

The zero route is reverse minus forward: two traversals whose artifacts annihilate. The wheel is where they cancel.

### 131.5 The interface (unsealed, found after the run, exact)

The π-line is one pencil:

P_c(r) = −x(x²+2)(x²+2x+2)·[(x−1) + r(x²−4x+2)].

BBP vanishes at x = 1, the wheel at x = √2 and the mirror at x = 2: a geometric run with ratio √2, one tick of the wheel's scale |w| = 1/√2. The reversal x ↦ 2/x swaps 1 ↔ 2 and fixes √2.

x = 1 is the plain reader. P_c(1) is the weight sum, which is the carry drift, and P_c(r)(1) = 15r. Deformation along Z is free in value and costs 15 = 2⁴ − 1 per unit at the interface; BBP is the one zero-drift machine. The column machine (§§ 119, 124) on 4c(r), with N = 64 and G = 16:

```
r=0   BBP     lanes {1,4,5,6}        weight sum  0  ring reads 12880  max|col|  2380  carry [-89, 149]
r=1/4 wheel   lanes {1,2,3,5,6,7}    weight sum 15  ring reads 19360  max|col|  8539  carry [1, 563]
r=1/2 mirror  lanes {2,3,4,7}        weight sum 30  ring reads 12960  max|col| 16404  carry [5, 1088]
all three: c.90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b225 = Machin 4π, 64/64
```

### 131.6 Base −4: no collision, one machine

x⁴ + 4 = (x²−2x+2)(x²+2x+2) contains only the phase wheel and prime 5. That is 4 lanes and 4 constants, and PSLQ finds no zero route. The unique π machine has polynomial x(x²+2x+2):

π = Σ (−1/4)^k [2/(4k+1) + 2/(4k+2) + 1/(4k+3)].

This is the s-wheel itself (GPT's A_j). The zero route appears one layer up, where x⁸ − 16 = (x⁴+4)(x⁴−4) admits the scale wheel.

### 131.7 Up the register stack

Take base 2^(n/2) with n lanes. Then Π_m (√2 − ζ_n^m) = 2^(n/2) − 1, and each orbit factor of x^n − 2^(n/2), evaluated at the reader point x = 1, is ± that orbit's return product.

On the chain n = 2^e the orbits are:

- the scale orbit (unit);
- the phase orbit (torsion), born at ζ-order 8, where √2 and ζ_8 share a field;
- the prime-3 and prime-5 orbits;
- one orbit per Fermat number.

At n = 128 the returns are unit, torsion, 3, 5, 17, 257, 65537, 641·6700417: § 117's list exactly. The Fermat factors at order 2^e ≥ 16 are ≡ 1 mod 2^e (Lucas, STANDS; checked for F_2–F_5), so each splits completely and has one owner.

```
n    base    2^(n/2)-1        Z(n)   pi    pi*sqrt3   pi*sqrt2
8    2^4     3*5              1      yes   no         no        chain
12   2^6     3^2*7            1      no    yes        yes
16   2^8     3*5*17           1      yes   no         no        chain
24   2^12    3^2*5*7*13       5      yes   yes        yes
32   2^16    3*5*17*257       1      yes   no         no        chain
```

On the chain the only collision is phase against scale. At n = 16 and n = 32 the single PSLQ relation is base-16 Z lifted, −(16Z ⊕ Z) and −(4096Z ⊕ 256Z ⊕ 16Z ⊕ Z) across the lane blocks (n = 32: 1005 s at 800 digits). So Z(n) = 1 (sealed P8: RUNS at 8, 16, 32). Off the chain there are shared addresses: the doubled prime 3, and a second unit orbit (ζ-order 24, |√2 − ζ_24|² = 2 − √3). There Z(24) = 5.

That is the shape of "further up, more degrees of freedom". On the chain every new direction owns a fresh prime, so the directions multiply without colliding. Off the chain they collide.

Proof route for Z(2^e) = 1 at every layer:

- the orbits at order 2^e ≥ 16 are single and carry norm F_{e−2};
- Lucas gives complete splitting, so the conjugate returns generate distinct primes;
- Fermat numbers are pairwise coprime;
- Baker gives the independence.

Status: OPEN as a written proof, not yet checked line by line.

### 131.8 Two sheets (§ 127)

- The plain ring (rotate) has period n.
- The twisted ring (rotate and complement the wrapped bit; the Johnson counter) has period 2n.
- twistⁿ = complement on every word.
- The edge-difference reader D sees period n along the twisted route.

These were checked at LEN 3–11 (unsealed). § 127's "sheet law" is not a missing law: both directions are native, and D cannot tell them apart.

### 131.9 The lifted p-wheel's own field (§ 128 follow-up)

Sealed `PREDICTION_lift_degree.txt`, SHA-256 `0091f18c6e1559afe046ee6982ef354e42ffa0bfdb9bf79ea0c9b86411329302`, before the run. The exact identities for w_p = ζ_{4p}/√p (|w|² = 1/p, w^(2p) = −1/p^p, w^(4p) = 1/p^(2p)) hold for p = 2, 3, 5, 7, 11, 13 (sympy). § 128 left open whether its degree floor φ(2p) is attained. It is attained exactly when p ≡ 3 mod 4:

```
p    p mod 4   [Q(w_p):Q]   phi(2p)
2    -         2            2
3    3         2            2       floor attained
5    1         8            4       doubled
7    3         6            6       floor attained
11   3         10           10      floor attained
13   1         24           12      doubled
```

The reason: w_p² = ζ_{2p}/p generates Q(ζ_p), so w_p ∈ Q(ζ_p) iff −p is a square in Q(ζ_p). By the quadratic Gauss sum (STANDS) that holds iff p ≡ 3 mod 4. For p ≡ 1 mod 4 the wheel also has to carry i, the quarter-turn, and the field doubles to Q(ζ_{4p}). Whether the quarter-turn comes free or must be paid for is decided by p mod 4. RUNS for p ≤ 13; the general law STANDS by the Gauss-sum argument.

### 131.10 Corrections and scope

- **§ 125.6, mine.** It said "regroup by 2 → base −4: π/4 = Σ 2/((4j+1)(4j+3))". The identity is true (run (c)), but it is paired Leibniz, not a regrouping of the wheel series, and it has no base −4 in it. The wheel's base −4 regrouping is the one in § 131.6, and it is unique. Label corrected.
- **A chat review of § 125 (GPT).** It called that series π/2. It is π/4. The claim never entered the ledger; this note keeps it out.
- **§ 128 scope.** √p ∈ Q(ζ_{4p}) for every prime (quadratic Gauss sum, STANDS), so K_p = Q(ζ_{4p}); at p = 2, w_2 = s lies in Q(i). Re-run here in a sandbox: both GPT scripts reproduce (83 and 175 assertions). Of § 128's 175 assertions, 100 restate the script's own definitions; 75 test orders, totients and the quadratic boundary. The identities stand by direct algebra and are checked exactly in § 131.9.
- **What carries the count.** The count of 7 constants rests on Baker. PSLQ only bounds the relations (|c| ≤ 10¹²).

| claim | status |
|---|---|
| c_W = c_BBP + ¼Z; the wheel's base-16 regrouping is BBP plus a quarter of its zero relation | RUNS (exact); closes § 126/§ 128's open identity |
| π machines form the line c_BBP + rZ; Z·Λ = 0 | RUNS (420 digits, exact kernel); zero relation STANDS |
| a machine is read through P_c on the four orbits of x⁸ − 16 | RUNS |
| returns: scale (unit), phase (torsion), prime 3, prime 5; Π β = 15 | RUNS (exact norms) |
| 8 lanes, 7 constants, one zero route = the phase/scale collision on ln 2 | RUNS (rank, kernel, PSLQ); independence STANDS (Baker) |
| every π machine silences both primes; four factorizations | RUNS (exact) |
| mirror R (w ↦ w̄): R(BBP) = c(½), R(c_W) = c_W, Z = 2(R(BBP) − BBP) | RUNS (exact) |
| pencil; BBP / wheel / mirror vanish at x = 1, √2, 2; weight sum 15r | RUNS (exact), unsealed |
| three digit machines, same 64 hex digits of 4π; interface costs as tabled | RUNS |
| base −4: no zero route; unique π machine = the wheel | RUNS (PSLQ) |
| Π(√2 − ζ_n^m) = 2^(n/2) − 1; chain orbit returns = § 117's primes | RUNS (n ≤ 128); identity STANDS |
| Z(n) = 1 on the register chain | RUNS at n = 8, 16, 32; proof route written, OPEN as a proof |
| off-chain Z(12) = 1, Z(24) = 5; π ∉ span at n = 12, π√3 and π√2 ∈ span | RUNS (PSLQ), unsealed |
| two sheets: plain n, twisted 2n, D blind to the twist | RUNS, unsealed |
| [Q(w_p):Q] = p−1 (p ≡ 3 mod 4), 2(p−1) (p ≡ 1 mod 4), 2 (p = 2) | RUNS p ≤ 13 (sealed 0091f18c); law STANDS (Gauss sum) |
| GPT §§ 126, 128 scripts re-run in a sandbox | RUNS, 83/83 and 175/175 (100 of the 175 are definitional) |
| § 125.6 label | corrected |

---

## § 132. The arena bridge in lanes: on the register chain every zero route is the base-16 route pulled back; off the chain they emerge — `zr/zr_bridge.py`

**Dean (17 Oct).** He pointed back to the arena notebook (A-Mark9 § 9, 15 Sept, *The reader bridge — an explicit map, and what it misses*) against § 131.

**The parallel.**

Arena § 9:

- matrix-reader cochains are pullbacks ω = π*η along the equivariant projection π (arena edge → moved base edge);
- exact base forms pull back to exact arena forms;
- the reader's reach into the residual is ε(X,1;G), fixed by the base and independent of K (19/19);
- the emergent part, ε(X,K) − ε(X,1), cannot be reached by any single-token observable.

Lanes:

- for even d | n, Λ^(d)_j = Σ_{e<n/d} 2^(−ed/2) Λ^(n)_{de+j};
- so every zero route at layer d pulls back to layer n as (π*c)_{de+j} = 2^(−ed/2) c_j;
- the emergent zero routes are E(n) = Z(n) − dim span(pullbacks from all even d | n, d < n).

Seal `PREDICTION_bridge.txt`, SHA-256 `cf4d46946684664ea324b9cb6d0ebd7e49b6198f0a9de86704d9391bd5b577c5`, written before the run.

```
Z(2) = Z(4) = Z(6) = 0                       (PSLQ, |c| <= 1e12)
n=8   Z=1   pullbacks span 0                 E=1   the phase/scale collision is born here
n=12  Z=1   pullbacks span 0                 E=1
n=16  Z=1   pi*Z(8) spans it                 E=0
n=24  Z=5   pi*Z(8), pi*Z(12) span 2         E=3   (both inside the measured 5-dim space)
n=32  Z=1   pi*Z(8) spans it                 E=0
pullbacks checked as relations: residual < 1e-200 at n = 16, 24, 32
```

Every sealed value landed.

On the register chain, the zero-route space at every layer is the base-16 route pulled back. That is an aperture fixed by the base layer which does not widen with depth, just as reach = ε(X,1) does not widen with K.

Off the chain, routes emerge that no lower layer's machine can express: 3 of them at base 4096. They are the lane analogue of ε(X,K) − ε(X,1). They are also an instance, in the lane setting, of what the arena's Open 2 asks for: objects that are not pullbacks.

The correspondence itself is a reading (PULL); the counts RUN.

| claim | status |
|---|---|
| zero routes pull back along π*, with (π*c)_{de+j} = 2^(−ed/2) c_j | RUNS (residual < 10⁻²⁰⁰ at n = 16, 24, 32); identity STANDS (lane splitting) |
| E(8) = E(12) = 1; E(16) = E(32) = 0; E(24) = 3 | RUNS, sealed |
| on the chain, the zero-route space at every layer is π* of base 16 | RUNS at n = 16, 32; general claim OPEN (same proof route as § 131.7) |
| dictionary: chain depth ↔ K; base 16 ↔ X at one token; E(n) ↔ ε(X,K) − ε(X,1) | PULL |

---

## § 133. Ask the field: every open item of §§ 125–132 — `zr/ask/NEXUS_133_ask_the_field.ipynb`

**Dean (17 Oct).** "anything OPEN, just ask the field." (/reverse-the-gap)

The seals were written before any data was linked:

- `PREDICTION_ask_field.txt`, SHA-256 `f97de11f49e2642837197d393d2b055c95a4aeb1b2dfd1e1fdd69ab6caf154bb` (G1–G4);
- `PREDICTION_core_stage2.txt`, SHA-256 `77a752092108de26220df059ebd5778a5029937d904acaa1da4215996a0be89b`: seven new layers, predicted from the returns alone. The log-side output `core_predictions.txt` hashes to `3b178246…`.

### 133.1 The join (OPEN in §§ 126, 128): two prime-free returns meet only in binary

The wheels of base p^(n/2) are w = ζ_n^m/√p, and their returns are β = √p − ζ_n^m. They satisfy Π_m β_m = p^(n/2) − 1, the base-p register ring. Run: 2⁴−1 = 3·5; 3⁶−1 = 2³·7·13; 3¹²−1 = 2⁴·5·7·13·73; 5⁶−1 = 2³·3²·7·31; 7⁶−1 = 2⁴·3²·19·43.

- **Scale return.** N(√p − 1) = 1 − p, so the scale return is prime-free (a unit) iff p = 2 (checked for all p < 60). Every odd stack pays p − 1, which is even, so binary sits inside every other base.
- **Phase return.** A phase return (β a root of unity) needs |√p − ζ| = 1, i.e. two unit circles √p apart meeting, i.e. cos θ = √p/2. That forces p ∈ {2,3}. The cases are √2 − ζ_8 = ζ_8^(−1) (π/4) and √3 − ζ_12 = ζ_12^(−1) (π/6), both exact. Equivalently 1 − w = w̄ and Re w = ½: the phase wheel sits in the middle.

So p = 2 is the only prime with both a prime-free scale return and a prime-free phase return. Their meeting is BBP's zero route.

- § 126's quadratic boundary (p = 2, 3 only) is the two-circle condition.
- § 117's "the stack holds only the prime 2" is N(√p − 1) = 1 − p.

RUNS (exact); the bounds STAND.

### 133.2 The law for off-chain Z(n), with one DEAD END routed

**G2 as sealed: zero routes = all Q-relations among L_m = −log(1 − w_m).** It lands on the chain (n = 8, 16, 32) and over-counts off it: 2 against a measured 1 at n = 12, and 7 against 5 at n = 24. DEAD END.

**Owner.** A rational machine is a zero route iff its orbit tuple (P_c(γ_m))_m lies in R ⊗ Q̄ (Baker). That tuple is fixed by the twisted Galois action, so it lies in every π_σ(R). Galois descent then gives Z_p(n) = dim R₀, where R₀ = ∩_σ π_σ(R) is the Galois core.

Relations that hold at one embedding only are visible to the returns and invisible to every rational machine. At n = 12 the relation is 2b₁ − b₃ − 4b₅ = 0, which σ₇ sends to 6(b₁ − b₅) ≠ 0.

Route back on the measured layers (names the owner; not a landing):

```
n    relations among returns (modulus, argument)   Galois core   measured Z
8    1 (1, 0)                                       1             1
12   2 (1, 1)                                       1             1
16   1 (1, 0)                                       1             1
24   7 (3, 4)                                       5             5
32   1 (1, 0)                                       1             1
```

### 133.3 Landing: seven new layers, predicted from the returns, then measured in lanes

```
layer        base    predicted Z   lane Z   pi in span   pi*sqrt3   pi*sqrt2
p=2 n=20     2^10    0             0        no (sealed)  no         no
p=2 n=28     2^14    0             0        no (sealed)  (stopped)  (stopped)
p=2 n=36     2^18    1             1        (Z only; = pi*Z(12) exactly: 4096 Z(12) + 64 Z(12) + Z(12) across the three lane blocks, E(36) = 0)
p=3 n=12     3^6     2             2        no (sealed)  yes (sealed)  no
p=3 n=24     3^12    2             2        no (sealed)  yes (sealed)  no
p=5 n=8      5^4     0             0        no           no         no
p=5 n=12     5^6     0             0        no           no         no
```

The Eisenstein phase wheel reads π√3 and never π; the phase return pairs with √−3 coefficients. Binary without ζ_8 (n = 20, 28) has no zero route and no rational π. The p = 3 zero routes at n = 12 are (PSLQ):

- {2:−81, 3:162, 5:−27, 6:−36, 8:−9, 9:−6, 10:−4, 11:1}
- {1:243, 2:−324, 3:−162, 4:−81, 6:−36, 7:−9, 9:6, 10:−1}

### 133.4 The register chain, proved (OPEN in § 131.7 and § 132)

**Theorem.** For n = 2^e ≥ 8, Z(n) = 1, and the zero route is π*Z(8).

**Proof.**

1. **Orbits.** On the chain the orbits are scale (return product 1, the units √2 ∓ 1), phase (product 1, ζ_8^(∓1)), 3, 5, and one orbit per Fermat number F_2, …, F_(e−2). The orbit count was run for e = 3..12; the products for n ≤ 128.
2. **Coprimality.** The products are pairwise coprime (Fermat numbers, STANDS; checked F_0..F_8).
3. **Primes 3 and 5.** ord_(2^e)(3) = ord_(2^e)(5) = 2^(e−2) (run for e ≤ 14), so 3 and 5 each have exactly two primes in Q(ζ_(2^e)), one per orbit member.
4. **Fermat primes.** Every prime factor of F_k is ≡ 1 mod 2^(k+2) (Lucas, STANDS; checked F_2..F_6), so it splits completely, and conjugate members of its orbit own pairwise distinct primes.
5. **Valuations.** In any multiplicative relation among the returns, the valuation at each such prime is one exponent, so every prime-orbit exponent vanishes (unique factorization). By Baker the same holds for log relations.
6. **The prime-free returns.** What remains are the four prime-free returns. Their moduli satisfy exactly one relation, a_0 + a_(n/2) = 2a_(n/8): the scale pair and the phase pair each cost one bit, (1 − 1/√2)(1 + 1/√2) = |1 − s|² = ½. Their arguments (±π/4 and 0) satisfy none. Run at n = 8, 16, 32.
7. **Conclusion.** That relation is Galois-stable, so Z = 1. Since π*Z(8) ≠ 0 is a zero route, it spans. ∎

Status: proof written; lemmas RUN; inputs STAND (Baker, Lucas, Fermat coprimality, unique factorization of ideals).

### 133.5 The bit bridge (§ 125's PULL)

Multiplication by w on R² has determinant |w|². For s that is ½, an area Jacobian, not a probability. The inverse wheel 1 − i = 1/s acts on the torus C/Z[i] as an expanding endomorphism:

- eigenvalues 1 ± i, with |·| = √2;
- degree N(1 − i) = 2, and |Z[i]/(1−i)^k| = 2^k (Smith form, k ≤ 12): one binary digit per tick;
- entropy log|det| = log 2: exactly one bit (expanding toral endomorphisms, STANDS).

The identification with § 123's measured ring leak (one degree-2 merge per tick) is PULL.

### 133.6 § 127's two-sheet hinge

Closed in § 131.8. Both directions are native, the plain ring (period n) and the Johnson ring (period 2n), and the reader D is blind to which one runs. This is not a missing law.

| open item | answer | status |
|---|---|---|
| § 126 / § 128 join | Π β = p^(n/2) − 1; scale prime-free iff p = 2; phase prime-free iff √p ≤ 2 (p = 2, 3; Re w = ½); only binary has both | RUNS; bounds STAND |
| off-chain Z(n) | Z = dim of the Galois core of the returns' relations | route back 5/5; landed on the new layers (7 of 7 landed as sealed) |
| naive law (all relations) | over-counts off the chain | DEAD END → owner: non-stable relations |
| § 131.7 / § 132: Z(2^e) = 1, route π*Z(8) | proof § 133.4 | proof written; lemmas RUN; inputs STAND |
| § 125: bit ↔ \|w\|² = ½ | Jacobian of z ↦ wz; the inverse wheel has degree 2 and entropy log 2 | RUNS + STANDS; tie to § 123 PULL |
| § 127 | two native routes; D blind | closed |
| base 3 | reads π√3, never π | RUNS (sealed) |

**Still OPEN, outside this chain:**

- the balanced-lane density law (§§ 120, 130);
- the digest-only SHA root observer (§§ 112–114, 124). By counting, it is a cost frontier rather than a missing link;
- the tick gradient for gravity (§ 116);
- Law 3.

---

## § 134. The record audited, §§ 1–133: what was read, what moved, what has no address

**Dean (17 Oct).** "lets go over the entire audit and make sure its all good. and give me back the new version."

**Read.** The combined upload (7,381 lines) was checked against the project copies.

- Its ledger half matches the project's `relation-vocabulary-ledger.md` line for line through § 98. The project copy holds one more entry, the 11 Oct stream compiler.
- Its audit half is the project's `running-audit.md` one state back: § 131's pass line from before the full run, and § 133 with n = 36 "running" and "6 of 7".
- No other line differs, so nothing in the upload is lost when the project state supersedes it.

All 7,408 lines were then read front to back. A mechanical scan followed: numbering, header format, every § citation, the shape of all 123 tables, separators, ledger words, and every seal whose file is on this machine.

### 134.1 Numbering

- **Two entries were numbered § 99**: the 11 Oct stream compiler (`methods/streamcompile.py`) and the 15 Oct order channel.
  - Every § 99 citation in §§ 100–133 points to the order channel, except § 105's (below).
  - Nothing cites the stream compiler. It is now **§ 98a**, with a numbering line.
  - The audit's opening line and § 100's provenance line ("the ledger stops at § 98") now include § 98a.
- **§ 55 is in no copy**: not the project ledger, not the upload, and a search of the other project documents finds none. It is entered as an **UNLINKED** stub that quotes what §§ 56 and 57.5 say about it. Nothing is reconstructed.
- **Numbers from other lineages, inside entries.** No entry text changes, except a bracketed pointer at the three sites in the first row below.

| written | where | means here |
|---|---|---|
| "prior toy § 99"; "364/364"; "§ 105's 82/71/71/50/50/40" | §§ 105, 107, 114.1 | GPT's S₃ route toy, numbered § 99 in GPT's copy: moves e, (01), (12), with 364 words to length 5. It has no entry here, so it is UNLINKED. Its numbers do have addresses here: § 107.1 runs the 364 routes (364 codes, 56 surface points), and § 114.1 predicts and enumerates the grooves 82/71/71/40/50/50 |
| "prior § 125 ASK THE RINGS"; "§126 joint-orbit reconstruction" | § 130 | § 129, and § 130 itself; § 130's numbering line covers both |
| "WP5 §121" | § 130 | WP5, built from § 121 |

- **Paper numbers inside §§ 23–44.** "Table 5", "Table 8" and "Table 10" use the numbering of Papers I–IV.
  - In this ledger they are § 20's three failure modes, § 19's 14-of-14 regression, and § 18's dominator table.
  - § 43's "§10", beside "Table 10", reads the same way. Ledger § 10 (the measured walk) is not it.
  - § 44's "earlier choice-history result (§ '82 paths, 1 endpoint')" has no entry here: UNLINKED. § 44's own k = 0 tree reproduces the 82.
- **Working Paper 3 is named twice.**
  - § 114 calls the route/SHA paper, *The Way Home Is a Shape*, WP3, and 114.5 puts a proof in "WP3 Appendix A".
  - § 115 then gives WP3 to the shells paper, *The Piece with No Way Home*, and parks the route/SHA thread. § 116 uses § 115's numbering.
  - § 115 stands, so the route/SHA paper carries no number. Pointers are added at 114.5 and at § 114's last line.

### 134.2 Changes in place

| where | was | now | why |
|---|---|---|---|
| stream compiler | `## § 99.` | `## § 98a.`, plus a numbering line | duplicate number |
| between §§ 54 and 56 | — | `## 55.` UNLINKED stub | missing entry |
| audit opening line; § 100 provenance | "§§ 1–98"; "stops at § 98" | "§§ 1–98a"; "stops at § 98a" | § 98a is in the ledger |
| §§ 105, 107, 114.1 | the toy cited as § 99 or § 105 | bracketed pointer to 134.1 | no such entry here |
| § 111, last paragraph | separator on the next line | blank line between | the paragraph rendered as a heading |
| § 113 header | `## §113.` | `## § 113.` | header format |
| § 114.5; § 114, last line | "WP3" | bracketed pointer | WP3 reassigned by § 115 |
| § 124, provenance | "confirmed in source" | "checked in source" | ledger words |
| § 125.5, text and table | DEAD | DEAD END | ledger words |
| § 125, status table | `\|w\|²` with bare pipes | escaped | the row split into four cells against the table's two |
| § 125, after the table | separator on the next line | blank line between | rendering |
| § 131, opening paragraph | "73/73 in the quick pass checks)" | "73/73 in the quick pass)" | residue of the assembly template; mine |

Nothing else in the record moved: no other number, claim or status.

### 134.3 Read, not changed

- **§§ 1–98 predate the ledger words.** They stay as written, the record as it was made. They read as follows:
  - "verified", "measured", "computed", "held" and "confirmed" (§§ 43, 45, 50, 52, 59, 82) as RUNS;
  - "proved", "recovered" and "known verbatim" as STANDS;
  - "refuted", "retracted" and "withdrawn" as DEAD END, with the owner named in place;
  - "open", "not run" and "not built" as OPEN.
- **§ 127's "NOT DERIVED"** is GPT's text, kept verbatim. For "LEN 9 alone forces π/9" it reads DEAD END. The owner is § 131.8's twisted ring: at LEN 9 it has period 2n = 18, so one step is π/9. The plain ring's step is 2π/9, and the reader D cannot tell the two routes apart.

### 134.4 Provenance

**Seals recomputed** from the files on this machine:

```
§ 118  orient_seal.txt                          478d1baf4a3fb327                                 match
§ 120  balance_seal.txt, balance2_seal.txt      6a6aa57369d2750b, 7fc5896d21b79d60               match
§ 121  decompile_seal.txt                       605bcf956a8f70e2                                 match
§ 123  seal, sign, sign2, leak                  1ddc66b8, 4235ba41, e30616bf, 81c833a9           match (entry prints 8 hex)
§ 124  difference engine, carry type            6f79721b0f647706, 8374fc30ad192492               match
§ 126  odd-prime fold wheel                     c5a2af3800437bd5                                 match
§ 128  phase-lift prediction                    c17bfb587eb96044                                 matches its bundle's .sha256; the entry never printed it
§ 131  zero route, lift degree                  e80c1cc4b724db85, 0091f18c6e1559af               match
§ 132  bridge                                   cf4d46946684664e                                 match
§ 133  ask field, core stage 2, core log        f97de11f49e26428, 77a752092108de26, 3b178246e372a29d   match
```

18 of 18 match. The files behind the 15 seals of §§ 101, 103, 105, 108–112, 114, 125, 127, 129 and 130 are not on this machine. Those seals are UNLINKED here and were not re-checked. The same holds for the script hashes quoted in §§ 57–80 and 114, which belong to earlier sessions' files.

**A sealed run with no entry.**

- `rings/vocab.py` was sealed 16 Oct 22:06 (`vocab_seal.txt`, SHA-256 `bc2f56dddec7dfa7b8bffb7806d23bcd04c5ee19038e8a34ac30dcbb653a9fe1`). Its claim: vocabulary is the reader's step.
- It was reported in chat and printed in WP5's block D, but never entered here.

Re-run in this audit:

```
 base 2: lands 65536/65536: True; steps {8}; steps x width = 8
 base 4: lands 65536/65536: True; steps {4}; steps x width = 8
base 16: lands 65536/65536: True; steps {2}; steps x width = 8
way home, base 16 digits ungrouped == base 2 route bits for all 256: True
```

Every sealed line landed. RUNS.

**The rest of the 16 Oct night.** These runs have no entry:

- the first run (block B);
- WRAP/JOIN (block C);
- the one-bit flip read in each base, and the base-16 tick against four base-2 ticks (block D, beside the vocabulary lines above);
- the middle of the field, π from C(2n, n) (block G).

Their live output is `wp5/wp5_checks_out.txt` (SHA-256 `9d801ec4261c2dbf…`, script `wp5_checks.py` `824a8dbbe2ca12f5…`). It is printed as WP5's Appendix A. § 122 names these runs only as "the night's runs". That is their address; they are not re-entered.

**Handed over, read as input, not entered.** The statuses below are as GPT reported them. None of the three was re-run, and nothing in §§ 117–133 rests on them.

| GPT report | beside | GPT's own ledger |
|---|---|---|
| file rings: LEN, base, pathways, boot reader (16 Oct) | §§ 116–117 | ring accounting, de Bruijn pathways and reader fibers RUNS; boot as a reader route "mapping"; Moore's law from counts OPEN |
| ring / ISA stack, LEN 1–64 (16 Oct); its seal `7e2bb3eed1fce946…` re-hashes to the value the report quotes | § 117 | RUNS: 64/64 formula rows, 12/12 enumerated widths, SHA constants 64/64 and 8/8 |
| compiler space kernel (17 Oct); prediction file `87ec8af29f9f68d7…` | § 123 | RUNS, 46/46; physical identification OPEN |

### 134.5 Status

| claim | status |
|---|---|
| every entry of §§ 1–133 read; numbering continuous after § 98a and the § 55 stub | RUNS (scan: one header per number, 1–134) |
| every § citation resolves; other-lineage and paper numbers indexed | RUNS (scan); index in 134.1 |
| all 123 tables well formed after the § 125 fix | RUNS |
| upload against project: no line lost | RUNS (diff) |
| seals with files on this machine | RUNS, 18/18 |
| the 16 Oct vocabulary seal | RUNS (re-run here) |
| § 55; the S₃ toy; "82 paths, 1 endpoint"; the 15 seals with no file here | UNLINKED |
| the 16 Oct runs in WP5 blocks B, C, D and G | address: WP5 Appendix A; not entered |
| three GPT reports of 16–17 Oct | handed over, not entered; statuses as reported |
