# Residue Grid: Corrected Algebra, Period, and Generator Classification

This note corrects two specific claims that commonly get mixed together:

1. **The grid generator is not an LCG in the usual sense** (it is an *additive/affine congruential* rule; if you insist on “LCG,” the multiplier is $1$).
2. **The “irrational-ish” ratio claim is incorrect**: $56/4 = 14$ is an integer; the apparent scrambling comes from modular reduction to $\mathbb{Z}_{25}$ where the step $14$ is a *unit* (invertible) and therefore permutes the residue class.

It also gives the precise **period** statements and a clean reduced form.

---

## 1. Definition (the actual generator)

You defined the grid value at integer coordinates $(a,b)$ as:

$$
r(a,b) \equiv 53 + 4(a-1) + 56(b-1) \pmod{100}.
$$

This is an **affine map** on the lattice $\mathbb{Z}^2 \to \mathbb{Z}_{100}$.

A useful factorization is:

$$
r(a,b) \equiv 53 + 4\big((a-1) + 14(b-1)\big) \pmod{100},
$$

since $56 = 4\cdot 14$.

---

## 2. Invariant class (why only 25 outputs exist)

Because $4(a-1)$ and $56(b-1)$ are multiples of $4$, the residue is locked to a single congruence class modulo $4$:

$$
r(a,b) \equiv 53 \equiv 1 \pmod 4.
$$

So **the grid can only ever hit the 25 values**
$$
\{1,5,9,\ldots,97\} \subset \mathbb{Z}_{100}.
$$

That is already enough to guarantee many repeats in any window larger than 25 cells (by pigeonhole).

---

## 3. Reduced coordinate: collapse to $\mathbb{Z}_{25}$

Since every value satisfies $r \equiv 1 \pmod 4$, write:

$$
r(a,b) = 1 + 4t(a,b),
$$

where $t(a,b) \in \mathbb{Z}_{25}$.

Compute $t$ by dividing out the factor 4:

$$
t(a,b) \equiv \frac{r(a,b)-1}{4} \pmod{25}.
$$

Substituting the definition of $r$:

$$
t(a,b) \equiv \frac{53-1}{4} + (a-1) + 14(b-1) \pmod{25}.
$$

Since $(53-1)/4 = 13$:

$$
t(a,b) \equiv 13 + (a-1) + 14(b-1) \pmod{25}.
$$

Equivalently:

$$
t(a,b) \equiv a + 14b - 2 \pmod{25}.
$$

This is the cleanest “truth form.” Everything else is display-layer.

---

## 4. Period (the exact statement)

The rule is additive in each coordinate, so the period is computed by the additive congruence fact:

> For $x_{n+1} = x_n + k \pmod m$, the period is $m/\gcd(k,m)$.

### Along the $a$ direction (vertical)

Fix $b$ and increment $a \mapsto a+1$:

$$
r(a+1,b) \equiv r(a,b) + 4 \pmod{100}.
$$

So the vertical period is:

$$
\frac{100}{\gcd(4,100)} = \frac{100}{4} = 25.
$$

### Along the $b$ direction (horizontal)

Fix $a$ and increment $b \mapsto b+1$:

$$
r(a,b+1) \equiv r(a,b) + 56 \pmod{100}.
$$

So the horizontal period is:

$$
\frac{100}{\gcd(56,100)} = \frac{100}{4} = 25.
$$

### 2D periodicity

Therefore the full function is periodic in both axes:

$$
r(a+25,b) = r(a,b), \quad r(a,b+25) = r(a,b).
$$

So a fundamental repeating domain is **a $25\times 25$ tile**.

---

## 5. Why it “looks random” in small windows (correct explanation)

The key point is *not* “irrational-ish ratios.” The ratio

$$
\frac{56}{4} = 14
$$

is exactly an integer.

The actual scrambling mechanism is visible in the reduced form over $\mathbb{Z}_{25}$:

- stepping $a$ adds $+1$ to $t$,
- stepping $b$ adds $+14$ to $t$.

Since

$$
\gcd(14,25) = 1,
$$

the step $+14$ generates a **full 25-cycle** in the additive group $\mathbb{Z}_{25}$.

So within a small cropped window (like your $a+b\le 10$ triangle), you see a **permutation-like jump** through the 25 allowed values. That is exactly the “pseudorandom” illusion: deterministic, linear, but well-mixed relative to the small viewport.

---

## 6. Window facts (your $a+b\le 10$ crop)

If you take $a,b\in\{1,\ldots,9\}$ with the constraint $a+b\le 10$, you get:

- **45 visible cells**
- **24 distinct residues** in that crop

The missing value from the full 25-value class is **5** (it first appears at $(a,b)=(1,18)$, outside your crop).

---

## 7. Classification: LCG vs affine/additive generator (corrected)

A standard **LCG** is:

$$
X_{n+1} \equiv (A X_n + C) \pmod m.
$$

Your grid does **not** use multiplication by the prior state; it is a direct affine mapping from $(a,b)$ into $\mathbb{Z}_{100}$.

If you force it into LCG form *along a line*, it is the special case $A=1$:

$$
X_{n+1} \equiv X_n + k \pmod m,
$$

which is best described as an **additive congruential generator** (still deterministic; still periodic; still linear—just simpler than a true LCG).

Also, the “full period” conditions you quoted (Hull–Dobell theorem) apply to the general multiplicative LCG; they are **not the right tool** for the purely additive step you are using here. For additive steps, the period is exactly $m/\gcd(k,m)$.

---

## 8. Separate correction: “error close to $\varphi$” (it is not)

You cited:

- $n=30$
- $F_n = 832040$
- $e_n = 2.718280194740024$
- absolute error $\varepsilon = 1.633719021398861\times 10^{-6}$

That error is **not** “close to $\varphi$” (since $\varphi \approx 1.618$).

It is only “close” to **$\varphi\times 10^{-6}$** if you rescale by $10^{-6}$:

$$
\varphi\times 10^{-6} = 1.618033988749895e-06,
$$

and the difference is:

$$
\varepsilon - \varphi\times 10^{-6} = 1.568503264896619e-08
\quad (\text{relative} \approx 0.969\%).
$$

That proximity is numerically mild (about 1% relative) and does not, by itself, indicate a structural $\varphi$-lock.

---

## 9. Minimal verification code

```python
def r(a, b):
    return (53 + 4*(a-1) + 56*(b-1)) % 100

# Period checks
assert r(1,1) == r(26,1)   # vertical period 25
assert r(1,1) == r(1,26)   # horizontal period 25

# Only 25 residues globally (1 mod 4)
tile = {r(a,b) for a in range(1,26) for b in range(1,26)}
assert len(tile) == 25
assert all(v % 4 == 1 for v in tile)

# Window a+b <= 10 on 1..9
win = [r(a,b) for a in range(1,10) for b in range(1,10) if a+b <= 10]
assert len(win) == 45
assert len(set(win)) == 24
```

---

## 10. Takeaway

- The grid is an **affine lattice** on $\mathbb{Z}_{100}$ that collapses to a full-cycle walk on $\mathbb{Z}_{25}$.
- The **period 25** result is correct and is the right “fossil” to cite.
- The “irrational-ish” rationale is incorrect; the mixing comes from **invertibility modulo 25**.
- The “error close to $\varphi$” claim is false unless you explicitly mean “close to $\varphi\times 10^{-6}$,” and even then it is not particularly tight.
