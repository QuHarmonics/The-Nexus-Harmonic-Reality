# Exact character transport through palindrome addresses

Let n be full width, m=ceil(n/2), N=2^n, M=2^m, and i_n(u) the known palindrome address map. Define S f by (S f)(i_n(u))=f(u), zero elsewhere. If H_N and H_M are normalized real Walsh matrices, T=H_N S H_M is the exact spectral transport. Since S^T S=I and the Walsh matrices are orthogonal, T^T T=I. This is an embedding isometry, not a square inverse for arbitrary N-dimensional signals.

Integer audit matrix C_st=sum_u chi_s(i_n(u))*chi_t(u), so T=C/sqrt(NM) and C^T C=NM I.

Because i_n(complement(u))=complement(i_n(u)), changing variables u->complement(u) multiplies C_st by (-1)^(weight(s)+weight(t)). Thus C_st=0 whenever the two parities differ. Degree equality is not required.

First mixing example at n=5, s=00001:

chi_00001(i_5(u))=(-chi_001(u)+chi_010(u)+chi_100(u)+chi_111(u))/2.

This is exactly sign-majority(-chi_001,chi_010,chi_100). With u_j indexed from the LSB, the full address is i_5(u)=4u+2u_2+Maj(1-u_0,u_1,u_2). All eight inputs were checked; their addresses are 0,4,9,12,19,22,27,31.

For latitude, the compressed function Z=2z has only singleton Walsh terms: -2 per bit for even n, or -1 on the half-word LSB and -2 on other bits for odd n. Therefore the full carrier transform is the exact linear combination of the m singleton columns C[:,2^j] with those coefficients.

Writing those integer columns as A, A^T A=NM I. Hence the spectral carrier projector is A A^T/(NM). Apply it as b=A^T F/(NM), followed by A b; never materialize an N by N matrix. On the full ring latitude spectrum F, this removes the nonpalindromic body and returns the palindrome carrier exactly. This is a theorem about the specified latitude family, not arbitrary signals or SHA digests.

Audit: complete matrices at n=2,...,12 passed exact parity and Gram checks. Singleton carrier reconstruction at every n=2,...,20 passed. At n=20, ten columns reconstructed all 1,048,576 full-address coefficients, with 512,674 nonzero carrier coefficients. The implementation explicitly constructs those expanded columns; this is not a claim of ten-operation evaluation of a million coefficients.

The main source and predictions were sealed before execution. The explicit majority formula and factored projection were additional post-main-run checks and are recorded separately, not backdated into the main seal.
