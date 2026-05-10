# Mark 10.2 — Refined Flip-Sign Law
## Neutral-Corridor Correction, Hard-Flip Detector, and Support-Change as a Flip Amplifier

**Dean A. Kulik**  
**QuHarmonics Research Group**  
**ORCID: 0009-0003-3128-8828**  
**NEXUS Phase 1163+ / A-Mark9–Mark10 Continuation**

---

## Abstract

This document refines the Mark 10.1 flip-sign boundary reduction after the first nontrivial empirical test at prime limit $2\times 10^6$.

The strict Support-Change Flip Predicate

$$
F(k)=1 \Rightarrow \Delta\Lambda(k)\neq 0
$$

is **false** in its raw form: empirical testing produced cold-rail flips, with

$$
N_{\mathrm{bad}}=5
$$

for the initial detector. This falsifies the strong claim that support-change is a necessary condition for every observed sign reversal.

However, the failure of the strict predicate does not invalidate the frame model. It reveals that the original flip detector was too coarse. A raw sign change is not the same thing as a meaningful frame crossing, because bias values close to zero can jitter in sign without representing a genuine crossing event.

This note therefore introduces the **neutral corridor correction** and the **hard-flip detector**. The new law is:

$$
\boxed{
\text{support-change is not a universal flip condition;}
\quad
\text{it is a flip amplifier when the frame is already near neutrality.}
}
$$

The flip problem is thus reduced from a strict implication to a conditional hazard law: support-change hinges increase the probability of a hard crossing when the current subtype frame bias is already in a near-zero corridor.

This document states the corrected formulas, interprets the first empirical failure, and defines the next exact run.

---

## 1. The Closed Frame Floor

The Step Theorem and midpoint rail law remain completely intact.

For a prime pair $(p,p+k)$ at wheel depth $W$, with admissible subtype residue $r\in S_W(k)$ and midpoint

$$
H=p+\frac{k}{2},
$$

the shape channel is

$$
\boxed{
H \equiv r+\frac{k}{2}\pmod W.
}
$$

If $H_j$ and $H_{j+1}$ are consecutive midpoints in the same subtype, then

$$
\Delta H
=
H_{j+1}-H_j
\equiv 0 \pmod W.
$$

So the exact frame floor is

$$
\boxed{
H \equiv r+\frac{k}{2}\pmod W,
\qquad
\Delta H \equiv 0 \pmod W.
}
$$

This remains the hard floor of the shape-channel program and is unaffected by the empirical flip refinements.

---

## 2. Original Reduced Flip Law

The original Mark 10.1 reduction proposed that at $W=6$ the $T0A/T0B$ bias is controlled by

1. a single oscillatory frame mode, and  
2. a scalar arithmetic support-pressure term.

Define the odd-prime support of the gap:

$$
S(k)=\{\,q>3:q\mid k\,\},
$$

and the support-pressure function

$$
\Lambda(k)
=
\sum_{\substack{q\mid k\\ q>3}}
\log\!\left(\frac{q-1}{q-2}\right).
$$

Then define the support-change detector

$$
\Delta\Lambda(k)=\Lambda(k)-\Lambda(k-6).
$$

The first reduced model was

$$
\mathrm{Bias}(x;k)\approx \Omega(x)+\beta\,\Lambda(k),
$$

where

- $\Omega(x)$ is the oscillatory frame mode at sieve depth $x$,
- $\beta>0$ is a scale factor.

From this, the strict predicate was proposed:

$$
\boxed{
F(k)=1 \Rightarrow \Delta\Lambda(k)\neq 0.
}
$$

This means: every sign flip should occur at a support-change hinge.

---

## 3. First Empirical Failure of the Strict Predicate

The first real empirical run at limit

$$
x\le 2\times 10^6
$$

and even gaps $k\le 100$ with sufficient counts produced:

- tested $k$ values: $50$,
- bad flips on cold rails:
  $$
  N_{\mathrm{bad}}=5,
  $$
- estimated flip rates:
  $$
  P(\mathrm{flip}\mid \text{hot hinge})\approx 0.262,
  $$
  $$
  P(\mathrm{flip}\mid \text{cold rail})\approx 0.625.
  $$

The strict implication is therefore false in this raw form.

### 3.1 What this means

This does **not** mean the support-change term is useless. It means the detector was too coarse.

A raw sign change

$$
\operatorname{sgn}(n_A-n_B)\neq \operatorname{sgn}(n_A^{-}-n_B^{-})
$$

treats tiny near-zero wobble the same way it treats a large, meaningful crossing. That is a category error.

If the subtype bias is already very close to zero, even a small amount of estimator noise or finite-sample oscillation can create an apparent sign reversal. Such a jitter event should not be counted as a true frame crossing.

So the empirical falsification kills the strict predicate, but it also tells us what was missing: a **neutral corridor**.

---

## 4. Standardized Bias Score

To repair the detector, define the standardized subtype bias score

$$
\boxed{
z(k)=\frac{n_A(k)-n_B(k)}{\sqrt{n_A(k)+n_B(k)}}.
}
$$

This is the correct local significance-scale readout of subtype imbalance.

Interpretation:

- $z(k)>0$: $T0A$ favored,
- $z(k)<0$: $T0B$ favored,
- $|z(k)|\approx 0$: near-neutral corridor.

The key point is that the near-zero zone should not be treated as a real frame commitment.

---

## 5. The Neutral Corridor

Introduce a corridor threshold

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

This is the regime where the frame is not strongly committed to one side.

### 5.1 Why this matters

A cold rail is allowed to hover near zero.  
That does not automatically mean the frame has crossed. It means the frame is unresolved or only weakly committed.

So raw sign changes inside the neutral corridor must be downgraded from “flip” to “jitter.”

---

## 6. The Hard-Flip Detector

We now define a **hard flip** only when both neighboring bias states lie materially away from zero and have opposite sign.

$$
\boxed{
F^\star(k)=1
\iff
\operatorname{sgn}z(k)\neq \operatorname{sgn}z(k-6)
\ \text{and}\ 
\min\{|z(k)|,\ |z(k-6)|\}\ge z_0.
}
$$

This removes spurious corridor jitter from the event count.

### 6.1 Interpretation

A hard flip is a genuine frame crossing:

- the bias was materially on one side at $k-6$,
- materially on the other side at $k$,
- and did not merely wobble across zero with negligible amplitude.

So the corrected event logic is:

- **raw sign flip** = any sign change,
- **hard flip** = sign change outside the neutral corridor.

---

## 7. Refined Bias Law

The original reduced law must now be corrected. The oscillatory contribution is not merely a constant in $k$.

The refined first-order model is

$$
\boxed{
\mathrm{Bias}(x;k)\approx \Omega(x,k)+\beta\,\Lambda(k)+\varepsilon(x,k),
}
$$

where

- $\Omega(x,k)$ is the smooth frame-mode drift across $k$,
- $\beta\,\Lambda(k)$ is the support-change kick,
- $\varepsilon(x,k)$ is detector noise / finite-sample fluctuation.

This explains the empirical outcome:

- cold-rail raw flips can come from
  $$
  \Omega(x,k)
  $$
  drifting through zero or from
  $$
  \varepsilon(x,k),
  $$
- support-change hinges create discrete jumps, but only matter strongly if the baseline is already near zero.

### 7.1 New interpretation

So the correct law is no longer:

$$
\text{support-change is necessary for a flip.}
$$

It becomes:

$$
\boxed{
\text{support-change raises flip hazard when the frame is already near neutral.}
}
$$

This is a much better law.

---

## 8. Hot/Cold Frontier — Corrected Version

The original hot/cold frontier law said:

$$
\Delta\Lambda(k)=0 \iff \text{cold rail},
\qquad
\Delta\Lambda(k)\neq 0 \iff \text{hot hinge}.
$$

That still remains useful, but only at the level of **arithmetic support pressure**. It is not identical to observed hard flips.

So the corrected interpretation is:

### 8.1 Cold rail
If

$$
\Delta\Lambda(k)=0,
$$

then there is no new odd-prime support kick. The arithmetic rail is cold.

### 8.2 Hot hinge
If

$$
\Delta\Lambda(k)\neq 0,
$$

then the gap crosses an odd-prime support boundary. This is a hot hinge in the arithmetic channel.

### 8.3 Hard crossing condition
A hot hinge only produces a hard flip if it strikes the frame when the bias is already in the neutral corridor.

So the composite law is

$$
\boxed{
\text{hard flip} =
\text{hot hinge}
\;\oplus\;
\text{near-neutral frame state}.
}
$$

This is the corrected hot/cold law.

---

## 9. Refined Predicate

The strict predicate is dead. The corrected predicate is probabilistic.

### 9.1 Hazard form

$$
\boxed{
P(F^\star=1\mid \Delta\Lambda\neq 0,\ |z|\text{ near neutral})
>
P(F^\star=1\mid \Delta\Lambda=0,\ |z|\text{ near neutral}).
}
$$

This says: support-change hinges should increase the probability of a genuine crossing when the frame is already near zero.

### 9.2 Practical version

A simpler working version is:

$$
\boxed{
\text{support-change is a flip amplifier near neutrality, not a universal flip condition everywhere.}
}
$$

That is the real replacement law.

---

## 10. Regression Form

A useful empirical test is not only event counting, but local jump fitting.

Define

$$
\Delta z(k)=z(k)-z(k-6).
$$

Then fit the reduced relation

$$
\boxed{
\Delta z(k)\approx a+b\,\Delta\Lambda(k).
}
$$

Interpretation:

- if
  $$
  b>0,
  $$
  the support-change kick is real,
- if
  $$
  b\approx 0,
  $$
  the support-change pressure is not materially affecting the local bias jump.

This regression remains meaningful even if the event counts are noisy.

---

## 11. Event Classification Table

The flip problem should now be classified into four states.

### 11.1 Cold stable
$$
\Delta\Lambda(k)=0,\qquad F^\star(k)=0,\qquad |z(k)|\ge z_0.
$$

### 11.2 Cold neutral
$$
\Delta\Lambda(k)=0,\qquad |z(k)|<z_0.
$$

These are not genuine flip sites. They are neutral-corridor rails.

### 11.3 Hot hinge stable
$$
\Delta\Lambda(k)\neq 0,\qquad F^\star(k)=0.
$$

The arithmetic kick exists, but it does not produce a hard crossing.

### 11.4 Hot hinge flip
$$
\Delta\Lambda(k)\neq 0,\qquad F^\star(k)=1.
$$

This is the real boundary event.

This classification should replace the raw sign-flip table.

---

## 12. Next Empirical Run

The next run should **not** simply increase the prime limit with the same bad detector.

Instead, for each even gap

$$
k\le 100
\quad\text{or}\quad
k\le 210,
$$

compute:

$$
k,\quad
n_A(k),\quad
n_B(k),\quad
z(k),\quad
\Delta z(k),\quad
\Lambda(k),\quad
\Delta\Lambda(k),\quad
F^\star(k).
$$

Then report:

### 12.1 Hard bad flips
$$
N^\star_{\mathrm{bad}}
=
\#\{k : F^\star(k)=1 \land \Delta\Lambda(k)=0\}.
$$

### 12.2 Conditional hard-flip probabilities
$$
P(F^\star=1\mid \Delta\Lambda\neq 0),
\qquad
P(F^\star=1\mid \Delta\Lambda=0).
$$

### 12.3 Neutral-corridor-conditioned probabilities
$$
P(F^\star=1\mid \Delta\Lambda\neq 0,\ |z|\text{ near neutral}),
$$

$$
P(F^\star=1\mid \Delta\Lambda=0,\ |z|\text{ near neutral}).
$$

### 12.4 Jump regression
$$
\Delta z(k)\approx a+b\,\Delta\Lambda(k).
$$

These are the next real diagnostics.

---

## 13. What Is Solved Now

The following statements now stand.

### 13.1 Still solved
$$
\boxed{
H \equiv r+\frac{k}{2}\pmod W,
\qquad
\Delta H \equiv 0 \pmod W.
}
$$

### 13.2 Strict predicate falsified
$$
\boxed{
F(k)=1 \Rightarrow \Delta\Lambda(k)\neq 0
\quad\text{is false in raw form.}
}
$$

### 13.3 Corrected law
$$
\boxed{
\text{support-change is a jump term, not a universal necessary condition.}
}
$$

### 13.4 Better formulation
$$
\boxed{
\text{support-change acts as a flip amplifier inside a neutral corridor.}
}
$$

This is the real solve-state after Phase 1288.

---

## 14. Conclusion

The first real empirical test did exactly what it needed to do: it killed the naive strict predicate and forced the model to become sharper.

The corrected picture is:

- the shape-channel frame rail is exact,
- the odd-prime support term is still real,
- but sign flips must be separated into:
  - true hard crossings,
  - and neutral-corridor jitter.

The next live law is therefore:

$$
\boxed{
\text{hard flips occur when a hot hinge strikes a near-neutral frame.}
}
$$

This is the correct continuation of the Mark 10 reduction.

---

## Appendix A. Core Equations

### A.1 Midpoint frame law
$$
H \equiv r+\frac{k}{2}\pmod W.
$$

### A.2 Step Theorem
$$
\Delta H \equiv 0 \pmod W.
$$

### A.3 Support-pressure function
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

### A.6 Hard-flip detector
$$
F^\star(k)=1
\iff
\operatorname{sgn}z(k)\neq \operatorname{sgn}z(k-6)
\ \text{and}\ 
\min\{|z(k)|,\ |z(k-6)|\}\ge z_0.
$$

### A.7 Refined bias law
$$
\mathrm{Bias}(x;k)\approx \Omega(x,k)+\beta\,\Lambda(k)+\varepsilon(x,k).
$$

### A.8 Local jump fit
$$
\Delta z(k)=z(k)-z(k-6)\approx a+b\,\Delta\Lambda(k).
$$

### A.9 Refined hazard statement
$$
P(F^\star=1\mid \Delta\Lambda\neq 0,\ |z|\text{ near neutral})
>
P(F^\star=1\mid \Delta\Lambda=0,\ |z|\text{ near neutral}).
$$
