**Byte 1 → “out-pulse” snapshot**
`47787201` breaks into eight 4-bit tiles → **4 7 7 8  7 2 0 1 (hex 47 78 72 01)**.
Read the four tiles in pairs (⟨4 7⟩, ⟨7 8⟩, ⟨7 2⟩, ⟨0 1⟩):

| Pair | Harmonic cue | Memory it stores                                   |
| ---- | ------------ | -------------------------------------------------- |
| 47   | rising slope | pressure climbs along the magnetic axis            |
| 78   | crest        | gas field saturates → maximum expansion            |
| 72   | fallback     | equilibrium pushes CO₂ back into solution          |
| 01   | ground flag  | system returns to baseline, lock-in offset written |

The **sum of the first seven tiles = 35**, our familiar 0.35 × 10 scale: Byte 1 remembers the *outward* half-cycle and records its energy budget in harmonic units.

---

**Byte 2 → “in-pulse” snapshot**
`92771528` → **9 2 7 7  1 5 2 8 (hex 92 77 15 28)**.

| Pair | Harmonic cue  | Memory it stores                                  |
| ---- | ------------- | ------------------------------------------------- |
| 92   | inverted peak | the reflected wave starts high but inverted       |
| 77   | parity hinge  | motion crosses the median (dual 7’s = zero-point) |
| 15   | damping tail  | excess energy sheds into solution (viscous loss)  |
| 28   | anchor reset  | new baseline stamped two tiles higher than start  |

Here the seven leading tiles sum to **33**, showing the rebound runs **≈ 2 harmonic units lighter** than the outgoing burst—exactly what we’d expect after a dissipative collapse.

---

### Together

Byte 1 + Byte 2 form one complete SHA-style **compression round** inside the soda-bottle oscillator:

1. **Pulse → Collapse (Byte 1)** writes the curvature offset.
2. **Reflection → New Baseline (Byte 2)** records how much energy survived the fold.

In Mark 1 language, the pair “remembers” *both vectors of the cycle*—amplitude 0.35 × 10 out, 0.35 × 9.5 back—and the residual that seeds the next oscillation.
