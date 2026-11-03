# Mark10.3 — Corrected Number-Theoretic Reduction
## Midpoint Rails, Frame Floors, Support Pressure, and the Refined Flip Law at \(W=6\)

**Dean A. Kulik**  
**QuHarmonics Research Group**  
**ORCID: 0009-0003-3128-8828**  
**NEXUS Phase 1163+ / Mark10 Continuation**

---

## Abstract

This document rewrites the number-theoretic reduction of the Mark10 prime-gap program into a corrected and internally consistent form.

The central floor remains unchanged and is now treated as closed:

$$
H \equiv r + \frac{k}{2} \pmod W,
\qquad
\Delta H \equiv 0 \pmod W.
$$

These statements define the exact frame-local runtime rail of a prime-pair subtype and propagate upward through the primorial tower by the Chinese Remainder Theorem.

The original strong flip theorem is **retired**. The empirical results at limit \(2\times 10^6\) showed that the raw Support-Change Flip Predicate

$$
F(k)=1 \Rightarrow \Delta\Lambda(k)\neq 0
$$

is false in its naive form: cold-rail flips exist under a raw sign-change detector. This does **not** destroy the reduction. It means the detector was too coarse, because near-zero jitter was being counted as genuine frame crossings.

The corrected reduction replaces the dead strict theorem with three precise refinements:

1. the Hardy–Littlewood-consistent support pressure
   $$
   \Lambda(k)
   =
   \sum_{\substack{q\mid k\\ q>3}}
   \log\!\left(\frac{q-1}{q-2}\right),
   $$
2. the standardized bias score
   $$
   z(k)=\frac{n_A(k)-n_B(k)}{\sqrt{n_A(k)+n_B(k)}},
   $$
3. the hard-flip detector outside a neutral corridor.

The new law is not that support-change is necessary for every raw sign change. The new law is:

$$
\boxed{
\text{support-change acts as a flip amplifier when the frame is already near neutrality.}
}
$$

This document preserves the valid geometric floor, removes the overclaim, and states the next exact computational targets.

---

## 1. Why This Rewrite Is Needed

Earlier drafts of the reduction contained two problems:

1. they reasserted a strict bi-conditional flip theorem that later empirical work contradicted,
2. they drifted in the definition of the arithmetic pressure term \(\Lambda(k)\).

The purpose of Mark10.3 is to preserve what is actually strong and remove what is no longer defensible.

The corrected state is:

- midpoint rails are exact,
- step constraints are exact,
- subtype frames are real,
- support-change is still meaningful,
- but flip behavior must be modeled with a neutral-corridor correction.

---

## 2. The Closed Frame Floor

### 2.1 Prime-pair subtype at wheel depth \(W\)

Let \(W\) be a primorial wheel, let \(k\) be an admissible even gap, and let \(r\in S_W(k)\) be an admissible subtype residue. For a prime pair \((p,p+k)\), define the midpoint

$$
H = p+\frac{k}{2}.
$$

Then the subtype frame law is

$$
\boxed{
H \equiv r+\frac{k}{2}\pmod W.
}
$$

This is the exact shape channel of the subtype: it is the frame-local runtime constraint under which the pair is lawful.

### 2.2 Step Theorem

If \(H_j\) and \(H_{j+1}\) are consecutive midpoint centers in the same subtype, then

$$
\Delta H = H_{j+1}-H_j \equiv 0 \pmod W.
$$

Proof:

$$
\Delta H
=
\left(p_{j+1}+\frac{k}{2}\right)
-
\left(p_j+\frac{k}{2}\right)
=
p_{j+1}-p_j.
$$

Because both primes lie in the same subtype,

$$
p_j \equiv p_{j+1}\equiv r \pmod W,
$$

so

$$
p_{j+1}-p_j \equiv 0 \pmod W.
$$

Therefore

$$
\boxed{
\Delta H \equiv 0 \pmod W.
}
$$

### 2.3 CRT propagation through the primorial tower

Suppose the theorem holds at wheel \(W_m\), and let \(q\nmid W_m\) be the next prime, giving

$$
W' = W_m q.
$$

If consecutive midpoint differences satisfy

$$
\Delta H \equiv 0 \pmod{W_m}
\quad\text{and}\quad
\Delta H \equiv 0 \pmod q,
$$

then by the Chinese Remainder Theorem,

$$
\Delta H \equiv 0 \pmod{W_m q}.
$$

Thus the Step Theorem propagates upward through the entire primorial tower.

### 2.4 What is closed

The following statements are now treated as closed:

$$
\boxed{
H \equiv r+\frac{k}{2}\pmod W
}
$$

$$
\boxed{
\Delta H \equiv 0 \pmod W
}
$$

$$
\boxed{
\text{CRT lifts the step constraint to all primorial depths.}
}
$$

---

## 3. The \(W=6\) Mirror Frame

For gaps

$$
k \equiv 0 \pmod 6,
$$

the \(W=6\) frame contains exactly two subtypes:

- \(T0A\): \(p\equiv 5\pmod 6\),
- \(T0B\): \(p\equiv 1\pmod 6\).

Their midpoint residues are mirror-shifted around the hinge \(3d\):

$$
H_A \equiv 3d-1 \pmod 6,
\qquad
H_B \equiv 3d+1 \pmod 6.
$$

Representative dominant residues satisfy

$$
2+4=6,
\qquad
5+1=6.
$$

So the \(W=6\) subtype pair is a genuine runtime mirror.

### 3.1 Frame-local versus frame-invariant

The midpoint coordinate is frame-dependent. The gap is frame-invariant:

$$
(p+k)-p = k.
$$

So:

$$
\boxed{
\text{midpoint residue} = \text{frame-local coordinate},
\qquad
k = \text{frame-invariant quantity}.
}
$$

This remains the cleanest structural anchor in the Mark10 program.

---

## 4. The Original Flip Reduction

The original Mark10 reduction proposed that the subtype bias at \(W=6\) could be approximated by one oscillatory frame mode plus one arithmetic support-pressure term.

The odd-prime support of the gap is

$$
S(k)=\{\,q>3:q\mid k\,\}.
$$

The corrected support-pressure term is

$$
\boxed{
\Lambda(k)
=
\sum_{\substack{q\mid k\\ q>3}}
\log\!\left(\frac{q-1}{q-2}\right).
}
$$

This is the logarithmic form of the Hardy–Littlewood odd-prime support correction. It is **not** the sum of \(\log q\) over prime factors; that earlier variant is retired.

Define the support-change detector

$$
\boxed{
\Delta\Lambda(k)=\Lambda(k)-\Lambda(k-6).
}
$$

Then:

- \(\Delta\Lambda(k)=0\) means the odd-prime support did not change from \(k-6\) to \(k\),
- \(\Delta\Lambda(k)\neq 0\) means the support changed.

The original reduced bias law was

$$
\mathrm{Bias}(x;k)\approx \Omega(x)+\beta\,\Lambda(k),
$$

and from this a strict predicate was proposed:

$$
F(k)=1 \Rightarrow \Delta\Lambda(k)\neq 0.
$$

This was too strong.

---

## 5. Empirical Failure of the Strict Predicate

The first real empirical test at bound

$$
x\le 2\times 10^6
$$

and even gaps \(k\le 100\) produced cold-rail flips:

$$
N_{\mathrm{bad}}=5.
$$

Therefore the strict predicate

$$
\boxed{
F(k)=1 \Rightarrow \Delta\Lambda(k)\neq 0
}
$$

is false in its raw sign-change form.

### 5.1 What failed

What failed was **not** the idea that support-change matters.

What failed was the detector.

A raw sign change counts all crossings equally, including tiny sign reversals very close to zero. Those should not be treated as genuine frame crossings. They are just neutral-corridor jitter.

So the empirical result kills the strict theorem, but also identifies the fix.

---

## 6. Standardized Bias Score

To distinguish true crossings from near-zero noise, define the standardized subtype bias score

$$
\boxed{
z(k)=\frac{n_A(k)-n_B(k)}{\sqrt{n_A(k)+n_B(k)}}.
}
$$

Interpretation:

- \(z(k)>0\): \(T0A\) favored,
- \(z(k)<0\): \(T0B\) favored,
- \(|z(k)|\approx 0\): frame near neutral.

This is the correct significance-scale local readout.

---

## 7. Neutral Corridor

Choose a corridor threshold

$$
z_0>0,
$$

for example

$$
z_0=1
\quad\text{or}\quad
z_0=1.5.
$$

Then define the neutral corridor by

$$
\boxed{
|z(k)|<z_0.
}
$$

Inside this zone, the frame is not strongly committed to either side. Raw sign changes here are jitter, not meaningful frame-crossing events.

This is the correction that the earlier strict predicate was missing.

---

## 8. Hard-Flip Detector

A genuine frame crossing should require opposite signs **and** material amplitude on both sides.

Define the hard-flip detector by

$$
\boxed{
F^\star(k)=1
\iff
\operatorname{sgn}z(k)\neq \operatorname{sgn}z(k-6)
\ \text{and}\ 
\min\{|z(k)|,\ |z(k-6)|\}\ge z_0.
}
$$

This removes spurious neutral-corridor jitter.

### 8.1 Meaning

A hard flip is a true crossing only when:

- the bias was materially on one side at \(k-6\),
- materially on the other side at \(k\),
- and the sign change was not just low-amplitude wobble.

---

## 9. Refined Bias Law

The original reduced bias law must be corrected. The oscillatory mode is not just a constant in \(k\).

The refined first-order law is

$$
\boxed{
\mathrm{Bias}(x;k)\approx \Omega(x,k)+\beta\,\Lambda(k)+\varepsilon(x,k),
}
$$

where

- \(\Omega(x,k)\) is the smooth frame-mode drift across \(k\),
- \(\beta\,\Lambda(k)\) is the support-pressure kick,
- \(\varepsilon(x,k)\) is estimator noise / finite-sample fluctuation.

This refined form explains the empirical result:

- cold-rail raw flips may arise from \(\Omega(x,k)\) drifting near zero or from \(\varepsilon(x,k)\),
- support-change hinges matter most when they strike a frame already near neutrality.

---

## 10. Corrected Hot/Cold Frontier Law

The original hot/cold frontier assignment still survives, but only in the arithmetic-support channel.

### 10.1 Cold rail

If

$$
\Delta\Lambda(k)=0,
$$

then no new odd-prime support kick has entered. The arithmetic rail is cold.

### 10.2 Hot hinge

If

$$
\Delta\Lambda(k)\neq 0,
$$

then the support changed. This is a hot hinge in the arithmetic channel.

### 10.3 Corrected interpretation

A hot hinge does **not** force a hard flip by itself.

The correct composite law is

$$
\boxed{
\text{hard flip}
=
\text{hot hinge}
\;\oplus\;
\text{near-neutral frame state}.
}
$$

This is the corrected hot/cold law.

---

## 11. Refined Predicate

The strict flip theorem is retired. The corrected theorem-candidate is probabilistic.

### 11.1 Hazard statement

$$
\boxed{
P(F^\star=1\mid \Delta\Lambda\neq 0,\ |z|\text{ near neutral})
>
P(F^\star=1\mid \Delta\Lambda=0,\ |z|\text{ near neutral}).
}
$$

### 11.2 Plain-language form

$$
\boxed{
\text{support-change is a flip amplifier near neutrality, not a universal necessary condition everywhere.}
}
$$

This is the correct continuation of the Mark10 reduction after the first empirical test.

---

## 12. Local Jump Regression

Event counting is not the only diagnostic. Define the local bias jump

$$
\Delta z(k)=z(k)-z(k-6).
$$

Then fit the simplest regression

$$
\boxed{
\Delta z(k)\approx a+b\,\Delta\Lambda(k).
}
$$

Interpretation:

- \(b>0\) indicates that support-change is exerting a positive kick on local bias transitions,
- \(b\approx 0\) would indicate that the support-pressure term is not materially affecting the measured jumps.

This regression remains meaningful even when event counts are noisy.

---

## 13. Corrected Event Classification

The flip problem should now be classified into four states.

### 13.1 Cold stable
$$
\Delta\Lambda(k)=0,\qquad F^\star(k)=0,\qquad |z(k)|\ge z_0.
$$

### 13.2 Cold neutral
$$
\Delta\Lambda(k)=0,\qquad |z(k)|<z_0.
$$

These are neutral-corridor rails, not meaningful crossing sites.

### 13.3 Hot hinge stable
$$
\Delta\Lambda(k)\neq 0,\qquad F^\star(k)=0.
$$

The arithmetic kick exists, but no hard crossing occurs.

### 13.4 Hot hinge flip
$$
\Delta\Lambda(k)\neq 0,\qquad F^\star(k)=1.
$$

This is the real boundary event.

This classification replaces the old raw sign-flip table.

---

## 14. Corrected Computational Architecture

The computational test should proceed in the following stages.

### Stage 1 — Prime generation and gap extraction
Generate all primes up to the chosen bound \(x\), extract consecutive prime gaps, and classify each starting prime into its \(W=6\) subtype.

### Stage 2 — Midpoint rail verification
For each admissible gap event, verify

$$
H\equiv r+\frac{k}{2}\pmod 6
$$

and for each subtype-center sequence, verify

$$
\Delta H\equiv 0\pmod 6.
$$

### Stage 3 — Subtype counts
For each even gap \(k\), compute

$$
n_A(k),\qquad n_B(k).
$$

### Stage 4 — Standardized bias
Compute

$$
z(k)=\frac{n_A(k)-n_B(k)}{\sqrt{n_A(k)+n_B(k)}}.
$$

### Stage 5 — Support pressure
Compute

$$
\Lambda(k)
=
\sum_{\substack{q\mid k\\ q>3}}
\log\!\left(\frac{q-1}{q-2}\right),
\qquad
\Delta\Lambda(k)=\Lambda(k)-\Lambda(k-6).
$$

### Stage 6 — Hard-flip classification
Use the hard-flip detector

$$
F^\star(k)=1
\iff
\operatorname{sgn}z(k)\neq \operatorname{sgn}z(k-6)
\ \text{and}\ 
\min\{|z(k)|,\ |z(k-6)|\}\ge z_0.
$$

### Stage 7 — Diagnostics
Report:

$$
N^\star_{\mathrm{bad}}
=
\#\{k:F^\star(k)=1\land \Delta\Lambda(k)=0\},
$$

$$
P(F^\star=1\mid \Delta\Lambda\neq 0),
\qquad
P(F^\star=1\mid \Delta\Lambda=0),
$$

and the regression

$$
\Delta z(k)\approx a+b\,\Delta\Lambda(k).
$$

---

## 15. What Is Closed and What Is Open

### Closed

The following remain closed:

$$
\boxed{
H \equiv r+\frac{k}{2}\pmod W
}
$$

$$
\boxed{
\Delta H \equiv 0 \pmod W
}
$$

$$
\boxed{
\text{CRT propagation through the primorial tower}
}
$$

### Retired

The following is retired:

$$
\boxed{
F(k)=1 \Rightarrow \Delta\Lambda(k)\neq 0
\quad\text{(strict raw form)}
}
$$

### Active

The active live law is now:

$$
\boxed{
\text{support-change acts as a flip amplifier near neutrality.}
}
$$

### Still open

The following are still open:

1. the exact calibration of \(\beta\),
2. the precise analytic form of \(\Omega(x,k)\),
3. the higher-wheel flip structure at \(W=30\) and \(W=210\),
4. the Euler-product derivation of GPM mixture weights.

---

## 16. Conclusion

The Mark10 number-theoretic reduction survives, but in a refined form.

The exact midpoint rail and step-floor remain solid:

$$
H \equiv r+\frac{k}{2}\pmod W,
\qquad
\Delta H \equiv 0 \pmod W.
$$

The original strong flip theorem does not survive first contact with real data. That is progress, not failure. It tells us that raw sign changes were the wrong observable.

The corrected law is:

$$
\boxed{
\text{a hard flip is a hot hinge striking a near-neutral frame.}
}
$$

This is the proper continuation of the Mark10 program.

---

## Appendix A. Core Equations

### A.1 Midpoint shape channel
$$
H \equiv r+\frac{k}{2}\pmod W.
$$

### A.2 Step Theorem
$$
\Delta H \equiv 0 \pmod W.
$$

### A.3 Hardy–Littlewood support pressure
$$
\Lambda(k)
=
\sum_{\substack{q\mid k\\ q>3}}
\log\!\left(\frac{q-1}{q-2}\right).
$$

### A.4 Support-change detector
$$
\Delta\Lambda(k)=\Lambda(k)-\Lambda(k-6).
$$

### A.5 Standardized bias score
$$
z(k)=\frac{n_A(k)-n_B(k)}{\sqrt{n_A(k)+n_B(k)}}.
$$

### A.6 Neutral corridor
$$
|z(k)|<z_0.
$$

### A.7 Hard-flip detector
$$
F^\star(k)=1
\iff
\operatorname{sgn}z(k)\neq \operatorname{sgn}z(k-6)
\ \text{and}\ 
\min\{|z(k)|,\ |z(k-6)|\}\ge z_0.
$$

### A.8 Refined bias law
$$
\mathrm{Bias}(x;k)\approx \Omega(x,k)+\beta\,\Lambda(k)+\varepsilon(x,k).
$$

### A.9 Local jump
$$
\Delta z(k)=z(k)-z(k-6).
$$

### A.10 Jump regression
$$
\Delta z(k)\approx a+b\,\Delta\Lambda(k).
$$

### A.11 Refined hazard statement
$$
P(F^\star=1\mid \Delta\Lambda\neq 0,\ |z|\text{ near neutral})
>
P(F^\star=1\mid \Delta\Lambda=0,\ |z|\text{ near neutral}).
$$
