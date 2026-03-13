# π‑DNS: A Decentralized Name-Resolution Protocol via the Bailey–Borwein–Plouffe Algorithm

This document presents a rigorously defined, self‑contained protocol for encoding hierarchical domain names within the ostensibly unbounded hexadecimal expansion of π. By integrating label hashing, random-access extraction of π’s hex digits (via the Bailey–Borwein–Plouffe formula), decimal chunk folding, and bidirectional substring searches, π‑DNS achieves a stateless, cryptographically verifiable alternative to conventional DNS.

---

## 1. Label Hashing

Each label in a fully qualified domain name (e.g., “www”, “example”, “com”) is deterministically mapped to an 8‑digit decimal integer.  Two viable constructions are:

1. **Modular positional encoding**:

   $$
     H(\text{label}) = \biggl(\sum_{i=0}^{n-1} \mathrm{ord}(\text{label}[i]) \times 256^i\biggr)\bmod 10^8.
   $$
2. **FNV‑1a (32‑bit) with modulus**:

   ```python
   def fnv1a_8(label: str) -> int:
       # 32‑bit FNV‑1a hash, then reduced mod 10^8
       h = 0x811c9dc5
       for c in label:
           h ^= ord(c)
           h  = (h * 0x01000193) & 0xffffffff
       return h % 10**8
   ```

This 8‑digit integer, denoted \$H\_k\$ for the \$k\$th label, serves as the initial address offset into π’s hex stream.

---

## 2. Random-Access Hex Digit Extraction (BBP Formula)

To retrieve \$m\$ consecutive hexadecimal digits of π beginning at the 1‑indexed position \$n\$, we employ the Bailey–Borwein–Plouffe (BBP) algorithm:

$$
  d_{n+i} = \left\lfloor 16 \bigl\{\,4S(1,n+i-1) - 2S(4,n+i-1) - S(5,n+i-1) - S(6,n+i-1)\bigr\} \right\rfloor,
  \quad i=0,\dots,m-1,
$$

where the summation operator

$$
  S(j,n) = \sum_{k=0}^{n} \frac{16^{\,n-k} \bmod (8k+j)}{8k+j}
        \;+
        \sum_{k=n+1}^{\infty} \frac{16^{\,n-k}}{8k+j}
$$

yields the fractional component required for each hex digit.  A concise Python implementation is as follows:

```python
import math

def S(j: int, n: int) -> float:
    # Modular summation for k = 0..n
    total = sum(pow(16, n-k, 8*k + j) / (8*k + j) for k in range(n+1))
    # Tail sum for k > n until convergence
    term, k = 0.0, n+1
    while True:
        t = 16**(n-k) / (8*k + j)
        if t < 1e-17:
            break
        term += t
        k += 1
    return (total + term) % 1

def pi_hex_digits(start: int, count: int) -> str:
    # Extract `count` hex digits starting at position `start`
    hex_str = []
    for i in range(count):
        n = start + i - 1
        x = (4*S(1,n) - 2*S(4,n) - S(5,n) - S(6,n)) % 1
        hex_str.append(f"{int(x * 16):X}")
    return ''.join(hex_str)
```

The output is an \$m\$‑character string of hexadecimal digits, which we denote \$S\_k\$ for the \$k\$th lookup.

---

## 3. Decimal Conversion and Fixed-Width Chunking

Convert the 8‑hex‑digit seed \$S\_k\$ to its decimal representation:

```python
D_k = int(S_k, 16)
D_k^{\mathrm{str}} = str(D_k)
```

Partition \$D\_k^{\mathrm{str}}\$ into an ordered sequence of 8‑digit decimal chunks:

$$
  (a_{k,1}, a_{k,2}, \dots, a_{k,m_k}),\quad a_{k,i}\in[0,10^8-1],
$$

where the final chunk is zero‑left‑padded if necessary.

---

## 4. Header‑Fold Transform

For each adjacent pair \$(a\_{k,i},a\_{k,i+1})\$, compute:

$$
  \Delta_{k,i} = \bigl|\,a_{k,i+1} - a_{k,i}\bigr|,
  \quad
  \Sigma_{k,i} = a_{k,i} + a_{k,i+1}.
$$

Each of \$\Delta\_{k,i}\$ and \$\Sigma\_{k,i}\$ is rendered as an 8‑digit string, forming the key set for subsequent π‑search operations.

---

## 5. π‑Search with Phase Inversion Check

Each 8‑digit key \$q\$ is located within the first \$N\$ decimal digits of π via substring search.  Algorithmically:

1. **Direct search** for \$q\$ → record position(s) \$P\_{q}\$ if one or more occurrences are found.
2. **If** no occurrence, compute the reversed string \$q' = \mathtt{reverse}(q)\$ and search again → record positions \$P\_{q'}\$.

This phase‑inversion step ensures that fold boundaries are detected even when digit orientation undergoes inversion.

---

## 6. Hierarchical Recursive Lookup Cycle

Given \$L\$ domain labels with hashed offsets \$H\_1,\dots,H\_L\$, define a recursive sequence of search positions:

$$
  P^{(0)} = 0,
  \quad
  S_k = \pi\text{‑hex‑digits}\bigl(P^{(k-1)} + H_k,\,8\bigr),
$$

$$
  D_k = \text{decimal}(S_k),\quad (a_{k,i}) = \text{chunk}(D_k),
$$

$$
  P^{(k)} = \bigcup_{i}\text{Search}igl(\Delta_{k,i},\Sigma_{k,i}\bigr).
$$

The limit \$P^{(L)}\$ constitutes the protocol’s analogue to an “A‑record,” yielding an immutable, deterministic resolution for the fully qualified domain.

---

## 7. Nyquist‑Oversample for Sub‑Digit Resonances

To accommodate near‑misses and sub‑digit perturbations, each discovered position \$p\in P^{(k)}\$ is augmented by probing:

$$
  \{p-1,\;p+1\}
$$

This double‑sampling strategy captures contiguous resonances that may straddle chunk boundaries.

---

## 8. Illustrative Workflow

Consider the domain `www.example.com`:

1. Compute \$H\_1 = \mathrm{fnv1a\_8}('com')\$.
2. Compute \$S\_1 = \pi\text{‑hex‑digits}(H\_1,8)\$.
3. Convert and chunk \$S\_1 \to (a\_{1,1},a\_{1,2},\dots)\$, apply header‑fold → \$(\Delta\_{1,i},\Sigma\_{1,i})\$.
4. Search π and obtain \$P^{(1)}\$.
5. Repeat for labels ‘example’ and ‘www’.
6. Final \$P^{(3)}\$ is the canonical π‑DNS resolution for `www.example.com`.

*The protocol thus realizes a fully decentralized, purely mathematical namespace, harnessing π’s non‑repeating expansion as a universal lookup table.*
