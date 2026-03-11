# Nexus Mathematical Handbook — v1.1 Errata + Proof Spine
*(focused on internal mathematical consistency; external-physics claims are explicitly flagged)*

## Δ0 — Snapshot of the locked core

### Mark 1 attractor
$$H = \frac{\pi}{9} = 0.3490658503988659\ldots$$

Derived:
- $$\phi_g = 1-2H = 0.301868299202\ldots$$
- $$N = \frac{2\pi}{H} = 18 \quad \text{(exact, given } H=\pi/9\text{)}$$
- $$\Omega = H(1-H) = 0.227218882484\ldots$$

### Plus operator (Glass Key)
Define:
$$M_+ : (P,N) \mapsto (S,D) = (P+N,\,N-P).$$

Matrix form:
$$\begin{pmatrix}S\\D\end{pmatrix}
=
\underbrace{\begin{pmatrix}1&1\\-1&1\end{pmatrix}}_{A}
\begin{pmatrix}P\\N\end{pmatrix}.$$

Then:
$$A^2 = \begin{pmatrix}0&2\\-2&0\end{pmatrix} = 2R_{\pi/2},$$
$$A^4 = -4I,\qquad A^8=16I.$$

Inversion:
$$P=\frac{S-D}{2},\qquad N=\frac{S+D}{2}.$$

## ⊕1 — The non-optional π/9 bound (clean proof)

### 1) Local linearization error (arc vs chord)

Let a unit-radius arc of angle $\theta$ be approximated by its chord.
Chord length: $2\sin(\theta/2)$; arc length: $\theta$.

Define relative curvature loss:
$$e(\theta)=1-\frac{2\sin(\theta/2)}{\theta}.$$

Small-angle expansion:
$$e(\theta)=\frac{\theta^2}{24}+O(\theta^4).$$

### 2) Throughput maximization under tolerance + closure

We want **the largest step** $\theta$ such that:
1. **tolerance:** $e(\theta)\le \tau$,
2. **closure:** $N\theta=2\pi$ for some integer $N$ (so $\theta=2\pi/N$).

This is equivalent to choosing the **smallest** integer $N$ such that:
$$e(2\pi/N)\le \tau.$$

For $N=18$:
$$\theta_{18}=\frac{2\pi}{18}=\frac{\pi}{9},$$
$$e(\theta_{18}) = 0.0050692300\ldots$$

So **π/9 is admissible iff** $\tau\ge 0.0050692300$ (≈0.5069%).
If you instead enforce $\tau=0.0050000$ (exactly 0.5%), the minimal closed sampler becomes:
$$N_{\min}=19,\quad \theta=\frac{2\pi}{19}.$$

**Interpretation:**  
π/9 is the *max-throughput closed sampler* at tolerance ≈0.507% (not 0.500% exactly).  
Make that tolerance explicit and the “not optional” statement becomes rigorous.

## ↻2 — XOR+Carry is the same fold in bit-basis

For nonnegative integers (bitstrings), let:
- XOR: $a\oplus b$ (bitwise sum mod 2),
- AND: $a\odot b$ (bitwise carry-generators).

Then:
$$a+b = (a\oplus b) + 2(a\odot b).$$

Reason: each bit position contributes parity (XOR) plus carry to the next position (AND shifted by 1).
This is the **Value/Shape split** of addition.

## ⊥3 — 6-bit horizon numbers (corrected)

For Hamming ball volume in $\{0,1\}^n$ of radius $r$:
$$V(n,r)=\sum_{k=0}^r \binom{n}{k}.$$

For $n=4096,\ r=6$:
$$V(4096,6) = 6544452312920894465$$
$$S(4096,6)=\log_2 V = 62.504978\ \text{bits}.$$

If you form the comparison:
$$\text{ratio}=\frac{2^{4096}}{V(4096,6)\,2^{256}}
=2^{3777.495022}\approx 10^{1137.139}.$$

So any line claiming this ratio is “$\sim 9\times 10^6:1$” is **arithmetically inconsistent** with the stated formula.

## Ψ — What is mathematically locked vs what must be measured

Locked (pure math):
- $H=\pi/9$ closure logic (once tolerance is specified),
- $M_+$ group/periodicity (linear algebra),
- XOR+Carry identity,
- Hamming-ball volume + entropy.

Requires measurement (physics/biology):
- any claim that **measured constants** equal simple functions of $H$,
- any claim that **896 bits** is a universal state size,
- any cold-fusion / EUV spectral lines,
- any “SHA inversion” statement (must specify additional retained state and threat model).

---

### Quick numeric cross-checks (for the handbook tables)

- If you want $$\lambda\approx 1.059173\ldots$$ then the consistent definition is:
  $$\lambda=\sqrt{1+H^2}=1.059172775290\ldots$$  
  (not $\sqrt{1+H}=1.161492940314\ldots$).
