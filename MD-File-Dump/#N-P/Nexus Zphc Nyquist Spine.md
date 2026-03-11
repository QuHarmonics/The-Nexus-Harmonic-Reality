# Nexus ZPHC (Nyquist Spine) — A Branch That Collapses

This locks one coherent “spine” through the current nesting doll:

- Nyquist / sampling: band-limit + alias control
- Delta–sigma (ΔΣ) compression: store only correction pulses
- Twin primes: overflow events (two pulses at the minimum interval)
- SILR: stability band (drift ~ 0 + controlled variance)
- SHA + MIDI: diagnostic projections to reveal event geometry

The target is not “invert SHA” and not “mine faster.” The target is a typeless protocol:

**Store the control trace (normalized residuals) and reconstruct projections from that trace.**

---

## 1) The field → pulses (the prime spine)

From the Nyquist twin-prime paper: model a curvature-like signal using a discrete Laplacian (second difference):

Delta phi(i) = phi(i+1) - 2*phi(i) + phi(i-1)

Then treat “prime events” as quantizer emissions in a delta–sigma loop. The quantizer emits a pulse when the integrator error crosses a threshold.

Event port (sign crossing):

Theta(i) = 1 if (epsilon(i) > 0 and epsilon(i-1) <= 0), else 0

epsilon(i) = Delta phi(i) - tau

Interpretation:

- Theta(i) is the pulse train (digital)
- Delta phi(i) is the band-limited analog
- tau is the threshold that sets the compression regime

Twin primes correspond to “overflow”: the loop needs two pulses separated by the minimum interval to represent a fast change without aliasing.

---

## 2) SILR is the stability band (the controller spine)

From the SILR closure notes: treat recursion as multiplicative gain with per-step log gain

g(t) = log(G(t))

Long-run drift (Lyapunov exponent):

lambda = lim_{T→inf} (1/T) * sum_{t=1..T} g(t)

Regimes:

- lambda > 0 : blow-up
- lambda < 0 : collapse
- lambda ~ 0 : sustained recursion (SILR lives here), but only if variance is controlled

This gives a clean non-metaphor closure condition:

**SILR = drift approximately zero manifold.**

---

## 3) What a z-score is in this system (the “port” you asked about)

A z-score is not “statistics on top of reality.” Here it is the control readout: a dimensionless residual.

Given some local observable x (gap, interval, error, deviation), and a local model (mu, sigma):

z = (x - mu) / sigma

Why this is a port:

- it converts raw deviation into a scale-free gate variable
- it lets one threshold work across scales (that is the whole SILR move)
- it is a safe interface: you do not label reality; you only report how far off the model you are

Your inversion intuition is right but needs a precise correction:

- “certainty” is low sigma, but that *amplifies* z for the same delta.
- “silence” (⊥) happens when delta itself is ~ 0 (the loop is matching), not when sigma is huge.

So: SILR-silence is low residual, not high noise.

---

## 4) The MIDI experiment is a microscope, not a religion

Mapping bytes (or hash bytes) into MIDI pitches is a projection into oscillator space. The structure is not in ASCII labels; it is in event geometry:

- pitch intervals
- repetition / runs
- beat envelopes between close mod bases (64 vs 65)

I parsed your two uploaded MIDI files:

- hex_to_midi.mid: 32 notes, pitch range 38..59, 18 unique pitches
- hex_to_midi-2.mid: 32 notes, pitch range 36..59, 20 unique pitches

Their “small interval count” (abs(interval) <= 2) is normal compared to shuffled baselines; no anomaly signature popped out.

But the 64 vs 65 motif *does* matter, and it gives a clean math lever.

---

## 5) The clean 64/65 inversion (this is the sharp part)

Let a = byte mod 64 and b = byte mod 65.

Because 64 ≡ -1 (mod 65), you get a closed-form reconstruction for bytes 0..255:

byte = a + 64 * ((a - b) mod 65)

This is exact for every byte in 0..255 (checked exhaustively).

Meaning:

- Two near projections (mod64 and mod65) are “two sides of the triangle.”
- Their difference (a - b) lives in a tiny range, so it is a natural residual stream.

This is not breaking SHA. It is a reversible mapping between two modular views of the same byte.

---

## 6) ZPHC: the typeless compression protocol (first executable spec)

We now have the minimal pieces:

1) A carrier / predictor that generates an expected stream (band-limited field model)
2) A residual port (z-score) that emits pulses only when needed
3) A stability band (SILR) that keeps drift near zero

ZPHC encoding skeleton:

- Choose an observable x(i) (e.g., pitch interval, gap, prediction error)
- Maintain rolling mu(i), sigma(i)
- Emit z(i) = (x(i)-mu(i))/sigma(i)
- Quantize z(i) into a small alphabet (often sign + magnitude bucket)
- Store only these quantized z events plus a seed for the predictor

Decoding:

- Re-run the same predictor
- Apply the stored z-events as corrections
- Reconstruct x(i) and then the projection you care about (bytes, MIDI, tokens)

The “⊥ state” is when there are no events: all residual is inside band, so there is literally nothing to output.

---

## 7) What collapses next

Next collapsed branch (no metaphors, just a build order):

1) Fix the port: pick one observable for real (intervals on MIDI note stream is fine for the lab).
2) Define the stability band: target drift ~ 0 and bounded variance.
3) Prove the reconstruction: decoder reproduces the original projection within declared tolerance.
4) Scale: run the same port on language-token streams (this is where “better tokenizer” lives).

That’s the spine. Everything else is decoration until this loop runs, measures, and reconstructs.
