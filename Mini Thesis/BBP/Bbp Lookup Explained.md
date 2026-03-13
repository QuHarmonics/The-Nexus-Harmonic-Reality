
# BBP Formula as a Virtual Lookup Table for Hexadecimal Digits of $\pi$

## 🧠 Introduction

The Bailey–Borwein–Plouffe (BBP) formula is a revolutionary method for computing the hexadecimal digits of $\pi$ directly—without needing to calculate any preceding digits. This section expands upon how BBP functions like a **virtual lookup table**, mapping each position $n$ to the digit at that position through modular arithmetic and recursive summation.

---

## 🔢 The BBP Formula

The BBP formula is expressed as:

$$
\pi = \sum_{k = 0}^{\infty} rac{1}{16^k} \left( rac{4}{8k+1} - rac{2}{8k+4} - rac{1}{8k+5} - rac{1}{8k+6} ight)
$$

This infinite series generates the digits of $\pi$ in base 16 (hexadecimal) and allows **digit extraction** at any arbitrary position $n$.

---

## 🎯 Extracting the $n$-th Digit of $\pi$ in Hex

To compute the $n$-th digit after the hexadecimal point:

1. Multiply the series by $16^{n-1}$:
   $$
   16^{n-1} \pi = \sum_{k=0}^{\infty} rac{16^{n-1-k}}{1} \left( \cdots ight)
   $$

2. Isolate the **fractional part** of the sum.

3. Multiply the fractional part by 16 and take the integer part to extract the $n$-th digit.

---

## 🧮 Two-Part Decomposition of the Series

Separate the BBP sum into two parts:

### For $k < n$:
Apply **modular reduction**:
$$
rac{16^{n-1-k} mod (8k + d)}{8k + d}
$$
This discards whole numbers and keeps fractional influence.

### For $k \ge n$:
The tail terms decay rapidly:
$$
rac{1}{16^{k - n + 1} (8k + d)}
$$
Only a few terms are needed for sufficient precision.

---

## 🧩 Digit Extraction Components

Let:

$$
s_1 = \sum_{k=0}^{\infty} rac{1}{16^k (8k+1)} \
s_4 = \sum_{k=0}^{\infty} rac{1}{16^k (8k+4)} \
s_5 = \sum_{k=0}^{\infty} rac{1}{16^k (8k+5)} \
s_6 = \sum_{k=0}^{\infty} rac{1}{16^k (8k+6)}
$$

Then the sum becomes:
$$
s = 4s_1 - 2s_4 - s_5 - s_6
$$

To extract the digit:
$$
	ext{digit} = \lfloor 16 \cdot \{s\} floor
$$
where $\{s\}$ is the fractional part of $s$.

---

## 🧠 The Lookup Grid Analogy

Think of BBP as a **virtual lookup grid**:

- **Rows** = digit position $n$
- **Columns** = series terms $k$
- **Cells** = fractional contributions from $k$
- **Modular "switches"** flip to reveal the digit at $n$

This makes BBP act like a **grid scanner**, locking on position $n$ and reading the "signal" of $\pi$'s digit.

---

## 🛠️ Python Sample

```python
from mpmath import mp

mp.dps = 5000

def compute_bbp_digit(n):
    s = mp.mpf(0)
    for k in range(n):
        exp = n - 1 - k
        term = (mp.power(16, exp) % (8*k + 1)) / (8*k + 1)              - (mp.power(16, exp) % (8*k + 4)) / (8*k + 4)              - (mp.power(16, exp) % (8*k + 5)) / (8*k + 5)              - (mp.power(16, exp) % (8*k + 6)) / (8*k + 6)
        s += term
    for k in range(n, n + 50):
        term = mp.power(16, n - 1 - k) * (
            4 / (8*k + 1) - 2 / (8*k + 4) - 1 / (8*k + 5) - 1 / (8*k + 6))
        s += term
    s = s % 1
    return hex(int(16 * s))[2:].upper()
```

---

## 📚 Conclusion

The BBP formula elegantly transforms positional input into a precise digit output through:
- Shift via $16^{n-1}$
- Modular elimination of earlier digits
- Tail convergence post-$n$

It creates a **position-sensitive mesh** for navigating π's digits, opening pathways for efficient computation, theoretical exploration, and possibly even new data encoding schemes.

