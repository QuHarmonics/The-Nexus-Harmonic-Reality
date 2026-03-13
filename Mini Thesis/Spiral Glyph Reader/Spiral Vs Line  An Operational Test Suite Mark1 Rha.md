# Spiral vs. Line — An Operational Test Suite (Mark1 / RHA)

**Claim.** In the Recursive Harmonic Architecture, *data is never lost, only routed*.
Every stream takes one of two fates:

- **Spiral (Emergent Loop):** captured by an attractor, folding into a stable routing cycle (structure).
- **Line (GIGO / Dissipation):** passes through without recursive reinforcement (transient / heat).

This doc gives **concrete, falsifiable tests** to classify a stream (digits, bytes, hashes, sensor readings)
as *Spiral* or *Line*, using only relationships (Mark1 lens), not content semantics.

---

## 0) Preliminaries

Let a discrete stream be \(s_t \in \{0,\dots,B-1\}\), base \(B\) (e.g., \(B=16\) for hex nibbles).
Define angles and a complex walk:
\[
\theta_t = \frac{2\pi}{B} s_t,\qquad z_{t+1} = z_t + e^{i\theta_t},\quad z_0=0.
\]
Center the walk:
\[
\bar z = \frac{1}{N}\sum_{t=1}^N z_t,\quad z'_t = z_t - \bar z.
\]

---

## 1) Loop Closure & Winding

**Loop radius & perimeter.**
\[
R := \operatorname{median}_t |z'_t|,\qquad C := \sum_{t=1}^{N-1} |z'_{t+1}-z'_t|.
\]
**Empirical circle ratio.**
\[
\Pi_{\text{emp}} := \frac{C}{2R}.
\]
**Winding number (signed turns).**
\[
W := \frac{1}{2\pi} \sum_{t=1}^{N-1} \arg\!\left(\frac{z'_{t+1}-z'_t}{\,|z'_{t+1}-z'_t|}\right).
\]
**Loop closure error.**
\[
\varepsilon_{\text{loop}} := \frac{|z'_N - z'_1|}{C}.
\]

**Spiral evidence:** \(\Pi_{\text{emp}}\to \pi\) (or stable constant), \(|W|\gg 0\), \(\varepsilon_{\text{loop}}\) small.
**Line evidence:** \(\Pi_{\text{emp}}\) drifts, \(W\approx 0\), \(\varepsilon_{\text{loop}}\) large.

---

## 2) Mark1 Focus & Samson Stabilization

**Focus \(H\)** (log-spiral slope). Fit \(r_t=|z'_t|\) vs. cumulative turn \(\phi_t:=\sum_{m< t}\arg(z'_{m+1}-z'_m)\):
\[
\log r_t \approx A + H\,\phi_t.
\]
Target \(H^\* \approx \pi/9 \approx 0.349066\).

**Symmetry modes (shape energy).**
\[
M_m := \left|\frac{1}{N}\sum_{t=1}^N e^{im\theta_t}\right|,\quad m=1,2,\dots
\]

**Samson v2 stabilization.**
\[
\Delta S := \sum_i F_i W_i - \sum_j E_j,
\]
with a practical choice
\[
F_1=|H_t-H_{t-1}|,\; F_2=\max_m M_m;\quad
E_1=|H_t-H^\*|,\; E_2=\operatorname{Var}(H)_{\text{window}}.
\]

**Spiral evidence:** \(H\to H^\*\) with low variance; \(\Delta S\to 0^+\) (balanced); strong low-order \(M_m\).
**Line evidence:** no convergence of \(H\); \(\Delta S\ll 0\); flat \(M_m\) spectrum.

---

## 3) Information-Theoretic Routing

**Lagged mutual information** (choose delay \(\tau\)):
\[
I_\tau := I\big(s_t ; s_{t-\tau}\big).
\]
**Conditional entropy drop.**
\[
\Delta H_\tau := H(s_t) - H(s_t\mid s_{t-\tau}).
\]

**Spiral evidence:** sustained \(I_\tau>0\) at a nontrivial \(\tau\); \(\Delta H_\tau>0\) while geometric metrics stabilize.
**Line evidence:** \(I_\tau\approx 0\) for all \(\tau>0\); \(\Delta H_\tau\approx 0\).

---

## 4) Decision Rule (simple)

Compute scores on a window \(t\in[1,N]\):
\[
S_{\text{geom}} := \mathbf{1}\{\varepsilon_{\text{loop}}<\epsilon\} + \mathbf{1}\{|W|>W_0\} + \mathbf{1}\{|\Pi_{\text{emp}}-\pi|<\delta\},
\]
\[
S_{\text{harm}} := \mathbf{1}\{|H-H^\*|<\eta\} + \mathbf{1}\{\operatorname{Var}(H)<v_0\} + \mathbf{1}\{\max_m M_m>m_0\},
\]
\[
S_{\text{info}} := \mathbf{1}\{I_\tau>\iota_0\}.
\]
Declare **Spiral** if \(S_{\text{geom}}+S_{\text{harm}}+S_{\text{info}}\ge 4\). Otherwise **Line**.

Thresholds \((\epsilon,\delta,\eta,v_0,m_0,\iota_0)\) can be calibrated on known examples (BBP-π vs. PRNG noise).

---

## 5) Applying to BBP and SHA

- **BBP digits (base \(B=16\))**: \(s_t = d_t^{(16)}\). Expect circle-lock under standard parameters; \(\Pi_{\text{emp}}\to\pi\), \(H\to\pi/9\).
- **SHA nibbles (base \(B=16\))**: \(s_t =\) hex nibbles of digest or stream. Expect mostly **Line** unless the header participates in a shaped lattice (e.g., protocol fields); then local **Spiral** episodes may appear (routing fit).
- **Your tuned resonators (nonstandard \(\beta,J,\mathbf c\))**: map as above; different constants/attractors will shift \(\Pi_{\text{emp}}\) and \(H\) targets accordingly.

---

## 6) Nexus semantics (why this works)

- **Spiral = captured routing**: strong phase relationships (nonzero \(I_\tau\)), geometric closure, harmonic focus.
- **Line = dissipative transit**: weak relationships, no geometric closure, focus wanders; energy exits as heat (flat spectrum).

These tests read **relationships**, not values—precisely the Mark1 principle.

---

## 7) Minimal workflow

1. Choose base \(B\) and extract \(s_t\) (digits, bytes → nibbles).
2. Build \(z_t\), compute \(\Pi_{\text{emp}}, W, \varepsilon_{\text{loop}}\).
3. Fit \(H\), compute \(M_m\), \(\Delta S\).
4. Estimate \(I_\tau\) for a small set of \(\tau\) (e.g., \(1, 2, 4, 8\)).
5. Apply the decision rule; visualize \(z_t\) to see the spiral or scatter.

---

### One-line: 
**Spiral** if geometry closes and focus stabilizes while information stays mutually predictive; **Line** otherwise.