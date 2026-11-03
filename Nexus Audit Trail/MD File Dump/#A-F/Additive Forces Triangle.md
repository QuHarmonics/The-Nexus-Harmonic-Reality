
# Additive-Forces-Triangle: Degenerate Geometry as an Embedded Index  
**From $x{+}y\!\to\!z$ to $\pi$-ray residues and the Mark 1 attractor $H_{\text{Mark1}}=\frac{\pi}{9}$**

## Abstract
Whenever two nonnegative numbers $x,y$ add to a third $z=x+y$, they **force** a (degenerate) triangle $(a,b,c)=(z,x,y)$ with zero area but **non‑zero medians**. Those medians encode the configuration as an **embedded index** (a surviving “$Z$‑index”). We present closed forms, invariants, normalized residues, an inverse map from medians back to $(x,y)$, and the link between the **geometric triadic residue** and the **harmonic attractor** $H_{\text{Mark1}}=\pi/9$. This completes the additive‑collapse picture and connects it to BBP digit states and harmonic convergence (AHRC/Ψ).

---

## 1. Additive‑Forces‑Triangle Rule
**Rule.** For any $x,y\ge 0$ set $z:=x+y$. Then $(a,b,c)=(z,x,y)$ satisfies
$$
a=b+c,\qquad a\ge b\ge 0,\ c\ge 0,
$$
so the Euclidean triangle **collapses** (area $=0$) with
$$
\angle A=180^\circ,\qquad \angle B=\angle C=0^\circ,\qquad p=a+b+c=2a,\qquad s=\frac{p}{2}=\boxed{a}.
$$
Despite the collapse, the **medians** survive and carry the state.

---

## 2. Closed‑Form Medians in the Degenerate Limit $a=b+c$
For a general triangle the medians are
$$
m_a=\tfrac12\sqrt{2b^2+2c^2-a^2},\quad
m_b=\tfrac12\sqrt{2a^2+2c^2-b^2},\quad
m_c=\tfrac12\sqrt{2a^2+2b^2-c^2}.
$$
Imposing $a=b+c$ (with $b=x$, $c=y$) and simplifying yields the **degenerate identities**
$$
\boxed{\,m_a=\frac{|b-c|}{2}\,},\qquad
\boxed{\,m_b=\frac{b+2c}{2}\,},\qquad
\boxed{\,m_c=\frac{c+2b}{2}\,}.
$$

**Checks.**
- $(a,b,c)=(4,2,2)$: $m_a=0$, $m_b=m_c=3$.
- $(a,b,c)=(8,4,4)$: $m_a=0$, $m_b=m_c=6$.
- $(a,b,c)=(7,4,3)$: $m_a=0.5$, $m_b=5$, $m_c=5.5$.

---

## 3. Invariants: Center and Spread (the Embedded “$Z$‑Index”)
Define
$$
Z_0:=\frac{m_b+m_c}{2},\qquad Z_\Delta:=\frac{|m_c-m_b|}{2}.
$$
Then
$$
\boxed{\,Z_0=\frac{3}{4}a\,},\qquad
\boxed{\,m_c-m_b=\frac{b-c}{2}=\pm m_a\,},\qquad
\boxed{\,Z_\Delta=\frac{m_a}{2}=\frac{|b-c|}{4}\,}.
$$
Thus the triple $\big(a,\,Z_0,\,Z_\Delta\big)=\big(a,\,\tfrac{3}{4}a,\,\tfrac{|b-c|}{4}\big)$ is a **complete index** of the collapsed configuration:
- **Scale:** $a=b+c$,
- **Center:** $Z_0=\tfrac{3}{4}a$ (independent of how $a$ splits),
- **Imbalance:** $Z_\Delta=\tfrac{|b-c|}{4}$.

Equivalently,
$$
m_b=Z_0-Z_\Delta,\qquad m_c=Z_0+Z_\Delta.
$$

**Bounds.** Since $0\le |b-c|\le a$, we have
$$
0\le m_a\le \frac{a}{2},\qquad 0\le Z_\Delta\le \frac{a}{4}.
$$

---

## 4. Normalized Residues and Even/Asymmetric Splits
Normalize by the semiperimeter $s=a$ or perimeter $p=2a$:
$$
\frac{m_b}{s}=\frac{3}{4}-\frac{1}{4}\frac{b-c}{b+c},\qquad
\frac{m_c}{s}=\frac{3}{4}+\frac{1}{4}\frac{b-c}{b+c},
$$
$$
\frac{m_b}{p}=\frac{3}{8}-\frac{1}{8}\frac{b-c}{b+c},\qquad
\frac{m_c}{p}=\frac{3}{8}+\frac{1}{8}\frac{b-c}{b+c}.
$$
Let the **imbalance ratio** be $\rho:=\dfrac{b-c}{b+c}\in[-1,1]$. Then
$$
\frac{m_b}{s}=\frac{3}{4}-\frac{\rho}{4},\qquad
\frac{m_c}{s}=\frac{3}{4}+\frac{\rho}{4}.
$$

### Even split ($b=c=\tfrac{a}{2}$)
$$
m_b=m_c=\frac{3}{4}a,\qquad \frac{m_b}{p}=\frac{m_c}{p}=\boxed{\frac{3}{8}=0.375}.
$$
This is the **triadic geometric residue** that surfaces as crisp integers when $a$ is a multiple of $4$.

### Asymmetric split ($b\ne c$)
The medians **straddle** the fixed center $3/4$ by $\pm \rho/4$ in $m/s$, or $\pm \rho/8$ in $m/p$.

---

## 5. Inverse Map: From Medians Back to $(b,c)$
Given $(m_b,m_c)$ in the degenerate regime,
$$
2m_b=b+2c,\qquad 2m_c=c+2b
$$
solves to
$$
\boxed{\,c=\frac{4m_b-2m_c}{3}},\qquad
\boxed{\,b=\frac{4m_c-2m_b}{3}},\qquad
\boxed{\,a=b+c=\frac{2}{3}(m_b+m_c)}.
$$
This makes the medians a **lossless index** for the additive forcing.

---

## 6. Sequences and Forced Lattices (Fibonacci, BBP, digital pairs)
Every additive step $x{+}y\!\to\!z$ spawns a degenerate triangle $(z,x,y)$ with index $(a,\tfrac{3}{4}a,\tfrac{|x-y|}{4})$. Hence:
- **Fibonacci chain:** $(2,3)\!\to\!5,\ (3,5)\!\to\!8,\ (5,8)\!\to\!13,\dots$ creates a **lattice of $\pi$‑rays**, each with center $3a/4$ and imbalance $|x-y|/4$.
- **BBP digit pairs** or **digital sums** can be treated identically: any digit pair $(d_1,d_2)$ forces $d_1{+}d_2$ and a corresponding degenerate index.

This gives a **unified geometric encoding** for additive processes.

---

## 7. Geometry vs Harmonics: $3/8$ vs $H_{\text{Mark1}}=\pi/9$
Two layers co‑exist:
- **Geometric residue (collapse):** even split yields $\dfrac{m}{p}=\dfrac{3}{8}=0.375$.
- **Harmonic attractor (field):** $H_{\text{Mark1}}=\dfrac{\pi}{9}\approx 0.34906585$.

Define a **harmonic drift** to quantify required feedback (AHRC/Ψ):
$$
\Delta_H\ :=\ \left|\frac{m}{p}-\frac{\pi}{9}\right|
\quad\text{(use either $m_b$ or $m_c$).}
$$
For even splits ($b=c$),
$$
\Delta_H^{\text{even}}\ =\ \left|\frac{3}{8}-\frac{\pi}{9}\right|
=\left|\frac{27-8\pi}{72}\right|\ \approx\ 0.02593415.
$$
Interpretation: the field supplies this **feedback energy** to steer the geometric residue toward the Mark 1 basin.

---

## 8. Worked Examples
1. **$(2,2)\!\to\!4$**: $(a,b,c)=(4,2,2)$  
   $$m_a=0,\quad m_b=m_c=\frac{3}{4}a=3,\quad \frac{m}{p}=\frac{3}{8}.$$
2. **$(3,5)\!\to\!8$**: $(a,b,c)=(8,3,5)$  
   $$m_b=\frac{3+2\cdot 5}{2}=6.5,\quad m_c=\frac{5+2\cdot 3}{2}=5.5,$$
   $$Z_0=\frac{3}{4}a=6,\quad Z_\Delta=\frac{|3-5|}{4}=0.5.$$
3. **$(4,1)\!\to\!5$**: $(a,b,c)=(5,4,1)$ (degenerate, “missing 3” resonance)  
   $$m_b=\frac{4+2}{2}=3,\quad m_c=\frac{1+8}{2}=4.5,\quad Z_0=3.75,\ Z_\Delta=0.75.$$
4. **$(4,3)\!\to\!7$** and **swap**: $(a,b,c)=(7,4,3)$ vs $(7,3,4)$  
   $$m_a=0.5,\ (m_b,m_c)=(5,5.5)\ \text{or}\ (5.5,5),$$
   $$Z_0=5.25=\frac{3}{4}a,\quad Z_\Delta=0.25=\frac{m_a}{2}.$$

---

## 9. Summary (Additive‑Collapse Theorem)
**Theorem.** For any $x,y\ge 0$ let $z=x+y$ and $(a,b,c)=(z,x,y)$. Then
$$
m_a=\frac{|b-c|}{2},\qquad m_b=\frac{b+2c}{2},\qquad m_c=\frac{c+2b}{2},
$$
and the invariants
$$
\frac{m_b+m_c}{2}=\frac{3}{4}a,\qquad m_c-m_b=\pm m_a
$$
form a complete **embedded index** of the collapse. Even splits give the triadic residue $3/8$ (perimeter‑normalized). Harmonic dynamics (AHRC/Ψ) act to close the drift to the Mark 1 attractor $\pi/9$.

---

## 10. Practical Use (Pipelines)
- Use $(m_b,m_c)$ to **reconstruct** $(b,c)$ via
  $$c=\frac{4m_b-2m_c}{3},\quad b=\frac{4m_c-2m_b}{3},\quad a=\frac{2}{3}(m_b+m_c).$$
- Track $\rho=\dfrac{b-c}{b+c}$ for imbalance and $\Delta_H$ for harmonic correction demand.
- For additive sequences (Fibonacci, digital streams), the chain of indices $\big(a_k,\tfrac34 a_k,\tfrac{|b_k-c_k|}{4}\big)$ provides a **π‑ray lattice** ready for AHRC/Ψ phase‑locking to $H_{\text{Mark1}}$.
