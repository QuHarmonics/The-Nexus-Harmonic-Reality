# Exact E/G position map

Use descending canonical representative offsets q. For L=2h, H=2^h and x=A H+B, define K=H-1-A. The source block start is D_K=K(K-1)/2+max(0,K-H/2); its size is s_K=K+1[K>=H/2]. Writing j=D_K+i, the middle-1 and middle-0 offsets are 2D_K+i and 2D_K+s_K+i. Thus the original triangular formulas hold when K<H/2.

Let R_h(u,v) count integers b with 0<=b<u and reverse_h(b)<v. This rectangle count is implemented by fixed-state mirrored-bit counting, not enumeration.

For arbitrary L-bit z=A H+B, define

Q_L(z)=binom(2H-1-A,2)+(H-1-A)+2(H-1-B)-A+R_h(B+1,A).

This is the descending canonical target offset of 0z1. Proof: the new high half is A and low half 2B+1. All odd low halves are allowed; an even low half 2b is allowed iff reverse_h(b)>=A. Above 2B+1 there are H-1-B odd lows and H-1-B-A+R_h(B+1,A) even lows. Add the target block start.

The requested branches obey q(G0)=Q_L(x), q(E0)=Q_L(x)+1, q(G1)=Q_L(P_L(x)). For palindromic x, q(E1)=Q_L(P_L(x))+1. For nonpalindromic x, q(E1)=j-s_L(x), where s_L(x)=max(0,K-H/2)+1[A<H/2 and reverse_h(A)>B]. This counts the larger canonical palindrome representatives omitted by one-padding.

The adjacency identities follow because 0z1 and 0z0 are adjacent canonical values whenever 0z0 is canonical. The nonpalindrome identity follows because padding preserves the reversal comparison but excludes palindrome representatives from the inherited block.

For target width n and M=2^(n-1), convert q to the physical canonical address by pos_n(q)=M for q=0, and M-1-q otherwise. The partner is at 2^n-1-pos_n(q). This explicitly implements the center swap.

Execution: all nine source widths 2,4,...,18 passed, covering 699,048 branch outputs, including every canonical target at width 20. Additional scalar comparisons at source widths 64,256,512 passed against an independent rank counter. The separately sealed audit source was checked before and after execution; the scalar convenience module is a derivative, not the sealed source.
