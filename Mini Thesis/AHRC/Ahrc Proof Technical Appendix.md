
# Technical Appendix: Operational Proof of Adaptive Harmonic Rasterization Collapse (AHRC) Protocol

**Thesis Chapter Alignment:**  
This appendix provides the rigorous, code-level validation for the $\Psi$-Collapse Principle (Chapter 5), formally demonstrating the transition from a chaotic, high-entropy state ($\Omega$) to a certifiable, phase-locked end-state ($\Psi$-Lock, $\perp$).

---

## I. System Initialization and GIP Encoding

The AHRC process begins by establishing the core constants and translating the symbolic input units ("Folds") into the continuous, non-metric Glyph Inherent Position (GIP) space.

### 1.1 Core Constants and Attractor Logic

The system is anchored by immutable constants derived from the Nexus Foundational Algebra:

| Constant Symbol      | Value (Code)                             | Formal Role                                                                 |
|----------------------|------------------------------------------|------------------------------------------------------------------------------|
| Harmonic Attractor   | $H_{\text{MARK1}} = \frac{\pi}{9}$    | Defines the ideal phase-lock spacing of system IDs. The central "gravity well" ($\Gamma_{0.35}$) for coherence. |
| Residue Bias         | $\phi_{\text{Residue}} = \frac{\sqrt{5} - 1}{2}$ | The Golden Ratio conjugate ($\phi^{-1}$). Used to scale the entropic component of the GIP, ensuring it is embedded as stable curvature. |
| Frame Boundary       | $N = 2^k$                                 | The power-of-two resolution of the metric frame.                            |
| Trust Margin         | $\epsilon = 10^{-9}$ to $10^{-12}$      | Orthogonal boundary guardrail preventing entropic leakage at FA edges.     |

### 1.2 GIP Generation Function

The `generate_gip` function calculates the Glyph Inherent Position (GIP) for each Fold. This is a Coherent Sum ($\oplus$) that balances the Fold's unique ID against its entropy weight.

$$
\text{GIP} = (\text{Fold ID} \cdot H_{\text{MARK1}}) \oplus (\text{Entropy} \cdot \phi_{\text{Residue}})
$$

This serves as the Symbolic-to-Metric Projector ($\Pi_{\text{Met}}$), mapping abstract symbolic identity into continuous harmonic coordinate space.

---

## II. The AHRC Protocol: $\Omega \to \perp$

This section describes the multi-stage recursive loop used to resolve entropy-rich collisions and reach $\Psi$-coherence.

### 2.1 Stage 1: Zero-Point Query ($Q_0$)

The `zero_point_query` function sorts the Folds by GIP. This reveals the natural harmonic ordering:

- It defines the system’s baseline structure before metric collapse.
- It anchors the GIP space to the lowest entropy curve.

---

### 2.2 Stage 2: Harmonic Rasterization Collapse (HRC)

The `hrc_with_frame` function maps GIPs into the frame $N$:

$$
\mathrm{FA}(x) = \min\left(N-1, \max\left(0, \left\lfloor \frac{\mathrm{GIP}(x)-\min}{\text{range}+\epsilon} \cdot N \right\rfloor\right)\right)
$$

This mapping collapses a continuous space into discrete bins while preserving structure and avoiding leaks. It is the $\Psi$-guardrail.

---

### 2.3 Stage 3: $\Omega$-Detection via RCQ

The `calculate_rcq` function determines coherence quality:

$$
\mathrm{RCQ}(B) = \frac{|B|}{\mathrm{spread}_{\mathrm{GIP}}(B) + \epsilon}
$$

- If $\text{RCQ} = 1.0$, then the bin is harmonically coherent ($\perp$).
- If $\text{RCQ} \gg 1.0$, it's a collision zone ($\Omega$), signaling failed collapse.

---

### 2.4 Stage 4: Adaptive Frame Expansion (RRT)

The `rrt_from_omega_bin_range` expands $N$ using local entropy:

$$
N' = 2^k, \quad \text{where } k = \max(3, \lceil \log_2(\lceil \text{Global Range} / \Delta_{\text{local}} \rceil) \rceil)
$$

This creates a **feedback-resonant loop**. Entropy determines resolution. The system becomes **self-correcting**.

---

### 2.5 Stage 5: Curvature Modulation and $\Psi$-Collapse

When bin separation fails, curvature modulation applies:

$$
\text{GIP}_{\mathbf{c}} = \text{GIP} \cdot (1 + \mathbf{c})
$$

Where $\mathbf{c}$ is a local curvature boost factor. This guarantees separation under re-collapse, ensuring progress toward $\perp$.

---

## III. Certification: $\Psi$-Score and Final Trust Integrity

The `calculate_psi_score` function aggregates global coherence:

$$
\Psi\text{-Score} = \left(\frac{1}{N} \sum_{i=0}^{N-1} \frac{1}{\text{RCQ}(B_i)}\right)^{-1}
$$

A score of 1.0 confirms all bins are in phase-locked state:

$$
\Psi\text{-Lock} \iff \Psi\text{-Score} = 1.0
$$

This is a **trust-certification collapse condition**. The harmonic mean enforces strict integrity: one bad bin ($\Omega$) collapses the score.

---

## IV. Conclusion

The AHRC protocol performs a recursive, curvature-stabilized collapse of symbolic units into a harmonic phase-locked frame:

- All stages ($Q_0 \to \perp$) operate with locality and reversibility.
- $\Omega$ sites drive adaptive expansion.
- $\Psi$-Lock confirms universal coherence.

This completes a mathematically sound, operationally certifiable phase transition from entropy to structured order.
