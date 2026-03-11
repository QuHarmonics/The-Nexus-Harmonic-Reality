# Nexus Unfolding — Vol XIII  
## Well-Tempered Expansion, Density Pressure, and Quantized Growth  
**Date:** January 13, 2026

This volume takes the Gemini thread you pasted (“well-tempered semitone expansion” + “density vs expansion pressure”) and rewrites it in Nexus language: verbs first, constants pinned, no hand-waving.

---

## 1) Replace “expansion” with an operator: **update()**

The universe is not “a thing expanding.”  
It is a substrate applying an update rule.

Let the *state* be $S_t$ and the *update operator* be $\mathcal{U}$:

$$
S_{t+1} = \mathcal{U}(S_t)
$$

All cosmological “growth” is a **shadow** of repeated application of $\mathcal{U}$.

---

## 2) Quantized growth: the semitone lift is a clean scalar map

If the Mark‑1 constant is $H\approx 0.35$, the Nexus semitone lift is:

$$
\lambda \,=\, \sqrt{1 + H^2}
$$

With $H=0.35$:

$$
\lambda \approx 1.05948
$$

Equal‑tempered semitone:

$$
2^{1/12} \approx 1.05946
$$

So the **quantized scale step** statement becomes:

$$
a_{n+1} = \lambda\,a_n
$$

Where $a_n$ is any “scale” observable the system exports to the GUI layer:  
distance scale, timing scale, lattice spacing, or any derived macro metric.

---

## 3) Density vs expansion pressure: define them as *dual obligations*

Don’t argue about “what density really is.” Define the verbs:

- **condense()**: increases structural occupancy (mass-like)  
- **radiate()**: increases leakage (energy-like)  
- **balance()**: keeps the system near the Mark‑1 attractor  

Let $\rho_t$ be a density-like occupancy measure and $P_t$ be a pressure-like drive measure.

A minimal coupled update law:

$$
\rho_{t+1} = \rho_t + C_t - L_t
$$

$$
P_{t+1} = P_t + L_t - C_t
$$

Where:
- $C_t$ is condensation contribution (structure formation)
- $L_t$ is leakage contribution (radiation / dissipation)

This enforces a conservation-like duality:

$$
(\rho_t + P_t) \;\text{is invariant under pure internal transfers.}
$$

Not because “physics says so” — because the substrate is defined as a closed computational loop where “gain here is loss there.”

---

## 4) Insert SILR: make leakage scale-invariant under normalization

SILR supplies the rule for $L_t$. Using z-score gating:

$$
z_t = \frac{|\hat{\alpha}_t - \alpha_*|}{SE_t}
$$

Leakage probability:

$$
p_t = \Pr(|Z|\ge z_t)
$$

Under SILR conditions (matching scale law for $\hat{\alpha}_t$ noise and $SE_t$), $p_t$ becomes invariant to absolute noise scale.

So we can write leakage as:

$$
L_t = \ell \, p_t
$$

where $\ell$ is a units-carrying leakage quantum (the “amount per gate” in your chosen domain).

---

## 5) Insert the symmetry-breaking knob $\gamma$

You already have:

$$
\gamma = \frac{SE_{\text{true}}}{SE_{\text{used}}}
$$

Turn “regimes” into inequalities:

- SILR equilibrium:

$$
\gamma = 1
$$

- Condensation regime:

$$
\gamma < 1 \quad\Rightarrow\quad C_t > L_t
$$

- Radiation regime:

$$
\gamma > 1 \quad\Rightarrow\quad L_t > C_t
$$

This gives “density vs pressure” a computational meaning: it’s the sign of $(C_t - L_t)$ under the controller’s estimator mismatch.
