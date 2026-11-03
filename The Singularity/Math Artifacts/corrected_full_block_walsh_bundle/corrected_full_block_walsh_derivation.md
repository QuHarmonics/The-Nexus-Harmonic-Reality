# Corrected full-block Walsh formula and degree-two audit

## Definitions

N=2^n, M=N/2, z(i)=wt(R_n[i])-n/2, E(i)=(z(i)+z(N-1-i))/2. The Walsh convention is hat f(s)=sum_i f(i)(-1)^popcount(s&i). Mode bits use least-significant-bit numbering. The radial slice index uses most-significant-bit numbering.

## Pair folding and center swap

E(i)=E(N-1-i), so odd-popcount modes vanish. For even-popcount s, the two sites of a pair contribute twice the canonical contribution. Swapping the center pair has no effect because its two addresses differ by N-1 and therefore have equal characters for even s.

Put t=s mod M. The canonical address for descending offset q may therefore be written M-1-q when evaluating an even character, including q=0. Since q<M, M-1-q=(M-1) xor q, yielding the prefactor (-1)^popcount(t).

## All blocks, even n=2h

H=2^h, e_K=1[K>=H/2], S_K=K+e_K, D_K=K(K-1)/2+max(0,K-H/2). Let r_i enumerate 0,...,S_K-1 by increasing h-bit reversal, and let eta_K(i)=1[r_i<K]. The canonical word has high half H-1-K and low half H-1-J_h(r_i), q=D_K+i. The r_i=K entry is the palindrome, and must retain its position but contribute zero to E.

The exact formula for even-popcount s is

Ehat(s)=2*(-1)^popcount(t)*sum_K sum_(i=0)^(S_K-1) eta_K(i)*(h-wt(K)-wt(r_i))*chi_t(D_K+i).

Define

C*_K(t)=sum_i eta_K(i)*chi_t(D_K+i),
C*_(K,l)(t)=sum_i eta_K(i)*chi_(2^l)(r_i)*chi_t(D_K+i).

Using wt(r_i)=sum_l(1-chi_(2^l)(r_i))/2 gives

Ehat(s)=2*(-1)^popcount(t)*sum_K[(h-wt(K))*C*_K(t)-(1/2)*sum_l(C*_K(t)-C*_(K,l)(t))].

Odd s gives zero. The original compressed K-entry formula is valid before palindrome entries appear, but not across all blocks.

For e_K=1 the palindrome slot is i_pal=R_h(K,J_h(K)). Thus the unweighted C*_K is the full interval-character sum on [D_K,D_K+S_K), minus the character at that one slot. The weighted signed sum remains explicit; no unproved general fast evaluation or continuum limit is claimed.

## Odd n=2h+1

There are middle halves mu=1 then mu=0. Use q_mu=2D_K+(1-mu)S_K+i and latitude h-1/2+mu-wt(K)-wt(r_i), with the same eta_K. Sum both halves and use the same pair-fold prefactor. This is what the audit uses for odd widths.

## Direct center-out spectrum identity

Let B(q)=E(M+q), q=0,...,M-1, and G(t)=sum_q B(q)chi_t(q). For a full mode s with low bits t and top bit s_top,

Ehat(s)=[(-1)^popcount(t)+(-1)^s_top]*G(t).

Hence Ehat(s)=0 for odd |s| and 2*(-1)^|t|G(t) for even |s|. The full degree is |s|=|t|+(|t| mod 2), so full degree 2 receives precisely the center-out degree-1 and degree-2 bins. Their energies are multiplied by four. This gives an exact finite-degree grouping identity, not a proof of an asymptotic quantum quadratic phase.

## Square-root counterexample

u=49/128,L=4: 16u=6+1/8, i=6, k=floor(4/8)=0, R4[6]=0111, observed bit 0. But tau=1-sqrt(15)/8>1/2 because sqrt(15)<4, so its first binary bit is 1. The disagreement is exact and not a rounding endpoint.

## Visible proof obligations

Only original Hole 1 and Hole 2 (links 2A-2C) were provided before the draft truncates. The five visible obligations are: (1) latitude spectrum and degree-energy explanation, (2) support-set block unions, (3) infinite continuation-language distinguishability, (4) asymptotic entropy/growth assertions, (5) benchmark certificates including D mod 3=2. Original numbered Holes 3-5 are not reconstructed or claimed audited.

1. Corrected finite spectrum formula passes; a compact general signed-block evaluator, all-depth energy theorem and proposed continuum cause remain distinct tasks.
2. Support-set intersection is exact when all addresses and faces are included. If this representation alone is the goal, it is supplied. A simplified analytic union for the benchmark at all depths still needs derivation/evaluation.
3. Myhill-Nerode requires a common finite suffix z allowed after one prefix but impossible after the other. Distinguishing individual selected rays is not sufficient. The finite square-root premise fails as above.
4. Finite depth-20 counts do not prove an asymptotic growth rate or entropy limit.
5. For D=13,...,96, exact rational certificate tests passed 28/28 in each class 0 and 1, and 6/28 in class 2. A universal class-2 witness is not supplied by that formula. At D=14 the failure is L=12,address=2052,slice=4,word=111101001111, actual 0 instead of required 1.

## Audit coverage and provenance

All widths n=2,...,20 were checked: 2,097,148 full-address coefficients reconstructed from the full masked blocks and the half-length center-out transform. Original grow/partner matching was independently checked through n=10. Exact energy shares use integer transforms of twice-latitude, so their ratios equal those for z. Participation ratios are approximate and separately labeled.

Source and scope declaration were sealed before execution and rechecked afterward over literal bytes, including final newlines. The scope explicitly measured degree shares rather than presuming particular percentages. The separate older root-product and Bell-state checks were not rerun in this extended degree audit; the new bundle is not represented as a byte-identical copy of that earlier archive.
