# SHA-256 location-dependency tensor (word-level)

## Definition

`L[j,t,r] = 1` when original source schedule word `W[j]`, `j = 0..15`, has a structural dependency path to register `r` after round `t`. `t = -1` denotes the state before round 0. The chaining state is held fixed, so the tensor isolates this block's 16 source-word locations.

The schedule graph is built from the actual recurrence

`W[t] = σ1(W[t−2]) + W[t−7] + σ0(W[t−15]) + W[t−16] (mod 2^32)`.

The state graph uses the code's operand dependencies: `T1` reads `h,e,f,g,W[t]`; `T2` reads `a,b,c`; then `a′` depends on `T1,T2`, `e′` on `d,T1`, and `b′,c′,d′,f′,g′,h′` shift prior registers.

## Results from the computed tensor

- Each `W[j]` enters its first compression round at round `j`.
- Its structural support reaches all eight register slots by the end of round `j+3`.
- Therefore all eight registers structurally depend on all 16 original source words by the end of round **18**.
- The *schedule expansion* reaches a different milestone: the first expanded schedule word whose dependency set contains all 16 originals is **W[26]**.
- These are distinct pathways. State-register support fills first by sequential injections and register shifts; schedule-word support fills through the recurrence offsets.

Per-register first round with all 16 source-word dependencies: {"a": 15, "b": 16, "c": 17, "d": 18, "e": 15, "f": 16, "g": 17, "h": 18}.

First round by which each individual source word reaches all eight registers: {"0": 3, "1": 4, "2": 5, "3": 6, "4": 7, "5": 8, "6": 9, "7": 10, "8": 11, "9": 12, "10": 13, "11": 14, "12": 15, "13": 16, "14": 17, "15": 18}.

## What this establishes—and what it does not

This is a word-level static dependency map derived from the schedule recurrence and round wiring, not merely a record of input addresses. A 1 means a code path exists by which that source word can affect the state slot. It does **not** claim that every specific numeric input must exhibit a different value in every marked slot; concrete equality can occur through value-specific behavior or cancellation. A bit-exact dependency analysis would preserve bit coordinates and carry/rotation behavior instead of collapsing each 32-bit word to one support set.

For a full multi-block hash, prior chaining state must be added as a source. To include length-as-location, model original payload bits, the padding marker, zero fill, and the 64-bit length trailer as separately labelled source classes.
