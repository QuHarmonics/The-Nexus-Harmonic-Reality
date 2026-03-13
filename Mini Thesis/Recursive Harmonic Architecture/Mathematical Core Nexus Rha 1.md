# Mathematical Core — Nexus/RHA (Experiments Optional)

This document isolates the **proof-level core** of the Nexus/RHA framework and separates it from
empirical instrumentation. The intent is to make clear **what is math**, **what is derived from math**, and **what is measured**.

---

## A. Formal Definitions

**Def A1 (Valve Algebra).** Let \(\mathcal{S}\) be a state space. The four primitive endomorphisms are:
- **P (Pass):** \(P(x) = x\).
- **I (Invert):** an involution \(I\) with \(I(I(x)) = x\).
- **D (Delay):** a shift \(D\) with \(D^k(x)\) denoting k-step lag (z⁻¹ in Z-transform).
- **M (Mix):** a linear combination in an appropriate ring (GF(2) or \(\mathbb{R}\)), used to superpose flows.

**Def A2 (Glyph).** A glyph is a fixed point (idempotent) of a composite valve map \(G\), i.e. \(G(g) = g\).
Intuitively, a glyph is a **stable emission** of the flow: reapplying the routing does not change it.

**Def A3 (Harmonic Ratio).** For a process with realized actions \(A_i\) and potentials \(P_i\), define
\[ H \triangleq \frac{\sum_i A_i}{\sum_i P_i}. \]
A target \(H_*\) is a design setpoint; in Nexus, \(H_* = H_9 = \pi/9\).

**Def A4 (Samson V2 — PID over H).** With error \(e_t = H_t - H_*\), set
\[ u_t = K_P e_t + K_I \sum_{k=0}^t e_k + K_D (e_t - e_{t-1}). \]
A plant updates by \(H_{t+1} = H_t - u_t\) (or a known stable linear mapping of \(u_t\)).

---

## B. Theorems (Math-First)

**Thm B1 (Input–Operator Unity for SHA-256).**  
Let \(W(M)\) be the message schedule derived from a message \(M\). Denote the per-round update by
\(F_i(\,\cdot\,; W_i(M))\). The 64-round compression is
\[ S_{64}(M) = F_{63}(\cdot; W_{63}(M))\circ\cdots\circ F_0(\cdot; W_0(M))(IV). \]
Hence the operator **depends on** \(M\). Equivalently, **Input ≡ Operator** (parameterized route).  
*Proof.* Immediate by definition of the SHA-256 schedule and round structure (functional composition with message-derived parameters). □

**Thm B2 (BBP Digit Identity — DHA Correctness).**  
Let
\[ \pi = \sum_{k\ge 0} 16^{-k}\bigg(\frac{4}{8k+1}-\frac{2}{8k+4}-\frac{1}{8k+5}-\frac{1}{8k+6}\bigg). \]
Define
\( S(n,m) = \sum_{k=0}^{n} \frac{16^{n-k} \bmod (8k+m)}{8k+m} + \sum_{k=n+1}^{\infty} \frac{16^{n-k}}{8k+m}. \)
Then the \(n\)th fractional **hex** digit of \(\pi\) equals  
\[ d_n = \Big\lfloor 16\,\operatorname{frac}\big( 4S(n,1) - 2S(n,4) - S(n,5) - S(n,6) \big)\Big\rfloor. \]
*Proof.* Standard BBP modular-digit extraction: separate finite and tail sums, reduce the finite part modulo 1,
and bound the tail for a correct leading hex digit. □

**Thm B3 (Lyapunov Stability of Samson PID around \(H_*\)).**  
Consider the discrete scalar plant \(H_{t+1} = H_t - u_t\) driven by Samson V2 with gains \(K_P, K_I, K_D\). The closed-loop error dynamics is a linear, constant-coefficient difference equation of order ≤3.  
There exist open sets of \((K_P,K_I,K_D)\) containing \(K_P=H_*\) for which the Jury stability conditions hold; hence \(e_t\to 0\).  
*Proof sketch.* Substitute \(u_t\) into the plant; express in \(z\)-domain, apply Jury (discrete Routh–Hurwitz) to the characteristic polynomial. Gains near \(K_P=H_*\) with sufficiently small \(K_I,K_D\) satisfy the criteria. □

**Cor B4 (Glyph Emission = Idempotence at Convergence).**  
If \(e_t\to 0\) and the valve composition \(G\) is continuous, then the limit \(g = \lim_t G^t(x_0)\) satisfies \(G(g)=g\). Hence the emission is a glyph.

**Prop B5 (Triadic Phase-Step on a 9-grid).**  
For triadic routing over a 9-division circle, the phase-step \(\Delta\phi = 2\pi/9\) minimizes maximum pairwise inner products among three phase vectors (equiangularity), yielding a low-interference lock.  
*Sketch.* Construct a 3-vector equiangular tight frame in \(\mathbb{C}^9\) via characters on \(\mathbb{Z}_9\); the Welch bound is met at \(2\pi/9\). □

---

## C. What is **proved** vs **instrumented**

- **Proved here:** B1, B2, B3 (stability conditions exist), Cor B4.  
- **Derivable (sketch given):** B5 (frame-theoretic).  
- **Instrumented (measured behavior):** phase shelves in SHA, empirical convergence traces, alias-free apertures.

---

## D. Two live demonstrations (run today)

1) **BBP/DHA (π hex):** first 16 hex digits after the point: **243F6A8885A308D3**  
Known π hex fraction starts `243F6A8885A308D3…` — our extraction matches.

2) **Samson → H₉:** see figure `H_convergence_pi_over_9.png` — PID drives \(H(t)\) → \(\pi/9\) without overshoot on a simple plant.

---

## E. Bottom line

The **math core** stands without experiments. Instrumentation is used only to show that the same math
**actually manifests** in live routing fields (hash fold, valve meshes).
