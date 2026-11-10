# Audit of the proposed quantum/open-hole closures

Scope: the visible draft only. Its final certificate argument is truncated, and later holes are not supplied. Original ring word_at was checked against grow for every word through width 10. No new ring ordering was introduced.

## Exact counterexamples

1. With zeta_n=exp(2*pi*i/n), prod_(m=0)^(n-1)(p-zeta_n^m)=p^n-1. At p=2,n=8 the product is 255, not 15. At p=3 every unit-root factor has magnitude at least 2, so the stated unit-magnitude condition cannot hold as written.

2. Finite square-root front-bit identity: L=4,u=49/128. Then floor(2^L u)=6, the slice is floor(4*1/8)=0, R4[6]=0111, so the radial bit is 0. But tau=1-sqrt(15)/8>1/2, so its first binary bit is 1. An asymptotic rank approximation cannot be substituted for this exact finite digit claim.

3. Full-block even-body formula: the unmasked K-element compressed index omits the slot occupied by the palindrome in blocks K>=H/2. At n=6, mode 000011, the direct unnormalized body Walsh coefficient is 0; the displayed compressed-index formula gives 8. Using all S_K=K+e_K slots and masking the r=K palindrome gives 0, and the repaired expression matched every checked coefficient at n=4,6,8,10,12.

4. The certificate u_D=1/2+2^(-p)+(2/3)2^(-(D-1)), p=floor(2D/3)+1, was checked with exact rational arithmetic for D=13,...,96. All 28 cases in each residue class 0 and 1 passed; only 6/28 cases in residue class 2 passed. At D=14, u=6157/12288, the first failure is L=12: address 2052, slice 4, word 111101001111 emits 0 where the target requires 1. A modified certificate in the unprovided continuation is not tested by this result.

## Correct block-character definitions

Let r_i list 0,...,S_K-1 in increasing h-bit reversal, with S_K=K+1[K>=H/2], and M_K(i)=1[r_i<K]. Replace the compressed block sums by

C*_K(s)=sum_(i=0)^(S_K-1) M_K(i) chi_s(D_K+i),
C*_(K,l)(s)=sum_i M_K(i) chi_(2^l)(r_i) chi_s(D_K+i).

Then use the same additive weight decomposition and canonical-rank character prefactor as in the draft. The center swap cancels for even-degree modes as stated. This repairs the finite expression; it does not alone establish the proposed continuum explanation of degree-two energy or its computational complexity.

## Nonregularity proof obligation

For profile prefixes p and q, distinguishing selected angles inside their supports is not sufficient. A Myhill-Nerode witness requires one common finite suffix z such that A(pz) is nonempty and A(qz) is empty (or vice versa). If both supports allow both outputs, different selected rays do not distinguish the continuation languages. An infinite pairwise-distinguishable family is not supplied by the argument. The finite square-root premise also has the counterexample above.

The block-slice support intersection is a valid exact definition when all physical addresses, both partner faces, and the center swap are included. It is not by itself an infinite-state or entropy-rate proof.

## Classical parity versus quantum coherence

Phi-plus and the mixture 1/2|00><00|+1/2|11><11| have the same computational-basis populations (1/2,0,0,1/2), and the same classical XOR parity zero, but different matrices. The Phi-plus 00/11 coherence is 1/2; the mixture's is zero. The audit also records their exact partial-transpose spectra. Thus the bit-pair support does not select a Bell state or its relative phase.

Area contraction |s|^2 is a valid linear-map identity, not by itself a Born-probability derivation. Likewise orthogonality of two classical functions is not an uncertainty relation for noncommuting quantum observables. Both classical functions are simultaneously defined on the same word; a common relabeling does not change that fact.

## Ledger treatment

Keep the independently established finite ring, rank, comparator, lift and spectral identities. Do not mark all five holes BOUND on the basis of this draft. Retain the quantum interpretations as PULL pending explicit state, measurement and dynamical bridges. The current displayed failures should be appended with their exact owners, not silently repaired or attributed to a different ring convention.

The new audit source and declaration were sealed before execution and checked afterward over literal bytes including final newlines. This verifies only this independent audit, not unprovided corpus scripts or reported seals.
