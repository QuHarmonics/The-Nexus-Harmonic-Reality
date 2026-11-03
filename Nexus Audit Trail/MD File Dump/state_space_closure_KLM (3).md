# State-Space Closure: Probes K, L, and M

Three independently defined observable classes test whether secondary
re-injection at $t = k + 16$ produces any detectable second wave in SHA-256
state space.  The claims marked **[FORCED]** follow directly from the computed
numbers and are not interpretive.

---

## Probe K — Cumulative New-Bit Support

### Metric

Let $M_k(r)$ denote the 256-bit XOR mask between the reference and perturbed
state after round $r$, averaged over 32 single-bit probes within source word
$k$.  Define the cumulative new-bit count at round $r$ as

$$
N_k(r) = \mathrm{HW}\!\left( M_k(r) \;\wedge\; \neg \bigvee_{t < r} M_k(t) \right)
$$

that is, the number of bits active in $M_k(r)$ that have never appeared in
any prior mask for word $k$.  The signal-to-noise ratio for the secondary
window is

$$
\mathrm{SNR}_K(k) =
\frac{\displaystyle\operatorname{mean}_{r \,\in\, [k+15,\; k+21]} N_k(r)}
     {\displaystyle\operatorname{mean}_{r \,\in\, [k+6,\; k+14]}  N_k(r)}
$$

### Results

| Word | base\_mean | sec\_mean | $\mathrm{SNR}_K$ |
|------|----------:|----------:|----------------:|
| W[0]  | 4.7291666667 | 0.0133928571 | 0.0028319698 |
| W[1]  | 4.5590277778 | 0.0089285714 | 0.0019584376 |
| W[2]  | 5.0000000000 | 0.0044642857 | 0.0008928571 |
| W[3]  | 4.4687500000 | 0.0133928571 | 0.0029970030 |
| W[4]  | 4.4826388889 | 0.0044642857 | 0.0009959057 |
| W[5]  | 4.2812500000 | 0.0223214286 | 0.0052137643 |
| W[6]  | 4.9930555556 | 0.0446428571 | 0.0089409895 |
| W[7]  | 4.1631944444 | 0.0089285714 | 0.0021446443 |
| W[8]  | 4.4791666667 | 0.0044642857 | 0.0009966777 |
| W[9]  | 4.6076388889 | 0.0223214286 | 0.0048444397 |
| W[10] | 4.4409722222 | 0.0223214286 | 0.0050262482 |
| W[11] | 4.3715277778 | 0.0357142857 | 0.0081697492 |
| W[12] | 4.6250000000 | **0.0000000000** | **0.0000000000** |
| W[13] | 4.8506944444 | **0.0000000000** | **0.0000000000** |
| W[14] | 4.8958333333 | 0.0401785714 | 0.0082066869 |
| W[15] | 4.4756944444 | 0.0178571429 | 0.0039898038 |

$$
\overline{\mathrm{SNR}}_K = 0.0035755736 \qquad \max_k \mathrm{SNR}_K(k) = 0.0089409895
$$

### W[12] and W[13] floating-point zero audit

The secondary-window values for W[12] and W[13] printed as `0.0000` in the
earlier scan.  A per-round inspection confirms this is not a display artifact:
every individual round value $N_k(r)$ in the secondary window for W[12]
(rounds 27–33) and W[13] (rounds 28–34) is exactly `0.0` in IEEE 754 float64
accumulation.

$$
N_{12}(r) = 0.0 \;\;\forall r \in [27, 33], \qquad
N_{13}(r) = 0.0 \;\;\forall r \in [28, 34]
$$

These two words lie in the $P = 3$ path-multiplicity regime.  The exact zeros
are consistent with the saturation picture: the support manifold for W[12] and
W[13] is fully exhausted before round 27. **[FORCED: literal float64 zeros,
confirmed per-round]**

### Verdict

**[FORCED]** The cumulative new-bit rate collapses to effectively zero before
the secondary window for every input word without exception.  The reachable
support manifold is exhausted by the primary injection wave.  Secondary
re-injection at $t = k + 16$ does not open a second support-expansion front.

---

## Probe L — Amplitude Inside Support

### Metrics

Let windows be defined as before: baseline $r \in [k+6, k+14]$, secondary
$r \in [k+15, k+21]$.  Define secondary/baseline ratios:

$$
R_{\mathrm{active}}(k) =
\frac{\displaystyle\operatorname{mean}_{r \,\in\, [k+15,\; k+21]} \mathrm{HW}\!\bigl(M_k(r)\bigr)}
     {\displaystyle\operatorname{mean}_{r \,\in\, [k+6,\; k+14]}  \mathrm{HW}\!\bigl(M_k(r)\bigr)}
$$

$$
R_{\mathrm{toggle}}(k) =
\frac{\displaystyle\operatorname{mean}_{r \,\in\, [k+15,\; k+21]} \mathrm{HW}\!\bigl(M_k(r) \oplus M_k(r-1)\bigr)}
     {\displaystyle\operatorname{mean}_{r \,\in\, [k+6,\; k+14]}  \mathrm{HW}\!\bigl(M_k(r) \oplus M_k(r-1)\bigr)}
$$

$$
R_{\mathrm{overlap}}(k) =
\frac{\displaystyle\operatorname{mean}_{r \,\in\, [k+15,\; k+21]} \mathrm{HW}\!\bigl(M_k(r) \wedge M_k(r-1)\bigr)}
     {\displaystyle\operatorname{mean}_{r \,\in\, [k+6,\; k+14]}  \mathrm{HW}\!\bigl(M_k(r) \wedge M_k(r-1)\bigr)}
$$

$$
R_{\mathrm{new}}(k) = \mathrm{SNR}_K(k) \quad \text{(same accumulation as Probe K)}
$$

### Significance tests for overlap dips

The word-level aggregate ratio $R_\text{overlap}$ uses 32 single-bit probes
per word, averaged together.  The natural sample unit for significance testing
is the 32 individual per-bit overlap ratios within each word, denoted
$\rho_{k,b}$ for $b \in \{0,\ldots,31\}$.  Two tests are applied to the three
previously flagged words W[9], W[12], W[13]:

**Step 1 — Bootstrap 95% CI** (4000 resamples, percentile method) on the
per-bit mean $\bar\rho_k = \frac{1}{32}\sum_b \rho_{k,b}$:

$$
\mathrm{CI}_{95}(k) = \bigl[\hat\theta_{\alpha/2}^*,\; \hat\theta_{1-\alpha/2}^*\bigr]
\quad \text{from } B = 4000 \text{ bootstrap replicates}
$$

**Step 2 — Permutation test** (10 000 permutations, one-sided,
$H_1$: $\bar\rho_k < \bar\rho_\text{pool}$) pooling the 32 per-bit ratios
from each flagged word against $13 \times 32 = 416$ per-bit ratios from the
remaining 13 words.

### Results

| Word | $R_\text{active}$ | $R_\text{toggle}$ | $R_\text{overlap}$ | $R_\text{new}$ |
|------|------------------:|------------------:|-------------------:|---------------:|
| W[0]  | 1.013708 | 1.010999 | 1.017772 | 0.002832 |
| W[1]  | 0.977335 | 0.974487 | 0.980434 | 0.001958 |
| W[2]  | 1.010478 | 1.011747 | 1.012451 | 0.000893 |
| W[3]  | 1.005402 | 0.988614 | 1.017149 | 0.002997 |
| W[4]  | 0.998316 | 0.985289 | 1.012928 | 0.000996 |
| W[5]  | 0.993599 | 1.002477 | 0.990250 | 0.005214 |
| W[6]  | 0.999551 | 1.004526 | 0.993313 | 0.008941 |
| W[7]  | 0.980625 | 0.989616 | 0.970536 | 0.002145 |
| W[8]  | 1.011131 | 1.009389 | 1.013780 | 0.000997 |
| W[9]  | 0.990132 | 1.013312 | 0.962814 | 0.004844 |
| W[10] | 0.990328 | 1.003060 | 0.976947 | 0.005026 |
| W[11] | 1.006199 | 1.004352 | 1.009769 | 0.008170 |
| W[12] | 0.985817 | 1.002880 | 0.971622 | 0.000000 |
| W[13] | 0.991645 | 1.016587 | 0.973507 | 0.000000 |
| W[14] | 1.008484 | 0.991457 | 1.029780 | 0.008207 |
| W[15] | 1.003619 | 1.006269 | 0.998255 | 0.003990 |

$$
\overline{R}_{\mathrm{active}} = 0.9979, \quad
\overline{R}_{\mathrm{toggle}} = 1.0009, \quad
\overline{R}_{\mathrm{overlap}} = 0.9957, \quad
\overline{R}_{\mathrm{new}} = 0.0036
$$

Per-bit significance results for the flagged words:

| Word | $\bar\rho_k$ | Bootstrap 95% CI | perm $p$ (one-sided) | verdict |
|------|-------------:|:----------------|---------------------:|:--------|
| W[9]  | 0.9687 | [0.9332, 1.0055] | 0.042 | **p < 0.05** |
| W[12] | 0.9801 | [0.9375, 1.0259] | 0.107 | ns |
| W[13] | 0.9817 | [0.9320, 1.0324] | 0.125 | ns |

Grand mean across all 512 bits: $\bar\rho_\text{grand} = 1.003$.

### Verdict

The W[9] overlap dip is statistically distinguishable from the pool at the
per-bit level (permutation $p = 0.042$); W[12] and W[13] are not
($p > 0.10$).  No bootstrap CI excludes the grand mean.

Critically, the word-level overlap ratio for W[9] is $R_\text{overlap}(9) =
0.963$, still within 4% of unity.  The permutation significance indicates that
W[9] undergoes a real but very small reduction in mask-to-mask overlap in the
secondary window.  This is a within-saturation modulation effect.  It does not
constitute a second amplitude wave: $R_\text{active}$, $R_\text{toggle}$, and
$R_\text{new}$ for W[9] are all within 1.5% of 1.0.

---

## Probe M — Phase-Selective Support Echo

### Metrics

For each source word $k$ and lag $L$, compute the mean Jaccard and cosine
similarity between the round-$r$ mask and the round-$(r+L)$ mask:

$$
J_k(L) = \operatorname{mean}_{r=0}^{63-L}
          \frac{\bigl|M_k(r) \wedge M_k(r+L)\bigr|}
               {\bigl|M_k(r) \vee  M_k(r+L)\bigr|}
$$

$$
C_k(L) = \operatorname{mean}_{r=0}^{63-L}
          \frac{\bigl|M_k(r) \wedge M_k(r+L)\bigr|}
               {\sqrt{\mathrm{HW}(M_k(r)) \cdot \mathrm{HW}(M_k(r+L))}}
$$

Lags $L \in \{10, 11, \ldots, 24\}$.

### Control design

The mask similarity profile is monotone-decreasing in $L$.  Consequently
$J_k(16) > \operatorname{mean}_{L \neq 16} J_k(L)$ trivially when the control
set includes lags $L > 16$.  A global-mean control confounds lag-16 resonance
with monotone decay and is not used as the primary test.

The correct null test uses the local adjacent-lag interpolant:

$$
\Delta J_{16}^{\mathrm{local}}(k) = J_k(16) - \tfrac{1}{2}\bigl[J_k(15) + J_k(17)\bigr]
$$

A genuine phase echo at period 16 would appear as a systematic positive
deviation in $\Delta J_{16}^{\mathrm{local}}$ across words and produce peaks
at $L = 16$ in the per-word argmax.

### Results

| Word | $J_\text{peak}$ | $J_k(15)$ | $J_k(16)$ | $J_k(17)$ | $\Delta J_{16}^\text{local}$ | $\Delta C_{16}^\text{local}$ |
|:----:|:-:|----------:|----------:|----------:|-----------------------------:|-----------------------------:|
| W[0]  | 11 | 0.3170783 | 0.3168038 | 0.3185732 | −0.0010219 | −0.0010656 |
| W[1]  | 10 | 0.3099951 | 0.3102901 | 0.3063069 | +0.0021391 | +0.0025683 |
| W[2]  | 10 | 0.3019286 | 0.3035361 | 0.3019619 | +0.0015908 | +0.0017003 |
| W[3]  | 10 | 0.2954626 | 0.2958664 | 0.2939559 | +0.0011571 | +0.0014294 |
| W[4]  | 11 | 0.2852572 | 0.2860522 | 0.2833274 | +0.0017599 | +0.0016062 |
| W[5]  | 11 | 0.2816563 | 0.2799083 | 0.2833408 | −0.0025903 | −0.0029449 |
| W[6]  | 10 | 0.2756262 | 0.2764559 | 0.2741520 | +0.0015667 | +0.0021291 |
| W[7]  | 10 | 0.2697998 | 0.2688620 | 0.2687274 | −0.0004016 | −0.0004579 |
| W[8]  | 11 | 0.2623664 | 0.2640145 | 0.2620395 | +0.0018116 | +0.0023539 |
| W[9]  | 10 | 0.2545209 | 0.2546108 | 0.2522783 | +0.0012112 | +0.0011229 |
| W[10] | 10 | 0.2500787 | 0.2468612 | 0.2442627 | −0.0003095 | −0.0006488 |
| W[11] | 10 | 0.2411822 | 0.2383952 | 0.2379343 | −0.0011630 | −0.0011885 |
| W[12] | 11 | 0.2338693 | 0.2323601 | 0.2274270 | +0.0017119 | +0.0018302 |
| W[13] | 10 | 0.2284903 | 0.2266245 | 0.2260826 | −0.0006620 | −0.0009671 |
| W[14] | 10 | 0.2221347 | 0.2211963 | 0.2171356 | +0.0015612 | +0.0019226 |
| W[15] | 10 | 0.2134383 | 0.2120865 | 0.2100584 | +0.0003382 | +0.0004844 |

$$
\overline{\Delta J_{16}^{\mathrm{local}}} = +0.000544, \quad
\hat\sigma_{\Delta J} = 0.001353, \quad
\text{mean/std ratio} = 0.40
$$

$$
\text{words peaking at } L = 16: \quad 0\,/\,16
$$

The global-mean control gives $\overline{\Delta J_{16}^{\mathrm{global}}} =
+0.00279$, but this is a monotone-decay artifact and is retained only for
reference.

### Verdict

**[FORCED]** No phase-locked support echo at lag 16.  The local-control mean
advantage ($+5.4 \times 10^{-4}$) is well within one standard deviation across
words ($1.35 \times 10^{-3}$), indicating no systematic lag-16 elevation above
the monotone-decay baseline.  The similarity profile peaks at lags 10–11 for
all 16 words; lag 16 is the argmax for 0 out of 16 words.

---

## Combined State-Space Closure

| Probe | Class | Primary statistic | Result | Status |
|:------|:------|:-----------------:|-------:|:-------|
| K | Support-growth | $\overline{\mathrm{SNR}}_K$ | $0.0036$ | **NULL** [FORCED] |
| K | W[12], W[13] | $N_k(r)$ per round | $0.0$ (float64 exact) | **NULL** [FORCED] |
| L | $R_\text{active/toggle/overlap}$ | word-level means | $\approx 1.000$ | **NULL** |
| L | W[9] overlap dip | per-bit perm. test | $p = 0.042$ | **sig., not a wave** |
| L | W[12], W[13] dips | per-bit perm. test | $p > 0.10$ | not significant |
| M | Phase-echo | $\overline{\Delta J_{16}^\text{local}}$ | $+5.4\times10^{-4} < \hat\sigma$ | **NULL** [FORCED] |

The W[9] permutation result ($p = 0.042$) is the only significant finding in
Probe L.  It indicates a real but small reduction in round-to-round mask
overlap during the secondary window, with word-level ratio
$R_\text{overlap}(9) = 0.963$ and all other metrics for W[9] within 1–2% of
unity.  This is a within-saturation modulation effect and does not weaken the
K or M nulls.

The joint conclusion is:

> Secondary re-injection at $t = k+16$ is algebraically certain in schedule
> space — Probe N measures $\mathbb{E}[\mathrm{HW}(\Delta W[k+16])] \approx
> 4.910$ bits.  Under all three observable classes defined here it produces no
> second support-expansion front, no second amplitude wave, and no phase-locked
> mask resonance in state space.

The remaining open object is the projection law

$$
\Delta W[t] \;\longrightarrow\; \Delta S[r]
$$

and the criterion separating schedule-space echoes that are support-forming
from those that are state-subcritical after primary saturation.
