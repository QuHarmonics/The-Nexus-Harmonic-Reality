# One hold, three locations: counter, sheet, and frames

**Status:** finite combinatorial checks RUNS. The physical interpretation remains PULL.

## Definition

At width \(n\), let \(P_n\) be the ring partner: reverse the bits if the word is not palindromic, and complement it if it is palindromic. For an ordered stream \(\sigma=(x_0,\ldots,x_{2^n-1})\), define the hold after \(t\) arrivals by

\[
H_\sigma(t)=\#\{\{x,P_n(x)\}:\text{exactly one member occurs among }x_0,\ldots,x_{t-1}\}.
\]

This counts partner pairs that cross the current prefix cut. It is an exact integer statistic of an ordering, not elapsed time.

## 1. Counter location: value order

For the counter stream \(0,1,\ldots,2^n-1\), the audited law is the existing W2 identity

\[
H_{\rm value}(t)=2r_n(t)-t
=\Delta_n(t)+\min(\pi_n(t),2H_p-\pi_n(t)),
\]

where \(r_n(t)\) counts canonical representatives below \(t\), \(\Delta_n\) is the reversal-pair cut imbalance, \(\pi_n(t)\) counts palindromes below \(t\), and \(H_p=2^{\lceil n/2\rceil-1}\). Its unique maximum is at the seam \(t=2^{n-1}\), with

\[
\max_t H_{\rm value}(t)=2^{n-2}+H_p.
\]

The exhaustive streamed profile matched `wheels.hold(t,n)` at every prefix for widths 2–12. This is the quarter-ring-scale hold plus the palindrome tent, rather than the address-order triangle.

## 2. Sheet and address location: the triangular profile

Address order emits \(R_n[0],R_n[1],\ldots\). By the facing law, the first half contains exactly one member of each partner pair; the second half closes those pairs in reverse order. Therefore

\[
H_{\rm address}(t)=\min(t,2^n-t).
\]

The W6 sheet order is reproduced exactly as the supplied runner defines it: concatenate the fixed-width words in the ring tape, reverse the entire bit tape, complement each bit, then re-chunk into \(n\)-bit words. The sheet word corresponding to address word \(x\) is \(F_n(x)=\bar{x}\) when \(x\) is non-palindromic and \(F_n(x)=x\) when \(x\) is palindromic. This map commutes with the partner involution and is bijective, so the first sheet half also contains one endpoint from each pair. Thus

\[
H_{\rm sheet}(t)=\min(t,2^n-t).
\]

The route-code order uses the corpus E/G route code with the side bit as the leading bit. All canonical representatives precede all partner-side words, so it has the same triangular profile:

\[
H_{\rm route}(t)=\min(t,2^n-t).
\]

The independent stream counter confirmed these three entire profiles are equal at every prefix, for every width 2–12—not merely their seam values. Each reaches \(2^{n-1}\) open pairs at \(t=2^{n-1}\).

## 3. Half-table and pair-frame location

A half-table index names a whole pair, not a single endpoint, so a word-level hold requires declaring how the pair is read. The audit uses the natural pair-adjacent lift: for each increasing canonical half-table index, emit the representative and then its partner. Under that explicit order,

\[
H_{\rm pair}(t)=t\bmod 2,
\]

so the hold alternates between one and zero and never exceeds one open pair. This distinguishes the half-table's unit pair-address from the larger prefix cuts of the full-tape orders.

## 4. Frame location: the full tower mirror

Let \(n=L+k\), \(1\le k\le L\), \(0\le t\le 2^L\), and \(q=\lceil t/2^k\rceil\). Define

\[
C_w(q)=\#\{x:0\le x<q,\;x>P_w(x),\;J_w(x)\ne x\},
\]

where \(J_w\) is bit reversal and \(C_0(q)=0\) for the width-zero base. The exact tower-mirror prediction is

\[
\boxed{H_{L+k}(t)=t-2C_{L-k}(\lceil t/2^k\rceil).}
\]

The count is specifically the number of **non-palindromic partner-side words** below \(q\), not all non-palindromic words. The distinction matters: the complement partner rule acts on palindromes and they are intentionally excluded from \(C_w\).

At \(t=2^L\), this reduces to the earlier seam result

\[
H_{L+k}(2^L)=2^L-\left(2^{L-k}-2^{\lceil(L-k)/2\rceil}\right),
\]

matching the existing 819-case seam check through \(L=40\).

The full profile was checked at every \(t\) for \(L=2\ldots16\), every \(k=1\ldots L\): 1,966,215 points, zero mismatches against `wheels.hold`; 130,111 of these points also matched an independent direct stream counter at target widths up to 16. All row-level predicted and returned values are retained in `tower_mirror_full_profile.csv.gz`.

## Audit scope and limits

The five explicit stream orders were exhaustive at widths 2–12 (40,995 prefix rows). The tower profile was exhaustive on the stated finite domain. The supplied ZIP does **not** contain the XLSX workbook itself; the sheet order here follows its W6 construction in the included runner, and this run did not independently re-read the workbook's cached cells. These results establish discrete pair-cut identities over the tested domains; they do not establish physical time or a physical interpretation of the hold.
