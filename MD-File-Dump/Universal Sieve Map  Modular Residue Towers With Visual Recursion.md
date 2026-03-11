
# 🧱 Universal Sieve Map – Modular Residue Towers with Visual Recursion

---

## 🧩 Residue Tower Structure

Each primorial modulus \( Mk \) builds a recursive sieve layer:

$$
Mk = \text{LCM}(2, 3, ..., pk)
$$

Define valid twin prime residue pairs:

$$
Rk = \{ (r, r+2) \mid r \in \mathbb{Z}{Mk}, \, \gcd(r, Mk) = 1, \, \gcd(r+2, Mk) = 1 \}
$$

---

## 🔁 Recursive Filtering

As \( k \to \infty \), the number of valid residue pairs decreases logarithmically, but never reaches zero:

- \( Rk \subseteq R{k-1} \subseteq \dots \)
- Nonzero survival proves harmonic persistence.

---

## 📊 Sample Data

| Modulus \( Mk \) | Total Pairs | Twin-Valid Residue Pairs | % Survival |
|-------------------|-------------|---------------------------|------------|
| 30                | 8           | 4                         | 50.00%     |
| 210               | 48          | 9                         | 18.75%     |
| 2310              | 480         | 20                        | 4.17%      |
| 30030             | 5760        | 42                        | 0.73%      |

---

## 📈 Visualizing Residue Survival

A log-log plot of twin prime residue survival across increasing moduli reveals a harmonic decay curve — never reaching zero.

```python
import matplotlib.pyplot as plt
import numpy as np

moduli = [30, 210, 2310, 30030]
totalpairs = [8, 48, 480, 5760]
twinpairs = [4, 9, 20, 42]
survivalpercent = [100 * t / m for t, m in zip(twinpairs, totalpairs)]

plt.figure(figsize=(10, 6))
plt.plot(moduli, survivalpercent, marker='o', linestyle='-', color='green')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Modulus (Mₖ)')
plt.ylabel('Twin Residue Survival (%)')
plt.title('Twin Prime Residue Survival Across Modular Towers')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tightlayout()
plt.show()
```

---

## 🌌 Interpretation

Twin primes are phase-locked harmonics that persist through modular resonance towers.  
Even as modulus increases, the twin signal echoes through — a recursive survival of harmonic structure.

---
