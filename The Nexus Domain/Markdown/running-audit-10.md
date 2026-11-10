# NEXUS running audit 10

Continues `running-audit-9.md` (§§ 200–201). The scripts for § 202 are printed in full in `running-audit-10-scripts.md`.

## § 202. The ring machine, built and run: a walk closes only at its own width, cut where it was written, from address 0 or the seam; at its own width the header complements one class of words in place; the register comes home by column parity — `ring_machine.ipynb`, `checks202.py`

**Dean (30 Oct).** "Build the ring machine as designed in §201: field, header, ring instructions, run, and save-from-read, as one self-contained notebook. Start from the 8-bit walk `27` and go up to the 256-byte walk of R₈. For each width, run every file under every header and report which close, which collide, and what the same files become when only the header changes. No instructions beyond what the rings already have; nothing fitted."

**Input, not instructions.** GPT `ba729573` (the TP and PT routes on R₂) and `ab640935` (the workbook's offset windows) both RUN as stated. From address 0, TP fixes 0 and 2, and PT goes 0 → 2 → 0 and fixes 1 and 3. The workbook's offset 3 is the same windows turned by 3. GPT's DI-chain partner 2^L−1−B is C, which equals P only at width 2.

**Built.** Test first: 16 checks, RED against a stub (16 failures), then GREEN.
- **Field.** The walks B₂ = `27` through B₈ (256 bytes), under both crease bits. The field is the only thing built, and `save` rebuilds all of it from the reader.
- **Header.** A reading (drawn, J, C, or sheet = C∘J), a crease bit, a reader width w = 1–8, and a frame: a cut at phase 0…w−1, or the slide (stride 1). That is 352 headers per walk and 2,464 runs in all. The start address is held at the first word, then turned separately.
- **Instructions.** Only the rings' own: PASS/FLIP, XOR, NEXT/BACK, TWIN, TP, PT, REVERSE (J), HEADER (C), WIDEN/NARROW, and centre-1 with its inverse. Each has its inverse (checked, n = 1–8).
- **Run.**
  - State reading: a run closes when every word appears once and every slot faces its twin.
  - Operand reading: XOR the words into a register from 0, then ask whether it comes home and whether it revisits a state.
- **Save from read.** As in § 201, now under both crease bits.
- **The notebook.** `ring_machine.ipynb` has 16 cells. Executed from an empty folder it gives 0 errors and 16/16 self-checks.
  - The delivered file's sha is `bd69e0e2ddbc98e83f743a20122fe15ef67fb6b325b1a6d8545f2e5073d74642`. A re-run changes only the execution timestamps.
  - `build_notebook.py` regenerates it from `ring_machine.py` and `test_ring_machine.py`.

**Sealed before the checks** (`seal202/predictions.txt`, sha `90723023128a7e061dce33226eb725b1d7d9a3225e2fe584d60ad9fb59e6b14f`).
- P1: at its own width, the header is an address-wise map.
- P2: each of the four maps commutes with P.
- P3: the register comes home iff column parity holds.
- P4: a closing run closes from start 0 and from N/2 only, and no full non-facing run faces from any start.
- P5: the drawn walk cut at its own width holds every word once exactly at phases {0, 1, 2}, for n = 6–14.

**What the run shows.**
1. **Which close.** A walk closes only at its own width, cut at phase 0. That is 8 of 352 headers for each of B₃–B₈ (4 readings × 2 crease bits). B₂ has 12. The extra 4 are the byte `27` cut one bit late (drawn/1, C/1, J/0, sheet/0): facing rings that start on a middle word.
2. **Start address.** Take a facing list of distinct words and turn it by k words. The turned list pairs address a with N−1−a+2k, so it still faces iff 2k ≡ 0 (mod N).
   - So every closing run also closes from the seam N/2, and from nowhere else (60/60).
   - **P4's second half is a DEAD END at n = 2.** The other four one-bit-late cuts of `27` face from starts 1 and 3. The reason: read from the other end, the circle `00100111` is itself turned 5 bits.
   - From n = 3 on, all 88 full non-facing cuts face from no start.
3. **What only the header changes.** This follows from the facing law R[N−1−a] = P(R[a]). Word a of the J reading is J(P(R[a])), which is R[a] off the palindromes and C(R[a]) on them. So at its own width the header does one thing in place at every address:
   - drawn: nothing;
   - J: complements the palindromes;
   - C: complements every word;
   - sheet: complements the non-palindromes.

   All four commute with P, so each reading of a ring is a ring. Drawn and sheet open on 0; J and C open on 1ⁿ, the twin file. RUNS n = 2–12, both crease bits (P1, P2).
   - At n = 2 the only non-palindromes are the seam pair 01 and 10, so complementing them swaps them. That is why the workbook's sheet reading is the counter's crease (RUNS), the bit § 200 left open.
   - **Reverse reading.** Reading from the other end looks like a reordering, but the facing law absorbs it: the same order comes back with one class of words complemented. So at its own width the header never reorders the field. It only sets the face of the palindromes, the non-palindromes, both, or neither. A new arrangement appears only when the cut moves (phase or width).
4. **Cut late, the alphabet survives.** At its own width, the walk cut 1 or 2 bits late still holds every word once. For drawn and C that is phases 1 and 2. For J and sheet it is phases n−2 and n−1, the same cuts seen from the other end.
   - This holds for n = 6–8 in the notebook, and for the drawn walk up to n = 14 (P5).
   - In the notebook (n = 3–8) these cuts face from no start, and 3 bits late brings copies. At n = 3–5 the crease bit decides some of the late cuts.
   - Why the tolerance is two bits: OPEN.
5. **Which collide.** Under one header, two files never read into one (n = 2–8), because every reading is a bijection. A file meets another file only across headers, and what it meets is one of its own readings.
   - Its twin is always in its own orbit. Orbits of size 2 are the palindromes and anti-palindromes; orbits of size 4 are the rest (n = 8: 32 + 224).
   - Inside a run, a collision is a word repeated at another address. The no-repeat matrix is in the output below.
6. **Other widths.**
   - At a smaller width dividing n, every header gives every smaller word in equal copies (256/256 runs).
   - At a smaller width not dividing n there are 640 runs: 312 hold every word in unequal copies, 292 in equal copies, and 36 hold only some words.
   - Wider than n, the files are partial: 512 of 1,232 have no word repeated. These are the short walks: B₂ 272, B₃ 148, B₄ 64, B₅ 28, B₆–B₈ 0.
7. **Operands.** A cut of stride s on a circle of length L gives L/g windows, g = gcd(L, s), one starting at every multiple of g. So register bit j collects the residue class (phase + j) mod g exactly once, and the register comes home iff every class mod g has even weight.
   - RUNS 2,464/2,464 (P3). The slides come home 448/448, since g = 1 and every walk has even weight n·2ⁿ⁻¹.
   - Coming home counts 1s and never sees the order. The order shows only in revisiting. A run comes home without revisiting only for B₂–B₄ read wider than their own width. At its own width a full cut holds the empty word 0, which leaves the register in place.
8. **Save from read.**
   - n = 2–8, both crease bits: `save` rebuilds the field word for word.
   - n = 64: the π word ↔ 2,427,008,858,123,944,441, and 200/200 random addresses round-trip, each twin at the mirror address.
   - B₄ saved as R₈ addresses [1, 33, 73, 97, 158, 180, 222, 106] reads back `0123567dbe9ac48f`.

**Corrections, mine (caught before delivery).**
- The draft notebook printed two claims as text: the inverses, and "same file under one header twice: 0". Both are now computed.
- It said the late cuts hold "for n ≥ 6" on n = 6–8 data. The text now gives the checked range, and P5 extends the drawn walk to n = 14.
- It said nothing was stored but the walks. In fact the field is the one thing built, and `save` rebuilds it from the reader.

| claim | status |
|---|---|
| ring machine: field, header, instructions, run, save from read, as one self-contained notebook | RUNS; 0 errors from an empty folder, 16/16 |
| closes only at own width, cut phase 0: 8/352 (B₃–B₈), 12/352 (B₂) | RUNS, 2,464 runs |
| a closing run closes from start 0 and from the seam N/2, nowhere else | RUNS 60/60; derived (2k ≡ 0 mod N) |
| no full non-facing cut faces from any start | RUNS n = 3–8 (88/88); DEAD END at n = 2 (4 face from starts 1, 3) |
| header at own width = in-place complement of palindromes / all / non-palindromes, commuting with P | RUNS n = 2–12; derived from the facing law |
| workbook sheet reading = the crease bit (n = 2) | RUNS; the non-palindromes of width 2 are the seam pair |
| cut 1–2 bits late keeps every word once | RUNS n = 6–8 (all readings), n = 6–14 (drawn); why: OPEN |
| register comes home iff column parity mod gcd(L, stride) is even | RUNS 2,464/2,464; derived |
| comes home without revisiting | RUNS; only B₂–B₄ read wider than their own width |
| no two files read into one under one header; twin in its own orbit | RUNS n = 2–8 |
| save from read, both crease bits | RUNS n = 2–8; n = 64, 200/200 |
| water test (§ 198) | OPEN, queued |

**Output** (`ring_machine.ipynb` as delivered, every code cell; then `python3 checks202.py`).

```
[The ring machine]
16 / 16 checks pass

[The field]
B_2:     8 bits =    1 bytes  27  sha256 265fda17a34611b1
B_3:    24 bits =    3 bytes  056767  sha256 5454c233565722d6
B_4:    64 bits =    8 bytes  0123567dbe9ac48f  sha256 c71e2cba6fffa5b4
B_5:   160 bits =   20 bytes  00443214c74a96d73e7dbe7d1b6ab2e329bc221f  sha256 57e5c7baf497c1b6
B_6:   384 bits =   48 bytes  00108310518724a2cc34e3d14935565d96dd79f8e59ebbfbdfdd79a71fa1bb69...  sha256 1f1154e449cd774b
B_7:   896 bits =  112 bytes  00041030814307102450b183470f22489942a58b99346ce1d3c7d0a246953275...  sha256 2ded5b7247c17397
B_8:  2048 bits =  256 bytes  000102030405060708090a0b0c0d0e0f1112131415161718191a1b1c1d1e1f21...  sha256 70a712c018e80677

B_4 as hex digits, each facing its twin across the crease:
  0 1 2 3 5 6 7 d  |  b e 9 a c 4 8 f
  twins: 0<->f  1<->8  2<->4  3<->c  5<->a  6<->9  7<->e  d<->b

[Instructions]
NEXT (T) : from address 0: 0 -> 1 -> 2 -> 3 -> 0   fixed addresses []   words 00 10 01 11
TWIN (P) : from address 0: 0 -> 3 -> 0   fixed addresses []   words 00 11
TP       : from address 0: 0 -> 0   fixed addresses [0, 2]   words 00
PT       : from address 0: 0 -> 2 -> 0   fixed addresses [1, 3]   words 00 01
inverses (NEXT/BACK, TWIN, TP, PT, REVERSE J, HEADER C, XOR d), every word and address n = 1..8: True

R_4, word by word: header bit, program (0 pass, 1 flip), twin; frame, middle, middle address one ring down (WIDEN undone)
   0 0000  header 0 program 000  twin 1111 (other header  )  frame 00 middle 00 -> R_2 address 0
   1 0001  header 0 program 001  twin 1000 (reversed route)  frame 01 middle 00 -> R_2 address 0
   2 0010  header 0 program 011  twin 0100 (reversed route)  frame 00 middle 01 -> R_2 address 2
   3 0011  header 0 program 010  twin 1100 (reversed route)  frame 01 middle 01 -> R_2 address 2
   4 0101  header 0 program 111  twin 1010 (reversed route)  frame 01 middle 10 -> R_2 address 1
   5 0110  header 0 program 101  twin 1001 (other header  )  frame 00 middle 11 -> R_2 address 3
   6 0111  header 0 program 100  twin 1110 (reversed route)  frame 01 middle 11 -> R_2 address 3
   7 1101  header 1 program 011  twin 1011 (reversed route)  frame 11 middle 10 -> R_2 address 1  centre block (follows R_2)
   8 1011  header 1 program 110  twin 1101 (reversed route)  frame 11 middle 01 -> R_2 address 2
   9 1110  header 1 program 001  twin 0111 (reversed route)  frame 10 middle 11 -> R_2 address 3
  10 1001  header 1 program 101  twin 0110 (other header  )  frame 11 middle 00 -> R_2 address 0
  11 1010  header 1 program 111  twin 0101 (reversed route)  frame 10 middle 01 -> R_2 address 2
  12 1100  header 1 program 010  twin 0011 (reversed route)  frame 10 middle 10 -> R_2 address 1
  13 0100  header 0 program 110  twin 0010 (reversed route)  frame 00 middle 10 -> R_2 address 1
  14 1000  header 1 program 100  twin 0001 (reversed route)  frame 10 middle 00 -> R_2 address 0
  15 1111  header 1 program 000  twin 0000 (other header  )  frame 11 middle 11 -> R_2 address 3

the seam carried up by the centre-1 insertion: [('110', '011'), ('11101', '10111'), ('1111011', '1101111')]

[Save from read]
n = 2..8, both crease bits: save(a) rebuilds every word of the field from the reader alone
n = 64: read(0x243F6A8885A308D3) = 2,427,008,858,123,944,441   save(2,427,008,858,123,944,441) = 0x243f6a8885a308d3
n = 64: 200/200 random addresses round-trip, each twin at the mirror address
B_4 saved as addresses in the byte ring R_8: [1, 33, 73, 97, 158, 180, 222, 106]  -> read back: 0123567dbe9ac48f

[The header]
workbook circle 00100111  sheet reading 00011011
  drawn sample 2, stride 1: 00 01 10 00 01 11 11 10   offset 3: 00 01 11 11 10 00 01 10   (offset 3 = the same windows rotated by 3: True)
  sheet sample 2, stride 1: 00 00 01 11 10 01 11 10   offset 3: 11 10 01 11 10 00 00 01   (offset 3 = the same windows rotated by 3: True)

B_2 crease 1:  drawn: ring (= R_n, record crease) | J: twin ring | C: twin ring | sheet: ring (= R_n, counter crease)
B_2 crease 0:  drawn: ring (= R_n, counter crease) | J: twin ring | C: twin ring | sheet: ring (= R_n, record crease)
B_3 crease 1:  drawn: ring (= R_n, record crease) | J: twin ring | C: twin ring | sheet: ring
B_3 crease 0:  drawn: ring (= R_n, counter crease) | J: twin ring | C: twin ring | sheet: ring
B_4 crease 1:  drawn: ring (= R_n, record crease) | J: twin ring | C: twin ring | sheet: ring
B_4 crease 0:  drawn: ring (= R_n, counter crease) | J: twin ring | C: twin ring | sheet: ring
B_5 crease 1:  drawn: ring (= R_n, record crease) | J: twin ring | C: twin ring | sheet: ring
B_5 crease 0:  drawn: ring (= R_n, counter crease) | J: twin ring | C: twin ring | sheet: ring
B_6 crease 1:  drawn: ring (= R_n, record crease) | J: twin ring | C: twin ring | sheet: ring
B_6 crease 0:  drawn: ring (= R_n, counter crease) | J: twin ring | C: twin ring | sheet: ring
B_7 crease 1:  drawn: ring (= R_n, record crease) | J: twin ring | C: twin ring | sheet: ring
B_7 crease 0:  drawn: ring (= R_n, counter crease) | J: twin ring | C: twin ring | sheet: ring
B_8 crease 1:  drawn: ring (= R_n, record crease) | J: twin ring | C: twin ring | sheet: ring
B_8 crease 0:  drawn: ring (= R_n, counter crease) | J: twin ring | C: twin ring | sheet: ring

B_3, the four readings word by word:
  drawn 000 001 010 110 011 101 100 111
  J     111 001 101 110 011 010 100 000
  C     111 110 101 001 100 010 011 000
  sheet 000 110 010 001 100 101 011 111

what each reading does to the word at every address, n = 2..8, both creases:
  drawn: nothing | J: complements the palindromes | C: complements every word | sheet: complements the non-palindromes -> True
  each of the four commutes with the twin map P on every word -> True
  n = 2: the non-palindromes are 01 and 10, the seam pair; complementing them swaps them, sheet(R_2) = counter crease -> True

[Saturation run 1: every word is a file]
n=2:   4 files  orbit size 2:   4 (palindromes  2 + anti-palindromes  2)  orbit size 4:   0  twin in its own orbit 4/4  programs ending on their header bit 2  two files read into one under a single header: 0
n=3:   8 files  orbit size 2:   4 (palindromes  4 + anti-palindromes  0)  orbit size 4:   4  twin in its own orbit 8/8  programs ending on their header bit 4  two files read into one under a single header: 0
n=4:  16 files  orbit size 2:   8 (palindromes  4 + anti-palindromes  4)  orbit size 4:   8  twin in its own orbit 16/16  programs ending on their header bit 8  two files read into one under a single header: 0
n=5:  32 files  orbit size 2:   8 (palindromes  8 + anti-palindromes  0)  orbit size 4:  24  twin in its own orbit 32/32  programs ending on their header bit 16  two files read into one under a single header: 0
n=6:  64 files  orbit size 2:  16 (palindromes  8 + anti-palindromes  8)  orbit size 4:  48  twin in its own orbit 64/64  programs ending on their header bit 32  two files read into one under a single header: 0
n=7: 128 files  orbit size 2:  16 (palindromes 16 + anti-palindromes  0)  orbit size 4: 112  twin in its own orbit 128/128  programs ending on their header bit 64  two files read into one under a single header: 0
n=8: 256 files  orbit size 2:  32 (palindromes 16 + anti-palindromes 16)  orbit size 4: 224  twin in its own orbit 256/256  programs ending on their header bit 128  two files read into one under a single header: 0

[Saturation run 2: every walk under every header]
2464 runs
state reading: closes
       w=1     w=2     w=3     w=4     w=5     w=6     w=7     w=8     
  B_2   0/16   12/24    0/32    0/40    0/48    0/56    0/64    0/72   
  B_3   0/16    0/24    8/32    0/40    0/48    0/56    0/64    0/72   
  B_4   0/16    0/24    0/32    8/40    0/48    0/56    0/64    0/72   
  B_5   0/16    0/24    0/32    0/40    8/48    0/56    0/64    0/72   
  B_6   0/16    0/24    0/32    0/40    0/48    8/56    0/64    0/72   
  B_7   0/16    0/24    0/32    0/40    0/48    0/56    8/64    0/72   
  B_8   0/16    0/24    0/32    0/40    0/48    0/56    0/64    8/72   
state reading: no word repeated (no collision)
       w=1     w=2     w=3     w=4     w=5     w=6     w=7     w=8     
  B_2   0/16   16/24    0/32   32/40   48/48   56/56   64/64   72/72   
  B_3   0/16    0/24   20/32   12/40    0/48   48/56   32/64   56/72   
  B_4   0/16    0/24    0/32   20/40    0/48    0/56    0/64   64/72   
  B_5   0/16    0/24    0/32    0/40   24/48    0/56    0/64   28/72   
  B_6   0/16    0/24    0/32    0/40    0/48   24/56    0/64    0/72   
  B_7   0/16    0/24    0/32    0/40    0/48    0/56   24/64    0/72   
  B_8   0/16    0/24    0/32    0/40    0/48    0/56    0/64   24/72   
operand reading: returns home
       w=1     w=2     w=3     w=4     w=5     w=6     w=7     w=8     
  B_2  16/16   24/24   32/32    8/40   48/48   56/56   64/64    8/72   
  B_3  16/16   24/24   32/32    8/40   48/48   32/56   64/64    8/72   
  B_4  16/16   24/24   32/32   40/40   48/48   56/56   64/64   40/72   
  B_5  16/16    8/24   32/32    8/40   48/48    8/56   64/64    8/72   
  B_6  16/16   24/24   32/32   24/40   48/48   56/56   64/64    8/72   
  B_7  16/16   24/24   32/32   24/40   48/48   56/56   64/64    8/72   
  B_8  16/16   24/24   32/32   40/40   48/48   56/56   64/64   72/72   
operand reading: returns home without revisiting a state
       w=1     w=2     w=3     w=4     w=5     w=6     w=7     w=8     
  B_2   0/16    0/24    4/32    4/40   24/48   56/56   64/64    8/72   
  B_3   0/16    0/24    0/32    0/40    0/48   30/56   34/64    8/72   
  B_4   0/16    0/24    0/32    0/40    0/48    0/56    0/64   32/72   
  B_5   0/16    0/24    0/32    0/40    0/48    0/56    0/64    0/72   
  B_6   0/16    0/24    0/32    0/40    0/48    0/56    0/64    0/72   
  B_7   0/16    0/24    0/32    0/40    0/48    0/56    0/64    0/72   
  B_8   0/16    0/24    0/32    0/40    0/48    0/56    0/64    0/72   

every closing run:
  B_2 crease 1 drawn w=2 cut phase 1: ring, other start
  B_2 crease 1 C     w=2 cut phase 1: ring, other start
  B_2 crease 0 J     w=2 cut phase 1: ring, other start
  B_2 crease 0 sheet w=2 cut phase 1: ring, other start
  plus, for every walk, the 8 headers at its own width cut at phase 0 (4 readings x 2 crease bits)

what the runs become, by reader width w against walk width n:
  w < n, w divides n            256 runs  every word, equal copies 256
  w < n, w does not divide n    640 runs  every word, unequal copies 312, every word, equal copies 292, some words, copies 36
  w = n                         336 runs  some words, copies 128, every word once, not facing 92, every word, unequal copies 44, ring 28, twin ring 28, every word, equal copies 12, ring, other start 4
  w > n                        1232 runs  some words, copies 716, some words, no copies 512, every word, unequal copies 4

own width, cut late: the phases at which the walk is still every word once (reading/crease)
  B_2: phase 1: drawn/1 J/1 C/1 sheet/1 drawn/0 J/0 C/0 sheet/0
  B_3: phase 1: drawn/1 C/1 drawn/0 J/0 C/0 sheet/0; phase 2: J/1 sheet/1 drawn/0 J/0 C/0 sheet/0
  B_4: phase 1: drawn/1 C/1 drawn/0 C/0; phase 2: drawn/0 J/0 C/0 sheet/0; phase 3: J/1 sheet/1 J/0 sheet/0
  B_5: phase 1: drawn/1 C/1 drawn/0 C/0; phase 2: drawn/0 J/0 C/0 sheet/0; phase 3: drawn/0 J/0 C/0 sheet/0; phase 4: J/1 sheet/1 J/0 sheet/0
  B_6: phase 1: drawn/1 C/1 drawn/0 C/0; phase 2: drawn/1 C/1 drawn/0 C/0; phase 4: J/1 sheet/1 J/0 sheet/0; phase 5: J/1 sheet/1 J/0 sheet/0
  B_7: phase 1: drawn/1 C/1 drawn/0 C/0; phase 2: drawn/1 C/1 drawn/0 C/0; phase 5: J/1 sheet/1 J/0 sheet/0; phase 6: J/1 sheet/1 J/0 sheet/0
  B_8: phase 1: drawn/1 C/1 drawn/0 C/0; phase 2: drawn/1 C/1 drawn/0 C/0; phase 6: J/1 sheet/1 J/0 sheet/0; phase 7: J/1 sheet/1 J/0 sheet/0

operand reading: the register comes home iff every residue class of the read string mod gcd(length, stride) has even weight
  agrees on 2464 / 2464 runs; slides come home 448 / 448

start address: every list that holds every word once, turned by k words, k = 0..N-1
  B_2       closes from start 0           12 runs  face from starts 0 and N/2 (the seam)
  B_2       every word once, not facing    4 runs  face from starts 1, 3
  B_3..B_8  closes from start 0           48 runs  face from starts 0 and N/2 (the seam)
  B_3..B_8  every word once, not facing   88 runs  face from no start
  the 8-bit circle read from the other end is itself turned by [5] bits

[checks202.py]
P1 header = address-wise map (drawn id, J flips palindromes, C flips all, sheet flips non-palindromes), n=2..12 both creases: True
P2 each map commutes with P on every word, n=2..12: True
runs rebuilt: 2464
P3 home <=> column parity mod gcd(L, stride) even: mismatches 0 of 2464
   slides returning home: 448 of 448
P4 runs reading every word once: 152  closing at k=0: 60
   closing runs whose closing rotations are exactly {0, N/2}: 60  other sets: 0
   non-facing full runs that face at some rotation: 4
P5 phases with every word once (drawn, own width):
   n= 6 crease 1: (0, 1, 2)
   n= 6 crease 0: (0, 1, 2)
   n= 7 crease 1: (0, 1, 2)
   n= 7 crease 0: (0, 1, 2)
   n= 8 crease 1: (0, 1, 2)
   n= 8 crease 0: (0, 1, 2)
   n= 9 crease 1: (0, 1, 2)
   n= 9 crease 0: (0, 1, 2)
   n=10 crease 1: (0, 1, 2)
   n=10 crease 0: (0, 1, 2)
   n=11 crease 1: (0, 1, 2)
   n=11 crease 0: (0, 1, 2)
   n=12 crease 1: (0, 1, 2)
   n=12 crease 0: (0, 1, 2)
   n=13 crease 1: (0, 1, 2)
   n=13 crease 0: (0, 1, 2)
   n=14 crease 1: (0, 1, 2)
   n=14 crease 0: (0, 1, 2)
P5 holds (all = (0, 1, 2)): True
```

**Scripts** (in full in `running-audit-10-scripts.md`): `ring_machine.py` sha `a6e94897e76ef7d3…`; `test_ring_machine.py` sha `6e897b9b8f01eb34…`; `build_notebook.py` sha `b67044ee1b0af592…`; `checks202.py` sha `9b36bc1e2dc585ad…`; `seal202/predictions.txt` sha `90723023128a7e06…`.
