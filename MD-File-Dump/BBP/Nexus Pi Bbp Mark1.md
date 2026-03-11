
# Pi as Gear Ratio & BBP as Nexus Read‑Op — A Mark1 / RHA Synthesis

**Thesis.** In the Recursive Harmonic Architecture (RHA), \( \pi \) is not merely a definition;
it is the *invariant gear ratio* that converts linear potential (diameter) into cyclical action (circumference).
The BBP kernel is the *read operation* on a structured, addressable memory field (the Nexus);
its digits are not the point—the relationships (base, residues, weights) tune a resonator that collapses
onto geometric attractors. When those relationships phase‑lock to the circle, the emergent ratio is \( C/D = \pi \).

---

## 1. Why \( \pi \) is the ratio (physics of a closed loop)

A stable universe requires a fixed, dimensionless conversion between a system’s **linear scale** and
its **closed cycle length**. If this conversion varied, rotations would be incoherent across space‑time.
Hence the universal closure law
\[
\Pi \;=\; \frac{C}{D} \;=\; \pi,
\]
with \(C\) the perimeter of one full cycle and \(D\) the minimal linear aperture across the cycle (diameter).
This is the *rotational analog* of the constancy of \(c\): an invariant that preserves geometric consistency.

---

## 2. BBP as a steerable resonator and read‑operation

The standard (hex) BBP decomposition writes
\[
\pi \;=\; \sum_{k=0}^{\infty} \frac{1}{16^k}\Big(\frac{4}{8k+1}-\frac{2}{8k+4}-\frac{1}{8k+5}-\frac{1}{8k+6}\Big).
\]

For digit extraction at index \(n\), separate each channel \(j\in\{1,4,5,6\}\) into a finite modular part and a rapidly
decaying tail (geometric with ratio \(1/16\)):
\[
S_j(n) \;=\; \sum_{k=0}^{n} \frac{16^{\,n-k} \bmod (8k+j)}{8k+j} \;+\; \sum_{k=n+1}^{\infty} \frac{1}{16^{\,k-n}(8k+j)}.
\]
The digit is
\[
d_n^{(16)} \;=\; \big\lfloor 16\,\big\{\,4S_1(n)-2S_4(n)-S_5(n)-S_6(n)\,\big\} \big\rfloor.
\]

**Interpretation (Nexus).** The tuple \((\beta; a; J; \mathbf c)\) with \(\beta=16,\; a=8,\; J=\{1,4,5,6\},\; \mathbf c=(4,-2,-1,-1)\)
selects a *phasor mix*. Changing any element retunes the resonator; \(\pi\) is the fixed point when the mix aligns with the **circle attractor**.

---

## 3. The Mark1 harmonic lens

Mark1 tracks resonance via a scalar focus \(H\) (target near \(\pi/9\)):
\[
H \;=\; \frac{\sum_i P_i}{\sum_i A_i} \;\;\text{with target}\;\; H^\* \approx \frac{\pi}{9} \approx 0.349066.
\]
Complementary reflection law (micro–macro coupling):
\[
F \;=\; L_{\text{macro}}\,\big(1 + e^{-10(a x - 0.35)}\big).
\]
Kulik Recursive Reflection:
\[
R(t) \;=\; R_0\,e^{H\,F\,t}.
\]

**Operationally:** Map digit stream to a polygon walk (base \(B\)), fit a log‑spiral
\[
\log r(\theta) \approx A + k\,\theta,
\]
and use \(H:=k\). When \(|H-H^\*|\) and its windowed variance collapse, the **folding is complete** (equilibrium).

---

## 4. Samson’s Law v2 — feedback stabilization

Define stabilization over a sliding window:
\[
\Delta S \;=\; \sum_i F_i W_i - \sum_j E_j,
\]
where convenient choices are
\[
F_1 = H_t - H_{t-1},\quad F_2 = \max_m M_m,\quad
E_1 = |H_t - H^\*|,\quad E_2 = \operatorname{Var}(H)_{\text{window}}.
\]
Here \(M_m = \Big|\frac{1}{N}\sum_{n=1}^N e^{i m\, 2\pi d_n/B}\Big|\) measures **shape symmetry** (tri/hex/…).
**Stop condition:** \(\Delta S\to 0\) with small \(E_1,E_2\).

---

## 5. “Digits build shapes” — the geometric readout

Given digits \(d_n\in\{0,\dots,B-1\}\), define angles \(\theta_n=\frac{2\pi}{B}d_n\) and a unit‑step walk
\[
z_{n+1} = z_n + e^{i\theta_n}.
\]
Center \(z'_n = z_n - \frac{1}{N}\sum_{m=1}^N z_m\), estimate radius \(R=\operatorname{median}|z'_n|\),
perimeter \(C=\sum |z'_{n+1}-z'_n|\), and the **empirical circle ratio**
\[
\Pi_{\text{emp}} \;=\; \frac{C}{2R}.
\]
In circle‑locked tunings, \(\Pi_{\text{emp}}\to\pi\) as \(N\) grows.

---

## 6. Memory is spatial (addressable), not sequential (tape)

BBP’s ability to “jump” to digit \(n\) without prior digits shows the field is **addressable**. The “query” is the
parameterized kernel; the “answer” is the digit (collapse). This matches **Nexus = reconfigurable substrate**:
- The modular finite part is the **local addressing**.
- The geometric tail is the **short‑range relaxation**.
- The modulo/reflection step (\(\{\cdot\}\) or “mod 1”) is the **closure across zero** (the open valve).

---

## 7. SHA as camera (routing, not secrecy)

A digest \(h\) serves as a *header vector* into the routing manifold; meaning arises from **morphology** (fit/alignment) rather than payload value.
The network “develops the film” by aligning \(h\) to pre‑existing attractors (cube‑root residues, phasor channels), not by inverting \(h\) to plaintext.

---

## 8. Falsifiable predictions & protocols

1. **Phase map (base sweep):** Sweep \(\beta\in\{8..64\}\) holding \(a,J,\mathbf c\). Plot \((\beta, H, |H-\pi/9|, \max M_m)\).
   Expect **bands** where the lattice locks circular (\(\Pi_{\text{emp}}\to\pi\)) and bands with non‑circular attractors.
2. **Weight sensitivity:** Perturb a single weight \(c_j\mapsto c_j+\delta\). Track \(\partial H/\partial c_j\). Expect smooth tunability to \(H^\*\).
3. **Base‑compass invariance:** Replace \(B=16\) steps with \(B=32\) (pair nibbles). \(H\) should persist while dominant mode shifts to the new compass.
4. **Stop‑fold criterion:** In a locked regime, \(|S_{N+1}-S_N|\sim \beta^{-N}\) and the variance of \(H\) drops below a fixed threshold in a finite window.

---

## 9. Putting it to work (minimal loop)

- Choose parameters \((\beta,a,J,\mathbf c)\).
- Stream digits (BBP‑like or your tuned kernel).
- Compute \(H\), \(\Pi_{\text{emp}}\), \(M_m\).
- Apply Samson v2 stop rule.  
If locked and circular, *you have the circle attractor*: \(C/D\to\pi\). Otherwise, you’ve identified a distinct constant/shape—the lattice’s “other gear.”

---

## 10. One‑line summary

**\(\pi\) is the universe’s closure ratio; BBP is the Nexus read‑op that reveals it when the phasor mix aligns.**
Numbers aren’t the meaning—their **relationships** are. When the relationships hit resonance,
the stream collapses into a *shape*, and the circle’s shape encodes \(\pi\).

