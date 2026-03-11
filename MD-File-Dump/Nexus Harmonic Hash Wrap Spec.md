# Harmonic Wrapping of Hash Streams (π–e–φ Triad)

This is a **working build spec** (Δ‑phase), not a claim of established physics or cryptanalysis.

**Objective:** Treat a SHA‑256 digest as a **method‑coordinate** (like “π digits by algorithm”), then apply **harmonic wraps** that reveal a **residual port** (z‑stream) suitable for typeless compression / SILR unfolding.

---

## Δ1 — Hash as method

A SHA‑256 digest is a deterministic function of its input:

$$
H(x) = \mathrm{SHA256}(x) \in \{0,1\}^{256}.
$$

A “hash as method” stance treats the 256‑bit output not as a terminal label, but as a **coordinate** that can seed repeatable structure generators:

- **Iterated orbit:**
  $$
  h_0 = H(x),\qquad h_{t+1} = H(h_t).
  $$
  This yields a deterministic pseudo‑random stream (a method).

- **π‑lattice pointer (BBP):** use the hash as an index/pointer into a BBP digit extractor for \(\pi\), making “random access” digits a deterministic function of \(h_0\).

Neither of these assumes invertibility of SHA. They just treat SHA output as a **seeded coordinate**.

---

## ⊕2 — Harmonic wraps as invertible carriers (mod \(2^{256}\))

Define an odd 256‑bit multiplier from an irrational constant \(c\in\{\pi,e,\varphi\}\):

$$
K_c = \Big\lfloor 2^{256} \cdot \{c\} \Big\rfloor\ \mathrm{OR}\ 1,
$$

where \(\{c\}=c-\lfloor c\rfloor\) is the fractional part, and OR‑1 forces oddness.

Then define the wrapped states:

$$
W_c(h) = (K_c\cdot h) \bmod 2^{256}.
$$

**Key property:** since \(K_c\) is odd, multiplication by \(K_c\) is invertible modulo \(2^{256}\). So these wraps are **lossless carriers** (relabelings) rather than compressions.

A triad braid (a deliberate “three‑frequency carrier”) can be defined as a projection:

$$
B(h)=W_\pi(h)\oplus \mathrm{ROTL}(W_e(h),1)\oplus \mathrm{ROTL}(W_\varphi(h),2).
$$

This braid is not invertible by itself (it’s a fold), but it is a useful **spectral probe**.

**Optional combined constant (“E hash Φ”):**

$$
K_{e\varphi}=\Big\lfloor 2^{256}\cdot \{e\varphi\}\Big\rfloor\ \mathrm{OR}\ 1,
\qquad W_{e\varphi}(h)=(K_{e\varphi}h)\bmod 2^{256}.
$$

---

## ↻3 — The 64/65 beat residual port

For any byte \(b\in\{0,\dots,255\}\), define two near‑quantizers:

$$
a=b\bmod 64,\qquad r=b\bmod 65.
$$

Define a **beat residual**:

$$
\delta = (a-r)\bmod 65.
$$

Empirically for bytes \(0\dots 255\), the folded distance

$$
\beta = \min(\delta,\ 65-\delta)
$$

stays tiny (often \(0..3\)). This is a concrete “near‑lattice” phenomenon: two almost‑identical moduli create a low‑range beat.

**Exact reconstruction (CRT‑style):** given \(a=b\bmod 64\) and \(r=b\bmod 65\), recover \(b\) uniquely in \(0..255\) via

$$
 b = a + 64\cdot\big((a-r)\bmod 65\big).
$$

Because \(64\equiv -1\pmod{65}\), the term \(((a-r)\bmod 65)\) is the “correction count” that lands you on the correct residue class.

**Interpretation:** the pair of channels (mod64, mod65) acts like a differential measurement; the residual \(\delta\) is the **port**. It’s where z‑streams live.

---

## Ψ4 — Circle wrap (the “\(2\pi r\)” mapping)

Convert a byte stream to points on the complex plane:

- radius \(\rho_k = b_k/255\)
- angle \(\theta_k = 2\pi\cdot\mathrm{frac}(\rho_k\cdot c)\) for \(c\in\{\pi,e,\varphi\}\)

$$
 z_k = \rho_k\,e^{i\theta_k}.
$$

This turns “byte soup” into a deterministic oscillator trace. The invariants you look for are **not ASCII labels**, but **geometry**:

- step lengths \(|z_{k+1}-z_k|\)
- turning angles \(\arg(z_{k+1}/z_k)\)
- recurrence / beat frequencies between different \(c\) carriers

The z‑stream is built from deviations of these observables relative to a null model.

---

## ⊥5 — When does this collapse to silence?

Define an error observable \(x_k\) (e.g., \(\beta_k\) from mod64/mod65, or a spectral amplitude). Define a sliding baseline \(\mu\) and scale \(\sigma\). The control readout:

$$
 z_k = \frac{x_k-\mu_k}{\sigma_k}.
$$

A strict “no remainder” halt condition is:

$$
\forall k:\ z_k\to 0\quad\text{and}\quad \Delta H\to 0
$$

(no correction pulses, no drift). Then the correct output is ⊥.

---

## Worked micro‑example: SHA256("hello")

Digest:

```
2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```

Using \(h=\mathrm{int}(\mathrm{digest})\) and the wraps \(W_\pi, W_e, W_\varphi\), the first 12 folded beat distances \(\beta\) (from the mod64/mod65 port) were:

- raw \(h\): `[0, 3, 1, 2, 1, 2, 2, 0, 0, 3, 0, 0]`
- \(W_\pi(h)\): `[0, 0, 0, 1, 2, 2, 2, 0, 2, 3, 2, 0]`
- \(W_e(h)\): `[3, 0, 1, 2, 2, 0, 2, 3, 1, 0, 1, 0]`
- \(W_\varphi(h)\): `[1, 2, 3, 3, 0, 2, 0, 1, 2, 2, 0, 1]`
- braid \(B(h)\): `[2, 2, 0, 1, 0, 3, 0, 2, 3, 2, 2, 0]`

All stayed within \(0..3\) on this sample.

**Nexus read:** the carrier (wrap) changes the surface stream, while the beat residual port stays low‑range. That is exactly the kind of “typeless handle” you can z‑score and feed into SILR.

---

## Next executable branch (no metaphors)

1. Generate many message hashes \(h_i\) (include structured families: `hello`, `hello0..hello999`, etc.).
2. For each, compute \(\beta\)-streams on:
   - raw \(h\)
   - \(W_\pi(h),W_e(h),W_\varphi(h)\)
   - braid \(B(h)\)
3. Build z‑streams of \(\beta\) under a null model (byte‑shuffle baseline) and test for:
   - stable banding \((0.30\le H\le 0.40,\ \Delta H\le 0.05)\) if using your Samson/SILR metrics
   - non‑random recurrence in circle‑wrap geometry (FFT of \(|z_{k+1}-z_k|\) sequences)
4. If a candidate port stays stable across wraps (invariant), treat it as **method‑true**. Everything else is Ω‑wobble.

