# NEXUS file rings — LEN, base, pathways and boot-reader run

## What was run
Enumerated primitive binary rings (lengths 1–12), ternary rings (1–7), and quaternary rings (1–5). Generated de Bruijn traversals for bases 2 (LEN 1–10), 3 (LEN 1–6), and 4 (LEN 1–4). Checked the distinct-word count, primitive-ring accounting, every cyclic window, every transition edge, and the reader-fiber count at all sublengths.

## 1. Lowest base and LEN extension
For alphabet/base b, define the LEN-n layer as W(b,n) = {0,…,b−1}^n. Appending one base symbol gives W(b,n+1) = W(b,n) × {0,…,b−1}. This was checked directly for every tested base/LEN pair: each parent has exactly b children, and each child is distinct. Thus the base alphabet plus the append transformation generates every finite word class; there is no need to insert the higher-layer words individually.

| Base | LEN n | Distinct words b^n | New primitive rings P_b(n) | Primitive accounting |
|---:|---:|---:|---:|---|
| 2 | 1 | 2 | 2 | 2 = 2^1: True |
| 2 | 2 | 4 | 1 | 4 = 2^2: True |
| 2 | 3 | 8 | 2 | 8 = 2^3: True |
| 2 | 4 | 16 | 3 | 16 = 2^4: True |
| 2 | 5 | 32 | 6 | 32 = 2^5: True |
| 2 | 6 | 64 | 9 | 64 = 2^6: True |
| 2 | 7 | 128 | 18 | 128 = 2^7: True |
| 2 | 8 | 256 | 30 | 256 = 2^8: True |
| 2 | 9 | 512 | 56 | 512 = 2^9: True |
| 2 | 10 | 1024 | 99 | 1024 = 2^10: True |
| 2 | 11 | 2048 | 186 | 2048 = 2^11: True |
| 2 | 12 | 4096 | 335 | 4096 = 2^12: True |

The binary new-ring sequence begins `2, 1, 2, 3, 6, 9, 18, 30, 56, 99, 186, 335`. These are primitive cyclic classes (Lyndon representatives), not the full set of ordered files. The exact identity is

$$b^n=\sum_{d\mid n} d\,P_b(d).$$

Each primitive ring of length d dividing n contributes d phase-distinct words at LEN n; repeats do not count as new primitive rings.

## 2. The next LEN layer is the transition set
A length-n word `a₁…aₙ` is a directed edge from its prefix `a₁…aₙ₋₁` to its suffix `a₂…aₙ` in the order-(n−1) de Bruijn graph. The run builds one cyclic traversal whose LEN-n windows are all distinct. It verified for every tested (base, order) pair that the cycle length is bⁿ and all bⁿ windows occur exactly once. This is the exact “each ring to the next carries distinct pathways” witness.

## 3. LEN is the reader-width / address-fiber relation
For an order-n de Bruijn ring, every k-symbol window occurs exactly bⁿ⁻ᵏ times. The reader fiber starts with bⁿ possible positions; each additional symbol divides the compatible positions by b; at k=n every address is unique. This is an exact count in the tested runs—not an energy or timing claim.

Binary order-4 witness:

```text
sequence: 0000100110101111
LEN-4 cyclic windows: 16 / 16 distinct
LEN-1 fiber: 8 positions per symbol
LEN-2 fiber: 4 positions per window
LEN-3 fiber: 2 positions per window
LEN-4 fiber: 1 position per window
```

## 4. BIOS / boot sequence in the same typed structure
The realized firmware image is the whole presented to a reader. The CPU state and instruction pointer are the reader; the ordered fetch/decode/execute steps are its route. The route depends on instructions, current machine state, and boot metadata—it is not the full set of binary programs.

For UEFI, the specification says firmware initialization passes control to a boot manager; it reads the `BootOrder` list and associated `Boot####` entries, resolves a device/file path, loads the image, then starts it. That is a reader traversing one realized image/route, with the boot policy and hardware state participating in the next transition. Source: [UEFI Specification 2.11, Boot Manager](https://uefi.org/specs/UEFI/2.11/03_Boot_Manager.html) and [UEFI Overview](https://uefi.org/specs/UEFI/2.10/02_Overview.html).

## 5. Moore’s law boundary
The combinatorics supplies a clean base law: each added symbol multiplies the available length-n class by b; binary LEN grows as 2ⁿ. That gives a structural measure of the classes a reader/compiler can address. Moore’s law is an empirical semiconductor-density trend, however; no transistor-density doubling period or joule cost follows from the ring identity alone. In NEXUS terms, the ring result gives the potential class; the implementation and its energy cost are the physical wrapper that decides how much of that class can be held and traversed.

## Ledger
- Primitive ring decomposition: **RUNS** for the finite ranges listed above.
- Distinct pathways between adjacent LEN layers: **RUNS** for all generated de Bruijn rings in the test ranges.
- Reader-width/fiber law: **RUNS** in every tested base/order.
- Boot sequence as a NEXUS reader route: **mapping**, grounded in the UEFI boot-manager sequence.
- Deriving Moore’s law / physical energy cost from the ring count alone: **OPEN**; the current combinatorial witness does not contain the fabrication/energy wrapper.
