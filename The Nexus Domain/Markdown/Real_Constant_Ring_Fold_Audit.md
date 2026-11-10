# Real-constant prefix and fold-count audit

This run uses the existing exact nested-ring `location`, `partner`, and `rank_word` routines. Fractional prefixes of pi, phi, and e were independently computed at 200-digit precision for widths 8, 16, 32, 64, 128, and 256. The ring was never materialized.

## Verified

- 18 prefix/width cases computed.
- All partner-address reflection identities pass.
- The exact fold-count coordinate `C_L(x)=rank_word(x,L)` was compared against `alpha-alpha^2/2` for every prefix.
- Prefixes agree when recomputed independently at 120 and 200 decimal digits for all 18 constant/width combinations.
- Normalized fold-count errors by width: 8: `0.0104490168751577`; 16: `0.0007291682423452`; 32: `2.91358543433e-6`; 64: `4.44666959001e-11`; 128: `1.03532094803e-20`; 256: `5.61248610538e-40` (below `6e-40`).
- Width-32 offsets from empty-digest anchor E3B0C442 reproduce with reflected sign reversal for all three constants.

## Width-32 empty-anchor offsets

| Constant | Prefix | Ring address | Signed offset from E3B0C442 | Reflected signed offset |
|---|---:|---:|---:|---:|
| pi | `243F6A88` | 4,013,904,055 | +685,208,475 | -685,208,475 |
| phi | `9E3779B9` | 2,464,615,091 | -864,080,489 | +864,080,489 |
| e | `B7E15162` | 3,274,529,653 | -54,165,927 | +54,165,927 |

## Center seam correction

The active R4 generator gives `R4[7]=13` and `R4[8]=11` (zero-based), so the twin-prime partner pair occupies the center seam exactly; `15-7=8`. `R4[1]` and `R4[2]` are [1, 2], so the position pair 1,2 in the supplied note is a typographical index error.

## Scope boundary

These checks establish a deterministic address/fold readout for the selected real-number prefixes. They do not establish that the SHA-256 round constants can be regenerated from pi, phi, e, or from the endpoints of the K sequence. Those are distinct claims requiring a separate dependency law.
