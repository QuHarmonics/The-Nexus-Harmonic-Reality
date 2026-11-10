# NEXUS — Oversampled Transformation Path Audit

**Run date:** 2026-10-16  
**Purpose:** Replace round-endpoint observation with exact sub-transition observation and run the path forward and backward in the same experiment.

## What changed

The previous SHA run sampled the state at round boundaries. That is enough to verify round inversion when operands are known, but it is too coarse to represent the internal path through each multi-bit addition. The new run expands each 32-bit modular addition into its 32 bit/carry stages, and expands one BBP base-16 phase transition into four binary transitions.

This is an exact **symbolic microtrajectory**, not a measurement of a physical chip's analog voltage. Nyquist–Shannon applies to a defined band-limited signal and requires sampling above twice its highest frequency for ideal reconstruction; a discrete algorithm does not, by itself, define that physical signal. (Background: [CMU, Nyquist–Shannon sampling theorem](https://www.cs.cmu.edu/~15322/book/ch07/01.html).)

## Result A — BBP: one hexadecimal step unfolded into four binary steps

Initial lane phases:

\[
 x=\left(\frac79,\frac13,\frac3{13},\frac17\right),\qquad
 c=(4,-2,-1,-1).
\]

For every lane, each binary microstep is

\[
 2x_i=b_i+x_{i+1},\quad b_i\in\{0,1\},\quad
 x_{i+1}=\{2x_i\}.
\]

The output branch and residual are both retained; the exact inverse at each microstep is

\[
 x_i=\frac{b_i+x_{i+1}}2.
\]

The oversampled branch sequences (most-significant binary branch first) are:

| Lane start | Four branch bits | Base-16 digit | Final phase |
|---|---:|---:|---:|
| \(7/9\) | 1100 | 12 | \(4/9\) |
| \(1/3\) | 0101 | 5 | \(1/3\) |
| \(3/13\) | 0011 | 3 | \(9/13\) |
| \(1/7\) | 0010 | 2 | \(2/7\) |

Applying the four-channel coefficient vector to each binary substep produces the local weighted sequence

\[
 h=(4,2,-2,-3).
\]

The coarse base-16 readout is 33. Reconstructing that readout from the finer sequence gives

\[
 8(4)+4(2)+2(-2)+1(-3)=32+8-4-3=\boxed{33}.
\]

All 16 lane-level microstep inversions passed. This is a direct witness of the distinction at issue: the one-number readout 33 folds a four-step weighted path into one value. The finer branch/residual path can be checked forward and backward exactly; the scalar alone does not name the path.

### The sampling/aliasing witness: a six-state orbit seen as three states

For the single lane starting at \(x_0=7/9\), the binary phase update \(x_{n+1}=\{2x_n\}\) has the exact orbit

\[
rac79	orac59	orac19	orac29	orac49	orac89	orac79.
\]

Its period is six binary microsteps. A base-16 observation advances four binary microsteps at a time, because \(16=2^4\). That stride sees only

\[
rac79	orac49	orac19	orac79,
\]

which is a three-state observed orbit. It skips the intermediate states \(5/9\), \(2/9\), and \(8/9\). Every fine transition reverses exactly by \(x_n=(b_n+x_{n+1})/2\).

This is the first concrete sampling result relevant to your objection: **the coarse radix-16 view has a different apparent orbit because it samples every fourth point of the radix-2 path.** Oversampling exposes the missing phase states.

The same test's normalized discrete Fourier magnitudes change from the six-bin fine-orbit spectrum

\[
(0.500000,\ 0.192450,\ 0,\ 0.055556,\ 0,\ 0.192450)
\]

to the three-bin stride-4 spectrum

\[
(0.444444,\ 0.192450,\ 0.192450).
\]

The original orbit has nonzero components at signed frequencies \(\pm1/6\) and \(-1/2\) cycles per binary microstep. The stride-4 sampling rate is \(1/4\) sample per microstep, so its Nyquist boundary is \(\pm1/8\). The \(\pm1/6\) components fold into \(\mp1/12\); the \(-1/2\) component folds into DC and changes the DC magnitude from 0.5 to 0.444444. This is spectral aliasing in the declared finite periodic sequence—not a physical voltage measurement.

The period law also holds across **48 odd denominators from 3 through 97**. For a reduced phase \(r/d\) with odd \(d\), the binary orbit period is \(n=\operatorname{ord}_d(2)\). Sampling every four binary steps uses \(T_{16}=T_2^4\), whose period is exactly

\[
oxed{\operatorname{ord}_d(16)=rac{\operatorname{ord}_d(2)}{\gcd(\operatorname{ord}_d(2),4)}}.
\]

Every one of the 48 exact modular-order checks passed. Examples: denominator 13 has periods 12→3 (nine states omitted); denominator 37 has 36→9 (27 omitted); denominator 97 has 48→12 (36 omitted). For denominator 7, the order is 3 and no states are omitted by the stride, so oversampling does not universally shrink every orbit; the effect is constrained by the orbit period.

[View the phase-orbit comparison](sandbox:/mnt/data/NEXUS_BBP_phase_oversampling.png) · [View the aliased spectrum](sandbox:/mnt/data/NEXUS_BBP_aliased_spectrum.png)

## Result B — SHA-256: sample inside every modular addition

A 32-bit addition was expanded from one word-level operation into 32 least-significant-bit-to-most-significant-bit stages. At each stage the audit records the two operand bits, incoming carry, sum bit, and outgoing carry. Each stage was checked against the local full-adder relation, and the carry profile was reconstructed from the operands and sum bits.

The test corpus and outcomes:

| Measurement | Result |
|---|---:|
| Messages | 54 |
| Compression blocks | 207 |
| Independent `hashlib` matches | 54/54 |
| Schedule words reconstructed from schedule tails | 13,248 |
| SHA rounds run forward | 13,248 |
| SHA rounds reversed and checked | 13,248 |
| Individual 32-bit modular additions expanded | 122,544 |
| Bit-position carry samples | 3,921,408 |
| Carry transitions observed | 954,761 |
| Round-end samples, if observing only the 64 round endpoints per block | 13,248 |

That is 296 bit-carry samples for every single round-end sample, once schedule expansion and the seven additions used per round are included in the defined microstep count. All digest checks, schedule reconstructions, local carry relations, and round-level reverse checks passed.

## What the experiment establishes

1. Endpoint-only round sampling hides the bit-position carry trajectories inside modular additions.
2. A finer symbolic observation makes those local transitions explicit and permits exact forward/reverse checks when the operands and round context are known.
3. The BBP example provides a compact shared handle: branch plus residual at each microstep; a weighted final readout folds the path.
4. SHA and BBP are **not thereby proved to be the same dynamical system**. The tested correspondence is narrower: both have a fine-grained transition path, local state, a branch/carry-like distinction, and a coarser readout that can hide path detail.

## What it does not establish yet

- This is not a physical electrical waveform capture. That would require a specified hardware implementation and an instrumented timing/power/voltage measurement.
- The Nyquist–Shannon theorem has not been applied to SHA's abstract code. We have not defined a continuous band-limited signal or its bandwidth.
- Sampling more internal variables does not automatically yield a minimal root observer. The SHA test still has known operands and source-derived schedule information; it does not invert a digest alone.
- The original open question remains: can the root observer derive the needed return coordinate from the transformation grammar and a strictly smaller residual, instead of retaining a recoding of the source?

## Files

- `nexus_oversampled_waveform_audit.py` — executable standard-library audit.
- `nexus_oversampled_waveform_results.json` — machine-readable result.
- `nexus_oversampled_waveform_run.txt` — captured run output.

## Ledger

**BBP fourfold binary unfolding and exact return:** RUNS.  
**SHA 32-bit-addition microtrajectory and local reverse checks:** RUNS.  
**SHA digest-only inverse:** OPEN/NOT ESTABLISHED.  
**Physical waveform / literal Nyquist sampling claim:** NOT TESTED; it requires a defined physical or continuous signal model.
