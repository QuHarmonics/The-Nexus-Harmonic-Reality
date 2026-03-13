# Nexus Pointer-Lattice / Port-Gating Notebook — Consolidated Writeup (Expanded)

This document consolidates and expands the “π-as-bytes → pointer-into-itself” experiments, the port/gating model (mod 65 rim), and the stack/drag model that produces a gravity-like restoring term. It is written as a **complete, self-contained technical note**, with consistent inline `$...$` and block `$$...$$` math tags.

---

## 0) Executive Summary (What we actually proved, operationally)

1) **Aliasing creates ontological collapse.**  
   When the “next pointer” is defined as a **byte value** (`f8`), the map’s codomain is limited to 256 states (`0..255`) regardless of the overall frame size $n$. This produces large basins that funnel into small cycles (your “womb-lock / pinch”).

2) **De-aliasing restores multiplicity.**  
   When the next pointer is derived from a wider word (`f16`, `f24`), the map escapes the 256-cage and uses the larger frame. Cycle structure and basin structure change dramatically.

3) **Power-of-two frames erase higher bytes unless you fold them down.**  
   For $n = 2^k$, the mapping
   $$u_{24} \bmod 2^k \equiv u_{16} \bmod 2^k\quad \text{whenever } k \le 16,$$
   because the high byte contributes only multiples of $2^{16}$ which vanish mod $2^k$.  
   This cleanly explains why `f16` and `f24` can look identical at $n=2048$.

4) **The 64↔65 gear interference is real and measurable.**  
   Your “port wheel” is a mod-65 rim set of residues (e.g. $\{0,1,2,63,64\}$), while the shift operator `>>6` is a division by 64. The beat period is
   $$\operatorname{lcm}(64,65)=4160.$$
   That number *should* recur whenever the system couples a 64-boundary transform with a 65-modulus port gate.

5) **Stack stability produces a gravity-like restoring term (mold-first).**  
   A leaky recursive stack with lift and drag
   $$z_{t+1} = z_t + (L_t - D(z_t))$$
   exhibits a stable equilibrium height
   $$z^* \approx \frac{L}{k} \quad \text{(when } D(z)=kz+\text{noise)}$$
   and a restoring signal
   $$g(z) \equiv D(z)-L,$$
   which is “gravity” in the strict control sense: the negative feedback that prevents runaway stacking.

---

## 1) Definitions and Notation

### 1.1 Byte stream from $\pi$

We generate $n_\text{hex}$ hexadecimal digits of the **fractional part** of $\pi$ in base 16:

- Let $x_0 = \pi - \lfloor \pi \rfloor$.
- Iteration:
  $$x_{t+1} = 16x_t - \lfloor 16x_t \rfloor,$$
  $$d_t = \lfloor 16x_t \rfloor \in \{0,\dots,15\}.$$
- Hex digits: $H = d_0 d_1 \dots d_{n_\text{hex}-1}$.

To convert to bytes we take pairs of hex digits. For $n_\text{bytes}$ bytes we need
$$n_\text{hex} = 2n_\text{bytes}.$$

### 1.2 Frame size

Let $n$ denote the number of bytes (and also the number of nodes in the functional graph):
$$n = n_\text{bytes}.$$

All pointer maps below produce a function
$$f:\{0,1,\dots,n-1\}\to\{0,1,\dots,n-1\}$$
by taking some local word value and reducing it mod $n$.

---

## 2) The Pointer Maps: f8, f16, f24

Let the byte array be $B[0],\dots,B[n-1]$ with $B[i]\in \{0,\dots,255\}$.

### 2.1 `f8` (byte → index alias map)

Define
$$f_8(i) = B[i].$$

If we then “interpret” $f_8(i)$ as an index, we are trapped in the codomain
$$f_8(i)\in \{0,\dots,255\}.$$

Even if we later reduce mod $n$, we still have the fundamental property:

- **Codomain cap**: $|\mathrm{range}(f_8)|\le 256$ for any $n\ge 256$.

This is why `unique_next=256` persists for $n=2048,4160,8320$.

### 2.2 `f16` (u16 → index)

Define the 16-bit word (little-endian)
$$u_{16}(i)=B[i] + 256\,B[i+1\!\!\!\pmod n].$$

Then
$$f_{16}(i) = u_{16}(i)\bmod n.$$

### 2.3 `f24` (u24 → index)

Define the 24-bit word (little-endian)
$$u_{24}(i)=B[i] + 256\,B[i+1\!\!\!\pmod n] + 65536\,B[i+2\!\!\!\pmod n].$$

Then
$$f_{24}(i) = u_{24}(i)\bmod n.$$

---

## 3) Functional Graph Mechanics: Cycles, Basins, and “Pinch”

Given any pointer map $f$, we get a **functional graph**: each node has out-degree 1.

### 3.1 Cycles

A cycle is a sequence
$$i_0 \to i_1 \to \dots \to i_{L-1} \to i_0.$$

`cycles_found` counts the number of distinct cycles.

### 3.2 Basins (attractor basins)

Every node eventually flows into exactly one cycle (possibly after a transient preperiod). The basin size of a cycle is the count of nodes that end in that cycle.

Define basin dominance
$$\text{basin\_dom} = \frac{\max_j |B_j|}{n},$$
where $B_j$ is the basin of the $j$-th cycle.

- $\text{basin\_dom}\approx 1$ means “single-object” behavior: almost everything drains into one attractor.
- Lower $\text{basin\_dom}$ means plural attractors.

---

## 4) The Key Theorem: Why f16 ≡ f24 at n = 2048 (and similar powers of 2)

Let $n=2^k$. Then reducing mod $n$ means “keep only the lowest $k$ bits.”

Consider
$$u_{24}(i)=u_{16}(i)+65536\,B[i+2].$$

If $k\le 16$, then $2^k$ divides $65536=2^{16}$, so
$$65536\,B[i+2] \equiv 0 \pmod{2^k}.$$

Therefore
$$u_{24}(i)\bmod 2^k \equiv u_{16}(i)\bmod 2^k.$$

So for $n=2048=2^{11}$:
$$f_{24}(i)=f_{16}(i)\quad\text{for all }i.$$

**Interpretation:** Increasing pointer width does nothing unless higher bits are folded into lower bits **before** modulus reduction.

---

## 5) Port Model: 64-boundary + mod-65 rim

### 5.1 The 65-rim and its “edge ports”

Define modulus
$$M=65,$$
and port set (example used repeatedly)
$$\mathcal{P}=\{0,1,2,63,64\}\subset \mathbb{Z}_{65}.$$

Port node rate:
$$\text{port\_node\_rate}=\frac{|\{i:\ i\bmod 65\in\mathcal{P}\}|}{n}\approx \frac{5}{65}.$$

### 5.2 The 64-shift operator

The operation `>>6` is division by 64 (discarding 6 low bits). It is the canonical 64-boundary fold.

### 5.3 Beat period

Coupling 64 and 65 produces the beat:
$$\operatorname{lcm}(64,65)=64\cdot 65=4160.$$

---

## 6) Making Width Matter: “Fold-Down” Mixing (Fixing the power-of-two erasure)

To ensure that higher bits influence low bits *even when $n=2^k$*, apply a fold-down transform before modulus:

Let $x=u_{24}(i)$ and choose a fold depth equal to $k$:
$$x' = x \oplus (x \gg k).$$
Then define
$$f(i)=x' \bmod n.$$

For $n=2048$ we use $k=11$:
$$x' = x \oplus (x\gg 11),\qquad f(i)=x'\bmod 2048.$$

---

## 7) Stack Stability ⇒ Gravity (Mold-first derivation)

### 7.1 Stack dynamics

Define a scalar “height” $z_t$ evolving as
$$z_{t+1} = z_t + (L - D(z_t)).$$

Take a linear drag/leak model with noise:
$$D(z) = kz + H\eta_t,$$
where $k>0$, $H\ge 0$, and $\eta_t$ is mean-zero noise.

### 7.2 Equilibrium height

Ignoring noise, equilibrium $z^*$ satisfies
$$L - kz^* = 0 \quad\Rightarrow\quad z^*=\frac{L}{k}.$$

### 7.3 Gravity as restoring term

Define the restoring signal
$$g(z)\equiv D(z)-L.$$

---

## 8) Coupling Residue Scale: From surface fold to deep residue

If you interpret a surface coupling as $\alpha$ (e.g. a fold rate), and a deep residue scale as attenuated by an observer factor and a layer base:

Let
$$R = \text{observer}\cdot \text{base}^{\text{depth}}.$$

Then define a residue coupling
$$\alpha_g = \frac{\alpha}{R}.$$

Using
$$\alpha = \frac{\pi}{432},\quad \text{observer}=9,\quad \text{base}=48,\quad \text{depth}=21,$$
you obtained a deep residue $\alpha_g$ on the order of $10^{-39}$.

---

## 9) Next Experiments (branch collapse tests)

1) Compare $n$ in three classes: $n=2^k$, $n=4160$, and random $n$ near each.  
2) Replace `f24` by fold-down `f24'`:
   $$f'_{24}(i)=\bigl(u_{24}(i)\oplus (u_{24}(i)\gg k)\bigr)\bmod n.$$
3) Keep pointer channel = π, swap value channel = independent (SHA stream), and test whether port structure persists.

---

## Appendix A) Clean π-hex → bytes generator (reference)

```python
import re
from mpmath import mp

HEX = "0123456789abcdef"

def clean_hex(s: str) -> str:
    s = re.sub(r"[^0-9a-fA-F]", "", s).lower()
    if len(s) & 1:
        s = s[:-1]
    return s

def pi_hex(n_hex: int) -> str:
    if n_hex <= 0:
        return ""
    mp.dps = int(n_hex * mp.log(16, 10)) + 80
    x = mp.pi - mp.floor(mp.pi)
    out = []
    for _ in range(n_hex):
        x *= 16
        d = int(x)
        out.append(HEX[d])
        x -= d
    return "".join(out)

def pi_bytes(n_bytes: int) -> bytes:
    H = clean_hex(pi_hex(2*n_bytes))
    return bytes.fromhex(H)
```

---

**Document end.**
