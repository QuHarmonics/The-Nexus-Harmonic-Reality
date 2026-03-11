# Avalanche as Widening: the Fan / Wedge View (with the Triangle Example)

This note formalizes your *“avalanche = anything that widens like a fan”* definition.  
The key idea is: **divergence can be measured by how *length*, *area*, or *volume* grows under a sweep**. In 2D, the “collective” effect naturally shows up as **area growth**, which is quadratic in scale.

---

## 1) The triangle you gave (and what it implies)

You specified:

- $a = 1$
- $b = 4$
- $c = 4.12311 = \sqrt{17}$
- area $= 2$
- perimeter $= 9.12311$
- circumradius $= 2.06155 = \sqrt{17}/2$

### 1.1 Area determines the included angle (backwards reasoning)

For any triangle with sides $a,b$ and included angle $C$ between them, the area is

$$
\\text{Area} = \\frac12 ab\\sin(C).
$$

Plugging in your values:

$$
2 = \\frac12(1)(4)\\sin(C) = 2\\sin(C)
\\quad\\Rightarrow\\quad
\\sin(C)=1
\\quad\\Rightarrow\\quad
C = 90^\\circ.
$$

So your triangle is **right-angled**, with legs $a=1$ and $b=4$.

### 1.2 Pythagorean confirmation of $c=\\sqrt{17}$

For a right triangle,

$$
c^2 = a^2 + b^2 = 1^2 + 4^2 = 17
\\quad\\Rightarrow\\quad
c = \\sqrt{17}.
$$

This is the “$a^2$ is right there” moment: **lengths square into areas** and (in higher dimensions) cube into volumes.

---

## 2) “Avalanche” as a widening wedge (fan geometry)

### 2.1 Width growth: the fan at distance $L$

A wedge with opening angle $\\alpha$ has a **width** at radius (travel distance) $L$ given by

$$
w(L) = 2L\\tan\\!\\left(\\frac{\\alpha}{2}\\right).
$$

This is **linear in $L$**.

### 2.2 “Collective” growth: swept area to distance $L$

If you track not just width but the **area covered by the widening**, the swept area is (sector model)

$$
A(L) = \\frac12 \\, \\alpha \\, L^2,
$$

which is **quadratic in $L$**.

So even when width grows linearly, the *footprint* grows like $L^2$. That’s why it feels like an “avalanche”: the **cumulative effect accelerates**.

---

## 3) Scaling law: why doubling length quadruples area

If you scale a whole 2D figure by a factor $k$ (all lengths multiply by $k$), then:

- lengths scale as $k$
- areas scale as $k^2$
- volumes (3D) scale as $k^3$

For your right triangle:

Original area:

$$
A = \\frac12 ab = \\frac12(1)(4) = 2.
$$

Scale by $k$:

$$
a' = ka,\\qquad b' = kb.
$$

New area:

$$
A' = \\frac12 (ka)(kb) = k^2\\left(\\frac12 ab\\right)=k^2A.
$$

So if you “make a 2” in the sense of doubling the linear scale ($k=2$),

$$
A' = 2^2A = 4A,
$$

i.e. area quadruples. This is exactly your “collective / cumulative” point.

---

## 4) When widening becomes *more* than quadratic

You also noted: “if the mountain narrows/widens, that’s part of it.”  
Mathematically: the opening angle can vary with distance, $\\alpha = \\alpha(L)$.

Then the incremental area added at radius $L$ is

$$
dA = \\frac12\\, \\alpha(L)\\, d(L^2) = \\alpha(L)\\,L\\,dL,
$$

so

$$
A(L) = \\int0^L \\alpha(r)\\, r\\, dr.
$$

If $\\alpha(r)$ increases with $r$, the sweep accelerates *faster* than the constant-angle case; if it decreases, the avalanche “pinches” and slows.

---

## 5) “A is also a manifold”: what that means in practice

A **manifold** is a space that *locally* looks flat like $\\mathbb{R}^k$ (you can take small steps and talk about directions), but *globally* it may curve, wrap, or have constraints.

In your wedge picture, the “manifold” can be taken as:

- the **state-space** you’re moving through,
- with a local notion of step and direction,
- and a global boundary/wrap that can turn straight travel into a sweep.

A flat edge that “opens to a full circle” is a perfect intuition: locally it’s a line segment; globally it can be a loop.

---

## 6) The clean generalization: expansion of measure under a map (Jacobian)

To formalize “widening” without relying on pictures, consider a transformation (a mapping)

$$
f:\\mathbb{R}^n \\to \\mathbb{R}^n.
$$

The **Jacobian matrix** at point $x$ is $Jf(x)$ (the matrix of partial derivatives). Then:

- in 1D, local stretch is $|f'(x)|$,
- in 2D, local **area expansion** is $|\\det Jf(x)|$,
- in 3D, local **volume expansion** is $|\\det Jf(x)|$.

So a precise definition of “avalanche as widening” is:

> Avalanche occurs when the mapping expands *measure* (length/area/volume) so that small regions spread into larger regions as you move forward.

In 2D, that is exactly:

$$
\\text{local area gain} = \\left|\\det Jf(x)\\right|.
$$

If $\\left|\\det Jf(x)\\right|>1$ over a region, the region expands—your “fan opens.”

---

## 7) Putting it all together (your frame, made explicit)

- Two points can define a line (a chord), but they do not define **turning**.
- A third point defines curvature/intent (discrete second difference):

$$
v = p1 - p0,\\qquad
a = p2 - 2p1 + p0.
$$

- A small angular opening $\\alpha$ creates a wedge whose width grows like $L$ but whose **area** grows like $L^2$:

$$
w(L)=2L\\tan\\left(\\frac{\\alpha}{2}\\right),\\qquad
A(L)=\\frac12\\alpha L^2.
$$

- Scaling a system by $k$ multiplies area by $k^2$ (collective amplification).
- If the opening changes with distance, the “mountain shape” becomes part of the avalanche:

$$
A(L)=\\int0^L \\alpha(r)\\, r\\, dr.
$$

- The most general statement is measure expansion under a map, captured by the Jacobian determinant:

$$
\\text{area/volume gain} = |\\det Jf(x)|.
$$

That is the complete mathematical backbone of your “avalanche = widening fan” concept: **divergence measured as growth of footprint**, not just separation along a single line.

---
