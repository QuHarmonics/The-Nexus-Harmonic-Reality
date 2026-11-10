# NEXUS quadratic phase on the three-lane slide subgroup

Date: 2026-10-10  
Status: exact algebraic derivation; floating-point regression run at 12 moduli  
Script: `nexus_quadratic_slide_chirp.py`

## Result

The one-dimensional quadratic chirp extends naturally to the actual two-dimensional translation subgroup of the three-lane machine. Index a sum-zero slide by

\[
(x,y,-x-y)\in (\mathbb Z/n\mathbb Z)^3.
\]

This identifies the slide subgroup with \(N_n\cong(\mathbb Z/n\mathbb Z)^2\). Let

\[
Q(x,y)=x^2+xy+y^2,\qquad
u(x,y)=\exp\!\left(\frac{2\pi i}{n}Q(x,y)\right).
\]

Unlike the one-dimensional \(a j^2\) construction, this pattern is adapted to the lane rotation. In coordinates, the rotation is

\[
R(x,y)=(-x-y,x),
\]

and direct substitution gives \(Q(R(x,y))=Q(x,y)\). It is also invariant under inversion: \(Q(-x,-y)=Q(x,y)\). Thus the quadratic phase is invariant under the linear \(C_3\) rotation and \(C_2\) inversion actions on the slide subgroup.

## Translation turns into a frequency character

For shift \((r,s)\),

\[
Q(x+r,y+s)-Q(x,y)
=(2r+s)x+(r+2s)y+Q(r,s).
\]

Consequently,

\[
u(x+r,y+s)=\nu(x,y)\,
\exp\!\left(\frac{2\pi i}{n}Q(r,s)\right)
\chi_{(2r+s,\,r+2s)}(x,y),
\]

where \(\chi_{(a,b)}(x,y)=\exp(2\pi i(ax+by)/n)\). The exact address-to-frequency map is

\[
\begin{pmatrix}r\\s\end{pmatrix}\longmapsto
\begin{pmatrix}2&1\\1&2\end{pmatrix}
\begin{pmatrix}r\\s\end{pmatrix}\pmod n.
\]

Its determinant is \(3\). It is invertible modulo \(n\) precisely when \(3\nmid n\). This is the mechanism, not a visual analogy: a slide address becomes a character index through the polar form of the quadratic phase.

## Exact cyclic correlation

Define

\[
C(r,s)=\sum_{x,y\bmod n}\nu(x+r,y+s)\overline{\nu(x,y)}.
\]

Substitution gives

\[
C(r,s)=\omega^{Q(r,s)}
\left(\sum_x\omega^{(2r+s)x}\right)
\left(\sum_y\omega^{(r+2s)y}\right),
\qquad \omega=e^{2\pi i/n}.
\]

Each geometric sum is \(n\) if its coefficient vanishes modulo \(n\), and zero otherwise. Thus \(C(r,s)\) is nonzero exactly when

\[
2r+s\equiv0,\qquad r+2s\equiv0\pmod n.
\]

The integer matrix has Smith normal form \(\operatorname{diag}(1,3)\), so this kernel has size \(\gcd(3,n)\): one element if \(3\nmid n\), three if \(3\mid n\). When \(3\mid n\), its three elements are

\[
(r,s)=t(n/3,n/3),\qquad t=0,1,2.
\]

For those elements, \(Q(r,s)=3t^2(n/3)^2\equiv0\pmod n\), so the nonzero correlation is exactly \(n^2\), not just a complex value of that magnitude. Therefore

\[
C(r,s)=
\begin{cases}
n^2,&(r,s)=(0,0),\quad 3\nmid n,\\
n^2,&(r,s)=t(n/3,n/3),\quad 3\mid n,\\
0,&\text{otherwise.}
\end{cases}
\]

For \(3\nmid n\), all \(n^2\) translated phase patterns are mutually orthogonal. For \(3\mid n\), each pattern repeats under a three-element translation kernel, leaving \(n^2/3\) distinct patterns. This is a complete classification of the shift collisions for this construction.

## Fourier power

Let

\[
A_{p,q}=\sum_{x,y}\nu(x,y)\omega^{-px-qy}.
\]

The finite Wiener–Khinchin identity makes \(|A_{p,q}|^2\) the Fourier transform of \(C\). Hence

\[
|A_{p,q}|^2=
\begin{cases}
n^2,&3\nmid n,\text{ for every }(p,q),\\
3n^2,&3\mid n\text{ and }p+q\equiv0\pmod3,\\
0,&3\mid n\text{ and }p+q\not\equiv0\pmod3.
\end{cases}
\]

So the spectrum is perfectly flat whenever the modulus is coprime to three. When the modulus contains the ramified factor three, exactly one third of the frequency bins remain, each with power \(3n^2\). The total power is \(n^4\) in both cases, as Parseval requires.

## Regression test

The script directly computed all two-dimensional cyclic correlations and Fourier powers for

\[
n\in\{2,3,4,5,6,7,8,9,12,16,24,32\}.
\]

All 12 widths matched the formula. In particular, powers of two through 32 had a one-element correlation kernel and perfectly flat Fourier power. Widths divisible by three had exactly three correlated shift addresses and the predicted one-third Fourier support.

The script uses complex floating-point arrays as a regression check. The proof above uses exact modular congruences and finite character sums; it does not depend on the numerical tolerance.

## Why this connects to the NEXUS machine

- The phase is indexed by exactly the two coordinates of the sum-zero slide subgroup.
- Its quadratic form is invariant under the chosen three-lane rotation and under inversion, the linear parts associated with the \(C_3\times C_2\) quotient.
- Each slide turns the base chirp into the base chirp times a specific character; when \(3\nmid n\), the character index uniquely identifies the slide.
- At \(n=2\), the four translated patterns are four mutually orthogonal real sign vectors: the four-element translation witness is directly readable by correlation. At every \(n=2^b\), the same construction remains nondegenerate because \(3\nmid 2^b\).
- The exceptional factor is exactly three, matching the determinant of the polar map and the degeneracy locus of the Eisenstein norm form. This is a structural alignment; it does not, by itself, prove any additional SHA-256 property or the §84 token-depth conjecture.

## Scope boundaries

This is an exact construction on the translation subgroup and an exact phase/correlation result. It is not yet an optical implementation, a claim about actual diffuser angular response, or a mapping of SHA-256 carry traces into token-loop modules. The Talbot connection stays as a separate physical realization of mode-dependent quadratic propagation phase and fractional shifted-copy reconstruction. The common mechanism is the conversion between a quadratic phase and displacement/frequency readouts, not identity of the two systems.
