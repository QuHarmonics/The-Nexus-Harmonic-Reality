# NEXUS Prime-Gap Program
## Refined Closure on the Remaining Branches
### Source Split of $\pi_{30}$, Unscreened-Prime Shoulder Law, and Effective Body-Coefficient Resolution

**Dean A. Kulik**  
**QuHarmonics Research Group**  
**A-Mark9 / NEXUS Phase 10+**

---

## Abstract

This document extends the canonical prime-gap closure ledger by resolving the structural source of the remaining empirical residuals in the twin-prime branch.

Three sharpenings are established.

First, the leading coefficient in the finite-$X$ same-subtype deficit law

$$
\frac{1}{3}-\pi_{30}(X)
=
\frac{A}{\ln X}
+
\frac{B}{\ln^2 X}
+
O\!\left(\frac{1}{\ln^3 X}\right)
$$

is shown to be **arithmetical**, not renewal-level. The competing-renewal contribution enters only at order $1/\ln^2 X$, forcing

$$
A = A_{\mathrm{HL}}.
$$

Second, the empirical body correction in the $k=2$, $W=30$ renewal shell is derived from the first unscreened prime beyond the wheel, namely $q=7$, and then refined by the next two unscreened primes $q=11$ and $q=13$. The correction is not a mysterious box-shaped patch, but the coarse projection of discrete modular enhancement shoulders.

Third, the empirical body coefficient

$$
\gamma_{\mathrm{fit}} \approx 0.075
$$

is shown to be nearly reproduced from first principles by the combined residue-shoulder corrections of $q=7,11,13$, yielding the projected value

$$
\gamma_{\mathrm{proj}} \approx 0.0795.
$$

This closes the body-correction branch at the mechanism level and reduces the remaining frontier to three exact problems:

1. exact evaluation of $A_{\mathrm{HL}}$,
2. analytic origin of the $k=30$ crossover threshold $T$,
3. global twin-prime / Polignac infinitude.

This document does **not** claim to solve the full twin-prime conjecture. It does claim that the main empirical residuals of the current NEXUS twin-prime shell are no longer conceptually ambiguous.

---

## 1. Background

The corrected Phase 10 and Phase 10 Extension state of the prime-gap branch leaves a small number of sharply posed open problems:

- the exact source of the leading coefficient $A$ in the $\pi_{30}$ deficit law,
- the analytic meaning of the body correction in the active $k=2$ shell,
- the threshold theory of the two-regime $k=30$ model,
- and the deep global infinitude problem.

The active $k=2$ shell is

$$
\mathbb{P}(M=m)
=
\frac{1}{Z}
\operatorname{NB}(m;r,p)\,
f_{\mathrm{spike}}(m)\,
f_{\mathrm{body}}(m),
$$

with

$$
M = \frac{\Delta H}{W},
\qquad
W = 30,
$$

and

$$
f_{\mathrm{spike}}(m)
=
1
+
\alpha_7 \mathbf{1}_{7\mid m}
+
\alpha_{11} \mathbf{1}_{11\mid m}
+
\alpha_{13} \mathbf{1}_{13\mid m},
$$

$$
f_{\mathrm{body}}(m)
=
1+\gamma\,\mathbf{1}_{6\le m\le 15}.
$$

The fitted body coefficient is approximately

$$
\gamma_{\mathrm{fit}} \approx 0.075.
$$

The purpose of this note is to replace the empirical body box by an explicit modular law and to isolate the true source of the $\pi_{30}$ leading term.

---

## 2. The $\pi_{30}$ Deficit: Renewal Versus Arithmetic

Define the same-subtype adjacency deficit by

$$
D_{30}(X)
=
\frac{1}{3}
-
\pi_{30}(X).
$$

The empirically stabilized law is

$$
D_{30}(X)
=
\frac{A}{\ln X}
+
\frac{B}{\ln^2 X}
+
O\!\left(\frac{1}{\ln^3 X}\right),
$$

with canonical numerical values

$$
A = 0.104115,
\qquad
B = 6.662432.
$$

The extension identifies two distinct mechanisms:

1. a competing-renewal process effect,
2. a Hardy–Littlewood singular-series weighting effect.

The problem is to decide which mechanism contributes at which asymptotic order.

### 2.1 Competing-renewal layer

In the common geometric approximation, the same-component consecutive probability is

$$
\pi_\infty^{\mathrm{geo}}(p)
=
\frac{p(1-p)^2}{1-(1-p)^3}.
$$

Therefore

$$
D_\infty^{\mathrm{geo}}(p)
=
\frac{1}{3}
-
\frac{p(1-p)^2}{1-(1-p)^3}.
$$

Expanding about $p=0$ gives

$$
D_\infty^{\mathrm{geo}}(p)
=
\frac{p}{3}
+
O(p^2).
$$

Now the midpoint-gap scale obeys

$$
\mathbb{E}[M] \asymp \ln^2 X,
$$

so the effective renewal parameter satisfies

$$
p(X) \asymp \frac{1}{\ln^2 X}.
$$

Substituting into the geometric expansion yields

$$
D_{\mathrm{CR}}(X)
=
O\!\left(\frac{1}{\ln^2 X}\right).
$$

This proves that the competing-renewal mechanism cannot generate the leading term

$$
\frac{A}{\ln X}.
$$

### 2.2 Consequence

The leading coefficient must be entirely arithmetic:

$$
\boxed{
A = A_{\mathrm{HL}}.
}
$$

The renewal contribution only enters at the next order:

$$
\boxed{
B = B_{\mathrm{HL}} + B_{\mathrm{CR}}.
}
$$

This closes the qualitative source question.

---

## 3. Asymptotic Expansion of the Weighted Singular-Series Ratio

The extension proposes the weighted ratio

$$
\pi_{30}(X)
\approx
\frac{\displaystyle\sum_{\substack{g\le G(X)\\30\mid g}} S(g)\,\ln^{-2}(X/g)}
{\displaystyle\sum_{g\le G(X)} S(g)\,\ln^{-2}(X/g)}.
$$

Set

$$
L = \ln X,
\qquad
\ell_g = \ln g.
$$

Then

$$
\frac{1}{\ln^2(X/g)}
=
\frac{1}{(L-\ell_g)^2}
=
\frac{1}{L^2}
\left(
1+\frac{2\ell_g}{L}+\frac{3\ell_g^2}{L^2}+O\!\left(\frac{1}{L^3}\right)
\right).
$$

Define the weighted sums

$$
N_0(X)
=
\sum_{\substack{g\le G(X)\\30\mid g}} S(g),
\qquad
N_1(X)
=
\sum_{\substack{g\le G(X)\\30\mid g}} S(g)\ln g,
$$

$$
D_0(X)
=
\sum_{g\le G(X)} S(g),
\qquad
D_1(X)
=
\sum_{g\le G(X)} S(g)\ln g.
$$

Then the ratio expansion gives

$$
\pi_{30}(X)
=
\frac{N_0}{D_0}
+
\frac{2}{L}\frac{N_1D_0-N_0D_1}{D_0^2}
+
O\!\left(\frac{1}{L^2}\right).
$$

As $X\to\infty$, the leading ratio tends to the equal-split limit:

$$
\frac{N_0}{D_0}\to \frac{1}{3}.
$$

Thus

$$
\pi_{30}(X)
=
\frac{1}{3}
-
\frac{A}{\ln X}
+
O\!\left(\frac{1}{\ln^2 X}\right),
$$

with

$$
A
=
\frac{2}{3}
\left(
\mu_{\mathrm{all}}-\mu_{\mathrm{same}}
\right),
$$

where

$$
\mu_{\mathrm{same}}
=
\lim_{X\to\infty}\frac{N_1(X)}{N_0(X)},
\qquad
\mu_{\mathrm{all}}
=
\lim_{X\to\infty}\frac{D_1(X)}{D_0(X)}.
$$

So the leading coefficient is the weighted log-gap mean separation between the same-subtype sector and the total transition sector.

### 3.1 Main formula for the leading coefficient

$$
\boxed{
A
=
\frac{2}{3}
\left(
\mu_{\mathrm{all}}-\mu_{\mathrm{same}}
\right).
}
$$

This is the cleanest available closed-form structural expression for the leading coefficient.

---

## 4. First Unscreened Prime Beyond the Wheel

The body correction is no longer treated as a phenomenological box. It is the first visible effect of primes not screened by the wheel

$$
W = 30 = 2\cdot 3\cdot 5.
$$

The first unscreened prime is

$$
q = 7.
$$

For same-subtype twin transitions, the relevant 4-tuple modulo $q$ is

$$
\{0,2,30m,30m+2\}\pmod q.
$$

Since

$$
30 \equiv 2 \pmod 7,
$$

this becomes

$$
\{0,2,2m,2m+2\}\pmod 7.
$$

The generic case occupies four distinct residues and has baseline factor

$$
\frac{7-4}{7}.
$$

Enhancement occurs when residue collisions reduce the number of distinct occupied classes.

---

## 5. Exact $q=7$ Enhancement Law

### 5.1 Core spike: $m\equiv 0\pmod 7$

If

$$
m\equiv 0\pmod 7,
$$

then

$$
2m\equiv 0\pmod 7,
$$

and the set becomes

$$
\{0,2,0,2\},
$$

occupying only 2 distinct residues. The relative enhancement is

$$
E_7^{(0)}
=
\frac{7-2}{7-4}
=
\frac{5}{3}.
$$

### 5.2 Shoulder spikes: $m\equiv \pm1\pmod 7$

If

$$
m\equiv \pm1\pmod 7,
$$

then one nontrivial overlap occurs and the set occupies only 3 residues. The relative enhancement is

$$
E_7^{(\pm)}
=
\frac{7-3}{7-4}
=
\frac{4}{3}.
$$

### 5.3 Generic case

All remaining residues give the generic 4-residue occupation, hence

$$
E_7 = 1.
$$

### 5.4 Full law

Therefore

$$
\boxed{
E_7(m)=
\begin{cases}
\dfrac{5}{3}, & m\equiv 0 \pmod 7,\\[8pt]
\dfrac{4}{3}, & m\equiv \pm1 \pmod 7,\\[8pt]
1, & \text{otherwise.}
\end{cases}
}
$$

This is the first exact correction law beyond the $W=30$ wheel.

---

## 6. Why the Empirical Body Window Is $[6,15]$

The first two $q=7$ enhancement triplets are

$$
\{6,7,8\}
\quad\text{and}\quad
\{13,14,15\},
$$

since these are precisely the first values with residues

$$
m\equiv -1,0,+1 \pmod 7.
$$

Hence the empirical body box

$$
[6,15]
$$

is the coarse envelope of the first two $q=7$ enhancement triplets.

This means that the original fitted body term

$$
1+\gamma\,\mathbf{1}_{6\le m\le 15}
$$

should be understood as a box-projection of the sharper law

$$
\mathbf{1}_{m\equiv 0,\pm1 \!\!\!\!\pmod 7}.
$$

---

## 7. Coarse-Grained $q=7$ Projection

### 7.1 Mean enhancement in the body window

On the interval $m\in[6,15]$, the residues mod $7$ are

$$
6,0,1,2,3,4,5,6,0,1.
$$

So the window contains:

- two core hits: $m\equiv 0$,
- four shoulder hits: $m\equiv \pm1$,
- four generic values.

The average enhancement over the window is

$$
\overline E_{7,[6,15]}
=
\frac{
2\cdot \frac{5}{3}
+
4\cdot \frac{4}{3}
+
4\cdot 1
}{10}
=
\frac{19}{15}.
$$

### 7.2 Mean enhancement over a full residue cycle

Across a full mod-$7$ cycle, the average enhancement is

$$
\overline E_{7,\mathrm{cyc}}
=
\frac{
1\cdot \frac{5}{3}
+
2\cdot \frac{4}{3}
+
4\cdot 1
}{7}
=
\frac{25}{21}.
$$

### 7.3 Projected body excess from $q=7$

Therefore the projected excess is

$$
\gamma_{7,\mathrm{proj}}
=
\frac{\overline E_{7,[6,15]}}{\overline E_{7,\mathrm{cyc}}}
-
1
=
\frac{19/15}{25/21}-1
=
\frac{8}{125}
=
0.064.
$$

So the $q=7$ shoulder alone produces a coarse body boost of

$$
\boxed{
\gamma_{7,\mathrm{proj}} = 0.064.
}
$$

This is already close to the fitted empirical body coefficient.

---

## 8. Universal Unscreened-Prime Shoulder Law

The same reasoning works for every prime

$$
q\nmid 30.
$$

Let

$$
a_q \equiv 30 \pmod q.
$$

Then the relevant pattern is

$$
\{0,2,a_qm,a_qm+2\}\pmod q.
$$

The generic case has four distinct residues. Collisions occur in the following cases:

### 8.1 Core spike
If

$$
a_qm \equiv 0 \pmod q,
$$

then

$$
m\equiv 0 \pmod q,
$$

and the enhancement is

$$
E_q^{(0)} = \frac{q-2}{q-4}.
$$

### 8.2 Shoulder spikes
If

$$
a_qm \equiv \pm 2 \pmod q,
$$

then

$$
m \equiv \pm 2a_q^{-1} \pmod q,
$$

and the enhancement is

$$
E_q^{(\pm)} = \frac{q-3}{q-4}.
$$

### 8.3 Full universal law

Thus for any unscreened prime $q$,

$$
\boxed{
E_q(m)=
\begin{cases}
\dfrac{q-2}{q-4}, & m\equiv 0 \pmod q,\\[8pt]
\dfrac{q-3}{q-4}, & m\equiv \pm 2a_q^{-1} \pmod q,\\[8pt]
1, & \text{otherwise.}
\end{cases}
}
$$

where

$$
a_q \equiv 30 \pmod q.
$$

This is the exact modular shoulder law beyond the $W=30$ wheel.

---

## 9. $q=11$ Shoulder Correction

For $q=11$,

$$
30\equiv 8 \pmod{11},
\qquad
8^{-1}\equiv 7 \pmod{11}.
$$

Hence the shoulder classes are

$$
m\equiv \pm 2\cdot 7 \equiv \pm 14 \equiv \pm 3 \pmod{11},
$$

that is,

$$
m\equiv 3,8 \pmod{11}.
$$

Therefore

$$
E_{11}(m)=
\begin{cases}
\dfrac{9}{7}, & m\equiv 0 \pmod{11},\\[8pt]
\dfrac{8}{7}, & m\equiv 3,8 \pmod{11},\\[8pt]
1, & \text{otherwise.}
\end{cases}
$$

### 9.1 Body-window mean

On $m\in[6,15]$, the residues mod $11$ are

$$
6,7,8,9,10,0,1,2,3,4.
$$

So the window contains:

- one core hit,
- two shoulder hits,
- seven generic values.

The mean enhancement is

$$
\overline E_{11,[6,15]}
=
\frac{
1\cdot \frac{9}{7}
+
2\cdot \frac{8}{7}
+
7\cdot 1
}{10}
=
\frac{37}{35}.
$$

### 9.2 Cycle mean

Across a full mod-$11$ cycle,

$$
\overline E_{11,\mathrm{cyc}}
=
\frac{
1\cdot \frac{9}{7}
+
2\cdot \frac{8}{7}
+
8\cdot 1
}{11}
=
\frac{81}{77}.
$$

### 9.3 Projected excess

Thus

$$
\gamma_{11,\mathrm{proj}}
=
\frac{37/35}{81/77}-1
=
\frac{14}{2835}
\approx 0.00494.
$$

So

$$
\boxed{
\gamma_{11,\mathrm{proj}} \approx 0.00494.
}
$$

---

## 10. $q=13$ Shoulder Correction

For $q=13$,

$$
30\equiv 4 \pmod{13},
\qquad
4^{-1}\equiv 10 \pmod{13}.
$$

Hence the shoulder classes are

$$
m\equiv \pm 2\cdot 10 \equiv \pm 20 \equiv \pm 7 \pmod{13},
$$

that is,

$$
m\equiv 6,7 \pmod{13}.
$$

Therefore

$$
E_{13}(m)=
\begin{cases}
\dfrac{11}{9}, & m\equiv 0 \pmod{13},\\[8pt]
\dfrac{10}{9}, & m\equiv 6,7 \pmod{13},\\[8pt]
1, & \text{otherwise.}
\end{cases}
$$

### 10.1 Body-window mean

On $m\in[6,15]$, the residues mod $13$ are

$$
6,7,8,9,10,11,12,0,1,2.
$$

So the window contains:

- one core hit,
- two shoulder hits,
- seven generic values.

The window mean is

$$
\overline E_{13,[6,15]}
=
\frac{
1\cdot \frac{11}{9}
+
2\cdot \frac{10}{9}
+
7\cdot 1
}{10}
=
\frac{47}{45}.
$$

### 10.2 Cycle mean

Across a full mod-$13$ cycle,

$$
\overline E_{13,\mathrm{cyc}}
=
\frac{
1\cdot \frac{11}{9}
+
2\cdot \frac{10}{9}
+
10\cdot 1
}{13}
=
\frac{121}{117}.
$$

### 10.3 Projected excess

Thus

$$
\gamma_{13,\mathrm{proj}}
=
\frac{47/45}{121/117}-1
=
\frac{6}{605}
\approx 0.00992.
$$

So

$$
\boxed{
\gamma_{13,\mathrm{proj}} \approx 0.00992.
}
$$

---

## 11. Effective Body Coefficient from $q=7,11,13$

Now combine the first three unscreened-prime projected factors:

$$
(1+\gamma_{7,\mathrm{proj}})
(1+\gamma_{11,\mathrm{proj}})
(1+\gamma_{13,\mathrm{proj}})
=
\frac{133}{125}\cdot \frac{2849}{2835}\cdot \frac{611}{605}
\approx 1.0795.
$$

So the total projected body excess is

$$
\gamma_{\{7,11,13\},\mathrm{proj}}
\approx 0.0795.
$$

Compare with the fitted empirical body coefficient

$$
\gamma_{\mathrm{fit}} \approx 0.075.
$$

The agreement is very close.

### 11.1 Main result

$$
\boxed{
\gamma_{\mathrm{proj}} \approx 0.0795 \approx \gamma_{\mathrm{fit}}.
}
$$

This shows that the fitted body coefficient is almost completely explained by the first three unscreened-prime shoulder structures.

---

## 12. Structural Interpretation of the Body Term

The body term is therefore not a free phenomenological patch. It is the box-projected residue shoulder produced by the first unscreened primes beyond the $W=30$ wheel.

At the sharp modular level, the body and spike structure is:

$$
\text{core spike: } m\equiv 0\pmod q,
\qquad
\text{shoulder spikes: } m\equiv \pm 2a_q^{-1}\pmod q.
$$

For $q=7$, this is

$$
m\equiv 0,\pm1\pmod 7.
$$

For $q=11$, this is

$$
m\equiv 0,3,8\pmod{11}.
$$

For $q=13$, this is

$$
m\equiv 0,6,7\pmod{13}.
$$

The empirical body box $[6,15]$ is the low-$m$ projection of the first two $q=7$ triplets, with smaller support from the $q=11$ and $q=13$ shoulders.

So the true interpretation is:

$$
\boxed{
\text{body correction}=
\text{the unscreened-prime residue shoulder of the }W=30\text{ wheel.}
}
$$

---

## 13. Subtype Infinitude Is Not an Independent Missing Branch

The subtype asymptotic statement is

$$
\pi_r(X)
\sim
\frac{1}{|S_W(k)|}C_k\operatorname{Li}_2(X),
\qquad
r\in S_W(k).
$$

For $k=2$, $W=30$ this becomes

$$
\pi_r(X)
\sim
\frac{C_2}{3}\operatorname{Li}_2(X),
\qquad
r\in\{11,17,29\}.
$$

So subtype infinitude is not a separate wall. It reduces to:

1. total twin-prime / Polignac infinitude,
2. orbit symmetry of the admissible subtype set.

Hence

$$
\boxed{
\text{subtype infinitude is not independently missing once global infinitude is granted.}
}
$$

---

## 14. What Is Now Closed

The following statements are now effectively closed at the structural level.

### 14.1 Leading-source split of the $\pi_{30}$ law
$$
\boxed{
A = A_{\mathrm{HL}},
\qquad
B = B_{\mathrm{HL}} + B_{\mathrm{CR}}.
}
$$

### 14.2 Leading coefficient formula
$$
\boxed{
A
=
\frac{2}{3}
\left(
\mu_{\mathrm{all}}-\mu_{\mathrm{same}}
\right).
}
$$

### 14.3 Exact unscreened-prime shoulder law
$$
\boxed{
E_q(m)=
\begin{cases}
\dfrac{q-2}{q-4}, & m\equiv 0 \pmod q,\\[8pt]
\dfrac{q-3}{q-4}, & m\equiv \pm 2a_q^{-1}\pmod q,\\[8pt]
1, & \text{otherwise.}
\end{cases}
}
$$

### 14.4 Effective body-coefficient explanation
$$
\boxed{
\gamma_{\mathrm{proj}}\approx 0.0795 \approx \gamma_{\mathrm{fit}}.
}
$$

### 14.5 Subtype-infinitude reduction
$$
\boxed{
\text{subtype infinitude}=
\text{global infinitude}+\text{orbit symmetry}.
}
$$

---

## 15. Remaining Open Problems

The remaining frontier is now very narrow.

### Open Problem 1 — Exact evaluation of $A_{\mathrm{HL}}$

The exact numerical value

$$
A = 0.104115
$$

still requires explicit evaluation of the weighted singular-series mean gap separation.

### Open Problem 2 — $k=30$ threshold theory

The two-regime $k=30$ shell is fitted, but the analytic origin of the threshold

$$
T
$$

is still open.

### Open Problem 3 — Global twin-prime / Polignac infinitude

This remains the deepest unresolved branch.

---

## 16. Final Closure Statement

The remaining twin-prime body branch is no longer conceptually open.

It is now resolved as follows:

$$
\boxed{
\text{The leading } \pi_{30} \text{ coefficient is arithmetic, not renewal.}
}
$$

$$
\boxed{
\text{The body correction is the unscreened-prime residue-shoulder law beyond } W=30.
}
$$

$$
\boxed{
\text{The fitted body coefficient is quantitatively explained by } q=7,11,13.
}
$$

So the surviving frontier is no longer a vague pile of residuals. It is a clean list of exact analytic targets.

---

## Appendix A. Core Equations

### A.1 Deficit law
$$
\frac{1}{3}-\pi_{30}(X)
=
\frac{A}{\ln X}
+
\frac{B}{\ln^2 X}
+
O\!\left(\frac{1}{\ln^3 X}\right).
$$

### A.2 Geometric competing-renewal law
$$
\pi_\infty^{\mathrm{geo}}(p)
=
\frac{p(1-p)^2}{1-(1-p)^3}.
$$

### A.3 Renewal deficit expansion
$$
D_\infty^{\mathrm{geo}}(p)
=
\frac{1}{3}
-
\frac{p(1-p)^2}{1-(1-p)^3}
=
\frac{p}{3}+O(p^2).
$$

### A.4 Weighted singular-series ratio
$$
\pi_{30}(X)
\approx
\frac{\displaystyle\sum_{\substack{g\le G(X)\\30\mid g}} S(g)\,\ln^{-2}(X/g)}
{\displaystyle\sum_{g\le G(X)} S(g)\,\ln^{-2}(X/g)}.
$$

### A.5 Leading coefficient formula
$$
A
=
\frac{2}{3}
\left(
\mu_{\mathrm{all}}-\mu_{\mathrm{same}}
\right).
$$

### A.6 $q=7$ enhancement law
$$
E_7(m)=
\begin{cases}
\dfrac{5}{3}, & m\equiv 0 \pmod 7,\\[8pt]
\dfrac{4}{3}, & m\equiv \pm1 \pmod 7,\\[8pt]
1, & \text{otherwise.}
\end{cases}
$$

### A.7 $q=7$ projected body excess
$$
\gamma_{7,\mathrm{proj}}
=
\frac{19/15}{25/21}-1
=
\frac{8}{125}
=
0.064.
$$

### A.8 Universal unscreened-prime shoulder law
$$
E_q(m)=
\begin{cases}
\dfrac{q-2}{q-4}, & m\equiv 0 \pmod q,\\[8pt]
\dfrac{q-3}{q-4}, & m\equiv \pm 2a_q^{-1}\pmod q,\\[8pt]
1, & \text{otherwise,}
\end{cases}
\qquad
a_q \equiv 30 \pmod q.
$$

### A.9 $q=11$ law
$$
E_{11}(m)=
\begin{cases}
\dfrac{9}{7}, & m\equiv 0 \pmod{11},\\[8pt]
\dfrac{8}{7}, & m\equiv 3,8 \pmod{11},\\[8pt]
1, & \text{otherwise.}
\end{cases}
$$

### A.10 $q=13$ law
$$
E_{13}(m)=
\begin{cases}
\dfrac{11}{9}, & m\equiv 0 \pmod{13},\\[8pt]
\dfrac{10}{9}, & m\equiv 6,7 \pmod{13},\\[8pt]
1, & \text{otherwise.}
\end{cases}
$$

### A.11 Projected body excesses
$$
\gamma_{11,\mathrm{proj}}
=
\frac{37/35}{81/77}-1
=
\frac{14}{2835}
\approx 0.00494,
$$

$$
\gamma_{13,\mathrm{proj}}
=
\frac{47/45}{121/117}-1
=
\frac{6}{605}
\approx 0.00992.
$$

### A.12 Combined projected body coefficient
$$
(1+\gamma_{7,\mathrm{proj}})
(1+\gamma_{11,\mathrm{proj}})
(1+\gamma_{13,\mathrm{proj}})
\approx 1.0795,
$$

so

$$
\gamma_{\mathrm{proj}}
\approx 0.0795.
$$

### A.13 Subtype asymptotic
$$
\pi_r(X)
\sim
\frac{1}{|S_W(k)|}C_k\operatorname{Li}_2(X).
$$

### A.14 Twin-prime subtype specialization
$$
\pi_r(X)
\sim
\frac{C_2}{3}\operatorname{Li}_2(X),
\qquad
r\in\{11,17,29\}.
$$
