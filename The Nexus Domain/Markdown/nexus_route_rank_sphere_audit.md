# NEXUS ring route → rank and sphere-lift audit

## Result

The E/G labeling yields an explicit, invertible route code and an exact route-to-ring-position map. The code retains the odd-width middle value and, at the following even width, appends the outer-pair residual. A separate side bit distinguishes a canonical word from its partner.

The script was SHA-256 sealed before execution and the pre-run seal verifies against the source file. This audit is independent of the unavailable `/tmp/r3/sphere.py` and `/tmp/r2/gauge.py` sources.

## 1. E/G construction and route code

For a word `x`, let `P(x)` be the ring partner: reverse a non-palindrome; complement a palindrome. Define `canon(x) = min(x, P(x))`.

For an even-width canonical parent `x` and value bit `m`:

```text
E_m(x) = canon(m + x + m)
G_m(x) = 0 + P(x) + 1    if m = 1
        = 0 + x + 1      if m = 0
```

The canonical route code is defined recursively:

- Width 2: `00 → 0`, `01 → 1`.
- Odd width: remove the middle bit `m`; route is `route(core) + m`.
- Even width ≥ 4: strip the outer pair, recover canonical core `x` and value `m` from the E/G frame/face rule, set `d = first_bit XOR last_bit`, and route is `route(x) + m + d`.

The full route code is one side bit plus the canonical route code: side `0` means canonical representative; side `1` means its partner. The palindrome/complement case is handled by recovering the core's canonical face rather than reading only the physical outer frame.

This gives exactly `L` route bits for every `L`-bit word. In the audited construction, each code bit is a readout from the current word/route: middle values at odd widths and outer-pair residuals at even widths.

## 2. Route to rank and physical address

Let `N = 2^L`, `M = 2^(L-1)`, and let `r_L(x)` count canonical representatives with numeric value less than canonical word `x`. A mirrored-pair digit DP computes this count without constructing the ring.

The descending representative offset is

```text
q = M - 1 - r_L(x)
```

The center-swapped physical address for the canonical word is

```text
pos(q) = M       if q = 0
         M - 1-q otherwise
```

The partner's address is `N - 1 - pos(q)`. This is the exact route-to-address function: decode route → canonical word → representative rank → descending offset → physical position → partner-side reflection if the side bit is `1`.

At even width `L=2h`, the same descending offset agrees with the mixed-block formula. With `H=2^h`, `x=A H+B`, and `K=H-1-A`:

```text
D_K = K(K-1)/2 + max(0, K-H/2)
i   = #{b : B < b < H and
          reverse_h(b) > A or
          (reverse_h(b) = A and A < H/2)}
q   = D_K + i
```

The block formula and digit-DP rank agree exhaustively on all canonical representatives at even widths 2, 4, 6, 8, 10, and 12.

## 3. Audit results

- Canonical route bijection: every code of length `L-1` maps to exactly one canonical representative for every width `L=2…18`.
- The route codec round-trips every canonical representative exhaustively through width 18 (131,072 representatives at width 18).
- Rank count and rank/unrank: checked against independently sorted representative lists for every width `L=2…12`.
- Physical ring positions and partner-reflection law: checked at every position for widths `L=2…10`.
- E/G block offsets: checked against rank at even widths 2, 4, 6, 8, 10, 12.
- Widths 64, 256, and 512: deterministic sample route round-trips, scalar rank calculation, and address-to-word round trips passed without materializing a ring array.

## 4. Latitude update under the E/G lift

Use the corpus coordinate

```text
z(x) = HammingWeight(x) - width(x)/2
```

For the even-to-odd lift that inserts middle value `m`,

```text
z(odd) = z(even) + (m - 1/2)
```

For the E/G odd-to-even step, with residual `d` of the new outer pair, the tested relation is

```text
z(child) = s * [z(odd) + (m - 1/2) * (-1)^d]
```

where `s=-1` exactly when the source core `x` is palindromic and `m=1`; otherwise `s=+1`. The sign flip is the complement-face exception, including both E1 and G1 outcomes for a canonical palindromic core.

Exhaustive E/G checks across source widths `L=2,4,…,18` covered 349,524 odd children and 699,048 even E/G children, with zero latitude-law failures. At source width `L`, the number of canonical palindromic cores is `2^(L/2-1)`. Because both `d=0` and `d=1` branches take the complement face when `m=1`, the number of sign-flip child transitions is `2^(L/2)`. Therefore `2^(L/2-1)` is the count of canonical palindromic cores, not the total count of flipped transitions.

## 5. Geometric qualification: partner reflection is not a literal half-turn

The exact ring-address identity is

```text
pos(P(x)) = 2^L - 1 - pos(x)
```

For equally spaced slot-center azimuths `theta_i = 2π(i+1/2)/2^L`, that maps `theta` to `2π-theta`: an azimuthal reflection. It is not the ordinary half-turn `theta → theta+π`. For example, at width 3, position 0's partner is at position 7, while the half-turn slot is position 4.

The latitude statement does hold exactly: reversal preserves Hamming weight for non-palindromes, while complementing a palindrome changes `z` to `-z`. But “partner is the geometric antipode exactly on palindromes” does not follow under ordinary equally spaced azimuth coordinates; the azimuth coordinate would also have to shift by π. The safe formal statement is: the partner map is an azimuthal reflection that preserves latitude off the palindrome branch and reverses latitude on the palindrome branch.

## Ledger

- **RUNS:** E/G route codec is a bijection on canonical representatives through width 18.
- **RUNS:** route → rank → physical address, including center swap, passed exhaustive small-width checks and wide scalar round trips.
- **RUNS:** the E/G latitude update passed 699,048 even-child checks, plus 349,524 odd-child checks.
- **QUALIFICATION:** the antipodal language requires a coordinate convention change; under ordinary ring azimuth, the partner action is reflection, not half-turn.
- **OPEN:** this establishes an exact address transform. It does not by itself establish that the abstract Hamming-weight sphere is a physical sphere or that the ladder's route bits have physical spin-½ dynamics.

## Files and provenance

`nexus_route_rank_sphere_audit.py` is the executable audit. `nexus_route_rank_sphere_audit_results.json` contains machine-readable counts. `nexus_route_rank_sphere_audit.sha256` contains the source seal made before execution. The script checksum verified after execution.
