# Palindrome carrier: order, re-addressing and Walsh spectrum

## Literal order

For n>=2 let m=ceil(n/2). In the original ring ordering, extracting palindrome words and taking their first m bits returns u=0,1,...,2^m-1, not the order R_m except at m=1. Proof: a palindrome is canonical exactly when its first bit is 0. Those canonical palindromes occur in increasing word order on the first face, which is increasing prefix order. The opposite face is their complemented reverse order, which continues increasing prefix order. The swapped center pair is nonpalindromic for n>=2 and does not alter this extraction.

Define B_n(u)=u||reverse(u) for n=2m, and B_n(u)=u||reverse(u without its final bit) for n=2m-1. Let i_n(u)=location_n(B_n(u)). Re-addressing by u=R_m(j) yields z_n(i_n(R_m(j)))=2 z_m(j) in even width, and 2 z_m(j)+1/2-lastbit(R_m(j)) in odd width.

## Exact placement without a large ring

Let R_h(a,b) count t with 0<=t<a and reverse_h(t)<b. This is computed using fixed-state bit comparisons.

For n=2m, H=2^m and u<H/2, put B=reverse_m(u). Then

i_n(u)=uH-u(u-1)/2+B-R_m(B,u+1).

For n=2m-1, h=m-1, H0=2^h, A=floor(u/2), c=u mod 2, B=reverse_h(A), and u<2^(m-1),

i_n(u)=2AH0-A(A-1)+c(H0-A)+B-R_h(B,A+1).

For upper-half prefixes use i_n(u)=2^n-1-i_n(2^m-1-u). n=1 is the base case i_1(u)=u.

The scalar formula passed every palindrome address at n=2,...,20 (4,090 cases), plus independent full-rank comparisons at 40 scalar cases through n=1024.

## Walsh parity and energy

Let f_n(i)=z_n(i), sigma(i)=2^n-1-i, E=(f+f o sigma)/2, O=(f-f o sigma)/2. E is exactly f off the palindrome support and zero on it; O is exactly f on the palindrome support and zero elsewhere. Walsh characters satisfy chi_s(sigma i)=(-1)^weight(s) chi_s(i). Therefore E has only even-degree Walsh support and O has only odd-degree support.

The odd-energy fraction is 2^(1-n/2) for even n and (4h+1)/((2h+1)2^h) for n=2h+1. Both formulas passed exact-fraction checks for every n=2,...,20. The even-width fraction halves at each +2 width step; the odd-width fraction has the displayed rational prefactor and only approaches a factor of 1/2.

## Compressed carrier

Write chi_j(u)=(-1)^u_j. In the natural prefix coordinate:

z_(2m)(B_(2m)(u))=-sum_j chi_j(u),
z_(2m-1)(B_(2m-1)(u))=-sum_(j<m) chi_j(u)-(1/2)chi_m(u).

Thus the compressed carrier has Walsh degree one only. The higher odd degrees in the full ring-address spectrum come from its embedding i_n(u). An arbitrary address permutation does not preserve Walsh degree.

The exact full-address spectral formula is

Ohat_n(s)=2^(-n) sum_u z_n(B_n(u)) (-1)^(s dot i_n(u)).

This is the correct bridge for a future spectral nesting theorem, rather than assuming an unchanged smaller Walsh spectrum.

## Operator qualification

Complement on a parent palindrome sends u to complement(u). After the smaller-ring re-addressing its action is R_m^(-1) C_m R_m, not generally R_m^(-1) P_m R_m. These differ once half-width m reaches 3, though the waveform re-addressing remains exact.

## Provenance

The main audit source and predictions were sealed before execution and checked afterward. The exact scalar placement formula was derived after that run and tested separately; it is not claimed to be part of the initial seal. The unprovided /tmp/r4 files and their reported seal were not independently verified. No cusp/smoothness claim was tested in this audit.
