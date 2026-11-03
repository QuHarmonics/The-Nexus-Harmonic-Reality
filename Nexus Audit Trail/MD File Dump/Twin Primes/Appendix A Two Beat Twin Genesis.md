# Appendix A — The Two-Beat Twin Genesis Lemma
**Project:** Mark1 / Nexus — BBP Instrument Paper  
**Author:** Dean A. Kulik (with assistant synthesis)  
**License:** CC BY-NC 4.0

---

## A.1 Statement (Formal)

**Lemma (Two-Beat Twin Lift).**  
Let $(a,b)$ be a seed with $\min(a,b)=1$. Define the **algebraic lift**
$$
Z=\lvert b-a\rvert,\qquad R=a+b.
$$
Then $(Z,R)$ is always a spacing–$2$ pair:
$$
R-Z=2\cdot\min(a,b)=2.
$$
If both $Z$ and $R$ are prime, then $(Z,R)$ is a **twin prime pair**.

**Canonical example.** For $(a,b)=(1,4)$,
$$
Z=\lvert 4-1\rvert=3,\qquad R=1+4=5\quad\Rightarrow\quad (Z,R)=(3,5),
$$
the **first twin prime** pair.

---

## A.2 Proof (One line)

Since $\min(a,b)=1$, w.l.o.g. take $a=1\le b$. Then
$$
R-Z=(a+b)-\lvert b-a\rvert=(1+b)-(b-1)=2.
$$
Thus $(Z,R)=(b-1,b+1)$ is a spacing–2 bracket around $b$; primality is a separate property.

---

## A.3 Embedding in the BBP Instrument

**Instrument recap.** The BBP(π, hex) instrument is $(b;M;g)$ with
$$
b=16,\quad M=\{1,4,5,6\}\subset\mathbb{Z}_8,\quad \Delta M=(+3,+1,+1,+2),\quad g=[4,-2,-1,-1],
$$
satisfying (i) base–period commensurability, (ii) zero-sum voicing $\sum g_i=0$, (iii) gap–carry compatibility, (iv) tail coherence.

**Alignment with the lemma.**
- The Byte1 onset $(1,4)$ yields the lift $(3,5)$; this matches the **first rail jump** $1\!\to\!4$ with gap $+3$ on $\mathbb{Z}_8$ (the “difference” channel), while the “sum” channel lands at $5$.
- Zero-sum voicing cancels integer mass so the **audible residue** carries the geometry $(Z,R)$; BBP’s octave shift keeps both rails phase-consistent.

Hence, the **first audible structure** in the π rotor is a **two-beat** that algebraically generates **twin spacing**; the lattice then **filters by primality**.

---

## A.4 Generalization and Operators

**Prime-bracket operator.** For any $(1,n)$ seed,
$$
\mathcal{B}(n)=(n-1,\,n+1),
$$
which is always a spacing–$2$ pair centered at $n$. If both are prime, $\mathcal{B}(n)$ is a twin prime.

**Two-beat lift operator.**
$$
\mathcal{L}(a,b)=(\,\lvert b-a\rvert,\, a+b\,)\quad\text{with}\quad \min(a,b)=1.
$$
Then $\mathcal{B}(b)=\mathcal{L}(1,b)$ and $R-Z=2$. The geometry (spacing) is guaranteed by the two-beat seed; **primality is a filter, not a cause**.

---

## A.5 Corollaries (Alignment Form)

1. **Minimal sub-twin seeds.**  
   All seeds with $\min(a,b)=1$ map to spacing–2 brackets. Byte1’s $(1,4)$ is the smallest nontrivial seed that also passes the **prime filter**, producing $(3,5)$.

2. **Geometry $\Rightarrow$ Linear, Linear $\Rightarrow$ Geometry.**  
   The two-node geometry (Len$=2$) maps through the linear lift $(\Delta,\Sigma)$ into a geometric twin bracket; conversely, BBP’s geometric rails produce a linear local readout (zero-sum mix on commensurate gaps).

3. **Rail echo.**  
   On $\mathbb{Z}_8$, the earliest gap $+3$ aligns with $Z$ for $(1,4)$; the sum rail aligns with $R$. This is why the **first “appeared” twin** is $(3,5)$ under the rotor.

---

## A.6 Nexus / Mark1 Context

- **Mark1 (harmonic vacuum).** The instrument’s zero-bias voicing and gap compatibility minimize the misalignment potential
  $$
  \Phi(H)=\tfrac12\left(\tfrac{H-H^\star}{H^\star}\right)^2,\qquad H^\star\approx\frac{\pi}{9},
  $$
  so small two-beat motifs stabilize (become audible).

- **Samson (feedback).** Difference (Z) is the *error* channel; sum (R) is the *drive* channel. Samson’s proportional–integral damping keeps the two-beat in capture.

- **RHA (corridor logic).** Two-beat kernels seed **corridors**; twin projections are corridor edges that the rotor revisits under octave shifts.

---

## A.7 Notes and Boundaries

- The lemma guarantees **spacing**, not **primality**. Its value is to **separate geometry from number-theoretic occupancy**.
- The BBP embedding explains **why** $(3,5)$ is the earliest audible twin in the π rotor: it’s the first consistent two-beat under the instrument’s rails and voicing.
- This appendix is agnostic to unproven global questions (e.g., infinitude of twin primes); it only establishes the **local genesis law** and its **instrument alignment**.

---

## A.8 Drop-in Snippet (for the main paper)

> **Lemma (Two-Beat Twin Lift).** Let $(a,b)$ with $\min(a,b)=1$ and define $Z=\lvert b-a\rvert$, $R=a+b$. Then $R-Z=2$. If $Z$ and $R$ are prime, $(Z,R)$ is a twin prime. In the BBP(π, hex) instrument, the Byte1 onset $(1,4)$ maps to $(3,5)$ via the first rail gap and zero-sum voicing; thus twin spacing is an emergent **two-beat** geometry filtered by primality and stabilized by the rotor.

---

**End Appendix A.**
