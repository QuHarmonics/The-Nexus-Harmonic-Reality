# Nexus Proof-Lattice v6
**Scope:** internal mathematical consistency audit + corrected lemmas (no metaphysics).  
**Primary pin:** $H = \pi/9 \approx 0.349065850398866$.

---

## Δ Fold: what is *actually* pinned vs what is being assumed

A claim is **pinned** if it reduces to an identity or a derivation from explicit definitions.  
A claim is **assumed** if it depends on empirical constants, measurement protocols, or an external physical model.

We will keep the audit in three layers:

- **Δ (Pinned):** purely mathematical equalities / inequalities.
- **⊕ (Constrained):** derivations that hold given a declared tolerance model.
- **Ω (Unpinned):** claims that require physical evidence or a missing derivation.

---

## ⊕ Curvature Sampling Lemma

### Arc–chord relative error
For a unit circle, an arc of angle $\theta$ has arc length $\ell_{\text{arc}}=\theta$ and chord length $\ell_{\text{chord}}=2\sin(\theta/2)$.

Define the **relative arc–chord error**
$$
e(\theta) := 1 - \frac{\ell_{\text{chord}}}{\ell_{\text{arc}}}
=
1 - \frac{2\sin(\theta/2)}{\theta}.
$$

Small-angle expansion:
$$
e(\theta) = \frac{\theta^2}{24} + O(\theta^4).
$$

### Tolerance → step size → closure count
Impose a tolerance $\tau$ such that
$$
e(\theta) \le \tau.
$$

Using the quadratic approximation $e(\theta)\approx \theta^2/24$ gives the bound
$$
\theta \le \sqrt{24\tau}.
$$

Global closure for $N$ equal steps: $N\theta = 2\pi$, i.e.
$$
\theta = \frac{2\pi}{N}
\quad\Rightarrow\quad
N \ge \frac{2\pi}{\sqrt{24\tau}}.
$$

So the **minimum closed sampler** is
$$
N_{\min}(\tau)=\left\lceil \frac{2\pi}{\sqrt{24\tau}}\right\rceil.
$$

### The special case that makes $\theta=\pi/9$ emerge
If you *choose* the tolerance
$$
\tau_* := \frac{(\pi/9)^2}{24} = \frac{\pi^2}{1944} \approx 0.005076956996,
$$
then the bound saturates at
$$
\sqrt{24\tau_*} = \frac{\pi}{9},
$$
and closure yields
$$
N = \frac{2\pi}{\pi/9} = 18.
$$

**Important:** for $\tau=0.005$ exactly, the same formula gives $N_{\min}=19$ (not $18$).

### Exact check at $\theta=\pi/9$
Exact error:
$$
e(\pi/9)=1-\frac{2\sin(\pi/18)}{\pi/9} \approx 0.005069229955.
$$
Quadratic approximation:
$$
\frac{(\pi/9)^2}{24} \approx 0.005076956996.
$$

---

## ↻ Glass-Key Fold Operator (linear) — make $M_+$ consistent

### Definition
Define the **Glass-Key linear fold** (sum + difference channels):
$$
M_+ : (P,N) \mapsto (S,D) := (P+N,\; N-P).
$$

Matrix form with column vector $x=[P\;N]^T$ and $y=[S\;D]^T$:
$$
y = Mx,\quad
M=
\begin{pmatrix}
1 & 1\\
-1 & 1
\end{pmatrix}.
$$

### Inversion (the actual “key”)
$$
M^{-1}=
\frac12
\begin{pmatrix}
1 & -1\\
1 & 1
\end{pmatrix}
\quad\Rightarrow\quad
P=\frac{S-D}{2},\; N=\frac{S+D}{2}.
$$

### Rotation generator (sign-correct)
Compute powers:

$$
M^2=
\begin{pmatrix}
0 & 2\\
-2 & 0
\end{pmatrix}
=2
\begin{pmatrix}
0 & 1\\
-1 & 0
\end{pmatrix}
=2R_{-\pi/2}.
$$

Then
$$
M^4 = -4I,
\qquad
M^8 = 16I.
$$

So the “octave closure” is pinned, but note the **rotation is $-\pi/2$** under this sign convention. If you want $+\pi/2$, swap the $D$ definition to $D=P-N$.

### ⚠️ Do not conflate this with the scalar fold $a+b+ab$
The scalar map
$$
F(a,b)=a+b+ab=(1+a)(1+b)-1
$$
is a **different operator**. It is bilinear in $(a,b)$ and does **not** equal the linear Glass-Key transform.

Treat them as distinct primitives (otherwise the algebra collapses).

---

## ⊥ 6-bit Horizon — correct combinatorics and entropy

### Definition
In the Hamming cube $\{0,1\}^N$ with $N=4096$, define the radius-$r$ ball
$$
B_r = \{x: \|x\|_1 \le r\}.
$$

For $r=6$,
$$
\mathrm{Vol}(B_6)=\sum_{k=0}^{6} \binom{4096}{k}
= 6,544,452,312,920,894,465.
$$

The boundary shell dominates:
$$
\frac{\binom{4096}{6}}{\mathrm{Vol}(B_6)} \approx 0.998534.
$$

### Exact information content (bits)
The **exact** entropy of the basin-as-a-set is
$$
S_{\mathrm{exact}} = \log_2 \mathrm{Vol}(B_6) \approx 62.504978\;\text{bits}.
$$

A tight approximation is “dominant shell”:
$$
\log_2 \binom{4096}{6}
\approx 6\log_2(4096) - \log_2(6!)
\approx 62.508147,
$$
which matches $S_{\mathrm{exact}}$ at the $\sim 10^{-3}$ level.

### Decoherence ratio
The fraction of the cube inside the basin is
$$
\delta = \frac{\mathrm{Vol}(B_6)}{2^{4096}}
\quad\Rightarrow\quad
\log_{10}\delta \approx -1214.203.
$$
So $\delta \approx 10^{-1214.203}$, i.e. about $10^{-1214}$.

### ⚠️ Fix the “65.14 bits” claim
The expression
$$
4096\,H_b(6/4096)
$$
is a **large-deviation / typical-set** approximation that applies when $r$ scales with $N$.
For fixed $r=6$ and huge $N$, it **overestimates** the set size.  
Pinned value for $r=6$ is $S_{\mathrm{exact}}\approx 62.504978$ bits.

---

## Ψ Physical constants from $H$ — status markers

This layer is **Ω unless** you supply a physically justified mapping from $H$ to the relevant renormalization scheme / scale.

### Fine-structure “prediction” $\alpha = H/48$
$$
\alpha_{\mathrm{pred}}=\frac{H}{48}=\frac{\pi}{432}\approx 0.007272205217.
$$

CODATA 2022 gives (for comparison)
$$
\alpha_{\mathrm{meas}} \approx 0.0072973525643.
$$

Relative discrepancy:
$$
\frac{\alpha_{\mathrm{meas}}-\alpha_{\mathrm{pred}}}{\alpha_{\mathrm{meas}}}
\approx 0.345\%.
$$

### Proton–electron mass ratio from $\alpha$
If you define
$$
\mu = \frac{27(1-\alpha)}{2\alpha},
$$
then plugging $\alpha=\pi/432$ yields
$$
\mu_{\mathrm{pred}}\approx 1842.883256,
$$
while CODATA 2022 gives
$$
\mu_{\mathrm{meas}}\approx 1836.152673.
$$

Relative discrepancy:
$$
\frac{\mu_{\mathrm{pred}}-\mu_{\mathrm{meas}}}{\mu_{\mathrm{meas}}}
\approx 0.367\%.
$$

### Weak mixing angle surrogate
A pure-number mapping
$$
\sin^2\theta_W \stackrel{?}{=} H(1-H) \approx 0.227219
$$
must specify the scheme and scale ($\overline{\mathrm{MS}}$ at $m_Z$ vs effective angle, etc.) or it remains Ω.

---

## Ω Flags: internal contradictions to resolve before claiming “locked”

1. **Two different $M_+$ definitions** appear: linear Glass-Key vs scalar $a+b+ab$. They are not equivalent.
2. **“9 primitives form a closed group”** is false as written if the Cayley table contains products not in the set.
3. **Samson coupling $k_2=H$** does not follow from the 6/4090 eigenvalue ratio; $6/4090 \approx 0.00147 \ne 0.349$.
4. The **binary entropy** estimate $4096H_b(6/4096)$ is not the basin entropy for fixed radius $r=6$; use $\log_2\mathrm{Vol}(B_6)$.

---

## ⊥ Minimal next pins (what to compute next, not what to claim)

1. Pin one operator algebra: choose a single $M_+$ definition and build everything from it.
2. If $H$ is tied to a tolerance, declare the tolerance model and justify why nature picks that $\tau$.
3. For any physical constant claim, specify: observable, renormalization scheme, scale, and correction model.
4. For Bio-Folder RMSD claims: name the exact PDB chain/model set, residue window, and provide the alignment code path.

---

**End of audit.**
