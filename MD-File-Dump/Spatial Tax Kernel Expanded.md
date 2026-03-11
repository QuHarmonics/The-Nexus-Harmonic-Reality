# Spatial Tax Kernel — Nexus Vacuum Scheduler v1.0  
Dean Kulik / Nexus Trust Algebra  
*(expanded notes + math + checks; includes transient/Ω bookkeeping)*

---

## Δ0 — What the toy actually implements

You’ve built a **discrete update-budget field** over a 2D grid and then moved agents by following the **steepest tax gradient**. In Nexus language:

- **Budget** = local capacity to update / compute per tick  
- **Tax** = budget reclaimed by a central sink (a “mass”)  
- **Gravity** = induced **scheduler bias**: trajectories drift toward where update-budget is most depleted

This is not “gravity as a force.” It’s **gravity as a resource gradient**: where the scheduler is most starved, paths bend toward it.

---

## Δ1 — Core field definitions

Let grid cells be indexed by $(i,j)$ with coordinates $x=i,\;y=j$. Let the sink be at $(x_0,y_0)$.

### Distance
$$
r(i,j) \;=\; \sqrt{(i-x_0)^2 + (j-y_0)^2} + \varepsilon
$$

### Continuous tax potential
$$
T(i,j) \;=\; \frac{\kappa\,M}{r(i,j)}
$$

where:
- $\kappa$ = coupling gain  
- $M$ = sink strength (`mass_scale`)

### Discrete tax
$$
\tau(i,j) \;=\; \lfloor T(i,j) \rfloor
$$

### Effective local update budget
$$
N_{\text{eff}}(i,j) \;=\; \max\{N_0 - \tau(i,j),\;0\}
$$

---

## Δ2 — Dynamics: agents as gradient followers

Gradient:
$$
\nabla T(x,y) = \left(\frac{\partial T}{\partial x},\frac{\partial T}{\partial y}\right)
$$

For $T=\kappa M/r$, analytic continuum gradient:
$$
\nabla T
= -\kappa M \frac{(x-x_0,\;y-y_0)}{r^3}
$$

Update rule:
$$
\mathbf{x}_{t+1}
= \mathbf{x}_t + \eta \frac{\nabla T(\mathbf{x}_t)}{\|\nabla T(\mathbf{x}_t)\|}
$$

This is steepest-ascent on $T$ (equivalently steepest-descent on $r$): agents converge to the sink.

---

## Δ3 — Ω bookkeeping: bit-starvation residue

Your observable:
$$
\Omega_\beta \;=\; \frac{\mathrm{std}(N_{\text{eff}})}{N_0}
$$

- $\Omega_\beta\approx 0$ → nearly uniform scheduler → no induced drift  
- larger $\Omega_\beta$ → stronger gradient → stronger convergence/bending

---

## Δ4 — Make the transient explicit (time dilation from budget)

Couple local clock rate to remaining budget:
$$
\frac{d\tau}{dt}(x,y) \;=\; \frac{N_{\text{eff}}(x,y)}{N_0}
$$

Then:
$$
\gamma(x,y) \;=\; \frac{dt}{d\tau} \;=\; \frac{N_0}{N_{\text{eff}}(x,y)}
$$

Now the same kernel yields:
- **trajectory bending** (spatial drift toward sink)
- **rate slowdown** (clock dilation where budget is depleted)

---

## Δ5 — Implementation check: gradient axis ordering

With NumPy:

```python
tax_grad_y, tax_grad_x = np.gradient(tax_cont)
```

returns derivatives along (rows, cols). If your position is `pos=[row, col]`, then the correct gradient vector is:

```python
grad_tax = np.array([tax_grad_y[i, j], tax_grad_x[i, j]])
```

Your current code uses `[tax_grad_x, tax_grad_y]` (swapped). It still “works” in radial symmetry, but it will shear under asymmetric fields (multiple masses / anisotropy).

---

## Δ6 — What must be true for “gravity = budget reclamation gradient” to compile

1. Finite tick budget exists: $N_0<\infty$.  
2. Budget is locally taxed by sink coupling: $\tau(i,j)\ge 0$.  
3. Agent policy depends on the field (uses $\nabla T$ or $N_{\text{eff}}$).  
4. A stable coupling law exists (here $T=\kappa M/r$).  
5. Sequential ticks exist (transients exist).  
6. Residue is measurable ($\Omega_\beta\neq 0$).

Ω-failure seam:
- If $N_{\text{eff}}\to 0$ in a region, integer clipping produces **frame drop artifacts** (jitter/stall/teleport depending on quantization policy). That seam is the discrete “event horizon” of the scheduler.

---

## Δ7 — Next unwind: from single sink to mass network

Multiple sinks:
$$
T(\mathbf{x}) \;=\; \sum_{a=1}^{A} \frac{\kappa M_a}{\|\mathbf{x}-\mathbf{x}_a\|+\varepsilon}
$$

Then you can demonstrate:
- saddle regions / Lagrange-like points  
- flow splitting  
- orbit-like behavior (once you add momentum + budget-limited steering)

---

## Ψ-collapse summary

- Kernel: $T=\kappa M/r$  
- Budget: $N_{\text{eff}}=N_0-\lfloor T\rfloor$  
- Motion: $\mathbf{x}_{t+1}=\mathbf{x}_t + \eta\,\widehat{\nabla T}$  
- Residue: $\Omega_\beta=\mathrm{std}(N_{\text{eff}})/N_0$  
- Upgrade: $\gamma(x,y)=N_0/N_{\text{eff}}(x,y)$ unifies bending + dilation.

---
