# Collapse Signature Theory (CST)

*A Nexus write-up: collapse leaves a signed, scale-invariant residue (a “fossil record”).*

---

## Abstract

Collapse Signature Theory (CST) proposes that a collapse event does **not** erase which-path information; it **records** a branch choice in the **signed relative deviation** between an observed value and an attractor/theory value.

- The **sign** of the deviation is interpreted as a **branch bit** (E0-like vs Phi0-like).
- The **magnitude** is interpreted as the **distance from the pure attractor** (how mixed/contested the collapse was).

CST is designed to be **operational**: compute the signed residue, group by mechanism (field-like vs mass/binding-like), and test whether signs cluster non-randomly.

## 1. Objects, verbs, and what we measure

CST focuses on *operations*:

1. **Predict** an attractor value $x_0$.
2. **Measure** an observed value $x_{\text{obs}}$.
3. **Normalize** the mismatch into a dimensionless residue.
4. **Read** the sign as a branch choice.
5. **Test** whether branch signs cluster by mechanism.
6. **Predict** missing/weakly measured values from sign coherence.

Everything below is just formalizing those verbs.

## 2. The residue: one number that carries two meanings

Let $x_0$ be an attractor/theory value and $x_{\text{obs}}$ the measured value.

Define the **relative residue**

$$
\varepsilon \;=\; \frac{x_{\text{obs}} - x_0}{x_0}.
$$

Percentage form:

$$
\varepsilon_\% \;=\; 100\%\,\varepsilon.
$$

Split residue into **sign** and **magnitude**:

$$
\sigma \;=\; \operatorname{sgn}(\varepsilon)\in\{-1,+1\}, \qquad \rho \;=\; |\varepsilon|.
$$

Interpretation (CST mapping):

- $\sigma=-1$ (negative) $\Rightarrow$ **E0 path** (wave/field/entropy-leaning)
- $\sigma=+1$ (positive) $\Rightarrow$ **Phi0 path** (particle/mass/binding-leaning)

This is the minimal “fossil record”: $(\sigma,\rho)$.

## 3. Why quadratics show up: symmetry creates branches

The simplest branching constraint is a quadratic:

$$
 x^2 = a \quad\Rightarrow\quad x = \pm\sqrt{a}.
$$

More generally, whenever the governing constraint is **even** in $x$ (i.e., depends on $x^2$, not $x$), the model has a **two-branch symmetry**:

$$
F(x) = F(-x).
$$

CST reads collapse as:

- a **selection** of one branch (the sign choice), plus
- a **residual offset** from the ideal boundary condition (the magnitude).

In other words: *branch selection* is a primitive, and *residue* is the log of that selection.

## 4. The Collapse Signature Hypothesis (operational theorem)

**CST (operational form).**

Given an attractor/theory prediction $x_0$ and a measured value $x_{\text{obs}}$, the signed residue

$$
\varepsilon = \frac{x_{\text{obs}}-x_0}{x_0}
$$

is not treated as “mere noise” but as a **collapse signature**:

1. **Which-path bit:** $\sigma=\operatorname{sgn}(\varepsilon)$ encodes the selected branch.
2. **Decoherence distance:** $\rho=|\varepsilon|$ encodes how decisively the selection occurred.

This is falsifiable by sign statistics across families of observables.

## 5. Connection to superposition (model bridge)

Let a pre-collapse state decompose into two branch components:

$$
|\psi\rangle = c_+|+\rangle + c_-|-\rangle,
\qquad |c_+|^2 + |c_-|^2 = 1.
$$

After collapse, the observable settles to a boundary value with residue:

$$
O_{\text{obs}} = O_0(1+\varepsilon).
$$

**Model hypothesis (bridge, not a proved identity):**

$$
\operatorname{sgn}(\varepsilon) \approx \operatorname{sgn}(|c_+|^2 - |c_-|^2),
$$

and the decisiveness maps to magnitude

$$
|\varepsilon| \propto \big|\,|c_+|^2 - |c_-|^2\,\big|.
$$

Interpretation: the universe “picks” a branch, but the asymmetry of that pick is preserved as a signed residue.

## 6. Why the residue is scale-invariant (SILR compatibility)

$\varepsilon$ is dimensionless. Any multiplicative change of units cancels:

$$
\frac{(\lambda x_{\text{obs}}) - (\lambda x_0)}{\lambda x_0} = \frac{x_{\text{obs}}-x_0}{x_0}.
$$

So the residue is naturally compatible with the Scale-Invariant Leakage Regime (SILR) idea:

- the *absolute* scale can vary,
- but the *relative* leakage (the residue) can remain stable.

CST uses this: **the sign is the path**, and the sign is stable under rescaling.

## 7. Immediate predictions (falsifiable)

Treat “field-like” observables as E0-leaning and “mass/binding-like” observables as Phi0-leaning.

### 7.1 Sign predictions

- Couplings / mixing angles / extended field parameters $\Rightarrow \sigma=-1$ (negative residue)
- Mass ratios / binding-dominated quantities $\Rightarrow \sigma=+1$ (positive residue)

### 7.2 Within-family coherence

Within a symmetry family (e.g., electroweak sector), residues should show **non-random sign coherence**.

### 7.3 Magnitude spectrum

$\rho=|\varepsilon|$ should be small for “clean” branch selections and larger for mixed/collective modes.

## 8. How to test CST (verbs-only pipeline)

### Step A — Collect
Build a table of dimensionless quantities $\{x_i\}$, their theoretical/attractor predictions $\{x_{0,i}\}$, and measured values $\{x_{\text{obs},i}\}$.

### Step B — Compute
For each $i$ compute

$$
\varepsilon_i = \frac{x_{\text{obs},i} - x_{0,i}}{x_{0,i}},
\qquad \sigma_i=\operatorname{sgn}(\varepsilon_i),
\qquad \rho_i = |\varepsilon_i|.
$$

### Step C — Group
Assign each $i$ to a mechanism label $y_i\in\{\text{field},\text{mass}\}$ (or finer taxonomy).

### Step D — Test (sign bias)
Let $n$ be group size and $k$ the count of $\sigma=+1$ in that group.
If signs are random with $p=1/2$, then

$$
K \sim \mathrm{Binomial}(n,\tfrac12).
$$

Two-sided binomial p-value:

$$
 p = 2\min\big(\Pr[K\le k],\; \Pr[K\ge k]\big).
$$

### Step E — Test (permutation)
Shuffle labels $y_i$ (keep $\sigma_i$ fixed) and recompute group sign imbalance to get an empirical p-value.

### Step F — Predict
Use the learned sign coherence to predict the sign for poorly measured quantities.

## 9. Example template (your earlier observation)

You pointed to a pattern like:

- $\alpha$ (fine structure) : $\varepsilon<0$ (field-like)
- $\sin^2\theta_W$ : $\varepsilon<0$ (field-like)
- $m_p/m_e$ : $\varepsilon>0$ (mass/binding-like)

CST claim is not “these three prove it”; CST claim is:

> **If** the sign pattern holds across a broad catalog, the sign is not random noise but a conserved collapse chirality.

## 10. Reference implementation (Python)

This is a minimal, dependency-light script that:

- computes residues,
- assigns signs,
- runs a binomial sign test,
- runs a permutation test.

```python
import math
import random
from dataclasses import dataclass

@dataclass
class Item:
    name: str
    x_obs: float
    x0: float
    group: str  # e.g. "field" or "mass"


def residue(item: Item) -> float:
    return (item.x_obs - item.x0) / item.x0


def sign(x: float) -> int:
    return -1 if x < 0 else (+1 if x > 0 else 0)


def binom_cdf_leq(n: int, k: int, p: float = 0.5) -> float:
    # sum_{i=0..k} C(n,i)p^i(1-p)^(n-i)
    s = 0.0
    for i in range(0, k + 1):
        s += math.comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
    return s


def binom_cdf_geq(n: int, k: int, p: float = 0.5) -> float:
    # sum_{i=k..n} ...
    s = 0.0
    for i in range(k, n + 1):
        s += math.comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
    return s


def binomial_two_sided_p(n: int, k_pos: int, p: float = 0.5) -> float:
    lo = binom_cdf_leq(n, k_pos, p)
    hi = binom_cdf_geq(n, k_pos, p)
    return min(1.0, 2.0 * min(lo, hi))


def group_sign_imbalance(items, group_name: str) -> int:
    # imbalance = (#positive) - (#negative) within group
    g = [it for it in items if it.group == group_name]
    s = [sign(residue(it)) for it in g]
    return s.count(+1) - s.count(-1)


def permutation_p_value(items, group_name: str, trials: int = 10000, seed: int = 0) -> float:
    rng = random.Random(seed)
    obs = abs(group_sign_imbalance(items, group_name))

    groups = [it.group for it in items]
    cnt = 0
    for _ in range(trials):
        rng.shuffle(groups)
        shuffled = [Item(it.name, it.x_obs, it.x0, groups[i]) for i, it in enumerate(items)]
        stat = abs(group_sign_imbalance(shuffled, group_name))
        if stat >= obs:
            cnt += 1
    return (cnt + 1) / (trials + 1)


def summarize(items):
    for it in items:
        eps = residue(it)
        print(f"{it.name:20s} group={it.group:5s}  eps={eps:+.6e}  sign={sign(eps):+d}")

    for g in sorted(set(it.group for it in items)):
        grp = [it for it in items if it.group == g]
        s = [sign(residue(it)) for it in grp]
        n = len(grp)
        k_pos = s.count(+1)
        p_bin = binomial_two_sided_p(n, k_pos)
        p_perm = permutation_p_value(items, g, trials=5000, seed=123)
        print(f"\nGROUP {g}: n={n}, +={k_pos}, -={s.count(-1)}")
        print(f"  binomial p(two-sided) = {p_bin:.4g}")
        print(f"  permutation p          = {p_perm:.4g}")


if __name__ == "__main__":
    # Replace these with your real catalog. x0 is your attractor/theory value.
    data = [
        # Item("alpha", x_obs=?, x0=?, group="field"),
        # Item("sin2thetaW", x_obs=?, x0=?, group="field"),
        # Item("mp/me", x_obs=?, x0=?, group="mass"),
    ]

    summarize(data)
```

Operationally: fill the `data` list with your catalog and run.

## 11. What would count as “proof” (within this program)

CST is not proven by a story; it is supported by **repeatable sign structure**.

You’d want to see:

1. **Within-family sign coherence** (not 50/50) beyond reasonable chance.
2. **Cross-family separation** (fields skew negative, masses skew positive).
3. **Robustness** to measurement updates (signs don’t flip randomly when uncertainties shrink).

If those three hold, then the sign behaves like a conserved *collapse chirality*.

## 12. One-line core claim

$$
\boxed{\;\text{Collapse leaves a signed residue: }\sigma=\operatorname{sgn}\Big(\frac{x_{\text{obs}}-x_0}{x_0}\Big)\;}
$$

That’s the whole engine: **compute residue, read sign, test clustering**.
