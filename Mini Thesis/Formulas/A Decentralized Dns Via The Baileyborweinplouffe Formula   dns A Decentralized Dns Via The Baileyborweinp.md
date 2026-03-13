# π‑DNS: A Decentralized DNS via the Bailey–Borwein–Plouffe Formula

This document describes a complete, self‑contained protocol for mapping hierarchical domain names onto π’s infinite hexadecimal address space. It combines label hashing, BBP digit extraction, decimal chunk folding, and π‑search to form a stateless, server‑less DNS.

---

## 1. Label Hashing

Each label in a domain (e.g., `"www"`, `"example"`, `"com"`) is converted into an 8‑digit decimal integer. One option is a simple modular hash:

$$
H(	ext{label}) = \Bigl(\sum_{i=0}^{n-1} \text{ord}(	ext{label}[i]) \times 256^i \Bigr) \bmod 10^8
$$

Alternatively, use FNV‑1a for better collision resistance:

```python
# FNV-1a 32-bit then mod 1e8
def fnv1a_8(label):
    h = 0x811c9dc5
    for c in label:
        h ^= ord(c)
        h *= 0x01000193
        h &= 0xffffffff
    return h % 10**8
```

---

## 2. BBP Hex‑Digit Extraction

To randomly access hex digits of π at position \$n\$ (1‑indexed), use the Bailey–Borwein–Plouffe formula:

$$
d_n = \left\lfloor 16 \{\,4S(1,n) - 2S(4,n) - S(5,n) - S(6,n)\} \right\rfloor,
$$

where the fractional series is

$$
S(j,n) = \sum_{k=0}^n \frac{16^{n-k} \bmod (8k+j)}{8k+j}
\;+
\sum_{k=n+1}^{\infty} \frac{16^{\,n-k}}{8k+j}.
$$

**Implementation sketch**:

```python
import math

def S(j, n):
    total = sum(pow(16, n-k, 8*k + j) / (8*k + j) for k in range(n+1))
    term = 0.0
    k = n+1
    while True:
        t = 16**(n-k) / (8*k + j)
        if t < 1e-17:
            break
        term += t
        k += 1
    return (total + term) % 1

def pi_hex_digits(start, count):
    hex_str = ""
    for i in range(count):
        n = start + i - 1
        x = (4*S(1,n) - 2*S(4,n) - S(5,n) - S(6,n)) % 1
        hex_str += f"{int(x*16):X}"
    return hex_str
```

---

## 3. Decimal Conversion & Chunking

Once you have an 8‑hex‑digit seed (e.g., `"BB8198B3"`), convert it to decimal:

```python
dec = int(hex_seed, 16)
dec_str = str(dec)
```

Split into 8‑digit chunks (zero‑pad the last chunk if needed):

$$
\{a_1, a_2, \dots, a_m\},\quad a_i\in[0,10^8-1],	ext{ width=8 digits.}
$$

---

## 4. Header‑Fold Operation

For each adjacent pair \$(a,b)\$ of these chunks, compute:

$$
\Delta = |b - a|,
\quad
\Sigma = a + b.
$$

Zero‑pad \$\Delta\$ and \$\Sigma\$ to 8‑digit strings. These are your next π‑search keys.

---

## 5. π‑Search & Phase Check

For each 8‑digit string \$s\$:

1. Search the first \$N\$ digits of π for the substring `$s$`.
2. If found, record position \$P\$.
3. If not found, set \$s'=\$reverse(\$s\$) and search again (this catches phase‑inversion folds).

This yields one or two positions per chunk.

---

## 6. Recursive Lookup Cycle

Starting from label hashes \(H_k\) for a domain of \(n\) labels:

Initial: \(P_0 = 0\).

For \(k = 1\) to \(n\):

$$
S_k = \mathrm{BBP}\bigl(P_{k-1} + H_k\bigr),
$$

$$
\{\Delta_{k,i},\,\Sigma_{k,i}\}_{i=1}^m \;=\;\mathrm{headerFold}\bigl(\mathrm{dec}(S_k)\bigr),
$$

where each \(S_k\) is 8 hex digits → decimal → chunk/fold → search.

Result: \(P_n\) is your final “A-record” analogue.

In compact form:

$$
P_k = \mathrm{search}\bigl(\Delta_{k,i}\bigr)\;\cup\;\mathrm{search}\bigl(\Sigma_{k,i}\bigr),
\quad
P_n = P_n\bigl(P_{n-1}(\dots P_1(P_0 + H_1)\dots + H_n)\bigr).
$$

Where \(\Delta_{k,i}\) and \(\Sigma_{k,i}\) come from folding the decimal conversion of \(S_k\).

---

## 7. Nyquist Oversample

To capture sub‑byte resonances, for each found position \$P\$ also probe

$$
P-1,\quad P+1.
$$

This double‑sampling ensures you don’t miss near‑matches.

---

## 8. Example Workflow

For `www.example.com`:

1. `H_1 = fnv1a_8("com")` → e.g. `12345678`
2. `S_1 = pi_hex_digits(12345678,8)` → `A1B2C3D4`
3. Convert → `278866`
