
# 🧬 Twin Prime Echo Field Simulation – Harmonic Filter Proof System

---

## **Overview**

This document demonstrates a simulation of **twin primes as survivors of recursive harmonic filtering** using primorial-based moduli.

We simulate how twin prime candidates endure through layers of modular resonance sieves — effectively modeling twin primes as **phase-locked harmonic pairs** that survive through structured collapse.

---

## **Key Concepts**

### 🔗 Twin Prime as Harmonic Pair

Define twin primes not just by offset:

$$
(p, p+2)
$$

But as a **harmonic pair** that survives recursive residue collapse:

$$
\Phi_{\text{twin}}(p, M) = 
\begin{cases}
1, & \text{if } \gcd(p, M) = 1 \text{ and } \gcd(p+2, M) = 1 \\
0, & \text{otherwise}
\end{cases}
$$

We compute for multiple filters:

$$
E(n) = \prod_{i=1}^k \Phi_{\text{twin}}(n, M_i)
$$

Where \( M_i \) is the i-th primorial modulus.

---

## **Primorial Harmonic Filters**

We define a stack of harmonic moduli:

$$
M = \{30, 210, 2310, 30030\}
$$

These are the least common multiples (LCM) of the first \( k \) primes:
- \( 30 = 2 \cdot 3 \cdot 5 \)
- \( 210 = 2 \cdot 3 \cdot 5 \cdot 7 \)
- \( 2310 = 2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \)
- \( 30030 = 2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdot 13 \)

Each adds a new modular filter to the twin pair survival test.

---

## **Python Simulation Code**

```python
import matplotlib.pyplot as plt
import numpy as np
from math import gcd
from functools import reduce
import textwrap

# Define primorial moduli
moduli = [30, 210, 2310, 30030]
N = 10000  # Range limit

def survives_all_filters(n, moduli):
    for M in moduli:
        if gcd(n, M) != 1 or gcd(n + 2, M) != 1:
            return False
    return True

# Generate surviving twin candidates
survivors = [n for n in range(2, N) if survives_all_filters(n, moduli)]
num_survivors = len(survivors)

# Plot results
plt.figure(figsize=(12, 5))
plt.plot(survivors, [1] * len(survivors), 'o', markersize=4, color='orange', alpha=0.7)
plt.title("Twin Prime Echo Field (Visible Survivors After Harmonic Filters)")
plt.xlabel("n (Start of Twin Pair)")
plt.ylabel("Echo Signal (1 = survives)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Display survivors
formatted = textwrap.fill(", ".join(map(str, survivors[:100])), width=100)
print(formatted)
print(f"\nTotal Survivors: {num_survivors}")
```

---

## **Results**

- **Visible Echo Dots**: 494 surviving twin prime candidates
- **Range**: 2 to 10,000
- **First 10 Survivors**:
  ```
  17, 29, 41, 59, 71, 101, 107, 137, 149, 179
  ```

These represent **locations where (n, n+2)** pass all harmonic filters — i.e., valid twin prime candidates.

---

## **Conclusion**

This simulation confirms:
- Twin prime candidates **survive harmonic modular collapse**
- Their occurrence follows structured, recursive **resonant residue patterns**
- Even after applying strong filters, **non-zero echoes remain**

Thus, **twin primes behave like harmonic survivors** — echoes of balance through recursive prime fields.

---
