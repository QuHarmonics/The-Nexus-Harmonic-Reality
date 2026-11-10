# NEXUS Manual — reader / method reference

**v0.1, 5 Oct 2026.** A working reference, written the way you would document a codebase:
types, interfaces, contracts, error codes, a cross-reference into the existing corpus, and a
test index. It is a map of what has been *run*; it is not a new result and adds no claim that
is not already in a ledger or a script.

Companion documents: `claude/relation-vocabulary-ledger.md` (§§1–60, the run log) and
`claude/program-overview-both-directions.md` (the standing four, as of §48).

---

## 0. How to read an entry

Every entry carries four tags. An entry missing one is not finished.

| tag | meaning |
|---|---|
| **forward** | how it is reached from constraint — nothing put in but the rule |
| **backward** | the established name it collides with, and who had it first |
| **status** | `run` (script named, output on record) · `run-earlier` (in a project doc, not re-run) · `corpus` (in Merged / Combined, not audited here) · `queued` (prediction written, test not yet executed) |
| **scope** | which parameters were pinned when it was measured |

**Precedence rule.** Where forward and backward meet, the result is *recovered* and belongs to
whoever published it first. Where only forward reaches, it is data and an open question.

**Both-directions rule.** A statement is entered only after it has been run in reverse — the
converse, the control that should fail, or the same quantity by an independent route.

**The pinned-parameter list.** Almost everything in §§57–60 was measured with all of these
pinned. Agreement between readers of the work cannot detect a pinned parameter; only a
changed run can.

```
K = 2            token count
X = witness      12 vertices, 30 edges, Aut(X) = C2 x A4 of order 24   (plus 4 control graphs)
cells = C<=4     all arena cycles of length 3 and 4                     (C<=L swept in §59 only)
field = Q        except the clock, which lives mod d
reader = subgroup of Aut(X)   26 of them
```

---

## 1. Quick start — the one fully worked object

Two tokens on the witness graph. Twelve of the 66 configurations form the **interior**. Every
layer of the framework can be read off those twelve states, and every line below has a script.

```
state        an unordered pair of adjacent tokens on the octahedral core      12 of them
reader G     cannot tell the 12 apart            -> every exact invariant price is 0 here
orient       G never swaps a pair's two ends     -> state = (prev, cur)
step         every interior move is (prev,cur) -> (cur,next)                  24 of 24
project      (prev,cur) -> cur is exactly 2-to-1                              1 bit erased
methods      T+, T-  : the two deterministic continuations, each four 3-cycles
shape        Cayley graph of <T+,T-> = the interior = cuboctahedron           edge for edge
relations    T+^3 = T-^3 = (T- T+^-1)^2 = 1      -> 4 + 4 triangles, 6 squares = 14 faces
residue      the K4 survivor h = 7529 on every forward step
period       22587 = 3 x 7529                    -> triangles carry it, squares cancel it
clock        U mod 22587, shifts by a character of order 3
reader H8    kernel of that character, order 8   -> 3 classes of 4 = 3 clock phases
cost         3 = chromatic number of the shape   -> the cheapest reader that resolves it
```

Scripts: `nest.py interior.py sphere2.py recheck.py why.py medial.py cutoff.py bind.py`.

---

## 2. Types

Each type: what it is, how it is constructed, its invariant, where it already appears in the
corpus, and its established name.

### `Arena`
- **is** the graph of K-token configurations on a base graph X; edges are single token moves.
- **constructor** `arena(n, E, K)` → 66 vertices, 300 edges on the witness at K = 2.
- **backward** Abrams' discrete configuration space UD^K(X) once the commuting squares are
  filled (`relation-layer-omitted-cycle…md`). *recovered.*
- **status** run. **scope** K = 2, 3 in earlier docs; K = 2 here.

### `Cell` / `Vocabulary`
- **is** a declared relation: a closed arena walk that is asserted to carry no circulation.
  A vocabulary is a set of cells; C≤L is "all cycles up to length L".
- **invariant** rank ∂₂ ≤ cycle rank of the arena (235 on the witness; reached at L = 4).
- **backward** first path homology (Grigor'yan–Lin–Muranov–Yau) at C≤4, trivial reader.
- **status** run-earlier (`relation-layer-paper-and-theorem.md`), rank re-run in `recheck.py`.

### `Reader`
- **is** a subgroup H of Aut(X). It identifies configurations in the same H-orbit.
- **invariant** what H can see of a module is dim λ^H = ⟨χ_λ, ℚ[G/H]⟩. The most symmetric
  reader sees one irreducible type of six.
- **backward** Frobenius reciprocity. *recovered* (ledger §47–48).
- **corpus** "everything is a reader and being read"; the reader-side cut of *Two Quotients*.
- **status** run. **scope** the 26 subgroups of C₂ × A₄.

### `Interface`
What a reader exposes. Three have been built; they differ in degree and in coefficient ring.

| interface | type | zero set | status |
|---|---|---|---|
| exact invariant price `p = dφ` | 1-cochain over ℚ, φ constant on H-orbits | every edge inside an H-orbit | run |
| clock `U mod d` | potential over ℤ/d, invariant up to a character | nothing on the interior | run |
| orientation cochain `α` | 2-cochain | — | run; its value 14 is a face count, nothing more |

### `State`, `Mark`
- **is** on the interior, a state is a core edge; the reader's own orientation makes it
  `(prev, cur)`. The mark is `prev`.
- **invariant** `project: (prev,cur) → cur` is exactly 2-to-1.
- **corpus** *Merged*, "The edge is the state; the projection is the writer": the step on
  edges is the reader, the projection erases exactly one bit. Same table, found here with no
  construction added.
- **backward** line digraph of an oriented graph; the edge-state lift used for
  non-backtracking walks. Named, not re-read this session.
- **status** run (`bind.py` H1). **scope** needs a reader that never swaps an edge's two ends.
  The full octahedral group does swap them, so this type does not exist for that reader.

### `Method`
- **is** a deterministic continuation rule on states. On the interior there are two that the
  A₄ reader admits: T₊ and T₋.
- **invariant** each is a permutation of the 12 states with cycle type 3⁴; together they act
  regularly; z T₊ z = T₋.
- **backward** generators of A₄; the interior is its Cayley graph (standard — MathWorld lists
  the cuboctahedral graph as a Cayley graph on two 3-cycles).
- **corpus** standing item 2, "shapes are methods". On this object it is literal: the shape is
  the graph of the methods and its faces are the relations among them.
- **status** run (`bind.py` H2).

### `Residue` (class)
- **is** an invariant cochain closed on every declared cell and not exact. On the witness at
  C≤4-squares-only there is one, h.
- **invariant** h on the interior is `7529 ×` (forward indicator), whichever representative is
  chosen, because exact invariant cochains vanish there.
- **corpus** the 𝒦₄ survivor of `relation-layer-k4-refutation.md`, first coordinate −7529.
- **status** run (`bind.py` H3).

### `Clock`
- **is** the residue reduced mod its period d: a single-valued potential U with
  U(w) − U(v) ≡ h(v→w).
- **invariant** U∘g − U is a character G → ℤ/d. On the witness it has order 3 and kernel of
  order 8.
- **corpus** `the-clock-mod-d.md` §3 (the lemma) and §4 ("present mod d; what is missing is
  the lift from ℤ/d to ℤ"). *Merged*, "the quotient is the weight, the remainder is the
  reading" says the same of n = 8k + r.
- **backward** a potential equivariant up to a 1-cocycle, i.e. a class in Hom(G, ℤ/d).
- **status** run (`bind.py` H4).

### `Cut`
- **is** a quotient of states by a reader, judged by four clauses: (1) boundary, (2) exact
  compression, (3) a transition that moves what the quotient distinguishes, (4) an induced
  update that reads only a bounded part.
- **corpus** *What a Cut Must Do to Make a Thing* v1.4 — proved for the adder.
- **status** on the interior: `queued` (test D2 below). The price-null reader fails clause 3
  by construction; that much is run.

---

## 3. Interfaces — signatures and contracts

Written as calls. The contract is the measured law; the number in brackets is the entry in §4.

```
internal(H)        -> edges with both ends in one H-orbit
blind(H)           -> cells whose whole boundary is internal(H)
   ensures  H1 <= H2  =>  internal(H1) c internal(H2)  and  blind(H1) c blind(H2)      [L2]
   ensures  blind(trivial) = {}                                                         [L2]

price(phi, H)      -> p = d(phi), phi constant on H-orbits
   ensures  p(e) = 0 for every e in internal(H)                                         [L3]
   ensures  length_w(c) = 0  <=>  c in blind(H)        (w = F(|p|), F(0) = 0)           [L3]

interior(X, H)     -> the graph on internal(H)
   ensures  = medial graph of the core, when the core's edges are one H-orbit           [L4]
   ensures  otherwise: the medial graph cut along H's orbit boundaries                  [L4]

closes(core, L)    -> does the interior's C<=L complex form one closed surface?
   ensures  true exactly at L = core degree d (deltahedral cores tested)                [L5]
   ensures  rank d_2 is constant for L >= d; extra cells only add redundancy            [L5]

orient(state, H)   -> (prev, cur)
   requires no h in H swaps the two ends of any state                                   [L6]
step(prev, cur)    -> {(cur, next)}        exactly 2 continuations on the interior      [L6]
project(prev, cur) -> cur                  exactly 2-to-1                               [L6]

T+, T-             -> permutations of states
   ensures  regular group of order 12; Cayley graph = interior; faces = relator cosets  [L7]

circulation(h, loop)
   ensures  = 3t on a triangle, 0 on a square, on the interior (t = 7529)               [L8]
   ensures  period(h) = 3|t|                                                            [L8]

clock(state)       -> Z/d
   ensures  clock . g - clock = chi(g), chi a character of order 3                      [L9]
   ensures  ker chi = the largest reader whose classes properly colour the interior     [L9]
```

---

## 4. Laws

Numbered so they can be cited. Each is a test that passed and a control that could have failed.

| # | law | control that could have failed | script | status / scope |
|---|---|---|---|---|
| L1 | A zero returned by an interface is a fact about the cut until the null support has been inspected | the null support could have been unstructured; it was a sphere | `interior.py` | run / witness |
| L2 | Refining the reader never creates blindness | 100 comparable subgroup pairs, 0 violations; the reversed inclusion fails on 45 | `recheck.py` C4 | run / 26 readers |
| L3 | An exact invariant price is zero exactly on reader-internal edges | order-8 reader: 0 null edges, all 14 faces priced, min 40 | `recheck.py` C2 | run / witness |
| L4 | Interior = pivot graph = medial graph of the core, if core edges are one orbit | pentagonal bipyramid: two disjoint pentagons instead of the 15-vertex medial graph | `medial.py`, `cutoff.py` | run / 5 graphs |
| L5 | The interior closes into one surface at L = d and only there; above d the boundary rank is constant (7, 13, 31) | L swept 3…6 on four cores | `cutoff.py` | run / vertex-transitive deltahedra |
| L6 | If no reader element swaps an edge's ends, states are (prev, cur), every interior move is a step, projection erases one bit | 24 of 24 head-to-tail; 0 tail-to-tail, 0 head-to-head | `bind.py` H1 | run / witness |
| L7 | The two continuation rules generate a regular group whose Cayley graph is the interior; faces are relator cosets | equality as edge sets, not up to isomorphism | `bind.py` H2 | run / witness |
| L8 | The surviving class is the forward indicator on the interior; period = 3 × its value | representative-independence checked on all 8 closed invariant cochains | `bind.py` H3 | run / witness, squares-only vocabulary |
| L9 | The clock is invariant up to a character; its kernel is the cheapest resolving reader | 24 clock values = 24 orbits of that kernel, constant on each, separating them | `bind.py` H4, `color.py` | run / witness |
| L10 | Deficiency is a module: χ_D = χ_A − χ_W answers every reader channel from one character | two independent routes to m(A) = (15, 4, 14, 4, 24, 36) | ledger §45 | run / witness |
| L11 | Saturation at the invariant reader does not certify closure | the 3⁻ witness: dim W^G = dim A^G = 15 with A/W ≠ 0 | ledger §46–47 | run / witness |
| L12 | Minimal orbit-generation of the relation module is max_λ ⌈m_λ s_λ / dim λ⌉ = 15, attained | explicit 15-set | ledger §47–48 | run / witness, over ℚ only |
| L13 | Detection is not closure; using a channel is not erasing it (I_h = 3, L_closure = 4) | cycle graphs, where the two coincide | `c1-is-the-abrams-hypothesis.md` §4 | run-earlier |
| L14 | h mod d is always exact: a single-valued clock exists | BFS potential checked on every edge | `the-clock-mod-d.md` §3 | run-earlier; re-run in `bind.py` |
| L15 | A static potential drives zero current through a residue channel | mixed drive gives exactly the non-gradient throughput | `c1-is-the-abrams-hypothesis.md` §5 | run-earlier / C₅, C₇ |
| L16 | On C_n, "no configuration is stuck" ⟺ n ≥ K+1 ⟺ Abrams' hypothesis (B′) | the K = n row | same doc §1 | run-earlier |
| L17 | 𝒦₄ = 𝒦_disj ⟺ X has no 4-cycle subgraph | 20 graphs, 0 mismatches | `instances-corrected-the-lemma.md` | run-earlier |
| L18 | Reader cut of the adder factorises over runs: F(S) = ∏ f(R) | proved all n | *Two Quotients* | run-earlier / proved |
| L19 | A gap of g positions forgets the carry iff m − 1 < b^g | 220 triples | `carry-capacity-ledger.md` | run-earlier |
| L20 | A digit at address n is directly readable when the pre-address part folds to computable residues and the tail contracts; alignment only makes it cheap | hex digits of e, with no 16^−k scale | `addressability-cost.md` | run-earlier |
| L21 | Put in only "cannot hold still, cannot escape": shapes are forced and countable — 0, 1, 5, 83 | OEIS A035512 | overview, item 2 | run / n ≤ 4 |

**An observation, not yet a law.** Below the cutoff the shortfall in boundary rank counts the
missing relations minus one: octahedron at L ≤ 3 has rank 8 against cycle rank 13, a deficit
of 5 = 6 vertex figures − 1; icosahedron at L ≤ 4 has rank 20 against 31, a deficit of
11 = 12 − 1. That is standing item 3 in miniature — the missing methods are *counted and
sized* by the deficit without enumerating them. Two cases, both from `cutoff.py`.

---

## 5. Error codes

The ways this work has gone wrong, each with the instance and the test that caught it. These
recur; the table is here so the next one is recognised on sight.

| code | what it is | instance | caught by |
|---|---|---|---|
| `E-VACUOUS` | a test that cannot fail | 2000 random cochains paired with the zero vector (§57.5) | asking what the other operand was |
| `E-FUSED` | two independent facts spliced into one causal chain | "price-null → S² → H₂ → C² → 14 → χ = 3" (§57) | running the cure for one against the other (order-8 reader, degree 1) |
| `E-PINNED` | a parameter held fixed everywhere, so agreement cannot see it | m = 2 operands; base 2; K = 2 here | changing it (carry-capacity; §59's L sweep) |
| `E-UNRUN` | a mechanism written down without being executed | "order-3 orbits are the four triangles" (§57.6) | the table three lines above it |
| `E-PRESORT` | output classified against an expectation before being read | six documents sorted "actionable / interpretive" (§54); `di3` (§56) | state what a measurement *separates* before what it *selects* |
| `E-FIXED-OBSERVER` | moving the object while holding the observable still | ⟨α, g·[Σ]⟩ = ±14 read as a failure (§57.5) | moving both |
| `E-GAP-IN-FIELD` | attributing a reader's zero to the object | "the 14 cells are unreachable" | L2: the zero moved when the reader did |
| `E-NAME-AS-RESULT` | arriving at a named object and stopping | "it's a cuboctahedron" (§57) | asking why (§58: it is the witness's own octahedron) |
| `E-DETECT≠CLOSE` | one name covering two operations | L_closure 3 vs 4; I_h vs L_closure | computing both |
| `E-REP` | a number that depends on the representative chosen | period 9 vs 22587; "24 = \|Aut\|" | L8, L9: quote ratios and characters, not raw values |
| `E-DIM` | a bookkeeping formula wrong while the data are right | Schur index multiplied into a dimension (§57.4); π(W) for W^G (§46) | an independent dimension count |
| `E-PARITY-OF-EVIDENCE` | a population that cannot exhibit the failure | 784 cases, all with dim ℋ¹ = 1 | `relation-layer-k4-refutation.md` |
| `E-BASE-2` | a base-2 magnitude read as a base-free law | Prop 5's "odd ⇒ no digit decomposition", false at b = 3 | *What a Cut Must Do* v1.4 |

---

## 6. The map — where each piece already lives

Rows are objects; columns are where they appear. "bound" means the link was executed on the
same data in this session; "pointer" means the structures match on paper and nothing was run.

| object | relation-layer (this ledger) | older corpus | established name | link |
|---|---|---|---|---|
| state = (prev, cur) | §60.1 | *Merged* Part III, "the edge is the state" | line digraph; edge-state lift | **bound** |
| writer erases one bit | §60.1 | *Merged* Part III, writer `(prev,cur) → cur` | 2-to-1 projection | **bound** |
| mark = prev | §60.1 | *Merged* §2 "every real change must leave a mark in something other than itself" | history coordinate | **bound** for the edge structure |
| memory layer makes the world reversible | — | *Merged* §4, third result (binary ring) | second-order reversible automata (Fredkin's construction) | pointer; arena test queued (D1) |
| methods T₊, T₋ | §60.2 | standing item 2; "the hidden methods in the shape of math are the controls" | generators of a regular group | **bound** |
| faces = relations | §60.2 | — | Cayley complex of a presentation | **bound** |
| 3-cycles as the unit of change | §60.2, §60.3 | *Merged* Part X, "the quantum of change is 3" | minimal support in an alternating group | pointer: T± are products of 3-cycles; the period is 3t |
| fixed-point-free involution | §57.4 (z), §60.2 (T₋T₊⁻¹) | *Merged* Part IX, the commutator that is "nearly weightless and fully opaque" | — | pointer; test queued (D3) |
| reader commutes with method | §60.2 | *Merged* Part IX "transparency = commutation"; Part XI "build along a commuting axis"; C1a | left and right regular actions | **bound** for A₄; z does not commute |
| reflection layer vs rotation layer | — | *Combined*, "reflection, rotation, spiral" | Cartan–Dieudonné | pointer; test queued (D3: involutions generate the clock's kernel) |
| residue h | §60.3 | `relation-layer-k4-refutation.md` | invariant harmonic class | **bound** — same vector reproduced |
| use at 3, erase at 4 | §60.3 | `c1-is-the-abrams-hypothesis.md` §4 | — | **bound** |
| triangles full rank, squares half | §60.3 | `relation-layer-omitted-cycle…md` | rank access | **bound** on the interior |
| clock mod d | §60.4 | `the-clock-mod-d.md` | potential mod d; lift obstruction | **bound** |
| "24 values" | §60.4 | same doc, recorded as coincidence | orbits of a kernel | **bound** — explained |
| quotient is weight, remainder is reading | §60.4 | *Merged*, BBP planes; n = 8k + r | winding number and phase | pointer |
| cheapest resolving reader | §57.6, §60.4 | *What a Cut Must Do*, four clauses | proper colouring | half bound; clause test queued (D2) |
| price-null ≠ absent | §57.9 | project instructions, "unreadable is not absent"; `c1…md` §5 "the residue is what no potential can realize" | exact vs closed | **bound** |
| interior sphere | §58 | `relation-layer-odd-cycle-blind-spot.md` already records "degree-7 part is the octahedron K(2,2,2) with antipodal pairs (0,3),(1,4),(2,5)" | rectification / medial graph | **bound** — the earlier note was the answer to §57's question |
| closure cutoff | §59 | L_closure in the paper; "bounded-closure problem" | relator length | **bound** on 4 cores |
| arena | §1–60 | *Two Quotients* cites Abrams as context | discrete configuration space | recovered |
| deficiency module | §43–48 | — | characters, Maschke, Frobenius | recovered |
| generation bound 15 | §47 | — | relation gap problem (rational side) | recovered; integral side open |
| forced shapes 0, 1, 5, 83 | — | project instructions | OEIS A035512 | recovered |
| addressing | — | BBP papers in *Merged*; `addressability-cost.md` | BBP; x ↦ 16x mod 1 | recovered |
| reader cut of the adder | — | *Two Quotients*, *What a Cut Must Do*, *Carry Capacity* | Myhill–Nerode | recovered |

**Not on the map.** H = π/9; the nine primitives; the 357 packet system and triadic 9-loop
programs; SonicDMX; SHA-256 as a C1-forward encoder; the mirror lattice; the RH operator work
in *Combined*. None has a run on record in the audited material, and nothing in §§57–60
touches them. The period 9 under the trivial reader and "triadic" are both threes; that is
not a link until a test says so (D4 is the test).

**Public record.** By search only — ORCID and Zenodo listings were not readable from this
session. Titles found on Zenodo under your name: *The Harmonic Ninth*; *Recursive Stack
Harmonics and Layered Logic Dynamics*; *The Nexus Recursive Harmonic Framework* (several
versions, including the KRRB paper and RHF RC1); *The Nexus Complete Fold*; *The Nexus
Framework: A Unified Meta-Computational Ontology of Recursive Harmonic Folding*. Only two
abstracts were read. None is bound to anything above.

---

## 7. Other domains — collisions and near-collisions

Same discipline: a collision is entered only where the structure was run here. "recalled"
means the outside result is quoted from memory and was not re-read this session.

| domain | their object | our object | state |
|---|---|---|---|
| group theory | Cayley graph of A₄ on two 3-cycles; presentation ⟨a, b ∣ a³, b³, (ab⁻¹)²⟩ | interior and its 14 faces | run; source checked (MathWorld) |
| group theory | abelianization A₄ → C₃ | the clock's three phases; T₊ and T₋ both step the phase by one | run in substance (L8, L9); naming recalled |
| group cohomology | function equivariant up to a 1-cocycle | clock with a character of order 3 | run; naming recalled |
| modular representation theory | Maschke fails when p divides \|G\| | Lemma 8.1 of Paper IV holds over ℚ and has an exception mod d, at the prime 3 | run for the exception; this is the first place the programme touches the integral side that the relation-gap problem lives on |
| polyhedra | rectification: tetrahedron → octahedron, octahedron → cuboctahedron, icosahedron → icosidodecahedron | interior of each core at L = d | run (`cutoff.py`) |
| crystallography | pyritohedral point group T_h ≅ A₄ × C₂, the symmetry of pyrite | Aut(X) acting on the core | naming recalled; the group and its action are run |
| topology of graphs | Abrams' discrete configuration space; Prue–Scrimshaw bound | arena with commuting squares | recovered, cited in earlier docs |
| path homology | GLMY: cycle space modulo 3- and 4-cycles | C≤4 at the trivial reader | recovered, cited in earlier docs |
| automata | Myhill–Nerode state count | reader cut of the adder | recovered, earlier papers |
| reversible computing | second-order automata: next = f(present) combined with previous, always invertible | *Merged* §4 memory layer; on the interior, a rule is a bijection iff prev → next is a bijection at each cur | recalled; arena census queued (D1) |
| symbolic dynamics | de Bruijn graph as iterated line digraph | (prev, cur) → (cur, next) | *Merged* already recovers the de Bruijn shift (the section before Part III); interior version run (L6) |
| graph colouring | Tait: the four-colour theorem is equivalent to 3-edge-colouring planar cubic graphs; Grünbaum colourings of triangulations | "resolving the interior costs 3" is a proper 3-colouring of a medial graph | recalled; a 3-colouring of the medial graph of a triangulated sphere is such a colouring, so the floor 3 would hold for every spherical core. **Not run beyond the octahedron.** Whether a *reader* attains it is a separate question (D6) |
| software | interface vs implementation; left action = what a refactor may change without changing behaviour, right action = the methods | reader vs method | an idiom for §2, not a claim |

---

## 8. Queued tests

Written with predictions so they can fail. `dig.py` holds D1–D5; it was written and could not
be executed before this version was saved.

| id | source in the corpus | prediction |
|---|---|---|
| D1 | *Merged* §4, memory layer | On the interior: 64 first-order rule-books, 4096 second-order. Under the A₄ reader no first-order rule is equivariant; exactly two second-order rules are (T₊, T₋), both bijective. Under full G, none of either. |
| D2 | *What a Cut Must Do*, four clauses | Over the 26 readers, the order-8 reader is the coarsest passing clauses 2–4, and on its quotient T₊ and T₋ become one tick of period 3. |
| D3 | *Merged* Parts IX, X; *Combined* ladder | z, T₋T₊⁻¹ and [T₊, T₋] are the three involutions of one Klein group, all fixed-point-free; its orbits are the clock classes; the reader's involutions generate exactly the clock's kernel. |
| D4 | `the-clock-mod-d.md`, period 9 at the trivial reader | 9 = 3 × the forward interior value — the same ratio as 22587 = 3 × 7529. If the trivial-reader harmonic space is not 1-dimensional the question is ill-posed and that is the finding. |
| D5 | omitted-cycle doc, 20 rotation + 180 spectator triangles | A table of which triangle types carry the period. No prediction. |
| D6 | Tait / Grünbaum | Medial graphs of the tetrahedron and icosahedron are 3-chromatic. For the tetrahedron the floor is attained by a reader (the Klein group, three classes of two). For the icosahedron: no prediction. |
| D7 | *Merged* §4 | Transfer the binary-ring experiment itself: paired-state bijectivity, no pastless states, no transients, on the arena rather than the interior. |
| D8 | L6's scope | Under the full octahedral group edges are swapped and `orient` does not exist. What replaces it? |

---

## 9. The standing four, located

| item | where it stands | nearest law |
|---|---|---|
| 1. how the transformation is done, not the values | addressing criterion; alignment buys cost, not possibility | L20 |
| 2. shapes are methods | literal on the interior: shape = Cayley graph of the methods, faces = their relations | L7 |
| 3. read the missing methods without searching | one character answers every reader channel; below the cutoff the rank deficit counts the missing relations | L10, the observation under §4 |
| 4. something real | rational side of the relation-gap shape is closed (15, attained); the integral side now has one concrete datum, a character of order 3 that exists mod d and not over ℚ | L12, L9 |

---

## 10. Test index

All exact arithmetic; no randomness except one seeded cochain in `recheck.py`.

| script | asserts | timed |
|---|---|---|
| `blind.py` | blind set: 14 cells, span 13, isotypic type | not timed |
| `nest.py` | blind set under all 26 readers; monotone; all internal edges in one orbit | not timed |
| `interior.py` | interior ≅ cuboctahedron, explicit isomorphism | not timed |
| `sphere2.py` | fundamental class carries 1⁻; z is the antipodal map | not timed |
| `color.py` | chromatic number 3, attained at order 8 | not timed |
| `recheck.py` | the §57 audit: C1–C5 | 9.0 s |
| `why.py` | orbit table, orbital menu, 2 of 31 close | 0.2 s |
| `medial.py` | interior = medial(core) as sets; three controls | 0.06 s |
| `cutoff.py` | closure at L = d; rank saturation; bipyramid boundary case | 0.19 s |
| `bind.py` | orientation, methods, residue, clock (L6–L9) | 0.35 s |
| `dig.py` | D1–D5 | **not yet run** |

The scripts live in a session scratch directory with a shared library. They are not archived
anywhere durable. That is the largest practical risk in this manual: every `run` above is
reproducible in principle and stored nowhere.
