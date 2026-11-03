# Residue Grid: Affine Modular Lattice (Corrected) — plus Fibonacci–$e$ and BBP context

This document consolidates and corrects the key claims about the “53-seed” residue grid and its interpretation. It also clarifies the separate Fibonacci–$e$ numeric check and the BBP (Bailey–Borwein–Plouffe) $\pi$-hex digit extractor context.

---

## 1) The grid definition (what is being generated)

We define a 2D residue field over integer coordinates $(a,b)$ using:

$$
R(a,b) \equiv \left(s + u(a-1) + v(b-1)\right) \bmod m
$$

with the concrete parameters:

- seed $s = 53$
- vertical step $u = 4$ (increment when $a \mapsto a+1$)
- horizontal step $v = 56$ (increment when $b \mapsto b+1$)
- modulus $m = 100$

So explicitly:

$$
R(a,b) \equiv \left(53 + 4(a-1) + 56(b-1)\right) \bmod 100.
$$

A common “visibility mask” used in the demo is:

$$
a+b \le 10
$$

which crops the infinite periodic lattice to a finite triangular window.

### Vector form (useful for reasoning)

Let $\Delta = \begin{bmatrix}a-1\\ b-1\end{bmatrix}$ and $w = \begin{bmatrix}u\\ v\end{bmatrix}$. Then

$$
R(a,b) \equiv (s + w^\top \Delta) \bmod m.
$$

This is an **affine linear form modulo $m$**—a modular lattice.

---

## 2) Correction: this is not a “true LCG” in the recursive sense

A standard (1D) linear congruential generator (LCG) is a **recurrence**:

$$
X_{n+1} \equiv (A X_n + C) \bmod m.
$$

The grid formula above **does not** depend on $R(a,b)$ to produce the next value. It is **direct evaluation** of a linear form in $(a,b)$.

### What is true (and still useful)

Along any straight path where you increment one coordinate by $1$ each step, the values *do* follow a simple modular recurrence—specifically an **additive congruential generator** (the special case $A=1$):

- Moving right: $(a,b)\mapsto(a,b+1)$
  $$
  R(a,b+1) \equiv R(a,b) + v \pmod m
  $$

- Moving down: $(a,b)\mapsto(a+1,b)$
  $$
  R(a+1,b) \equiv R(a,b) + u \pmod m
  $$

So: **the grid is an affine modular lattice; each row/column is an additive congruential sequence.** Calling it “LCG-like” is fine as intuition, but the mathematically precise label is:

> **2D affine congruential map** (linear form modulo $m$), with 1D additive congruential sequences along coordinate directions.

---

## 3) Period and reachable values (the key modular facts)

### 3.1 Axis periods

The period of repeated stepping by $k$ mod $m$ is:

$$
\text{period}(k;m) = \frac{m}{\gcd(k,m)}.
$$

Here:

- $\gcd(u,m) = \gcd(4,100) = 4$  
  $$
  \Rightarrow \text{period}(u;m) = \frac{100}{\gcd(u,m)} = 25
  $$

- $\gcd(v,m) = \gcd(56,100) = 4$  
  $$
  \Rightarrow \text{period}(v;m) = \frac{100}{\gcd(v,m)} = 25
  $$

So every fixed row repeats every $\text{period}(v;m)=25$ steps in $b$, and every fixed column repeats every $\text{period}(u;m)=25$ steps in $a$.

Equivalently:

$$
R(a+25,b) = R(a,b), \qquad R(a,b+25) = R(a,b).
$$

### 3.2 Only 25 distinct residues exist (global constraint)

Since both increments are multiples of $\gcd(u,v,m)=4$, we have:

$$
u(a-1) + v(b-1) \equiv 0 \pmod 4
$$

which implies:

$$
R(a,b) \equiv s \pmod 4.
$$

Because $s=53\equiv 1\pmod 4$, the grid can only ever hit residues congruent to 1 modulo $4$. That means **exactly $100/4 = 25$ residues are reachable** in the entire infinite grid.

This corrects any claim that the grid “scrambles across all 00–99.” It cannot; it lives on a 25-value coset.

---

## 4) Correction: row-major traversal is not a standard LCG

A claim like “if you traverse row-major it becomes a standard LCG with a combined step” is generally **false**.

If a row has width $W$, a row-major index $n$ maps to:

$$
a = \left\lfloor \frac{n}{W} \right\rfloor + 1, \qquad b = (n \bmod W) + 1.
$$

Substituting into the grid formula gives a **piecewise** expression involving both $\left\lfloor n/W\right\rfloor$ and $(n\bmod W)$:

$$
R(n) \equiv \left(s + u\left\lfloor \frac{n}{W} \right\rfloor + v(n \bmod W)\right) \bmod m,
$$

which is not of the LCG form $R(n+1)=AR(n)+C \bmod m$ with constant $A,C$.

If you want a true 1D recurrence, pick a **path with constant step vector** (e.g., diagonal). Example: along $(a,b)\mapsto(a+1,b+1)$, the step is $(u+v)\bmod m = (4+56)\bmod 100 = 60$:

$$
R(a+1,b+1) \equiv R(a,b) + (u+v) \pmod m.
$$

That is still additive (not multiplicative), and its period is:

$$
\frac{m}{\gcd(u+v,m)} = \frac{100}{\gcd(60,100)} = 5.
$$

So the diagonal repeats very quickly—another reason to avoid calling this “hash-like” without qualifiers.

---

## 5) Why it *looks* random in the cropped view

Even though the structure is linear, it can look “noisy” when:

1. You view only a small crop (e.g., $a+b\le 10$) rather than a full period tile.
2. You map values into a **nonlinear display predicate**, e.g. “print only when printable ASCII.”

A typical predicate for ASCII visibility is:

$$
\text{visible}(a,b) =
\begin{cases}
1,& 33 \le R(a,b) \le 126\\
0,& \text{otherwise}
\end{cases}
$$

This turns a smooth modular lattice into a **thresholded point field**, which can visually resemble “random scattering.” The “chaos” is in the *masking*, not in the generator.

### Correction on the “45/129” ratio

For the common $9\times 9$ window with mask $a+b\le 10$, the number of included cells is:

$$
\sum_{a=1}^{9} (10-a) = 45.
$$

If the underlying uncropped window is $9\times 9$, the total is $81$, so the ratio is:

$$
\frac{45}{81} = 0.555\ldots
$$

So the specific ratio $45/129\approx 0.3488$ cannot describe a $9\times 9$ crop. If “129” is a different denominator (e.g., a multi-layer count), it must be defined explicitly; otherwise it is inconsistent.

---

## 6) Correction: the $56/4$ “$\pi$-closeness” claim

The statement “$56/4=14$ is close to $\pi$” is false:

$$
14 - \pi \approx 10.8584.
$$

The **actual** quantity that is close-ish to $\pi$ is:

$$
\frac{14}{4} = 3.5,
$$

and the difference is:

$$
3.5 - \pi \approx 0.358407346410207.
$$

If you want to express this using the grid steps, one legitimate (though still numerological) way is:

$$
\frac{v}{16} = \frac{56}{16} = 3.5 \approx \pi + 0.3584.
$$

This corrects the earlier arithmetic slip (missing the divide-by-4).

---

## 7) Fibonacci–$e$ check (your “is the error close to $\varphi$?” question)

You gave:

- $n=30$
- $F_n = 832040$
- an approximation $e_n = 2.718280194740024$
- error $\varepsilon_n = 1.633719021398861\times 10^{-6}$

If we interpret that as:

$$
\varepsilon_n = e - e_n,
$$

then with $e=2.718281828459045\ldots$ we get:

$$
\varepsilon_n \approx 1.633719020954771395e-06.
$$

### Is $\varepsilon_n$ “close to $\varphi$”?

Not directly: $\varphi\approx 1.6180339887$ is order-1, while $\varepsilon_n$ is order $10^{-6}$.

However, if you compare to the *scaled* quantity $\varphi\times 10^{-6}$:

$$
\varphi\times 10^{-6} \approx 1.618033988749894843e-06,
$$

then

$$
\varepsilon_n - \varphi\times 10^{-6} \approx 1.568503220487655215e-08.
$$

Relative difference (dimensionless):

$$
\frac{\varepsilon_n}{\varphi\times 10^{-6}} - 1 \approx 0.009694.
$$

So the error is within about **1%** of $\varphi\times 10^{-6}$. Without a derivation that forces $\varphi$ into the approximation mechanism, treat this as **likely coincidence**, not evidence of structural coupling.

---

## 8) BBP context (for $\pi$ hex digits)

The BBP formula is:

$$
\pi = \sum_{k=0}^\infty \frac{1}{16^k}
\left(
\frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} - \frac{1}{8k+6}
\right).
$$

It enables extraction of hexadecimal digits of $\pi$ without computing all prior digits (a base-16 positional digit-extraction property).

This is **separate** from the residue-grid lattice. Both are modular/arithmetic phenomena, but their mechanisms are different:

- Grid: **affine linear form mod 100**, periodic, 25 reachable residues.
- BBP: **rapidly convergent series with base-16 structure**, digit-extraction property in base 16.

---

## 9) Bottom line

**Airtight:**
- The grid is deterministic.
- The closed form $R(a,b)=(s+u(a-1)+v(b-1))\bmod m$ exactly generates it.
- The “randomness” impression comes from masking/cropping and display predicates.

**Corrected:**
- It is **not** a recursive LCG in the strict sense; it is an affine modular lattice.
- Row-major traversal does **not** turn it into a standard LCG.
- $56/4=14$ is **not** “close to $\pi$”; the meaningful comparison is $3.5\approx \pi+0.3584$.
- The grid cannot hit all residues 0–99; it hits **exactly 25** residues (a single class modulo 4).
- The Fibonacci–$e$ error is not “close to $\varphi$” unless you explicitly scale by $10^{-6}$; even then it is only within ~1%.

---

*Generated on 2026-01-22.*
