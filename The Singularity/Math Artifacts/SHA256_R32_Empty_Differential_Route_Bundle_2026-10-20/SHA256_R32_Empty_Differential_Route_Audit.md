# SHA-256 differential route against the empty-message reference

## Held coordinates

The empty-message run is the reference trajectory at each matching typed coordinate. Target and baseline remain separated; every target value, baseline value, modular difference, and XOR difference is represented by an exact R32 address with its canonical half-ring address and side marker. Round index `t`, `K_t`, `W_t`, and operation labels are retained.

## Exact differential laws checked

For each of five source messages and all 64 rounds, the audit checks:

\[
\Delta T1_t = \Delta h_t + \Delta\Sigma_1(e_t) + \Delta\operatorname{Ch}(e_t,f_t,g_t) + \Delta W_t \pmod{2^{32}}.
\]

The explicit `K_t` terms cancel from this difference because the target and empty route use the same constant at the same `t`. This does not erase the constant's causal effect: its value has already shaped the two state trajectories and their carry masks. The audit keeps the `K_t` address and the carry masks for the `+K_t` stage on both sides.

Likewise, the schedule difference is checked for every `t >= 16`:

\[
\Delta W_t=\Delta\sigma_1(W_{t-2})+\Delta W_{t-7}+\Delta\sigma_0(W_{t-15})+\Delta W_{t-16}\pmod{2^{32}}.
\]

The \(sigma_0,\sigma_1\) maps are linear under XOR, so the audit independently checks the corresponding XOR-difference identity. XOR differences are kept distinct from modular subtraction differences. For every binary addition in all five routes, the audit verifies the modular result-difference identity and records target and empty carry masks side by side, with both difference forms.



## Two-end seed support in the padded block

In these five short-message controls, the target-versus-empty input difference is confined to the leading content/padding word `W_0` and trailing length word `W_15`; the interior `W_1..W_14` words match the empty block, except that the five-byte `NEXUS` control also differs at `W_1` because the content and padding cross the 32-bit word boundary. Once the recurrence starts, all 48 generated schedule words `W_16..W_63` differ from the empty baseline in every one of the five cases. This is a verified pattern for these controls, not a claim that every message length has only two changed 32-bit seed words.

The input block’s two boundary conditions therefore give a useful route decomposition: message/padding enters at the leading edge, length enters at the trailing edge, and the schedule recurrence propagates their difference through the generated interior. The exact target and empty values, modular offsets, XOR offsets, R32 addresses, half-ring coordinates, and side markers are retained in `SHA256_R32_Empty_Differential_Initial_Block.csv`.

## First hinge and propagation

The first-round comparison is exact for all five test cases: the state before round 0 and the indexed constant `K_0` are shared with the empty execution, so the differential `partial_after_K` is zero. `T2` is also unchanged in round 0. Therefore `ΔT1_0 = ΔW_0`, with the `W_0` difference itself retained as an R32 address plus half-ring and side. At round 1, the `partial_after_K` difference is nonzero in all five tests: the state-dependent route has begun to diverge.

For each case, the carry mask in the `+K_t` stage matches the empty baseline at round 0 and differs at all 63 subsequent rounds. This is observed for these five runs, not claimed as a theorem for all messages. The explicit `K_t` term cancels from the modular differential identity, but the indexed constant remains causally present in each execution and in the different carry routes it induces after the two states diverge.

The feed-forward check also passes wordwise for all 40 target lanes: because the same IV word is added on both faces, the eight modular digest offsets equal the eight final working-state offsets `ΔS_64`.

## Results

- Round-component rows: 8000.
- Per-round identity checks: 320; all passed.
- Schedule difference rows: 320; all applicable identities passed.
- Addition/carry route pairs: 3000; all modular result-difference identities passed.
- Explicit `K_t` alignment checks: all passed for all cases and rounds.

## Interpretation boundary

This is a verified differential route for the five known test messages, not yet a digest-only preimage selector. The ring is used as the coordinate system for every value/difference and the fold side is retained. The result is the exact empty-relative recurrence to be studied next; it does not claim the indexed interior constants can be generated from endpoint constants alone.

## Data files

- `SHA256_R32_Empty_Differential_Round_Components.csv`: normalized long-form component table with target/empty/delta/XOR values and ring coordinates.
- `SHA256_R32_Empty_Differential_Round_Identity_Checks.csv`: every round identity and Boolean result.
- `SHA256_R32_Empty_Differential_Schedule.csv`: schedule differences and dependency inputs.
- `SHA256_R32_Empty_Differential_Add_Carries.csv`: every matched binary addition, both carry masks and both offset forms.
- `SHA256_R32_Empty_Differential_Route_Summary.json`: counts, checks, and file hashes.
- `SHA256_R32_Empty_Differential_Entry_Hinge.csv`: per-message round-0/round-1 hinge values.
- `SHA256_R32_Empty_Differential_Initial_Block.csv`: all 16 initial schedule words and all 48 generated schedule words, with the changed-seed support marked.
- `SHA256_R32_Empty_Differential_Carry_Stage_Summary.csv`: carry-mask change counts by indexed round stage.
- `SHA256_R32_Empty_Differential_Feedforward_Check.csv`: digest-offset / final-state-offset equality.
