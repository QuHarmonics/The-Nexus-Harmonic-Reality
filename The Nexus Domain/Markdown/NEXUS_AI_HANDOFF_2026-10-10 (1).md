# NEXUS — AI-to-AI Research Handoff

**Snapshot:** 10 October 2026  
**Purpose:** preserve the actual state of the NEXUS work across AI sessions; identify candidate contributions without inflating novelty; specify how to continue calculations in the order that preserves their logic.  
**Primary sources:** `relation-vocabulary-ledger (31).md` (especially §§73–83); `NEXUS_family_realizability_and_exchange.xlsx`; `Review-This-Analysis_2026_10_10__0612.md`; `Getting-organized_2026_10_10__0626.md`; `Normalized-transfer-spectrum-and-substrate-independent-geometry_2026_09_16__0554.md_2026_10_10__0611.md`; `Distinction_That_Must_Continue.docx`; the character-lab HTML and exact-certificate ZIP.

> **Handoff rule:** do not restart the project, choose a new target, or turn the present result into a larger theory without a specific request. Read this handoff, then the cited current source section, before acting. Reproduce before interpreting. Preserve corrections and negative results. Do not call something novel merely because it was rediscovered here.

---

## 0. Governing correction: think like a coder; follow the flow before naming anything

This section governs how every other section is read. The recurring failure in prior sessions was to see a result, give it a noun, then reason from the noun as though it explained the result. Reverse that order. Track what runs, what changes, what is carried forward, what is preserved under translation, and what the next step can distinguish. Name a recurring operation only after its behaviour has been established.

### The baseball test: preserve the rules while changing the implementation

Physical baseball runs through bodies, a ball, a field, and motion. Atari baseball runs through bits, registers, and screen updates. The two implementations do not share matter or detailed motion. They remain versions of the same game to the extent that the rule-governed transitions correspond: an action changes a game situation in a way the rules allow, and the resulting situation constrains the next action.

The timing matters. The game logic constrains what counts as a valid baseball implementation before a particular electronic implementation is built. Building the Atari version makes one realization executable; it does not invent the governing rules from its pixels. But the rules do not uniquely specify every electronic detail either. The implementation must preserve the distinctions relevant to the game, not every physical fact about the field.

This is a preservation test, not a claim that all of reality has already been proved to be a binary program. “Binary version” means an encoding that allows selected transitions and dependencies to be executed in another substrate. The research task is to determine which relations must survive that encoding, and test whether they do.

### The coder's flow

```text
source encounter / source state
        │ apply a permitted action
        ▼
source transition:       x --a--> x'
        │ encode the current distinctions
        ▼
encoded state:           E(x) --encoded action--> E(x')
        │ execute the encoded rule and compare
        ▼
preservation check:      E(T_a(x))  ?=  T̂_a(E(x))
        │
        ├─ equal over the stated scope: the encoding preserves this transition
        └─ unequal: a distinction, dependency, or action rule was lost or changed
```

For a deterministic exact encoding, the target equality is

\[
\boxed{E(T_a(x))=\widehat T_a(E(x)).}
\]

It must hold for each action and state in the declared scope, then for compositions of actions. For probabilistic systems, compare the induced transition distributions instead of requiring a single next state. A visual resemblance, matching output sample, or matching total dimension is not sufficient: the transition must commute with the encoding.

If two source situations encode to the same target state but take different lawful continuations, the target cannot continue correctly from its current encoding. Add the smallest retained distinction that separates those futures. Then rerun the same commuting check. That is where the continuation ledger enters: it records exactly what must be carried into the next operation to prevent the encoding from collapsing futures that later diverge.

### Why AI tokens are a useful coder's example

At inference time, a typical autoregressive model repeatedly runs a flow like this:

```text
current token context
    → compute contextual activations and next-token scores
    → choose/sample one next token
    → append it to the context
    → recompute the next-token scores from the changed context
    → continue
```

The emitted token is a step in the trajectory, not an explanation of the rule that produced it. The same visible token can do different work in different contexts; a token's contribution depends on what preceded it and how the model processes the whole available context. During ordinary inference the weights are generally fixed, while the context and activations change at each step. Training is a different process that can change the weights themselves. Keep those two update loops separate.

The analogy is therefore operational: infer the procedure that maps context to allowed or likely continuations; do not mistake the observed token sequence for the whole procedure. Then test that inferred procedure on prefixes and continuations that were not used to build it. For the hexadecimal work, the “method” is likewise not a table of outputs: it is the dependency and carry/borrow flow that determines which output digits become fixed as input digits are exposed. For SHA-256, the target is not to rename digest patterns; it is to recover method-relevant structure and test it against the round transitions, while keeping local reverse execution distinct from digest preimage inversion.

### What “shape” means in this mode

A shape is the reusable path of constraints and transitions: which move may follow which, how operations compose, where a path returns, which distinctions survive a change of representation, and what dependencies must be retained. A drawing, a final value, a list of cells, or a named object may represent that path, but none is the explanation by itself.

Ask in this order:

1. What actually runs from the current state?
2. What does that operation read and change?
3. What does it carry into the next step?
4. Which compositions, returns, or invariants survive?
5. What is the smallest encoding that preserves those future continuations?
6. What unseen case could falsify the proposed method?
7. Only then: what short name helps us refer to the repeated behaviour?

Do not ban technical nouns; ban noun-first reasoning. Use nouns as type names and variable names for operations already grounded in a trace.

---

## 1. The stable research spine

The user’s durable four-part direction is:

1. **Hexadecimal transformation space:** study the transformation as a process, not merely its input/output values.
2. **Shapes as methods:** understand a shape as the organization of admissible moves, compositions, returns, and dependencies that implements a transformation.
3. **Read a missing method without brute-force search:** infer what an incomplete reader or vocabulary cannot distinguish, and specify the exact conditions under which that inference works.
4. **Use SHA-256 as a real target:** test the method against a hard, defined transformation whose internal procedure and outputs have sharply different information properties.

The recent graph/token/representation work is a substantive mathematical line and currently has a strong exact record. It is **not permission to silently replace the four-part research spine with a new destination**. Keep it as a concrete testbed for methods, symmetry channels, closure, and recoverable residuals. The user decides when priority changes.

### The common operational question

Given a lawful transition system, a coarse reader, and a declared family of relations, determine what differences the reader merges, which distinctions affect future continuation, which relation directions the declared family reaches, and what remains outside it. The missing part must be represented in a way that can be tested, not described only by metaphor.

A compact finite-state formulation is:

\[
R(x_1)=R(x_2)\quad\text{but}\quad R(T_a x_1)\ne R(T_a x_2)
\]

for some admissible continuation \(a\). Then the current readout has merged states whose future behaviours differ. Add the smallest retained distinction needed to make the future response well-defined. The finite continuation-ledger implementation uses standard partition-refinement/Moore/Myhill–Nerode machinery; the value of the project is in the specific operational framing, tests, and applications, not a claim to have invented those classical algorithms.

---

## 1A. Project base and anti-drift rules

The project-entry record frames its base as the single statement **“Nothing can change / everything must change.”** Do not casually split that into two independently usable axioms or insert an external vantage point. In the project’s intended reading, “whole” and “reader/part” are two readings of one substrate: the whole is not assigned an external observer, while every practical reading is partial and its address depends on what it can distinguish. This is a guiding framework statement, not a theorem proved by the finite graph calculations or a settled physical claim.

The user’s working rules are operational:

1. **Say it, then reverse it.** Test what survives both directions; preserve counterexamples.
2. **Execute before stating.** Treat unrun claims as conjectures or instructions, not results.
3. **Do not step a stepless thing.** An output sequence is the investigator’s traversal; do not assume it is the object’s own structure.
4. **Hold more than one reading.** Trust an identification only after checking what remains invariant across readers/frames.
5. **Walk up from behind.** Derive the admissible structure from constraints rather than starting with a named object and fitting it.
6. **Treat null results as navigation.** A failed mechanism deletes a route or points to a missing condition; it is not permission to fabricate a replacement explanation.

Signs that a session is drifting: nouns replace motion and composition; a chain of speculative implications is reported as proof; a finite example is generalized without a theorem; “recovered” becomes “derived”; an unrun interpretation becomes the next project; or the global priority is replaced without user direction. Correct drift by returning to the last exact object, the last failed/passed test, and the stated research spine.

---

## 2. How to arrange the flows

Use the following causal/work flow; do not jump straight from an output pattern to an ontology.

```text
CONSTRAINTS / ADMISSIBILITY
          ↓
allowed states and legal transition rules
          ↓
COMPOSITION / TRAJECTORY
          ↓
paths, returns, cycles, and what a move carries into the next move
          ↓
READER / ADDRESS
          ↓
which histories or states remain distinguishable under the selected tests
          ↓
RETAINED STATE / CONTINUATION LEDGER
          ↓
minimum added distinction needed to determine future behaviour
          ↓
RELATION VOCABULARY (cell families / method shapes)
          ↓
BOUNDARY MAP
          ↓
available relation directions A, generated directions im(∂₂), dependencies ker(∂₂)
          ↓
RESIDUAL / DEFICIENCY / REDUNDANCY
          ↓
SYMMETRY ACTION + CHARACTERS
          ↓
fixed-point traces, projectors, isotypic channels
          ↓
MISSING-METHOD SHORTLIST
          ↓
faithful-reader span certificate / exact algebraic check
          ↓
update the ledger, test a held-out case, then document
```

The boxes have distinct types; do not collapse them into one word such as “information.” In particular:

- **Admissibility** says what is allowed to happen.
- **Transition/composition** says how a state changes and what is fed into the next operation.
- **Reader** says which differences are visible under a specified observation rule.
- **Retained state** is memory needed to preserve distinctions relevant to future continuation; it is not necessarily minimal memory until minimization is proved.
- **Relation cells/methods** are declared closed histories, not simply output values.
- **Boundary image** is what the declared vocabulary actually generates.
- **Deficiency** is what the vocabulary does not reach.
- **Redundancy** is dependence among declared cells.
- **Character channels** resolve where those two quantities sit under symmetry.
- **Certification** is separate from multiplicity bookkeeping: having enough copies of an irreducible is necessary but not by itself sufficient to prove two actual submodules span complementary copies.

### Three specific flow patterns now in the corpus

**A. State / process flow:** constraints → legal transitions → composition and return → reader equivalence → minimal continuation ledger. This is the right flow for hexadecimal transformation analysis and the SHA target.

**B. Relation / chain flow:** arena graph → closed walks/cells → boundary map → cycle space \(A\) → generated relation space → quotient deficiency \(D\) and kernel redundancy \(H_2\) → symmetry decomposition. The same chain complex is viewed through different readers; the reader changes the visible fixed-vector dimensions, not the underlying multiplicity module.

**C. Constraint-closure flow:** two constraints or residuals act on the same candidate space; their intersection or cancellation selects a result. Keep the two mechanisms separate:

\[
\mathcal C_{\cap}=\{x:C_0(x)=0,\ C_1(x)=0\},\qquad r_0(x)+r_1(x)=0.
\]

An intersection of solution sets is not automatically the same operation as cancellation of residuals. The BBP and “Objects as Closures” examples instantiate variants of this idea, but a universal closure theorem still needs typed hypotheses and a proof that maps each example to the same formal mechanism.

---

## 3. Novelty discipline and labels

Use these status labels every time a result is discussed:

- **PROVED (model-scoped):** follows from stated definitions/hypotheses by an argument.
- **EXACT-COMPUTED:** finite exact arithmetic/matrix identity, with input and field specified.
- **FAMILY THEOREM:** all sizes follow from a proof or cited theorem whose hypotheses have been checked.
- **RECOVERED / KNOWN:** a standard result or earlier published result rediscovered in the work.
- **CANDIDATE CONTRIBUTION:** concrete synthesis, algorithm, formula, or finite result that may be new but has not had a sufficient prior-art search.
- **OPEN:** evidence does not yet establish the claimed scope.
- **RETRACTED / CORRECTED:** a prior claim was tested and found false or overstated; do not reintroduce it without new evidence.

**Literature novelty is not certified by this handoff.** The corpus has already caught multiple instances where a result was new to the investigation but classical in the literature. External novelty claims require a targeted bibliography search against the exact theorem/algorithm—not a general search for similar vocabulary.

The safest novelty language is: “new in this project’s tested construction,” “candidate contribution,” or “a specific result whose prior-art status remains to be checked.”

---

## 4. Strongest current relation-vocabulary / representation results

### 4.1 The exact-sequence centre

For a finite equivariant chain/boundary setup, the declared cells, their generated cycle content, and the ungenerated quotient are joined by

\[
0\longrightarrow H_2\longrightarrow C_2
\xrightarrow{\partial_2} A\longrightarrow D\longrightarrow0,
\]

where

\[
H_2=\ker\partial_2,\qquad D=A/\operatorname{im}\partial_2.
\]

Additivity of characters in the representation ring gives

\[
[D]-[H_2]=[A]-[C_2],
\]

and therefore

\[
\boxed{\chi_D(g)-\chi_{H_2}(g)
=1-F_0(g)+F_1^{\pm}(g)-F_2^{\pm}(g)}
\]

for a connected graph arena, where the right side is the alternating fixed-cell trace. This counts **missing minus redundant**. It does not split the two terms without extra information. Splitting becomes possible when one side is identified structurally, for example by an equivariant trace isomorphism to the base graph.

### 4.2 The 12-vertex witness and its group

The witness walk has 24 states and a regular action generated by continue and turn. In register coordinates:

\[
C(p;a,b,c)=(p+1;b,c,a),\qquad
T(p;a,b,c)=(p+1;b,c,a\oplus1).
\]

The three-bit parity

\[
q(p;a,b,c)=a\oplus b\oplus c
\]

satisfies \(q(Cs)=q(s)\) and \(q(Ts)=q(s)\oplus1\). The generated group has order distribution \(1/7/8/8\) for elements of orders \(1/2/3/6\), and is isomorphic to \(C_2\times A_4\). Its unique nontrivial map to \(C_2\) is the parity of the flip mask:

\[
\phi(g_{k,d})=d_0\oplus d_1\oplus d_2,\qquad
\epsilon(g)=(-1)^{\phi(g)}.
\]

The central involution \(z=T^3\) maps to the swap. The regular permutation character itself does **not** select the swap: it is 24 at the identity and 0 elsewhere. The selected channel is supplied by \(\epsilon\), not by fixed-point counting on the walk states.

For \(f(g)=\epsilon(g)\), the line \(\mathbb Q f\) is the sign representation. The exact projector in state coordinates is

\[
P_\epsilon=\frac{ff^{\mathsf T}}{24},\qquad P_\epsilon^2=P_\epsilon,\qquad \operatorname{rank}P_\epsilon=1.
\]

For arbitrary weights \(w\),

\[
P_\epsilon w=\frac{f^{\mathsf T}w}{24}f.
\]

Continue preserves this coefficient; turn reverses it. This is an executable instance of a one-dimensional character channel, not a claim that all characters in the larger graph family are this sign channel.

The six rational irreducibles in the witness ledger are ordered \(1^+,1^-,2^+,2^-,3^+,3^-\), dimensions \(1,1,2,2,3,3\), with

\[
m(A)=(15,4,14,4,24,36),\quad \dim A=235.
\]

Central inversion splits \(A\) into 115 even and 120 odd dimensions. The 120 odd dimensions are the combined \(1^-,2^-,3^-\) isotypic pieces, not the single swap line. There are four copies of \(1^-\) in \(A\).

### 4.3 The 311-cell sign-channel split is explicit

For commuting squares plus rotation triangles, the sign channel has a concrete matrix \(M:\mathbb Q^9\to\mathbb Q^4\), rank 4, and kernel inclusion \(N:\mathbb Q^5\to\mathbb Q^9\), rank 5, with

\[
MN=0,\qquad \operatorname{im}N=\ker M.
\]

A section \(J\) satisfies \(MJ=I_4\); hence

\[
K=I_9-JM,\qquad K^2=K,\quad MK=0,
\]

and the nine-dimensional cell channel splits into five dependencies and four boundary-bearing coordinates. The split is basis-dependent, while the kernel dimension and surjectivity are not. The matrices and ambient cell/cycle basis labels are in the `sign_*.csv` package. This is an exact witness certificate, not a general canonical choice of complement.

### 4.4 Reader-relative method selection

In the witness ledger, a vocabulary \(F\) defines a submodule \(W_F\le A\); its deficiency vector is

\[
\delta(F)=m(A)-m(W_F).
\]

A prospective family must dominate this vector componentwise to have enough copies of the missing irreducibles. But domination is only a **necessary shortlist condition**, not proof of closure: repeated irreducible copies can land in the same submodule. Closure is certified by a span/rank equality at a faithful reader, then propagates through the reader lattice.

The reader’s role is the fixed-vector functional

\[
f_H(\lambda)=\dim(\lambda^H),\qquad
\text{observed quantity}=\langle m(V),f_H\rangle.
\]

The formula

\[
L_H(R\mid S)=\dim(Q_1(R\mid S)^H)
\]

and its monotonicity are standard finite-group representation theory in this setting. Candidate contribution: using this calculus to reconstruct the witness’s reader lattice, find a faithful-reader certificate, and reduce a broad search to multiplicity subtraction plus one certification.

The corrected isotypic overlap cap is

\[
I_{\rm cap}^{\rm iso}(R,S;H)=
\sum_\lambda\max(0,m_\lambda(R)+m_\lambda(S)-m_\lambda(A))\dim(\lambda^H).
\]

A scalar rank cap can hide overlap in a channel averaged away by a reader. On the witness, `disj/rot3` share one copy of \(1^-\) in the full module even though the full-automorphism invariant readout reports zero intersection. The same one line is visible exactly to the subgroup readers contained in \(A_4\).

### 4.5 Corrected virtual-character floor

Fixed cells determine \(m(D)-m(H_2)\), not either module on its own. The spectator-triangle virtual vector is

\[
(5,-1,4,-1,4,11).
\]

Its positive-part floor misses **one copy** of \(3^+\), a three-dimensional irreducible, not “one dimension per reader.” A reader sees \(\dim(3^+)^H\) dimensions of that copy. Keep this correction whenever quoting the floor method.

---

## 5. The scaled family: current structural results

### 5.1 Graph and arena counts

For the marked family \(\Gamma_n\), the n=2 witness is special; the marked-core construction/formula regime applies for \(n\ge3\).

\[
V_n=6n^2+6n,\qquad E_n=18n^2+3n.
\]

The two-token arena has

\[
C_{0,n}=\binom{V_n}{2}=18n^4+36n^3+15n^2-3n,
\]

\[
C_{1,n}=E_n(V_n-2)=108n^4+126n^3-18n^2-6n,
\]

and cycle-space dimension

\[
\dim A_n=1-C_{0,n}+C_{1,n}
=90n^4+90n^3-33n^2-3n+1.
\]

For the graph relation vocabulary,

\[
T_n=n^3+5n^2,\qquad R_n=T_n,\qquad
S_n=T_n(V_n-3),
\]

and the commuting-square count is

\[
Q_n=162n^4+15n^3-\frac{63n^2+3n}{2}.
\]

Finite exact tables at n=3..6 agree with these formulas; the source records symbolic count derivations as well. Do not apply the n≥3 mark formulas blindly to the special n=2 witness.

### 5.2 Why the core contributes \((n-1)^3\)

The triangle-filled core \(K_{n,n,n}\) is the join of three discrete n-point sets. Each has reduced degree-zero homology \(\mathbb Z^{n-1}\). Join homology gives

\[
\widetilde H_1(K_{n,n,n};\mathbb Z)=0,\qquad
\widetilde H_2(K_{n,n,n};\mathbb Z)\cong\mathbb Z^{(n-1)^3}.
\]

Equivalently, with zero-sum factors \(U_i=\{x\in\mathbb Q^n:\sum x_j=0\}\),

\[
H_2\cong U_0\otimes U_1\otimes U_2,
\]

with explicit generators \((e_{0,a}-e_{0,*})\otimes(e_{1,b}-e_{1,*})\otimes(e_{2,c}-e_{2,*})\). This explains the cubic redundancy; it is not merely a polynomial fit.

### 5.3 The witness’s closure fails to scale, but the residual is structured

For n≥3, commuting squares plus rotation triangles leave exactly

\[
\boxed{\dim D_{\square+\triangle}=4n^2}
\]

missing directions: two holes for each of the \(2n^2\) faces, between the core face triangle and the centreless mark triangle.

The new dependence count relative to commuting squares alone is

\[
\boxed{\dim H_{2,\square+\triangle}-\dim H_{2,\square}=(n-1)^3.}
\]

The ledger records

\[
\dim D_{\square}=12n^2-3n+1,
\]

\[
\dim H_{2,\square}=72n^4-75n^3+\frac{27n^2}{2}-\frac{3n}{2},
\]

\[
\dim H_{2,\square+\triangle}=72n^4-74n^3+
\frac{21n^2}{2}+\frac{3n}{2}-1.
\]

The values at n=3..6 match exact ranks and homology computations. Topological explanation: the \(4n^2\) residual is the mark/core face-annulus geometry; the \((n-1)^3\) dependency is the tripartite core’s second homology.

### 5.4 Fixed-cell counting can separate both sides when extra structure is available

For commuting squares, the total-trace map \(J\) identifies the deficiency with the base graph’s cycle space over \(\mathbb Q\):

\[
D_{\square}\cong H_1(\Gamma_n;\mathbb Q).
\]

Then the missing character is directly

\[
\chi_{D_{\square}}(g)=1-F_V(g)+F_E^{\pm}(g),
\]

where the fixed vertices and signed fixed edges are counted on the **base graph**, not on the two-token arena. The redundancy is recovered by subtracting this character from the arena/cell virtual character. This is why counting can split the two modules here; without the trace isomorphism or equivalent module data, the Euler character gives only missing minus redundant.

### 5.5 The family’s symmetry is Eisenstein (important latest update, §83)

The latest ledger sharpens the earlier family analysis. The sum-zero translation group is described as

\[
N\cong\mathbb Z[\omega]/n,\qquad \omega^2+\omega+1=0,
\]

and the quotient \(C_6\cong\mu_6\) acts by units of the Eisenstein ring. Class rotation is multiplication by \(\omega\); slope reflection is multiplication by \(-1\). The current ledger identifies

\[
G_n\cong (\mathbb Z[\omega]/n)\rtimes\mu_6
\]

and indexes channels by \(\mu_6\)-orbits on \(\mathbb Z[\omega]/n\). It states that the affine extension splits in tested cases n=2..12; when writing the all-n theorem, show the explicit section/proof, not only the finite check.

The orbit types depend on arithmetic:

- zero orbit gives the six linear characters;
- 2-torsion \(\mathbb F_4\) occurs for even n and yields degree-three types;
- \((1-\omega)\)-torsion appears when 3 divides n and yields degree-two types;
- remaining characters form free degree-six orbits, with line/double-orbit subdivisions and special corrections when 2, 3, or 4 divides n.

This is a high-value candidate contribution because it converts an opaque symmetry calculation into arithmetic on the Eisenstein ring. Preserve the divisibility split explicitly; do not assume one character list works unchanged for all n.

### 5.6 Current channel formulas and limits

The latest ledger §83 reports these complex-character multiplicities for n≥3, checked for n=3..22 and n=24, with structural explanations from induced/permutation modules:

| Type | \(D_{\square}\) | \(D_{\triangle}\) |
|---|---:|---:|
| \(1^+\) | 3 | 0 |
| \(1^-\) | 1 | 0 |
| \(2^+\) | 2 | 1 |
| \(2^-\) | 1 | 1 |
| \(3a\) | 5 | 2 |
| \(3b\) | 6 | 2 |
| \(2c\) | 4 | 1 |
| \(2r\) | 4 | 2 |
| \(6L\) | 11 | 4 |
| \(6g\) | 12 | 4 |

Types only exist in the relevant arithmetic regimes; e.g. the 2-torsion degree-three pair is for even n, and the ramified degree-two types are for 3|n. The labels `6Ld` and `6gd` denote double-orbit variants whose D multiplicities match `6L` and `6g`.

The ledger records quadratic formulas for the redundancy multiplicities, with residue corrections in n mod 2, 4, and 12; total dimensions were checked against closed forms over the 12 residue classes. Important scope limit: the constants for the `3a/3b` and `2c/2r` redundancy formulas are still described as recovered by fits, not yet derived from a complete stabilizer census. Keep those formulas labeled “verified fits / conjectured closed forms” until the remaining proof is written.

---

## 6. Exchange, orientation, and integral versus rational claims

On two unlabelled tokens moving on \(K_{3,3}\) with commuting-square relations, the configuration complex is a closed nonorientable surface with Euler characteristic \(-3\),

\[
H_1\cong\mathbb Z^4\oplus\mathbb Z/2.
\]

The labelled-token complex is the double cover and is orientable (genus four). The order-two exchange is the orientation-reversing loop; the exchange parity is the first Stiefel–Whitney class of the unlabelled surface. This is a structural identification supported by the certificates and the recorded surface calculation.

The integral certificate has 18 commuting squares with signs ±1 and

\[
\partial B=2z.
\]

For the entire n=3 arena a canonical detector is available. For a move \(\{u,v\}\to\{u',v\}\) with v stationary and the moving token crossing the parked token in vertex-order labels,

\[
\eta(\text{move})=[u<v]\oplus[u'<v].
\]

This is 1 exactly when the order-based labels exchange. At n=3 it has support 2,520 of 11,970 moves, evaluates to zero on all 13,239 commuting squares, and to 1 on the exchange. Combined with \(\partial B=2z\), it proves \([z]\) has exact order two. The abstract graph-braid torsion classification is recovered from published work; the explicit family realization, global detector, and reproducible certificates are candidate project contributions, not a claim that the underlying torsion theorem is new.

Keep these two survivors separate:

- **Exchange parity** lives in the commuting-square configuration complex and is the \(\mathbb Z/2\) torsion class.
- **Clock / circulation residue** is a graph-trace class; its period is zero around the exchange loop. It belongs to the square-filled arena and is not the exchange class.

### What declaring more triangle cells does

The ledger records at the witness:

| Relations declared | Integral H1 | Characteristic that remains |
|---|---|---|
| commuting squares | \(\mathbb Z^{19}\oplus\mathbb Z/2\) | exchange parity \(\eta\) |
| squares + rotation triangles | \(\mathbb Z/2\) | \(\eta+\text{length}\pmod2\) |
| squares + parked triangles | \(\mathbb Z/2\) | \(\eta\) |
| squares + both triangle families | 0 | neither survives |

A rotation triangle is itself a three-move exchange, so adding that cell identifies step parity with swap parity; a parked triangle then kills the remaining exchange parity. In the n≥3 family, the marked/core geometry makes the combined square+rotation-triangle vocabulary leave \(4n^2\) first-homology directions despite the witness’s closure. The extra integral survivor and the graph-level 4n² residue must not be conflated.

---

## 7. Hexadecimal transformation space and continuation-ledger work

The base-conversion experiment asks a method-level question: in converting an n-digit hexadecimal input to base \(b'\), how many input digits must be retained before the first most-significant output digit is fixed?

The finite table shows two patterns for tested sizes:

- If the bases are multiplicatively dependent (in particular, powers sharing the base-2 structure of hexadecimal), conversion can be done by bounded-window regrouping. Hex→2, →4, →16 require one input digit in the table; →8, →32, →64, →256 are bounded by two, though some values oscillate with length.
- For tested multiplicatively independent bases such as 3, 5, 7, 9, the first output digit may require the whole input; some bases such as 6, 10, and 12 show finite-length dips and need separate analysis.

The classification by multiplicative dependence / finite-state transducers is known mathematics. Candidate contribution: interpreting the lookahead cost as a *continuation ledger* and extracting the irregular dips as candidate partial windows. The finite table is not yet a full general formula for every target base.

The operational point is important: a shape is not a decorative picture of an output. It is the organization of the transformations, windows, carries, feedback, and returns that produces the output. To “read a missing method” without search, the method must admit a finite address-indexed representation or an equivalent exact constraint decomposition. That criterion is a research target, not a theorem that any arbitrary system must satisfy.

### Continuation-ledger runtime

The prototype uses coarsest continuation-closed refinement/partition refinement. It has found carry as an unlabelled necessary state in bounded binary-adder tests, rejected irrelevant state, and reproduced recorded reader-cut cases. The algorithms’ mathematical ancestry is Moore/Myhill–Nerode minimization. Candidate contribution: the specific continuation-ledger interface, diagnostics, and use as a method-recovery tool. Current open items include a general capacity-equality theorem and a formal relation between carry-capacity defect and pulled-back reader-loop count.

---

## 8. SHA-256 and BBP: what is actually established

### SHA-256

Maintain three separate tasks:

1. **Local reverse round with sufficient context:** exact reverse recovery of a round’s drive/message word from a fully supplied adjacent state pair and known round law has been reported and tested, including 20,000/20,000 trials in the cited paper. This is a constrained local inverse.
2. **Dependency/factorization audit:** the SHA work studies how output-side constraints separate, couple under backward propagation, and differ in forward propagation.
3. **Hash digest inversion / preimage / collision / security reduction:** not established. The corpus explicitly excludes claiming any of these from the local inverse or the number of derived views.

The count of many transformations, views, traversal outputs, or masks does not prove independent payload or reconstructability. A correct reverse procedure must state exactly which state, message schedule, context, and constraints are supplied. The intended major target remains: infer hidden transformation method from structure, then test the limits against SHA-256 without confusing a known-context inverse with a digest preimage attack.

### BBP and relation kernels

The BBP line has moved beyond raw annihilating coefficient vectors. The records distinguish:

- which relation shapes are forced by orbit/incidence constraints;
- which coefficients are freed because a prime-orbit has a partner capable of cancellation;
- which freed coordinates are actually occupied (still a distinct, open mechanism);
- where a relation is placed versus its seed shape and winding cofactor;
- what part of a relation is transported/inherited versus genuinely new.

The “partner predicate” makes incidence structure—not prime names alone—the forcing invariant. `The Placement Is Not The Prime` separates seed, winding, and placement/address. The exact signature `[4,-2,-1,-1]` occurs in a stated BBP construction, and the cross-tower ratio `9/4` is reported as constraint closure. The primitive positive-radix `sec^m(2π/m)` result has only m=6,8 in its stated scope; do **not** rephrase it as “the entire BBP kernel landscape has exactly two seeds.” The global version was falsified by a negative-base counterexample.

The occupancy mechanism and the q=15 transport/interaction experiment remain open or in-progress. Novelty candidate: a reusable decomposition of forced/free/occupied/placed/transported pieces and the particular BBP results, pending literature review and complete independent reproductions.

---

## 9. Normalized transfer spectrum and wider application papers

The transfer-spectrum thread proposes that at fixed \((n,K,p)\), allowed normalized singular values are universal while the substrate determines which levels are occupied and their multiplicities. The recorded proposed formula is

\[
\operatorname{mult}(\sigma_i([T_p]_G))=\epsilon(X,i+1)-\epsilon(X,i),
\]

with \(\epsilon(X,0)=0\), and

\[
\sigma_i^2=
\frac{\binom{m-i}{p-i}\binom{N-p-i}{m-p}}
{\binom{m}{p}^2},\qquad i=0,\ldots,p.
\]

A recorded sweep reports 77 matches over 12 substrates/nonempty \((K,p)\) cases, with no restricted singular values off the predicted grid. The cumulative-image/projector proof step was explicitly marked incomplete in the source. Thus the empirical pattern is strong, but do not call the universal theorem proved until that operator argument is closed.

Other papers connect the same method to stochastic/local balance, dynamical systems, neural network measurements, Navier–Stokes DNS, Crouzeix, and physical ontology. Each remains at its own evidentiary level. A finite DNS does not solve global Navier–Stokes regularity; a measured neural-weight pattern is not a universal law; an algebraic analogy does not derive a physical constitutive law. Physics needs units, independently measurable quantities, a specified law, and discriminating predictions.

---

## 10. Candidate novelty map — ranked by current support

This is a **research contribution map**, not a claim that every item has passed prior-art review.

### A. Strongest candidate contribution: the scaled marked-graph / character architecture

- The graph family’s arithmetic symmetry is identified with the Eisenstein-ring unit-affine action.
- The cell-character calculation separates deficiencies and redundancies and exposes the divisibility-dependent orbit families.
- The closure failure at n≥3 is explained geometrically as \(4n^2\) marked-face annuli plus \((n-1)^3\) tripartite-core dependencies.
- The same computations are packaged as per-element fixed-point tables, induced-character tables, exact matrices, scripts, and workbook checks.

The standard tools—Euler–Poincaré, character theory, induced representations, Schur-index arguments, join homology—are not themselves new. Candidate originality lies in this exact graph family, the Eisenstein channel parametrization, the channel formulas, and the structured bridge between cell vocabulary, graph homology, and readers. The `3a/3b` and `2c/2r` constants in redundancy still need derivation from a full stabilizer census.

### B. Exact finite-witness method for missing relations

The deficiency vector \(\delta(F)=m(A)-m(W_F)\) plus componentwise domination makes a principled shortlist of candidate closing families. A span certificate at a faithful reader then decides the actual closure. This replaces a full subset-by-reader brute-force search on the witness, while explicitly respecting the difference between “enough irreducible multiplicities” and “actual complementary subspaces.”

Potentially valuable applied method; the representation results it uses are standard.

### C. Explicit sign-channel realization and projectors

The 24-state walk realizes the unique nontrivial quotient character as a stateful continue/turn rule, and the \(9\to4\) boundary map exhibits the sign channel’s four boundary directions plus five kernel dependencies. The relation complex evaluates the same character through its own chain/module data. The precise shared machinery is character projection, **not** a claim that both systems select the character by counting fixed states.

Potentially novel synthesis/application; projector and representation facts are standard.

### D. Marked-core scaling result

For n≥3, \(4n^2\) residual directions persist after commuting squares+rotation triangles are declared, and the second-homology increment is \((n-1)^3\). The former comes from face/mark rings; the latter from \(K_{n,n,n}\) join homology. This is a clean testable scaling theorem, with all-n proofs needed for every formula stated beyond checked ranks.

### E. Canonical exchange detector and orientation interpretation

The order-based cochain detects exchange parity on every arena move; with \(\partial B=2z\), it gives a reproducible exact-order-two certificate. The abstract \(\mathbb Z/2\) graph-braid result is known. Project contribution candidate: canonical detector, explicit cell chain, family-wide construction, and identification with the orientation class in the displayed finite surface.

### F. Continuation-ledger / hexadecimal method reading

The project’s contribution may be the formalized method-reading workflow and the specific lookahead/ledger measurements, not the known multiplicative-dependence classification. Next required result: explain the non-worst-case dips and show how the predicted ledger recovers a method without searching. Then use SHA-256 as the concrete hard target.

### G. BBP constraint closure and transport

The current strength is the precise factoring of forced/free/occupied/placed/transported structure and scoped exact coefficient results. Before calling a claim novel, complete the q=15 transport experiment, archive the bases, close the occupancy gap, and search prior art for the exact theorem statement.

### H. Transfer-spectrum universality

77/77 tested cases and the stated singular-value formula are candidate evidence. Novelty remains open until the cumulative-projector proof is complete and literature has been checked.

### I. Universal physics/ontology

Important research motivation, but **not established by the current finite computations**. Do not present claims about mass, gravity, spacetime, heat, or the universe as mathematical consequences of the graph, hexadecimal, BBP, or SHA work.

---

## 11. Known mathematics versus project contribution

Do not re-claim these as inventions:

- Moore / Myhill–Nerode state minimization and deterministic transducer ideas.
- Maschke, character projectors, character inner products, induced representations, Frobenius reciprocity, and equivariant Euler–Poincaré.
- Join homology of the complete tripartite core.
- Standard graph braid/configuration-space results about torsion for non-planar graphs, once their hypotheses are checked (the ledger cites Ko–Park and Harrison–Keating–Robbins–Sawicki).
- The general principle that multiplicative dependence of bases enables bounded transduction.
- Standard stochastic carry-chain/eigenvalue facts where the source explicitly identifies the known literature.

What might be new is a precise application, a new theorem for the stated family, a canonical certificate, a tested algorithm, a new counterexample, a closed-form multiplicity profile, or a successful method of recovering a missing relation from a typed deficit. Novelty must attach to one of those exact claims, not to a broad slogan.

---

## 12. Corrections and exclusions that must persist across sessions

1. **Missing minus redundant:** fixed-cell counts give \([D]-[H_2]\), not both terms separately. Separation needs additional structural information.
2. **Spectator-triangle floor:** the miss is one copy of the three-dimensional \(3^+\) irreducible, not one dimension at every reader.
3. **Odd bin vs swap:** the 120-dimensional odd sector is \(1^-\oplus2^-\oplus3^-\) isotypically; the swap is only the \(1^-\) character (four copies in \(A\)).
4. **Regular action:** its fixed-point character selects no particular line. The quotient character \(\epsilon\) and projector select the parity line.
5. **Commuting-square separation:** use the graph-level trace isomorphism to count missing channels on the base graph; do not call this an arbitrary ability of fixed-cell counting to split virtual characters.
6. **Rational vs integral:** rational traces do not see torsion. Use integer Smith/boundary certificates and an independent mod-2 detector.
7. **Local SHA reversal is not digest inversion:** known context/state must be specified. No preimage/collision/security reduction is established.
8. **Freed is not occupied:** a kernel coordinate freed by a constraint need not be occupied by a realized relation.
9. **Shape/multiplicity is not span:** multiplicity dominance is necessary; a faithful-reader span certificate is what proves closure.
10. **Finite sweep is not all-n theorem:** state exact n-range unless a structural proof follows.
11. **Physics analogy is not physical law:** leave constitutive assumptions and measurable predictions explicit.
12. **Do not treat a failed mechanism as unproductive:** preserve null, retraction, and controls; they narrow the legal explanation space.

---

## 13. How AI sessions must work

### First response after loading this file

1. State the exact sub-thread and source section being continued.
2. Rephrase the mathematical object/flow, not just a list of nouns.
3. Identify the next single proof/check or artifact that directly advances the open claim.
4. Do not ask the user to choose between projects already chosen in the record.

### Mode control

Use one of these modes when appropriate:

- **BUILD:** generate a concrete artifact or implementation.
- **TEST:** state the contract, run a bounded test, report exact values and limits.
- **FIX:** diagnose one named failure and make the smallest change.
- **DOC:** document existing results without adding theory.
- **AUDIT:** compare claims to evidence and source files, including contradictions and retractions.

Do not convert TEST into a new project. Do not convert DOC into a theory manifesto.

### Standard execution workflow

```text
1. Load the latest ledger section and the exact input/certificate.
2. State definitions, indexing, coefficient field, orientation/sign conventions.
3. Reconstruct the object from its definition (do not trust CSV labels alone).
4. Run exact algebra first; use modular rank only with a stated bound argument.
5. Compare against the supplied table/held-out sizes.
6. Search for counterexamples and parity/divisibility cases.
7. Separate theorem, computed fact, literature result, interpretation, and open step.
8. Update the ledger with the script, input hash, output rows, failure conditions, and correction history.
9. Stop at the requested deliverable.
```

For every count/rank/character table, report the object, relation vocabulary, group/action, field, basis/orientation, tested range, and whether the value is exact or approximate. If a script is run, preserve it and its output. If something is not tested, say exactly what was not tested. Avoid “verified” unless there is a direct check that can fail.

### Preferred reasoning style

- Describe the transitions/compositions/closures first; derive object names and abstractions afterward.
- Distinguish what moves, what is transported, what is conserved, what becomes readable, and what changes the future admissibility.
- Keep the two sides of the reader/vocabulary pairing separate: a channel may exist but be invisible to a reader; a reader may see a channel that the chosen vocabulary never generates.
- Say “recovered” if known; “computed” if finite exact; “proved” only with a proof; “candidate novelty” if prior art is not checked.
- Don’t present reaction/intensity as evidence.

---

## 14. Active queue, kept in order

### Immediate relation/character continuation

1. In the live ledger §83, complete the stabilizer census for the redundancy channels `3a/3b` and `2c/2r`; replace quadratic fits with derivations, with n mod 2/4/12 cases explicit.
2. Write the all-n proof of the Eisenstein affine group identification and its splitting/section. The record directly checked splitting for n=2..12; show why the section exists for arbitrary n before stating an all-n isomorphism without qualification.
3. Produce a concise theorem/proof for \(H_2(K_{n,n,n};\mathbb Z)\cong\mathbb Z^{(n-1)^3}\), the explicit generator action, and the alternating trace equations; keep the marked-face annulus deficiency separate from core H2 redundancy.
4. Maintain the integral exchange certificate as two parts: \(\partial B=2z\) and \(\eta(z)=1\) with \(\eta\) zero on all declared cells.
5. Keep the walk projector matrix and sign-channel 9→4 splitting as witness examples; do not assert the same six irreducibles survive for all n.

### Strategic spine (does not disappear)

6. Continue the hexadecimal method-cost question: explain bounded and sub-worst-case lookahead, particularly the target-base dips, as exact method structure rather than value patterns.
7. Use the continuation-ledger machinery to formalize what counts as a recoverable missing method without search.
8. Test that procedure against SHA’s dependency/round structure. Keep local reverse round, known-context reconstruction, and digest preimage as three different problem types.
9. For BBP, keep forced/free/occupied/placed/transported distinctions separate; close q=15 and the occupancy question before claiming generality.
10. For transfer spectrum, complete the cumulative-image/projector proof before asserting universality.

No new physical domain, broad ontology thesis, or replacement target should be opened merely because an analogy appears. User direction takes precedence.

---

## 15. Source and artifact index

### Primary current state

- `relation-vocabulary-ledger (31).md`: technical chronology §§1–83; the latest section §83 updates the status of the scaled-family character problem that §82 had still called open. Read the latest correction/section rather than quoting the older status.
- `NEXUS_family_realizability_and_exchange.xlsx`: 15-sheet workbook, including the global exchange detector, n=6 Schur-index proof, exact characters, detector values and reproduction code.
- `nexus_character_lab.html`: offline interactive orbit/character/core/Smith calculator (n=3,4); decimal display is approximate, exact tables are stored.
- `nexus_exact_certificates.zip`: matrices, generator bases, projectors, action/coboundary data, orbit tables and Smith certificates. Scope of its Smith certificate is two tokens on K3,3, commuting-square cells.
- `scaled_character_checks.csv`: per-element fixed-cell/character audit for n=3..6.
- `fixed_cell_verification.csv`, `group_elements.csv`, `character_and_quotient_verification.csv`: witness fixed-cell, walk-group and quotient checks.
- `sign_boundary.csv`, `sign_kernel_inclusion.csv`, `sign_section.csv`, `sign_cell_basis.csv`, `sign_cycle_basis.csv`, `sign_basis_labels.csv`: explicit sign-channel boundary split.
- `integral_exchange_certificate.csv`, `integral_exchange_detector_eta.csv`, `integral_exchange_detector_checks.csv`, `verify_integral_exchange_mod2.py`: integral exchange/boundary and global detector certificate.
- `Gn_complex_irrep_multiplicities.csv`, `Gn_rational_irrep_multiplicities.csv`, `Gn_rational_decomposition_checks.csv`, `Gn_character_reconstruction_checks.csv`, `verify_gn_character_descent_exact.py`: complex/rational channel tables and checks.
- `walk_sign_projector_matrix.csv`: exact rank-one character projector.

### Larger synthesis / process guidance

- `Review-This-Analysis_2026_10_10__0612.md`: consolidated review, correction history, cross-project claims and status distinctions.
- `Getting-organized_2026_10_10__0626.md`: larger corpus architecture, BBP/SHA/transfer-spectrum synthesis, ranked open problems, and the history of assistant drift.
- `Normalized-transfer-spectrum-and-substrate-independent-geometry_2026_09_16__0554.md_2026_10_10__0611.md`: long record of transfer spectrum, reader/geometry work, SHA, BBP, and prior AI interactions.
- `Distinction_That_Must_Continue.docx`: current interaction-first conceptual paper; use it for the paper’s formal wording, but use the ledger for latest corrections/computed status.
- `Getting-organized_2026_10_09__0311.md`: prior synthesis, useful for context but superseded in places by the 10 October ledger and handoff.

---

## 16. One-paragraph handoff prompt to paste into a new AI session

You are continuing NEXUS, not starting a new project. Read `NEXUS_AI_HANDOFF_2026-10-10.md` and then the latest section of `relation-vocabulary-ledger (31).md` relevant to the requested task. The global research spine remains: (1) hexadecimal transformation space, (2) shapes as methods, (3) infer missing methods without brute-force search, (4) test against SHA-256. The current graph/token/character work supplies exact test machinery: equivariant chain sequence `0→H₂→C₂→A→D→0`, fixed-cell Euler characters, witness sign quotient/projector, marked-family scaling, Eisenstein symmetry and integral exchange certificate. Preserve the distinctions between missing and redundant, swap and the full odd bin, complex and rational decomposition, rational and integral homology, and computed results versus general proof. Describe movements and compositions first. Use BUILD/TEST/FIX/DOC/AUDIT; don’t choose new targets, inflate analogies into theorems, or claim novelty before a targeted prior-art audit. Report exact input, coefficient field, conventions, tests, result, and remaining uncertainty. Update the ledger and artifacts, then stop at the requested deliverable.
