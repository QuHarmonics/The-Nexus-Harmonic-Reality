# Interior-body rank and digit-sum law

## Main result

Let \(J_n(x)\) be reversal of the \(n\)-bit word, and let the partner map be
\[
P_n(x)=
\begin{cases}
J_n(x),&J_n(x)\ne x,\\
\overline{x},&J_n(x)=x.
\end{cases}
\]
Call \(x\) canonical when \(x<P_n(x)\). Define the comparator
\[
c_n(x)=\operatorname{sgn}(J_n(x)-x),\qquad
\Delta_n(p)=\sum_{x<p}c_n(x).
\]
The signed palindrome-prefix correction is
\[
\Pi_n(p)=
\#\{x<p:J_n(x)=x,\ \operatorname{msb}(x)=0\}
-\#\{x<p:J_n(x)=x,\ \operatorname{msb}(x)=1\}.
\]

Then, for every integer threshold \(0\le p\le 2^n\),
\[
\boxed{\operatorname{rank}_n(p)
=\#\{x<p:x<P_n(x)\}
=\frac{p+\Delta_n(p)+\Pi_n(p)}2.}
\]

This is a prefix-rank formula for all words, not only palindromes.

## Proof by partitioning the prefix

Among the \(p\) words \(x<p\), write:
- \(A\): nonpalindromes with \(x<J_n(x)\);
- \(B\): nonpalindromes with \(x>J_n(x)\);
- \(P_0\): palindromes whose leading bit is zero;
- \(P_1\): palindromes whose leading bit is one.

These exhaust the prefix, so \(p=A+B+P_0+P_1\). The comparator prefix is \(\Delta_n(p)=A-B\); palindromes contribute zero to it. The signed correction is \(\Pi_n(p)=P_0-P_1\). Therefore
\[
\frac{p+\Delta_n(p)+\Pi_n(p)}2
=\frac{(A+B+P_0+P_1)+(A-B)+(P_0-P_1)}2
=A+P_0.
\]
A word is canonical exactly when it is a nonpalindrome satisfying \(x<J_n(x)\), or a palindrome with leading bit zero. Thus \(A+P_0\) is exactly the number of canonical words below \(p\). This proves the identity.

## Closed palindrome correction

Let \(M_p=2^{\lceil n/2\rceil}\) be the total number of \(n\)-bit palindromes, and set
\[
t_n(p)=\#\{x<p:J_n(x)=x\}.
\]
The palindromes are in numeric order by their first \(\lceil n/2\rceil\) bits. The first \(M_p/2\) have leading bit zero and contribute \(+1\) to \(\Pi_n\); the last \(M_p/2\) have leading bit one and contribute \(-1\). Hence
\[
\boxed{\Pi_n(p)=\min(t_n(p),M_p-t_n(p)).}
\]

For \(p<2^n\), write \(h=\lfloor n/2\rfloor\), \(H=2^h\), \(U=\lfloor p/H\rfloor\), and \(B=p\bmod H\). The palindrome matching prefix \(U\) has suffix \(\operatorname{rev}_h(U\gg(n\bmod2))\). All prefixes less than \(U\) are already below \(p\); the palindrome with prefix \(U\) is below \(p\) exactly when its suffix is less than \(B\). Consequently
\[
\boxed{t_n(p)=U+
\mathbf 1\{\operatorname{rev}_h(U\gg(n\bmod2))<B\}.}
\]
At \(p=2^n\), \(t_n(p)=M_p\) and \(\Pi_n(p)=0\).

For a **canonical palindrome** \(p\), its leading bit is zero, the same-prefix indicator is zero, and its half-word value \(u\) equals both \(t_n(p)\) and \(\Pi_n(p)\). This recovers
\[
\operatorname{rank}_n(p)=\frac{p+u+\Delta_n(p)}2.
\]
The reduction does not apply to a noncanonical palindrome; there \(\Pi_n(p)=M_p-t_n(p)\).

## Closed \(\Delta\) formula used in the test

With \(R_h(u,v)=\#\{b:0\le b<u,\operatorname{rev}_h(b)<v\}\), \(H=2^h\):

For \(n=2h\), if \(p=AH+B\),
\[
\Delta_{2h}(p)=A(H-A)+B-2R_h(B,A)
-\mathbf1\{\operatorname{rev}_h(A)<B\}.
\]

For \(n=2h+1\), if \(p=(2A+\mu)H+B\),
\[
\Delta_{2h+1}(p)=2A(H-A)+\mu(H-1-2A)+B
-2R_h(B,A)-\mathbf1\{\operatorname{rev}_h(A)<B\}.
\]
Both endpoint values are \(\Delta_n(0)=\Delta_n(2^n)=0\).

The rectangle count \(R_h\) was tested in two ways. Exhaustively for every \(u,v\) at \(h=1,\ldots,8\), it agrees with direct counting. Its scalar digit-sum implementation uses reversal-prefix blocks: for each set bit \(u_k=1\), let \(r_k\) be the low \(h-k-1\) bits of \(\operatorname{rev}_h(u)\). That bit contributes
\[
\max\left(0,\left\lceil\frac{v-r_k}{2^{h-k}}\right\rceil\right).
\]
The sum over set bits is \(R_h(u,v)\); \(R_h(H,v)=v\).

## From rank to the body waveform

Let \(s_n(i)\) be the canonical representative of rank \(i\), i.e. the unique canonical \(p\) with \(\operatorname{rank}_n(p)=i\). The left-face latitude is the digit-sum readout
\[
z_n(i)=\operatorname{wt}(s_n(i))-\frac n2
\]
before the center swap. The ring then applies its defined central exchange: positions \(M-1\) and \(M\) are swapped, with \(M=2^{n-1}\). Away from that central pair, the physical left face is the rank-selected canonical word; the right face follows \(R_n[2^n-1-i]=P_n(R_n[i])\).

Thus the body is an exact discrete popcount signal composed with the inverse of an explicit prefix-rank function. This is a rank/select statement, not a claim of a closed algebraic formula for the inverse and not a smoothness claim. The earlier normalized closure-spike result is unchanged.

## Executed checks

- All 2,097,148 thresholds p=0,...,2^n-1 for widths n=2,...,20: rank identity, closed Delta, signed palindrome correction, and palindrome-prefix count matched direct counts; each terminal threshold p=2^n was separately checked against rank 2^(n-1), Delta=0, and Pi=0.
- 4,090 palindromes checked; 2,045 canonical-palindrome special cases reduced to the half-word formula.
- 88,408 rectangle-counter pairs exhaustively checked for \(h=1,\ldots,8\).
- 32,777 scalar \(\Delta\) checks against direct comparator-prefix sums at widths 2–14.
- 4,160 rank/select inverse checks, including every canonical rank at widths 2–12 and wide samples through width 1,024.
- 108 wide scalar prefix ranks at widths 21, 32, 63, 64, 127, 128, 255, 256, 511, 512, 1,023 and 1,024 matched an independent mirrored-pair rank DP.
- Materialized ring addresses were checked for widths 2–20, including physical-address uniqueness after the center swap; the partner-facing law passed at every width.

## Provenance qualification

The first audit attempt stopped at width 3 because a validation assertion incorrectly extended \(\Pi_n(p)=u\) to **all** palindromes; it is true for canonical palindromes only. The general identity and compact signed correction were left intact, the special-case statement was corrected in the prediction, and a new prediction hash was sealed before the successful run. A subsequent generated-source syntax error was caught before any test ran and fixed before the successful run. The active prediction/source hashes below were verified after execution.
