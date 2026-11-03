# Append-only stroke: the even-body seam profile

The definition is E_n(i)=(z_n(i)+z_n(2^n-1-i))/2. It equals z at nonpalindromes and is exactly zero at palindromes. This is not a punctured curve with missing palindrome samples.

## Exact nonpalindromic block profile

Let h=floor(n/2), H=2^h. Restrict to blocks 1<=K<H/2, before palindrome representatives enter. Let r range over 0<=r<K in increasing h-bit-reversal order, with within-block index i.

For even n, q=K(K-1)/2+i and deficit D(q)=n/2-E_n(center +/- q)=wt(K)+wt(r).

For odd n, q=K(K-1)+(1-mu)K+i and D(q)=wt(K)+wt(r)+1-mu.

The underlying canonical word has high half H-1-K and low half H-1-J_h(r), plus the middle mu at odd width. Except for the swapped center pair, the right face reads its partner. This gives exact words, not only weights. The zero positions occupy a core of at most 2*bit_length(K) bits (+one middle bit), with ones outside.

The scalar selector for r uses fixed lower-bit residue counts below K; it does not enumerate r or the ring. At fixed q, the word is padded by one 1 at each end under n->n+2, the body increases by 1 and the deficit is unchanged, whenever the declared block domain holds.

## What is logarithmic

Writing ell=bit_length(K), D<=2ell-1 at even width and D<=2ell at odd width. Since q is of order K^2, this is a logarithmic upper envelope/core-size bound. There is no comparable pointwise logarithmic lower bound: for K=2^t, q=K(K-1)/2 has r=0 and deficit exactly 1 at arbitrarily large depths across the stack.

The mean deficit of an even block is wt(K)+(1/K)*sum_(r<K)wt(r). The sum has the standard per-bit complete-period/remainder count. The odd block adds 1/2 to that mean. No smooth monotone cusp is inferred from these means.

For the clean family q=2^(2t-1), K=2^t and r=1, so the even deficit is exactly 2. This must not be broadened to every raw dyadic q: at n=10,q=64, K=11,r=3 and R_10[576]=1110000101 has five zeros. This is not an audit of additional conditions in the unprovided full statement of Theorem C.

## Outer closure certificate

For all n>=2,

E_n(0)=E_n(2^n-1)=0,
E_n(1)=E_n(2^n-2)=1-n/2.

Thus for normalized height e_n=2E_n/n, an adjacent closure difference is 1-2/n across angular separation 2pi/2^n. The original pole-to-pole discontinuity is absent, but the exact zero-filled even projection has narrow spikes. Any family of interpolants retaining all sample values lacks a uniform Lipschitz bound there. A separate coarse-graining, gap-filling, or continuum-limit claim remains OPEN and must name its readout and normalization.

## Executed checks

- 261,121 nonpalindromic center depths; 522,242 paired-face samples through n=20.
- 65,025 fixed-depth comparisons under n->n+2, all exact.
- Ninety-six scalar word/address checks through n=1025, without full rings.
- Every closure identity at n=2,...,20.
- Exact graph data and a two-panel PDF at n=12.

## Status

SEALED, RUNS: exact block profile, logarithmic core-size/upper-deficit bound, fixed-depth stability, power-family identities, and closure-adjacency identities.

The blanket two-or-three-zero reading of every raw dyadic distance is a DEAD END in this coordinate; its owner is the missing domain/offset qualifier, not a failure of the partner rule.

A uniformly smooth outer closure for the exact Walsh-even sample sequence is a DEAD END under the stated normalization. A separately specified smoothed or punctured profile is OPEN. The compact even-degree Delta spectrum, profile-language regularity and full A(q_D) union remain unchanged OPEN items. SHA remains parked.

## Byte provenance

Both active seals hash literal file bytes, including the prediction file's final newline. No normalization or stripping. One source-only draft revision was made and re-sealed before the first audit execution, replacing a reference-derived center value with its independent scalar prediction. The seal manifest records the superseded hash and active hash. Active source and prediction hashes matched after execution.
