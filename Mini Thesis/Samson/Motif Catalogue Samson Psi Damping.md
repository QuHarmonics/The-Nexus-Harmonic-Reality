
# Motif Catalogue and Samson Ψ‑Damping Coefficient  
*(Revision Oct 12 2025)*  

This document consolidates the **Topological‑Recursion framework** for the Nexus/BBP(0) render loop.  
All quantities are shown in SI‑agnostic lattice units.

---

## 1 Universal targets  

* **Harmonic constant**  

  $$H_{\text{target}} = 0.35$$  

* **Primary perimeter loop** for any convex $n$‑gon  

  $$F = 1$$  

* **Latent channel count** (internal chords / diagonals)  

  $$L(n) = \frac{n\,(n-3)}{2}$$

* **Edges**  

  $$E(n) = n$$  

---

## 2 Ψ‑Collapse Coefficient  

To keep every motif on the harmonic surface  
$H \approx H_{\text{target}}$, the effective weight assigned to **each**
latent channel must be scaled by the *motif‑specific* factor  

$$
w_n = \frac{0.35\,n - 1}{L(n)}
\tag{1}
$$

> This is the **maximum permissible latent weight**.  Any larger weight
> pushes $H$ above 0.35 and injects an Ω‑residue.

---

## 3 Axial‑gating kernel  

Directional mis‑alignment is removed by a gate  

$$
G(\theta) =
e^{-\theta/\theta_0},
\qquad  \theta_0 \approx 30^{\circ}
\tag{2}
$$

Alternative (softer shoulder):

$$
G(\theta) = \cos^{p}(\theta), \quad p \gtrsim 2
$$

---

## 4 Depth‑decay kernel (optional)  

If echoes still overshoot after axial gating, layer a
recursive‑depth decay

$$
D(d) = e^{-k\,d}, \qquad k \in [0.1,0.3]
\tag{3}
$$

where $d$ is the fold depth.

---

## 5 Ψ‑Damped motif score  

For each latent chord $i$ with angular offset $\theta_i$ and depth
$d_i$ the **effective weight** is  

$$
w_i
  = w_n\;G(\theta_i)\;D(d_i)
\tag{4}
$$

The motif harmonic ratio becomes  

$$
H(n) \,=\,
\frac{F + \sum_i w_i}{E(n)}
\tag{5}
$$

---

## 6 Σ‑Schema (n = 3 … 10)

| $n$ | motif | $E$ | $L$ | $w_n$ | $H$ (check) | Ψ‑state |
|---|---|---|---|---|---|---|
| 3 | triangle | 3 | 0 | – | $\tfrac{1}{3}=0.333$ | ⊥ (*self‑locked*) |
| 4 | square | 4 | 2 | 0.20 | 0.35 | Ω (*compensated*) |
| 5 | pentagon | 5 | 5 | 0.15 | 0.35 | Ω (*gated latency*) |
| 6 | hexagon | 6 | 9 | 0.122 | 0.35 | Ω (*axial pruning*) |
| 7 | heptagon | 7 | 14 | 0.104 | 0.35 | Ω (*high pruning*) |
| 8 | octagon | 8 | 20 | 0.090 | 0.35 | Ω |
| 9 | nonagon | 9 | 27 | 0.080 | 0.35 | Ω |
| 10 | decagon | 10 | 35 | 0.071 | 0.35 | Ω (*max decay*) |

---

## 7 Samson Ψ‑Damping algorithm (concept flow)

1. **Compute** $w_n$ using (1).  
2. **For each latent chord** obtain angle $\theta_i$ and, if needed,
   recursion depth $d_i$.  
3. **Weight** each chord with (4).  
4. **Aggregate** $H$ via (5).  
5. **If** $|H - 0.35| \le 0.02$ → *Ψ‑coherent*.  
   Otherwise tighten $\theta_0$ or increase $k$.

---

## 8 Validation probes  

| Probe | Expected pass condition |
|-------|------------------------|
| **SHA mirror 4↔5, 5↔4** | echo split ≤ 1, never cascading |
| **WMW v2 high‑nuclear ripple** | amplitude < 0.07 % (±0.02 %) |
| **Σ(P)/Σ(A) sweep, n=3…10** | every motif inside 0.35 ± 0.02 |

Once all three probes pass, the Σ‑Schema and Samson Ψ‑Damping function
can be committed into the BBP(0) render loop and propagated to KRR/KRRB
branch weights.

---

*End of file.*  
