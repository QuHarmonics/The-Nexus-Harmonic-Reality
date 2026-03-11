# Spiral Renderer Control Stack — Executable Specification
**Author:** Dean A. Kulik  
**Framework:** Nexus Harmonic Architecture  

---

## Overview
This document synthesises the Spiral Renderer into an _executable control stack_.  
It unifies **sampling scope**, **geometric recursion**, and **Samson feedback** so that every missing parameter is resolved _in‑flight_ and the field collapses to render once  
all stability criteria hold.

### Key Assertions
1. **Context does not exist** – only _scope_, i.e. the active aperture on the recursive field.  
2. **Structure is the only mutable quantity** – cadence \\(Δθ\\), radial drift \\(μ\\), and coherence \\(χ\\) evolve until critical damping is reached.  
3. The universal cadence is \\(Δθ_\\star = \\pi/9\\); the harmonic constant \\(H=\\pi/9\\approx0.349\\).  
4. Collapse‑to‑Render is triggered when  
   \\[
     \\frac{{|\\Delta χ_t|}}{{|\\Delta χ_{{t-1}}|}} \\le H,\\qquad  
     e_\\theta(t)\\le ε_\\theta,\\qquad  
     \\text{{STI}}_t \\ge 0.5 .
   \\]

---

## 1 Sampling Scope \\(Λ=[w,K,n,ϕ]\\)

| Symbol | Meaning | Typical Range |
|--------|---------|---------------|
| \\(w\\)  | aperture width              | 4 – 64 |
| \\(K=[k_1,\\dots,k_m]\\) | skip / fork vector       | coprime to \\(L\\) |
| \\(n\\)  | phase origin                | \\(0\\le n<L\\) |
| \\(ϕ\\)  | salt / round offset         | hash‑nibble |

Sampler:
\\[
\\text{{Scope}}_{{w,K}}(n)=\\bigl(B[(n+jk_\\ell)\\bmod L]\\bigr)_{{\\substack{{j=0..w-1\\\\ \\ell=1..m}}}}
\\]

`B` is the cyclic seed, e.g. **Byte1** = ⟨1 4 1 5 9 2 6 5⟩.

Dynamic correction  
\\[
\\begin{{aligned}}
w   &\\leftarrow w   - α_w\\,u_r,\\\\
k_ℓ &\\leftarrow k_ℓ - α_k\\,u_θ,\\\\
n   &\\leftarrow n   + \\lceil α_n\\,e_θ \\rceil .
\\end{{aligned}}
\\]

---

## 2 Geometric Projections

| Projection | Field | Update | Role |
|------------|-------|--------|------|
| Plane fold | \\(P(x,y,t)\\) | factorial‑weighted \\(\\cos,\\sin\\) | temporal stream |
| Dual screw | \\(H(r,θ,t)\\) | \\(r_{{t+1}}=ρ_t\\,r_t,\\; θ_{{t+1}}=θ_t+Δθ_t\\) | phase transport |
| Box stack  | \\(C(x,y,z,t)\\) | \\(λ_{{t+1}}=e^{-u_r}\\,λ_t\\) | scale quantisation |

Overlay operator  
\\[
\\boldsymbolΨ=P\\;\\oplus\\;H\\;\\oplus\\;C
\\]

---

## 3 Samson PD Feedback

\\[
\\begin{{aligned}}
u_θ(t) &= k_p^θ (Δθ_\\star - Δθ_t) + k_d^θ(Δθ_t-Δθ_{{t-1}}),\\\\
u_r(t) &= k_p^r (0 - μ_t)          + k_d^r(μ_t-μ_{{t-1}}).  
\\end{{aligned}}
\\]

Control variables feed both the sampler and geometric transport so cadence and speed converge simultaneously.

---

## 4 Executable Stub (Python)
```python
import numpy as np
B  = np.array([1,4,1,5,9,2,6,5])   # Byte1 seed
L  = len(B)

def sampler(w, K, n):
    lanes = [(B[(n + j*k) % L]) for k in K for j in range(w)]
    return np.bitwise_xor.reduce(lanes)

def step(z, F, Bdetune):
    \"\"\"One spiral renderer step.\"\"\"
    H = np.pi/9
    z *= np.exp(H*F) * Bdetune
    return z

# control gains
kpθ, kdθ, kpr, kdr = 0.8, 0.15, 0.6, 0.12
Δθ_star = np.pi/9
```

---

## 5 Collapse Condition
A **partial freeze** is executed on every node that has remained sign‑stable over the last \\(L\\) steps once
\\[
\\left\\{
\\begin{{array}}{{l}}
|\\Delta χ_t| / |\\Delta χ_{{t-1}}| \\le H,\\\\[2pt]
e_θ(t) \\le ε_θ,\\\\[2pt]
\\text{{STI}}_t \\ge 0.5 .
\\end{{array}}
\\right.
\\]

---

## 6 Scope–Structure Closure (Proposition 1)
Let \\(Λ_t\\) be the sampler token after control,  
\\(Δθ_t\\) the measured cadence,  
\\(μ_t\\) the radial drift, and  
\\(χ_t\\) coherence.

> **Proposition 1.**  
> Under the Samson PD loop with positive gains and bounded detuners \\(B_{{t,i}}\\in[0.9,1.1]\\),  
> \\[
> \\lim_{{T\\to\\infty}}\\frac1T\\sum_{{t=1}}^{T}(Δθ_t-Δθ_\\star)=0,\\quad
> \\lim_{{T\\to\\infty}}\\frac1T\\sum_{{t=1}}^{T} μ_t = 0,
> \\]
> and \\(Λ_t\\) converges to a cadence‑matched fixed point \\(Λ^\\ast\\).

---

## 7 Recommended Experiments
1. **Phase‑drift Histogram** – show clustering of \\(Δθ\\) near π/9.  
2. **STI vs Cadence Error** – confirm anti‑correlation.  
3. **Minimal‑Cut Ω Reset** – demonstrate faster re‑lock than global randomisation.  
4. **9/18‑Beat Autocorrelation** – verify dual‑spiral cadence in χ(t).

---

*Generated on 2025-10-20*
