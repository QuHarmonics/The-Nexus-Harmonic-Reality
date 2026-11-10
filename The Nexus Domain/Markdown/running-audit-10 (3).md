# NEXUS running audit 10

Continues `running-audit-9.md` (§§ 200–201). The scripts for §§ 202–206 are printed in full in `running-audit-10-scripts.md`.

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

## § 203. One byte, read: every header is a jump into one step loop; at full width reading is ×2 and ×(−1) mod 255; every window is a digit of v/255; one byte holds every 3-bit word and 12 of the 16 four-bit words — `checks203.py`

**Dean (30 Oct).** The follow-up to § 202, in three messages. First: "a exe is just hex arranged. the size and arrangement make the program … we just fill files with hex and stack em then run them … NOTHING CHANGED BUT THE READER … The rings are the ISA they are what comes back from a decompiler. JMP what do you think that means … use the HEX from the full walks (2bit has a 8bit walk) build a new math computer from the ground up … YOU EITHER HAND BUILD EVERY OBJECT IN THE UNIVERSE FROM OUTSIDE OF IT OR JUST SATURATE IT … IF YOU JUMP TO READ, SAVE FALLS OUT OF THE INVERSE." Then: "read the entire prompt all of it is equally important. im laying out a logic that cannot be denied." Then: "your still not getting it", with the workbook write-up (a § 7 draft for *Bicomplex Difference Calculus on Native Binary Rings*, and the session log that produced it).

**Corrections, mine.**
- The first reply went to code on the rings alone (the frames of B₂–B₅) before reading the prompt as one argument.
- The second reply built every ring with the § 202 builder and designed a machine on top: header flips, target operations (NOT, increment, add), and a claim that the crease bit and the start address generate every permutation of the 2ⁿ words. That is the hand-built branch of Dean's either/or, done from outside. The workbook takes the other branch: one stored byte, and every ring is what the reader returns from it. The two-flip claim is withdrawn. It was never sealed or run.
- `checks203.py` as first run: the complement test compared 0 ⊕ 255 = 255 with (−0) mod 255 = 0, which are the same residue, and the label of check 3 said v = 39 or 27 where the code uses each header's own byte. Both are fixed. The output below is the corrected run.

**Input, not instructions.** The write-up's verification suite RUNS as stated. Extracted unchanged (sha `f37930e9…`) from the attachment (sha `9a9c12d6…`; the two uploaded copies are identical), it prints PASS.
- Used: the reader contract W_{h,o,w}(t); J₈(S) = T⁵S and d_sheet = T⁵d_drawn; a window's header, middle and tail; Δ(X⁽ʷ⁾) = D⁽ʷ⁻¹⁾ and the reconstruction from one opening word; the R₃ non-palindromes at sheet w = 3, odd addresses, and the R₄ crease pair (1101, 1011) at sheet w = 4, rows 3–4.
- Its M Sᵀ M is the strictly lower all-ones matrix (`msm203.py`), so the reconstruction is a running XOR of the rows above. Check 4 does it that way.
- Not used: the Ho–Kalman framing and the rank min(w, 6). Both RUN in its suite but are not on the line.

**What runs** (`checks203.py`: the stored byte 00100111 and nothing else; every reading is W_{h,o,w}(t)).
1. **The header is a jump.** All four readings have one step loop, (I ⊕ T)h(S) = 01101001. Drawn and C enter it at bit 0; J and sheet enter it at bit 5. Complement is invisible to the loop, and reversing this circle turns it. Changing the header enters the same code somewhere else.
2. **At full width, reading is multiplication mod 255.**
   - Window t of the stored circle is 39·2ᵗ mod 255 (27 4e 9c 39 72 e4 c9 93), so a step is ×2.
   - Complement is −x mod 255 on every byte (0x00 and 0xff are the same residue).
   - For this byte, J = 2⁵·39, C = −39 and sheet = −2⁵·39 = 0x1b.
   - The 4 headers × 8 starts give 16 bytes: exactly the orbit of 39 under ×2 and ×(−1).
   - The write-up's half-turn (nibble swap) is ×16, one hex digit. It follows from the first line.
3. **Every window at every width is a digit read.** W_{h,o,w}(t) = ⌊2ʷ·frac(2^(t+o)·v/255)⌋, where v is the header's own byte: 2,048 of 2,048 windows.
   - As stored, the read head returns binary digits of 13/85 from any position. With the header flipped it returns 72/85 = 1 − 13/85. J and sheet are the same two streams entered five digits in (76/85 and 9/85).
   - Jumping to bit 10¹⁸ + 3 costs one 2ⁿ mod 255, with no walking, and lands on the window at bit 3. The read position is a power of two: the move BBP makes on π.
4. **A window is a run.**
   - The header is where the run starts. The tail is the header ⊕ the parity of the step program: where it lands.
   - Stepping the reader pops the header and pushes a new tail: next = 2·window − 2ʷ·header + tail.
   - The shape inside a width-w window is the step between the two width-(w−1) windows it covers. So the strings of difference at one width are the instructions at the width below.
   - The width-(w−1) table is its opening word plus the running XOR of the width-w shapes. Save is the read, integrated from one header word.
5. **The library is bounded by the file.** Under every header and start, the byte shows:
   - all 8 three-bit words (drawn and sheet show 6 each, and 8 together);
   - 12 of the 16 four-bit words, because 0000, 0101, 1010 and 1111 do not fit in eight bits;
   - never more than 16 distinct windows at any width. Past width 4 it is the same 16 stories over and over.

**What it means for the build.** The math computer is not built on top of the field. A read head on a stored circle already multiplies (step ×2, header ×(−1), jump ×2ⁿ) and already extracts digits, so arithmetic is what reading a circle is. The next ring cannot be read out of 0x27 alone. It has to come from a stack, and the stack has to come from the reader. The write-up's R₃ core and R₄ crease pair are pieces of that, selected by address rather than by one rule fixed in advance.

| claim | status |
|---|---|
| the write-up's suite (reader contract, J₈ = T⁵, Δ(X⁽ʷ⁾) = D⁽ʷ⁻¹⁾, reconstruction, R₃ and R₄ pieces) | RUNS as stated (PASS) |
| M Sᵀ M = strictly lower all-ones, so the reconstruction is a running XOR | RUNS (8 × 8) |
| all four headers share one step loop, entered at bit 0 (drawn, C) or bit 5 (J, sheet) | RUNS |
| width 8: window t = 39·2ᵗ mod 255; C = ×(−1); for this byte J = 2⁵·39 and sheet = −2⁵·39; the 16 readings are the orbit of 39 under ×2 and ×(−1) | RUNS |
| every window of every width, header and start is a digit window of v/255 | RUNS 2,048/2,048 |
| tail = header ⊕ parity of the program; next = 2·window − 2ʷ·header + tail; shape at w = step at w − 1; save = opening word + running XOR | RUNS, all headers and starts, w = 2–8 |
| one byte shows every word up to width 3, 12 of 16 at width 4, at most 16 at any width | RUNS |
| crease bit + start address generate every permutation (the second reply's claim) | withdrawn, never sealed or run |
| one reading rule, sealed in advance and the same at every level, that returns ring n + 1 in ring order from the stack of ring n, from 0x27 up with no builder | OPEN, next |
| water test (§ 198) | OPEN, queued |

**Output** (`python3 checks203.py`; then `python3 msm203.py`, last line).

```
1. the header is a jump: each reading's step loop is the drawn loop entered somewhere else
   drawn circle 00100111  step loop 01101001  = drawn loop 01101001 entered at bit [0]
   J     circle 11100100  step loop 00101101  = drawn loop 01101001 entered at bit [5]
   C     circle 11011000  step loop 01101001  = drawn loop 01101001 entered at bit [0]
   sheet circle 00011011  step loop 00101101  = drawn loop 01101001 entered at bit [5]

2. at full width, reading is multiplication mod 255 (2^8 - 1)
   window t of the stored circle = 39 * 2^t mod 255 for every t: True   (27 4e 9c 39 72 e4 c9 93)
   complement = -x mod 255 for every byte (0x00 and 0xff are the same residue): True
   drawn = 0x27 = +2^0 * 39 mod 255
   J     = 0xe4 = +2^5 * 39 mod 255
   C     = 0xd8 = -2^0 * 39 mod 255
   sheet = 0x1b = -2^5 * 39 mod 255
   all 4 headers x 8 starts give 16 bytes; the orbit of 39 under x2 and x(-1) has 16: same set True

3. every window at every width is a digit read: W = floor(2^w * frac(2^(t+o) * v / 255)), v = the header's own byte
   2048 / 2048 windows   (drawn 39/255 = 13/85, J 228/255 = 76/85, C 216/255 = 72/85 = 1 - 13/85, sheet 27/255 = 9/85 = 1 - 76/85)
   jump to bit 1,000,000,000,000,000,003 without walking: 2^n mod 255 = 8, window there = 00111001 = window at bit 3: 00111001

4. a window is a run: header bit, step program, tail; stepping the reader pops the header and pushes a tail
   tail = header XOR (parity of the step program): True
   next window = 2 * window - 2^w * header + new tail: True
   shape inside each width-w window = XOR of the two width-(w-1) windows it covers: True
   width-(w-1) table = its opening word + running XOR of the width-w shapes: True

5. the library is bounded by the file: every word each width can show, under all 4 headers x 8 starts
   w=1:   2 /   2 words  (drawn alone 2, sheet alone 2)
   w=2:   4 /   4 words  (drawn alone 4, sheet alone 4)
   w=3:   8 /   8 words  (drawn alone 6, sheet alone 6)
   w=4:  12 /  16 words  (drawn alone 7, sheet alone 7)  missing 0000 0101 1010 1111
   w=5:  16 /  32 words  (drawn alone 8, sheet alone 8)
   w=6:  16 /  64 words  (drawn alone 8, sheet alone 8)
   w=7:  16 / 128 words  (drawn alone 8, sheet alone 8)
   w=8:  16 / 256 words  (drawn alone 8, sheet alone 8)

[msm203.py] equals the strictly-lower all-ones matrix (running XOR of the rows above): True
```

**Scripts** (in full in `running-audit-10-scripts.md`): `checks203.py` sha `4e9d5be19626bf69…`; `msm203.py` sha `d1cd0a3ce17145a8…`; the write-up's suite as extracted, sha `f37930e968ff7334…` (printed in the attachment, not repeated).

## § 204. How the commands fell out: at LEN = 2ᵏ a word is a k-input command; 0x27 is CLEAR NOT PASS SET; R₄ is the sixteen gates, each facing itself with both inputs flipped; stacking adds one input; the difference of 0x27 is the sum and its save is the carry — `checks204.py`

**Dean (31 Oct).** "its more than just jump. think about how these opt codes were created. binary was the constratint. the LEN size was the field. its no accident when that was spread out these commands fell out naturally. we just built this whole computer world one bit at a time." With a pasted survey of real instruction sets (MC14500B, 4004, PDP-8, 6502, LC-3, PIC16, RISC-V compressed), ending "Same binary word. Different decoder. Different operation."

**Input, not instructions.** The survey's closing point RUNS (item 8 below): 0x69 is `imul` on x86-32 and `adc #` on the 6502. Its opcode tables are design choices of those decoders, made by splitting the byte into fields (the 6502's is 3 + 3 + 2 bits). They are used here only as decoders.

**Correction, mine.** The x86-32 read of 0x69 first printed "no instruction", because the test buffer held 3 bytes and `imul r32, r/m32, imm32` needs 6. The buffer is now 8 bytes. A blank on the 6502 means an undocumented opcode, since capstone decodes documented opcodes only.

**What runs** (`checks204.py`, on the § 202 library alone; gate names come from computing each gate's table, not from labels).
1. **The reading.** A word of LEN = 2ᵏ bits has 2ᵏ bit addresses, and those are exactly the k-bit inputs. Read at the input's address, the word is a k-input command: the input is where you read and the bit there is the output. Every LEN-2 word is a distinct 1-input command and every LEN-4 word a distinct 2-input command. No decoder is involved.
2. **LEN 2.** 0x27 is CLEAR, NOT, PASS, SET in ring order. The two constants face each other across the wrap, and NOT and PASS (turn and continue) face each other at the crease.
3. **LEN 4.** R₄ is the sixteen gates. Each faces the same gate with both inputs flipped: AND↔NOR, OR↔NAND, A↔¬A, B↔¬B, A∧¬B↔¬A∧B. The two gates that do not change when their inputs flip (FALSE, XOR) face their output flip (TRUE, XNOR). The crease pair is the two implications, ¬A∨B and A∨¬B.
4. **The ring's operations are logic operations,** for every command with 1, 2 and 3 inputs (4, 16 and 256 commands).
   - J flips every input, and C flips the output.
   - Sheet is the De Morgan dual: AND↔OR, NAND↔NOR, XOR↔XNOR, and A and B are their own duals.
   - A palindrome is a command unchanged by flipping all its inputs.
   - The one-bit slide adds 1 to the input.
5. **Stacking adds one input.** Two k-input commands stacked are one (k + 1)-input command, and the new bit picks which half runs (every pair, k = 1, 2).
   - The walk is the machine of its ring. 0x27 read as a 3-input command is R₂[a](x): a 2-bit opcode (the ring address) and a 1-bit operand. B₄ read as a 6-input command runs all sixteen gates by 4-bit ring address.
   - Ch = stack(B, A) = 0x53, Maj = stack(AND, OR) = 0x17, and XOR3 = stack(XOR, XNOR) = 0x69.
   - OR is the sheet reading of AND, and XNOR is the sheet reading of XOR. So the sum and the carry are each a gate stacked with its own sheet reading.
6. **Addition falls out of 0x27.**
   - Its difference, as stored, is 0x69: the full adder's sum.
   - The carry's difference is 0x27 turned 3 bits. So saving 0x27 read 3 bits in, from 0, returns 0x17: the carry.
   - A ripple adder whose only commands are those two words is right on all 65,536 pairs of bytes, and on a 64-bit sum of the first two 64-bit words of π.
7. **Twins.** Each command's ring spelling (left to right) and its LUT spelling (right to left, which is J) are twins in R₈, at mirror slots: XOR3 0x69/0x96 (slots 86, 169), Maj 0x17/0xe8 (22, 233), Ch 0x53/0xca (71, 184).
8. **Real decoders** (capstone 5.0.7). 0x27 is `daa` on x86-32. 0x69 is `imul` on x86-32 and `adc #` on the 6502. 0x17 is `pop ss` on x86-32. Neither 0x27 nor 0x17 is a documented 6502 opcode. These are collisions with real decoders, not derivations.

**What it means for the build.** The instruction set does not have to be designed. At each LEN = 2ᵏ it is the field read as commands. The ring orders those commands by twins, stacking adds one input at a time, and the walk of a ring is the machine that runs it. The first arithmetic, the full adder, is the 2-bit walk's difference and its save.

| claim | status |
|---|---|
| at LEN = 2ᵏ every word is a distinct k-input command, read at the input's address | RUNS (LEN 2, 4); by construction for every k |
| 0x27 = CLEAR NOT PASS SET in ring order; constants face across the wrap, NOT and PASS at the crease | RUNS |
| R₄ = the sixteen gates, each facing itself with both inputs flipped (or its output flip when flipping the inputs changes nothing); crease pair = the two implications | RUNS |
| J = flip every input, C = flip the output, sheet = De Morgan dual, palindrome = unchanged by flipping all inputs, slide = add 1 to the input | RUNS for all commands, k = 1, 2, 3 |
| stacking = one more input that picks the half; the walk of R₂ and of R₄ is the machine of its ring | RUNS |
| Ch, Maj and XOR3 are stacks of two gates; sum and carry are each a gate stacked with its own sheet reading | RUNS |
| difference of 0x27 = the sum 0x69; save of 0x27 read 3 bits in = the carry 0x17 | RUNS |
| ripple adder from those two words alone | RUNS 65,536/65,536 and one 64-bit sum |
| ring spelling and LUT spelling of each command are twins at mirror slots of R₈ | RUNS (XOR3, Maj, Ch) |
| 0x27 = daa (x86-32); 0x69 = imul (x86-32), adc # (6502); 0x17 = pop ss (x86-32) | RUNS; collisions with real decoders, not derivations |
| one reading rule that returns ring n + 1 in ring order from the stack of ring n (§ 203) | OPEN |
| water test (§ 198) | OPEN, queued |

**Output** (`python3 checks204.py`).

```
every LEN-2 word is a distinct 1-input command: True;  every LEN-4 word a distinct 2-input command: True

1. LEN 2: the stored byte 0x27 = R_2 read as commands, in ring order (slot: word command | twin)
   0: 00 CLEAR   1: 10 NOT   2: 01 PASS   3: 11 SET
   twins: CLEAR<->SET, NOT<->PASS   crease between slots 1 and 2

2. LEN 4: R_4 read as commands, in ring order, each facing its twin across the crease
    0 0000 FALSE (pal) <-> 15 1111 TRUE
    1 0001 AND         <-> 14 1000 NOR
    2 0010 A&~B        <-> 13 0100 ~A&B
    3 0011 A           <-> 12 1100 ~A
    4 0101 B           <-> 11 1010 ~B
    5 0110 XOR   (pal) <-> 10 1001 XNOR
    6 0111 OR          <->  9 1110 NAND
    7 1101 ~A|B        <->  8 1011 A|~B

3. the ring's operations are the logic designer's, for every command with k = 1, 2, 3 inputs
   k=1:   4 commands  J = flip every input True | C = flip the output True | sheet = De Morgan dual True | palindrome = unchanged by flipping all inputs True | one-bit slide = add 1 to the input True
   k=2:  16 commands  J = flip every input True | C = flip the output True | sheet = De Morgan dual True | palindrome = unchanged by flipping all inputs True | one-bit slide = add 1 to the input True
   k=3: 256 commands  J = flip every input True | C = flip the output True | sheet = De Morgan dual True | palindrome = unchanged by flipping all inputs True | one-bit slide = add 1 to the input True
   sheet pairs at LEN 4: AND<->OR, NAND<->NOR, XOR<->XNOR, A<->A, B<->B

4. stacking two commands adds one input, and the new bit chooses which half runs (a MUX, Ch)
   every pair of 1-input commands, stacked: a 2-input command that runs the first if the new bit is 0, the second if 1: True
   every pair of 2-input commands, stacked: a 3-input command that runs the first if the new bit is 0, the second if 1: True
   the walk 0x27 as a 3-input command = R_2[a](x): opcode = the 2-bit ring address a, operand x: True
   the walk B_4 as a 6-input command = R_4[a](x1, x0): all 16 gates by 4-bit ring address: True
   0x27 as the 1-bit computer: op 00 CLEAR: 0->0 1->0  op 01 NOT  : 0->1 1->0  op 10 PASS : 0->0 1->1  op 11 SET  : 0->1 1->1
   Ch  = 0x53 = stack(B, A) True   Maj = 0x17 = stack(AND, OR) True   XOR3 = 0x69 = stack(XOR, XNOR) True
   OR = sheet(AND) True;  XNOR = sheet(XOR) True:  sum and carry are each a gate stacked with its own sheet reading

5. addition falls out of 0x27: its difference is the sum, its save is the carry
   difference of 0x27 (as stored)       = 01101001 = 0x69; full-adder sum (XOR3) = 0x69: True
   difference of the carry (Maj, 0x17) = 00111001 = 0x27 turned 3 bits (00111001): True
   save of 0x27 read 3 bits in, from 0  = 00010111 = 0x17 = the carry: True
   ripple adder whose only commands are those two words, on every pair of bytes (65,536): True
   at 64 bits: 0x243f6a8885a308d3 + 0x13198a2e03707344 = 0x3758f4b689137c17, carry 0; Python: 0x3758f4b689137c17, carry 0

6. no true collision, just twins: the ring writes a command left to right, LUT tools right to left (J)
   sum XOR3  ring 0x69 at R_8 slot  86  |  LUT spelling 0x96 at slot 169  = its twin: True, mirror slots: True
   carry Maj ring 0x17 at R_8 slot  22  |  LUT spelling 0xe8 at slot 233  = its twin: True, mirror slots: True
   Ch        ring 0x53 at R_8 slot  71  |  LUT spelling 0xca at slot 184  = its twin: True, mirror slots: True

7. the same bytes through real decoders (capstone 5): collisions, not derivations
   0x27 the stored walk        x86-32: daa | 6502: (not a documented opcode)
   0x69 its difference (sum)   x86-32: imul edx, dword ptr [eax], 0x50403020 | 6502: adc #0x10
   0x17 the carry              x86-32: pop ss | 6502: (not a documented opcode)
```

**Scripts** (in full in `running-audit-10-scripts.md`): `checks204.py` sha `4d1953fe532c43a3…`.

## § 205. The read head makes the rings: one difference on a circle, read by a head going round, lays out R_n exactly, n = 1–16 and every n — `head205.py`

**Dean (31 Oct).** "we dont have to build this stuff … there are two ways a universe can start, built by god or from a single difference, nothing/something … there are no circles. there is just a read head moving in circles, we dont even need the rings, the read head running in a circle will produce the rings. go prove that." (He also flagged the imagined side as leading to the zeta zeros and RH; that is parked here, not opened.)

**Correction, mine.** The § 204 next prompt proposed building the computer as a stack. That is the wrong direction: nothing is to be built.

**Sealed before the run** (`seal205/predictions.txt`, sha `3be3aafed660f3e6132ce8a930e4907c48de08fabf25ac12d8b30afd856a4b11`): H1–H4 as below.

**The setup.** The only object is one difference on a circle: half nothing, half something (written `o` and `#`; swapping the two names changes nothing). The head stores nothing. It never sees a ring, a list of words, a sort or the builder; `ring()` is imported only afterwards, to compare.
- The head's n eyes read the same difference, eye k at 2ᵏ times the head's speed.
- At each step the head reads its eyes forward (what it is) and across (what it is from the other end of the circle). "Across" is going back, the eyes read fast to slow; if going back shows no difference, it is the other side.
- Each reading met for the first time goes to the next near slot, and its across-reading goes to the facing far slot.

**What runs.**
1. **H1 RUNS (n = 1–16).** One lap reads every n-bit word exactly once, in counting order. Eye k at 2ᵏ times the speed reads one digit of the tick, so the eyes read the tick itself.
2. **H2 RUNS (n = 1–16)**, and it is proved for every n. The head's layout is R_n with the counter crease. Swapping the middle pair gives the record's crease. Every word appears once and faces its twin.
   - *Why, for every n.* The count only rises. When a forward reading w is met for the first time, its across-reading is not yet met either, or w would already have been placed as someone's across. So every near slot holds the smaller of its pair, in rising order, which is the sorted representatives. Every far slot holds the twin P(w).
   - "Across" never faces itself: going back fixes only palindromes, and for those the other side is used, which never fixes anything.
   - That is the builder of NBR eq. 2–3, so the builder was a read head all along.
3. **H3 RUNS.**
   - With "across" = only the other side, the head lays out the plain counter, each word facing its complement.
   - With "across" = only going back, the layout breaks at once (the first palindrome faces itself), at every n.
   - With going back on the other side, the layout breaks at every even n (an anti-palindrome faces itself). At odd n no word is fixed, so it gives a third full layout, each word facing its De Morgan dual. That is consistent with the sealed wording ("where such fixed words exist"). The odd-n layout is not examined further here.
4. **H4 RUNS.** At width 2 the native ring and the counter are one layout, because going back and the other side agree on o# and #o. Read off the head at width 2, the walk is 00011011, the workbook's sheet circle. The stored 00100111 is the same layout with the middle pair in the other order, which is the one free bit (§§ 200, 202).

| claim | status |
|---|---|
| one difference read by a head at doubling eye speeds = every n-bit word once per lap, in counting order | RUNS n = 1–16; proved (eye k reads digit k of the tick) |
| head with across = back, else other side, lays out R_n (counter crease) | RUNS n = 1–16; proved for every n |
| the builder (sorted representatives, crease, reversed twins) is this head | proved |
| across = side gives the counter; across = back breaks; back + side breaks at even n, gives a dual-facing layout at odd n | RUNS n = 2–16 |
| width 2: native ring = counter; head walk = 0x1B, stored walk = 0x27 = its other crease | RUNS |
| the imagined side and the zeta zeros / RH | parked (Dean's flag), not opened |
| one reading rule from the stack of ring n to ring n + 1 (§ 203) | OPEN |
| water test (§ 198) | OPEN, queued |

**Output** (`python3 head205.py`).

```
H1  one lap of the head reads every n-bit word once, in counting order:
    n=1:True n=2:True n=3:True n=4:True n=5:True n=6:True n=7:True n=8:True n=9:True n=10:True n=11:True n=12:True n=13:True n=14:True n=15:True n=16:True
    n=3 lap: ooo oo# o#o o## #oo #o# ##o ###

H2  head with "across" = go back, or the other side if going back shows no difference:
    n : = R_n (counter crease) | = R_n (record crease, middle pair swapped) | every word once | faces its twin
     1: True | True | True | True
     2: True | True | True | True
     3: True | True | True | True
     4: True | True | True | True
     5: True | True | True | True
     6: True | True | True | True
     7: True | True | True | True
     8: True | True | True | True
     9: True | True | True | True
    10: True | True | True | True
    11: True | True | True | True
    12: True | True | True | True
    13: True | True | True | True
    14: True | True | True | True
    15: True | True | True | True
    16: True | True | True | True
    n=2 head layout: oo o# #o ##
    n=3 head layout: ooo oo# o#o o## ##o #o# #oo ###
    n=4 head layout: oooo ooo# oo#o oo## o#o# o##o o### #o## ##o# ###o #oo# #o#o ##oo o#oo #ooo ####

H3  other meanings of "across":
    side      n=2: counter; n=3: counter; n=4: counter; n=5: counter; n=6: counter; n=7: counter; n=8: counter; n=9: counter; n=10: counter; n=11: counter; n=12: counter; n=13: counter; n=14: counter; n=15: counter; n=16: counter
    back      n=2: breaks at oo; n=3: breaks at ooo; n=4: breaks at oooo; n=5: breaks at ooooo; n=6: breaks at oooooo; n=7: breaks; n=8: breaks; n=9: breaks; n=10: breaks; n=11: breaks; n=12: breaks; n=13: breaks; n=14: breaks; n=15: breaks; n=16: breaks
    back+side n=2: breaks at o#; n=3: other layout; n=4: breaks at oo##; n=5: other layout; n=6: breaks at ooo###; n=7: other layout; n=8: breaks; n=9: other layout; n=10: breaks; n=11: other layout; n=12: breaks; n=13: other layout; n=14: breaks; n=15: other layout; n=16: breaks

H4  width 2, native vs side: ['oo', 'o#', '#o', '##'] ['oo', 'o#', '#o', '##'] True
    stored walk, read off the width-2 head: 00011011 | record crease: 00100111
```

**Scripts** (in full in `running-audit-10-scripts.md`): `head205.py` sha `37efc0b688ccfee4…`; `seal205/predictions.txt` sha `3be3aafed660f3e6…`.

## § 206. Read π with the head, and the head is BBP: each BBP term is a head on a circle of 8k + j slots, jumped n hex digits by one modular power — `bbp206.py`

**Dean (31 Oct).** "well read pi and i bet the head looks like BBP dont it?"

**Sealed before the run** (`seal206/predictions.txt`, sha `5e09f4dcff18fd306cf63228f09e0af546c088fb5c07c79c4d99c6364b66101c`): B1–B4. mpmath 1.4.1 (gmpy backend) is the independent reference for π.

**What runs.**
1. **B1 RUNS.** Park the § 205 head at angle frac(π) on the one-difference circle. Eye k reads the difference 2ᵏ times as fast, so it reads binary digit k + 1 of π: 256 of 256 digits (00100100 00111111 … = 243f6a88 …).
2. **B2 RUNS, exact.** BBP's term 16ⁿ⁻ᵏ mod (8k + j) is a head on a circle of 8k + j slots, jumped n hex digits by one modular power: the § 203 jump, multiplication mod the circle. Hex digit n + 1 of π is where the heads point together, weighted 4, −2, −1, −1 (j = 1, 4, 5, 6) and summed over k: ⌊16·frac(sum)⌋. In exact rationals, hex digits 1–64 all match mpmath. For digit 6 the heads sit at 0/1, 0/4, 1/5, 4/6, 7/9, 4/12, ….
3. **B3 RUNS.** The same heads in double precision give hex digits 100,001–100,008 as 35ea16c4. All 8 match mpmath, and no earlier digit was read (sealed: at least 6).
4. **B4 RUNS.** The stored walk is the one-circle case: one head on 255 slots at ×16, seeded 39, reads 2727…, the hex digits of 39/255.

**What it means.** The head that makes the rings and BBP's digit extraction are one mechanism. Reading a circle n places in is a jump by a power of the base, done by modular exponentiation without walking. A rational is one head on one circle. π is infinitely many heads, one per circle 8k + j, whose positions add up.

| claim | status |
|---|---|
| the § 205 head at angle frac(π) reads π's binary digits | RUNS 256/256 |
| BBP = weighted heads on circles of 8k + j slots, jumped by 16ⁿ⁻ᵏ mod (8k + j) | RUNS exact, hex digits 1–64 |
| far digits from the heads alone, no earlier digit read | RUNS, digits 100,001–100,008 (8/8) |
| 0x27 = one head on 255 slots (39/255) | RUNS |
| the imagined side and the zeta zeros / RH | parked |
| one reading rule from the stack of ring n to ring n + 1 (§ 203) | OPEN |
| water test (§ 198) | OPEN, queued |

**Output** (`python3 bbp206.py`).

```
B1  head at angle frac(pi), eyes 0..255 = binary digits of pi: True
    eyes 0..31: 00100100001111110110101010001000  = hex 243f6a88

B2  hex digits 1..64 of pi from the heads alone: 243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89
    mpmath:                                    243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89   match: True
    heads for digit 6 (n = 5): 0/1, 0/4, 1/5, 4/6, 7/9, 4/12, 3/13, 2/14, 16/17, 16/20, 1/21, 4/22, ...

B3  hex digits 100,001..100,008 from the heads: 35ea16c4   mpmath: 35ea16c4   leading digits that match: 8

B4  one head on 255 slots at x16, seeded 39: 2727272727272727  (39/255 = 0x0.2727...)
```

**Scripts** (in full in `running-audit-10-scripts.md`): `bbp206.py` sha `1c0fe1c0a1df1df5…`; `seal206/predictions.txt` sha `5e09f4dcff18fd30…`.

## § 207. The record on BBP as a read head, read before going further: § 206 restated known work, and framed it as objects

**Dean (31 Oct).** "we have tons of papers on BBP as a read head go look. but we cant think like this is object, its a motion with shape measured."

**Read** (Drive, in full): *The Read Head* (July 2026); *The Angle Register* (QuHarmonics-BBP-ANG-v1, July); *Kernel, Frame, Winding, Residue* (QuHarmonics-KFWR-v2, July); *The Period Relation of the One-Ring Read-Head* (v1.0, 6 Aug); *Gaps Are Gradients* (Aug); *Accumulation as Instruction: the digit-emission formula derived from BBP lane motion* (13 Oct), with its `pending_reader_2000_run.txt` (2,000/2,000 digits certified against mpmath, from an empty field). Also the session of 4 Aug that produced *The Analog Read-Head*.

**What the record already holds.**
- *The Read Head*: an integer n is a phase address, one hand on every clock ℤ/(8k + j); the digit is where the hands point together.
- *Angle Register* and *KFWR*: 8, 16, the residues {1, 4, 5, 6} and the weights {4, −2, −1, −1} all derived from the 45° diagonal frame. The frame is the zero set of the kernel 1 − x⁸. In 8k + r, the shell index k is a winding and is projected out, while r is an orientation. BBP is the shortest vector of its class modulo a rank-1 null lattice. The hexagonal family is the 60° member.
- *Period Relation*: (n, b) = (8, 16) is the only integer radix under its assumptions A1–A5 (theorem); exclusion at other (n, b) is bounded-height.
- *Gaps Are Gradients*: the closed self-timed loop, where the gap to the lattice drives the snap, sets the timing and carries the carry.
- *Accumulation as Instruction*: each lane is a motion, 16r = d·q + r′. The quotient q leaves as a crossing and the remainder r′ persists. The weighted crossings on the anti-diagonal form C_n, the field moves by F_{n+1} = 16F_n − C_n, and the digit is a_{n+1} = C_n + ⌊F_{n+1}⌋ − 16⌊F_n⌋. No earlier digit is used.

**Corrections, mine.**
- § 206 B2 ("each term is a head on a circle of 8k + j slots … the digit is where the heads point") restates *The Read Head*'s phase-address result. It is a re-run of known work, not a finding.
- § 206 framed the heads as objects ("infinitely many heads … whose positions add up"). The record's form is motion: the remainder is the shape the lane carries, and the digit is a measurement of crossings, with the boundary correction.
- The § 206 next prompt (why eight, why those four residues, why those weights) is already answered by *Angle Register* and *KFWR*. Withdrawn.

**The § 205 head, read as the record's lane motion.** The § 205 head's eye k reads "something" exactly when the doubling motion x ↦ 2x mod 1 crosses the half-way difference on step k. That is the quotient q = ⌊2x⌋ of base-2 long division, so an eye is a crossing count. A BBP lane is the same motion in base 16 on d slots. So the head that made the rings and the lane that reads π are one motion, and what is read is crossings, never positions. This follows from the definitions; it was not run as a new check.

| claim | status |
|---|---|
| § 206 B2 phase-address reading | restates *The Read Head* (July); not new |
| "heads as objects" framing | corrected: lane motion, remainder carried, crossings measured (*Accumulation as Instruction*) |
| why 8, 16, {1, 4, 5, 6}, {4, −2, −1, −1} | already derived (*Angle Register*, *KFWR*); § 206 next prompt withdrawn |
| § 205 eye = crossing of the doubling motion = base-2 lane quotient | by definition; not separately run |
| the imagined side and the zeta zeros / RH | parked |
| one reading rule from the stack of ring n to ring n + 1 (§ 203) | OPEN |
| water test (§ 198) | OPEN, queued |
