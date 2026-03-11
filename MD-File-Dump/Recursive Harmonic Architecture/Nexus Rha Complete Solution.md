
# The Π‑Ray Inverse and the Nexus Harmonic Closure  
**(Complete Markdown, with inline $…$ and block $$…$$ math)**

**Author:** Dean A. Kulik (Δ‑phase synthesis, Ψ‑field consolidation)  
**Date:** November 2025

---

## 0. Orientation (Δ → Ψ)

We model the flat (degenerate) triangle family with side relation
$$
A = B + C,\qquad A,B,C>0
$$
as a Π‑ray (all three vertices collinear). Heights and area vanish, yet the **medians** retain non‑zero structure and carry a harmonic signature. We define the **harmonic signature**
$$
H := \frac{m_c}{p},
$$
where $p$ is the perimeter and $m_c$ is the median to side $c$. For the Π‑ray family this yields a linear, exactly invertible mapping between $(A,H)$ and $(B,C)$.

> **Key result (invertible core):**
> $$
> B \;=\; A(4H-1),\qquad C \;=\; A(2-4H), \qquad \tfrac14 < H < \tfrac12.
> $$

This document collects all definitions, proofs, closure relations, and safe model extensions needed for a **complete solution** of the Π‑ray inverse, plus a right‑triangle resonance appendix and trustworthy quality metrics. (Notes on cryptography appear only as **non‑security toy constructions**; no cryptographic inversion is attempted.)

---

## 1. Geometry Backbone (Π‑ray family)

### 1.1 Canonical embedding and basic quantities
Place vertices on the $x$‑axis:
$$
V_A=(0,0),\quad V_B=(B,0),\quad V_C=(-C,0).
$$
Side naming ($a$ opposite $A$, etc.) gives lengths
$$
a=A=B+C,\qquad b=C,\qquad c=B,
$$
and perimeter / semiperimeter
$$
p = A + B + C = 2A,\qquad s=\frac{p}{2}=A.
$$

Area and heights collapse:
$$
\Delta = 0,\qquad h_a=h_b=h_c=0.
$$

### 1.2 Median lengths (exact, via standard median formula)
For any triangle,
$$
m_a = \tfrac12\sqrt{2b^2+2c^2-a^2},\quad
m_b = \tfrac12\sqrt{2a^2+2c^2-b^2},\quad
m_c = \tfrac12\sqrt{2a^2+2b^2-c^2}.
$$
Substitute $a=B+C$, $b=C$, $c=B$:
$$
\begin{aligned}
m_a &= \tfrac12\sqrt{2C^2+2B^2-(B+C)^2}
     = \tfrac12|B-C|, \\[4pt]
m_b &= \tfrac12\sqrt{2(B+C)^2+2B^2-C^2}
     = \tfrac12(B+2C), \\[4pt]
m_c &= \tfrac12\sqrt{2(B+C)^2+2C^2-B^2}
     = \tfrac12(2B+C).
\end{aligned}
$$

### 1.3 Normalized median ratios (harmonic observables)
With $p=2A$:
$$
\frac{m_a}{p}=\frac{|B-C|}{4A},\qquad
\frac{m_b}{p}=\frac{B+2C}{4A},\qquad
\frac{m_c}{p}=\frac{2B+C}{4A}.
$$

We adopt the **harmonic signature**
$$
H := \frac{m_c}{p}=\frac{2B+C}{4A}.
$$

Useful linear relations:
$$
\frac{m_b+m_c}{p}=\frac{3}{4},\qquad
\frac{m_b}{p}=\frac{4H-1}{2},\qquad
\frac{m_a}{p}=\frac{|B-C|}{4A},\qquad
\frac{m_{\text{mean}}}{p}=\frac{m_a+m_b+m_c}{3p}
= \frac{1}{3}\!\left(\frac{|B-C|}{4A}+\frac{4H-1}{2}+H\right).
$$

Domain constraints (from $B,C>0$):
$$
\tfrac14 < H < \tfrac12,\qquad
\frac{B}{C} \;=\; \frac{4H-1}{\,2-4H\,}.
$$

---

## 2. Inverse Mapping (Ψ‑collapse)

Starting with
$$
H=\frac{m_c}{p}=\frac{\tfrac12(2B+C)}{2A}=\frac{A+B}{4A}=\frac14+\frac{B}{4A},
$$
solve for $B$:
$$
B = A(4H-1).
$$
Using $A=B+C$, solve $C$:
$$
C = A - B = A(2-4H).
$$

**Boxed inverse (complete):**
$$
\boxed{\,B=A(4H-1),\qquad C=A(2-4H),\qquad \tfrac14<H<\tfrac12\,}
$$

When integer $B,C$ are desired, pick
$$
H = \frac14 + \frac{k}{4A}\quad\text{with }k\in\{1,2,\dots,A-1\},
$$
so that
$$
B=k,\qquad C=A-k.
$$

**Echo relations (medians):**
$$
m_b-m_c=\tfrac12(B+2C)-( \tfrac12(2B+C))=\tfrac12(C-B)=-\,m_a,
$$
$$
m_b+m_c=\tfrac12(3A)\quad\Rightarrow\quad \frac{m_b+m_c}{p}=\frac{3}{4}.
$$

---

## 3. Nexus Trust Algebra (Δ,⊕,↻,⊥,Ψ)

- **Δ (trigger):** choose $(A,H)$ with $\tfrac14<H<\tfrac12$.
- **⊕ (projection):** construct $(B,C)=\big(A(4H-1),\,A(2-4H)\big)$.
- **↻ (feedback):** recompute observables $(m_a/p,\,m_b/p,\,m_c/p)$ and verify closures.
- **⊥ (invalid fold):** if $H\not\in(\tfrac14,\tfrac12)$ or $B,C\le0$, isolate and retune.
- **Ψ (collapse):** ratios satisfy the identities; inverse is stable.

A compact *trust* indicator for any observed scalar $x$ (e.g. a measured median ratio) against target $H$:
$$
Q(H;x)=1-|x-H|\in[0,1],\qquad
\mathrm{align}_H(x)=\max\!\left(0,\,1-\frac{|x-H|}{1-H}\right).
$$
Aggregate multiple checks $\{x_i\}$ by
$$
Q_{\text{mean}}=\frac1n\sum_i Q(H;x_i),\qquad Q_{\min}=\min_i Q(H;x_i).
$$

> **Note:** These $Q$’s are **model quality metrics**, not cryptographic invariants.

---

## 4. Coordinate Formulas (useful for tables/plots)

With $(0,0)$, $(B,0)$, $(-C,0)$:
$$
\text{Centroid } G=\frac{V_A+V_B+V_C}{3}=\left(\frac{B-C}{3},\,0\right).
$$
As expected for collinearity, medians are collinear segments whose lengths equal those in §1.2; all heights vanish, and
$$
r=0,\qquad R=\frac{abc}{4\Delta}\to\infty\quad(\Delta=0).
$$

---

## 5. Π‑Ray Census Identities (quick checks)

Given any row $(A,B,C)$ with $A=B+C$:

- Perimeter: $p=2A$.
- Medians: $m_a=\tfrac{|B-C|}{2}$, $m_b=\tfrac{B+2C}{2}$, $m_c=\tfrac{2B+C}{2}$.
- Normalizations:
$$
\frac{m_b}{p}=\frac{4H-1}{2},\qquad \frac{m_c}{p}=H,\qquad
\frac{m_b+m_c}{p}=\frac{3}{4}.
$$
- Inverse from $(A,H)$:
$$
B=A(4H-1),\qquad C=A(2-4H).
$$

These identities reproduce and validate the sample rows like $(A,B,C)=(4,2,2)$, $(5,2,3)$, $(7,3,4)$, etc., and explain the constant $0.35\approx\pi/9$ fingerprints when $H$ is chosen near $\pi/9$.

---

## 6. Right‑Triangle Resonance (Mark1, small‑angle lens)

For a right triangle with legs $(a,b)$ and angle
$$
\theta=\arctan\!\Big(\frac{a}{b}\Big),
$$
a **resonant family** is $(a{:}b)=(3{:}8)$ and its scalings:
$$
\theta\approx 0.358771\ \text{rad}\approx 20.556^\circ,\qquad
\left|\theta-\frac{\pi}{9}\right|\approx 9.705\times10^{-3}.
$$

Error control (mean value bound for arctan):
$$
|\arctan x-\arctan y|\le \frac{|x-y|}{1+\min\{x^2,y^2\}}.
$$
This provides a clean way to sieve rational slopes close to a target harmonic angle (e.g. $\pi/9$).

---

## 7. A Safe, Reversible **Toy Harmonic Digest** (non‑cryptographic)

To demonstrate true **decompression** without touching real cryptography, define:

**Forward (encode)**  
Pick integers $A>1$ and $k\in\{1,\dots,A-1\}$:
$$
B:=k,\quad C:=A-k,\quad H:=\frac14+\frac{B}{4A},\quad D:=\mathrm{Enc}(A,H).
$$

**Backward (decode)**  
Given $(A,H)$, reconstruct
$$
(B,C)=\big(A(4H-1),\,A(2-4H)\big).
$$
If you quantize $H$ to rationals of the form $\tfrac14+\tfrac{k}{4A}$, then $(B,C)$ are integers **exactly**.

> This toy digest is purely pedagogical: it exhibits genuine, lossless inverse mapping of the Π‑ray family. It is **not** a cryptosystem and carries **no** security claims.

---

## 8. Why This **Does Not** Invert SHA‑256 (⊥ gate)

- Standard SHA‑256 outputs a 256‑bit digest with **no embedded $(A,H)$ pair** corresponding to Π‑ray medians.  
- Any statistic like “fraction of ones” concentrates near $0.5$ for pseudorandom outputs, not near a geometric $H$.
- Preimage resistance assumptions deny an efficient inverse for arbitrary digests; the Π‑ray inverse is a **geometric result**, not a cryptanalytic tool.

Thus, use the Π‑ray inverse to power **geometry‑based compressors, validators, and toy digests**, not to attack cryptography.

---

## 9. Extended Identities & Short Proofs

**(i) Linearization of $H$**  
$$
H=\frac{m_c}{p}=\frac{2B+C}{4A}
=\frac{B}{4A}+\frac{C}{4A}+\frac{B}{4A}
=\frac14+\frac{B}{4A}.
$$

**(ii) Ratio recovery**
$$
\frac{B}{C}=\frac{A(4H-1)}{A(2-4H)}=\frac{4H-1}{2-4H},\quad
H\in\Big(\frac14,\frac12\Big).
$$

**(iii) Sum/difference of medians**
$$
m_b\pm m_c=\frac{B+2C}{2}\ \pm\ \frac{2B+C}{2}
=\frac{3A}{2}\ \ \text{and}\ \ \frac{C-B}{2}.
$$

**(iv) Mean normalized median**
$$
\frac{m_{\text{mean}}}{p}=\frac{1}{3}\Big(\frac{|B-C|}{4A}+\frac{4H-1}{2}+H\Big).
$$

---

## 10. Practical Checklist (Ψ‑aligned workflow)

1. **Choose** $A$ and target $H\in(\tfrac14,\tfrac12)$ (e.g. $H\approx \pi/9$).  
2. **Reconstruct** $B=A(4H-1)$, $C=A(2-4H)$; if integer outputs are desired, let $H=\tfrac14+\tfrac{k}{4A}$.  
3. **Verify** closures: $p=2A$, $m_b/p=(4H-1)/2$, $m_c/p=H$, $(m_b+m_c)/p=3/4$.  
4. **Score** with $Q(H;x)$ on any observable $x$ to monitor model fit.

---

## Appendix A: Notation Map (Nexus symbols)

- **Δ** – input perturbation / choice of $(A,H)$  
- **⊕** – forward projection $(A,H)\mapsto(B,C)$  
- **↻** – feedback/validation using median and perimeter identities  
- **⊥** – invalid fold (domain violation)  
- **Ψ** – stable collapse (all identities satisfied)

---

## Appendix B: Table of Core Formulas

- $p=2A$, $s=A$, $\Delta=0$, $h_a=h_b=h_c=0$, $r=0$, $R\to\infty$.
- $m_a=\tfrac{|B-C|}{2}$, $m_b=\tfrac{B+2C}{2}$, $m_c=\tfrac{2B+C}{2}$.
- $H=\dfrac{m_c}{p}=\dfrac14+\dfrac{B}{4A}$.
- Inverse: $B=A(4H-1)$, $C=A(2-4H)$, with $\tfrac14<H<\tfrac12$.
- Ratios: $\dfrac{B}{C}=\dfrac{4H-1}{2-4H}$; $\dfrac{m_b+m_c}{p}=\dfrac34$; $\dfrac{m_b}{p}=\dfrac{4H-1}{2}$; $\dfrac{m_c}{p}=H$.

---

## Appendix C: Mark1 Angle Sieve (right‑triangle)

Given target angle $H_\theta$ (e.g. $\pi/9$), sieve coprime integer pairs $(a,b)$ so that
$$
\big|\arctan(a/b)-H_\theta\big|<\varepsilon,
$$
using the bound
$$
|\arctan x-\arctan y|\le \frac{|x-y|}{1+\min\{x^2,y^2\}}.
$$
The family $(a{:}b)=(3{:}8)$ and its scalings is a concrete near‑hit at $\varepsilon\approx 9.7\times10^{-3}$.

---

**End of document.**
