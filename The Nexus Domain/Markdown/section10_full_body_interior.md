# Append-only section 10: full interior, corrected rank, and palindrome blocks

This entry does not replace earlier sections. SHA remains parked.

## Rank extension: all palindromes versus canonical palindromes

Let pi_n(p)=#{palindromes x<p}, m=ceil(n/2), and T_n(p)=min(pi_n(p),2^(m-1)). Then T counts canonical palindrome representatives below p. The all-threshold rank is

r_n(p)=(p-pi_n(p)+Delta_n(p))/2+T_n(p)
      =(p+pi_n(p)+Delta_n(p))/2-max(0,pi_n(p)-2^(m-1)).

Proof: the nonpalindromic words below p split into x<Jx and x>Jx, whose difference is Delta and whose total is p-pi. Add only the canonical palindromes, not every palindrome. The original plus-pi formula is correct whenever pi=T, in particular on the lower half containing canonical palindromes, but not for all representatives. At n=4,p=1011, pi=3,T=2,Delta=2: the uncorrected value is 8, actual rank 7. At n=20 the uncorrected formula fails on 130,816 canonical words; the corrected formula passes every threshold.

The palindrome count also needs no search: let u be the first ceil(n/2) bits of p, and B_n(u) its palindrome completion. Then pi_n(p)=u+1[B_n(u)<p], with endpoint pi_n(2^n)=2^m.

## Full block decomposition

Put h=floor(n/2), H=2^h, K=H-1-A, e_K=1[K>=H/2], S_K=K+e_K and D_K=K(K-1)/2+max(0,K-H/2). The admitted low-half labels are exactly r=0,...,S_K-1, ordered by increasing h-bit reversal. The sole palindrome label is r=K when e_K=1.

For even n: q=D_K+i, canonical word a=(H-1-K)H+(H-1-J_h(r)).
For odd n: q=2D_K+(1-mu)S_K+i, a=(H-1-K)2H+mu H+(H-1-J_h(r)).

For nonpalindromes, n/2-E_n=wt(K)+wt(r)+(1-mu if odd). At r=K, E_n is exactly zero. Partners and the center swap provide both physical faces.

## Full block sums

Let nu=1 for even n and 2 for odd n; F(S)=sum_(0<=r<S)wt(r), evaluated by per-bit complete periods and remainders.

Canonical-zero sum:
Z_can=nu*(S_K*wt(K)+F(S_K))+(nu-1)*S_K.

Exact even-body deficit sum:
D_body=Z_can+nu*e_K*(h-2wt(K)).

The correction replaces each canonical palindrome's digit-sum latitude by the actual zero in the even projection. Canonical zeros, right-face zeros and body deficits are different sums once palindromes enter; the formula above names the owner explicitly.

## Direct full-ring reader

For either face, let q be center depth and Q=floor(q/nu). If Q<binom(H/2,2), K=floor((1+sqrt(1+8Q))/2). Otherwise K=floor((sqrt(1+8(Q+H/2))-1)/2). Integer square root implements these exactly. Determine i and middle mu from q, D_K and S_K. Select r in reversal order with binary residue counts below S_K. Reconstruct a and apply the physical partner side, including the center swap at q=0.

This avoids binary search over possible word values. The scalar reader uses one integer square root and at most h residue decisions; this is an arithmetic-operation description, not a claim of constant-cost large integers.

## Whole waveform

If a_i is the canonical representative selected by physical address i, then

E_n(i)=1[a_i != J(a_i)]*(wt(a_i)-n/2).

Thus the complete body is a centered digit sum read through the corrected Delta rank/unrank, with the palindrome mask retained. At the closure, r(p)=p for p<2^floor(n/2), giving the address digit sum; at the seam the same general reader reduces to the triangular block law. No extra interpolation or smoothness claim is introduced.

## Execution

All n=2,...,20: 2,097,148 rank thresholds, 2,097,148 full-ring word predictions, 3,049 blocks including 1,534 palindrome-containing blocks. All pointwise body predictions and block sums passed. Additional 120 scalar word/address returns and 90 independent rank comparisons through n=1024 passed. Source and prediction were sealed before execution, using literal file bytes including final newlines, and verified afterward.

## Ledger update

- Corrected all-threshold Delta rank: SEALED, RUNS.
- Uncorrected plus-all-palindromes extension to upper canonical representatives: DEAD END; owner is noncanonical palindromes counted below the cut.
- Full block rule including r=K palindrome entries: SEALED, RUNS.
- Full block canonical-zero sums and even-body deficit sums: SEALED, RUNS.
- Whole pointwise even-body reader: SEALED, RUNS in the audited domains, with scalar wide queries.
- Compact even-degree Delta coefficients, profile-language regularity, full A(q_D) union and physical interpretations retain their previous statuses.
