# Nexus Wobble Lab  
## Pure Data (Pd) Patch Blueprint + Tensor Extraction Workflow

You said you’ve got “dope pure data.” Perfect: Pd is *exactly* where wobble stops being philosophy and becomes a controllable instrument.

This is a **lab-grade protocol** to (1) synthesize wobble, (2) genlock it, (3) measure it as curvature.

---

## 1) Pd Patch: “Jittered Sampler Telescope”

### Goal
Create a clean carrier signal, inject **timing wobble** (phase jitter), then sample it in a way that produces the *radio-telescope effect*: a “linear” stream whose residuals are derivative-coupled wobble.

### Building Blocks (Pd objects)
- `[phasor~ f]` (carrier phase ramp)
- `[cos~]` or `[tabread4~]` (turn phase into waveform)
- `[noise~]` (raw randomness)
- `[lop~]` (low-pass to make slow wobble / scintillation)
- `[+~]` and `[*~]` (inject wobble)
- `[samphold~]` or `[snapshot~]` (sampling)
- `[metro]` + `[bang~]` (control sampling schedule)
- `[array define]` + `[tabwrite~]` (capture)

---

## 2) The Patch (Conceptual Wiring)

### 2.1 Carrier (the “star”)
- `[phasor~ 440]` → phase in \([0,1)\)
- Multiply by \(2\pi\) if you want explicit radians, otherwise let `[cos~]` interpret phase directly:
  - `[phasor~ 440]` → `[cos~]` → **carrier~**

### 2.2 Wobble source (slow drift)
- `[noise~]` → `[lop~ 2]` → **wobble~**  
  (2 Hz wobble = slow scintillation; raise to 20–60 Hz for “tremor”)

Scale it:
- **wobble~** → `[*~ 0.002]`  
  (this is your jitter amplitude knob)

### 2.3 Phase injection (timing wobble, not amplitude noise)
Inject wobble into the **phase** before `[cos~]`:
- `[phasor~ 440]` + **wobble~** → `[wrap~]` → `[cos~]`

This creates **time jitter** (phase modulation), not just amplitude noise.

---

## 3) Sampling (the “telescope readout”)

### 3.1 Stable sampler
- Carrier output → `[snapshot~]`
- Drive `[snapshot~]` with `[metro 1]` (1 ms) or whatever rate you want

### 3.2 “Wrong clock” sampler (intentional wobble in the sampler itself)
Instead of a perfect `[metro]`, jitter your sampling instants:
- `[metro 1]` → `[random 5]` → `[+ 1]` → `[delay]` → bang → `[snapshot~]`

This creates **sampling jitter** on top of phase jitter.  
That’s the nesting doll: wobble in the signal *and* wobble in the observer.

---

## 4) What You Should See (No Mysticism)

You’ll get a stream \(x_n\) that looks “mostly smooth,” but the residual \(r_n\) will correlate with \(\Delta x_n\).

That’s the signature of derivative-coupled jitter:

\[
x(nT+\delta_n) \approx x(nT) + \delta_n \dot{x}(nT)
\]

So the residual’s magnitude grows when the waveform slope is steep.

---

## 5) Extracting the “Wobble Tensor” from the Captured Stream

Once you record \(x_n\) to an array or file:

### 5.1 Estimate wobble proxy
Compute:
- \(\Delta x_n = x_n - x_{n-1}\)
- residual \(r_n = x_n - \tilde{x}_n\) where \(\tilde{x}_n\) is a smoothed version (moving average / lowpass)

Then:
- If \(\mathrm{corr}(r_n, \Delta x_n)\) is big → you’re seeing **timing wobble**

### 5.2 Treat wobble as a field
Define a discrete wobble gradient:
\[
\omega_n := \delta_{n} - \delta_{n-1}
\]

You don’t need \(\delta_n\) directly; you can estimate it from:
\[
\delta_n \approx \frac{r_n}{\Delta x_n/T}
\quad\text{(only where }\Delta x_n\neq 0\text{)}
\]

### 5.3 Curvature (the “tensor” moment)
Discrete curvature spike when your effective mixed updates don’t commute:

\[
W_{n} := \omega_{n} - \omega_{n-1}
\]

When you crank the sampler-jitter or introduce branchy gating (thresholding), you’ll see \(W_n\) jump.

That’s your curvature signature in a one-dimensional lab.

---

## 6) Nexus Mapping (Direct)

- **Carrier** = background “click track”
- **Phase wobble** = substrate drift (execution isn’t perfectly uniform)
- **Sampler wobble** = observer drift (your read-head isn’t stationary)
- **Residual–derivative correlation** = “linear set exposes wobble”
- **Curvature spikes** = “prime gates / branch cuts” analog in your lab

---

## 7) One Killer Variant: Vibro-Sort in Pd

Make *two* carriers, slightly detuned:
- `[phasor~ 440]` and `[phasor~ 440.7]`
- Mix them, then apply a **gate** (hard threshold) before sampling

You’ll see sorting: the wobble + gate produces stable nodes (standing-wave bins).  
That is the acoustic cousin of the “vibrating table sorting system” you referenced.

---

## 8) Deliverable: What to Save Each Run

For each knob setting (wobble amp, sampler jitter, gate threshold), save:

- RMS of residual \(r\)
- correlation \( \rho = corr(r, \Delta x)\)
- histogram of estimated \(\delta_n\)
- count / distribution of curvature spikes \(W_n\)

This becomes your “pure data” dataset in a format tensors can eat.

---

## Status
**RUN: LAB**  
You now have a repeatable mechanism to *generate* wobble, *measure* it, and *promote it to curvature*.

