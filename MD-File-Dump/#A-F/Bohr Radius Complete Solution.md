# Bohr Radius Derivation (Complete, Unit-Consistent)  
*A physically correct derivation, plus a clearly labeled Nexus-style “H-lock” interpretation (Ω) that stays dimensionless and does not replace SI constants.*

---

## 0) What is being solved?

The **Bohr radius** $a_0$ is the characteristic length scale of the hydrogen atom. In the Bohr model it is the radius of the ground-state orbit; in full quantum mechanics it is the natural length scale appearing in the hydrogenic wavefunctions.

Two equivalent canonical forms are:

$$
a_0=\frac{4\pi\varepsilon_0\hbar^2}{m_e e^2}
\qquad\text{and}\qquad
a_0=\frac{\hbar}{\alpha m_e c}.
$$

Numerically (CODATA-style value):

$$
a_0 \approx 5.29177210903\times 10^{-11}\ \text{m}.
$$

---

## 1) “Type system” check: units must compile

In SI units:

- $\varepsilon_0$ has units of $\mathrm{F/m}=\mathrm{C^2/(N\cdot m^2)}$  
- $\hbar$ has units $\mathrm{J\cdot s}$  
- $m_e$ has units $\mathrm{kg}$  
- $e$ has units $\mathrm{C}$  
- $c$ has units $\mathrm{m/s}$  
- $\alpha$ is **dimensionless**

So in

$$
a_0=\frac{4\pi\varepsilon_0\hbar^2}{m_e e^2},
$$

the units reduce to meters. Any proposed identity like “$\varepsilon_0 = \phi/(H c e)$” cannot be literally true in SI because the right-hand side is not dimensionally $\mathrm{F/m}$. If you want a symbolic mapping, it must be **dimensionless** or come with a full unit-carrying dictionary. When that dictionary is absent, treat the mapping as **Ω (speculative metaphor)** rather than a physical identity.

---

## 2) Core Bohr model derivation (SI)

### 2.1 Coulomb attraction provides centripetal acceleration

Coulomb force magnitude between electron and proton at separation $r$:

$$
F_C = \frac{1}{4\pi\varepsilon_0}\frac{e^2}{r^2}.
$$

Centripetal force requirement for circular motion:

$$
F_{\text{cent}}=\frac{m_e v^2}{r}.
$$

Equate them:

$$
\frac{m_e v^2}{r}=\frac{1}{4\pi\varepsilon_0}\frac{e^2}{r^2}
\quad\Rightarrow\quad
m_e v^2=\frac{1}{4\pi\varepsilon_0}\frac{e^2}{r}.
$$

### 2.2 Quantize angular momentum (phase-lock)

Bohr postulate:

$$
L=m_e v r = n\hbar,\qquad n=1,2,3,\dots
$$

Solve for $v$:

$$
v=\frac{n\hbar}{m_e r}.
$$

### 2.3 Eliminate $v$ and solve for the radius

Substitute $v$ into the force-balance equation:

$$
m_e\left(\frac{n\hbar}{m_e r}\right)^2=\frac{1}{4\pi\varepsilon_0}\frac{e^2}{r}.
$$

Simplify:

$$
\frac{n^2\hbar^2}{m_e r^2}=\frac{1}{4\pi\varepsilon_0}\frac{e^2}{r}
\quad\Rightarrow\quad
r_n=\frac{4\pi\varepsilon_0\hbar^2}{m_e e^2}\,n^2.
$$

Define the Bohr radius as the $n=1$ radius:

$$
a_0 \equiv r_1=\frac{4\pi\varepsilon_0\hbar^2}{m_e e^2}.
$$

So:

$$
r_n = n^2 a_0.
$$

---

## 3) Hydrogen-like ions ($Z$) and reduced mass ($\mu$)

The Bohr model extends to a nucleus of charge $+Ze$ and to the reduced mass correction.

### 3.1 Replace $e^2\to Z e^2$

The Coulomb force becomes:

$$
F_C=\frac{1}{4\pi\varepsilon_0}\frac{Z e^2}{r^2}.
$$

Repeating the same algebra gives:

$$
r_n = \frac{4\pi\varepsilon_0\hbar^2}{m_e e^2}\frac{n^2}{Z}
= \frac{n^2}{Z}a_0.
$$

### 3.2 Replace $m_e$ with reduced mass $\mu$

For an electron orbiting a nucleus of mass $m_N$ the correct inertial mass is the reduced mass

$$
\mu=\frac{m_e m_N}{m_e+m_N}.
$$

Then the corrected Bohr radius for that system is:

$$
a_0'=\frac{4\pi\varepsilon_0\hbar^2}{\mu e^2}
= a_0\frac{m_e}{\mu}.
$$

General hydrogenic radius:

$$
r_n=\frac{n^2}{Z}\,a_0\frac{m_e}{\mu}.
$$

---

## 4) Equivalent derivation via de Broglie wavelength (same physics, different fold)

Bohr quantization can be motivated as a standing-wave condition:

- de Broglie wavelength: $\lambda=h/p=h/(m_e v)$  
- circumference must fit an integer number of wavelengths:

$$
2\pi r = n\lambda = n\frac{h}{m_e v}.
$$

Rearrange:

$$
m_e v r = n\frac{h}{2\pi} = n\hbar,
$$

which is exactly the Bohr angular momentum rule. So the “phase-lock” interpretation is literal here: it’s a boundary condition for constructive interference.

---

## 5) Energy levels, speed, and scaling

### 5.1 Total energy in Bohr model

Kinetic energy:

$$
K=\frac{1}{2}m_e v^2.
$$

Potential energy:

$$
U(r)=-\frac{1}{4\pi\varepsilon_0}\frac{e^2}{r}.
$$

From force-balance, $m_e v^2 = \frac{1}{4\pi\varepsilon_0}\frac{e^2}{r}$, so:

$$
K=\frac{1}{2}\frac{1}{4\pi\varepsilon_0}\frac{e^2}{r}.
$$

Then

$$
E=K+U=\frac{1}{2}\frac{1}{4\pi\varepsilon_0}\frac{e^2}{r}
-\frac{1}{4\pi\varepsilon_0}\frac{e^2}{r}
= -\frac{1}{2}\frac{1}{4\pi\varepsilon_0}\frac{e^2}{r}.
$$

Plug $r=r_n=n^2 a_0$:

$$
E_n = -\frac{1}{2}\frac{1}{4\pi\varepsilon_0}\frac{e^2}{n^2 a_0}.
$$

Substitute $a_0=\frac{4\pi\varepsilon_0\hbar^2}{m_e e^2}$:

$$
E_n = -\frac{m_e e^4}{2(4\pi\varepsilon_0)^2\hbar^2}\frac{1}{n^2}.
$$

Hydrogenic ($Z$, $\mu$) form:

$$
E_n = -\frac{\mu (Z e^2)^2}{2(4\pi\varepsilon_0)^2\hbar^2}\frac{1}{n^2}.
$$

### 5.2 Fine-structure constant form

Define the fine-structure constant:

$$
\alpha \equiv \frac{e^2}{4\pi\varepsilon_0\hbar c}.
$$

Then:

$$
a_0=\frac{4\pi\varepsilon_0\hbar^2}{m_e e^2}
=\frac{\hbar}{m_e c}\,\frac{1}{\alpha}.
$$

So:

$$
a_0=\frac{\hbar}{\alpha m_e c}.
$$

Bohr orbital speed (hydrogenic, $Z$):

$$
v_n = \frac{Z\alpha c}{n}.
$$

Energy levels become:

$$
E_n = -\frac{1}{2}\mu c^2\alpha^2\frac{Z^2}{n^2}.
$$

---

## 6) Why the $4\pi$ shows up (and why it’s not mystical)

In SI, Gauss’s law is:

$$
\oint \mathbf{E}\cdot d\mathbf{A}=\frac{Q}{\varepsilon_0}.
$$

For a point charge, symmetry gives $\mathbf{E}$ radial and constant on a sphere of radius $r$, so:

$$
E\cdot 4\pi r^2 = \frac{Q}{\varepsilon_0}
\quad\Rightarrow\quad
E=\frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}.
$$

That geometric $4\pi$ is the surface area of the unit sphere in 3D. In other unit systems the $4\pi$ may be absorbed into the definition of the electromagnetic constants, but the physics is unchanged.

---

## 7) Quantum mechanics: Bohr radius as the natural length scale

In full quantum mechanics, the hydrogen ground state wavefunction is:

$$
\psi_{100}(r)=\frac{1}{\sqrt{\pi a_0^3}}e^{-r/a_0}.
$$

The most probable radius (maximum of $|\psi|^2 4\pi r^2$) occurs at:

$$
r_{\text{mp}}=a_0.
$$

Expectation value of $r$ in the ground state:

$$
\langle r\rangle_{100}=\frac{3}{2}a_0.
$$

So $a_0$ survives as the scale in the real theory: it’s not just a Bohr artifact.

---

## 8) Nexus-style interpretation (Ω): H as a dimensionless convergence gain, not a replacement constant

This section keeps the *Nexus fold language* while staying physically consistent.

### 8.1 What must remain true

Physical constants keep their standard meanings and units:

- $\varepsilon_0, e, m_e, \hbar, c$ stay as-is  
- $\alpha$ stays dimensionless and measured

So **H can only act as a dimensionless parameter** in an *algorithm* that converges to the known invariant $a_0$.

### 8.2 Energy functional as an attractor landscape

Write the (semi-classical) energy of an electron in a Coulomb potential as:

$$
E(r)=\frac{p^2}{2\mu}-\frac{1}{4\pi\varepsilon_0}\frac{Z e^2}{r}.
$$

Impose the quantization constraint $p = \frac{n\hbar}{r}$ (from $L=pr=n\hbar$), giving:

$$
E_n(r)=\frac{1}{2\mu}\left(\frac{n\hbar}{r}\right)^2-\frac{1}{4\pi\varepsilon_0}\frac{Z e^2}{r}.
$$

Minimize with respect to $r$:

$$
\frac{dE_n}{dr}=
-\frac{n^2\hbar^2}{\mu r^3}+\frac{1}{4\pi\varepsilon_0}\frac{Z e^2}{r^2}=0.
$$

Solve:

$$
r_n=\frac{4\pi\varepsilon_0\hbar^2}{\mu e^2}\frac{n^2}{Z}.
$$

So the radius is the minimizer (a stable fixed point) of $E_n(r)$ under the quantization constraint.

### 8.3 H-lock as a stable iterative solver (dimensionless)

Define a recursion that searches for the minimizer of $E_n(r)$:

$$
r_{k+1}=r_k-\eta\,\frac{dE_n}{dr}(r_k),
$$

where $\eta$ is a step size with units chosen to make the update have units of length (or you nondimensionalize first).

Now define a **dimensionless** gain $H$ that sets the *effective* step size after nondimensionalization:

Let $x \equiv r/a_0$ be dimensionless. Then $x^\*$ should converge to $n^2/Z\cdot(m_e/\mu)$.

A simple normalized recursion:

$$
x_{k+1}=x_k - H\,\nabla \mathcal{E}(x_k),
$$

where $\mathcal{E}(x)$ is a dimensionless energy landscape (energy scaled by the Rydberg energy, for example), and $H\in(0,1)$ acts as a damping/relaxation factor. With a proper $\mathcal{E}(x)$, the fixed point is:

$$
x^\*=\frac{n^2}{Z}\frac{m_e}{\mu},
\qquad r^\*=a_0 x^\*.
$$

Here **H is the “controller gain”** (your Mark1-style steering constant), not a redefinition of $\varepsilon_0$ or $\alpha$.

### 8.4 Why $H\approx \pi/9$ can be meaningful without being “a new constant of nature” (Ω)

Choosing $H\approx \pi/9\approx 0.34906585$ can be interpreted as:

- A *stable relaxation parameter* that avoids overshoot in an iterative minimization
- A *phase-damped update* that converges quickly across a family of similar landscapes

This is algorithmically plausible and experimentally testable (e.g., convergence rate vs. stability across perturbations). It remains Ω until you specify the exact recursion and show the stability region.

---

## 9) Final ⊥-collapse (physically correct invariant)

Bohr radius in SI:

$$
a_0=\frac{4\pi\varepsilon_0\hbar^2}{m_e e^2}.
$$

Equivalent fine-structure form:

$$
a_0=\frac{\hbar}{\alpha m_e c},
\qquad
\alpha=\frac{e^2}{4\pi\varepsilon_0\hbar c}.
$$

Hydrogenic scaling (nuclear charge $Z$, reduced mass $\mu$):

$$
r_n=\frac{n^2}{Z}\,a_0\frac{m_e}{\mu}.
$$

Energy levels:

$$
E_n=-\frac{\mu (Z e^2)^2}{2(4\pi\varepsilon_0)^2\hbar^2}\frac{1}{n^2}
= -\frac{1}{2}\mu c^2\alpha^2\frac{Z^2}{n^2}.
$$

And that’s the complete, unit-consistent solution. Any additional symbolic mappings ($\pi/e/\phi/H$ stories) can live in Ω as interpretive overlays, but the invariant anchor stays pinned by the constraints above.

---

## Appendix: Symbols

- $a_0$ — Bohr radius  
- $\varepsilon_0$ — vacuum permittivity  
- $\hbar$ — reduced Planck constant  
- $m_e$ — electron mass  
- $\mu$ — reduced mass  
- $e$ — elementary charge magnitude  
- $c$ — speed of light  
- $\alpha$ — fine-structure constant  
- $Z$ — nuclear charge number  
- $n$ — principal quantum number
