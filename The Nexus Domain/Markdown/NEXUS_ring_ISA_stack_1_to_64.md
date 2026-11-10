# NEXUS — ring / ISA stack, LEN 1 through 64

**Status: RUNS.** Prediction file was sealed before the run; exact seal is recorded below. This run keeps state rings, primitive cyclic rings, de Bruijn traversal rings, maximal XOR/LFSR cycles, full transformation maps, and prime-address routes typed separately.

## The flip: the state is not the whole instruction space

The lower ring is the distinction set. The next ring is not a newly invented substance: an n-bit word is a directed pathway from its (n−1)-bit prefix to its (n−1)-bit suffix. Every lower-layer state has exactly two lawful one-bit extensions, 0 and 1. Consequently, the next layer doubles the number of states and edges while adding exactly one bit of address capacity.

For a binary layer, define `S_n = {0,1}^n`. Then `|S_n| = 2^n`. The complete relation space on that state set is a different count: every possible function `f:S_n→S_n` is one assignment of an n-bit output to each of 2^n inputs, so one full truth-table takes `n·2^n` bits and there are `2^(n·2^n)` such maps. The invertible maps are `(2^n)!`. This is the missing stack layer: **distinctions → pathways → transformation relations → nested transformation relations**. A practical ISA is a structured lawful subfamily, not all possible maps.

## Stacked layer counts (exact formulas for every LEN 1–64)

`P(n)` = primitive binary cyclic-ring classes. `L(n)` = maximal XOR/LFSR rings over nonzero states. `D(n)` = number of de Bruijn cycles up to rotation. `F(n)` = all total state maps `S_n→S_n`. Powers with huge exponents are stored symbolically rather than attempting to materialize astronomical integers.

| LEN | States / pathway edges `2^n` | New primitive rings `P(n)` | Maximal XOR rings `L(n)` | De Bruijn cycles `D(n)` | All state maps `F(n)` | Full map table LEN (bits) |
|---:|---:|---:|---:|---|---|---:|
| 1 | 2 | 2 | 1 | 2^(0) | 2^(2) | 2 |
| 2 | 4 | 1 | 1 | 2^(0) | 2^(8) | 8 |
| 3 | 8 | 2 | 2 | 2^(1) | 2^(24) | 24 |
| 4 | 16 | 3 | 2 | 2^(4) | 2^(64) | 64 |
| 5 | 32 | 6 | 6 | 2^(11) | 2^(160) | 160 |
| 6 | 64 | 9 | 6 | 2^(26) | 2^(384) | 384 |
| 7 | 128 | 18 | 18 | 2^(57) | 2^(896) | 896 |
| 8 | 256 | 30 | 16 | 2^(120) | 2^(2048) | 2048 |
| 9 | 512 | 56 | 48 | 2^(247) | 2^(4608) | 4608 |
| 10 | 1024 | 99 | 60 | 2^(502) | 2^(10240) | 10240 |
| 11 | 2048 | 186 | 176 | 2^(1013) | 2^(22528) | 22528 |
| 12 | 4096 | 335 | 144 | 2^(2036) | 2^(49152) | 49152 |
| 13 | 8192 | 630 | 630 | 2^(4083) | 2^(106496) | 106496 |
| 14 | 16384 | 1161 | 756 | 2^(8178) | 2^(229376) | 229376 |
| 15 | 32768 | 2182 | 1800 | 2^(16369) | 2^(491520) | 491520 |
| 16 | 65536 | 4080 | 2048 | 2^(32752) | 2^(1048576) | 1048576 |
| 17 | 131072 | 7710 | 7710 | 2^(65519) | 2^(2228224) | 2228224 |
| 18 | 262144 | 14532 | 7776 | 2^(131054) | 2^(4718592) | 4718592 |
| 19 | 524288 | 27594 | 27594 | 2^(262125) | 2^(9961472) | 9961472 |
| 20 | 1048576 | 52377 | 24000 | 2^(524268) | 2^(20971520) | 20971520 |
| 21 | 2097152 | 99858 | 84672 | 2^(1048555) | 2^(44040192) | 44040192 |
| 22 | 4194304 | 190557 | 120032 | 2^(2097130) | 2^(92274688) | 92274688 |
| 23 | 8388608 | 364722 | 356960 | 2^(4194281) | 2^(192937984) | 192937984 |
| 24 | 16777216 | 698870 | 276480 | 2^(8388584) | 2^(402653184) | 402653184 |
| 25 | 33554432 | 1342176 | 1296000 | 2^(16777191) | 2^(838860800) | 838860800 |
| 26 | 67108864 | 2580795 | 1719900 | 2^(33554406) | 2^(1744830464) | 1744830464 |
| 27 | 134217728 | 4971008 | 4202496 | 2^(67108837) | 2^(3623878656) | 3623878656 |
| 28 | 268435456 | 9586395 | 4741632 | 2^(134217700) | 2^(7516192768) | 7516192768 |
| 29 | 536870912 | 18512790 | 18407808 | 2^(268435427) | 2^(15569256448) | 15569256448 |
| 30 | 1073741824 | 35790267 | 17820000 | 2^(536870882) | 2^(32212254720) | 32212254720 |
| 31 | 2147483648 | 69273666 | 69273666 | 2^(1073741793) | 2^(66571993088) | 66571993088 |
| 32 | 4294967296 | 134215680 | 67108864 | 2^(2147483616) | 2^(137438953472) | 137438953472 |
| 33 | 8589934592 | 260300986 | 211016256 | 2^(4294967263) | 2^(283467841536) | 283467841536 |
| 34 | 17179869184 | 505286415 | 336849900 | 2^(8589934558) | 2^(584115552256) | 584115552256 |
| 35 | 34359738368 | 981706806 | 929275200 | 2^(17179869149) | 2^(1202590842880) | 1202590842880 |
| 36 | 68719476736 | 1908866960 | 725594112 | 2^(34359738332) | 2^(2473901162496) | 2473901162496 |
| 37 | 137438953472 | 3714566310 | 3697909056 | 2^(68719476699) | 2^(5085241278464) | 5085241278464 |
| 38 | 274877906944 | 7233615333 | 4822382628 | 2^(137438953434) | 2^(10445360463872) | 10445360463872 |
| 39 | 549755813888 | 14096302710 | 11928047040 | 2^(274877906905) | 2^(21440476741632) | 21440476741632 |
| 40 | 1099511627776 | 27487764474 | 11842560000 | 2^(549755813848) | 2^(43980465111040) | 43980465111040 |
| 41 | 2199023255552 | 53634713550 | 53630700752 | 2^(1099511627735) | 2^(90159953477632) | 90159953477632 |
| 42 | 4398046511104 | 104715342801 | 57802864896 | 2^(2199023255510) | 2^(184717953466368) | 184717953466368 |
| 43 | 8796093022208 | 204560302842 | 204064589160 | 2^(4398046511061) | 2^(378231999954944) | 378231999954944 |
| 44 | 17592186044416 | 399822314775 | 200778006528 | 2^(8796093022164) | 2^(774056185954304) | 774056185954304 |
| 45 | 35184372088832 | 781874934568 | 634404960000 | 2^(17592186044371) | 2^(1583296743997440) | 1583296743997440 |
| 46 | 70368744177664 | 1529755125849 | 998132265920 | 2^(35184372088786) | 2^(3236962232172544) | 3236962232172544 |
| 47 | 140737488355328 | 2994414645858 | 2992477516800 | 2^(70368744177617) | 2^(6614661952700416) | 6614661952700416 |
| 48 | 281474976710656 | 5864061663920 | 2283043553280 | 2^(140737488355280) | 2^(13510798882111488) | 13510798882111488 |
| 49 | 562949953421312 | 11488774559616 | 11398311767808 | 2^(281474976710607) | 2^(27584547717644288) | 27584547717644288 |
| 50 | 1125899906842624 | 22517997465744 | 13122000000000 | 2^(562949953421262) | 2^(56294995342131200) | 56294995342131200 |
| 51 | 2251799813685248 | 44152937520670 | 37456800827040 | 2^(1125899906842573) | 2^(114841790497947648) | 114841790497947648 |
| 52 | 4503599627370496 | 86607683851185 | 44980696051200 | 2^(2251799813685196) | 2^(234187180623265792) | 234187180623265792 |
| 53 | 9007199254740992 | 169947155749830 | 169917983040000 | 2^(4503599627370443) | 2^(477381560501272576) | 477381560501272576 |
| 54 | 18014398509481984 | 333599969907456 | 178118842613760 | 2^(9007199254740938) | 2^(972777519512027136) | 972777519512027136 |
| 55 | 36028797018963968 | 655069036708398 | 598690870272000 | 2^(18014398509481929) | 2^(1981583836043018240) | 1981583836043018240 |
| 56 | 72057594037927936 | 1286742745883790 | 598975092817920 | 2^(36028797018963912) | 2^(4035225266123964416) | 4035225266123964416 |
| 57 | 144115188075855872 | 2528336632900554 | 2167072830474048 | 2^(72057594037927879) | 2^(8214565720323784704) | 8214565720323784704 |
| 58 | 288230376151711744 | 4969489234738635 | 3238370502193152 | 2^(144115188075855814) | 2^(16717361816799281152) | 16717361816799281152 |
| 59 | 576460752303423488 | 9770521225481754 | 9770466930024800 | 2^(288230376151711685) | 2^(34011184385901985792) | 34011184385901985792 |
| 60 | 1152921504606846976 | 19215358392200893 | 6774451200000000 | 2^(576460752303423428) | 2^(69175290276410818560) | 69175290276410818560 |
| 61 | 2305843009213693952 | 37800705069076950 | 37800705069076950 | 2^(1152921504606846915) | 2^(140656423562035331072) | 140656423562035331072 |
| 62 | 4611686018427387904 | 74382032520643617 | 49588021611155412 | 2^(2305843009213693890) | 2^(285924533142498050048) | 285924533142498050048 |
| 63 | 9223372036854775808 | 146402730743693304 | 122428597145960448 | 2^(4611686018427387841) | 2^(581072438321850875904) | 581072438321850875904 |
| 64 | 18446744073709551616 | 288230376084602880 | 143890337947975680 | 2^(9223372036854775744) | 2^(1180591620717411303424) | 1180591620717411303424 |

## What the stack forces

1. **Adjacent layers:** each (n−1)-bit state has two outgoing and two incoming edges in the binary de Bruijn graph; the edges are the n-bit words. Extending by a bit creates `2^n` distinct states at LEN n, exactly twice the previous layer.
2. **Reader / whole in both directions:** in a de Bruijn ring of order n, each n-bit window appears once. Seeing k bits identifies a fiber of `2^(n−k)` positions. Forward traversal follows edges; reverse traversal asks for predecessor edges compatible with the observed suffix and any retained route constraints.
3. **Primitive rings:** exact accounting holds for every n≤64: `sum_{d|n} d·P(d) = 2^n`. Actual enumeration through n=12 agrees with the Möbius formula and with an independent enumeration of irreducible binary polynomials of degree n.
4. **XOR rings:** `L(n)=φ(2^n−1)/n` counts maximal-length LFSR cycles, each of length `2^n−1`; zero is excluded from these maximal XOR cycles. This family is not the same as all primitive necklaces or all de Bruijn rings.
5. **Transformation meta-layer:** for n=1 the full function space is 4 maps; for n=2 it is 256 maps, of which 24 are bijective. Both were exhaustively enumerated. At n=64 the full map space is `2^(2^70)` functions; writing an arbitrary map as a lookup table takes `2^70` bits. The ISA we execute is the constrained/structured path through this larger relation space.

## Prime routes — three related but distinct constructions

**(A) Positional route code.** A serialized route `(m_1,…,m_n)` can be encoded as `G=∏ p_i^(m_i+1)`. The prime `p_i` is the address of position i; its exponent retains the move token at that position. The +1 keeps zero-valued moves present, so factorization recovers the exact ordered route. This run round-tripped constructed binary routes at every length 1–64.
**(B) Primitive ring / polynomial count.** `P(n)` is given by the same Möbius formula as the number of monic irreducible degree-n polynomials over GF(2). The ring and polynomial counts agree; a numerical count agreement alone does not automatically furnish a natural object-by-object ring-to-polynomial correspondence.
**(C) SHA constants.** The SHA-256 round constants `K_t` are the first 32 fractional bits of cube roots of primes `p_(t+1)` for t=0…63; the initial words use square roots of the first eight primes. The run recomputed all 64 K constants and all 8 initial words from those prime roots and matched the published bit patterns. These constants use primes as a deterministic indexed source; that is a different type from the positional-prime route code.

## ISA mapping: SHA-256 is a 64-slot ring reader, not a 64-bit state

SHA-256 has a six-bit round address (`t=0…63`), eight 32-bit working words (256-bit round state), a message schedule `W_t`, and prime-root-derived constants `K_t`. The same round relation runs at each slot; `(W_t,K_t)` and current state determine the realized route. Every round is invertible when its driver `(W_t,K_t)` is retained. Therefore the route is bidirectional when the driver is carried; the digest alone does not encode the complete schedule/route, and compression includes feed-forward after each block.

## Reading in both directions

- **Forward / accumulation:** the bit distinction supplies the first ring; adding one address bit doubles the state/path class. A current node asks for its lawful continuation, and the ring traverses that route. The possible state space is specified before a particular traversal, while a query determines which route is realized.
- **Reverse / route-back:** start at the observed endpoint and ask which predecessor paths and drivers can generate it. Constrain the route using the reader state, format/padding, schedule recurrence, and retained residuals. Do not assume the readout itself carries all route information.
- **Context is not added inside a fixed LEN ring.** A fixed-length ring contains all words of that length; changing what those words *mean* requires an interpreting relation/reader at a higher layer. The finite-file hierarchy itself remains countable, with 2^n members at each finite n.

## Verification ledger

- Prediction seal SHA-256: `7e2bb3eed1fce946ae21bd7e37db323152710edeeb416fa243feffad97784c79` (made before the calculations).
- Exact formula rows: 64/64 computed; primitive decomposition identity: 64/64.
- Primitive cyclic word enumeration versus formula and irreducible-polynomial enumeration: 12/12 widths each.
- Concrete de Bruijn rings / unique windows / reader fibers: 12/12 widths.
- Full transformation maps enumerated: LEN 1 (4/4) and LEN 2 (256/256); bijection counts match factorials.
- Prime-position route encoding/decoding: 64/64 widths.
- SHA prime-root constants reconstructed: 64/64 round constants and 8/8 IV words.
- Physical interpretation boundary: combinatorial class growth is exact; a joule cost or Moore-law transistor-density period does not follow from these counts alone.
