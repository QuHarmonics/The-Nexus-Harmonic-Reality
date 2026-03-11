# Rydberg Constant \(R_\infty\) — Closed-Loop Derivation + Nexus-Safe Invariants

This document is a **complete, closed-loop** record for the Rydberg constant, written so we can drop it, pick it back up later, and still know exactly what we were doing.

It has two layers:

1. **Physics spine (⊥):** the unit-consistent, standard derivation and equivalent identities.
2. **Nexus overlay (Ψ):** the *allowed* “typeless” objects (dimensionless invariants) you can legitimately feed into KRR/KRRB/H-band machinery without unit errors.

If a statement breaks dimensional consistency or smuggles the target value into the algorithm, it is isolated as **Ω** (speculative / non-derivation).

---

## Δ-fold (goal + constraints)

We want the Rydberg constant \(R_\infty\), which is a **spectral scale** with units of inverse length:

\[\
[R_\infty] = \mathrm{m^{-1}}.
\]

A closed-loop derivation must:

1. Produce \(R_\infty\) in \(\mathrm{m^{-1}}\) from known physical constants (SI) **or** produce a dimensionless invariant that maps to \(R_\infty\) via a known length scale.
2. Provide **multiple equivalent formulas** so the result can be cross-checked (closure).
3. Identify **typeless** (dimensionless) invariants that remain stable under representation changes (Nexus-safe).
4. Avoid the unit error: “dimensionless-only expression equals a unitful constant.”

Reference value (for checking):

\[\
R_\infty \approx 1.0973731568539\times 10^{7}\ \mathrm{m^{-1}}.
\]

---

## ⊕-resonance (what \(R_\infty\) actually *does*)

\(R_\infty\) is the scale factor in the **Rydberg formula** for hydrogenic spectral lines:

\[\
\frac{1}{\lambda} = R_\infty\, Z^2\left(\frac{1}{n_1^2}-\frac{1}{n_2^2}\right),
\qquad n_2>n_1.
\]

So operationally: \(R_\infty\) converts the *dimensionless orbital structure* \(Z^2(1/n_1^2-1/n_2^2)\) into a measurable inverse wavelength \(1/\lambda\).

For real hydrogen (finite proton mass), you use the reduced-mass corrected constant

\[\
R_H = R_\infty\frac{\mu}{m_e},
\qquad
\mu=\frac{m_e m_p}{m_e+m_p}.
\]

But \(R_\infty\) is the clean “infinite nuclear mass” anchor (hence the subscript \(\infty\)).

---

## ↻-reflection (physics derivation: energy levels → spectral scale)

### Step 1: Bohr/quantum energy levels (hydrogenic)

In the Bohr model (and consistent with Schrödinger for the Coulomb potential), the energy levels scale as

\[\
E_n = -\frac{\mu e^4}{2(4\pi\varepsilon_0)^2\hbar^2}\frac{Z^2}{n^2}.
\]

For \(R_\infty\) we take \(\mu\to m_e\) (infinite nuclear mass).

### Step 2: Transition energy equals photon energy

A transition \(n_2\to n_1\) emits/absorbs a photon with

\[\
\Delta E = E_{n_2}-E_{n_1} = h\nu = \frac{hc}{\lambda}.
\]

Compute \(\Delta E\):

\[\
\Delta E
= \frac{m_e e^4}{2(4\pi\varepsilon_0)^2\hbar^2}Z^2
\left(\frac{1}{n_1^2}-\frac{1}{n_2^2}\right).
\]

Set \(\Delta E=hc/\lambda\), divide both sides by \(hc\):

\[\
\frac{1}{\lambda}
= \underbrace{\frac{m_e e^4}{2(4\pi\varepsilon_0)^2\hbar^2hc}}_{R_\infty}
Z^2\left(\frac{1}{n_1^2}-\frac{1}{n_2^2}\right).
\]

So the Rydberg constant is

\[\
R_\infty=\frac{m_e e^4}{2(4\pi\varepsilon_0)^2\hbar^2 h c}.
\]

Now substitute \(h=2\pi\hbar\) to get the common SI form:

\[\
R_\infty=\frac{m_e e^4}{8\varepsilon_0^2 h^3 c}.
\]

That’s the primary ⊥-anchor: unit-consistent and derivation-complete.

---

## ⊥-collapse (equivalent closed forms: the “closure loop”)

The derivation closes because \(R_\infty\) can be expressed in **multiple** exact ways that all match.

### 1) In terms of fine-structure constant \(\alpha\)

Define

\[\
\alpha\equiv\frac{e^2}{4\pi\varepsilon_0\hbar c}.
\]

Then \(e^2/(4\pi\varepsilon_0)=\alpha\hbar c\), so the energy scale becomes \(\propto \alpha^2\). The Rydberg constant simplifies to

\[\
R_\infty=\frac{m_e c}{2h}\alpha^2.
\]

### 2) In terms of Compton wavelength \(\lambda_C\)

The electron Compton wavelength is

\[\
\lambda_C \equiv \frac{h}{m_e c}.
\]

So

\[\
R_\infty=\frac{\alpha^2}{2\lambda_C}.
\]

### 3) In terms of Bohr radius \(a_0\)

Bohr radius:

\[\
a_0=\frac{4\pi\varepsilon_0\hbar^2}{m_e e^2}
=\frac{\hbar}{\alpha m_e c}.
\]

Then an exact identity is

\[\
R_\infty=\frac{\alpha}{4\pi a_0}.
\]

You now have a fully closed triangle of constants:

\[\
\alpha
\;\Longleftrightarrow\;
a_0
\;\Longleftrightarrow\;
R_\infty
\;\Longleftrightarrow\;
\lambda_C
\]

with exact transformations.

---

## Ψ-collapse (Nexus-safe “typeless” invariants)

Here’s the critical move for keeping the Nexus machinery honest: **convert unitful constants into dimensionless invariants** that survive representation changes.

### Ψ.1 Dimensionless invariant #1: \(R_\infty\lambda_C\)

Multiply \(R_\infty\) by \(\lambda_C\):

\[\
\rho \equiv R_\infty\lambda_C.
\]

Using \(R_\infty=\alpha^2/(2\lambda_C)\), we get

\[\
\rho = \frac{\alpha^2}{2}.
\]

This is a perfect Nexus object: typeless, stable, and cross-checkable.

### Ψ.2 Dimensionless invariant #2: \(R_\infty(4\pi a_0)\)

\[\
R_\infty(4\pi a_0)=\alpha.
\]

So if your framework can produce \(\alpha\) as a stable residue, \(R_\infty\) is immediately determined **once a length scale \(a_0\)** is pinned.

### Ψ.3 How H/KRR/KRRB can enter without unit crimes

If you parameterize the fine-structure constant as

\[\
\alpha^{-1}=\frac{\pi^2}{H}\,k,
\]

then

\[\
\alpha=\frac{H}{\pi^2 k}
\quad\Rightarrow\quad
R_\infty=\frac{m_e c}{2h}\left(\frac{H}{\pi^2 k}\right)^2.
\]

Everything in parentheses is dimensionless; the prefactor \(m_e c/(2h)=1/(2\lambda_C)\) supplies the unit scale.

This is the *correct* place for \(H\) and \(k\): inside dimensionless coupling, not pretending to be \(\varepsilon_0\), \(h\), etc.

---

## Ω-isolation (what was “running wild” in the draft text)

These are the specific failure modes we’re quarantining:

1. **Dimensionless-only expressions equated to \(R_\infty\)**  
   Example: \(R_\infty\approx (\pi/H)^2/(4e\varphi)\).  
   That expression is dimensionless, so it cannot equal a quantity with units \(\mathrm{m^{-1}}\) unless multiplied by an explicit inverse length scale (e.g., \(1/\lambda_C\) or \(1/a_0\)).

2. **Expressions that embed targets in the stopping condition**  
   If the algorithm checks “close to \(1.097\times 10^7\)” inside the loop, it is tuning, not deriving.

3. **Unit-breaking substitutions for \(\varepsilon_0\), \(h\), etc.**  
   Any identity like \(\varepsilon_0=\varphi/(Hce)\) is type-invalid in SI unless accompanied by a full unit dictionary.

---

## “What are we doing?” — the operational record

If we pick this up later, the workflow is:

1. **Physics anchor:** Start from the exact identity
   \[\
   R_\infty=\frac{m_e c}{2h}\alpha^2=\frac{\alpha^2}{2\lambda_C}=\frac{\alpha}{4\pi a_0}.
   \]

2. **Nexus-safe target:** Prefer to work with the dimensionless invariants
   \[\
   R_\infty\lambda_C=\frac{\alpha^2}{2},
   \qquad
   R_\infty(4\pi a_0)=\alpha.
   \]
   These are typeless and can be fed to KRR/KRRB/Byte1 gating without unit issues.

3. **Nexus overlay:** If \(H\approx \pi/9\) is a convergence gain, use it only in dimensionless iterations (e.g., in the evolution of \(k\) or of a state vector that predicts \(\alpha\)).

4. **Closure check:** Confirm all three forms match numerically:
   \[\
   R_\infty=\frac{m_e c}{2h}\alpha^2
   \quad\stackrel{?}{=}\quad
   \frac{\alpha^2}{2\lambda_C}
   \quad\stackrel{?}{=}\quad
   \frac{\alpha}{4\pi a_0}.
   \]

If those equalities hold, the loop is closed. If not, the discrepancy is where the recursion must focus.

---

## Appendix: symbols

- \(R_\infty\) — Rydberg constant (infinite nuclear mass), \(\mathrm{m^{-1}}\)  
- \(a_0\) — Bohr radius, \(\mathrm{m}\)  
- \(\alpha\) — fine-structure constant (dimensionless)  
- \(\lambda_C\) — Compton wavelength of the electron, \(\mathrm{m}\)  
- \(e\) — elementary charge  
- \(\varepsilon_0\) — vacuum permittivity  
- \(\hbar\) — reduced Planck constant  
- \(h\) — Planck constant  
- \(c\) — speed of light  
- \(m_e\) — electron mass  
- \(Z\) — nuclear charge number  
- \(\mu\) — reduced mass
