
# 🔐 Nexus Harmonic Nonce Projection Engine

## 📡 Final Recursion: Now with Real Data and Bidirectional Entanglement

> This is not guesswork. This is resonance.

---

## 🌌 Core Principle

**Hashes do not age. Entanglement only works on true data.**  
We begin from the center and walk forward and backward simultaneously.  
By aligning phase-centered structures — nonce, hash, and magnitude — we enter a reflective space.

---

## ✨ Constants

Let:

- $\phi = \frac{1 + \sqrt{5}}{2}$ be the golden ratio  
- $H = 0.35$ be the harmonic constant  
- $\text{DELTA}_i = \lfloor \cos(\phi i) \cdot H \cdot (i \bmod 32 + 1) \rfloor$

---

## 🔁 Hashing System

We define the core SHA operations:

```python
def sha256(data):
    return hashlib.sha256(data).digest()

def double_sha256(data):
    return sha256(sha256(data))
```

This mimics:

$$
\text{SHA2}(x) = \text{SHA}(\text{SHA}(x))
$$

---

## 📐 Vector Harmonic Mapping

Given two hash states $h_1, h_2$, define:

$$
\Delta_i = |h_{1i} - h_{2i}| \\
r_i = (\Delta_i \bmod 32 + 1) \cdot H \\
\theta_i = i \cdot \phi \\
x_i = r_i \cdot \cos(\theta_i), \quad y_i = r_i \cdot \sin(\theta_i)
$$

This forms a 64-point vector spiral, mapped to the RSM-I plane.

---

## 🔺 Triangle Magnitude Function

Let $\vec{p}_0, \vec{p}_1$ be points on the harmonic spiral:

$$
a = \|\vec{p}_0\|, \quad b = \|\vec{p}_1\| \\
c = \sqrt{a^2 + b^2}
$$

This $c$ serves as the **harmonic deviation scalar**.

---

## 🔄 Nonce Projection Protocol

We scan both directions from a base nonce:

```python
base_nonce ± i → modified_header → SHA2 → harmonic_vector → ∆c
```

This produces a list of $(\text{nonce}, h_1, h_2, \Delta c)$

---

## 🧲 Glide Path Attractors

Using a moving window, we detect minima in harmonic deviation:

### Quadratic Interpolation for Attractor Vertex:

$$
A = \frac{c_2(n_0 - n_1) + c_1(n_2 - n_0) + c_0(n_1 - n_2)}{(n_0 - n_1)(n_0 - n_2)(n_1 - n_2)} \\
B = \frac{c_2^2(n_1 - n_0) + c_1^2(n_0 - n_2) + c_0^2(n_2 - n_1)}{(n_0 - n_1)(n_0 - n_2)(n_1 - n_2)} \\
\text{vertex} = n_1 - \frac{B}{2A}
$$

Where:

- $c_i$ is the $\Delta c$ at window index $i$
- $n_i$ is the nonce at window index $i$

This gives the attractor nonce — the harmonic center of a dip.

---

## 💬 Reflection

> SHA is not a lock to be picked — it's a resonance to be tuned.  
> Respect the harmonic field, center yourself, and SHA will reflect the truth, not resist it.

---

## 📜 Summary

The system now treats SHA not as a brute target, but as a **harmonic partner**.  
Nonce becomes the tuner.  
The hash is the carrier wave.  
The correct zeros are the data — not guessed, but aligned.

---

## 🗂 Output Fields

- Nonce
- SHA256 (partial)
- SHA256² (partial)
- ∆c Magnitude
- Projected Attractors

