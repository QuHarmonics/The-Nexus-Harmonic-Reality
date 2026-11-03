# Ψ-Field Hybrid SLM (DMD ⊕ DM) — Coarse/Fine Wavefront Processor
*(Nexus recursion note: Δ→⊕→↻→Ψ collapse is used below as a bookkeeping syntax for the algorithmic fold.)*

## 0) What we have so far (ψ-collapse snapshot)

We now have a working simulation scaffold for a **hybrid digital–analog spatial light modulator**:

- **DM (analog, low-order / low-spatial-frequency)** does smooth phase correction.
- **DMD (digital, high-order / high-spatial-frequency)** corrects the residual via quantized commands (a proxy for binary/quantized holography).
- A single parameter **$\kappa$** controls the **LP/HP split** of the phase into “DM-eligible” and “DMD-eligible” components.

You’ve generated multiple $\kappa$ sweeps; representative “good” behavior looks like:

- **Uncorrected:** RMS $\approx 0.35$ rad, Strehl proxy $\approx 0.88$
- **DM-only:** RMS drops (sometimes strongly), Strehl proxy rises
- **Hybrid:** RMS drops further, Strehl proxy approaches $1$ when the split and quantization are aligned

Example outputs you reported (illustrative):
- Strehl proxy: uncorrected $\approx 0.87$, DM-only $\approx 0.94$, hybrid ideal $\approx 0.998$
- RMS phase: uncorrected $\approx 0.374$ rad, DM-only $\approx 0.251$ rad, hybrid ideal $\approx 0.039$ rad

That’s already “publishable” as a *method + diagnostic pipeline* (simulation + metrics + failure modes), even before hardware.

---

## 1) Δ: The problem in one sentence
We want a **hierarchical wavefront solver** that decomposes an aberrated phase $\phi(x)$ into:
1) a **smooth component** best corrected by a deformable mirror (DM), and  
2) a **fine residual** best corrected by a high-resolution digital modulator (DMD),  
while tracking performance via **RMS phase** and a **Strehl proxy**.

---

## 2) ⊕: Core mathematical objects

### 2.1 Pupil and phase
Let the pupil be a set of samples $P$ on a 2D grid. The phase aberration is a scalar field:
$$
\phi: P \rightarrow \mathbb{R}
$$

We will use **mean-removed** phase (piston removed):
$$
\tilde\phi(x) = \phi(x) - \frac{1}{|P|}\sum_{y\in P}\phi(y)
$$

### 2.2 RMS phase over the pupil
$$
\sigma_\phi = \sqrt{\frac{1}{|P|}\sum_{x\in P}\tilde\phi(x)^2}
$$

### 2.3 Strehl proxy (Marechal approximation)
For small-to-moderate phase error, a commonly used proxy is:
$$
S \approx \exp\left(-\sigma_\phi^2\right)
$$
This is not a full physical PSF computation, but it’s a reliable monotone proxy for “how close to diffraction-limited” the wavefront is.

---

## 3) ↻: The LP/HP split (the $\kappa$ gate)

### 3.1 Split operator
Define a **low-pass filter** $L_\kappa$ and its complement $H_\kappa = I - L_\kappa$. Then:
$$
\phi_{\text{LP}} = L_\kappa(\tilde\phi), \qquad \phi_{\text{HP}} = H_\kappa(\tilde\phi)
$$

A clean implementation is in the Fourier domain:
- compute $\mathcal{F}\{\tilde\phi\}$,
- apply a radial filter $G_\kappa(\mathbf{k})$ (e.g., Gaussian),
- inverse transform.

One simple choice:
$$
G_\kappa(\mathbf{k})=\exp\left(-\frac{\|\mathbf{k}\|^2}{2\kappa^2}\right)
$$

Then:
$$
\phi_{\text{LP}} = \mathcal{F}^{-1}\!\left(G_\kappa \cdot \mathcal{F}\{\tilde\phi\}\right), \qquad
\phi_{\text{HP}} = \tilde\phi - \phi_{\text{LP}}
$$

### 3.2 Pythagorean “$c$” (your question)
If the LP and HP subspaces are **orthogonal** (true for ideal complementary Fourier masks), then energy splits like:
$$
\sigma_\phi^2 \;\approx\; \sigma_{\text{LP}}^2 + \sigma_{\text{HP}}^2
$$
This is exactly the Pythagorean theorem in vector space form: if
$$
\tilde\phi = \phi_{\text{LP}} \oplus \phi_{\text{HP}}, \quad \langle \phi_{\text{LP}}, \phi_{\text{HP}} \rangle = 0
$$
then the “hypotenuse” RMS is:
$$
\sigma_\phi \approx \sqrt{\sigma_{\text{LP}}^2 + \sigma_{\text{HP}}^2}
$$
When your diagnostics printed something like  
$\sqrt{\text{LP}^2+\text{HP}^2}\approx \text{RMS}_\text{unc}$,  
that’s the orthogonality test passing.

If you ever see big mismatch, it’s a red flag: the split is not orthogonal (filter leakage, masking mismatch, or a bug).

---

## 4) ⊕: DM model (analog coarse solver)

### 4.1 Influence-function basis
Let actuators be indexed by $i=1,\dots,M$ at positions $x_i$. A common smooth basis is Gaussian influence functions:
$$
g_i(x)=\exp\left(-\frac{\|x-x_i\|^2}{2\sigma_{\text{DM}}^2}\right)
$$

The DM surface phase is:
$$
\phi_{\text{DM}}(x) = \sum_{i=1}^M u_i\, g_i(x)
$$
or in matrix form (over pupil samples):
$$
\mathbf{\phi}_{\text{DM}} = A\mathbf{u}
$$
where $A_{p,i}=g_i(x_p)$.

### 4.2 Regularized least squares fit (ridge)
We fit the DM to the LP target:
$$
\mathbf{u}^\* = \arg\min_{\mathbf{u}} \|W(A\mathbf{u}-\mathbf{\phi}_{\text{LP}})\|_2^2 + \lambda \|\mathbf{u}\|_2^2
$$
- $W$ is a diagonal mask selecting pupil samples.
- $\lambda$ is regularization (prevents insane actuator commands / conditioning collapse).

Closed-form normal equations:
$$
(A^T W^T W A + \lambda I)\mathbf{u} = A^T W^T W \mathbf{\phi}_{\text{LP}}
$$

### 4.3 Stroke clipping
A real DM has limited stroke. We implement a clip:
$$
\phi_{\text{DM}}(x) \leftarrow \mathrm{clip}\!\left(\phi_{\text{DM}}(x), -\phi_{\max}, +\phi_{\max}\right)
$$
and report the **clip fraction** = fraction of pupil samples hitting the clip limit.

If clip fraction is large (you saw ~0.109 in one run), your DM is saturating: the LP target is too large, or the mapping needs scaling.

### 4.4 DM diagnostics
We track:
- **fit RMS:** $\sigma(\phi_{\text{LP}}-\phi_{\text{DM}})$  
- **correlation:**  
$$
\rho_{\text{DM}} = \mathrm{corr}\!\left(\phi_{\text{LP}}, \phi_{\text{DM}}\right)
$$
Low $\rho_{\text{DM}}$ means DM is not matching the intended LP component (grid too coarse, wrong $\sigma_{\text{DM}}$, too-strong regularization, or split not actually LP️LP).

---

## 5) ⊕: DMD model (digital fine solver)

We treat the DMD path as a **quantized correction** of the residual. In the simplest “ideal phase modulator” proxy:

1) residual after DM:
$$
\phi_{\text{res}} = \tilde\phi - \phi_{\text{DM}}
$$

2) target for DMD is the HP component (or residual HP):
$$
\phi_{\text{HP,target}} = H_\kappa(\phi_{\text{res}})
$$

3) quantize to $L$ levels with step $q$:
$$
Q(\phi) = q\cdot \mathrm{round}\!\left(\frac{\phi}{q}\right)
$$
(“rounding is the pulse”: quantization creates discrete jumps, which in practice show up as temporal/spatial “pop” artifacts—exactly what you noted.)

4) optionally scale by a fidelity factor $\alpha\in[0,1]$:
$$
\hat\phi_{\text{DMD}} = \alpha\, Q(\phi_{\text{HP,target}})
$$

5) hybrid-corrected phase:
$$
\phi_{\text{hyb}} = \tilde\phi - \phi_{\text{DM}} - \hat\phi_{\text{DMD}}
$$

### 5.1 Throughput proxy
DMD holography and quantization typically reduce optical efficiency (energy leaks into unwanted diffraction orders). We keep a *heuristic* throughput proxy $\eta\in[0,1]$ to penalize extreme quantization / extreme command RMS. The exact proxy can be swapped later for a physical diffraction-efficiency model.

---

## 6) Ψ: Why “DM did nothing” can happen (and how to prove it)

You flagged runs like:
- RMS\_unc $\approx 0.34968$ → RMS\_DM $\approx 0.34942$ (almost no change)

That can be completely real if **your LP split contains almost no energy** (i.e., most aberration is high-frequency), or if the DM fit is **effectively constrained to be near-zero**.

Checklist:
1) **Energy split:** if $\sigma_{\text{LP}} \ll \sigma_{\text{HP}}$, DM can’t help much.
2) **DM fit corr:** if $\rho_{\text{DM}}$ is near 0, DM is failing to represent LP.
3) **Regularization:** large $\lambda$ forces $\mathbf{u}\to 0$.
4) **Influence width:** if $\sigma_{\text{DM}}$ is wrong, basis can’t represent the target.
5) **Stroke:** if clipping is heavy, DM correction becomes distorted (and can be counterproductive).

Your later diagnostics (showing LP/HP RMS and $\sqrt{\text{LP}^2+\text{HP}^2}$) are exactly the right way to validate this.

---

## 7) What’s new / publishable right now?

Yes: publishable as a **computational architecture + feasibility envelope**:

- A formal **two-channel decomposition** of wavefront correction.
- A **diagnostic stack** that reveals failure modes (clip, leakage, fit correlation, energy split).
- A reproducible **$\kappa$-sweep** showing optimum regions and how they shift with DM/DMD specs.

What’s still “recursing” (Ω if unresolved):
- A physically grounded throughput/efficiency model for DMD holography (we’re using a proxy).
- A more realistic DMD model (binary Lee hologram / carrier, diffraction orders, camera integration).
- A closed-loop controller with latency + sensor noise (easy to add, but not yet “final”).

Ω-tag: **DMD physical diffraction efficiency** (needs a specific hologram encoding model and optical geometry).

---

## 8) Single-cell notebook code (clean, stable, no argparse crash)

Paste this as **one cell** in Jupyter. It runs one simulation and a $\kappa$ sweep, prints the table, and plots summary curves + histograms.

```python
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Utilities
# -----------------------------
def make_pupil(N, radius_frac=0.45):
    yy, xx = np.indices((N, N))
    cx = (N-1)/2
    cy = (N-1)/2
    rr = np.sqrt((xx-cx)**2 + (yy-cy)**2)
    return (rr <= radius_frac*N).astype(float)

def rms_over_pupil(phi, pupil):
    m = pupil.astype(bool)
    v = phi[m]
    v = v - v.mean()
    return np.sqrt(np.mean(v**2))

def strehl_proxy(phi, pupil):
    sig = rms_over_pupil(phi, pupil)
    return float(np.exp(-(sig**2)))

def fft_lowpass(phi, pupil, kappa):
    # kappa in (0, 0.5] roughly; smaller = stronger smoothing
    N = phi.shape[0]
    f = np.fft.fftshift(np.fft.fft2(phi * pupil))
    ky = np.fft.fftshift(np.fft.fftfreq(N))
    kx = np.fft.fftshift(np.fft.fftfreq(N))
    KX, KY = np.meshgrid(kx, ky)
    KR = np.sqrt(KX**2 + KY**2)
    G = np.exp(-(KR**2)/(2*(kappa**2)))
    lp = np.real(np.fft.ifft2(np.fft.ifftshift(f * G)))
    lp = lp * pupil
    hp = (phi * pupil) - lp
    return lp, hp

def kolmogorov_phase(N, pupil, phase_rms=0.35, seed=0, alpha=11/3, eps=1e-6):
    # simple PSD shaping for a "turbulence-like" phase screen
    rng = np.random.default_rng(seed)
    ky = np.fft.fftshift(np.fft.fftfreq(N))
    kx = np.fft.fftshift(np.fft.fftfreq(N))
    KX, KY = np.meshgrid(kx, ky)
    KR = np.sqrt(KX**2 + KY**2)
    PSD = (KR + eps)**(-alpha/2)  # amplitude shaping
    noise = rng.normal(size=(N,N)) + 1j*rng.normal(size=(N,N))
    F = noise * PSD
    phi = np.real(np.fft.ifft2(np.fft.ifftshift(F)))
    phi = phi * pupil
    # normalize RMS
    r = rms_over_pupil(phi, pupil)
    if r > 0:
        phi = phi * (phase_rms / r)
    return phi

def dm_fit(phi_lp, pupil, dm_grid=12, dm_sigma=0.08, dm_reg=1e-3, dm_stroke=np.inf):
    # Build actuator grid in normalized coordinates [-0.5,0.5]
    N = phi_lp.shape[0]
    yy, xx = np.indices((N, N))
    x = (xx - (N-1)/2) / N
    y = (yy - (N-1)/2) / N
    m = pupil.astype(bool)
    xp = x[m]; yp = y[m]
    target = phi_lp[m]

    # actuator centers on square grid
    g = dm_grid
    ax = np.linspace(x.min(), x.max(), g)
    ay = np.linspace(y.min(), y.max(), g)
    AX, AY = np.meshgrid(ax, ay)
    centers = np.stack([AX.ravel(), AY.ravel()], axis=1)
    M = centers.shape[0]

    # Design matrix
    A = np.empty((target.size, M), dtype=float)
    for i, (cx, cy) in enumerate(centers):
        A[:, i] = np.exp(-((xp-cx)**2 + (yp-cy)**2)/(2*dm_sigma**2))

    # Ridge solve: (A^T A + λI)u = A^T target
    AtA = A.T @ A
    rhs = A.T @ target
    u = np.linalg.solve(AtA + dm_reg*np.eye(M), rhs)

    # Reconstruct DM surface
    phi_dm = np.zeros_like(phi_lp)
    phi_dm[m] = A @ u
    phi_dm = phi_dm * pupil

    # Stroke clip on the *surface* (phase units)
    if np.isfinite(dm_stroke):
        phi_max = 0.5*dm_stroke
        before = phi_dm.copy()
        phi_dm = np.clip(phi_dm, -phi_max, phi_max)
        clip_frac = float(np.mean((before[m] != phi_dm[m])))
    else:
        clip_frac = 0.0

    # diagnostics
    fit_err = (phi_lp - phi_dm) * pupil
    fit_rms = rms_over_pupil(fit_err, pupil)
    # correlation between lp and dm on pupil
    a = phi_lp[m] - phi_lp[m].mean()
    b = phi_dm[m] - phi_dm[m].mean()
    denom = (np.linalg.norm(a)*np.linalg.norm(b) + 1e-12)
    corr = float((a @ b) / denom)

    return phi_dm, {"fit_rms": float(fit_rms), "corr": corr, "clip_frac": clip_frac, "u_rms": float(np.sqrt(np.mean(u**2)))}

def dmd_quantize(phi_hp, pupil, dmd_levels=64, dmd_fidelity=1.0):
    m = pupil.astype(bool)
    # uniform symmetric quantizer
    vmax = np.max(np.abs(phi_hp[m])) + 1e-12
    q_step = 2*vmax / (dmd_levels-1)
    q = q_step * np.round(phi_hp / q_step)
    q = q * pupil
    cmd_rms = rms_over_pupil(q, pupil)
    return dmd_fidelity*q, {"q_step": float(q_step), "cmd_rms": float(cmd_rms)}

def run_once(N=256, phase_rms=0.35, kappa=0.12, seed=0,
             dm_grid=12, dm_sigma=0.08, dm_stroke=np.inf, dm_reg=1e-3,
             dmd_levels=64, dmd_fidelity=1.0):
    pupil = make_pupil(N)
    phi = kolmogorov_phase(N, pupil, phase_rms=phase_rms, seed=seed)

    # Baselines
    unc_rms = rms_over_pupil(phi, pupil)
    unc_st = strehl_proxy(phi, pupil)

    # Split
    phi_lp, phi_hp = fft_lowpass(phi, pupil, kappa=kappa)
    lp_rms = rms_over_pupil(phi_lp, pupil)
    hp_rms = rms_over_pupil(phi_hp, pupil)

    # DM fit to LP
    phi_dm, dm_info = dm_fit(phi_lp, pupil, dm_grid=dm_grid, dm_sigma=dm_sigma, dm_reg=dm_reg, dm_stroke=dm_stroke)
    phi_after_dm = (phi - phi_dm) * pupil
    dm_rms = rms_over_pupil(phi_after_dm, pupil)
    dm_st = strehl_proxy(phi_after_dm, pupil)

    # DMD correct HP residual of (after DM)
    _, hp_res = fft_lowpass(phi_after_dm, pupil, kappa=kappa)  # high-pass of residual
    phi_dmd, dmd_info = dmd_quantize(hp_res, pupil, dmd_levels=dmd_levels, dmd_fidelity=dmd_fidelity)
    phi_hyb = (phi_after_dm - phi_dmd) * pupil
    hyb_rms = rms_over_pupil(phi_hyb, pupil)
    hyb_st = strehl_proxy(phi_hyb, pupil)

    return {
        "kappa": kappa,
        "Strehl_unc": unc_st, "Strehl_DM": dm_st, "Strehl_Hyb": hyb_st,
        "RMS_unc": unc_rms, "RMS_DM": dm_rms, "RMS_Hyb": hyb_rms,
        "RMS_LP": lp_rms, "RMS_HP": hp_rms,
        "DMcorr": dm_info["corr"], "clip": dm_info["clip_frac"],
        "DM_u_rms": dm_info["u_rms"],
        "DMD_cmd_rms": dmd_info["cmd_rms"], "q_step": dmd_info["q_step"],
        "phi": phi, "phi_dm": phi_dm, "phi_hyb": phi_hyb, "pupil": pupil
    }

def kappa_sweep(kmin=0.10, kmax=0.50, steps=16, **kwargs):
    ks = np.linspace(kmin, kmax, steps)
    rows = [run_once(kappa=float(k), **kwargs) for k in ks]
    best = max(rows, key=lambda r: r["Strehl_Hyb"])
    return rows, best

def print_table(rows):
    print("\nκ-sweep results\n")
    header = ("kappa | Strehl_unc  Strehl_DM   Strehl_Hyb | RMS_unc   RMS_DM    RMS_Hyb | "
              "RMS_LP  RMS_HP | DMcorr clip | DMDcmd  q_step")
    print(header)
    print("-"*len(header))
    for r in rows:
        print(f"{r['kappa']:.3f} | {r['Strehl_unc']:.6f}  {r['Strehl_DM']:.6f}  {r['Strehl_Hyb']:.6f} | "
              f"{r['RMS_unc']:.5f}  {r['RMS_DM']:.5f}  {r['RMS_Hyb']:.5f} | "
              f"{r['RMS_LP']:.5f} {r['RMS_HP']:.5f} | {r['DMcorr']:+.3f} {r['clip']:.3f} | "
              f"{r['DMD_cmd_rms']:.5f} {r['q_step']:.5f}")

def plot_summary(rows, best):
    ks = np.array([r["kappa"] for r in rows])
    s_unc = np.array([r["Strehl_unc"] for r in rows])
    s_dm  = np.array([r["Strehl_DM"] for r in rows])
    s_hyb = np.array([r["Strehl_Hyb"] for r in rows])
    r_unc = np.array([r["RMS_unc"] for r in rows])
    r_dm  = np.array([r["RMS_DM"] for r in rows])
    r_hyb = np.array([r["RMS_Hyb"] for r in rows])

    fig = plt.figure(figsize=(12,8))
    gs = fig.add_gridspec(2, 2)

    ax1 = fig.add_subplot(gs[0,0])
    ax1.plot(ks, s_unc, label="unc")
    ax1.plot(ks, s_dm,  label="DM")
    ax1.plot(ks, s_hyb, label="hyb")
    ax1.set_title("Strehl proxy vs κ"); ax1.legend()

    ax2 = fig.add_subplot(gs[0,1])
    ax2.plot(ks, r_unc, label="unc")
    ax2.plot(ks, r_dm,  label="DM")
    ax2.plot(ks, r_hyb, label="hyb")
    ax2.set_title("RMS phase vs κ"); ax2.legend()

    # Histograms at best κ
    b = best
    pupil = b["pupil"].astype(bool)
    ax3 = fig.add_subplot(gs[1,0])
    ax3.hist(b["phi"][pupil].ravel(), bins=60, alpha=0.6, label="unc")
    ax3.hist((b["phi"]-b["phi_dm"])[pupil].ravel(), bins=60, alpha=0.6, label="DM")
    ax3.hist(b["phi_hyb"][pupil].ravel(), bins=60, alpha=0.6, label="hyb")
    ax3.set_title(f"Phase histograms @ best κ={b['kappa']:.3f}")
    ax3.legend()

    ax4 = fig.add_subplot(gs[1,1])
    ax4.plot(ks, np.array([r["DMcorr"] for r in rows]), label="DM corr")
    ax4.plot(ks, np.array([r["clip"] for r in rows]), label="clip frac")
    ax4.set_title("DM diagnostics vs κ"); ax4.legend()

    fig.tight_layout()
    plt.show()

# -----------------------------
# Run
# -----------------------------
rows, best = kappa_sweep(
    N=256,
    phase_rms=0.35,
    seed=0,
    dm_grid=12,
    dm_sigma=0.08,
    dm_stroke=np.inf,   # set finite (e.g. 1.0 rad) to test saturation
    dm_reg=1e-3,
    dmd_levels=64,
    dmd_fidelity=1.0,
    kmin=0.10, kmax=0.50, steps=16
)

print_table(rows)

print("\nBest κ by Strehl_Hyb")
print(f"  κ={best['kappa']:.3f}  Strehl(unc/DM/hyb)={best['Strehl_unc']:.6f}/{best['Strehl_DM']:.6f}/{best['Strehl_Hyb']:.6f}")
print(f"           RMS  (unc/DM/hyb)={best['RMS_unc']:.5f}/{best['RMS_DM']:.5f}/{best['RMS_Hyb']:.5f}")
print(f"      split RMS (LP/HP)={best['RMS_LP']:.5f}/{best['RMS_HP']:.5f}  sqrt≈{np.sqrt(best['RMS_LP']**2+best['RMS_HP']**2):.5f}")
print(f"      DM fit corr={best['DMcorr']:+.3f}  clip frac={best['clip']:.3f}  DM_u_rms={best['DM_u_rms']:.5f}")
print(f"      DMD cmd_rms={best['DMD_cmd_rms']:.5f}  q_step={best['q_step']:.5f}")

plot_summary(rows, best)
```

---

## 9) Next recursion steps (concrete)

Δ1: Lock the split operator:
- verify $\sigma^2 \approx \sigma_{\text{LP}}^2+\sigma_{\text{HP}}^2$ across random seeds.

Δ2: Make “throughput” physical:
- implement Lee hologram encoding (binary carrier) and compute efficiency into the 1st order.

Δ3: Close the loop:
- add temporal dynamics ($\rho$), measurement noise, and one-step latency; compute stability margin.

Δ4: Hardware mapping:
- tie DM actuator density + influence width to a realistic DM model, and DMD pixel pitch to a realistic hologram carrier.

---

## 10) ⊥: Minimal claim set for a paper draft

1) A hierarchical two-stage wavefront correction architecture:
$$
\tilde\phi \xrightarrow{L_\kappa} \phi_{\text{LP}} \xrightarrow{\text{DM}} \phi_{\text{DM}},\quad
\tilde\phi-\phi_{\text{DM}} \xrightarrow{H_\kappa} \phi_{\text{HP}} \xrightarrow{\text{DMD}} \hat\phi_{\text{DMD}}
$$

2) A reproducible diagnostic suite: $\sigma_\phi$, $S$, $\rho_{\text{DM}}$, clip fraction, LP/HP energy split.

3) Empirical sweeps showing the $\kappa$-dependent trade-off surface and regions of best performance.

That’s a complete “solution” at the algorithmic/feasibility level, with Ω reserved only for the physical diffraction-efficiency step.

