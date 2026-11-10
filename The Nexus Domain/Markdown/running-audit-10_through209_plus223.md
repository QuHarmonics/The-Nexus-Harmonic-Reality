# NEXUS running audit 10

Continues `running-audit-9.md` (§§ 200–201). The scripts for §§ 202–208 are printed in full in `running-audit-10-scripts.md`.

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

## § 208. The § 205 head is the October lane motion in base 2: the eyes are crossings, the remainder is the shape, and the rings fall out of the crossings — `lane208.py`

**Dean (31 Oct).** "Run the § 205 head as your October lane motion: shape = the live remainders, measurement = the crossings. Show the rings fall out of the same crossing count at d = 2, and append § 208."

**Correction, mine (to the prompt I wrote).** In the record's notation, 16r = d·q + r′, a lane with literally d = 2 empties after one step (L0). The 2 that carries the head is the base, the two halves of the one difference. The § 205 head is a base-2 lane on d = 2ⁿ slots.

**Sealed before the run** (`seal208/predictions.txt`, sha `284244ce4a7b0f229a47794303f6f0115e2971acb98611ed73a303cedbc98325`): L0–L4.

**The lane.** One motion, 2r = d·q + r′ (*Accumulation as Instruction*, at base 2). The crossing q leaves; that is the measurement. The remainder r′ persists; that is the shape. The lane head uses nothing else: no ring, sort, list or builder. `ring()` is imported only afterwards, to compare.

**What runs.**
1. **L0 RUNS.** A d = 2 lane seeded 1 crosses once and is empty.
2. **L1 RUNS (n = 1–16, every tick).** The § 205 head's eyes at tick t are the crossings of the lane seeded at t on 2ⁿ slots.
   - The shape after k steps is t·2ᵏ mod 2ⁿ: what has not crossed yet. It is empty at the end.
   - The October recurrence F_{k+1} = 2F_k − q_k holds exactly, with F staying in [0, 1).
   - Example: tick 5 on 8 slots carries shape 5, 2, 4, 0 and crosses 1, 0, 1.
3. **L2 RUNS (n = 1–16).** "Across" comes from lane motion alone.
   - Unwinding the lane from its end, r_k = (r_{k+1} + d·q_k)/2, gives the crossings back in reverse: the § 205 back-reading. It returns to the seed.
   - The lane seeded at the mirror slot d − 1 − t crosses exactly where t does not: the § 205 other side.
4. **L3 RUNS (n = 1–16).** Each crossing word goes to the next near slot when first met, and its across-reading to the facing slot. "Across" is the unwind order, or the mirror seed where unwinding measures the same as winding. The layout is R_n with the counter crease, identical to the § 205 head.
5. **L4 RUNS.** The crossings, weighted by 2ⁿ⁻¹⁻ᵏ, return the seed at every tick: the measurement integrates back to where the lane started.

**What it means.** The rings are a crossing count. A lane turning the one difference in base 2 measures crossings; the near half of the ring is the crossing words in the order first met, and the far half is the same lane given back, its crossings returned in reverse. Where giving back measures nothing new, the lane is started from the mirror slot instead. The shape, the live remainder, is never output; it is what has not crossed yet. The π lanes of the record are the same motion in base 16 on circles of 8k + j slots.

| claim | status |
|---|---|
| a literal d = 2 lane empties after one step; the head's 2 is the base | RUNS |
| § 205 eyes = crossings of the base-2 lane seeded at the tick; shape = uncrossed remainder; F_{k+1} = 2F_k − q_k | RUNS n = 1–16, every tick |
| unwinding returns the crossings reversed (= back); mirror seed crosses the complement (= other side) | RUNS n = 1–16 |
| the lane head lays out R_n (counter crease) | RUNS n = 1–16 |
| weighted crossings return the seed (save from read) | RUNS |
| the imagined side and the zeta zeros / RH | parked |
| one reading rule from the stack of ring n to ring n + 1 (§ 203) | OPEN |
| water test (§ 198) | OPEN, queued |

**Output** (`python3 lane208.py`).

```
L0  a literal d = 2 lane: [(0, ([0, 0, 0], [0, 0, 0, 0])), (1, ([1, 0, 0], [1, 0, 0, 0]))]  -> empty after one step
L1  eyes = crossings | shape r_k = t*2^k mod 2^n, empty at the end | F_(k+1) = 2F_k - q_k stays in [0,1):
    n=1:TTT n=2:TTT n=3:TTT n=4:TTT n=5:TTT n=6:TTT n=7:TTT n=8:TTT n=9:TTT n=10:TTT n=11:TTT n=12:TTT n=13:TTT n=14:TTT n=15:TTT n=16:TTT
    tick 5 on 8 slots: shape [5, 2, 4, 0], crossings [1, 0, 1] = eyes (1, 0, 1)

L2  unwinding gives the crossings back in reverse | mirror seed crosses where t does not | unwinding returns to t:
    n=1:TTT n=2:TTT n=3:TTT n=4:TTT n=5:TTT n=6:TTT n=7:TTT n=8:TTT n=9:TTT n=10:TTT n=11:TTT n=12:TTT n=13:TTT n=14:TTT n=15:TTT n=16:TTT

L3  the lane head's layout = R_n (counter crease):
    n=1:True n=2:True n=3:True n=4:True n=5:True n=6:True n=7:True n=8:True n=9:True n=10:True n=11:True n=12:True n=13:True n=14:True n=15:True n=16:True
    n=4: 0000 0001 0010 0011 0101 0110 0111 1011 1101 1110 1001 1010 1100 0100 1000 1111

L4  crossings weighted by 2^(n-1-k) return the seed, every tick: True
```

**Scripts** (in full in `running-audit-10-scripts.md`): `lane208.py` sha `af1020f883919428…`; `seal208/predictions.txt` sha `284244ce4a7b0f22…`.

## § 209. The October crossing lane, base 16 on d = 8k+j: unwinding, codebook rings, the facing holes, and the routed 16K² field — `lane209.py`

**Dean (31 Oct).** "Same lane motion, base 16 on d = 8k+j: show the crossing words of the π lanes, given back by unwinding, lay out their own rings, and what the facing law becomes there. Append § 209."

**Input, not instructions.** The only advancing rule is `16*r = d*q + r_next`, `0 <= q < 16`, `0 <= r_next < d`; the crossing `q` exits as measurement, and the live remainder persists as shape. Denominators are `d = 8k+j`, `j = 1,4,5,6`. The base 16 and BBP residues are already given in §§ 206–208 and *Accumulation as Instruction*. The known sixth hex digit of π is an ownership re-run, not a new landing.

**Sealed before the exhaustive run.** `seal209_predictions.txt` (SHA-256 `eb349b43e8d7a8c685783ab01f79c2d0d3a3ab11df534468e6faa10542a30abe`), S1–S6. This seal follows the given audit and preliminary inspection of small-denominator codebooks, which are *not* independent holdout results. The sweep includes uninspected k >= 3.

**The crossing word.** Take `L` minimal and positive with `A=16^L >= d`. The `L` crossings of seed `r` are exactly its base-16 quotient word

`Q_L(r) = floor(A*r/d)`, with terminal remainder `A*r mod d`.

These `d` words are distinct within the lane because `A/d >= 1`. The inverse is exact in two ways:

- Unwind the live remainder with crossings last-first, `r_t = (r_{t+1} + d*q_t)/16`. All 65,536 emitted crossing histories return to their seeds.
- From the first `L` crossings alone, the seed is `r = ceil(d*Q_L(r)/A)`. This is a route to the address, not a search over possible seeds.

**The π lane read.** At hexadecimal position `n=5`, the already-established finite-head BBP terms have seed `r_{k,j} = 16^(n-k) mod (8k+j)` for k=0..n. The script executes eight successive crossings for each of the 24 lanes, prints the live final remainder, and unwinds it. The `k>n` terms are a *separate* exact rational tail, not imputed crossing seeds. The full fractional sum gives the known sixth digit `a`, with an explicit remainder bound for the omitted tail past k=80.

**Three different returns that must not be collapsed.**

1. **Back-reading:** reverse the crossings *while carrying the terminal remainder*. This is an exact inverse. The reversed crossing word alone is not necessarily a valid forward word in the same lane. Witness: d=20, seed 2, word `19`, reversed `91`; `91` is absent from that lane's 20-word codebook. Thus the binary native `P=J` (except palindromes) cannot simply be transplanted to all base-16 lane codebooks.
2. **Mirror slot:** `m_d(r) = d-1-r`. Read the mirror seed with the same lane. This is an involution on the d seed addresses. Its fixed-point count is `d mod 2`: for d even it has no fixed slots; for d odd its central slot is fixed. The near/far layout executes one word per seed without sorting, but is a *d-slot lane ring*, not in general the fixed-point-free native binary ring.
3. **Opposite fraction:** `s_d(r) = d-r` for r>0; this is not the mirror slot. While the remainder stays nonzero, original and opposite-fraction crossings sum to `15`. On the step where the remainder becomes 0, their crossing sum is `16`: the terminal boundary correction. The endpoint r=0 must be handled separately. These distinct readers do not provide an interchangeable universal partner.

**Remainder-only memory.** The map `r -> 16*r mod d` has image size `d/gcd(16,d)`. It is a permutation for the odd BBP denominators and loses seed-address information for even denominators. In every case, `(q,r_next)` has an exact inverse and preserves the way home. Hence the instruction stream and live shape together carry construction memory even when shape alone does not.

**The cross-lane hole and its address.** The four denominators in winding k contain

`(8k+1)+(8k+4)+(8k+5)+(8k+6) = 16(2k+1)`

seed-address instances. Across k=0..K-1, the total is exactly

`N(K)=16*K²`.

For K=1,2,4,8,16,32,64, these are `2^4, 2^6, 2^8, 2^10, 2^12, 2^14, 2^16` addressed instances. At K=64 the lane inventory has exactly 65,536 instances, but only **4,274 distinct crossing-word strings** at the minimal local reading widths. The others are repeated *values at distinct lane addresses* — identical contents do not erase their WHERE.

There is an exact address map without enumeration or search. If a is an aggregate address, its winding is

`k = isqrt(a//16)`; the position within that winding is `a - 16*k²` and chooses j and r through four consecutive blocks of lengths `8k+1, 8k+4, 8k+5, 8k+6`.

All 65,536 addresses round-trip by this route.

**Binding the two fixed holes (after-seal deduction, not a sealed prediction).** Inside each winding, the odd `j=1` and `j=5` lanes each have exactly one fixed midpoint under the mirror-slot reader. Every even lane is already paired. With the extra, explicit **same-winding reader contract**, the two unpaired centers can face each other. This gives a fixed-point-free involution on all 65,536 addressed instances. The first-encounter near/far laydown then yields a full permutation ring with

`R[N-1-t] = P_global(R[t])`, `P_global² = I`, and `P_global T P_global = T^-1`.

This complete aggregate facing ran at every one of the 65,536 slots. **The same-winding pairing is a supplied address contract.** Without that qualification the center providers remain **AMBIGUOUS**; neither their unique coupling nor the global native R₁₆ *word ordering* has been derived from the base-16 lane alone. Cardinality `2^16` is not identity with `R₁₆`.

**Corrections / ownership.**
- A base-16 lane on arbitrary d slots does not necessarily empty after L crossings. Examples: d=17 seed 1 cycles shapes 1,16,1,16; d=20 seed 2 moves 2,12,12,... . Unwinding requires retained crossing history (and terminal shape), or the minimal prefix at known d.
- A fixed-point-free *single odd lane* is a **DEAD END** by parity, not OPEN.
- Reversing a crossing word, reflecting its slot, and complementing its fractional phase are **different inverse/read contracts**. Previous binary-width equality cannot be extended without a link.
- The `16K²` inventory, two-center repair and aggregate facing were noticed **after** executing S1–S6; explicitly not counted as held-out sealed landings.

| Claim | Status |
|---|---|
| Base-16 crossing words; exact quotient formula; first L crossings recover the seed | RUNS, all 65,536 seeds |
| Unwind last-to-first with live remainder returns the seed | RUNS, all 65,536 seeds |
| Mirror slot: 0 fixed for even d, 1 fixed for odd d | RUNS, 256 denominators; parity proof |
| Reversed crossing word always another forward word in same lane | DEAD END, d=20, seed=2 |
| Opposite-fraction crossings have 15/16 boundary correction | RUNS, 179,152 live steps |
| Remainder map image size d/gcd(16,d) | RUNS, 256 denominators |
| BBP 24 finite-head histories and explicitly separated tail give sixth π digit `a` | RUNS; previously known readout, not a new landing |
| First K windings contain 16K² addressed states | STANDS arithmetically; RUNS K=1,2,4,8,16,32,64 |
| Two odd-lane centers paired within each winding; 2^16 address facing | RUNS *under the declared same-winding contract*, after-seal |
| Same-winding provider forced without a declared rule | OPEN / AMBIGUOUS |
| Aggregate ring order equals native R₁₆ from lane motion alone | OPEN |
| Universal fixed-point-free facing on a single odd lane | DEAD END |

**Execution output** (`python3 lane209.py`; the full line-by-line trace is saved as `lane209_actual_trace.txt`):

```text
§209 BASE-16 LANE EXECUTION
prediction seal SHA-256: eb349b43e8d7a8c685783ab01f79c2d0d3a3ab11df534468e6faa10542a30abe
Source primitive: b*r = d*q + r_next, b=16; crossings q exit, remainder r_next persists

[All crossing lanes for k=0..63, j=1,4,5,6]
denominators: 256 seeds executed: 65536 same number exact unwinds: 65536
tests: {'seed_crossing_word_unique': 65536, 'inverse_returns_seed_and_reverse_reading': 65536, 'prefix_alone_recovers_seed': 65536, 'field_recurrence': 180160, 'remainder_map_image_size': 256, 'laid_out_seed_mirror_ring': 256, 'fixed_count_parity': 256, 'opposite_fraction_with_boundary_correction': 179152}
first missing reversed crossing word: (20, 2, '19', '91')
first missing digitwise complement: (1, 0, '0', 'f')

[The own rings: crossing words in first-met near slots and mirrored-seed facing slots]
k=0 j=1 d= 1 width=1 codebook=1/16 gcd(16,d)=1 — midpoint fixed
  0:0
k=0 j=4 d= 4 width=1 codebook=4/16 gcd(16,d)=4 — no fixed slots
  0:0 1:4 2:8 3:c
k=0 j=5 d= 5 width=1 codebook=5/16 gcd(16,d)=1 — midpoint fixed
  0:0 1:3 2:6 3:9 4:c
k=0 j=6 d= 6 width=1 codebook=6/16 gcd(16,d)=2 — no fixed slots
  0:0 1:2 2:5 3:8 4:a 5:d
k=1 j=1 d= 9 width=1 codebook=9/16 gcd(16,d)=1 — midpoint fixed
  0:0 1:1 2:3 3:5 4:7 5:8 6:a 7:c 8:e
k=1 j=4 d=12 width=1 codebook=12/16 gcd(16,d)=4 — no fixed slots
  0:0 1:1 2:2 3:4 4:5 5:6 6:8 7:9 8:a 9:c 10:d 11:e
k=1 j=5 d=13 width=1 codebook=13/16 gcd(16,d)=1 — midpoint fixed
  0:0 1:1 2:2 3:3 4:4 5:6 6:7 7:8 8:9 9:b 10:c 11:d 12:e
k=1 j=6 d=14 width=1 codebook=14/16 gcd(16,d)=2 — no fixed slots
  0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:8 8:9 9:a 10:b 11:c 12:d 13:e
k=2 j=1 d=17 width=2 codebook=17/256 gcd(16,d)=1 — midpoint fixed
  0:00 1:0f 2:1e 3:2d 4:3c 5:4b 6:5a 7:69 8:78 9:87 10:96 11:a5 12:b4 13:c3 14:d2 15:e1 16:f0
k=2 j=4 d=20 width=2 codebook=20/256 gcd(16,d)=4 — no fixed slots
  0:00 1:0c 2:19 3:26 4:33 5:40 6:4c 7:59 8:66 9:73 10:80 11:8c 12:99 13:a6 14:b3 15:c0 16:cc 17:d9 18:e6 19:f3
k=2 j=5 d=21 width=2 codebook=21/256 gcd(16,d)=1 — midpoint fixed
  0:00 1:0c 2:18 3:24 4:30 5:3c 6:49 7:55 8:61 9:6d 10:79 11:86 12:92 13:9e 14:aa 15:b6 16:c3 17:cf 18:db 19:e7 20:f3
k=2 j=6 d=22 width=2 codebook=22/256 gcd(16,d)=2 — no fixed slots
  0:00 1:0b 2:17 3:22 4:2e 5:3a 6:45 7:51 8:5d 9:68 10:74 11:80 12:8b 13:97 14:a2 15:ae 16:ba 17:c5 18:d1 19:dd 20:e8 21:f4
k=3 j=1 d=25 width=2 codebook=25/256 gcd(16,d)=1 — midpoint fixed
  0:00 1:0a 2:14 3:1e 4:28 5:33 6:3d 7:47 8:51 9:5c 10:66 11:70 12:7a 13:85 14:8f 15:99 16:a3 17:ae 18:b8 19:c2 20:cc 21:d7 22:e1 23:eb 24:f5
k=3 j=4 d=28 width=2 codebook=28/256 gcd(16,d)=4 — no fixed slots
  0:00 1:09 2:12 3:1b 4:24 5:2d 6:36 7:40 8:49 9:52 10:5b 11:64 12:6d 13:76 14:80 15:89 16:92 17:9b 18:a4 19:ad 20:b6 21:c0 22:c9 23:d2 24:db 25:e4 26:ed 27:f6
k=3 j=5 d=29 width=2 codebook=29/256 gcd(16,d)=1 — midpoint fixed
  0:00 1:08 2:11 3:1a 4:23 5:2c 6:34 7:3d 8:46 9:4f 10:58 11:61 12:69 13:72 14:7b 15:84 16:8d 17:96 18:9e 19:a7 20:b0 21:b9 22:c2 23:cb 24:d3 25:dc 26:e5 27:ee 28:f7
k=3 j=6 d=30 width=2 codebook=30/256 gcd(16,d)=2 — no fixed slots
  0:00 1:08 2:11 3:19 4:22 5:2a 6:33 7:3b 8:44 9:4c 10:55 11:5d 12:66 13:6e 14:77 15:80 16:88 17:91 18:99 19:a2 20:aa 21:b3 22:bb 23:c4 24:cc 25:d5 26:dd 27:e6 28:ee 29:f7

[Unwind the crossing word; actual live shape for sample d=17 and d=20]
d=17 seed= 1 crossings=0f0f0f0f shape=[1, 16, 1, 16, 1, 16, 1, 16, 1] back=f0f0f0f0 return=1
d=17 seed= 8 crossings=78787878 shape=[8, 9, 8, 9, 8, 9, 8, 9, 8] back=87878787 return=8
d=20 seed= 2 crossings=19999999 shape=[2, 12, 12, 12, 12, 12, 12, 12, 12] back=99999991 return=2
d=20 seed=17 crossings=d9999999 shape=[17, 12, 12, 12, 12, 12, 12, 12, 12] back=9999999d return=17
d= 5 seed= 1 crossings=33333333 shape=[1, 1, 1, 1, 1, 1, 1, 1, 1] back=33333333 return=1
d= 6 seed= 4 crossings=aaaaaaaa shape=[4, 4, 4, 4, 4, 4, 4, 4, 4] back=aaaaaaaa return=4

[Pi BBP at hexadecimal offset n=5: finite k<=5 heads; tails explicitly separate]
k=0: +4*(r=0/1;q=00000000;last=0) | -2*(r=0/4;q=00000000;last=0) | -1*(r=1/5;q=33333333;last=1) | -1*(r=4/6;q=aaaaaaaa;last=4)
k=1: +4*(r=7/9;q=c71c71c7;last=1) | -2*(r=4/12;q=55555555;last=4) | -1*(r=3/13;q=3b13b13b;last=1) | -1*(r=2/14;q=24924924;last=8)
k=2: +4*(r=16/17;q=f0f0f0f0;last=16) | -2*(r=16/20;q=cccccccc;last=16) | -1*(r=1/21;q=0c30c30c;last=4) | -1*(r=4/22;q=2e8ba2e8;last=16)
k=3: +4*(r=6/25;q=3d70a3d7;last=1) | -2*(r=4/28;q=24924924;last=16) | -1*(r=24/29;q=d3dcb08d;last=7) | -1*(r=16/30;q=88888888;last=16)
k=4: +4*(r=16/33;q=7c1f07c1;last=31) | -2*(r=16/36;q=71c71c71;last=28) | -1*(r=16/37;q=6eb3e453;last=1) | -1*(r=16/38;q=6bca1af2;last=20)
k=5: +4*(r=1/41;q=063e7063;last=37) | -2*(r=1/44;q=05d1745d;last=4) | -1*(r=1/45;q=05b05b05;last=31) | -1*(r=1/46;q=0590b216;last=12)
known sixth pi hex digit from the finite lanes PLUS explicit k>5 tail: a
finite fraction contribution: 2.6579512951148216 tail fraction contribution: 0.0003792759199925696 certified omitted tail abs < 4.0341805569986455e-94
NOTE: this digit was already known in §206; this is an ownership/route repeat, not a new landing.

STATUS: RUNS base16 crossing/unwind, codebook/ring layout, parity-dependent facing, side boundary, BBP decomposition.
DEAD END: a fixed-point-free facing inside any odd-sized individual lane (parity obstruction).
OPEN: a canonical cross-lane reader/width contract yielding the native binary ring order.

[AFTER-SEAL DEDUCTION: the cross-lane hole and the complete address ring]
This section was derived AFTER the original S1–S6 seal. It is not a pre-sealed prediction.
address (k,j,r) <-> flat address: 65536/65536 exact round trips
cross-facing: 65536/65536 involutive; 0 fixed; exactly two odd-lane centers paired per k
block sizes: sum_j(8k+j)=16(2k+1); prefix blocks end at 16*(k+1)^2
  first  1 windings:     16 instances = 2^4
  first  2 windings:     64 instances = 2^6
  first  4 windings:    256 instances = 2^8
  first  8 windings:   1024 instances = 2^10
  first 16 windings:   4096 instances = 2^12
  first 32 windings:  16384 instances = 2^14
  first 64 windings:  65536 instances = 2^16
whole 2^16-address ring: near/far first encounter executed, full coverage, no fixed points; PTP=T^-1 all 65536 slots
reader ownership: odd centers paired only within the SAME winding; without that contract owner remains AMBIGUOUS
addressed instances: 65536 distinct crossing WORD STRINGS: 4274 duplicate string instances: 61262 most common: [('000', 128), ('00', 120), ('c0', 94), ('80', 92), ('0f', 64), ('1e', 64)]
  slot=    0: owner=(0, 1, 0) crossings=0 facing=65535
  slot=    1: owner=(0, 4, 0) crossings=0 facing=65534
  slot=    2: owner=(0, 4, 1) crossings=4 facing=65533
  slot=    3: owner=(0, 5, 0) crossings=0 facing=65532
  slot=    4: owner=(0, 5, 1) crossings=3 facing=65531
  slot=    5: owner=(0, 6, 0) crossings=0 facing=65530
  slot=    6: owner=(0, 6, 1) crossings=2 facing=65529
  slot=    7: owner=(0, 6, 2) crossings=5 facing=65528
  slot=32765: owner=(63, 6, 252) crossings=7e7 facing=32770
  slot=32766: owner=(63, 6, 253) crossings=7ef facing=32769
  slot=32767: owner=(63, 6, 254) crossings=7f7 facing=32768
  slot=32768: owner=(63, 6, 255) crossings=800 facing=32767
  slot=32769: owner=(63, 6, 256) crossings=808 facing=32766
  slot=32770: owner=(63, 6, 257) crossings=810 facing=32765
  slot=65532: owner=(0, 5, 4) crossings=c facing=3
  slot=65533: owner=(0, 4, 2) crossings=8 facing=2
  slot=65534: owner=(0, 4, 3) crossings=c facing=1
  slot=65535: owner=(0, 5, 2) crossings=6 facing=0
STATUS ADDENDUM: RUNS (computed after seal): total 16K^2; routed instance address; pairing of two center holes per k; global facing with explicit same-k contract.
OPEN: whether the cross-lane facing provider, or the global slot order, follows from the lane motion alone without the declared pairing rule.
```

**Files:** `lane209.py` (full single-file executable), `seal209_predictions.txt` (pre-execution SHA-256 seal), `lane209_actual_trace.txt` (captured stdout); all included in `running-audit-10-section209-scripts.md`.


> **Document continuity:** §§210–222 were described in the supplied conversation but their latest edited audit files were not attached or mounted. This copy preserves §§202–209 and appends §223 without inventing or overwriting the missing intervening sections. Insert §223 into the current master after §222 once that master is available.

## § 223. Address plus generator: the ring's complete binary signature regenerates on demand; the shared reader uses an information-minimal address — `section223_address_generator.py`

**Dean (31 Oct).** "Memory can be generated with math. All transformations are binary. All things have a binary signature." The requested next step: "Memory is an address plus a generator. Take one thing's binary signature and find the smallest address-and-rule pair that regenerates it on demand, the way BBP regenerates π. Append §223."

**Scope and correction.** The object selected is the *entire width-16 native-ring walk* as a single ordered 1,048,576-bit signature. This is generated output, not a pre-stored file used by the reader. The smallest-address claim below is exact **only within the specified model**: a fixed, shared, lossless reader that must be able to select any one of all 2^n different n-bit words. It does **not** prove a shortest total program for this particular string. Earlier paper outputs, including `0x27`, the width-4 `0123567dbe9ac48f` walk, and the previously recorded 64-bit π word/address, were already known. The run is an independently implemented execution route and regression, not an independent blind landing.

**Prediction seal.** Before the execution, the text file `seal223_predictions.txt` was written and hashed SHA-256 `33c2bb8283516406e5e9f5b53e8511e98a7854b762d8e59d16697af95211ef72`; all seven scoped predictions held. The known source outputs in that text are identified as regressions.

**One reader, not a stored ring.** Let `P_n(x)` be the existing involution: reverse the word unless it is palindromic, in which case complement it. Write `M_n={x: x<P_n(x)}`. For any fixed binary prefix, the count of completions in `M_n` can be obtained by walking **symmetric bit pairs**, recording whether the prefix has already become smaller than its reversal. If all pairs match, only a leading zero survives. No candidate words, sorted representative list, or ring builder enter the reader. Repeated branch counts unrank the representative at any near address; the established partner maps it into the far address.

With `N=2^n`, `h=N/2`, and `u(i)` the branch-count unranking operator,

```
G_counter(n,a) = u(a)                if a < h
                 P_n(u(N-1-a))     if a >= h

G_record(n,a) = G_counter(n,a)      except at a=h-1 and a=h,
where those two words exchange places (n>=2).
```

The inverse `SAVE` computes the representative's lexicographic rank by adding the counts of skipped zero branches along the input word's bits. The partner side determines the far address; the record-crease exception swaps the two center addresses back. Both directions use the same fixed rule.

**The §208 lane supplies the bit execution.** For any returned word `x`, run `2r = 2^n q + r'` for `n` steps, starting `r=x`. Its crossing bits are exactly the bits of `x`, and the remainder reaches 0. Conversely, integrating the crossings in base two returns `x`. This is the recorded lane, not an invented instruction set.

**The actual run.** Script `section223_address_generator.py` was executed successfully, comparing only *after generation* to an independent conventional ring builder. Widths 1–12 were run at every address under both crease contracts, verifying uniqueness, `READ -> SAVE`, crossing reconstruction, and the facing involution. At width 16, the reader emitted every word at its address, all 65,536 addresses returned exactly from the emitted word, all 32,768 facing pairs held, and the conventional builder agreed when invoked afterwards.

```
TARGET:             complete record-crease R_16 walk
NUMBER OF WORDS:    65,536
WORD WIDTH:         16 bits
BINARY SIGNATURE:   1,048,576 bits = 131,072 bytes
INPUT TO READER:    n=16, crease=record, address a (16 bits)
NO RING TABLE:      in READ or SAVE
SHA-256 OF OUTPUT:  ba3eac43b1c08d6d3267535fd587238a159eab6a1a2060328aa02890867fd961
OUTPUT FILE:        R16_signature_regenerated.bin (written by executor, not loaded by it)
```

**Previously recorded 64-bit object.** Independently, using the recorded ring address `2,427,008,858,123,944,441` and the same shared reader at width 64 returns `0x243f6a8885a308d3`; `SAVE` returns the recorded address. This is a return to an already known datum, not a new prediction.

**Smallest address, with its exact qualifier.** A shared fixed reader must distinguish `2^n` possible n-bit values. No fixed-length address shorter than `n` bits has that many encodings. `G(n,a,c)` uses exactly `n` address bits when `n` and the crease contract are fixed. The generator code has a separate, shared cost, and a particular highly structured word can have a shorter description. The result proves optimal *universal address width*, not absolute Kolmogorov minimality or that arbitrary signatures compress.

**What moves.** `READ` is not a materialized copy of the field. The address determines the next binary word by an executable rule; `SAVE` computes its inverse address; the same word's lane emits its crossings. The 131,072 output bytes are an *artifact of execution* and can be discarded and reproduced. That is exactly the distinction between generating memory and storing an independent copy of its contents.

| Claim | Status |
|---|---|
| address-wise generation and inverse on both crease contracts, n=1..12, every address | RUNS |
| complete R_16 output without input ring table, every word once | RUNS |
| all R_16 32,768 facing pairs and independent builder match | RUNS |
| base-2 crossings and weighted save return word | RUNS (n=1..12 exhaustive; follows §208 algebra at n=16) |
| previously recorded 64-bit π word/address reconstruct | RUNS — previously seen data, provenance regression |
| address-width lower bound n for a shared lossless reader | STANDS — counting argument |
| absolute smallest total address-and-rule program for this string | OPEN — depends on machine/description language |
| unique physical generation of all real-world objects from binary signatures | OPEN — not asserted by this execution |

**Files.** `section223_address_generator.py`; `section223_actual_run.txt`; `seal223_predictions.txt`; `R16_signature_regenerated.bin`. `READ` contains no call to the independent `regression_ring` oracle; that function is executed only to compare after the generated output exists.
