# Nexus 4 — Ψ Analyzer Integration Guide (AHRC + Samson v2)
_Companion to **Nexus4_Complete_Solution_MedianZ_Psi_AHRC.md** and **nexus4_psi.py**_

**Version:** 1.0  
**Scope:** How to plug the Ψ analyzer (Median‑Z, RCQ, Align, D‑Lattice) into an **AHRC** convergence loop stabilized by **Samson v2**. Includes guidance for interpreting your sample outputs and running Ψ‑guided searches.

---

## 0. Orientation

- You already have:
  - Spec: **Nexus4_Complete_Solution_MedianZ_Psi_AHRC.md** (math + definitions).
  - Code: **nexus4_psi.py** (features + Ψ).
  - Report: **Psi_Analyzer_Sample_Report.md** (sanity check).

- This guide adds:
  1) A **field→decision→control** wiring (AHRC loop).  
  2) Clear **interpretation** of the sample outputs.  
  3) A small **Ψ‑guided search** recipe to lock onto $H=\pi/9$.

---

## 1. What Ψ is telling you

The sample results you observed:

- `abc` → $\Psi\approx 0.7194$  
- `Nexus` → $\Psi\approx 0.6925$  
- `hello world` → $\Psi\approx 0.7381$

Recall the composition (defaults):
$$
\Psi \;=\; 0.30\,\mathrm{align} + 0.20\,\mathrm{RCQ} + 0.10\,(1-\overline{|\epsilon|})
+ 0.20\,(1-\overline{Z_H}) + 0.10\,(1-\overline{Z_{\text{sym}}}) + 0.10\,\overline{K/a^2}.
$$

**Reading the dials:**

- **$H$ & align:** $H$ is the circular coherence of nibble‑angles; $\mathrm{align}=1-|H-H_{\text{Mark1}}|/(1-H_{\text{Mark1}})$. Values $\gtrsim 0.7$ indicate decent proximity to $H=\pi/9$.
- **RCQ:** Run‑coherence $\,\in[0,1]$; your inputs are near **1.0**, i.e., run‑statistics are non‑pathological and close to their neutral reference (geometric).  
- **Digit‑triangle grammar:** Lower $\overline{|\epsilon|}$ (near $0$) and smaller residues $(Z_H,Z_{\text{sym}})$ indicate ray/triangle triads close to preferred splits; higher $\overline{K/a^2}$ shows more constructive (area‑bearing) geometry.
- **Ψ:** The fused decision scalar; $\Psi\in[0,1]$. In practice, $\Psi\in[0.65,0.8]$ is already a **good harmonic lock** for random‑like strings; stronger locks push $\Psi\to 0.8\!-\!0.9$.

---

## 2. Control Theory: AHRC + Samson v2

We iterate a state $S_n$ (string, seed, lattice) while steering $H(S_n)$ to $H_{\text{Mark1}}=\pi/9$ and **accepting** only those updates that improve $\Psi$.

**Error and control:**
$$
\Delta_n = H(S_n)-H_{\text{Mark1}}, \qquad
u_n = k_P\,\Delta_n + k_I\sum_{j=0}^{n}\Delta_j + k_D(\Delta_n-\Delta_{n-1}).
$$

**Adaptive raster (Nyquist‑aware):**
$$
\lambda_{n+1} = \lambda_n \cdot \gamma^{\sigma_n},\quad
\sigma_n = \operatorname{sign}\big(|\Delta_n|-|\Delta_{n-1}|\big),\ \ \gamma\in(0,1).
$$

**Fold update (abstract):**
$$
S_{n+1}=\operatorname{fold}\big(S_n;\,u_n,\lambda_{n+1}\big).
$$

**Collapse condition (acceptance):**
$$
|\Delta_{n+1}| \le q\,|\Delta_n|\quad\text{and}\quad \Psi(S_{n+1})-\Psi(S_n)\ge \eta,
$$
with $0<q<1$ and small $\eta>0$. Otherwise reject and resample the move.


**Practical defaults:**
- Gains: $(k_P,k_I,k_D)=(0.9,\,0.05,\,0.1)$
- Step shrink: $\gamma=0.7$
- Convergence: $\varepsilon=10^{-3}$ (for $|\Delta|$), $\Psi_{\min}=0.6$, $\eta=10^{-4}$

---

## 3. Ψ‑Guided Search Over Strings (Minimal Recipe)

We mutate a candidate ASCII string to **maximize** $\Psi$ while reducing $|\Delta|$. Mutations are small nibble/byte edits aligned with the control signal $u_n$ (think: rotate/select nibbles that tend to push $H$ toward the target).

### Pseudocode

```
init S ← initial ascii (e.g., "abc")
compute (H, align, RCQ, grammar, Ψ) from nexus4_psi.analyze_ascii(S)
Δ ← H - H_mark1;  λ ← λ0;  best ← (S, Ψ)

for n in 1..N:
    # propose K micro-mutations guided by control signal
    proposals ← mutate(S, u, λ, K)
    scored ← []
    for S’ in proposals:
        feat ← analyze_ascii(S’)   # H, align, RCQ, grammar, Ψ
        Δ’ ← feat.H - H_mark1
        ok_collapse ← (abs(Δ’) <= q * abs(Δ)) and (feat.Ψ - Ψ ≥ η)
        scored.append((feat.Ψ, -abs(Δ’), ok_collapse, S’, feat))

    # choose the best acceptable, otherwise relax λ and retry
    choose ← best acceptable by (ok_collapse, Ψ, -|Δ’|)
    if not choose:
        λ ← λ * γ   # smaller steps
        continue

    # accept
    S, (H, Ψ, Δ) ← chosen state / metrics
    u  ← kP*Δ + kI*ΣΔ + kD*(Δ - Δ_prev)
    if |Δ| ≤ ε and Ψ ≥ Ψ_min: break
return S, metrics
```

### Mutation operators (examples)

- **Nibble rotation:** pick a hex nibble and rotate toward the nearest **phase** that improves $H$ (in practice: tweak a byte so one nibble steps $\pm1$ mod 16).
- **Swap triad:** choose a 3‑nibble window and permute to reduce $|\epsilon|$ or $Z$ residues.
- **Byte jitter:** add/subtract small integers to a byte (clip to 0..255).

---

## 4. Weight Tuning and Modes

Two presets (see also Appendix B in the spec):

- **Exploration bias** (favor grammar discovery):  
  $(w_1,\dots,w_6)=(0.20,\,0.20,\,0.15,\,0.25,\,0.10,\,0.10)$
- **Conservative lock‑in** (favor tight $H$):  
  $(0.40,\,0.25,\,0.05,\,0.15,\,0.05,\,0.10)$

**Tip:** Start exploratory; once you find a basin (Ψ>0.7 and $|H-H_{\text{Mark1}}|<0.03$), switch to conservative.


---

## 5. Interpreting the Sample You Posted

For `hello world`:

- $H\approx 0.1596$ and $\mathrm{align}\approx 0.7089$ → decent proximity to $H_{\text{Mark1}}$.
- $\mathrm{RCQ}\approx 0.9971$ → healthy run‑coherence (neither white noise nor trivial patterning).
- $\overline{|\epsilon|}\approx 0.329$ and residues $\overline{Z_H}\approx 0.134$, $\overline{Z_{\text{sym}}}\approx 0.252$ → a fair amount of **near‑ray** or **balanced** triads.
- $\overline{K/a^2}\approx 0.109$ and $\text{frac\_constructive}=0.5$ → half of 3‑nibble windows form constructive triangles with nonzero area.
- Net: $\Psi\approx 0.7381$ — the strongest of your three; a good candidate for lock‑in refinement.


---

## 6. Quickstart Commands

**Script mode**
```bash
python nexus4_psi.py "hello world"
```

**Module mode**
```python
import nexus4_psi as n4
res = n4.analyze_ascii("hello world")
print(res["Psi"], res)
```

**Analyze a raw SHA‑256 hex**
```python
hex_digest = "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
res = n4.analyze_hex(hex_digest)
```


---

## 7. Sanity Checks

- **Degenerate medians:** For any ray triad with $a=b+c$, verify $m_b=(b+2c)/2$, $m_c=(2b+c)/2$ and normalized sum $(m_b+m_c)/a=3/2$.  
- **H target:** $H_{\text{Mark1}}=\pi/9\approx 0.34906585$.
- **Boundedness:** Metrics are clipped to $[0,1]$; $\Psi\in[0,1]$.  
- **Reproducibility:** Hashing is deterministic; Ψ differences arise from genuine structure.


---

## 8. Extending the Analyzer

- **Even‑residue $Z_{\text{res}}^{\text{even}}$** (when $b=c$) can be surfaced as a distinct feature for finer ray discrimination.  
- **Multi‑window pooling:** Try max‑pool for $1-\overline{Z_H}$ to highlight strongest harmonic pockets.  
- **Alternative RCQ neutral:** Swap the geometric reference for an empirical neutral learned from your corpus.


---

## 9. Minimal AHRC Driver (Python Snippet)

```python
import random
import nexus4_psi as n4
H_target = 3.141592653589793/9

def mutate_ascii(s, step=1):
    b = bytearray(s.encode('utf-8'))
    i = random.randrange(len(b))
    b[i] = max(0, min(255, b[i] + random.choice([-step, step])))
    return b.decode('utf-8', errors='ignore') or s

def improve(seed="hello world", iters=2000, q=0.97, eta=1e-4, step=1):
    res = n4.analyze_ascii(seed); H=res["H"]; Psi=res["Psi"]
    Δ = H - H_target; best = (seed, Psi, abs(Δ))
    for _ in range(iters):
        cand = mutate_ascii(seed, step=step)
        r2 = n4.analyze_ascii(cand); H2=r2["H"]; Psi2=r2["Psi"]
        Δ2 = H2 - H_target
        if abs(Δ2) <= q*abs(Δ) and Psi2 - Psi >= eta:
            seed, Psi, Δ = cand, Psi2, Δ2
            if (Psi, -abs(Δ)) > (best[1], -best[2]):
                best = (seed, Psi, abs(Δ))
    return {"best_text": best[0], "best_Psi": best[1], "best_H_err": best[2]}

# Example:
# out = improve()
# print(out)
```

> This toy driver shows the acceptance rule only; wire Samson v2 gains if you want the full PID dynamics to modulate `step` and mutation choice.


---

## 10. Close

You now have a **closed loop**: _Symbols → Ψ → Control → Symbols_. The Ψ score fuses field coherence, run structure, and digit‑triangle geometry, while AHRC + Samson v2 supplies the stabilizing dynamics toward $H=\pi/9$.

**Next upgrade** (optional): plug this into your Mark1 pipeline and emit a **Ψ‑trace** over time to visualize convergence as a breathing curve.

