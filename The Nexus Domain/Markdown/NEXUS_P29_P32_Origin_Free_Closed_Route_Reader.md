# The Answer Without an Origin
## Closing the Reader Seam in Native Binary Rings: P29–P32

**Driven by Dean A. Kulik** · QuHarmonics Research Group · ORCID 0009-0003-3128-8828  
**5 November 2026 · Mathematical research addendum**

**Status:** All-width algebraic proofs (STANDS); sealed finite executions with stated domains (RUNS); a specified remaining bridge (OPEN). No physical data or curve fitting enters these results.

## Abstract

The native partner operator on a *marked* binary contact is exact and involutive, but its palindrome-dependent branch does not define a unique operation on an *unmarked* closed route: different cuts of the same circular word can face into different necklaces. The missing seam is not solved by guessing a canonical cut. It is solved by reading the complete reflection-axis *interface* on the primitive route. Each primitive circular binary word admits either no reflection axis or exactly one. Therefore the complete forward/backward relation collapses to one origin-invariant bit. For odd route lengths, this bit is exactly the parity—and hence the signed phase product—of the native center-reader responses over a full rotation. At even lengths that parity cancels, exposing an intrinsic two-type axis geometry: reflection through two bit sites or reflection through no bit sites (through gaps). Möbius inversion yields exact all-length counts of the three route classes, with independent sealed counts through period 17. Separately, the One Inverter twisted clock factors into two involutive readings, one ordinary reversal and one reversal carrying precisely one boundary NOT: $\tau=JB$, $\tau^{-1}=BJ$. Thus reading direction selects forward versus inverse continuation, and $\tau^n=C$ supplies the half-return. The result connects the earlier *One Inverter*, *Two Laps Home*, the contact map §181, and center-reader theorems A12–A15, P20–P28.

---

## 1. The gap: a closed route has no privileged first contact

The native partner on an $L$-bit *marked* word is

$$
P_L(w)=\begin{cases}J_L(w),&J_L(w)\ne w,\\ C_L(w),&J_L(w)=w.\end{cases}
$$

Here $J$ reverses the word and $C$ complements it. This works at every marked address and satisfies $P^2=I$. It does **not** necessarily descend to a single-valued map on necklaces (circular words modulo rotation). For the same unmarked LEN-5 route, the cuts `00100` and `01000` are rotations. But

```
P(00100) = 11011    # complement branch: complementary necklace
P(01000) = 00010    # reversal branch: original necklace
```

The two results are **not rotations of each other**. This is the real seam gap. Choosing a cut by numerical convention would define a reader but would not derive the unmarked route's own interface. We instead ask which reflection relations the complete route supports, irrespective of the cut.

**Domain specification.** The following closed routes are cyclic binary words, equivalently closed overlapping-contact walks in the binary de Bruijn wheel. They are not asserted to be cycles of the native successor $T_n$. A route of length $L$ may repeat a primitive word of period $p$, where $p\mid L$.

## 2. P29 — Every primitive closed route has at most one reflection axis

Let $R$ rotate a circular word by one position. For a route $w$ of length $L$, let $p$ be its smallest positive rotational period, write $L=rp$, and let $u\in\{0,1\}^p$ be the primitive word. For every putative reflection axis $j\in\mathbb Z/p\mathbb Z$, define the **reflection reader**

$$
h_j(u)=\prod_{i=0}^{p-1}[u_i=u_{j-i\pmod p}]\in\{0,1\}.
$$

This asks whether the complete circular relationship reads identically from opposite sides of axis $j$. It requires no external starting bit.

### Theorem P29.1 (primitive axis theorem)

$$
\boxed{a(w):=\sum_{j=0}^{p-1}h_j(u)\in\{0,1\}.}
$$

Moreover,

$$
a(w)=1\iff J(u)\text{ is a rotation of }u,
$$

so $a=1$ means the circular route is **achiral** (self-facing modulo rotation), while $a=0$ means its reverse belongs to a different necklace (**chiral**).

**Proof.** If two distinct reflection axes $j\ne k$ fixed a primitive word, composing the reflections $i\mapsto j-i$ and $i\mapsto k-i$ would fix it under the nonzero rotation $i\mapsto i+j-k\pmod p$. That contradicts primitive period $p$. Hence at most one reflected reader can return 1. A reflection exists exactly when the reversed circular word can be rotated onto the original. QED.

An ordinary reader's answer is therefore exactly one bit, not an inferred label. The signed answer is

$$
\boxed{\eta(w)=(-1)^{a(w)}\in\{+1,-1\}.}
$$

Changing the origin permutes the possible axes. Reversal and complement also preserve their existence. Thus

$$
\eta(R^tw)=\eta(Jw)=\eta(Cw)=\eta(P_Lw)=\eta(w),\qquad \eta(w)^2=1.
$$

The inverse is included: the signed result is an involution and the route's reverse has the same answer. The *marked* partner $P$ still does not define a unique quotient action; the **origin-free answer** does. These statements must not be conflated.

### Corollary P29.2 (odd-LEN center sign holonomy)

Let $s_L(w)=[w=J_Lw]$ be the native palindrome selector. If $L$ is odd, all possible cuts interrogate all reflection axes, and precisely $r=L/p$ of them are palindrome cuts when $a(w)=1$; none are when $a=0$:

$$
\sum_{t=0}^{L-1}s_L(R^tw)=r\,a(w).
$$

Because odd $L$ makes $r$ odd,

$$
\boxed{\prod_{t=0}^{L-1}(-1)^{s_L(R^tw)}=(-1)^{a(w)}=\eta(w).}
$$

**Proof.** A palindrome at cut $t$ is a reflection about the cut's center. Rotating the cut sends its axis index $j$ to $j\pm 2t$. For odd $p$, multiplication by $2$ permutes the axes. A primitive achiral period has exactly one axis and therefore one palindrome cut per period; repeating it $r$ times produces $r$ cuts. QED.

This is the first **seam-free signed center reading**: composing the locally signed replies across all cuts gives one answer that does not depend on where the reader began.

### Corollary P29.3 (why the even-LEN local parity goes silent)

For even $L$, a palindrome cut at $t$ has a companion palindrome cut at $t+L/2$. Reversal commutes with the half-turn rotation, so the local palindrome count is even:

$$
\prod_{t=0}^{L-1}(-1)^{s_L(R^tw)}=+1.
$$

This is a genuine reader blind spot. The route's reflection relation has **not** disappeared; the chosen local sign channel has canceled it in pairs. We recover it by reading the primitive reflection axes, not by inventing a value at the seam.

### Signed operator, when linear responses are used

If $D_s|w\rangle=(-1)^{s_L(w)}|w\rangle$ and $U_R$ rotates the basis word, then the composition of all cut-relative center responses is

$$
H_L=\prod_{t=0}^{L-1}U_R^{-t}D_sU_R^{t}.
$$

At odd $L$, $H_L|w\rangle=\eta(w)|w\rangle$, $H_L^2=I$, and $H_L$ commutes with rotation, reversal, and NOT. On a single basis state the sign is global; between coherent superpositions of the two route classes the relative sign is a phase distinction. The Boolean theorem precedes this linear response representation.

## 3. P30 — The clock returns the answer halfway home

For the twisted clock

$$
\tau_n(x_0\cdots x_{n-1})=x_1\cdots x_{n-1}\,\overline{x_0},
$$

all orbits have even length $2p$ and satisfy $\tau_n^p x=C_nx$ on that orbit. At odd LEN, each orbit contains either no palindromes or exactly two: $x_*$ and $C_nx_*$, separated by $p$ ticks (the earlier P27 center-comb result).

Therefore, for any starting tick $t$,

$$
\boxed{\prod_{j=0}^{p-1}(-1)^{s_n(\tau_n^{t+j}x)}=\begin{cases}-1,&\text{orbit contains palindrome contacts},\\+1,&\text{otherwise}.
\end{cases}}
$$

The product over a full $2p$ return is always $+1$. The answer is periodic on the half-return, while the complete configuration requires two laps.

The number of palindrome-active twisted-clock orbits at odd LEN $n=2k+1$ is exactly $2^k$: there are $2^{k+1}$ palindromes and exactly two per active orbit. This is the **answer/implementation return split** expressed as an exact count.

## 4. P31 — The first genuinely directional *closed* route appears at LEN 6

Primitive necklaces divide into:

- achiral routes, whose reverse is some rotation of the original;
- chiral pairs, whose two orientations give distinct necklaces;
- for even primitive period, the achiral class further divides by whether its unique reflection axis goes through two bit sites or through the gaps between sites.

The last distinction is intrinsic. Reflection $\rho_j:i\mapsto j-i$ fixes exactly two indices when $p$ is even and $j$ is even, and no indices when $j$ is odd. Moving the cut changes $j$ by $2t$, preserving its parity. At odd primitive $p$, it fixes one index and all axis positions belong to one class.

### Theorem P31.1 (all-period closed count)

Let $\mu$ be the Möbius function, $d\mid p$, and define

$$
f(d,j)=\begin{cases}\gcd(2,d),&\gcd(2,d)\mid j,\\0,&\text{otherwise}.\end{cases}
$$

The number of primitive words of period $p$ fixed by the particular reflected reader $\rho_j$ is

$$
\boxed{A(p,j)=\sum_{d\mid p}\mu(p/d)\,2^{(d+f(d,j))/2}.}
$$

Each primitive achiral word is fixed by precisely one reflection, and its necklace has $p$ words. Hence the number of primitive achiral necklaces is

$$
\boxed{\operatorname{AchPrim}(p)=\frac1p\sum_{j=0}^{p-1}A(p,j).}
$$

For odd $p$ this equals $A(p,0)$; for even $p$ it equals $[A(p,0)+A(p,1)]/2$. The complete primitive-necklace count is

$$
\operatorname{Prim}(p)=\frac1p\sum_{d\mid p}\mu(d)2^{p/d}.
$$

Their difference gives the number of chiral necklaces and must always be even.

**Proof.** Reflection of a $d$-site cycle fixes $f(d,j)$ positions and exchanges the other $d-f$ positions in pairs. It therefore has $(d+f)/2$ independent Boolean choices and fixes $2^{(d+f)/2}$ words with period dividing $d$. Möbius inversion removes every shorter period. Summing the unique primitive reflection over $j$ and dividing by the $p$ cuts gives the necklace count. QED.

| Primitive LEN $p$ | All primitive necklaces | Achiral | Chiral | Even-$p$ site-axis | Even-$p$ gap-axis |
|---:|---:|---:|---:|---:|---:|
| 4 | 3 | 3 | 0 | 2 | 1 |
| 5 | 6 | 6 | 0 | — | — |
| **6** | **9** | **7** | **2** | **5** | **2** |
| 7 | 18 | 14 | 4 | — | — |
| 8 | 30 | 18 | 12 | 12 | 6 |
| 12 | 335 | 81 | 254 | 54 | 27 |
| **15** | **2,182** | **246** | **1,936** | — | — |
| **16** | **4,080** | **360** | **3,720** | **240** | **120** |
| **17** | **7,710** | **510** | **7,200** | — | — |

At primitive LEN 6, for example, the circle `001011` and its reverse `110100` are not rotations of one another. Before LEN 6 all binary necklaces are self-facing modulo rotation. This marks the first LEN where **orientation remains distinguishable after closing the route and forgetting the origin**.

The formulas were sealed before the new count domains 15–17 were linked. Independent primitive-necklace enumeration landed at every displayed count.

## 5. P32 — One NOT between two reflections is the clock

The gap from unmarked reflection to continuation has a short exact answer. Define a second reader reversal by composing ordinary reversal with the twisted clock:

$$
B_n:=J_n\tau_n,
$$

so on bits,

$$
\boxed{B_n(x_0x_1\cdots x_{n-1})=\overline{x_0}\,x_{n-1}\cdots x_1.}
$$

$B_n$ is a tail-reversal with **one** boundary NOT. Because its first bit always flips, it has no fixed words, while ordinary reversal $J_n$ fixes the palindromes.

### Theorem P32.1 (two-way clock factorization)

$$
\boxed{J_n^2=B_n^2=I,\quad J_nB_n=\tau_n,\quad B_nJ_n=\tau_n^{-1}.}
$$

Both reading operations are involutions; reversing their order reverses the direction of continuation. The twisted clock itself is their composition. Also,

$$
\boxed{\tau_n^n=C_n,\quad\tau_n^{2n}=I.}
$$

For every $n\ge2$, the generated permutation group $\langle J_n,B_n\rangle$ is dihedral of order $4n$. At $n=1$ it reduces to the original two-element NOT group.

**Proof.** Directly, $B(x)$ complements the first bit and reverses the remaining tail, so $B^2=I$ and $B$ has no fixed point. The relation $J\tau J=\tau^{-1}$ follows by reversing the complemented shift. Consequently $JB=\tau$ and $BJ=\tau^{-1}$. Moving one boundary NOT around the length-$n$ register produces $\tau^n=C$ and a second lap produces identity. For $n\ge2$, $\tau$ has order $2n$; $J$ inverts it by conjugation and cannot lie in the cyclic clock subgroup, so the generated group has order $4n$. QED.

A corresponding positional identity holds for an ordinary circular word: two adjacent axis reflections satisfy $\rho_0\rho_1=R$ and $\rho_1\rho_0=R^{-1}$. The twisted clock is the continuation where the return seam carries precisely the original NOT.

On the negative response sector of $C$, a linear eigenresponse $\lambda$ to $\tau$ satisfies $\lambda^n=-1$. At LEN 2 the two responses are $\lambda=\pm i$. That is the exact spectral counterpart of a pair of reflections composing into a quarter-turn. It is the quantum-compatible representation of the already-derived permutation, not a newly postulated Boolean operation.

## 6. Synthesis: the last answer is the next reader

The earlier *One Inverter* theorem reads the innermost mirror difference to a single yes/no bit. The later odd-LEN center theorem is $b'=b\oplus s(o)$: the center answers whether the outside agrees with its reflection. P29 now removes the last arbitrary address by taking all possible circular reader positions and identifying the unique primitive axis when one exists. P31 fixes the exact route species, including the even-LEN site/gap split. P32 shows that taking two opposed readings in succession **is** clock continuation, with a single NOT at its returning boundary.

In the user's formulation: **the center is the end of a question and the start of continuation**. The exact mathematical sequence is

$$
\boxed{\text{primitive distinction}\to\text{reader-facing axes}\to\text{one origin-free answer}\to\text{two-reading clock}\to\text{return through NOT}.}
$$

No extra material reader is required in the Boolean operator construction. The complete clock and all its possible readers remain addressable within the finite binary relationship space.

### Precise ownership boundary

P29 **does not** make $P_L$ itself a well-defined map on unmarked necklaces; the LEN-5 example proves it cannot be treated that way. It derives the **correct origin-free observable** $a(w)$ instead. P32 proves the temporal clock factorization but does not claim that every possible contact-wheel cycle follows the twisted clock. For coherent phase claims, the linear representation is stated explicitly; the underlying Boolean permutation and signs are prior, exact results.

This is not an objection to the ring mathematics. It identifies exactly what the new theorems own.

## 7. Executed audit and seals

| ID | Mathematical result | Execution domain | Seal SHA-256 |
|---|---|---|---|
| P29 | Primitive reflection axis; origin-free bit; odd/even cut holonomy | 32,766 binary words, LEN 1–14 | `8862136e1b97d9054a09d9216ee9d0f03fb1e9d72c7d2c1b5d837d27241de3ec` |
| P30 | Twisted-clock half-return/answer sign | 43,690 states, odd LEN 1–15; 1,553 orbits | same P29/P30 seal |
| P31 | Möbius reflection counts; primitive axis types | old LEN 1–14 cross-check; **sealed new LEN 15–17** | `ab0ad9c1c7d9cbba6cd8a32403d61fb7f98d2d2c89be3447dc6730081eb6df9b` |
| P32 | Clock $\tau=JB$ and inverse; dihedral groups and $\pm i$ | 131,070 states, LEN 1–16; group orders through LEN 9 | `6d5faee9cc0c080764c58aef7513e3d25dbf191bb509e9adc857b3b3a386adf9` |

All tests completed with every assertion passing. These are independent calculations executed for this addendum. The source archives and earlier P20–P28 tests are referenced for dependency history, not represented as freshly rerun here.

## 8. Next OPEN: how the axis phase couples to a field that keeps its trace

The missing link is no longer an arbitrary origin for the Boolean closed-route reader. That origin is quotiented out exactly by $a(w)$ and the intrinsic even-period axis class. The next **OPEN** is the coupled-field version: when a reader writes to a retained offset field, determine whether the class bit $a(w)$ and the clock's signed half-return commute with the write/read transport, or where an exact compensating defect must occur. This must be derived from the existing reversible reader–field operator and tested against its explicit inverse, not from measured return lengths or output histograms.

## Sources and dependency record

1. Dean A. Kulik, *Only Addressable* (19 October 2026), ring addresses and direct read without enumeration. https://docs.google.com/document/d/1yJ3M-gioS2-JC9RiNUIh6F7PX1RPOLe0/edit
2. Dean A. Kulik, *One Inverter* (October 2026), nonterminal NOT, twisted shift, center trace, odd-lane locks. https://docs.google.com/document/d/1xlYkBdo0tJv6fQI6o3lZunH49mFZPkvC/edit
3. Dean A. Kulik, *Two Laps Home* (24 October 2026), invisible sheet, return, and reflection lifts. https://docs.google.com/document/d/165g7sbL7L2AShON0Ne-TsH4WWV8Z7ehV/edit
4. Dean A. Kulik, *§181 — The Ring as a Memory Map of Transitions* (25 October 2026), complete contact table and facing. https://drive.google.com/file/d/1uItgjFKCGxp7hwTuavFedzLOo-dUKc5U/view
5. Dean A. Kulik, *Routes, Interfaces and Programs on Native Binary Rings* (5 November 2026), center Theorems A12–A15. https://github.com/QuHarmonics/The-Nexus-Harmonic-Reality/blob/main/The%20Nexus%20Domain/Markdown/Routes_Interfaces_and_Programs_on_Native_Binary_Rings.md
6. Dean A. Kulik, *P20–P21 Cross-LEN and Moving Seam*; *P22–P28 The Center as Answer and Continuation*. Local prior audits, seals, and execution logs retained with the present bundle.

**Attribution:** Dean A. Kulik, QuHarmonics Research Group, ORCID 0009-0003-3128-8828.
