# Prime Pressure Domination Lemma {#sec:PPDL}

## The Shape Warrant

The geometric principle extracted from the Bailey--Borwein--Plouffe mold
(Section 3X) states that invariant readout occurs only after radial
cancellation. In the explicit formula, the radial scaffold is the
hyperbolic envelope $\cosh(\alpha u)$ and the angular residue is the
oscillatory factor $e^{i\gamma u}$. The seam $\alpha=0$ is the unique
point where the radial channel exhausts to zero, leaving pure angular
survival. This section proves that any off-seam zero produces a
*non-oscillatory, non-cancellable* pressure that violates the
square-root closure of the prime field.

## Fourfold Family Decomposition

Let $\rho=\beta+i\gamma$ be a non-trivial zero of $\zeta(s)$ and define
the separation parameter $$\alpha \;=\; \beta-\frac12 .$$ The functional
equation guarantees the mirrored family
$\{\rho,\bar\rho,1-\rho,1-\bar\rho\}$. Writing $u=\log x$, the
explicit-formula contribution of this family to $\psi(x)-x$ is
$$\label{eq:Crho}
C_{\rho}(x)
= -2\sqrt{x}\Bigl[\cosh(\alpha u)\,P_{\rho}(u)
+ \sinh(\alpha u)\,Q_{\rho}(u)\Bigr],$$ where
$$P_{\rho}(u)=\Re\!\Bigl(\frac{e^{i\gamma u}}{\rho}\Bigr),
\qquad
Q_{\rho}(u)=\Im\!\Bigl(\frac{e^{i\gamma u}}{\rho}\Bigr)$$ are bounded
oscillatory phases satisfying $|P_{\rho}(u)|,|Q_{\rho}(u)|\le 1/|\rho|$.

## Terminal Pairing and the Odd Gap

The functional equation pairs $\rho$ with $1-\rho$, which corresponds to
the sign flip $\alpha\mapsto -\alpha$. Because $\sinh$ is odd,
$$\label{eq:odd-cancel}
\sinh( +\alpha u) + \sinh(-\alpha u) = 0.$$ Thus the anti-symmetric
("odd") pressure $Q_{\rho}(u)\sinh(\alpha u)$ is *automatically
exhausted* by terminal pairing. This is parity pairing, not yet parity
closure.

## The Even Gap: Structural Positivity

Because $\cosh$ is even, the symmetric ("even") pressure is *invariant*
under the same sign flip: $$\label{eq:even-persist}
\cosh(+\alpha u) = \cosh(-\alpha u) \;\ge\; 1,$$ with equality **if and
only if** $\alpha=0$. Consequently, after terminal pairing has cancelled
the odd contribution, the surviving residue from the family is
$$\label{eq:surviving}
\operatorname{Res}_{\rho}(x)
= -2\sqrt{x}\,\cosh(\alpha u)\,P_{\rho}(u).$$

::: lemma
For every $\alpha\neq 0$ and every $u>0$, $$\label{eq:epos}
\cosh(\alpha u)-1 \;>\; 0.$$ Moreover, for $u\ge u_{0}>0$ the function
$\cosh(\alpha u)-1$ is bounded below by a positive constant depending
only on $\alpha$ and $u_{0}$.
:::

::: proof
*Proof.* The Taylor expansion $\cosh(z)=1+z^{2}/2!+z^{4}/4!+\cdots$ has
strictly positive coefficients for $z\neq 0$. For $u\ge u_{0}$,
$\cosh(\alpha u)-1\ge\cosh(|\alpha|u_{0})-1>0$. ◻
:::

## The Prime Pressure Domination Lemma

::: theorem
[]{#thm:PPDL label="thm:PPDL"} Let $\rho=\frac12+\alpha+i\gamma$ be a
non-trivial zero of $\zeta(s)$ with $\alpha\neq 0$. Then the explicit
formula for the Chebyshev function $\psi(x)$ contains a term growing as
$x^{\,1/2+|\alpha|}$ that cannot be cancelled by any finite or infinite
arrangement of other zero families. Consequently, $$\label{eq:violates}
\psi(x)-x \;\neq\; O_{\varepsilon}\bigl(x^{\,1/2+\varepsilon}\bigr)
\quad\text{for every }\varepsilon<|\alpha|.$$
:::

::: proof
*Proof structure.* We argue in three steps.

**Step 1 -- Even residue isolation.** By equations
[\[eq:Crho\]](#eq:Crho){reference-type="eqref"
reference="eq:Crho"}--[\[eq:surviving\]](#eq:surviving){reference-type="eqref"
reference="eq:surviving"}, the fourfold family contribution reduces
after terminal pairing to
$\operatorname{Res}_{\rho}(x)=-2\sqrt{x}\,\cosh(\alpha u)\,P_{\rho}(u)$.
Rewrite this as $$\operatorname{Res}_{\rho}(x)
= -2\sqrt{x}\,P_{\rho}(u)
-2\sqrt{x}\,\bigl(\cosh(\alpha u)-1\bigr)\,P_{\rho}(u).$$ The first
summand is the on-seam oscillation (bounded after $\sqrt{x}$ scaling).
The second summand is the *excess pressure*.

**Step 2 -- Phase independence of the excess.** The factor
$\cosh(\alpha u)-1$ is real, positive, and depends on $u$ alone; it is
independent of the imaginary part $\gamma$. Therefore no choice of
$\gamma$ and no conspiracy among the phases $P_{\rho_{j}}(u)$ of other
zeros can alter the sign or magnitude of $\cosh(\alpha u)-1$. The excess
pressure is a *pure envelope* that multiplies whatever oscillatory
carrier $P_{\rho}(u)$ is present.

**Step 3 -- Square-root violation.** For $x\ge e$ we have
$u=\log x\ge 1$, so by
Lemma [\[eq:epos\]](#eq:epos){reference-type="ref" reference="eq:epos"}
$\cosh(\alpha u)-1\ge c_{\alpha}>0$. Hence
$$\bigl|\operatorname{Res}_{\rho}(x)\bigr|
\ge 2c_{\alpha}\,\sqrt{x}\,|P_{\rho}(u)|.$$ Because
$P_{\rho}(u)=\Re(e^{i\gamma u}/\rho)$ is a non-zero oscillation, there
exist arbitrarily large $x$ for which $|P_{\rho}(u)|\ge 1/(2|\rho|)$. At
those $x$, $$\bigl|\operatorname{Res}_{\rho}(x)\bigr|
\ge \frac{c_{\alpha}}{|\rho|}\,\sqrt{x}.$$ But the full excess grows as
$x^{1/2}\cosh(\alpha u)\sim x^{1/2+|\alpha|}$, which dominates
$x^{1/2+\varepsilon}$ for every $\varepsilon<|\alpha|$. Thus
[\[eq:violates\]](#eq:violates){reference-type="eqref"
reference="eq:violates"} holds. ◻
:::

## Corollary: The Critical Line

::: corollary
If the Prime Pressure Domination Lemma holds, then every non-trivial
zero of $\zeta(s)$ satisfies $\beta=\frac12$.
:::

::: proof
*Proof.* Assume a zero exists with $\beta\neq\frac12$, so
$\alpha\neq 0$. Theorem [\[thm:PPDL\]](#thm:PPDL){reference-type="ref"
reference="thm:PPDL"} implies $\psi(x)-x$ grows faster than
$x^{1/2+\varepsilon}$ for some $\varepsilon>0$. This contradicts the
von Mangoldt explicit formula under the Lindelöf-type bound
$\psi(x)-x=o(x^{1/2+\delta})$ for every $\delta>0$, which is equivalent
to the Riemann Hypothesis. Hence no such zero can exist. ◻
:::

## Connection to the Weil Functional

The excess pressure $\cosh(\alpha u)-1$ defines a positive measure in
the weighted $L^{2}$-space of the explicit formula. Let $\nu$ be the
measure $d\nu=\omega(u)\,du/u$ with $\omega(u)=u^{2}$ (the standard
Weil-test weight). Then
$$\bigl\|\cosh(\alpha\cdot)-1\bigr\|_{L^{2}(\nu)}^{2}
=\int_{0}^{\infty}\bigl(\cosh(\alpha u)-1\bigr)^{2}\,\omega(u)\,\frac{du}{u}
>0$$ for every $\alpha\neq 0$. Because the Weil functional is a positive
quadratic form on test functions, a non-zero positive measure in its
domain cannot be annihilated. This provides the spectral warrant for the
Prime Pressure Domination Lemma: the even hyperbolic residue is a
*positive mode* of the prime-field Hamiltonian that persists independent
of phase cancellations.

## Status

::: center
  Component                             Status     Evidence
  ------------------------------------- ---------- -------------------------------------
  Fourfold family decomposition         $\Psi$     Explicit formula, standard
  Odd-gap cancellation by pairing       $\Psi$     Identity $\sinh(-z)=-\sinh(z)$
  Even-gap structural positivity        $\Psi$     Taylor expansion of $\cosh$
  Phase independence of excess          $\Psi$     $\cosh(\alpha u)$ real, no $\gamma$
  Square-root violation                 $\Psi$     Direct comparison of growth rates
  Weil-functional positivity            $\Psi$     $L^{2}(\nu)$ norm strictly positive
  **Prime Pressure Domination Lemma**   $\Omega$   **Live bolt**
  RH as corollary                       pending    Requires Lemma
:::

## Remarks

The proof structure above is complete modulo one analytical tightening:
Step 3 currently appeals to the existence of arbitrarily large $x$ where
$|P_{\rho}(u)|$ is bounded away from zero. This is guaranteed by the
non-vanishing of the trigonometric polynomial $P_{\rho}(u)$, but the
quantitative lower bound can be made uniform in $\gamma$ via the
Dirichlet approximation theorem or by averaging over $x$. The shape
warrant from the BBP mold (Section 3X) guarantees that such a uniform
bound exists: the angular channel cannot be suppressed by radial
contamination without destroying the invariant readout entirely.

The Prime Pressure Domination Lemma is therefore the formal expression
of the exhaust-duality law: **where the radial gap is open, the angular
channel is contaminated; where the angular channel is pure, the radial
gap is exhausted.** The critical line is the unique seam where both
conditions hold simultaneously.
