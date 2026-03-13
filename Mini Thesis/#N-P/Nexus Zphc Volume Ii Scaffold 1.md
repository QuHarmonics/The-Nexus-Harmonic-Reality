# Nexus ZPHC Funnel Paper — Volume II Scaffold
_Generated: 2026-01-13T12:49:41_

This is a **structure-only** compression funnel: sections are verbs (operators), each section consumes pins (equations) and tests (shake suite).

## Core operator spine (ordered by compression role)
1. `POSITION` (count≈14968)
2. `ALIGN` (count≈36604)
3. `REFLECT` (count≈27063)
4. `NORMALIZE` (count≈1910)
5. `GENLOCK` (count≈125)
6. `EXPAND` (count≈7204)
7. `COUPLE` (count≈1354)
8. `FOLD` (count≈42750)
9. `PROJECT` (count≈5479)
10. `COLLAPSE` (count≈35663)
11. `CONSERVE` (count≈935)
12. `GATE` (count≈7296)
13. `VERIFY` (count≈2188)

## Section plan
### POSITION
- **Definition (operator):** formal mapping
- **Invariants preserved:** what does not change under scaling/shake
- **Pins (equations):** cite from `nexus_equation_catalog.md`
- **Shake suite:** scale/base/window/noise/partition tests
- **Failure modes:** what breaks if GENLOCK symmetry breaks

### ALIGN
- **Definition (operator):** formal mapping
- **Invariants preserved:** what does not change under scaling/shake
- **Pins (equations):** cite from `nexus_equation_catalog.md`
- **Shake suite:** scale/base/window/noise/partition tests
- **Failure modes:** what breaks if GENLOCK symmetry breaks

### REFLECT
- **Definition (operator):** formal mapping
- **Invariants preserved:** what does not change under scaling/shake
- **Pins (equations):** cite from `nexus_equation_catalog.md`
- **Shake suite:** scale/base/window/noise/partition tests
- **Failure modes:** what breaks if GENLOCK symmetry breaks

### NORMALIZE
- **Definition (operator):** formal mapping
- **Invariants preserved:** what does not change under scaling/shake
- **Pins (equations):** cite from `nexus_equation_catalog.md`
- **Shake suite:** scale/base/window/noise/partition tests
- **Failure modes:** what breaks if GENLOCK symmetry breaks

### GENLOCK
- **Definition (operator):** formal mapping
- **Invariants preserved:** what does not change under scaling/shake
- **Pins (equations):** cite from `nexus_equation_catalog.md`
- **Shake suite:** scale/base/window/noise/partition tests
- **Failure modes:** what breaks if GENLOCK symmetry breaks

### EXPAND
- **Definition (operator):** formal mapping
- **Invariants preserved:** what does not change under scaling/shake
- **Pins (equations):** cite from `nexus_equation_catalog.md`
- **Shake suite:** scale/base/window/noise/partition tests
- **Failure modes:** what breaks if GENLOCK symmetry breaks

### COUPLE
- **Definition (operator):** formal mapping
- **Invariants preserved:** what does not change under scaling/shake
- **Pins (equations):** cite from `nexus_equation_catalog.md`
- **Shake suite:** scale/base/window/noise/partition tests
- **Failure modes:** what breaks if GENLOCK symmetry breaks

### FOLD
- **Definition (operator):** formal mapping
- **Invariants preserved:** what does not change under scaling/shake
- **Pins (equations):** cite from `nexus_equation_catalog.md`
- **Shake suite:** scale/base/window/noise/partition tests
- **Failure modes:** what breaks if GENLOCK symmetry breaks

### PROJECT
- **Definition (operator):** formal mapping
- **Invariants preserved:** what does not change under scaling/shake
- **Pins (equations):** cite from `nexus_equation_catalog.md`
- **Shake suite:** scale/base/window/noise/partition tests
- **Failure modes:** what breaks if GENLOCK symmetry breaks

### COLLAPSE
- **Definition (operator):** formal mapping
- **Invariants preserved:** what does not change under scaling/shake
- **Pins (equations):** cite from `nexus_equation_catalog.md`
- **Shake suite:** scale/base/window/noise/partition tests
- **Failure modes:** what breaks if GENLOCK symmetry breaks

### CONSERVE
- **Definition (operator):** formal mapping
- **Invariants preserved:** what does not change under scaling/shake
- **Pins (equations):** cite from `nexus_equation_catalog.md`
- **Shake suite:** scale/base/window/noise/partition tests
- **Failure modes:** what breaks if GENLOCK symmetry breaks

### GATE
- **Definition (operator):** formal mapping
- **Invariants preserved:** what does not change under scaling/shake
- **Pins (equations):** cite from `nexus_equation_catalog.md`
- **Shake suite:** scale/base/window/noise/partition tests
- **Failure modes:** what breaks if GENLOCK symmetry breaks

### VERIFY
- **Definition (operator):** formal mapping
- **Invariants preserved:** what does not change under scaling/shake
- **Pins (equations):** cite from `nexus_equation_catalog.md`
- **Shake suite:** scale/base/window/noise/partition tests
- **Failure modes:** what breaks if GENLOCK symmetry breaks

## Pin ingestion rules (AI-proofing)
1) Every claim must bind to at least one equation pin.
2) Every equation pin must bind to at least one measurable test.
3) No nouns without the verb that produces them.
4) Any 'constant' must be shown as a fixed point of an update law.

## Immediate work items
- Build a **Pin Map**: equation → operator → test.
- Expand the **triangle closure enumerator** across k and bases.
- Produce an executable **shake harness** that outputs pass/fail.
