# NEXUS §87 follow-through: inertia-orbit census

Date: 2026-10-10  
Status: exact finite enumerations plus an all-n stabilizer argument for the equality of the three ramified extensions. The proposed all-even-n stabilizer-count formulas below match every tested width but still require a symbolic orbit-family proof before they are called an all-n theorem.

## 1. The counting identity

Let a finite inertia group \(T\) act on oriented cells \(X\). For \(g\in T\), let \(\epsilon(g,x)\in\{\pm1\}\) be the orientation sign when \(gx=x\), and let \(\psi:T\to\mathbb C^\times\) be a one-dimensional character. The character inner product is

\[
 m_\psi(X)=\frac1{|T|}\sum_{g\in T}\overline{\psi(g)}\,\operatorname{tr}(g\mid X)
 =\frac1{|T|}\sum_{g\in T}\overline{\psi(g)}\sum_{x:gx=x}\epsilon(g,x).
\]

Group the second sum by \(T\)-orbits. If \(x\) has stabilizer \(H=T_x\), its orbit contributes

\[
\frac1{|H|}\sum_{h\in H}\overline{\psi(h)}\epsilon(h,x).
\]

Because both \(\psi|_H\) and \(\epsilon(\cdot,x)\) are one-dimensional characters, this is exactly 1 if they agree on all of \(H\), and 0 otherwise. Hence

\[
\boxed{m_\psi(X)=\#\{T\text{-orbits }[x]:\psi|_{T_x}=\epsilon(\cdot,x)|_{T_x}\}.}
\]

This is the orbit/stabilizer form of the user's §87 rule. It handles vertices and configurations with trivial orientation sign, and edges, moves and squares with the signed cell action.

## 2. Exact equality of the three 2-torsion/ramified extensions on these layers

For \(3\mid n\), the degree-two inertia group is \(T=N\rtimes C_3\). Its three extensions differ only by the factor \(\omega^{rk}\) on the class-rotation exponent \(k\in\{0,1,2\}\), while agreeing on the translations \(N\).

No element with \(k\ne0\) stabilizes any cell in the five layers used here:

- every graph edge has a class/role profile with period three under a nontrivial cyclic class rotation;
- consequently no such rotation fixes a two-vertex configuration or a graph edge;
- it cannot fix a move because the move contains one graph edge;
- it cannot fix a square because it would have to preserve a two-element set of graph edges, which would force either a fixed edge or a two-cycle of edges, both impossible when every edge's class profile has period three.

Therefore every cell stabilizer \(H\) lies in \(N\). The three extensions restrict identically to each \(H\), so their multiplicities are exactly equal on vertices, edges, configurations, moves and commuting squares. This is a structural result for the declared cell construction, not a numerical coincidence. The character multiplicities of \(H_2\) are then also equal because \(H_2\) is recovered by the same alternating-character calculation and \(D_\square\) has multiplicity 4 in each of these three channels.

The orbit enumeration checked the equal values at \(n=3,6,9,12\):

| \(n\) | vertices | edges | configurations \(C_0\) | moves \(C_1\) | squares \(C_2\) | \(A=C_1-C_0\) | \(D_\square\) | \(H_2=C_2-A+D\) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 2 | 6 | 93 | 442 | 490 | 349 | 4 | 145 |
| 6 | 2 | 6 | 294 | 1540 | 1957 | 1246 | 4 | 715 |
| 9 | 2 | 6 | 597 | 3286 | 4408 | 2689 | 4 | 1723 |
| 12 | 2 | 6 | 1014 | 5680 | 7819 | 4666 | 4 | 3157 |

The values for \(H_2\) match \(24n^2-25n+4\) at odd \(n\) and \(24n^2-25n+1\) at even \(n\) in these tests. The extension-equality statement is proved by the stabilizer argument above; the closed form for the common multiplicity remains to be proved by a symbolic census of the translation-stabilizer types.

## 3. The even-width 3a/3b result

Use \(T=N\rtimes\langle F\rangle\), \(|T|=2n^2\), with \(n\) even. The characters \(3a\) and \(3b\) agree on \(N\) and differ by a sign on the slope-reversing coset. Thus an orbit whose stabilizer contains a slope reversal can contribute to one extension, both, or neither according to the exact restriction of the translation character and the orientation sign. The mod-4 effect occurs because for a half-width translation

\[
h=\frac n2(e_0,e_1,e_2),\quad e_i\in\{0,1\},\quad e_0+e_1+e_2\equiv0\pmod2,
\]

the order-two character \(\theta(d)=(-1)^{d_0+d_1}\) gives

\[
\theta(h)=(-1)^{(n/2)(e_0+e_1)}.
\]

When \(n\equiv0\pmod4\), it is +1 on all of \(N[2]\); when \(n\equiv2\pmod4\), it is nontrivial on some of \(N[2]\). This accounts for the location of the mod-4 branch in stabilizers containing order-two translations. It does not, by itself, count every orbit family.

### Exact finite census: commuting-square orbit signatures

The script groups a square orbit by the signature

\[
(|H|,\ \#\{h\in H:s(h)=-1\},\ \#\{s=-1,\epsilon=+1\},\ \#\{s=-1,\epsilon=-1\}),
\]

where \(H\) is the inertia stabilizer. For even \(n=4,6,8,10,12,14,16\), the orbit counts are exactly as follows:

| Signature | Candidate count formula | Scope |
|---|---:|---|
| \((2,1,0,1)\) | \(9n(n-1)\) | verified at every tested even width |
| \((1,0,0,0)\) | \(\frac{153}{2}n^2+12n-36\) | verified at every tested even width |
| \((4,2,1,1)\) | 6 | verified at every tested even width |
| \((2,1,1,0)\) | 21 | verified at every tested even width |
| \((n,n/2,0,n/2)\) | \(\frac{3(n-2)}2\) | verified at every tested even width |
| \((2n,n,n/2,n/2)\) | 3 | verified at every tested even width |
| \((2,0,0,0)\) | 15 | verified at every tested even width |

The counts sum to the total number of inertia-orbits on commuting squares:

\[
\boxed{|T\backslash C_2|=\frac{171}{2}n^2+\frac92n+6.}
\]

The exact character-match counts by signature, also measured directly, are:

| Signature | Match in 3a | Match in 3b |
|---|---:|---:|
| \((1,0,0,0)\) | \(\frac{153}{2}n^2+12n-36\) | same |
| \((2,1,0,1)\), \(n\equiv0\pmod4\) | \(\frac{9n^2-12n}{2}\) | \(\frac{9n^2-6n}{2}\) |
| \((2,1,0,1)\), \(n\equiv2\pmod4\) | \(\frac{9n^2-12n+4}{2}\) | \(\frac{9n^2-6n-4}{2}\) |
| \((2,1,1,0)\) | 7 | 14 |
| \((4,2,1,1)\) | 0 | 4 if \(n\equiv2\pmod4\), otherwise 0 |
| \((n,n/2,0,n/2)\), \(n\equiv0\pmod4\) | \(n/4-1\) | \(n/4\) |
| \((n,n/2,0,n/2)\), \(n\equiv2\pmod4\) | \((n-2)/4\) | \((n-2)/4\) |
| \((2n,n,n/2,n/2)\) | 0 | 1 if \(n\equiv2\pmod4\), otherwise 0 |
| \((2,0,0,0)\) | 10 if \(n\equiv2\pmod4\), otherwise 0 | same |

Summing those contributions gives the commuting-square character multiplicities

\[
m_{3a}(C_2)=
\begin{cases}
81n^2+\frac{25n}{4}-30,&n\equiv0\pmod4,\\
81n^2+\frac{25n}{4}-\frac{35}{2},&n\equiv2\pmod4,
\end{cases}
\]

\[
m_{3b}(C_2)=
\begin{cases}
81n^2+\frac{37n}{4}-22,&n\equiv0\pmod4,\\
81n^2+\frac{37n}{4}-\frac{19}{2},&n\equiv2\pmod4.
\end{cases}
\]

Subtracting the two expressions gives the much simpler relation

\[
\boxed{m_{3a}(C_2)-m_{3b}(C_2)=-3n-8.}
\]

The displayed signature formulas are the compact pattern extracted from exact enumerations. Their symbolic proof still needs to derive each orbit-family count from the affine coordinate equations; the finite test does not alone establish that they hold for every even \(n\).

### Carry the census through the alternating chain calculation

For the verified even widths, the lower layers give the following recovered forms:

\[
\begin{array}{c|cc}
 & 3a & 3b\\\hline
V & 3 & 5\\
E & 8 & 11\\
C_0 & 9n^2+19n+\kappa_{0a} & 9n^2+19n+\kappa_{0b}\\
C_1 & 54n^2+64n-22 & 54n^2+64n-4
\end{array}
\]

where \((\kappa_{0a},\kappa_{0b})=(6,12)\) for \(n\equiv0\pmod4\) and \((-1,5)\) for \(n\equiv2\pmod4\). With \(m_{3a}(D_\square)=5\), \(m_{3b}(D_\square)=6\), and

\[
m_\psi(H_2^\square)=m_\psi(C_2)-m_\psi(C_1)+m_\psi(C_0)+m_\psi(D_\square),
\]

the formulas become

\[
m_{3a}(H_2^\square)=36n^2-\frac{155n}{4}+
\begin{cases}3,&n\equiv0\pmod4,\\\frac{17}{2},&n\equiv2\pmod4,\end{cases}
\]

\[
m_{3b}(H_2^\square)=36n^2-\frac{143n}{4}+
\begin{cases}0,&n\equiv0\pmod4,\\\frac{11}{2},&n\equiv2\pmod4.\end{cases}
\]

Thus the previously fitted formulas are now decomposed into explicit inertia-stabilizer contributions. The remaining proof obligation is localized: provide a parameterization/counting proof for the seven square-stabilizer signatures and the lower-layer orbit formulas, rather than perform another unconstrained polynomial fit.

## 4. Exact checks included

- 3a/3b all five layers at \(n=4,6,8,10,12,14,16\).
- The three 2c/2r extensions, all five layers at \(n=3,6,9,12\); all three agreed at every tested layer.
- Every orbit and character match was enumerated with integer indices and signs; no floating-point arithmetic is used in the counting.

The CSV outputs contain per-layer multiplicities and per-signature counts. The Python script constructs \(\Gamma_n\), applies the affine group action, tracks orientation signs, and applies the stabilizer-character test.
