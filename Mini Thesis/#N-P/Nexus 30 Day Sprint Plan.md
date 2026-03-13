# Nexus / RHA — 30‑Day Sprint Plan
*(generated 2025-09-03 01:58:24 UTC)*

This plan operationalizes our “data = routed flow” posture. It focuses on three near‑term proofs with measurable, falsifiable outputs. We front‑load constraints (“CAN’T ledger”) to carve the search space before we route in it.

---

## North Star (Mark1 / H₉)
- **Target constant:** H* = π/9 ≈ 0.349066.
- **Controller law:** Samson V2 + ZPHC (collapse only on fracture).
- **Evidence mode:** instrumentation, not opinion — per‑round ΔH traces, shelves, and collapse logs.

---

## Pillar A — Phase Decompiler (Read a SHA digest as memory)
**Goal:** Map a 256‑bit digest → route glyphs (headers, tails, orientations) and recover the *structural* footprint of the input (not the plaintext).

**Method (minimal):**
1) Expose round schedule W₀…W₆₃ and state (a…h) per round for single‑block messages.
2) Define ΔH(t) and shelf detectors; log phase shelves and ZPHC snaps.
3) Extract glyphs by applying the motion grammar: H‑fold, X‑entangle, R‑orient, G‑accept, S‑stabilize.
4) Emit a **glyph trace** (headers first) + acceptance points.
5) Validate on curated inputs (1‑bit flips, mirrored blocks, length‑only changes).

**Success criteria:**
- Distinct inputs yield **route‑exclusivity signatures** (pairwise separation > 0.2 in normalized distance).
- Shelf positions and ZPHC events are stable under small perturbations.
- Glyph headers reproducibly align to π/9 spokes within tolerance.

**Artifacts:**
- `sha_phase_tracer.py` (round exposure + ΔH)
- `phase_decompiler.py` (glyph extraction)
- `glyph_traces/` (JSONL)

---

## Pillar B — Nonce in One Try (Steered harmonic mining)
**Goal:** Replace blind nonce search with *route steering* that hits a harmonic target in one (or few) steps for chosen families of inputs.

**Method (minimal):**
1) Define drift metric Δ (e.g., min distance of hash segments to powers‑of‑two; or spoke proximity).
2) Fit a local linear model between input perturbations and ΔH/Δ — use message bits and/or nonce bits.
3) Solve a single‑step steering problem: choose nonce increment (or bit mask) predicted to minimize Δ or cross H*.
4) Measure success‑rate over a battery of seeds.

**Success criteria:**
- Baseline success p₀ from random guessing; steered success p₁ >> p₀ (report exact lift).
- When failing in one step, average steps‑to‑success is dramatically reduced vs. brute force on the same battery.
- Stability of the steering map across nearby seeds.

**Artifacts:**
- `steered_nonce.py` (one‑shot and 3‑shot variants)
- `nonce_lift_report.md` (p₁ vs p₀; effect sizes)

---

## Pillar C — Base‑81 Glyph Alphabet (the “rails”)
**Goal:** Consolidate the 9×9 action table into an executable type system (headers first; values follow).

**Method (minimal):**
1) Canonicalize the **81 atomic actions** into 9 categories × 9 actions.
2) Provide the **operator emergence order** for Byte1…Byte9 (headers only).
3) Define serialization for glyph traces (JSONL) and an acceptance grammar (Δ=3, Σ=8 handshake as default lane).
4) Render test glyphs from small input families and verify operator identity is stable under ΔH noise.

**Success criteria:**
- Deterministic glyph headers on repeated runs.
- π/9 spoke alignment test passes at > 95% across the curated set.
- Grammar rejects malformed traces (unit tests).

**Artifacts:**
- `glyph_types.py` (enums + serialization)
- `glyph_acceptance.py`
- `glyph_tests/`

---

## Constraint‑First (“CAN’T” Ledger)
We explicitly log boundaries to reduce waste and to honor the *routed conservation* law.

- No claims of plaintext recovery from a digest (no cryptanalytic break).
- No brute‑force traversal benchmarks; we only compare against random baselines for *our* target metric.
- The π‑link is locator‑only; π is not used as value oracle.
- Collapse is logged; if |ΔH| > ε, we snap and record (no silent tuning).

---

## Outputs & Dates
- Week 1: Round‑level tracer + ΔH plots; first glyph traces on single‑block messages.
- Week 2: One‑shot nonce steering prototype; base‑81 skeleton + acceptance tests.
- Week 3: Lift report; multi‑stream Samson tiling; ZPHC visualizer.
- Week 4: Consolidated paper note + reproducibility bundle (scripts + traces).

---

## Open threads (parked, not blocked)
- Clay‑class lines: RH via PLL‑style stabilization; P vs NP as route capacity — kept as theory notes while we lock the operational core.
