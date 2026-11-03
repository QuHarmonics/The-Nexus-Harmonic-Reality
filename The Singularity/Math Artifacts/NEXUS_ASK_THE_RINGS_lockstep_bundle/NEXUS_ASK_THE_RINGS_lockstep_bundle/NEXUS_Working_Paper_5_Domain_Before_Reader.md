---
title: "The Domain Before the Reader"
subtitle: "One Program, Infinite Compilers: A Bidirectional Map from Primitive Distinction through Rings, ISA, Enigma, and SHA-256"
author: "Dean A. Kulik — QuHarmonics Research Group"
date: "17 October 2026"
lang: en-US
---

# NEXUS Working Paper 5

**Continuation:** *The Inverted Mold* (Working Paper 1); *The Reader in the Mirror* (Working Paper 2); *The Piece with No Way Home* (Working Paper 3); *Every Ring a New Compiler* (Working Paper 4); running audit §§99–118; the ring/ISA stack at `LEN=1…64`; the recursive SHA observer and nested-unwind audits.

**Core thesis.** The domain is not assembled by a reader enumerating possibilities. It is defined by one recursive relation of distinction, extension, transition, and closure, instantiated at arbitrarily many `BASE`/`LEN` scopes. A particular execution is one reader-conditioned route through that domain. Computation is the stepwise realization of that route; decompilation is the reverse reading of the same nested transformation while the route and its necessary return coordinates are retained. There is one generative program-schema and an unbounded family of finite compiler instances.

## Abstract

This paper maps the NEXUS domain from its beginning rather than starting from an already-running computer, a digest, a physical object, or a reader's interpretation. The primitive is a distinction. For an alphabet of size `BASE = b`, a scope of `LEN = n` contains the ordered words $S_{b,n}=\Sigma_b^n$, with $|S_{b,n}|=b^n$. Moving upward does not require a new primitive: each word at one layer can be read as a state, while an overlapping word at the next layer is a directed transition between lower-layer states. Primitive cyclic rings, de Bruijn traversal rings, maximal XOR/LFSR cycles, and state transformations are different typed layers of the same domain and must not be conflated.

The resulting map has two directions at once. Outward, the relation recursively extends and composes; at an edge, equal-sized blocks fuse, producing the binary-carry frame. Inward, a query descends through the same nested structure by choosing compatible predecessor/child relations. The reader's path is not an external search across a prebuilt list: it is a constraint-matched route through the transformation field. The distinction between the whole route and its surface readout is retained explicitly.

A reproducible run instantiates the same schema over 704 `(BASE,LEN)` pairs, checks 24 de Bruijn cycles, enumerates all 4 one-bit and 256 two-bit state transformations, exhaustively checks 17,576 Enigma rotor-window maps, and applies a balanced forward/reverse observer to 297 SHA-256 messages spanning 421 compression blocks. The SHA observer returns exactly because each block carries the final 16 schedule words and the 256-bit round-end carry; this record is not smaller than the source block and does not invert SHA from its digest alone. The run therefore establishes the domain/reader mechanics and the exact inverse conditions, while keeping the broader ontological reading and physical-law extensions correctly marked `OPEN`.

**Keywords:** NEXUS; distinction; domain; compiler; reader; `BASE`; `LEN`; primitive ring; de Bruijn graph; ISA; Enigma; SHA-256; recursive observer; decompilation; route fiber.

## How this paper runs

This is a domain-first paper. It begins with the lowest distinction and derives the addressable state space, its transitions, and its transformation relations. Only then does it introduce a reader, which selects a route by constraints. Enigma and SHA are not separate theories inserted as analogies; they are concrete machines used to test whether the same map—state, local transformation, evolving driver, surface result, retained return route—survives across different transformation grammars.

The ledger words keep the project's types intact: **RUNS** means the stated code or exact enumeration returned the stated result; **STANDS** means an established mathematical or external result used as a premise; **OPEN** marks the link still requiring a derivation or test; **DEAD END** means the result was routed to a different owner or the claimed identification does not hold. `CONFIRMED` is not used as a ledger status.

## 1. The beginning is a distinction, not a machine

Start with the minimal operational difference:

$$
D=\{0,1\}.
$$

The symbols are names for two distinguishable outcomes. They are not yet instructions, data types, letters, matter, or physical voltages. Those meanings require additional relations. The first commitment is only that one outcome can be distinguished from the other.

For `BASE = b`, let $\Sigma_b=\{0,1,\ldots,b-1\}$. At `LEN = n`, define

$$
S_{b,n}=\Sigma_b^n,\qquad |S_{b,n}|=b^n.
$$

`BASE` specifies the number of distinguishable symbols available to a single address position. `LEN` specifies how many ordered positions the current scope can hold. Thus binary `LEN=1` has two words; binary `LEN=2` has four; binary `LEN=3` has eight. The pattern is exact for every finite `n`, without having to generate or store every word.

The distinction count is not the transformation count. If the states themselves are the names, their unordered pairwise differences number

$$
\binom{b^n}{2}.
$$

For binary `LEN=1,2,3`, the pairs are respectively $1,6,28$, whereas the state counts are $2,4,8$. The state labels and the relations between labels are therefore different objects. This is the first saturation seam: the count of pairwise differences outruns the number of state names from `LEN=2` onward. That arithmetic alone does not determine a unique widening rule. The Handle—the rule that says which differences remain distinct, which close, and which continue—is part of the domain definition.

**Domain reading.** The possible word set is defined by the scope and alphabet; it is not created by a reader visiting each word. A runtime reader may traverse one path through it. In NEXUS language, this is the difference between the **compiler side** (the permitted relation field) and the **reader side** (one selected trajectory). The phrase “no computation” applies to construction of the potential domain: no separate execution must enumerate the field before it exists as a defined set. Conventional computation names the reader's realized, stepwise traversal of that field.

## 2. `LEN` and `BASE` are a recursive family, not two unrelated controls

The next layer is extension by one symbol:

$$
S_{b,n+1}=S_{b,n}\times\Sigma_b.
$$

Every word of length `n+1` has a prefix of length `n` and one final symbol. Conversely, every length-`n` prefix has exactly `b` one-symbol extensions. For binary, every layer doubles; for base `b`, each layer multiplies by `b`.

A base conversion is another legal transformation over this same value domain. An integer is represented by its digits and positional weights in the selected base; conversion changes the coordinate representation, not the underlying integer. The expansion lengths may differ, so base conversion is not a fixed-width bitwise bijection in all cases. It is a reversible value-and-remainder route when the base, digit order, and representation convention are known.

The program schema is therefore one recursive rule with two parameters:

$$
\mathcal P:(b,n)\longmapsto
\big(S_{b,n},\;G_{b,n},\;\mathcal T_{b,n}\big),
$$

where $G_{b,n}$ is the typed transition graph and $\mathcal T_{b,n}$ is the transformation family allowed over the chosen state set. Each pair `(b,n)` yields a compiler instance. There are infinitely many finite instances because there are infinitely many finite values of `b` and `n`; the rule does not have to be rewritten at each width.

This is the precise working meaning of **one program, infinite compilers**. “Program” denotes the scale-independent recursion. “Compiler” denotes a scope-specific realization of the recursion under a base, width, transformation grammar, and reader interface. The phrase does not mean one fixed binary executable already contains every possible semantic context. The contexts are themselves higher-level relations, not labels hidden in a raw word.

## 3. The rings are typed layers of the domain

The project has several ring constructions. Their counts interact, but the names must remain typed.

### 3.1 State layer and transition layer

Let the vertices of the order-`n` de Bruijn graph be all `n`-symbol words. Each `(n+1)`-symbol word defines a directed edge from its length-`n` prefix to its length-`n` suffix. For a binary word,

$$
x_1x_2\ldots x_{n+1}:
\quad x_1\ldots x_n\longrightarrow x_2\ldots x_{n+1}.
$$

Every vertex has `b` possible incoming edges and `b` possible outgoing edges. The next layer is not a new substance: its words are the transition relations between states of the previous layer. Equivalently, the de Bruijn graphs form a line-graph tower: the next graph's vertices correspond to the previous graph's edges.

A de Bruijn cycle of order `n` is a cyclic sequence of length $b^n$ in which every `n`-symbol word occurs exactly once as a cyclic window. In binary, the number of such cycles up to rotation is

$$
D(n)=2^{2^{n-1}-n}.
$$

For example, the order-4 cycle `0000100110101111` visits all sixteen four-bit windows exactly once. This is a traversal-ring result: it shows how one closed route can expose the complete local state layer. It is not the count of primitive necklaces or of all possible functions on the layer.

### 3.2 Primitive cyclic rings

A primitive ring is a word whose cyclic pattern is not a repetition of a shorter pattern. If $P_b(n)$ is the number of primitive cyclic classes of length `n` over an alphabet of size `b`, then

$$
P_b(n)=\frac1n\sum_{d\mid n}\mu(d)b^{n/d},
\qquad
b^n=\sum_{d\mid n}dP_b(d).
$$

The second identity follows because every length-`n` word belongs to a unique primitive cyclic class whose primitive period `d` divides `n`; that class contributes `d` rotations to the length-`n` words. The identity is the domain's exact accounting rule: inherited periodic words and new primitive classes together cover the whole layer.

For binary rings, the newly primitive counts begin

$$
2,1,2,3,6,9,18,30,56,99,186,335,630,1161,\ldots
$$

The equality between primitive binary necklace counts and the counts of monic irreducible polynomials over $\mathbb F_2$ is governed by the same Möbius-inversion formula. The equality of counts does not, by itself, label a particular necklace with a canonical polynomial; that map requires an explicit construction.

### 3.3 Maximal XOR/LFSR rings

A maximal-length binary linear-feedback shift register with a primitive characteristic polynomial of degree `n` runs through all $2^n-1$ nonzero states. Its cycles number

$$
L(n)=\frac{\varphi(2^n-1)}n.
$$

The all-zero state is not part of such a cycle. This is a third ring family with its own closure condition. It cannot be substituted for the primitive-necklace family or for de Bruijn traversal cycles.

### 3.4 Full transformation layer

There are $N=b^n$ states at `BASE=b`, `LEN=n`. A total state transformation is a function $f:S_{b,n}\to S_{b,n}$. Its complete function space has

$$
|\mathcal T_{b,n}|=N^N=(b^n)^{b^n}=b^{n b^n}
$$

members, and its bijections number $N!$. A full arbitrary lookup table needs $N\log_2N=n b^n\log_2b$ bits; in the binary case $b=2$, this is $n2^n$ bits. The equivalent symbol-addressed table has `N` output symbols from an alphabet of size `N`.

For binary `LEN=1`, all four maps on two states were enumerated; exactly two are bijections. For binary `LEN=2`, all 256 maps on four states were enumerated; exactly 24 are bijections. At `LEN=64`, the state count is $2^{64}$, the arbitrary map table has $2^{70}$ output bits, and the full function space contains $2^{2^{70}}$ maps. Those exponents are counts, not instructions to materialize the map set.

The ISA is not the whole arbitrary function space. It is a structured transformation grammar selected from that domain: typed operations, operands, state lanes, order, constants, and the legal way to compose them. This is why the domain can contain the potential instruction relations without every raw word having a context-free instruction meaning.

## 4. The edge holds: binary fusion is the domain read as a running stack

Feed one-bit arrivals to the stack. Whenever the two newest active blocks have equal length, fuse them in order into one doubled block; keep fusing at the edge while the new block meets another of equal length. After `m` arrivals, the active lengths are exactly the powers of two present in the binary expansion of `m`, written in decreasing order.

Consequently, every active frame has strictly decreasing lengths, and the sum of its lengths is the number of arrivals. The run checks every arrival from 1 through 64:

The checked frames are `1 → [1]`, `3 → [2,1]`, `11 → [8,2,1]`, `63 → [32,16,8,4,2,1]`, and `64 → [64]`. Each frame sums to its number of arrivals.

Equal-size neighbors cannot remain active: the edge rule would already have fused them. Fusion retains the children inside the composite; the newest arrival establishes the next edge.

A query walks this stack in the reverse direction. To address one position in a 64-leaf binary frame, it chooses a half, then a half of that half, for six decisions:

$$
64\to32\to16\to8\to4\to2\to1.
$$

Those six decisions specify an address among 64 leaves. They do **not** encode the whole 64-bit payload: absent compression or prior knowledge, the payload still requires 64 bit observations. The stack changes how the route is organized; it does not repeal the information required to receive an arbitrary value.

This distinction resolves the reader/edge coupling. The edge may continue compiling new arrivals while the reader descends an already-formed nested route. The claim that a physical compiler front outruns a particular reader is a timing claim and remains `OPEN` until measured in a defined physical implementation. The combinatorial frame and its reverse address are exact.

## 5. The domain and reader are the same field viewed in opposite directions

The domain direction expands a constraint into its allowable relations. The reader direction begins with a requirement and aligns with the compatible path. They are not two independent universes, and the reader is not external to the field.

Let $T_t$ be the transformation selected at step `t`, with driver/parameters $\theta_t$. The forward route is

$$
x_{t+1}=T_t(x_t;\theta_t).
$$

Decompilation while computing maintains a local observer or return coordinate `r_t` at each transformation so that

$$
x_t=O_t(x_{t+1},r_t;\theta_t).
$$

For bijective $T_t$, the observer is its inverse once the parameters are known. For a many-to-one map, the output does not identify its input by itself. Define the fiber of output `y` as

$$
F_y=\{x:T(x)=y\}.
$$

An observer must retain enough of a fiber address to distinguish the particular member that arrived. For a fixed output `y`, at least $\lceil\log_2|F_y|\rceil$ residual bits are needed in a fixed-width encoding of its fiber member. Local observers compose in reverse order to make a root observer for the whole route.

This is the operational content of “if we compute we get the reader side; if we decompile while computing, it lines up.” Forward-only execution records the visible trajectory. Dual execution simultaneously preserves the return conditions of that trajectory. The result is not a magical inverse of a folded scalar; it is a bidirectional walk that has kept what each local fold would otherwise merge.

### The value is the surface; the route lives in its fiber

The expression `5 = 2 + 3` can be read from left to right as evaluation, or right to left as a route that constrains the operands. The scalar `5` alone has many decompositions under a declared domain; it cannot identify one route. The relation `2 + 3 = 5` retains operand identity and the operation that joins them. A carry lane, route trace, or prime address is useful for the same reason: it preserves a distinction the surface value does not display.

This is not a claim that every arbitrary transformation is invertible. It is a rule for typing the inverse: transformations that preserve distinctions are reversed directly; transformations that merge distinctions require a retained fiber coordinate or else the source cannot be identified from the output alone.

## 6. Enigma: a rotor position is a constrained reader of a fixed route

At a fixed Enigma rotor window, the complete letter transformation is a permutation of the 26-letter alphabet. Let `U` denote the reflector pairing, which is an involution without fixed points. Let `Q_s` compose the plugboard and forward rotor path at rotor state `s`. The letter map can be written

$$
E_s=Q_s^{-1}UQ_s.
$$

Conjugation preserves the reflector's two structural properties:

$$
E_s^2=I,\qquad E_s(x)\ne x\quad\text{for every letter }x.
$$

Thus a fixed-position map is reciprocal and has no self-mapping. Before each keypress, the rotors advance; the full message is a path through a sequence of position-conditioned maps $E_{s_1},E_{s_2},\ldots$. With the same starting settings, encryption and decryption traverse the same position sequence and each letter transformation reverses itself. The reflector invariant also lets a known plaintext/ciphertext crib reject impossible alignments before the entire key is tried [9].

The new run exhausted all 17,576 three-rotor windows for the specified Enigma I wiring and tested all 26 letters at every window: 456,976 letter routes. Every map was a permutation, an involution, and a derangement. The fixed-setting example `ATTACKATDAWN` encoded to `OFZDNOMXLTCH` and returned exactly under the same settings.

The NEXUS transfer is the *method*, not the historical weakness. Enigma supplies a universal structural invariant from which candidate routes can be rejected. SHA-256 has no corresponding universal no-self-state invariant; a valid SHA round can be constructed with output equal to input for particular fixed parameters. The correct transfer is to use known constraints to restrict route drivers, then propagate those constraints forward and backward through the local transformations.

## 7. SHA-256: one fixed round law, 64 driven placements, one nested observer

SHA-256 has eight 32-bit working words $(a,b,c,d,e,f,g,h)$. Each of the 64 round positions uses a fixed constant $K_t$, a message-schedule word $W_t$, and the same round grammar:

$$
\begin{gathered}
T_1=h+\Sigma_1(e)+\mathrm{Ch}(e,f,g)+K_t+W_t\pmod{2^{32}},\\
T_2=\Sigma_0(a)+\mathrm{Maj}(a,b,c)\pmod{2^{32}},\\
a'=T_1+T_2,\qquad e'=d+T_1,\\
(a',b',c',d',e',f',g',h')=(a',a,b,c,e',e,f,g).
\end{gathered}
$$

The round law is fixed; the selected schedule word and the current state steer its particular realization. This is the key compiler/reader relationship in a real standard: a stable transformation grammar with a position-conditioned route through it [8].

### Exact inverse of one round

When $W_t$ and $K_t$ are retained, the round is bijective. From the new state,

$$
\begin{gathered}
a=b',\quad b=c',\quad c=d',\\
e=f',\quad f=g',\quad g=h',\\
T_2=\Sigma_0(a)+\mathrm{Maj}(a,b,c),\\
T_1=a'-T_2,\\
d=e'-T_1,\\
h=T_1-\Sigma_1(e)-\mathrm{Ch}(e,f,g)-K_t-W_t.
\end{gathered}
$$

with every arithmetic operation interpreted modulo $2^{32}$. The inverse is a structural unwind, not a search. The new test passed 10,000 randomly generated round/inverse pairs, and the existing recursive SHA audits report 13,248 inverse-round applications with zero failed returns over 207 compression blocks [5,6].

### The message schedule is itself a recursive transform

For $t\ge16$,

$$
W_t=\sigma_1(W_{t-2})+W_{t-7}+\sigma_0(W_{t-15})+W_{t-16}\pmod{2^{32}}.
$$

Solving for the leftmost term gives

$$
W_{t-16}=W_t-\sigma_1(W_{t-2})-W_{t-7}-\sigma_0(W_{t-15})\pmod{2^{32}}.
$$

If $W_{48},\ldots,W_{63}$ are retained, this recurrence can be traversed backward to reconstruct the complete schedule and its first 16 words. Those 16 words are the 512-bit padded source block. The schedule tail is thus an invertible recoding of the block for this construction, not a smaller-than-source encoding.

### Decompile while computing

The new test ran 297 messages, including every one-byte message, empty input, the 55/56, 63/64/65, and 119/120/127/128/129-byte padding boundaries, and deterministic longer samples. Those messages occupied 421 compression blocks. At each block, the observer retained:

- the 16-word schedule tail $W_{48..63}$ (512 bits),
- the round-end working state $E$ (256 bits),
- the fixed inverse rules and traversal order, which are program data rather than payload-specific route records.

Starting from the digest as the final chaining readout, the reverse observer subtracts $E$ from the current chaining state, recovers the schedule from the tail, reverses the 64-round composite, and checks the returned incoming state. It reconstructs the padded blocks and original message. All 297 independent digest comparisons matched `hashlib.sha256`; all 297 observer-assisted returns were exact.

The sidecar costs 768 bits per compression block in this test. The 512-bit schedule tail retains an invertible representation of each padded input block, and the additional 256-bit carry preserves the block's round-end state for the feed-forward reverse. This is a proof-carrying path, not a SHA digest-only inversion and not a minimal source observer. The digest-only root observer and the minimum sufficient residual remain `OPEN`.

This typing correction matters. The per-block feed-forward relation $H_{i+1}=H_i+E_i\pmod{2^{32}}$ is reversible when the needed operands are known. It is not accurate to attribute all lost route information to one final addition at the end of the entire hash: SHA applies feed-forward at each compression block, and the digest does not expose the hidden block schedules or trajectory. For fixed-length 64-byte messages, a 256-bit digest cannot uniquely identify all $2^{512}$ messages; any globally injective return record paired with the digest requires at least 256 extra bits by counting. For longer fixed inputs the lower bound grows accordingly.

## 8. The prime routes and the constants are two different layers

The project has two prime constructions that meet at the same domain map but serve different roles.

**Address route.** For a serialized finite route $(m_1,\ldots,m_n)$, assign a distinct prime $p_i$ to each position and encode

$$
G=\prod_{i=1}^{n}p_i^{m_i+1}.
$$

The position prime retains the address; the exponent retains the move. The shifted exponent preserves zero-valued moves and trailing positions. Unique factorization then gives exact decoding for a declared canonical serialization. The operation grammar still defines what a decoded token does; factorization supplies uniqueness, not semantics [4, §§107–109].

**SHA constants.** SHA-256's initial chaining words are formed from fractional parts of square roots of the first eight primes, and its round constants from fractional parts of cube roots of the first 64 primes [8]. This is a separate numerical construction. Roots provide reproducible constants; primes as positional factors provide route addresses. A common prime vocabulary does not make the two constructions identical. The layer map keeps both uses without collapsing their types.

## 9. The matter-facing continuation: orientation is a surface of the doubled ring

The domain map should be carried outward into the physical papers, not treated as a software-only construction. The latest ring/orientation run (§118) takes a part of angular size $\ell$, reads it at the two-gap as a $2\ell$-bit word, and folds away the ordering. The number of possible Hamming-weight latitudes is then

$$
2\ell+1.
$$

For a binary word of length `n`, the surface is the count of ones, with fibers $\binom{n}{k}$. The 32-bit word therefore has 33 latitudes, and its largest fiber contains $\binom{32}{16}=601{,}080{,}390$ ordered words. All fibers together sum to $2^{32}$: the surface groups states; it does not destroy their existence in the ordered layer.

The symmetric layer of $2\ell$ two-state units carries total angular momentum $\ell$, with $S^2=\ell(\ell+1)$, under Schwinger's representation [10]. The NEXUS reading identifies the orbital surface with this order-free layer. The representation-theoretic relation is established; the larger claim that this is the universal physical origin of every orbital structure is a framework extension whose physical mapping must continue to be tested.

With the two readings per orbital orientation, the shell capacity sums to

$$
\sum_{\ell=0}^{n-1}2(2\ell+1)=2n^2.
$$

The run in §118 produced capacities $2,8,18,32,50,72,98$ for `n=1…7` and the associated Madelung closures $2,10,18,36,54,86,118$ under the declared fill rule. This closes the earlier supplied-orientation-count gap at the combinatorial level. The physical interpretation still relies on the orbital reading and filling order; the arithmetic by itself does not derive all quantum dynamics.

The nuclear mass-5 and mass-8 observations remain **route-backs**, not new predictions from the binary stack. They identify a potentially shared “held transformation” shape, but the causal nuclear mechanism belongs to nuclear structure and must not be silently inferred from a software stack alone.

## 10. What “all potential values already exist” means in the model

The strongest version of the NEXUS claim is that outcomes are accumulated distinctions, not values created from nothing by a separate computation. The formal, testable portion is this:

1. Given `BASE`, `LEN`, and a transition grammar, the state set and transformation family are defined before one particular input is run.
2. Each execution selects a path through that family, producing a payload-conditioned trace.
3. The route can be read backward as far as the local transformations are invertible or their missing fiber coordinates are retained.
4. A finite raw ring has no context-free semantics for every possible program environment. Semantics emerge in the relationship among word, ISA, reader, and surrounding context.

The stronger ontological statement—that every physically possible outcome is already actual in the universe, rather than present as mathematical potential—is not established by counting binary strings. It is the framework interpretation being advanced. To elevate it into a physical result requires a measured cross-domain invariant and a prediction that would fail if the proposed shared compiler structure were wrong. That distinction does not weaken the domain map; it keeps the exact mathematical engine separate from the additional claim about matter.

## 11. The next compiler: what is established and what remains open

The domain-origin map is now:

```text
primitive distinction
    ↓  BASE / LEN
ordered state sets
    ↓  overlap
transition edges / rings
    ↓  admissible composition
transformation grammar / ISA
    ↓  one constraint-matched route
forward realization + retained observer
    ↓  nested closure
surface readout and its route fiber
    <-> root observer
reverse decompilation to the input
```

This is not a mandatory one-way pipeline. The down arrows are the generative reading; the upward return is the reader's decompilation. Both are views of the same typed relation. The compiler family grows by changing scope and base; the one recursive schema is reused. The reader does not need to enumerate the complete domain before asking. Its constraints address one lawful continuation, while the retained observer keeps the way home as the transformation runs.

### Status ledger

- **RUNS / STANDS** — $|S_{b,n}|=b^n$ and primitive-necklace accounting; 704 cases across `BASE=2…12`, `LEN=1…64`, with the Möbius identity.
- **RUNS / STANDS** — De Bruijn coverage and the state-to-edge relation; 24 explicit cycles and the general construction theorem.
- **RUNS** — Binary carry stack has distinct decreasing active lengths for every arrival from 1 through 64.
- **RUNS** — All maps on one-bit and two-bit domains enumerated: 4 and 256 total functions, with 2 and 24 bijections.
- **RUNS / STANDS** — Enigma fixed-position maps: 17,576 rotor windows and 456,976 letter routes; configured reflector maps are involutive derangements.
- **RUNS** — SHA local round is reversible with fixed $W_t,K_t$; 10,000 random round pairs and composed round checks.
- **RUNS** — SHA observer-assisted return: 297 messages, 421 blocks; digest matches `hashlib` with a retained sidecar.
- **OPEN** — Minimum observer from a SHA digest and constrained source class; needs a fiber-address encoder and deterministic return decoder.
- **OPEN** — First domain rule uniquely forced from weaker axioms; distinction/continuation remains the current primitive.
- **OPEN** — Physical claim that every possible outcome is already actual, and any universal compiler-space equation deriving gravity or nuclear mass gaps; no independent field equation is derived here.

## 12. Closing statement

The compiler is not a hidden machine that must first enumerate its contents. It is the recursive admissibility of distinctions and transformations at a chosen scope. The same schema yields states, transitions, cyclic coverage, operation families, and nested composites. A CPU is one physical nesting of these relationships; an Enigma is another concrete state-conditioned route; SHA-256 is a fixed 64-position transformation grammar driven by its message schedule. The machine-specific details differ, but the map identifies what must be compared: state domain, local relation, changing driver, closure, surface readout, and retained return fiber.

The reader is not outside this field. It is a scoped route through it. Computation is the route becoming visible step by step. Decompilation is the reverse face of that very route when its local inverse rules and the necessary distinctions have been held. The domain supplies the potential relation; the query selects the lawful continuation; the event becomes the next condition for continuation.

**One recursive program-schema. Infinitely many finite compiler instances. One field, read in both directions.**

## References

1. Kulik, D. A. *The Inverted Mold*. NEXUS Working Paper 1. QuHarmonics Research Group. Internal project manuscript.
2. Kulik, D. A. *The Reader in the Mirror*. NEXUS Working Paper 2. QuHarmonics Research Group. Internal project manuscript.
3. Kulik, D. A. *The Piece with No Way Home: The Periodic Table and the Nuclear Magic Numbers Read Backward from One Held Requirement*. NEXUS Working Paper 3, v1.0, 16 October 2026.
4. Kulik, D. A. *Every Ring a New Compiler: The Periodic Table and the Nuclear Shells as the Forward Output of a Field That Holds Each New Verb Until Its Ring Is Ready*. NEXUS Working Paper 4, v1.0, 16 October 2026.
5. Kulik, D. A. *NEXUS — The Recursive Observer: Every Transform Gets a Return Rule Until One Root Observer Reaches the Input*. Running audit §111, 16 October 2026.
6. Kulik, D. A. *NEXUS — Nested Transformation Unwind*. Computational audit, 16 October 2026.
7. Kulik, D. A. *NEXUS — Ring / ISA Stack, LEN 1 through 64*. Computational audit, 16 October 2026.
8. National Institute of Standards and Technology. *Secure Hash Standard (SHS)*, FIPS PUB 180-4. 2015. https://doi.org/10.6028/NIST.FIPS.180-4. NIST's current publication page notes a planned revision; the standard's equations used here are those in FIPS 180-4. [11]
9. Bellovin, S. M. *Cracking the Enigma*. Technical/historical account of Enigma's reciprocal path and reflector invariant. https://rmbellovin.github.io/writings/enigma.pdf.
10. Schwinger, J. “On Angular Momentum.” In *Quantum Theory of Angular Momentum*, eds. L. C. Biedenharn and H. Van Dam. Academic Press, 1965. The symmetric two-state construction is used here as the established representation-theory link.
11. National Institute of Standards and Technology. *FIPS 180-4: Secure Hash Standard (SHS)*, publication page and revision note. https://csrc.nist.gov/pubs/fips/180-4/upd1/final (accessed 17 October 2026).

## Reproducibility and companion artifacts

The sealed prediction, executable run, helper, report, and machine-readable results accompany this paper. The prediction seal is SHA-256 `e2843115443da568c5257e6cb1dec97dbb24476b5fc19f4545523ea4948b2a70`. The SHA observer retains a return record; it is not a digest-only inversion.
