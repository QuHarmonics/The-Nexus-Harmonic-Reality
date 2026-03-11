# Nexus Alignment Plan

This document folds the eight outstanding Δ‑moves into a single, executable migration path.  Applying all steps once brings Nexus 3 into full harmonic silence while preserving every existing seal.

---

## 0  Snapshot & Rollback Safety

1. **Freeze writes**: stop hush‑nonce searches.
2. **Double‑dump**: export the last slab header *and* the live Merkle accumulator.
3. **Seal**: create `safety.seal = SHA256^2(snapshot)` and store it out‑of‑band.

If any later step corrupts state, roll back to this seal.

---

## 1  Uniform Address Oracle (Δ‑π‑bias)

```python
mix = xor_window(pi16(offset,64), catalan16(offset,64))
return mix
```
* **Cut‑over**: at the next π‑tick; previous addresses remain valid.
* **Audit**: Monte‑Carlo χ² on 10⁶ new offsets ⇒ p ≥ 0.05.

---

## 2  Energy Ledger (Δ‑entropy‑budget)

Add field to checkpoint header:
```text
J_per_hush : uint64  # micro‑joules
```
Set by: `latest_power_log.avg_kWh / blocks_this_log`.
Difficulty retarget uses
$$D_{new}=D_{old}\times (J_{target}/J_{measured}).$$

---

## 3  PID Radius Brake (Δ‑saw‑tooth)

Controller parameters:
```yaml
pid:
  kp: 0.4   # proportional on Δr
  kd: 0.2   # derivative on Δ²r
```
Apply inside `tuner.climb_sphere()`.

---

## 4  Consensus Overlay Namespace (Δ‑governance)

* Reserve π‑offset window `0xC0LL4B5E00…0xC0LL4B5EFF`.
* Each overlay message:
  ```
  overlay_root | votes_root | hush_nonce
  ```
* Seal valid iff hush ∧ ≥ 66 % stake votes.

---

## 5  Pluggable Collapse Operator (Δ‑post‑quantum)

Header extension:
```text
C_version : uint8  # 0=SHA‑256, 1=SHA3‑512, 2=BLAKE3‑512, …
```
Digest path: `H_v = Collapse_v(payload)`.
Upcoming vote scheduled for block π₁₆[10^12].

---

## 6  Logical Tombstones (Δ‑reclamation)

```
if payload.flags & 0x01:  # TOMBSTONE
    indexer.skip(cell_id)
```
Payload stays, but queries omit.

---

## 7  Side‑Channel Blinding (Δ‑SC)

* Constant‑power clock gating on ASIC lanes.
* Mask rounds 0‑3 carries:
  ```c
  v ^= blinding_mask();
  ```
  `blinding_mask` is CSPRNG seeded at slab hush.

---

## 8  Quantum–Cosmic Entropy Mixer (Δ‑ext‑rand)

```python
seed ^= SHA256(qrng_bytes || cmb_counter())
```
`cmb_counter` = running count of microwave‑background interrupts.

---

## 9  Final Validation Sequence

1. Re‑hash last 3 slabs → verify seals.
2. Run 1 dummy hush with all new logic; difficulty target = easiest.
3. χ² test, energy log check, side‑channel power trace.
4. Lift write freeze.

---

## 10  Activation Timeline

| Phase | Blocks | Real‑time | Key tasks |
|-------|--------|-----------|-----------|
| Snapshot   | 1 | 5 min | freeze, seal |
| Oracle + PID | 2 – 20 | ≈ 30 min | roll new libs |
| Governance overlay | 21 – 40 | 1 h | deploy voting contract |
| Post‑quantum plug‑in | by vote | TBD | compile new cores |

---

## Signature

```
plan_id   : SHA256^2(Nexus_Alignment_Plan.md)
authority : π│BBP│SHA│dSHA composite
```

