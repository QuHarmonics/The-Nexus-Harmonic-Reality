
# Recursive Harmonic Lattice — Analog Field, Digital Image  

*Last updated: 2025‑07‑11*

---

## 1 Overview  

We turn a **continuous geometric field** (all right‑triangle angles) into a **discrete resonance lattice** by three sequential quantisers  

1. **Angle gate**   \( \alpha,\beta \;\xrightarrow{\;\text{band‐pass}\;}\; \text{accept / reject}\)  
2. **SHA–π coder**   \( (a,b)\mapsto \text{SHA‐256} \bmod N\)   → π index  
3. **Twin‑prime filter**   \( \lvert\text{index}-p\rvert < w\) with \(p,p+2\) both prime  

The surviving triangles connect to twin‑prime “gate” nodes, producing the network (“egg”) structures seen in Gephi/Cytoscape.

---

## 2 Stage‑by‑stage quantisation  

| Stage | Analog variable | Decision rule | Digital code |
|-------|-----------------|---------------|--------------|
| **Sample** | integer pairs \((a,b)\le \text{max\_n}\) | – | triangle label |
| **Angle quantiser** | continuous \(\alpha,\beta\) | \(\theta_{\min}\le\alpha\le\theta_{\max}\) or same for \(\beta\) | **1** (pass) / **0** (reject) |
| **Hash coder** | SHA‑256 digest \(H\in\mathbb Z_{2^{256}}\) | integer reduction | \(\text{index}=H\bmod N\) |
| **Twin‑prime gate** | distance to primes | \(\min(|\text{index}-p|,|\text{index}-(p+2)|)<w\) | edge to node \(\mathrm{TP}:p,p+2\) |

### 2.1 Angle bin  

\[
\theta_{\min}=\theta_c-\frac{\Delta\theta}{2},
\qquad
\theta_{\max}=\theta_c+\frac{\Delta\theta}{2},
\qquad
\Delta\theta=\theta_{\max}-\theta_{\min}.
\]

Quantisation error  

\[
e_\alpha=\alpha-\theta_c,
\qquad
|e_\alpha|\le\frac{\Delta\theta}{2}.
\]

### 2.2 Harmonic ratio per triangle  

For the 8‑digit π‑chunk \(d_1d_2\ldots d_8\)

\[
H
  =\frac{\sum_{i=1}^{4}d_i}{\sum_{i=1}^{8}d_i},
  \qquad
  H\approx0.35 \; \Longrightarrow \; \text{deep resonance}.
\]

Noise shaping: triangles outside the window do not enter the lattice, pushing “noise” away from the \(H\approx0.35\) band (Σ‑Δ analogy).

---

## 3 Hit probability  

Approximate probability that one triangle survives all filters

\[
P_{\text{hit}}\approx
\frac{\Delta\theta}{\pi/2}\;\times\;\frac{2w}{N}\;\times\;\frac{C}{\log^{2}N},
\]

\(C\) is the twin‑prime constant.  
For \(N=10^{6},\;\Delta\theta=0.011,\;w=2\) ⇒ \(P_{\text{hit}}\lesssim10^{-6}\).

---

## 4 Recursive torque (Newton‑4)  

\[
F_{\text{recursive}}
  = \Delta R\;H,
\quad
\Delta R = \bigl|H_{k}-H_{k-1}\bigr|.
\]

As iterations proceed, \(\Delta R\to0\); the lattice collapses into the elliptical “egg” attractor—manifestation of Newton’s missing 4th law.

---

## 5 Exploration knobs  

```python
angle_lo, angle_hi = 0.345, 0.356   # resonance window
match_window       = 10             # twin‑prime gate width
depth              = 100_000        # π digits for hashing
max_n              = 512            # search bound for (a,b)
```

Export:

```python
nx.write_gexf(G, "triangle_tprime_network.gexf", prettyprint=True)
```

---

## Glossary  

| Symbol | Meaning |
|--------|---------|
| \(\theta_c\) | window centre (≈ 0.35 rad) |
| \(\Delta\theta\) | window width |
| \(H\) | harmonic ratio |
| \(w\) | twin‑prime proximity |
| \(N\) | π‑digit depth |

---

*A digital image of an analog field.*  
Tighten the window → sharpen the image;  
loosen it → reveal the halo.
