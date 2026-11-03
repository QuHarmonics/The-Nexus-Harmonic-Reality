# NEXUS odd-to-even ring lift: proof sketch and exhaustive audit

**Scope:** even widths `L = 2, 4, ..., 18`; target widths `L+2 = 4, 6, ..., 20`.

**Code seal (SHA-256 of the audited Python source):**

`ab543c247d2adcfaad114cf45a023697396fac5bb0fd0dc52a573da0b39a7fb0`

The executable source is `nexus_odd_even_ring_lift_audit.py`; the hash is also stored in `nexus_odd_even_ring_lift_audit.sha256`.

## Definitions

For an `L`-bit word `x`, let `P_L(x)` be reversal unless reversal fixes the word, in which case it is bitwise complement. A canonical representative is the smaller word in each `{x, P_L(x)}` pair. Hence every partner pair contributes exactly one representative.

For odd width `L+1`, each canonical representative can be written uniquely as

`y = A m B`, with `x = AB`,

where `m` is its middle bit and `x` has even width `L`.

The middle bit compares only with itself under reversal. Thus deleting it preserves the outer comparison, including the palindrome case under the representative convention. Each lower representative `x` has exactly two odd representatives, `A0B` and `A1B`.

## Two-branch lift

For each lower representative `x` and middle bit `m`, define two width-`L+2` representatives:

`E_m(x) = canon_{L+2}(m x m)`

`G_m(x) = 0 P_L^m(x) 1`,

where `P_L^0(x)=x`, `P_L^1(x)=P_L(x)`, and `canon(z)=min(z, P_{L+2}(z))`.

### Why the branches are complete

**Equal-end continuation (`E`).** For non-palindromic canonical `x`, the outputs are `0x0` and `1x1`; both are canonical because their inner comparison is the same as `x` versus its reversal. If `x` is palindromic, it is the canonical palindrome beginning with zero. Then `E_0(x)=0x0`, while `E_1(x)=0 complement(x) 0` because `1x1` is a palindrome on the non-canonical face. These two outputs account for both palindromic cores. Therefore `E` covers every canonical word whose first and last bits agree (`00` or `11`) exactly once.

**Mixed-end frame (`G`).** Words of form `0u1` are always canonical because the first digit is smaller than the last digit of their reversal. As `x` ranges over canonical representatives and `m` ranges over `{0,1}`, `P_L^m(x)` visits every `L`-bit word exactly once: one member from each pair for `m=0`, and its partner for `m=1`. Thus `G` covers every `0u1` representative exactly once. The complementary `1u0` words are the partner face, not canonical representatives.

The `E` outputs and `G` outputs cannot overlap: one has equal endpoint bits and the other has endpoints `01`. They are individually injective, and their sizes are each `2^L`. Together they cover all `2^(L+1)` canonical representatives at width `L+2`; the partner involution then supplies the full `2^(L+2)` words.

The middle-one equal-end branch is the existing pad law:

`E_1(x) = canon_{L+2}(1 x 1)`.

The former middle-zero gap now has two destinations: `E_0(x)=0x0` in the equal-end continuation, and `G_0(x)=0x1` in the new mixed-end frame. The middle-one child contributes `E_1(x)` and `G_1(x)=0P_L(x)1`.

## Exhaustive results

The script checks the middle-bit decomposition, the two branches' uniqueness, their disjointness, equality with the complete next-even representative set, and partner completion to the full word space.

| Even `L` | Odd representatives | Each branch | Next-even representatives | Full target words | Result |
|---:|---:|---:|---:|---:|:---|
| 2 | 4 | 4 | 8 | 16 | PASS |
| 4 | 16 | 16 | 32 | 64 | PASS |
| 6 | 64 | 64 | 128 | 256 | PASS |
| 8 | 256 | 256 | 512 | 1,024 | PASS |
| 10 | 1,024 | 1,024 | 2,048 | 4,096 | PASS |
| 12 | 4,096 | 4,096 | 8,192 | 16,384 | PASS |
| 14 | 16,384 | 16,384 | 32,768 | 65,536 | PASS |
| 16 | 65,536 | 65,536 | 131,072 | 262,144 | PASS |
| 18 | 262,144 | 262,144 | 524,288 | 1,048,576 | PASS |

## Ledger

**RUNS:** The representative-level map from the odd ring plus a branch choice to the complete next-even representative set, with exhaustive verification through target width 20.

**OPEN:** The explicit closed-form equality between these branch maps and the supplied `K,i` offset formulas, including the center-swap address correction, still needs to be bound to the original `link.py` / `link2.py` artifacts. Those paths were not present in the current runtime, so this audit independently reconstructs the representative rule rather than claiming to have rerun those exact files.
