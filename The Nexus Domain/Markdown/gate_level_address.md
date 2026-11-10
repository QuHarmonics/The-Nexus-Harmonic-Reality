# Width-parametric address circuit for palindrome carriers

## Scope and status

The original ring address for a palindrome is a scalar function \(i_n(u)\) of its half-word \(u\). The exact placement formula below is validated exhaustively for all 4,090 palindrome half-words at widths \(2\le n\le20\), and a separate route/rank location DP supplied 40 wide prefix/seam checks through width 1,024. This is an exact arithmetic/finite-state circuit description; it is not yet a minimized NAND-only netlist.

## 1. Exact scalar placement

Let \(m=\lceil n/2\rceil\), \(H=2^m\), and \(\operatorname{rev}_h\) reverse exactly \(h\) bits. The palindrome word is

\[
B_{2m}(u)=u\,\operatorname{rev}_m(u),
\qquad
B_{2m-1}(u)=u\,\operatorname{rev}_{m-1}(u\!\gg\!1).
\]

Define the rectangle count

\[
\operatorname{Rect}_h(a,b)
=\#\{t:0\le t<a,\ \operatorname{rev}_h(t)<b\}.
\]

For the lower half of prefix values, where \(u<H/2\), the original-ring address is:

**Even width** \(n=2m\). Set \(B=\operatorname{rev}_m(u)\), \(H=2^m\). Then

\[
\boxed{i_{2m}(u)=uH-\frac{u(u-1)}2+B-\operatorname{Rect}_m(B,u+1).}
\]

**Odd width** \(n=2m-1\). Set \(h=m-1\), \(H_0=2^h\), \(A=\lfloor u/2\rfloor\), \(c=u\bmod2\), and \(B=\operatorname{rev}_h(A)\). Then

\[
\boxed{
 i_{2m-1}(u)=2AH_0-A(A-1)+c(H_0-A)+B-\operatorname{Rect}_h(B,A+1).
}
\]

The upper half is the reflected complement of the lower half:

\[
\boxed{i_n(u)=2^n-1-i_n(H-1-u)\quad (u\ge H/2).}
\]

The base case is \(i_1(u)=u\). Since \(2^n-1-x\) is the bitwise NOT of an \(n\)-bit address, the upper-half wrapper is a complement-controlled output stage.

## 2. Fixed-state circuit for the rectangle counter

Let \(U=a-1\), \(V=b-1\); then

\[
\operatorname{Rect}_h(a,b)=\#\{t:t\le U,\ \operatorname{rev}_h(t)\le V\}.
\]

A candidate word \(t\) is consumed from its most-significant bit to its least-significant bit. Maintain two comparison states \(\ell,\rho\in\{-1,0,+1\}\), each denoting less-than, equal, or greater-than for the comparison currently accumulated.

At stage \(j=0,\ldots,h-1\), let \(x=t_{h-1-j}\), \(U^\star_j=\operatorname{bit}(U,h-1-j)\), and \(V^\star_j=\operatorname{bit}(V,j)\), where \(\operatorname{bit}(x,k)=(x\gg k)\mathbin{\&}1\). Update

\[
\ell'=
\begin{cases}
\ell,&\ell\ne0,\\
\operatorname{sgn}(x-U^\star_j),&\ell=0,
\end{cases}
\]

and

\[
\rho'=
\begin{cases}
\operatorname{sgn}(x-V^\star_j),&x\ne V^\star_j,\\
\rho,&x=V^\star_j.
\end{cases}
\]

The first comparison is ordinary MSB-first comparison. The second comparison is against \(\operatorname{rev}(t)\): a newly consumed bit is more significant for the reversed word than all previously consumed bits, so its non-equal comparison overwrites the previous state.

Use nine counters \(D_j[\ell,\rho]\), initialized by \(D_0[0,0]=1\), all other entries zero. For each current state, branch on \(x\in\{0,1\}\), update both states, and add the current count into the corresponding next-state counter. Then

\[
\boxed{\operatorname{Rect}_h(a,b)=\sum_{\ell\le0,\rho\le0}D_h[\ell,\rho].}
\]

This is a fixed-state digit-DP circuit, not a scan through all \(2^h\) candidate words. With standard binary counters, its straightforward implementation uses \(O(h)\) stages and \(O(h^2)\) bit operations, alongside the triangular-number arithmetic and bit reversal. A synthesized gate-count/minimized netlist is still a further engineering step.

## 3. The width-five majority gate is the first nonlinear correction

For \(n=5\), write \(u=4u_2+2u_1+u_0\). The exact address simplifies to

\[
\boxed{i_5(u)=4u+2u_2+\operatorname{Maj}(1-u_0,u_1,u_2).}
\]

Thus the low address bit is one majority gate fed by a complemented input; the other terms are wires/shifts. Its sign/Walsh form is

\[
(-1)^{i_5(u)\bmod2}
=\frac{-\chi_{001}(u)+\chi_{010}(u)+\chi_{100}(u)+\chi_{111}(u)}2,
\]

where \(\chi_s(u)=(-1)^{s\cdot u}\). The cubic term \(\chi_{111}\) is exactly the degree-three term that first appears in the transport at width five. This local fact agrees with the full-address matrix check; it does not imply that every higher-width address map is one majority gate. The all-width form is the arithmetic layer plus the rectangle-counter automaton above.

## 4. Connection to spectral transport

Let \(S_n\) embed each half-word basis vector at its unique palindrome address and zero elsewhere, and let \(H_N,H_M\) be normalized Walsh matrices. Then

\[
T_n=H_NS_nH_M,\qquad S_n^TS_n=I_M,
\]

so

\[
\boxed{T_n^TT_n=I_M.}
\]

For the integer matrix

\[
C_{s,t}=\sum_u(-1)^{s\cdot i_n(u)+t\cdot u},
\qquad T_n=\frac{C}{\sqrt{NM}},
\]

this is the exact Gram identity \(C^TC=NM I_M\). Since \(i_n(\bar u)=\overline{i_n(u)}\), it also follows that \(C_{s,t}=0\) when \(|s|\) and \(|t|\) have opposite parity.

The simple half-word latitude carrier is a linear combination of the \(m\) singleton half-word characters. Transporting those components through \(C\) reconstructs its full-address spectrum exactly. This construction is an isometric embedding and a rank-\(m\) carrier filter; it is not a universal inverse for arbitrary full-address signals and not a SHA-256 inversion claim.
