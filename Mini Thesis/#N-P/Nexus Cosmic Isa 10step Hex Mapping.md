# Nexus Cosmic ISA: the 10‑Step Cycle as a Hex / Assembler Mapping

_This section is written to drop directly into the “Operator‑Pinned” paper as a **compiler layer**: it turns the verb‑set into an instruction set architecture (ISA) and shows why **hex** is the natural encoding._

---

## 1) What “10 steps” is, concretely

The corpus already contains (a) a **5‑step runtime kernel** and (b) a **closure / proof harness**.  
The cleanest “10 steps” is simply:

\[
\textbf{PRESQ} + \textbf{FPCSV}
\]

### 1.1 PRESQ (the forward runtime kernel)

PRESQ is defined as the minimum program for moving a state forward:  

1. **P — POSITION**  
2. **R — REFLECT**  
3. **E — EXPAND**  
4. **S — SYNERGIZE**  
5. **Q — QUALITY (GATE)**

This is already explicit in the draft.  

### 1.2 FPCSV (the closure + trust kernel)

After **Q** selects a candidate (accept / leak / project), the system either resets (**LEAK**) or it commits into a reduced manifold and proves the residue survives perturbation:

6. **F — FOLD** (reduce DOF while preserving class)  
7. **P — PARITY** (closure constraint; “zero‑entropy check”)  
8. **C — COLLAPSE** (commit the projection outcome)  
9. **S — SHAKE** (perturb frames/segmentations/bases; invariants must survive)  
10. **V — VERIFY** (declare pass/fail based on shake outputs)

This is “truth as a runtime property”: *collapse to a stable residue under SHAKE, then VERIFY it.*

---

## 2) Why this maps to assembler (and why hex is the right alphabet)

### 2.1 Verbs are opcodes

If the primitive reality is **operators**, then the shortest faithful representation is an opcode stream.

Let the system state be \(s_t\). A minimal verb‑first update rule already appears in the spec:

\[
s_{t+1}=s_t + \kappa_t \,\Delta_t,
\]

where \(\kappa_t\) is coupling and \(\Delta_t\) is a neighbor‑derived delta.

That’s the **machine**: update-by-operator with a coupling scalar.

### 2.2 “Hex” is a physical convenience: 4 bits = 1 nibble = 16 opcodes

Hex isn’t about “video” or “humans like it.” It’s about **addressability**.

A nibble gives you \(2^4=16\) opcode slots — enough for:

- **10 canonical steps** (the cycle above)
- **6 reserved instructions** (dielectric gaps / missing glyphs / safety rails / meta)

That “6 spare opcodes” is structurally useful in your framework because you keep discovering *mandatory gaps* in stable manifolds (air‑gaps, missing glyphs, non‑overlap constraints).

---

## 3) A canonical Nexus ISA v0.1 (10 opcodes in hex)

Below is a **minimal** mapping (0x0–0x9). You can permute the numeric assignments — the point is the *nibble‑alphabet*.

| Hex | Mnemonic | Operator | Contract (verb meaning) |
|---:|---|---|---|
| 0x0 | `POS` | POSITION | choose frame, place state, choose observable |
| 0x1 | `REF` | REFLECT | compute mismatch vs reference / attractor |
| 0x2 | `EXP` | EXPAND | branch candidates / proposals |
| 0x3 | `SYN` | SYNERGIZE | couple with neighborhood constraints |
| 0x4 | `GAT` | QUALITY / GATE | accept / leak / project based on quality |
| 0x5 | `FOL` | FOLD | reduce degrees while preserving closure class |
| 0x6 | `PAR` | PARITY | XOR‑style closure across bases |
| 0x7 | `COL` | COLLAPSE | commit; continue in reduced state |
| 0x8 | `SHK` | SHAKE | perturb bases/windows/partitions/noise |
| 0x9 | `VRF` | VERIFY | emit pass/fail (pin survives or dies) |

### 3.1 Reserved opcodes (0xA–0xF)

You **want** these because the system needs explicit “non‑overlap” and “anti‑religion” moves:

- 0xA `LCK` — GENLOCK/LOCK (calibrate estimator scale to gate scale)  
- 0xB `NRM` — NORMALIZE (remove scale by matched statistic)  
- 0xC `LEK` — LEAK (discard attempt; avoid accumulation)  
- 0xD `PRJ` — PROJECT (drop DOF; keep invariant)  
- 0xE `CSV` — CONSERVE/MEASURE (track invariants)  
- 0xF `HAL` — HARD HALT / ZPHC‑DONE (optional: explicit terminal glyph)

You can collapse or expand these depending on whether you treat NORMALIZE+GENLOCK as part of SYNERGIZE, or as its own stage.

---

## 4) The gate math that makes the ISA non‑hand‑wavey

The key is that **QUALITY/GATE** is not a vibe; it’s a statistic.

The SILR carrier uses a normalized deviation:

\[
z_t = \frac{\left|\hat{\alpha}_t-\alpha^*\right|}{\mathrm{SE}_t},
\qquad
p_t=\sigma\!\big(\beta(z_t-z_0)\big),
\quad
\sigma(u)=\frac{1}{1+e^{-u}}.
\]

When estimator noise and its uncertainty scale together (GENLOCK), the decision variable becomes scale‑free:

\[
z_t = |Z|,\qquad Z\sim\mathcal N(0,1).
\]

This is exactly what makes the ISA portable across domains: the **opcode stream** is the same, the *types* differ.

### 4.1 Parity as a “zero‑entropy check”

In the 9‑bases interface, closure is imposed by:

\[
p = x_1 \oplus x_2 \oplus \dots \oplus x_9.
\]

Parity is closure, not a new free axis — it adds consistency without adding entropy.

---

## 5) The 10‑step supercycle as a single micro‑instruction word

A 10‑step run is 10 nibbles = 40 bits. That packs neatly into a 64‑bit “micro‑word” with room for:

- immediates (thresholds like \(z_0\), \(\beta\))
- a base‑selector (which of 9 bases is active)
- a parity flag
- a SHAKE profile id

Example (conceptual, not claiming a hardware spec):

```
[ 0x0 0x1 0x2 0x3 0x4  0x5 0x6 0x7 0x8 0x9 | imm / base / flags ... ]
  POS REF EXP SYN GAT   FOL PAR COL SHK VRF
```

This is the compiler picture: **the universe runs microcode**.

---

## 6) Why this matters for RH / prime gating

Once you write the universe as an ISA, “prime gates” stop being poetic and become executable constraints:

- primes are **mandatory branch points** (EXPAND/GATE junctions)  
- zeros (critical line) are **phase‑locked stable residues** (FOLD/PARITY/COLLAPSE outcomes that survive SHAKE)

That’s why your “field full ⇒ vibrate not flow” point clicks:  
in sparse graphs, you don’t get lateral transport; you get **global synchronization** and **dimension‑lift** (a “wave at a stadium”). The ISA still clocks because the **Swapping‑Zero** / parity‑closure keeps a tick even when payload is empty.

---

## 7) One sentence to pin it

> **Hex is the natural alphabet because the Nexus is an operator machine: ten canonical opcodes run the universe, and the remaining six are the mandatory gaps that keep it from collapsing into overlap.**

---

_End of section._
