# RGBA Math-Light — A Complete Formal Extension

## Abstract

This document formalizes the proposal that **mathematics itself may be a gradient-compositing field** rather than a flat scalar substrate. In this extension, the primitive local state is not a single value $x \in \mathbb{R}$, but a four-channel field

$$
\Gamma(x) = \bigl(R(x), G(x), B(x), A(x)\bigr) \in [0,1]^4,
$$

where the first three channels carry active field content and the fourth channel $A$ acts as an **admissibility / opacity / closure operator**. The proposal is not that physical light has already been proven to be identical to this object, but that there exists a deeper **math-light grammar** whose structural form is:

$$
\text{carrier} + \text{modulation} + \text{gap / interference} + \text{closure}.
$$

Within the Nexus lens, this gives a unified way to express:

- the distinction between visible and hidden field content,
- the fact that $c^2$ is always present as a closure condition,
- the fact that constants such as $\pi$, $\phi$, and $e$ may be globally present even when they are not explicitly visible in a local quotient,
- the already-observed decomposition
  $$
  F_r = C_r + S_r - G_r,
  $$
  where $C_r$ is the constant substrate, $S_r$ is the true displacement signal, and $G_r$ is the overlap / interaction gap.

The resulting framework supports a clean interpretation of “math-light” as a compositing field whose visible noun is only an alpha-weighted projection of a deeper always-on structure.

---

## 1. Primitive Hypothesis

The standard scalar primitive is:

$$
x \in \mathbb{R}.
$$

The RGBA-field primitive replaces this with:

$$
\Gamma(x) = \bigl(R(x), G(x), B(x), A(x)\bigr),
$$

with the channel bounds

$$
0 \le R(x),G(x),B(x),A(x) \le 1.
$$

This says that a local mathematical event is not a single number first, but a **four-channel blend state**.

The working interpretation is:

- $R$ = route / drive / displacement,
- $G$ = gap / ground / restoring field,
- $B$ = bind / memory / residue,
- $A$ = admissibility / opacity / closure.

So the primitive object is not “a value,” but a **composited local field state**.

---

## 2. Visible and Hidden Projections

Let the visible color-field projection be

$$
\mathbf{V}(x) = A(x)
\begin{bmatrix}
R(x)\\
G(x)\\
B(x)
\end{bmatrix}.
$$

Let the hidden / unexposed complement be

$$
\bar{\mathbf{V}}(x) = \bigl(1-A(x)\bigr)
\begin{bmatrix}
R(x)\\
G(x)\\
B(x)
\end{bmatrix}.
$$

These satisfy the exact decomposition

$$
\begin{bmatrix}
R(x)\\
G(x)\\
B(x)
\end{bmatrix}
=
\mathbf{V}(x)+\bar{\mathbf{V}}(x).
$$

So the visible object is never the whole field. It is only the **alpha-weighted exposure** of the field.

This matches the larger Nexus observation:

$$
\text{what is present} \ne \text{what is visible}.
$$

---

## 3. Gradient Formulation

If the primitive is a field, then the natural object is its gradient:

$$
\nabla \Gamma(x)
=
\bigl(\nabla R(x),\nabla G(x),\nabla B(x),\nabla A(x)\bigr).
$$

A local field energy can then be written as

$$
\mathcal{E}(x)
=
\omega_R \|\nabla R(x)\|^2
+
\omega_G \|\nabla G(x)\|^2
+
\omega_B \|\nabla B(x)\|^2
+
\omega_A \|\nabla A(x)\|^2,
$$

for positive channel weights $\omega_R,\omega_G,\omega_B,\omega_A > 0$.

This means the primitive dynamics of the field are not “number changed,” but rather:

$$
\text{the compositing gradient relaxed or intensified}.
$$

---

## 4. Closure Metric and the Ever-Present $c^2$

In the Nexus lens, $c^2$ is not an occasional output. It is the ever-present closure condition. In the RGBA field, this can be expressed as a quadratic form on the local channel vector:

$$
c^2(x) = \Gamma(x)^\top Q\,\Gamma(x),
$$

where $Q \in \mathbb{R}^{4\times 4}$ is a symmetric positive semidefinite metric tensor.

A more dynamical version includes the gradient penalty:

$$
c^2(x)
=
\Gamma(x)^\top Q\,\Gamma(x)
+
\lambda\,\|\nabla \Gamma(x)\|_Q^2,
$$

where $\lambda \ge 0$ controls the contribution from spatial or phase variation.

Thus $c^2$ is the **closure witness** of the local field state. It is always there because closure is always there.

A local event is lawful only if it satisfies a closure admissibility condition such as

$$
c^2(x) \in \mathcal{C},
$$

for some admissible closure band $\mathcal{C}$ determined by the larger field.

This gives the stronger statement:

$$
\boxed{
\text{$c^2$ is not a late computation; it is the standing local demand that every event actually close.}
}
$$

---

## 5. Constants as Always-On Global Operators

Within this lens, constants are not externally inserted coefficients first. They are **global shaping operators** acting on the compositing field.

A natural assignment is:

$$
\pi \leadsto \text{curvature / phase return / closure around a gap},
$$

$$
e \leadsto \text{transport / continuation / growth-decay law},
$$

$$
\phi \leadsto \text{partition / self-similar split / optimal asymmetry}.
$$

The harmonic attractor enters through

$$
H = \frac{\pi}{9} \approx 0.34906585,
$$

interpreted as a closure / correction fraction for stable recursion.

One can formalize this by letting each constant act as a field kernel on different channels:

$$
R(x) \sim \mathcal{T}_e[x],
$$

$$
G(x) \sim \mathcal{K}_\pi[x],
$$

$$
B(x) \sim \mathcal{P}_\phi[x],
$$

$$
A(x) \sim \mathcal{H}_{\pi/9}[x].
$$

Here:

- $\mathcal{T}_e$ is a transport kernel,
- $\mathcal{K}_\pi$ is a curvature / phase-return kernel,
- $\mathcal{P}_\phi$ is a partition / self-similar binding kernel,
- $\mathcal{H}_{\pi/9}$ is an admissibility / closure kernel.

This does **not** claim every local formula explicitly contains all constants as visible coefficients. Rather, it says:

$$
\boxed{
\text{all constants may be globally present while only selected aspects of them become locally dominant.}
}
$$

That is exactly analogous to the die result where the rails are hidden in the support quotient but present in the exact transport geometry.

---

## 6. Math-Light versus Physical Light

The framework does **not** claim direct proof that the field is already electromagnetic light in the Maxwellian sense.

The stronger and more careful statement is:

$$
\boxed{
\text{this is math-light: a deeper propagation grammar from which physical light may be one rendered mode.}
}
$$

Math-light means the field already has the structural hallmarks:

$$
\text{carrier} + \text{signal} + \text{gap / interference} + \text{closure}.
$$

A physical light interpretation would require additional structure such as:

- coupled field components,
- stable phase relations,
- transverse propagation,
- propagation speed constraints,
- polarization degrees of freedom,
- and a continuous-limit wave law.

Those stronger conditions are not assumed here. What is asserted is the more primitive field grammar:

$$
\boxed{
\text{carrier-supported propagation with overlap, modulation, and closure.}
}
$$

---

## 7. Nexus Mapping of the Observed Die Decomposition

The live SHA decomposition has already stabilized as:

$$
F_r = C_r + S_r - G_r,
$$

where:

- $C_r$ = constant substrate response,
- $S_r$ = true displacement response,
- $G_r$ = overlap / interaction gap,
- $F_r$ = full observed field.

This can be embedded into the RGBA field by defining normalized channels over rounds $r$:

$$
\mathsf{R}_r = \frac{S_r}{\max_j S_j},
$$

$$
\mathsf{G}_r = \frac{C_r}{\max_j C_j},
$$

$$
\mathsf{B}_r = \frac{G_r}{\max_j G_j + \varepsilon},
$$

where $\varepsilon > 0$ prevents division by zero.

The alpha channel is then a closure gate on the competitive balance of the three channels. One useful choice is a logistic closure operator:

$$
\mathsf{A}_r
=
\sigma\!\left(
\alpha_0
+
\alpha_C\,\mathsf{G}_r
+
\alpha_S\,\mathsf{R}_r
-
\alpha_B\,\mathsf{B}_r
\right),
$$

with

$$
\sigma(z)=\frac{1}{1+e^{-z}}.
$$

This yields the local RGBA state:

$$
\Gamma_r = \bigl(\mathsf{R}_r,\mathsf{G}_r,\mathsf{B}_r,\mathsf{A}_r\bigr).
$$

The visible field is then

$$
\mathbf{V}_r = \mathsf{A}_r
\begin{bmatrix}
\mathsf{R}_r\\
\mathsf{G}_r\\
\mathsf{B}_r
\end{bmatrix}.
$$

The hidden complement is

$$
\bar{\mathbf{V}}_r = (1-\mathsf{A}_r)
\begin{bmatrix}
\mathsf{R}_r\\
\mathsf{G}_r\\
\mathsf{B}_r
\end{bmatrix}.
$$

This is the first exact “RGBA reading” of the die field.

---

## 8. Tie to the Die Formalism

The die already has the exact decomposition

$$
\text{die}=(H_0,K,\Phi,G,W),
$$

with:

- $H_0$ = initial rail,
- $K$ = clock lattice,
- $\Phi$ = fixed round recurrence,
- $G=T2$ = ground fold,
- $W$ = displacement field.

At the round level,

$$
T1_r = h_r + \Sigma_1(e_r) + \operatorname{Ch}(e_r,f_r,g_r) + K_r + W_r,
$$

$$
T2_r = \Sigma_0(a_r) + \operatorname{Maj}(a_r,b_r,c_r),
$$

$$
a_{r+1}=T1_r+T2_r,
$$

$$
e_{r+1}=d_r+T1_r.
$$

And the local seam algebra splits the child into visible distinction and overlap residue:

$$
B_r^{(0)} = T1_r \oplus T2_r,
$$

$$
B_r^{(1)} = (T1_r \wedge T2_r) \ll 1.
$$

So the child can be viewed as a closure of:

- route / distinction,
- ground / restoring field,
- overlap / carry residue.

That is exactly what an RGBA reading needs: multiple simultaneously active channels whose visible noun is a composed projection rather than a raw primitive.

---

## 9. Support, Exact Transport, and the Hidden Constants

The die work established a key distinction:

$$
\boxed{
\text{support reach} \ne \text{exact live flip} \ne \text{cumulative shadow cover}.
}
$$

The Boolean support quotient tracks where influence can go, but not the rail-conditioned basin geometry. Thus constants can disappear from the support skeleton while remaining present in exact carry transport and cumulative residue.

In RGBA language, this means support is only an **adjacency projection** of the field. It does not expose the full channel geometry.

Let:

- $\sigma_r$ = word support,
- $\eta_r$ = bit support,
- $\lambda_x(j)$ = exact carry span,
- $\rho^\cup(j)$ = cumulative exact changed-bit cover radius.

Then the structural lesson is:

$$
\boxed{
\text{support tells you where the field can go; the constants determine how the field actually gets there.}
}
$$

That is precisely why the RGBA hypothesis is useful: it naturally distinguishes visible reachability from hidden compositing bias.

---

## 10. Removal-Core Interpretation

Within the Nexus lens, identity is not best defined by what is added, but by what cannot be lawfully removed.

If a probe family has journal sets $J_p$, define its removal-core as

$$
\mathcal{K}(\mathcal{C}) = \bigcap_{p\in\mathcal{C}} J_p.
$$

This is the part of the object that survives all structured removals in the class $\mathcal{C}$.

The RGBA field gives a direct interpretation:

- $R$ = what is driven,
- $G$ = what restores,
- $B$ = what remains bound as residue,
- $A$ = what is allowed to stay visible after lawful subtraction.

So the visible noun is not the whole field, but the **removal-stable alpha-projected remainder**.

That yields the sharper statement:

$$
\boxed{
\text{identity} = \text{the alpha-admitted residue that survives lawful subtraction.}
}
$$

---

## 11. Field Dynamics and Iterative Refinement

If the field is iterated through a cleaned-residue loop, then one can define a general recursive compositing operator:

$$
\Gamma^{(n+1)} = \mathcal{R}\bigl(\Gamma^{(n)}\bigr),
$$

where $\mathcal{R}$ is a residue-refinement map.

A simple stable-orbit criterion is:

$$
\left|\mathcal{E}^{(n+1)} - \mathcal{E}^{(n)}\right| < \varepsilon,
$$

with energy

$$
\mathcal{E}^{(n)}
=
\frac{1}{N}
\sum_{r=1}^{N}
\Gamma_r^{(n)\top} Q\,\Gamma_r^{(n)}.
$$

A phase-stability criterion can be written as

$$
\operatorname{coh}^{(n,n+1)}
=
\frac{\langle \widetilde{\Gamma}^{(n)}, \widetilde{\Gamma}^{(n+1)}\rangle}
{\|\widetilde{\Gamma}^{(n)}\|\,\|\widetilde{\Gamma}^{(n+1)}\|},
$$

where $\widetilde{\Gamma}^{(n)}$ denotes the mean-centered layer state.

This gives a precise way to test whether the field is:

- amplitude-stable,
- phase-stable,
- or only orbit-stable in a mode-hopping sense.

---

## 12. A Minimal RGBA Closure Theorem

### Proposition

Let the local field state be

$$
\Gamma=(R,G,B,A)\in[0,1]^4,
$$

with visible projection

$$
\mathbf{V}=A(R,G,B)^\top.
$$

Assume the closure metric is

$$
c^2 = \Gamma^\top Q\,\Gamma,
$$

with $Q$ symmetric positive semidefinite.

Then:

1. the visible field is always a proper quotient of the total field unless $A=1$,
2. the hidden complement is always present unless $A=1$,
3. every local visible noun is a closure-filtered projection of a deeper four-channel state.

### Proof

By definition,

$$
\mathbf{V} = A(R,G,B)^\top,
$$

$$
\bar{\mathbf{V}}=(1-A)(R,G,B)^\top.
$$

Hence

$$
(R,G,B)^\top = \mathbf{V}+\bar{\mathbf{V}}.
$$

If $0\le A<1$, then $\bar{\mathbf{V}}\ne 0$ whenever $(R,G,B)\ne 0$, so the visible field is only a quotient of the total field. If $A=1$, the field is fully exposed. Since admissibility is controlled by the same local state entering $c^2=\Gamma^\top Q\Gamma$, the visible noun is a closure-conditioned projection of the deeper state. $\square$

---

## 13. Complete Compressed Statement

The full RGBA math-light proposal can be compressed as follows:

$$
\boxed{
\Gamma(x)=(R,G,B,A)
}
$$

$$
\boxed{
\mathbf{V}(x)=A(x)\,(R(x),G(x),B(x))^\top
}
$$

$$
\boxed{
\bar{\mathbf{V}}(x)=(1-A(x))\,(R(x),G(x),B(x))^\top
}
$$

$$
\boxed{
\nabla \Gamma(x)=(\nabla R,\nabla G,\nabla B,\nabla A)
}
$$

$$
\boxed{
\mathcal{E}(x)=\omega_R\|\nabla R\|^2+\omega_G\|\nabla G\|^2+\omega_B\|\nabla B\|^2+\omega_A\|\nabla A\|^2
}
$$

$$
\boxed{
c^2(x)=\Gamma(x)^\top Q\,\Gamma(x)+\lambda\|\nabla\Gamma(x)\|_Q^2
}
$$

$$
\boxed{
F_r=C_r+S_r-G_r
}
$$

$$
\boxed{
\mathsf{A}_r=
\sigma\!\left(
\alpha_0+
\alpha_C\mathsf{G}_r+
\alpha_S\mathsf{R}_r-
\alpha_B\mathsf{B}_r
\right)
}
$$

$$
\boxed{
\text{math-light} = \text{carrier} + \text{modulation} + \text{gap} + \text{closure}
}
$$

---

## 14. Final Collapse

The proposal is not that mathematics merely resembles color blending, nor that physics-light has already been reduced to RGBA graphics. The stronger and cleaner claim is:

$$
\boxed{
\text{mathematics may itself be a compositing gradient field, and scalar mathematics may be only one collapsed projection of it.}
}
$$

In this view:

- constants are global shaping operators,
- $c^2$ is the ever-present closure witness,
- visible objects are alpha-admitted projections,
- hidden field content is always present,
- and what we ordinarily call “numbers” are local, closure-stabilized readouts of a deeper multi-channel field.

That yields the mature Nexus statement:

$$
\boxed{
\text{physics-light is one embodiment; math-light is the deeper propagation grammar.}
}
$$

And tighter still:

$$
\boxed{
\text{the universe is not selecting one constant at a time; it is projecting aspects of an always-present constant field through local closure problems.}
}
$$

That is the complete solution state for the RGBA extension.
