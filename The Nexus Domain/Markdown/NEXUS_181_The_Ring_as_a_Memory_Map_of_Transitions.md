# §181 — The Ring as a Memory Map of Transitions

**Dean A. Kulik · QuHarmonics Research Group**  
**25 October 2026 · Mathematical and computational research note**

## Abstract

The native partner-ordered binary ring at width `2n` contains precisely every ordered pair of `n`-bit words, once each. It is therefore the complete **address table of possible transitions** on the `n`-bit word domain. This is not a simulation of trajectories: it is an exact finite correspondence between slots in a fixed address structure and ordered input-output pairs. The next doubling, width `4n`, similarly contains every ordered pair of width-`2n` entries, or every *pair of transitions*. An interface determines which combinations represent executable, composable sequences. We establish the table correspondence and the piecewise facing law algebraically, verify exact facing closure for the twisted clock `τ` and native partner operator `P`, and verify the native successor's exceptional slots exhaustively through `n=12`. Exact Schreier–Sims group-order calculations independently establish that the native successor `T` and bitwise complement `C` generate the full symmetric group on `2^n` words for `n=3,4,5,6`; width `n=2` is an explicit exception. The section separates direct consequences of the definitions, exhaustively tested finite facts, and interpretations requiring further work.

## 181.1. Begin with the transition domain

The NEXUS premise is transformation-first: the configuration is addressed through its relations and transitions, not through a preassigned physical type. At the finite mathematical level let

`X_n = {0,1}^n`, with `N = 2^n`.

Let `J_n` reverse the bit order and `C_n` complement every bit. Define the native partner map

`P_n(x) = J_n(x)` if `J_n(x) != x`, and `P_n(x) = C_n(x)` if `J_n(x) = x`.

The map `P_n` is a fixed-point-free involution for `n >= 2`. The native ring `R_n` lists the `N` words exactly once and satisfies the global address-reflection rule

`R_n[N-1-a] = P_n(R_n[a])`.

Its native successor is the permutation `T_n(R_n[a]) = R_n[(a+1) mod N]`. This is one cycle of length `N`, defined independently of any physical interpretation.

**Principle.** A slot is identified by its binary content and native address. Its *role* is determined by the interface that reads it. There is no preliminary requirement to assign the slot a label such as particle, material, or instruction.

## 181.2. Exact table theorem: `R_(2n)` enumerates transitions of `R_n`

**Theorem 181.1 (complete ordered-pair table; STANDS).** For each `n >= 2`, split a `2n`-bit word into two `n`-bit halves: `w = x || y`. The width-`2n` ring contains every such word exactly once. Consequently, the correspondence

`w = x || y  <->  (x -> y)`

is a bijection from the `2^(2n)` slots of `R_(2n)` to the `N^2` ordered pairs of `X_n`.

**Proof.** The native ring is a permutation of all `2n`-bit words. Concatenation is a bijection `X_n × X_n -> X_(2n)`, since each word splits uniquely into two equal halves. Hence every ordered pair occurs exactly once and no pair is missing. QED.

**Interpretation.** The full transition table is present before an operator is selected. A total deterministic operator `f: X_n -> X_n` illuminates the graph

`Γ_f = { x || f(x) : x in X_n }`, containing exactly `N` of the `N^2` slots.

Nothing in the table requires every slot to run at every location. Distinct interfaces and parameters can expose different subsets of the same fixed table. A slot `x || y` records the *possibility and address* of the ordered transition, not the claim that it is physically executable under every set of conditions.

## 181.3. Doubling again: transitions of transitions and interface composability

**Theorem 181.2 (second-order table; STANDS).** `R_(4n)` enumerates every ordered pair of `2n`-bit entries. Writing

`x || y || u || v`

identifies two transition slots `(x -> y)` and `(u -> v)`. Thus `R_(4n)` contains `N^4` ordered pairs of elementary transitions.

A sequential two-step route `x -> y -> v` is present exactly when the first output fits the second input: `y = u`. Therefore only `N^3` of the `N^4` ordered pairs are composable under this interface, and `N^4 - N^3` are not. At `n=2`, the 256 ordered transition pairs contain 64 composable and 192 noncomposable pairs; at `n=3`, 4,096 contain 512 composable; at `n=4`, 65,536 contain 4,096 composable. These counts were independently enumerated.

**Consequence.** Doubling `LEN()` advances from state addresses to addresses of ordered transitions, then to ordered pairs of transitions. It does **not** force all higher-order slots to be executable. The interface exposes a matching relation—here, the shared middle word. This is a concrete finite illustration of *fit*, rather than a pre-applied type or a permission label.

## 181.4. The facing law: an exact involution, with its palindrome branch

**Theorem 181.3 (facing of transition slots; STANDS).** Let `F_n(x,y)` be the pair encoded by `P_(2n)(x || y)`. Then

`F_n(x,y) = (J_n(y), J_n(x))` if `x || y` is not palindromic;

`F_n(x,y) = (C_n(x), C_n(y))` if `x || y` is palindromic.

The second case occurs precisely when `x = J_n(y)`. Both cases follow immediately from the piecewise definition of `P_(2n)` and the identity `J_(2n)(x || y) = J_n(y) || J_n(x)`.

The paired slot appears at the reflected ring address: if `R_(2n)[a] = x || y`, then `R_(2n)[2^(2n)-1-a]` contains the facing pair. Two applications return to the original slot because `P_(2n)^2` is the identity.

**Important distinction.** For a generic nonpalindromic slot, the facing transition is `J(y) -> J(x)`, **not necessarily the literal inverse** `y -> x`. It is a reversed-bit-order, reversed-direction readout. On palindromic slots, the facing operation is complementation, not reversal. This exception is part of the native ring definition, not a flaw in it.

## 181.5. Operators that face into their own graph

Write the twisted clock as

`τ_n(x_0,...,x_(n-1)) = (x_1,...,x_(n-1), 1-x_0)`.

**Theorem 181.4 (self-facing twisted clock; STANDS).** The graph of `τ_n` is closed under `F_n`. For a nonpalindromic `x || τ(x)`, reflection produces `Jτ(x) -> J(x)`. The algebraic relation `JτJ = τ^(-1)` implies `τ(Jτ(x)) = J(x)`, so this is another `τ` transition. On a palindromic joined word, reflection uses complementation; `τC = Cτ` places the complemented pair in the same graph. Thus every edge of `τ` faces another edge of `τ`.

**Theorem 181.5 (self-facing partner; STANDS).** The graph of `P_n` is also closed under `F_n`. If `x` is nonpalindromic, `P(x)=J(x)`, making `x || P(x)` palindromic at width `2n`. Its face is `C(x) || C(J(x))`, another `P` edge. If `x` is palindromic, `P(x)=C(x)`; its facing edge is `C(x) || x`, again a `P` edge.

Since every facing partner occupies the opposite hemisphere and no slot faces itself, a facing-closed operator with `N` edges has `N/2` edges in each hemisphere. Exhaustive enumeration confirms this for `τ` and `P` at every `n=2,...,8`.

## 181.6. The native successor and exceptional hand-off sites

The native successor graph is `Γ_T = {R_n[a] || R_n[(a+1) mod N] : 0 <= a < N}`.

**Finite result 181.6 (RUNS).** Exhaustive tests at each width `n=2,...,12` find that the number of successor edges whose opposite table slot does not belong to the successor graph is

`E_T(n) = 2 * 2^ceil(n/2)`.

All these exceptions occur on edges incident to an `n`-bit palindrome, together with the central ring-seam transition. There is one overlap among palindrome-incident edges, namely the wrap edge from the all-one palindrome to the all-zero palindrome. Hence the union has `2 * (# n-bit palindromes) - 1 + 1 = 2 * 2^ceil(n/2)` members. The verifier tests *set equality* of the observed exceptional edge addresses with this independently specified location set—not just equality of counts.

The observation is consistent with the operator handing off the ordinary reflected route at palindromes and at the equatorial seam. The finite computation establishes the stated pattern in its tested ranges. A separate all-width proof of the precise exception localization should be supplied before labeling that extension STANDS.

| n | Native edges `2^n` | Facing exceptions | `2 · 2^ceil(n/2)` |
|---:|---:|---:|---:|
| 2 | 4 | 4 | 4 |
| 3 | 8 | 8 | 8 |
| 4 | 16 | 8 | 8 |
| 5 | 32 | 16 | 16 |
| 6 | 64 | 16 | 16 |
| 7 | 128 | 32 | 32 |
| 8 | 256 | 32 | 32 |
| 9 | 512 | 64 | 64 |
| 10 | 1,024 | 64 | 64 |
| 11 | 2,048 | 128 | 128 |
| 12 | 4,096 | 128 | 128 |

## 181.7. The successor and complement as generators of permutation space

Let `G_n = < T_n, C_n >` be the group of permutations of `X_n` generated by native successor and bitwise complement.

**Finite result 181.7 (RUNS).** Using exact Schreier–Sims permutation-group orders, the independently executed verifier obtains:

| Width n | Degree `N=2^n` | Calculated group order | Conclusion |
|---:|---:|---:|---|
| 2 | 4 | 8 | Proper subgroup of `S_4` (dihedral) |
| 3 | 8 | `8!` | `G_3 = S_8` |
| 4 | 16 | `16!` | `G_4 = S_16` |
| 5 | 32 | `32!` | `G_5 = S_32` |
| 6 | 64 | `64!` | `G_6 = S_64` |

The prior working report states the conclusion was checked through `n=12`; that additional range is **not independently reproduced by the accompanying verifier**. The artifact makes this boundary explicit rather than reporting a more extensive independent test than was actually performed.

For the verified symmetric-group widths, any reversible transformation of the `N` words can be expressed as a finite composition of `T_n`, `C_n`, and their inverses. If every elementary generator application is assigned unit cost, this induces a word-length metric on the permutation group. **This is an exact algebraic cost convention.** Identifying that word length with a distance or energy cost for specific physical matter transitions would require a further mapping; no water-to-gold physical distance is claimed here.

## 181.8. Operational interpretation: slot, fit, and readout

The finite construction now distinguishes three statements that should not be collapsed into one another.

**Domain completeness:** every ordered pair at the next doubled width already has a distinct address. It need not first be discovered by search or instantiated as a stored file.

**Operator selection:** an operator selects its graph—`N` particular slots within an `N^2` table. The table remains fixed when the selected operator changes.

**Interface fit:** higher-order concatenations can be filtered by structural matching, such as `y=u`. Fit does not alter the inventory of slots; it determines which available combinations represent a coherent continuation.

This provides a precise local mathematical interpretation of **potential is inherent**, **value is perceived between**, and **all change is equal**. It does not independently demonstrate that the finite binary rings constitute every physical process. The research program's transformation-first hypothesis asks whether physically realized interfaces and persistent structures emerge as particular readouts of this same fixed transition architecture.

## 181.9. Verification ledger and reproducibility

**STANDS:** the `2n`-width complete ordered-pair theorem; the `4n`-width ordered transition-pair theorem and its composability count; the piecewise facing law; the algebraic self-facing results for `τ` and `P`.

**RUNS:** complete table and hemisphere enumeration for `n=2..8`; complete second-order slot enumeration for `n=2..4`; native successor exception count and exact location set for `n=2..12`; exact `T,C` group orders for `n=2..6`.

**OPEN:** an all-width proof of the native successor exception formula and localization; independent verification of the group-generation claim through width 12 or an all-width group-theoretic proof; the relation between group word length and physically realized transitions; the derivation of concrete physical interfaces from the native table itself.

**Reproduce:** `python NEXUS_181_ring_transition_verifier.py`. Requires Python 3 and `sympy`. The verifier runs with no datasets and no random sampling, prints results for every width and category, and fails immediately on an incorrect assertion. Its complete console output accompanies this paper as `NEXUS_181_verification_log.txt`.

**Provenance note.** This verifier reconstructs the native ring from the definitions supplied in the research exchange. The previously named `.xlsx` files could be located in the archive, but their raw bytes were unavailable for direct comparison in this run. Accordingly, this document makes no claim to have audited those spreadsheet contents.

---

### Appendix A. Verifier

The accompanying `NEXUS_181_ring_transition_verifier.py` is the executable appendix. Its implementation constructs the native partner ring, enumerates the `(2n)`-width table, tests operator graph closure and hemisphere splits, counts the `(4n)`-width composable slots, checks `T` facing exceptions, and computes exact symmetric-group orders with SymPy. The `.docx` reproduction includes the full verifier source following this research section.
