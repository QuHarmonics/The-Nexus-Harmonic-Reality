# NEXUS continuation: core homology, its action, and the all-n group proof

**Scope.** This note follows the marked graph construction for every integer \(n\ge3\). It separates (i) the marked graph's \(4n^2\)-dimensional residual after commuting squares and rotation triangles from (ii) the \((n-1)^3\) dependencies among core triangle boundaries. They are different homological quantities.

## 1. Repair to the submitted all-n automorphism proof

The asserted group identification is correct for the stated marked graph, but one step in the pasted proof is not: the quotient does **not** act faithfully on the three core classes as a dihedral group. The class index sees only the \(C_3\) rotation; slope \(-1\) fixes each class and supplies a separate commuting involution. The correct quotient is

\[
G_n/N\cong C_3\times C_2\cong C_6\cong\mu_6,
\]

not \(D_3\cong S_3\). The claim is repaired by classifying the allowed label maps directly.

### The marked graph and its intrinsic roles

Write the three core classes as \(C_i=\{c_{i,x}:x\in\mathbb Z_n\}\), \(i\in\mathbb Z/3\). The core induces \(K_{n,n,n}\). There are leaves \(\ell_{i,x}\), each joined to \(c_{i,x}\) and all of \(C_{i+1}\). For each face

\[
f=(x_0,x_1,x_2),\qquad x_0+x_1+x_2\in\{0,1\}\pmod n,
\]

there is a marker triangle \(m_{f,0},m_{f,1},m_{f,2}\), with \(m_{f,i}\) joined to \(c_{i,x_i}\). For \(n\ge3\), the three vertex roles have distinct degrees: core \(5n+1\), leaf \(n+1\), marker \(3\). Thus every automorphism preserves these roles.

The core's complete-tripartite structure identifies its three classes, initially up to a permutation. A leaf has exactly one neighbour in \(C_i\), namely \(c_{i,x}\), and all \(n\) neighbours in \(C_{i+1}\). Hence an induced class permutation \(p\) must satisfy \(p(i+1)=p(i)+1\); only class rotations are allowed. Write the induced label bijections as \(f_i:\mathbb Z_n\to\mathbb Z_n\). Marker-triangle incidence says exactly that

\[
x_0+x_1+x_2\in\{0,1\}
\iff
f_0(x_0)+f_1(x_1)+f_2(x_2)\in\{0,1\}.
\tag{1}
\]

### The face relation forces one common affine slope

Fix \(x,y\). The two labels \(z=-x-y\) and \(z+1\) are exactly the two choices completing a marked face. By (1), \(f_2\) maps every adjacent pair \(\{z,z+1\}\) to an adjacent pair. The same argument applies to each \(f_i\). Since each is bijective, it is an automorphism of the cycle on \(\mathbb Z_n\); for every \(n\ge3\),

\[
f_i(x)=s_i x+a_i,\qquad s_i\in\{+1,-1\}.
\]

The signs must agree. If \(s_i\ne s_j\), replace a face's labels by \(x_i+d,x_j-d\), leaving the third coordinate fixed. The source sum stays fixed, but the target sum moves through a coset of \(2\mathbb Z_n\). For odd \(n\), that coset is all of \(\mathbb Z_n\); for even \(n\ge4\), it has \(n/2\ge2\) elements of one parity, while \(\{0,1\}\) contains only one element of either parity. Either case contradicts the requirement that every target sum lie in \(\{0,1\}\). Thus \(s_0=s_1=s_2=s\).

Let \(A=a_0+a_1+a_2\). Face sums \(0,1\) map to \(A,A+s\); these must be exactly \(\{0,1\}\), so

\[
A=\frac{1-s}{2}\pmod n.
\]

Therefore every automorphism has the form

\[
\boxed{g(k,s,a):c_{i,x}\mapsto c_{i+k,sx+a_i},\quad
 a_0+a_1+a_2\equiv(1-s)/2\pmod n.}
\tag{2}
\]

The same formula uniquely determines the leaf and marker images. Conversely, every map (2) preserves the core edges, leaf incidence, both face layers and each marked triangle. There are three choices of \(k\), two choices of \(s\), and \(n^2\) offset triples for each allowed sum. Hence

\[
|\operatorname{Aut}(\Gamma_n)|=6n^2.
\]

### Splitting and the Eisenstein module

The map \(g(k,s,a)\mapsto(k,s)\) is a homomorphism onto \(C_3\times C_2\), with kernel

\[
N=\{(a_0,a_1,a_2):a_0+a_1+a_2=0\}\cong (\mathbb Z_n)^2.
\]

Choose \(\rho=g(1,-1,(1,0,0))\). It projects to the order-six element \((1,-1)\); direct composition gives \(\rho^6=1\), so \(\langle\rho\rangle\cong C_6\) is a section. Conjugation on \(N\) is class rotation \(R\) combined with sign inversion. Since \(R^2+R+I=0\), the action makes \(N\) a rank-one module over \(\mathbb Z[\omega]/n\): take \(\omega\cdot v=Rv\), with \(v=(1,-1,0)\); \(v,Rv\) form a \(\mathbb Z_n\)-basis and \(v+Rv+R^2v=0\). The section generator acts as \(-R\), corresponding to the unit \(-\omega\) of order six. Thus

\[
\boxed{\operatorname{Aut}(\Gamma_n)\cong
(\mathbb Z[\omega]/n)\rtimes\mu_6,\qquad n\ge3.}
\]

This proves the identification from the graph's incidence rules; it does not rely on extrapolating finite group-order checks.

## 2. Integral core homology and an explicit basis

Let \(D_i\) be the discrete set of \(n\) vertices in core class \(C_i\). The filled core is the simplicial join

\[
K_{n,n,n}=D_0*D_1*D_2.
\]

For each class, let

\[
U_i=\widetilde H_0(D_i;\mathbb Z)
=\left\{(z_x)\in\mathbb Z^n:\sum_xz_x=0\right\}\cong\mathbb Z^{n-1}.
\]

The join homology formula (or the augmented chain complex of the join) gives

\[
\widetilde H_1(K_{n,n,n};\mathbb Z)=0,\qquad
H_2(K_{n,n,n};\mathbb Z)\cong U_0\otimes U_1\otimes U_2
\cong\mathbb Z^{(n-1)^3}.
\tag{3}
\]

There is no torsion term: each \(U_i\) is free abelian. This is an integral theorem for all \(n\), not a rank fit.

Choose a base label \(*\) in each class and put \(u_{i,a}=e_{i,a}-e_{i,*}\), for \(a\ne *\). The explicit generators are

\[
Z_{abc}=([a]-[*])*([b]-[*])*([c]-[*])
=\sum_{x\in\{a,*\},\ y\in\{b,*\},\ z\in\{c,*\}}
\epsilon_x\epsilon_y\epsilon_z[x,y,z],
\]

where \(\epsilon_a=+1\) and \(\epsilon_*= -1\). Each is a signed sum of eight core triangles. Every edge in its boundary occurs twice with opposite signs, so \(\partial Z_{abc}=0\). They are independent because the all-nonbase triangle \([a,b,c]\) occurs only in \(Z_{abc}\). There are exactly \((n-1)^3\) of them, the rank in (3); since the core has no 3-simplices, these cycles form an integral basis for \(H_2\).

## 3. Transporting the group action to the generators

For \(g=g(k,s,a)\), each zero-sum factor is carried by

\[
g(u_{i,x})=
 e_{i+k,sx+a_i}-e_{i+k,s*+a_i}\in U_{i+k}.
\tag{4}
\]

Writing (4) in the \(u\)-basis gives an integer matrix \(A_i\) on the corresponding factor. The action on (3) applies the three factor maps and cyclically permutes the factors by \(k\). This is the explicit generator action; no choice of a homology basis needs to be guessed from numerical matrices.

For an affine label map define

\[
F(s,b)=\#\{x\in\mathbb Z_n:sx+b\equiv x\pmod n\}.
\]

The full permutation space \(\mathbb Q^n\) has trace \(F(s,b)\); its trivial line has trace one. Therefore the trace on the zero-sum factor is exactly \(F(s,b)-1\). If \(k=0\), the factors remain separate and traces multiply:

\[
\boxed{\chi_{H_2^{\rm core}}(g)=\prod_{i=0}^2(F(s,a_i)-1),\quad k=0.}
\tag{5}
\]

If \(k\ne0\), the tensor factors cycle. The trace of a cyclic tensor permutation is the trace of the composite map around that cycle. Its offset is

\[
b=\begin{cases}
 a_0+s a_1+a_2,&k=1,\\
 a_0+s a_2+a_1,&k=2,
\end{cases}
\]

so

\[
\boxed{\chi_{H_2^{\rm core}}(g)=F(s,b)-1,\quad k=1,2.}
\tag{6}
\]

The fixed-label count itself is elementary:

\[
F(+1,b)=\begin{cases}n,&b=0,\\0,&b\ne0,\end{cases}
\qquad
F(-1,b)=\begin{cases}\gcd(2,n),&\gcd(2,n)\mid b,\\0,&\text{otherwise.}\end{cases}
\tag{7}
\]

Thus the parity split follows from solving \(2x\equiv b\pmod n\).

## 4. The alternating trace and the separate residual

For any finite group element acting on the triangle-filled core, equivariant Euler–Poincaré gives

\[
\chi_{C_0}(g)-\chi_{C_1}(g)+\chi_{C_2}(g)
=\chi_{H_0}(g)-\chi_{H_1}(g)+\chi_{H_2}(g).
\]

The core is connected and \(H_1(K_{n,n,n})=0\), so

\[
\boxed{\chi_{H_2^{\rm core}}(g)=
\chi_{C_2}(g)-\chi_{C_1}(g)+\chi_{C_0}(g)-1.}
\tag{8}
\]

Equations (5)–(7) calculate the left-hand side from the generator action; fixed-vertex, signed-edge and signed-triangle counts calculate the right-hand side from the chain action. Their equality is the character-level consistency check used in the scaled ledger.

Now let \(X\) be the commuting-square complex and \(Y\) the complex after adjoining rotation triangles. Under the established equivariant trace map \(J:H_1(X;\mathbb Q)\to H_1(\Gamma_n;\mathbb Q)\), the connecting map for the newly attached triangle cells is the graph-triangle boundary map. Consequently the relative long exact sequence gives

\[
0\to H_2(X;\mathbb Q)\to H_2(Y;\mathbb Q)\to H_2(K_{n,n,n};\mathbb Q)\to0.
\]

Over \(\mathbb Q\), this sequence splits as a representation (not necessarily canonically), hence

\[
\boxed{H_2(Y;\mathbb Q)\cong H_2(X;\mathbb Q)\oplus H_2(K_{n,n,n};\mathbb Q).}
\tag{9}
\]

The core therefore adds exactly \((n-1)^3\) dependencies, with the channel-by-channel increment given by the character of (5)–(7).

**Keep this separate from the marked-face residual:** the \(4n^2\) directions remaining after squares plus rotation triangles are a first-homology/deficiency term arising two per marked face. The \((n-1)^3\) term is second-homology redundancy from the tripartite core. Equation (9) relates the old and new second homologies; it does not identify the \(4n^2\) residual with core homology.

## 5. Exact finite regression

`verify_nexus_core_homology.py` reconstructs the marked graph from the incidence rules and, for each \(n=3,\ldots,8\):

- enumerates all \(6n^2\) maps in (2);
- verifies every map is a bijection preserving every graph edge;
- constructs all \((n-1)^3\) displayed core cycles and checks their integral boundaries vanish;
- computes the tensor-action trace directly in the zero-sum basis and checks it equals (5)–(7) for every group element.

All checks pass. These are regression checks of the explicit action and trace formulas; the all-n conclusions follow from the incidence classification, join-homology theorem, and the character identities above—not from finite testing alone.
