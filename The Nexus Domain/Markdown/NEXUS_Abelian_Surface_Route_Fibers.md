# The Abelian Surface: Route Fibers, Degree Slices, and Orbital Periods

**NEXUS working note — independent algebraic audit**  
**Status:** exact combinatorial results separated from physical interpretation and open parameter selection.

## Abstract

A route of length \(n\) over \(k\) primitive symbols is a word in the free monoid \(F_k\). Forgetting the order of its symbols maps the word to its exponent vector in the free commutative monoid \(\mathbb N^k\). The degree-\(n\) surface contains \(\binom{n+k-1}{k-1}\) exponent vectors, while the interior contains \(k^n\) words. The fibers are multinomial permutation orbits, and their sizes sum exactly to \(k^n\). An inside-only reciprocal-fiber sample provides an unbiased estimator of the number of surface points. Separately, grouping atomic orbital labels by Madelung degree \(d=n+\ell\), with radial node condition \(n_r=n-\ell-1\geq0\), gives paired degree-slice capacities \(2\lfloor(d+1)/2\rfloor^2\), provided the standard spin-included subshell capacity \(2(2\ell+1)\) is used. These counting identities are exact; by themselves they do not prove that the quotient is physically inert, derive atomic energy ordering, or force the generator count \(k=2\).

## 1. The route space and its surface

Let \(\Sigma_k=\{a_1,\ldots,a_k\}\) be a set of \(k\) primitive symbols. The interior route space at length \(n\) is the set of words

\[
W_{k,n}=\Sigma_k^n,\qquad |W_{k,n}|=k^n.
\]

Define the order-forgetting map

\[
\pi:W_{k,n}\to C_{k,n},\qquad
\pi(w)=(\alpha_1,\ldots,\alpha_k),
\]

where \(\alpha_i\) counts the occurrences of \(a_i\) in \(w\). Thus \(\alpha_i\geq0\) and \(\sum_i\alpha_i=n\). The surface is the degree-\(n\) slice

\[
C_{k,n}=\left\{\alpha\in\mathbb N^k:\sum_i\alpha_i=n\right\}.
\]

By stars and bars,

\[
\boxed{|C_{k,n}|=\binom{n+k-1}{k-1}.}
\]

Concatenation inside the route space becomes vector addition on the surface:

\[
\pi(uv)=\pi(u)+\pi(v).
\]

This is the canonical abelianization of the free monoid: it preserves symbol multiplicity and composition length while erasing order. It is universal among homomorphisms from \(F_k\) into commutative monoids, but it is not literally the only map one can define from \(F_k\).

**Interpretation.** The surface cannot distinguish routes that differ only by order. It can still carry commutative dynamics through vector addition. The theorem is loss of order-sensitive process under this quotient—not absence of all mathematics or all possible processes on the surface.

## 2. The fibers are permutation orbits

For an exponent vector \(\alpha=(\alpha_1,\ldots,\alpha_k)\), the fiber is

\[
\pi^{-1}(\alpha)=\{w:\pi(w)=\alpha\}.
\]

The symmetric group \(S_n\) acts on words by permuting positions. Each fiber is precisely one orbit of this action, with size

\[
\boxed{|\pi^{-1}(\alpha)|=\frac{n!}{\alpha_1!\cdots\alpha_k!}.}
\]

The orbit-stabilizer description makes the order loss exact: the quotient retains the multiplicities but identifies every positional arrangement with those same multiplicities.

Since the fibers partition \(W_{k,n}\),

\[
\boxed{\sum_{\alpha\in C_{k,n}}|\pi^{-1}(\alpha)|=k^n.}
\]

This identity is a theorem for every positive integer \(k\) and nonnegative integer \(n\), not merely a finite test result.

## 3. Measuring the surface from route samples

Draw a word \(W\) uniformly from \(W_{k,n}\), and let \(F(W)=|\pi^{-1}(\pi(W))|\) be its fiber size. Then

\[
\begin{aligned}
\mathbb E\!\left[\frac1{F(W)}\right]
&=\sum_{\alpha\in C_{k,n}}
\frac{|\pi^{-1}(\alpha)|}{k^n}\frac1{|\pi^{-1}(\alpha)|}\\
&=\frac{|C_{k,n}|}{k^n}.
\end{aligned}
\]

Therefore

\[
\boxed{k^n\,\mathbb E[1/F(W)]=\binom{n+k-1}{k-1}.}
\]

For \(m\) independent uniform route samples, the estimator

\[
\widehat C_{k,n}=\frac{k^n}{m}\sum_{j=1}^{m}\frac1{F(W_j)}
\]

is unbiased for the exact number of surface points. A finite sample is an estimate, not an exact count. Its variance can be substantial because rare words with small fibers contribute large reciprocal weights. This reciprocal-fiber mean is a valid inside-only estimator; it is **not uniquely the only possible statistic** that estimates the surface count.

### Exact checks

| Alphabet size \(k\) | Route length \(n\) | Interior \(k^n\) | Surface \(\binom{n+k-1}{k-1}\) | Sum of fiber sizes |
|---:|---:|---:|---:|---:|
| 2 | 8 | 256 | 9 | 256 |
| 3 | 6 | 729 | 28 | 729 |
| 4 | 8 | 65,536 | 165 | 65,536 |
| 3 | 9 | 19,683 | 55 | 19,683 |

The accompanying script also runs seeded 2,000-sample estimates so finite-sample deviations are visible rather than hidden.

## 4. Degree is a discrete radial coordinate

The quotient degree is

\[
\operatorname{deg}(\alpha)=\sum_i\alpha_i=n.
\]

If we choose the \(L^1\) grading as the radial coordinate, the degree-\(n\) slice is literally the discrete shell at radius \(n\) in the nonnegative lattice. Thus `LEN()` may be read as a radius under this specified metric/grading. This is exact once the grading is defined; the word “radius” does not supply a unique metric independently of that choice.

## 5. Atomic degree slices from \(n+\ell\)

Let the degree be the Madelung index

\[
d=n+\ell,
\]

where \(n\) is the principal quantum number and \(\ell\) the angular-momentum quantum number. Impose the radial-node admissibility condition

\[
n_r=n-\ell-1\geq0.
\]

Substituting \(n=d-\ell\),

\[
 d-2\ell-1\geq0
 \quad\Longleftrightarrow\quad
 0\leq\ell\leq\left\lfloor\frac{d-1}{2}\right\rfloor.
\]

The allowed angular-momentum values are \(\ell=0,1,\ldots,m-1\), where

\[
m=\left\lfloor\frac{d+1}{2}\right\rfloor.
\]

Using the standard spin-included subshell capacity \(2(2\ell+1)\), the total capacity at degree \(d\) is

\[
\begin{aligned}
C(d)&=\sum_{\ell=0}^{m-1}2(2\ell+1)\\
&=2m^2\\
&=\boxed{2\left\lfloor\frac{d+1}{2}\right\rfloor^2}.
\end{aligned}
\]

Hence the first ten degree-slice capacities are

\[
2,2,8,8,18,18,32,32,50,50.
\]

The repeated pair is exact because the floor term is unchanged between \(d=2m-1\) and \(d=2m\):

\[
C(2m-1)=C(2m)=2m^2.
\]

**Scope boundary.** The count follows from the degree grouping, the allowed quantum-number inequality, and the spin-included orbital capacity. The capacity rule \(2(2\ell+1)\) is an essential input; the derivation is not literally based on the inequality alone. And the counting result does not independently derive the physical energy ordering of orbitals. Madelung grouping is a useful ordering rule, not a universal exact law for every atom.

## 6. The nodeless member and its missing predecessor

A nodeless orbital has

\[
n_r=0\quad\Longleftrightarrow\quad \ell=n-1.
\]

Its degree is therefore

\[
d=n+\ell=2n-1,
\]

which is odd. So this nodeless member occurs only on odd degree slices.

Ask for its same-\(\ell\) predecessor at degree \(d-1\). That would require principal quantum number \(n-1\) with the same \(\ell=n-1\), giving

\[
n_r'=(n-1)-(n-1)-1=-1,
\]

which violates radial admissibility. The predecessor is not an allowed member of the quantum-number domain. This is the exact combinatorial “no way home” result for the chosen same-\(\ell\) relation.

It identifies a structural boundary. By itself it does not prove why a real electron occupies an orbital earlier or later energetically; that ordering depends on the physical Hamiltonian and its interactions.

## 7. Ledger

| Claim | Status | Exact scope / remaining work |
|---|---|---|
| Word count is \(k^n\) | **STANDS** | Definition of length-\(n\) words over \(k\) symbols |
| Surface points are exponent vectors; count is \(\binom{n+k-1}{k-1}\) | **STANDS** | Stars-and-bars theorem |
| Fiber size is multinomial and fibers partition the interior | **STANDS** | Exact orbit-stabilizer and partition identities |
| Reciprocal-fiber route statistic estimates surface count without enumerating surface points | **STANDS** | Unbiased under uniform word sampling; sample variance must be reported |
| The quotient carries no order-sensitive process | **STANDS** | It still carries commutative composition; “no math at all” would overstate the result |
| `LEN()` is literally a radius | **MODEL** | True under the chosen degree / \(L^1\) grading |
| Orbital slice capacities pair as \(2,2,8,8,18,18,32,32,50,50\) | **STANDS, conditional on stated orbital rules** | Requires \(n+\ell\) degree and capacity \(2(2\ell+1)\) |
| Nodeless orbital has no same-\(\ell\) predecessor in the previous degree | **STANDS** | Follows from \(n_r'=-1\) |
| Abelianization alone explains physical filling order | **OPEN** | Needs a derivation linking the physical energy operator to route selection |
| The quotient is the only map available | **CORRECTION** | Canonical universal commutative quotient; other maps certainly exist |
| C1a forces \(k=2\) rather than allowing it as a parameter | **OPEN** | Must derive generator count from the primitive constraints, not from the desired application |
| WAN/LAN proves where free will can act | **INTERPRETATION / OPEN** | The algebra establishes order erasure vs order retention; agency needs separate operational criteria |

## 8. The binding question: what fixes \(k\)?

The abelianization theorem works for every \(k\geq1\). It does not select \(k=2\). The orbital application uses two labels, \((n,\ell)\), but that fact alone cannot prove that the primitive field has exactly two generators: coordinate count and generator count need not coincide without an explicit construction tying them together.

To close this gap, state a generator-minimality theorem with a domain and a failure criterion. For example: identify what independent distinctions must be represented, prove that one generator cannot encode them while preserving the route distinctions required by C1/C1a/C2, then prove that two suffice and that every additional generator is composite or redundant under those same constraints. Until that proof is supplied, \(k=2\) remains a selected model parameter, not a consequence of abelianization.

## Reproducibility

Run:

```bash
python nexus_abelian_surface_audit.py
```

The script is standard-library-only. `nexus_abelian_surface_results.json` contains the exact finite checks, seeded Monte Carlo estimates, and orbital degree-slice enumeration. The general proofs above do not depend on the random estimates.
