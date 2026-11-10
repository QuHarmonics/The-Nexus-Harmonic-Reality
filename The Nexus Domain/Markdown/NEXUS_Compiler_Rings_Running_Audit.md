# Compiler Rings — Consolidated Running Audit

Dean A. Kulik · QuHarmonics Research Group · ORCID 0009-0003-3128-8828
Consolidated 2026-10-21 from the available project record and this conversation.

## Reading the ledger

- STANDS: a theorem or established result is identified.
- RUNS: a specified executable check passed on the stated finite domain.
- SEALED: the pre-run text or code has a recorded byte-level digest.
- DEAD END: a stated route was tested and failed; retain the result and name its owner.
- OPEN: the required link is not yet closed.
- PULL: an interpretation or physical identification, not established by the discrete computation.

Never silently turn a finite check into an all-width theorem, a codec into compression, or a classical identity into a physical law.

### Provenance rule for this consolidated copy

This is one readable log. It is not byte-identical to prior logs or bundles. Entries explicitly marked “conversation-reported” summarize a user-provided run report. Entries marked “independently rerun here” refer to executions performed in this conversation. Referenced `/tmp/...` scripts that were not attached were not independently run. Where original code or seals were absent, that limitation is stated rather than inferred away.

---

## 0. Base held from the ring corpus

The original ring uses the partner map

\[
P_L(x)=\begin{cases}J_L(x),&J_L(x)\ne x,\\C_L(x),&J_L(x)=x,\end{cases}
\]
where `J` reverses bits and `C` complements them. It is a fixed-point-free involution. The ring lists canonical representatives and their partners with a center swap, and satisfies

\[
R_L[2^L-1-i]=P_L(R_L[i]).
\]

The ring is immutable; rank, face, orientation, phase, and reader are coordinates/readouts over it. The second face is reconstructed from one ordered half and the partner rule. These are mathematical properties of the declared construction. STANDS / RUNS in the source corpus.

The partner address is reflection, not a universal angular half-turn. On the declared sphere coordinates it reflects azimuth for every word and reverses latitude on the palindrome branch. It equals the full antipode only at the poles. Earlier loose half-turn/antipode language is corrected here.

---

## 1. One-bit cross-length lift and two-branch completion

For an even-width canonical word `x`, inserting a middle bit gives

\[
I_m(x)=x_{0:h}\,m\,x_{h:L},\qquad m\in\{0,1\}.
\]

The two odd children are distinct and exhaustive. In canonical descending representative coordinates, the clean triangular-block offsets are

\[
j_1=K(K-1)+i,\qquad j_0=K^2+i,
\]
with the extended palindrome-aware block start/size recorded in the position-map entry below.

To reach the next even width, the later audit found the four families

\[
F(x)=\operatorname{canon}(1x1),\quad0x0,\quad0x1,\quad0P_L(x)1.
\]
They partition the next even canonical representative set. Equivalently, from the odd child with middle bit `m`, the `E/G` choices are

\[
E_m(x)=\operatorname{canon}(mxm),\qquad G_m(x)=0P_L^m(x)1.
\]

The middle bit is the value channel; the outer-pair residual is retained separately. Padding is one selected two-step path, not the whole extension law. Palindrome/complement cases are part of the rule.

**Reported and independently checked ranges:** source widths 2–18; target through width 20. The independent audit in this conversation checked 699,048 branch outputs, block offsets, face/center conversion and partner positions. The original `/tmp/r/link.py` files were not present.

---

## 2. Route, canonical rank and physical address

A route code records the width-2 root choice, the successive middle bits, the E/G branch bits, and the final partner side. It has exactly `L` bits for an `L`-bit word. It is a reversible coordinate encoding, not compression.

For canonical representative `a`, let `r_L(a)` be its increasing canonical rank and

\[
q=2^{L-1}-1-r_L(a).
\]

With `M=2^(L-1)`, the center-swapped physical address of the canonical representative is

\[
p_L(q)=\begin{cases}M,&q=0,\\M-1-q,&q>0.\end{cases}
\]

The partner address is `2^L-1-p_L(q)`. Keep representative rank, physical position, center-out depth and face distinct.

The rank formula for all thresholds uses all palindromes and then subtracts the noncanonical ones. If `pi_n(p)` counts all palindromes below `p`, `m=ceil(n/2)` and `T_n(p)=min(pi_n(p),2^(m-1))` counts canonical palindromes, then

\[
r_n(p)=\frac{p-\pi_n(p)+\Delta_n(p)}2+T_n(p).
\]

The tempting extension with `+pi/2` alone is wrong above the first half. Example `n=4,p=1011`: `pi=3`, `T=2`, `Delta=2`; naive rank 8, actual rank 7.

**RUNS:** route/rank/address cross-checks at small widths and scalar wide queries; the full-body audit checked 2,097,148 thresholds and 2,097,148 ring words through width 20, plus scalar queries through width 1,024. Historical seals are reported in prior records; the consolidated file does not claim byte identity with those artifacts.

---

## 3. Literal fold and runtime reflection

For a serialized ring tape `S=A || B`, folding the lower half backward gives

\[
D=A\oplus J(B),\qquad S=A\Vert J(A\oplus D).
\]

For the original small rings:

| Ring | CW tape | Upper half | Reversed lower half | XOR difference |
|---|---|---|---|---|
| R2 | `27` | `2` | `E` | `C` |
| R3 | `056767` | `056` | `E6E` | `E38` |
| R4 | `0123567DBE9AC48F` | `0123567D` | `F123597D` | `F0000F00` |

Palindromic words pair with complements; nonpalindromic words pair with reversals. The fold difference is therefore the observed overlap readout, not a mask inserted beforehand.

In folded runtime coordinates `(depth,face)`, some steps hold depth constant while changing face. Unfolding the retained face restores the original moving successor. Literal fold/unfold round trips passed on R2–R4; individual packet-bit flips changed the reconstruction. Difference alone loses the reference and is not a decoder.

---

## 4. Runtime compiler and grammar

A new reference compiler front end was built in this conversation for the fixed original ring descriptions. Source grammar accepts a literal cycle or a fold packet with root and retained reference halves. It normalizes the fold, validates width, uniqueness, original ordering and center swap, then builds an intermediate representation containing:

- state width and encoding;
- cycle, successor, predecessor and partner tables;
- forward and inverse Boolean algebraic normal forms (ANF).

The target is guarded Python using Boolean XOR and AND, with shared products named once. R2–R4 compilers were checked on all states; all widths 1–8 passed 510 state cases. Literal and folded descriptions produced identical IR and byte-identical targets. Malformed sources/runtime calls were rejected. Width cap 12 is an implementation resource policy, not a mathematical limit.

For R3 the generated forward rule is

\[
(a,b,c)\mapsto(a\oplus b,\ a\oplus b\oplus c\oplus ab,\ 1\oplus b\oplus c\oplus ab).
\]

Its inverse was generated and exhaustively checked. This is an executable compiler demonstration for these declared finite rings, not a universal compiler or physics proof.

---

## 5. Bridge square root, LEN=6 detachment and global rungs

Define `T` as ring successor, `C` complement, `P` partner, `T_C=CTC`, `S=PC T^-1` and `B=T_C T^-1`. The exact algebra gives

\[
PTP=T^{-1},\quad T_C=(PC)T^{-1}(PC),\quad B=S^2.
\]

With `tau` the address reflection, `S=C tau`. At widths 2–5 the alternating Origin-to-Seam walk covers the whole S-cycle. At LEN=6 it occupies 32 of 64 states; the other 32 form a detached component. S cycle lengths are 32,16,16; B cycle lengths are 16,16,8,8,8,8. The ordinary ring successor `T` still forms one 64-cycle and crosses between those S-components.

A global rung matching can be constructed by pairing each B-cycle `A` with its complement image `C(A)`, choosing a phase and transporting it by B. This works even when the cycle length is odd because it pairs two distinct cycles rather than pairing adjacent points inside one odd cycle. One deterministic convention preserves the original origin rung and anchors detached pairs at their least unprocessed state.

**RUNS:** statewise involution and commutation checks through word widths 2–16; LEN=8’s two odd S-cycles of length 27 are paired across cycles. There are phase choices; the convention is explicit, not uniquely forced.

**Corrections:** the LEN=4 prism embeds in Q4 under a Gray relabeling, but is not a subgraph in the original word labels. The differential map `d(x)=(x xor (x>>1))&7` is a vertex quotient, not a cover of the simple Q3 graph; the claimed operator labels P3C3 and P3 fail on the checked examples. All-width Frobenius orthogonality remains OPEN because excluding S two-cycles is still needed.

---

## 6. Sphere coordinates and palindrome carrier

Use radius `n`, latitude `z=wt(x)-n/2`, height `Z=2z`, and azimuth from the physical ring address. The partner reflects azimuth. Nonpalindromes keep latitude; palindromes reverse it. This is a defined combinatorial embedding; identifying it with physical spin remains PULL.

The E/G lift has exact half-step latitude updates. For an even canonical core `x`, middle bit `m` and branch `d`,

\[
z_{odd}=z_x+m-\tfrac12,
\qquad
z_{child}=s\left[z_{odd}+(m-\tfrac12)(-1)^d\right],
\]
where `s=-1` exactly when `x` is palindromic and `m=1`. Finite checks through source width 18 passed 699,048 outputs.

The palindrome address map is `i_n(u)=location_n(B_n(u))`. In half-word coordinates the palindrome carrier latitude has only singleton Walsh components, but its placement in full address coordinates mixes degrees. The transport matrix is an isometric embedding; degree parity is preserved, degree itself can mix.

---

## 7. Comparator, Delta and complete spectrum

Let `J` reverse the word and

\[
c_n(x)=\operatorname{sgn}(J(x)-x),\qquad
\Delta_n(p)=\sum_{x<p}c_n(x).
\]

For `n=2h`, `H=2^h`, `p=AH+B`, and rectangle count `R_h(u,v)=#{b<u:J_h(b)<v}`,

\[
\Delta_n(p)=A(H-A)+B-2R_h(B,A)-[J_h(A)<B].
\]

For `n=2h+1`, `p=(2A+c)H+B`,

\[
\Delta_n(p)=2A(H-A)+c(H-1-2A)+B-2R_h(B,A)-[J_h(A)<B].
\]

The comparator has exactly `2(2^floor(n/2)-1)` nonzero Walsh coefficients with the mirrored-pair sparse support. The full nonzero Delta spectrum follows from the inclusive-prefix kernel. For `s!=0`, let `j=LSB(s)`, `e_k=2^k`, `p=popcount(s)`:

\[
|s|\text{ odd}:\quad \widehat\Delta(s)=-\tfrac12\widehat c(s),
\]

\[
|s|\text{ even}:\quad
\widehat\Delta(s)=-2^{j-1}\widehat c(s\oplus e_j)+\sum_{k<j}2^{k-1}\widehat c(s\oplus e_k).
\]

The zero mode is also closed:

\[
\widehat\Delta(0)=\frac{N^2}{6}(1-4^{-\lfloor n/2\rfloor})-\frac{N\lfloor n/2\rfloor}{4}
=\frac{N(4N-3n-4-(n\bmod2))}{24}.
\]

**RUNS:** all 2,097,148 modes through width 20; wide scalar checks through width 1,024. The word-value comparator spectrum and physical ring-address carrier spectrum remain distinct domains connected only by the rank/address transform.

---

## 8. Seam profile and full interior body

For the exact Walsh-even body `E_n(i)=(z(i)+z(N-1-i))/2`, a clean seam block has a triangular block index `K` and reversal-ordered intra-block label `r`. Its deficit is `wt(K)+wt(r)` (plus the odd-middle correction). This is an exact digital staircase with a logarithmic upper envelope, not a smooth profile. At `n=10,q=64`, the word is `1110000101` and the deficit is five zeros; a blanket two/three-zero claim at raw dyadic offsets is false.

The exact full-block reader uses

\[
S_K=K+[K\ge H/2],\quad D_K=K(K-1)/2+\max(0,K-H/2),
\]
retains the palindrome slot `r=K`, masks that slot to zero in the Walsh-even body, and distinguishes all canonical representatives. The corrected rank uses all palindromes minus noncanonical palindromes, not an uncorrected `+pi` term.

**RUNS:** all 2,097,148 rank thresholds and ring words through width 20; block sums including 1,534 palindrome-containing blocks; scalar word/address queries through width 1,024. The exact Walsh-even closure has adjacent sample jump `1-2/n` under normalized height, so uniform smooth closure is a DEAD END without a separately specified smoothing/readout.

---

## 9. Corrected full-block Walsh and degree-two result

The full-block formula retains `S_K` slots and mask `1[r_i<K]`; this prevents the palindrome gap from shifting later Walsh phases. The corrected formula reproduces the direct even-body transform exactly.

Measured degree-two energy share of full latitude: 53.125% at `n=6`, 46.7403% at `n=12`, and 32.7503% at `n=20`. Relative to even-body energy the `n=12` and `n=20` shares are 48.2481% and 32.8144%. Degree two is the largest full-energy degree bin for widths 4–20, but is not a majority at n=12 or n=20.

The full degree-two bin is the sum of center-out degree-one and degree-two bins after face-pairing. Therefore the finite concentration passes, while a unique quadratic-phase or quantum explanation remains unproved. The exact square-root digit identity in the supplied draft fails at `L=4,u=49/128`: actual R4 bit is 0; the claimed tau bit is 1. The displayed D=13..96 certificate passes all 28 cases in residue classes 0 and 1, but only 6/28 in class 2.

---

## 10. Running compiler audit continuation

The executable finite runtime audit, compiler grammar, IR, generated R3 rules, edge cases and one-bit ladder results are recorded in earlier append entries in this same file where available. Important distinction: a compiler must preserve operational semantics, not merely output a ring word. The R2–R4 reference compiler passed exhaustive finite states, but its width cap is an implementation resource limit and it is not a universal compiler theorem.

---

## 11. Readiness-first experiment

For the fixed flattened R2 orbit `00100111`, paired-difference blocks close immediately when both equal-width inputs are present: 2-bit units close at arrivals 2,4,6,8; 4-bit units at 4,8; the 8-bit unit at 8. A 64-arrival stream's first 8-bit unit still closes at arrival 8.

For all 65,536 operand pairs of 8-bit addition, each output bit was released at its first event where every completion of the unseen inputs agreed. LSB-first, MSB-first and center-out orders had different readiness profiles. In MSB-first order, the final carry was fixed after two arrivals for half of all pairs. This is event-index readiness, not physical-time measurement or a universal eight-bit threshold.

---

## 12. Fold/unfold execution

Literal equal-half folding `D=A xor reverse(B)` unfolds as `A || reverse(A xor D)`. R2, R3, R4 all return exactly from their residuals plus retained reference halves. The folded depth can appear stationary at a face change; the full `(depth,face)` state continues around the original ring. Difference alone is lossy; reference plus difference is reversible.

---

## 13. LEN=8 versus LEN=10 odd-cycle continuation test

The proposed fixed outer-frame/one-middle-bit 27-to-28 template failed its first test: the LEN=8 27-cycle has 12 distinct left 4-bit frames and 12 distinct right 4-bit frames. Exhaustive one-bit insertion at all 9 positions and both values found no embedding of a 27-cycle into a LEN=10 28-cycle. A broader bounded search timed out and is not a result. Direct projection of the LEN=8 cycle's top bit yields 24 distinct parents among 27 states and is not a pairwise one-bit lift.

Status: the simple insertion proposal is a bounded DEAD END; a more general cross-width morphism remains OPEN. Do not promote the timeout to a negative proof.

---

## 14. Corrected quantum-closure draft audit

The displayed root product with standard roots of unity is `p^n-1`, not `p^(n/2)-1`. The exact square-root front-bit identity has a finite counterexample at `L=4,u=49/128`. The unmasked compressed block Walsh formula fails at `n=6,s=000011` (direct coefficient 0, draft expression 8); the full-size palindrome mask repairs the finite formula. The supplied radial certificate passes 28/28 for D mod 3 equal to 0 or 1, but only 6/28 for residue 2 in D=13..96.

A Bell state and a classical correlated mixture share computational-basis populations but differ in coherence. This ring audit does not derive the Born rule, Heisenberg uncertainty, Bell entanglement, or other physical claims. Such identifications remain PULL until states, measurements, and dynamics are explicitly connected.

---

## 15. Current ledger

| Item | Status |
|---|---|
| Original ring partner, ordering, center swap, rank/unrank | STANDS / RUNS in stated domains |
| E/G two-branch extension and exact target addresses | RUNS through target width 20 |
| Route ↔ word ↔ rank ↔ physical address | RUNS in audited ranges |
| Fold residual + retained reference unfolding | RUNS on R2–R4 |
| R2–R4 finite transition compiler | RUNS on every state; width cap is implementation policy |
| Square-root operator B=S² and LEN=6 detached component | Algebra identity + RUNS through LEN16 |
| Global C-paired B-cycle rungs | Constructive rule + RUNS through word width 16; phase convention explicit |
| Universal Frobenius zero proof | OPEN; short detached-cycle exclusion needed |
| Differential quotient as a graph cover of simple Q3 | DEAD END for the stated map; it is a vertex quotient, not an edge cover |
| Walsh parity, comparator/Delta spectra, full corrected body | SEALED / RUNS in stated domains |
| Seam profile | SEALED / RUNS; exact digital staircase, not smooth closure |
| Degree-two concentration | RUNS finite n=2..20; continuum/quantum cause OPEN |
| Exact square-root radial bit law | DEAD END as stated; finite counterexample recorded |
| D mod 3=2 benchmark certificate | OPEN; displayed witness fails many tested cases |
| Odd-cycle LEN8→LEN10 one-bit insertion | DEAD END in tested grammar; general morphism OPEN |
| Profile-language regularity, full A(q_D) union | OPEN |
| Physical quantum, spin, gravity identifications | PULL |
| SHA as a preimage decoder / global orbit compiler | PARKED / OPEN; codec relabeling is not inversion |

---

## 16. Provenance and cautions

This Markdown combines source-corpus notes, user-reported audits, and independent conversation executions. The individual appended audit entries preserve their narrower provenance and finite scopes. A seal on a script validates those bytes, not every interpretation in the prose. Reported `/tmp/...` files were not independently executed unless explicitly stated. The file is an append-only research log, not a claim that every open item has been solved.
