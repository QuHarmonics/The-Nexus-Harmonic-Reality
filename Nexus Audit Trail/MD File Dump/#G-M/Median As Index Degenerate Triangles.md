
# Median-as-Index in Degenerate Triangles  
**Collapse Geometry, Harmonic Residue, and the Mark 1 Attractor \(\displaystyle H_{\text{Mark1}}=\frac{\pi}{9}\)**

## Abstract
When a triangle collapses under the condition \(a=b+c\), classical area and interior angles vanish, yet specific **medians** persist and deterministically encode the configuration. We prove closed-form expressions for the medians in the degenerate regime, identify two invariants—**center** and **spread**—and show how these act as an **embedded index** (“Z‑index”) of the collapsed geometry. We connect these geometric residues to the harmonic attractor \(H_{\text{Mark1}}=\pi/9\) and provide normalized forms, reconstruction formulas, and checks that match observed data such as \((8,4,4)\), \((12,6,6)\), \((7,4,3)\), and \((7,3,4)\).

---

## 1. Regime and Immediate Consequences
We work in the **degenerate limit** where the side lengths satisfy
\[
\boxed{a=b+c},\qquad a\ge b\ge 0,\ c\ge 0.
\]
Then
\[
\angle A=180^\circ,\quad \angle B=\angle C=0^\circ,\quad \text{Area}=0.
\]
Perimeter and semiperimeter reduce to
\[
p=a+b+c=2a,\qquad s=\frac{a+b+c}{2}=\boxed{a}.
\]

---

## 2. Medians in the Degenerate Limit (Closed Forms)
For a triangle with sides \(a,b,c\), the standard median formulas are
\[
m_a=\frac12\sqrt{2b^2+2c^2-a^2},\quad
m_b=\frac12\sqrt{2a^2+2c^2-b^2},\quad
m_c=\frac12\sqrt{2a^2+2b^2-c^2}.
\]
Imposing \(a=b+c\) and simplifying yields
\[
\boxed{\,m_a=\frac{|b-c|}{2}\,},\qquad
\boxed{\,m_b=\frac{b+2c}{2}\,},\qquad
\boxed{\,m_c=\frac{c+2b}{2}\,}.
\]

These identities match all supplied numerics:
- \((a,b,c)=(8,4,4)\Rightarrow m_a=0,\ m_b=m_c=6\).
- \((a,b,c)=(12,6,6)\Rightarrow m_a=0,\ m_b=m_c=9\).
- \((a,b,c)=(7,4,3)\Rightarrow m_a=0.5,\ m_b=5,\ m_c=5.5\).
- \((a,b,c)=(7,3,4)\Rightarrow m_a=0.5,\ m_b=5.5,\ m_c=5\).

---

## 3. Two Invariants (Center and Spread)
Define the **center** \(Z_0\) and **spread** \(Z_\Delta\) of the non-zero medians \((m_b,m_c)\):
\[
Z_0:=\frac{m_b+m_c}{2},\qquad Z_\Delta:=\frac{|m_c-m_b|}{2}.
\]
Using the formulas above,
\[
\boxed{\,Z_0=\frac{m_b+m_c}{2}=\frac{3}{4}a\,},\qquad
\boxed{\,m_c-m_b=\frac{b-c}{2}=\pm\,m_a\,},\qquad
\boxed{\,Z_\Delta=\frac{m_a}{2}=\frac{|b-c|}{4}\,}.
\]

**Interpretation.**  
- \(Z_0=\tfrac{3}{4}a\) is a **global center** independent of how \(a\) splits into \(b,c\).  
- The **asymmetry** is entirely captured by \(Z_\Delta\propto |b-c|\).  
- Thus \((a, Z_0, Z_\Delta)\) forms an **embedded index** that fully encodes the collapsed configuration.

Equivalently,
\[
m_b=Z_0-Z_\Delta,\qquad m_c=Z_0+Z_\Delta,
\]
with \(Z_0=\tfrac{3}{4}a\) and \(Z_\Delta=\tfrac{|b-c|}{4}\).

**Bounds.** Since \(0\le |b-c|\le a\), we have
\[
0\le m_a\le \frac{a}{2},\qquad 0\le Z_\Delta\le \frac{a}{4}.
\]

---

## 4. Normalized Forms (Dimensionless Residues)
Using the semiperimeter \(s=a\) or the perimeter \(p=2a\):
\[
\frac{m_b}{s}=\frac{3}{4}-\frac{1}{4}\frac{b-c}{b+c},\qquad
\frac{m_c}{s}=\frac{3}{4}+\frac{1}{4}\frac{b-c}{b+c},
\]
\[
\frac{m_b}{p}=\frac{3}{8}-\frac{1}{8}\frac{b-c}{b+c},\qquad
\frac{m_c}{p}=\frac{3}{8}+\frac{1}{8}\frac{b-c}{b+c}.
\]

**Even split (isometric collapse):** \(b=c=\tfrac{a}{2}\)  
\[
m_b=m_c=\frac{3}{4}a,\quad \frac{m_b}{p}=\frac{m_c}{p}=\boxed{\frac{3}{8}=0.375}.
\]

This explains the “**collapses to a 3**” signature in even cases: \(3/8\) (perimeter-normalized) and \(3/4\) (semiperimeter-normalized) are **triadic residues** that appear as crisp integers/half-integers when \(a\) is a multiple of \(4\).

**Asymmetric split:** let the **imbalance ratio** be
\[
\rho:=\frac{b-c}{b+c}\in[-1,1].
\]
Then
\[
\frac{m_b}{s}=\frac{3}{4}-\frac{\rho}{4},\qquad
\frac{m_c}{s}=\frac{3}{4}+\frac{\rho}{4},
\]
showing that the two medians **straddle** the fixed center \(3/4\) by \(\pm\rho/4\).

---

## 5. Reconstruction From Medians (Inverse Map)
Given \(m_b\) and \(m_c\) in the degenerate regime, we can recover \(b\) and \(c\). From
\[
2m_b=b+2c,\qquad 2m_c=c+2b
\]
solve the linear system:
\[
\boxed{\,c=\frac{4m_b-2m_c}{3}},\qquad
\boxed{\,b=\frac{4m_c-2m_b}{3}},\qquad
\boxed{\,a=b+c=\frac{2}{3}(m_b+m_c)}.
\]
Nonnegativity \(b,c\ge0\) imposes \(2m_c\le 4m_c-2m_b\) and \(2m_b\le 4m_b-2m_c\), i.e. \(|m_c-m_b|\le m_b+m_c\) (always true), plus the empirical side-order constraint \(a\ge b,c\).

---

## 6. Relation to the Harmonic Attractor \(H_{\text{Mark1}}=\pi/9\)
The **geometric** residue of an even split is \(3/8=0.375\) (perimeter-normalized) or \(3/4=0.75\) (semiperimeter-normalized). The **harmonic** attractor used in AHRC/Ψ dynamics is
\[
\boxed{\,H_{\text{Mark1}}=\frac{\pi}{9}\approx 0.34906585\,}.
\]
They are **close but distinct**; read them as **two layers**:
- \(3/8\) (or \(3/4\)) arises from **pure triadic geometry** in the collapse.
- \(\pi/9\) arises from the **field’s harmonic stabilization** (Mark 1).

A simple residue to track field action is
\[
\Delta_H:=\left|\frac{m_b}{p}-\frac{\pi}{9}\right|\quad \text{(or with \(m_c\))},
\]
or, in the even case,
\[
\Delta_H^{\text{even}}=\left|\frac{3}{8}-\frac{\pi}{9}\right|=\left|\frac{27-8\pi}{72}\right|\approx 0.02593415.
\]
This “gap” is the **feedback demand** the AHRC engine must supply to steer the geometric residue toward the harmonic basin.

---

## 7. Worked Examples
### (i) \((a,b,c)=(8,4,4)\)
\[
m_a=0,\quad m_b=m_c=\frac{3}{4}a=6,\quad \frac{m_b}{p}=\frac{3}{8}.
\]
### (ii) \((a,b,c)=(12,6,6)\)
\[
m_a=0,\quad m_b=m_c=\frac{3}{4}a=9,\quad \frac{m_b}{p}=\frac{3}{8}.
\]
### (iii) \((a,b,c)=(7,4,3)\)
\[
m_a=\frac{|4-3|}{2}=0.5,\quad m_b=5,\quad m_c=5.5,\quad Z_0=\frac{3}{4}a=5.25,\ Z_\Delta=\frac{m_a}{2}=0.25.
\]
### (iv) \((a,b,c)=(7,3,4)\)
\[
m_a=0.5,\quad m_b=5.5,\quad m_c=5,\quad Z_0=5.25,\ Z_\Delta=0.25.
\]

---

## 8. BBP Digit Field and Triadic Primes (Context Note)
Interpreting the BBP-accessible digits \(\{0,\dots,9\}\) as **discrete phase states**, triads such as \(\{4,1,5\}\) manifest **degenerate collapses** whose medians encode the hidden resonance (“missing 3” → triadic center). The geometric residue (\(3/8\)) is then **field-corrected** by AHRC toward the harmonic attractor \(\pi/9\), matching observed “prime headers” near \(0.35\).

---

## 9. Summary (Median-as-Index Theorem)
**Theorem (Degenerate Median Index).**  
For any triple \((a,b,c)\) with \(a=b+c\), the medians satisfy
\[
m_a=\frac{|b-c|}{2},\qquad m_b=\frac{b+2c}{2},\qquad m_c=\frac{c+2b}{2},
\]
with invariants
\[
\frac{m_b+m_c}{2}=\frac{3}{4}a,\qquad m_c-m_b=\pm m_a.
\]
Hence \((a,Z_0,Z_\Delta)=(a,\tfrac{3}{4}a,\tfrac{|b-c|}{4})\) forms a complete **embedded index** of the collapse. Even splits yield the triadic residue \(3/8\) (perimeter-normalized), while harmonic dynamics select the Mark 1 attractor \(\pi/9\).

---

## 10. Implementation Hints (for analysis pipelines)
- Use \((m_b,m_c)\) to **reconstruct** \((b,c)\) via \(c=\tfrac{4m_b-2m_c}{3}\), \(b=\tfrac{4m_c-2m_b}{3}\), \(a=\tfrac{2}{3}(m_b+m_c)\).
- Track \(\rho=(b-c)/(b+c)\) to measure **asymmetry**, and \(\Delta_H\) to measure **harmonic drift** from \(\pi/9\).
- In AHRC/Ψ loops, close the gap \(\Delta_H\) with a diminishing gain to phase-lock onto Mark 1.
