# Runtime Reflection of the BBP Formula: Proof of the Persistent Pending-Field Reader

**Proof note — 12 October 2026**

## Abstract

This note proves the correctness of the persistent pending-field reader implemented in `pending.py`. The reader does not evaluate unopened BBP terms to estimate their value. Instead, it advances a retained set of reciprocal-remainder lanes, stores their scaled partial sum in an integer accumulator, and encloses the unopened contribution with a rational geometric bound. The three operations—OPEN, WIDEN, and EMIT—preserve exact state identities. Those identities imply an interval containing the exact unread value, make certification sound, and, under the specified scheduling rule, guarantee that every hexadecimal digit of π is eventually certifiable.

The claim is operational rather than ontological: no new constant, denominator family, or physical primitive is introduced. The reader is aligned to arithmetic already present in the BBP representation. “Potential sealed on opening” means that, once a lane's denominator and remainder are fixed, all its future quotient/remainder states are determined by a recurrence. The empirical counts reported by the executable audit are kept distinct from the universal theorems proved here.

## 1. The object being read

Write the BBP identity as

\[
\pi=\sum_{k=0}^{\infty}\sum_{j\in J}c_j\frac{16^{-k}}{8k+j},
\qquad J=\{1,4,5,6\},
\]

with

\[
(c_1,c_4,c_5,c_6)=(4,-2,-1,-1).
\]

Let \(x_n\) denote the fractional part of \(16^n\pi\), a value between zero and one. For zero-based position \(n\), the target hexadecimal digit is

\[
d_n=\operatorname{floor}\left(16x_n\right).
\]

Equivalently, because taking a fractional part changes a number only by an integer,

\[
d_n=\operatorname{floor}\left(16^{n+1}\pi\right)\bmod16.
\]

The lane weights sum to \(4\) on the positive side and to \(4\) in absolute value on the negative side:

\[
\sum_{c_j>0}c_j=4,\qquad\sum_{c_j<0}|c_j|=4,\qquad\sum_{j\in J}|c_j|=8.
\]

These equalities supply the constants in the enclosure proof.

## 2. Machine state and lane invariant

At a machine state let:

- \(n\) be the number of digits already emitted;
- \(K\) be the largest opened layer, so layers \(k=0,\ldots,K\) are retained;
- \(P\) be the number of hexadecimal places represented below the read point;
- for each opened lane \((k,j)\), \(D_{k,j}\) be its fixed denominator, \(r_{k,j}\) its top remainder, and \(b_{k,j}\) its lower remainder;
- \(S\) be the signed integer accumulator.

If layer \(k\) is opened at position \(n_o\), its denominator is

\[
D_{k,j}=(8k+j)16^{k-n_o},\qquad k\ge n_o.
\]

Opening initializes \(r_{k,j}=1\bmod D_{k,j}\). Every EMIT applies long division:

\[
(q,r')=\operatorname{divmod}(16r,D).
\]

Thus \(r/D\) is the current lane contribution, and its next contribution is \(r'/D\). The remainder sequence is deterministic once \(D\) and the opening remainder are fixed. No later decision changes that lane's transition law.

For every live lane, the lower cursor satisfies the exact invariant

\[
b_{k,j}=(16^P r_{k,j})\bmod D_{k,j}.
\qquad\mathrm{(1)}
\]

The accumulator invariant is

\[
S=\sum_{k=0}^{K}\sum_{j\in J}
 c_j\operatorname{floor}\left(\frac{16^P r_{k,j}}{D_{k,j}}\right).
\qquad\mathrm{(2)}
\]

Both are integer identities. They do not depend on floating-point arithmetic.

### Lemma 1 — a lane represents the right term

At every position \(n\) after a lane \((k,j)\) was opened at \(n_o\),

\[
\frac{r_{k,j}}{D_{k,j}}=\left(\frac{16^{n-k}}{8k+j}\right)\bmod1.
\qquad\mathrm{(3)}
\]

**Proof.** At opening, \(r=1\bmod D\), so \(r/D=\{1/D\}=\{16^{n_o-k}/(8k+j)\}\), where braces denote fractional part. This includes the exceptional \(D=1\) case: then \(r=0\) and \(\{1/D\}=0\). Each EMIT multiplies the lane value by 16 and subtracts the integer quotient \(q\), exactly implementing fractional-part evolution. Induction over the number of emissions proves (3). \(\square\)

## 3. The unresolved continuation and its bound

Define the opened field and unopened continuation by

\[
F_{n,K}=\sum_{k=0}^{K}\sum_{j\in J}c_j\frac{r_{k,j}}{D_{k,j}},
\qquad
U_{n,K}=\sum_{k=K+1}^{\infty}\sum_{j\in J}
 c_j\frac{16^{n-k}}{8k+j}.
\]

For the states used to certify output, \(K\ge n\), so every unopened layer is strictly to the right of the read point. But the geometric bound below is valid whenever the displayed sum is formed, including intermediate states immediately after an emission.

By Lemma 1, replacing an opened term \(16^{n-k}/(8k+j)\) with its fractional part removes an integer only. Since the coefficients \(c_j\) are integers, there is an integer \(Q_{n,K}\) such that

\[
Y_{n,K}:=F_{n,K}+U_{n,K}=16^n\pi-Q_{n,K}.
\qquad\mathrm{(4)}
\]

Consequently, \(Y_{n,K}\) has exactly the target hexadecimal digit at position \(n\), modulo the integer shift \(Q_{n,K}\). The continuation is not evaluated lane by lane. It appears in the algorithm only through a bound.

### Lemma 2 — unopened-tail bound

For every \(n,K\),

\[
|U_{n,K}|\le B_{n,K}:=
\frac{128}{15(8K+9)}16^{n-K-1}.
\qquad\mathrm{(5)}
\]

**Proof.** For \(k\ge K+1\), every denominator satisfies \(8k+j\ge 8K+9\). Taking absolute values and using \(\sum_j|c_j|=8\),

\[
|U_{n,K}|
\le \frac{8}{8K+9}\sum_{k=K+1}^{\infty}16^{n-k}.
\]

The remaining geometric sum is

\[
\sum_{h=0}^{\infty}16^{-h}=\frac{16}{15}.
\]

Therefore

\[
|U_{n,K}|\le\frac{8}{8K+9}16^{n-K-1}\frac{16}{15}
=\frac{128}{15(8K+9)}16^{n-K-1}=B_{n,K}.
\]

This uses the geometric sum, not evaluation of the unopened terms. \(\square\)

## 4. The integer enclosure

Let \(L=K+1\) be the number of opened layers. From (2), for a positive coefficient each truncated contribution lies between its integer floor and that floor plus one; for a negative coefficient the inequality reverses. Therefore

\[
S-4L < 16^P F_{n,K}\le S+4L.
\qquad\mathrm{(6)}
\]

Set

\[
T=\operatorname{ceil}\left(16^P B_{n,K}\right),
\qquad
\ell=S-4L-T,
\qquad
u=S+4L+T.
\qquad\mathrm{(7)}
\]

Since \(T\ge16^P|U_{n,K}|\), equations (4)–(7) give the central invariant:

\[
\boxed{\ell\le16^P Y_{n,K}\le u.}
\qquad\mathrm{(8)}
\]

The implementation computes exactly these integer endpoints. The only operation involving the unopened contribution is the closed-form rational bound (5), rounded upward to \(T\).

## 5. The three operations preserve the state

### Theorem 1 — OPEN preserves the accumulator and enclosure invariants

OPEN advances \(K\) by one, adds the four lanes of the new layer, and adds their corresponding floors to \(S\). For a lane opened at the current position, \(D=(8k+j)16^{k-n}\), \(r=1\bmod D\), and \(b=(16^P r)\bmod D\). Its contribution to the accumulator is exactly \(c_j\operatorname{floor}\left(16^P r/D\right)\), so (1) and (2) hold for the added lanes as well as the retained ones. Opening transfers a layer from \(U\) to \(F\) by replacing each full lane term with its fractional part. Because the coefficients are integers, the change in \(Y=F+U\) is an integer; identity (4) therefore continues to hold with an updated integer \(Q_{n,K}\), and the target digit modulo 16 is unchanged. The first OPEN is the exceptional case: the \((k,j)=(0,1)\) lane has unweighted term 1 and weight 4, so it shifts \(Y\) from \(\pi\) to \(\pi-4\) while leaving the hexadecimal digit unchanged. Every later opened term is less than one before weighting. Recomputing (5) after incrementing \(K\) gives a valid new tail bound, so (8) continues to hold.

The bound tightens geometrically at each OPEN:

\[
\frac{B_{n,K+1}}{B_{n,K}}=
\frac{8K+9}{16(8K+17)}<\frac1{16}.
\qquad\mathrm{(9)}
\]

### Theorem 2 — WIDEN preserves the invariants

For each lane write

\[
16^P r=qD+b,\qquad 0\le b<D.
\]

Then

\[
\operatorname{floor}\left(\frac{16^{P+1}r}{D}\right)
=16q+\operatorname{floor}\left(\frac{16b}{D}\right).
\qquad\mathrm{(10)}
\]

WIDEN sets \(g=\operatorname{floor}\left(16b/D\right)\), replaces \(b\) with \(16b\bmod D\), and updates

\[
P\leftarrow P+1,\qquad S\leftarrow16S+\sum_{k,j}c_jg_{k,j}.
\]

Equation (10), summed with the signed weights, proves (2) at the new precision. The lower-cursor invariant (1) is updated by the same modular step. No term is opened, no address moves, and the represented exact value \(Y_{n,K}\) is unchanged; only the enclosure becomes more precise in actual-value units.

### Theorem 3 — EMIT preserves the invariants and advances the represented value

For each lane let

\[
(q,r')=\operatorname{divmod}(16r,D),\qquad
(g,b')=\operatorname{divmod}(16b,D),
\]

and let \(C=\sum c_jq\), \(G=\sum c_jg\). Since \(r'=16r-qD\) and (1) holds,

\[
\operatorname{floor}\left(\frac{16^Pr'}D\right)
=16\operatorname{floor}\left(\frac{16^Pr}D\right)+g-16^Pq.
\qquad\mathrm{(11)}
\]

Summing gives the implemented update

\[
S\leftarrow16S-16^P C+G,
\qquad n\leftarrow n+1.
\qquad\mathrm{(12)}
\]

The top and bottom cursor updates preserve (1), and (11) preserves (2). The opened field obeys \(F_{n+1,K}=16F_{n,K}-C\); the unopened continuation obeys \(U_{n+1,K}=16U_{n,K}\). Hence

\[
\boxed{Y_{n+1,K}=16Y_{n,K}-C.}
\qquad\mathrm{(13)}
\]

Thus EMIT advances the represented value by the exact crossing recurrence. It does not recompute the carry from a BBP digit-extraction routine.

## 6. Certification is sound

The code emits only if \(K\ge n\) and the two endpoint floors agree:

\[
a=\operatorname{floor}\left(\frac{16\ell}{16^P}\right),
\qquad
b=\operatorname{floor}\left(\frac{16u}{16^P}\right),
\qquad a=b.
\qquad\mathrm{(14)}
\]

Because (8) encloses \(Y_{n,K}\), monotonicity of the floor function gives

\[
\operatorname{floor}\left(16Y_{n,K}\right)=a=b.
\]

From (4), \(Y_{n,K}=16^n\pi-Q_{n,K}\) with integer \(Q_{n,K}\). Multiplication by 16 makes the shift \(16Q_{n,K}\) an integer multiple of 16, so reduction modulo 16 removes it:

\[
\boxed{a\bmod16=d_n.}
\]

**Therefore every emitted digit is correct if the machine emits it.** This is a proof from the interval invariant; agreement with an independent decimal computation is a separate implementation check.

## 7. Every digit is eventually certifiable

First, no target lies exactly on a hexadecimal digit boundary. If \(16^n\pi\) were an integer multiple of \(1/16\), then \(16^{n+1}\pi\) would be an integer, implying that \(\pi\) is rational. Therefore the target \(Y_{n,K}\), which differs from \(16^n\pi\) by an integer, is never a boundary \(m/16\).

It remains to show that the scheduled interval width tends to zero if certification has not yet succeeded. At a fixed output position \(n\), the scheduler does this:

- OPEN if \(K<n\) or \(T\ge4(K+1)\);
- otherwise WIDEN.

The invariant \(K\ge n-1\) holds: it is true initially, and each EMIT increments \(n\) once while leaving \(K\) unchanged. Thus the \(K<n\) case is only the one-layer catch-up after an emission.

Suppose the loop never certifies. Then \(K\) must be unbounded. If it were bounded, eventually every iteration would WIDEN; at fixed \(K\), \(B_{n,K}>0\) and \(16^PB_{n,K}\to\infty\) as \(P\) grows, forcing \(T\ge4(K+1)\) and another OPEN, a contradiction. Likewise, \(P\) must be unbounded: if it were bounded while \(K\to\infty\), then \(B_{n,K}\to0\) and hence \(T=1\) eventually, while \(4(K+1)\to\infty\), forcing WIDEN and contradicting bounded \(P\).

Unbounded \(K\) and \(P\) alone are not enough; we also need the opened-field rounding radius to vanish. At any OPEN after the one-layer catch-up, the trigger gives

\[
T=\operatorname{ceil}(U)\ge4(K+1),\quad
U=16^PB_{n,K},
\]

so \(U>4K+3\). Substituting (5) yields

\[
16^P>
\frac{15(4K+3)(8K+9)}{128}\,16^{K+1-n}.
\qquad\mathrm{(15)}
\]

Consequently \((K+1)/16^P\to0\) along OPEN states as \(K\to\infty\). Between OPEN operations, \(K\) is fixed and WIDEN only increases \(P\), so the same ratio cannot increase. Also,

\[
\frac{T}{16^P}\le B_{n,K}+16^{-P}\longrightarrow0.
\]

Using \(u-\ell=8(K+1)+2T\), we conclude

\[
\frac{u-\ell}{16^P}
=\frac{8(K+1)+2T}{16^P}\longrightarrow0.
\qquad\mathrm{(16)}
\]

The interval therefore becomes arbitrarily narrow around a value that is not on a digit boundary. Eventually its two endpoints fall in the same hexadecimal digit interval, satisfying (14). This contradicts the assumption that certification never succeeds.

**Termination theorem.** The scheduler eventually certifies each digit. Together with Theorems 1–3, this proves that the reader emits the correct hexadecimal expansion of \(\pi\) indefinitely, under exact arithmetic and the stated BBP identity. \(\square\)

## 8. What “sealed potential,” “alignment,” and “balance” mean here

These expressions are interpretations of the proved mechanism, not additional mathematical axioms.

**Sealed potential.** When a lane opens, its denominator and remainder determine every subsequent quotient and remainder. The future is not supplied by an outside lookup. The program mutates the current remainder in place, but each update is a deterministic transformation of the retained state.

**Alignment, not invention.** The reader does not create \(\pi\), the BBP identity, the denominator family, or the base-16 long-division law. Its contribution is a way to read those existing relations incrementally, with a certificate for each released digit. In research terms, any novelty claim concerns this reader design, proof, and measured behavior relative to prior literature—not a claim that the underlying arithmetic was newly created. A priority claim should wait for a full prior-art search.

**Balance.** Certification of digit \(n\) requires \(K\ge n\). Starting from \(K=-1\), producing \(N\) digits therefore requires at least \(N\) opened layers. Each layer introduces four lane records, while each emitted hexadecimal digit is one four-bit symbol. In the audited 2,000-digit run, exactly 2,000 layers were opened and none was discarded or reopened; hence the observed count is exactly one opened layer per emitted digit. This equality is a measured property of this run, not a universal theorem that no difficult input can ever require extra lookahead. The structural lower bound—at least one opening per emitted digit—does follow from the state invariant.

**Carry.** The carry is not a separate answer fetched from the original digit-extraction code. The signed accumulator \(S\) is advanced by (12), and the integer part is read from the current certified interval. When the interval does not yet determine that integer part, the reader reports no certified carry rather than guessing.

## 9. Reproducibility and scope of the executable audit

The supplied implementation was rerun with the acceptance harness configured for 2,000 digits. All 2,000 emitted digits match a high-precision `mpmath` reference computed independently of BBP; all 2,003 OPEN/WIDEN refinements and all 2,000 post-emission interval checks pass the harness's numerical containment test. At the final state, all 8,000 top cursors and all 8,000 lower cursors satisfy the checked state identities. The independently computed carry recurrence matches at 400 audited positions. The operation counts are 2,000 OPEN, 3 WIDEN, and 2,000 EMIT; the final state is \(n=2000,K=1999,P=7\).

The companion `pending_proof_audit.py` checks exact integer identities at every state: the accumulator sum (2), bottom-cursor relation (1), OPEN denominator initialization, WIDEN equation (10), EMIT crossing and remainder equations, and exact rational arithmetic for the bound used by the code. Its run reports 4,004 state checks, 16,009,004 lane checks, and 8,004,064 top-transition checks, all passing.

The exact proof above is not based on `mpmath`; the reference comparison is a regression check. The currently executable `pending.py`/`accept.py` pair is configured for 2,000 digits. A separate 10,000-digit result appears in the project notes, but that configuration was not the source audited in this proof note and should not be described as independently reproduced by this run.

The four-rule reflection result has a separate scope: the advance rule was unique among the declared candidate family \((a r+b)\bmod D\), with \(0\le a\le255\) and \(0\le b\le15\), not among every mathematically conceivable rule. The weights were recorded from constants the observed BBP implementation applied; they were not inferred from digit outputs alone.

## 10. Conclusion

The proof's central object is a continuation that is partly explicit and partly bounded. OPEN moves one deterministic lane layer from the unopened continuation into the retained field. WIDEN increases the exact resolution of that field without moving the address. EMIT advances all retained remainders and the accumulator through the same crossing relation. The interval encloses the represented value throughout; its endpoints eventually agree on a digit because the target is irrational and the scheduled interval contracts to zero. The reader therefore releases digits only when the current state certifies them.

That is the defensible mathematical meaning of “the process runs when its conditions are met”: fixed relations determine the next state, and the reader exposes the next distinction when the bound proves it is stable.

## References

Bailey, D. H., Borwein, P. B., and Plouffe, S. (1997). “On the Rapid Computation of Various Polylogarithmic Constants.” *Mathematics of Computation*, 66(218), 903–913.

Gibbons, J. (2006). “Unbounded Spigot Algorithms for the Digits of Pi.” *The American Mathematical Monthly*, 113(4), 318–328. Included as relevant context for streaming digit generation; this proof note does not claim a completed prior-art comparison.
