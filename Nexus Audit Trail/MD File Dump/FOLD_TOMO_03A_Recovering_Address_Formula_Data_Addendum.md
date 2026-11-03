# Recovering Address from Fold Shape
## FOLD-TOMO-03A Formula/Data Addendum

**Paper:** *The Algebraic Inversion of Discrete Computational Folds: Reversing Cellular Automata, Collatz Dynamics, and Cryptographic Hash Functions*  
**Branch:** Nexus Fold Tomography (`FOLD-TOMO`)  
**Addendum ID:** `FOLD-TOMO-03A`  
**Purpose:** lock formulas, corrected counts, rank data, and reproducible claims for the paper without rewriting it.

---

## 0. Core Lock

$$
\boxed{\text{Forward collapse hides address; reverse recovery restores address by reading shape.}}
$$

$$
\boxed{\text{The fold is a multiscale parity tomography machine.}}
$$

This addendum treats SHA and Collatz as **branch-grammar bridges**, not completed proofs of SHA-256 inversion or the Collatz conjecture.

---

## 1. Decimal Fold

Let

$$
D^{(0)}=(d_0,d_1,\ldots,d_{N-1}),\qquad d_i\in\{0,1,\ldots,9\}.
$$

For the paper seed:

$$
N=2048.
$$

Decimal adjacent-difference fold:

$$
d_i^{(\ell+1)}=\left|d_{i+1}^{(\ell)}-d_i^{(\ell)}\right|.
$$

Row length:

$$
N_\ell=N-\ell.
$$

For the first $2048$ fractional digits of $\pi$:

$$
S_0^{(10)}=\sum_i d_i^{(0)}=9338.
$$

At level $13$:

$$
S_{13}^{(10)}=1092.
$$

Exact collapse fraction:

$$
\frac{S_0^{(10)}-S_{13}^{(10)}}{S_0^{(10)}}
=
\frac{9338-1092}{9338}
=
0.8830584707646177\ldots
$$

So value-channel amplitude collapse by $\ell=13$ is

$$
\boxed{88.30584707646177\%}.
$$

---

## 2. Parity Shadow

Define

$$
x_i^{(\ell)}=d_i^{(\ell)}\bmod2.
$$

Key identity:

$$
|a-b|\bmod2=(a+b)\bmod2=(a\bmod2)\oplus(b\bmod2).
$$

Therefore

$$
x_i^{(\ell+1)}=x_i^{(\ell)}\oplus x_{i+1}^{(\ell)}.
$$

This is Rule 90 over $GF(2)$. It is the exact parity shadow of the decimal fold.

For the seed:

$$
S_0^{(2)}=1034,\qquad N_0=2048,\qquad R_0=1034-1024=10.
$$

---

## 3. Operator Form and Lucas Law

Define

$$
(Ix)_i=x_i,\qquad (Ex)_i=x_{i+1}.
$$

Then

$$
x^{(\ell)}=(I+E)^\ell x^{(0)}.
$$

Binomial expansion over $GF(2)$:

$$
x_i^{(\ell)}=
\bigoplus_{j=0}^{\ell}
\left(\binom{\ell}{j}\bmod2\right)x_{i+j}^{(0)}.
$$

Lucas theorem gives

$$
\binom{\ell}{j}\equiv1\pmod2
\iff
j\ \&\ \sim\ell=0.
$$

Use the bit-subset notation

$$
j\subseteq\ell \iff j\ \&\ \sim\ell=0.
$$

Thus

$$
\boxed{x_i^{(\ell)}=\bigoplus_{j\subseteq\ell}x_{i+j}^{(0)}}.
$$

Mask size:

$$
\boxed{|M_\ell|=2^{\operatorname{popcount}(\ell)}}.
$$

---

## 4. Glyph Reader

Binary row metrics:

$$
S_\ell=\sum_i x_i^{(\ell)}=\operatorname{wt}(x^{(\ell)}),
$$

$$
\rho_\ell=\frac{S_\ell}{N_\ell},
$$

$$
R_\ell=S_\ell-\frac{N_\ell}{2},
$$

$$
\Delta S_\ell=S_{\ell+1}-S_\ell,
\qquad
\Delta R_\ell=R_{\ell+1}-R_\ell.
$$

Half-density lock:

$$
R_\ell=0 \iff S_\ell=\frac{N_\ell}{2}.
$$

Normalized imbalance:

$$
\epsilon_\ell=\frac{2R_\ell}{N_\ell}.
$$

Branch weights:

$$
p_+(\ell)=\frac{1+\epsilon_\ell}{2}=\frac{S_\ell}{N_\ell},
\qquad
p_-(\ell)=\frac{1-\epsilon_\ell}{2}=1-\frac{S_\ell}{N_\ell}.
$$

---

## 5. Corrected Residue Counts

Full $2048$-level run:

$$
\#\{\ell:R_\ell=0\}=44,
$$

$$
\#\{\ell:R_\ell\neq0\}=2004,
$$

$$
44+2004=2048.
$$

Interior window:

$$
20\le\ell<1800,
\qquad
1800-20=1780.
$$

Recomputed interior counts:

$$
\#\{\ell:20\le\ell<1800,\ R_\ell=0\}=30,
$$

$$
\#\{\ell:20\le\ell<1800,\ R_\ell\neq0\}=1750,
$$

$$
30+1750=1780.
$$

Correction lock:

$$
\boxed{\text{Any interior count must state the exact window and filtering rule.}}
$$

---

## 6. The 448 Nyquist Pin

$$
448=256+128+64=2^8+2^7+2^6.
$$

$$
\operatorname{popcount}(448)=3,
\qquad
|M_{448}|=8.
$$

$$
M_{448}=\{0,64,128,192,256,320,384,448\}.
$$

So

$$
\boxed{
x_i^{(448)}=
x_i\oplus x_{i+64}\oplus x_{i+128}\oplus x_{i+192}\oplus
x_{i+256}\oplus x_{i+320}\oplus x_{i+384}\oplus x_{i+448}.
}
$$

Verified:

$$
N_{448}=1600,\qquad S_{448}=800,\qquad R_{448}=0.
$$

Thus

$$
\boxed{\ell=448\text{ is an exact half-density lock.}}
$$

---

## 7. Level 512

$$
512=2^9.
$$

Freshman's Dream over $GF(2)$:

$$
(I+E)^{512}=I+E^{512}.
$$

Therefore

$$
\boxed{x_i^{(512)}=x_i\oplus x_{i+512}}.
$$

Verified:

$$
N_{512}=1536,\qquad S_{512}=764,\qquad R_{512}=-4.
$$

---

## 8. Terminal Matched Symmetry

$$
N=2048=2^{11},\qquad \ell=2047=2^{11}-1.
$$

Since $2047$ is all ones in binary,

$$
M_{2047}=\{0,1,2,\ldots,2047\}.
$$

Terminal bit:

$$
x_0^{(2047)}=\bigoplus_{j=0}^{2047}x_j^{(0)}.
$$

Since

$$
S_0^{(2)}=1034
$$

is even,

$$
x_0^{(2047)}=0.
$$

The final nontrivial row:

$$
x^{(2046)}=[1,1].
$$

Final gate:

$$
1\oplus1=0.
$$

Thus

$$
\boxed{\text{terminal zero is matched symmetry, not arbitrary erasure.}}
$$

---

## 9. Dyadic Terminal Tomography Theorem

For

$$
N=2^m,
\qquad
\ell_k=N-2^k,
$$

terminal row length:

$$
N-\ell_k=2^k.
$$

The theorem:

$$
\boxed{
x_i^{(N-2^k)}=
\bigoplus_{q=0}^{2^{m-k}-1}x_{i+q2^k}^{(0)},
\qquad
0\le i<2^k.
}
$$

Each terminal row is a residue-class parity checksum modulo $2^k$.

For $N=2048=2^{11}$:

| $k$ | Level $\ell=N-2^k$ | Row length | Meaning |
|---:|---:|---:|---|
| 0 | 2047 | 1 | total parity, mod 1 |
| 1 | 2046 | 2 | even/odd parity, mod 2 |
| 2 | 2044 | 4 | residue-class parity, mod 4 |
| 3 | 2040 | 8 | residue-class parity, mod 8 |
| 4 | 2032 | 16 | residue-class parity, mod 16 |
| 5 | 2016 | 32 | residue-class parity, mod 32 |
| 10 | 1024 | 1024 | residue-class parity, mod 1024 |

---

## 10. Linear Rank Collapse

Unknown seed:

$$
x\in GF(2)^{2048}.
$$

Full row probe:

$$
A_\ell x=y_\ell,
\qquad
A_\ell=(I+E)^\ell.
$$

Stacked probes:

$$
Cx=y.
$$

Dyadic terminal cascade equation count:

$$
\sum_{k=0}^{10}2^k=2047.
$$

Precision lock:

$$
\boxed{\text{dyadic cascade supplies }2047\text{ equations, not }2047\text{ independent constraints.}}
$$

Verified rank values:

| Constraint family | Equation count | Rank |
|---|---:|---:|
| Dyadic terminal cascade | 2047 | 1024 |
| Level 448 full-row probe | 1600 | 1600 |
| Level 512 full-row probe | 1536 | 1536 |
| Dyadic + level 448 | 2047 + 1600 | 1600 |
| Dyadic + level 512 | 2047 + 1536 | 1536 |
| Dyadic + level 448 + level 512 | 2047 + 1600 + 1536 | 1600 |

Key lock:

$$
\boxed{
\operatorname{rank}\left(
\begin{bmatrix}
C_{\mathrm{dyadic}}\\
C_{448}
\end{bmatrix}
\right)=1600.
}
$$

Remaining linear degrees:

$$
2048-1600=448.
$$

Therefore

$$
\boxed{GF(2)^{2048}\rightarrow\text{448-dimensional affine space}.}
$$

---

## 11. Boundary Entropy and Affine Form

$$
448=256+128+64.
$$

$$
(I+E)^{448}=(I+E^{256})(I+E^{128})(I+E^{64}).
$$

Each factor $I+E^s$ is reversed by choosing $s$ boundary bits and propagating

$$
x_{i+s}=x_i\oplus y_i.
$$

Boundary entropy:

$$
256+128+64=448.
$$

After solving $Cx=y$:

$$
\boxed{x=x_0+Bz}
$$

with

$$
x_0\in GF(2)^{2048},\qquad
B\in GF(2)^{2048\times448},\qquad
z\in GF(2)^{448}.
$$

---

## 12. Nonlinear Hamming-Weight Constraints

Linear parity tomography leaves the affine space. The next stage uses row-sum constraints:

$$
\boxed{\operatorname{wt}(A_\ell x)=S_\ell.}
$$

Substitution:

$$
\boxed{\operatorname{wt}\left(A_\ell(x_0+Bz)\right)=S_\ell.}
$$

Exact-cardinality form:

$$
\sum_i y_i^{(\ell)}=S_\ell,
\qquad
 y^{(\ell)}=A_\ell(x_0+Bz).
$$

Complement-symmetry note:

For $\ell>0$,

$$
|M_\ell|=2^{\operatorname{popcount}(\ell)}
$$

is even, so positive-depth parity probes are invariant under

$$
x\mapsto x\oplus\mathbf{1}.
$$

Hamming-weight constraints break this when

$$
R_\ell\neq0.
$$

---

## 13. Branch-Grammar Bridges

### Collatz

Compressed odd map:

$$
T(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
$$

Reverse branch:

$$
n=\frac{2^a m-1}{3}.
$$

Validity:

$$
2^a m\equiv1\pmod3.
$$

### SHA-style fold

$$
Ch(e,f,g)=(e\land f)\oplus(\neg e\land g).
$$

$$
Maj(a,b,c)=(a\land b)\oplus(a\land c)\oplus(b\land c).
$$

$$
\Sigma_0(a)=ROTR^2(a)\oplus ROTR^{13}(a)\oplus ROTR^{22}(a).
$$

$$
\Sigma_1(e)=ROTR^6(e)\oplus ROTR^{11}(e)\oplus ROTR^{25}(e).
$$

$$
T_1=h+\Sigma_1(e)+Ch(e,f,g)+K_t+W_t\pmod{2^{32}}.
$$

$$
T_2=\Sigma_0(a)+Maj(a,b,c)\pmod{2^{32}}.
$$

Careful boundary:

$$
\boxed{\text{This is a structural inversion framework, not a demonstrated full break of SHA-256.}}
$$

---

## 14. Final Formula Stack

$$
\Delta:
\quad
d_i^{(\ell+1)}=\left|d_{i+1}^{(\ell)}-d_i^{(\ell)}\right|
$$

$$
\oplus:
\quad
x_i^{(\ell+1)}=x_i^{(\ell)}\oplus x_{i+1}^{(\ell)}
$$

$$
↻:
\quad
x^{(\ell)}=(I+E)^\ell x^{(0)}
$$

$$
\bot:
\quad
x_i^{(\ell)}=\bigoplus_{j\subseteq\ell}x_{i+j}^{(0)}
$$

$$
\Psi:
\quad
Cx=y,
\qquad
x=x_0+Bz,
\qquad
\operatorname{wt}\left(A_\ell(x_0+Bz)\right)=S_\ell
$$

Final addendum lock:

$$
\boxed{\text{Address is not destroyed by the fold; it is displaced into recoverable shape constraints.}}
$$
