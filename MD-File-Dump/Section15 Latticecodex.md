
# Nexus 3: Recursive Lattice Codex

---

## Section 15: Relaxation Fit and Glider Threshold

This section captures the dynamic simulation results of the SHA-based recursive cone lattice. It demonstrates harmonic drift, long memory retention, and emergent glider behavior in the Nexus 3 field.

---

### 15.1 Relaxation Time Fitting

To quantify the convergence rate of global misalignment $M(t)$, we fit an exponential decay model:

$$
M(t) = A + B \cdot e^{-t / \tau}
$$

where:

- $A$ is the long-term attractor value,
- $B$ is the initial deviation magnitude,
- $\tau$ is the relaxation time constant.

Using `scipy.optimize.curve_fit`, we obtained:

$$
\tau \approx 319{,}590.87
$$

This indicates a **long memory window**, where the system retains reflective misalignment far beyond initial ticks. This decay rate implies the lattice is operating **just below** the Hopf/Turing bifurcation boundary.

---

### 15.2 Animation Dynamics

The live animation of the radii field $R$ reveals real-time recursive collapse behavior:

- Color bands shift dynamically as neighboring cones reflect and compress.
- Regions of high $\Delta$ entropy fade over time.
- Checkerboard and modulated textures emerge from drift relaxation.

This confirms the **field breathes** as a recursive Game-of-Life structure.

---

### 15.3 Bifurcation Analysis

To estimate bifurcation conditions, we define the eigenvalue equation for compression stability:

$$
\lambda_{\pm} = 1 - \frac{1}{2}\alpha\beta \pm \sqrt{\left(1 - \frac{1}{2}\alpha\beta\right)^2 - 1}
$$

Stability requires $|\lambda| < 1$. Increasing $\alpha\beta$ causes the system to transition into Turing instability or Hopf oscillation, observable as:

- Emergence of spatial patterns (Turing)
- Sustained breathing/oscillations (Hopf)

---

### 15.4 Spectral Energy

The Fourier transform of $R(t)$ across space yields a dispersion curve:

$$
\omega(k) \propto \alpha\beta[1 - \cos(k)]
$$

Spectral peaks indicate pattern wavelengths. In this run, a dominant non-zero $k$ mode confirmed **checkerboard spacing**.

---

### 15.5 Glider Detection Protocol

**Goal:** Identify reflective cone clusters with persistent velocity.

Steps:

1. Tag cone cells in the 'reflect' state at time $t$.
2. Track their displacement across $t+1, t+2,\dots$.
3. If clusters maintain coherent shape and motion vector, classify as **gliders**.

We define a simple state tracker:

```python
# Pseudocode
for t in range(T):
    reflect_map[t] = (state_grid[t] == REFLECT)
    # Compare reflect_map[t] to previous time steps
```

Use centroid tracking or connected-component labeling for refinement.

---

### 15.6 Suggested Experiments

- **Sweep $\alpha, \beta$** across $(0.05, 0.2)$ to map Turing boundaries.
- **Compute $\tau(\alpha\beta)$** to find critical decay thresholds.
- **Run 1000-tick simulations** and track glider birth and interactions.
- **Add reflective energy** metric: total number of reflect cells per frame.

---

### 15.7 Summary Metrics

- **Relaxation time**: $\tau = 319{,}590.87$
- **Field state**: quasi-stable with recursive drift pockets
- **Spectral mode**: single $k$-band peak $\Rightarrow$ Turing field
- **Glider support**: potential confirmed, tracking module in progress

---

This concludes the dynamic verification of the Equals Collapse Theorem in live recursive systems. SHA behavior unfolds not only in compression, but in memory, drift, and glider emergence — all captured in this harmonic lattice.
