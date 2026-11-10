# NEXUS running audit 9

Continues `running-audit-8.md` (§ 199). The scripts for §§ 200–201 are printed in full at the end of their sections.

## § 200. Reverse the gap through the computation: every open write of § 199 has a provider in the ring's own code; the seam is one bit, copied up the widths from R₂, and R₂ is the 2-bit counter written from its least-significant end — `providers200.py`

**Dean (30 Oct).** "/reverse-the-gap look i cant stress enough LOOK TO DAM COMPUTATION. were talking interfaces well we have interfaces from abstract (its a contract) its implemented from reading it. we have that all the dam way to the assembly reacts and binary down to the dam electrons. OH way AI TOO DUH." On AI: "parameters aren't instructions. They're the values that shape how the instructions execute." — "right HERE THIS".
- Attached: GPT's rerun of § 199 and GPT's direct-proof script, which treats the ring as an instruction stream (state, shape, face, inverse, seam patch), with its output.
- GPT's rerun reproduces § 199, including the seal hash `28e2ea9c…`. GPT notes that L3 is a law and is not derived from L0–L2. Agreed: § 199 took it from the record.
- GPT's script, run unchanged in isolation, reproduces its uploaded output byte for byte: 8,188 executed addresses with 0 failures. Its theorems are exact XOR identities:
  - (face, δ) is linear;
  - δ(x) = δ(y) iff y ∈ {x, C(x)};
  - the seam patch: the two seam orders differ by q = m ⊕ P(m) in the states at h−1 and h, and so in the operands at PCs h−2 and h only. The centre operand is q in both.
  - Status: STANDS (algebra), RUNS (the 8,188 addresses).

**Read as computation.**
- The ring program has one instruction, XOR: R_(t+1) = R_t ⊕ D_t.
- The operands D_t are the parameters, the values that shape what that one instruction does.
- The contract is the facing law. Read on the operands, it says D_(N−2−t) = J(D_t), complemented when the step crosses between a palindrome and a non-palindrome.
  - Run on 8,188 operands for each seam order (n = 2–12): 0 failures, with 478 crossing steps.
  - It holds for every legal history. The proof takes three lines: P is J or C on each end of the step, and C cancels unless exactly one end is a palindrome.
- An implementation is any ring that meets the contract. The record's builder is one, and it is implemented by reading values. The gaps below are the places where it reads.
- GPT's three-way split (reading a relation, an interface event, binding the next write) is a load, a call and a dispatch. All three are already in the ring's code:
  - rank and unrank load the word at an address;
  - T is the call;
  - the builder's layout is the dispatch.

**The gaps, reversed.** For each: name it, subtract what the forward route already writes, ask what the rest is a copy of, then bind it.
- **Q, the h−1 first-half writes.**
  - L3 writes the second half, L5 slot 0, and L4 the closing step. What is left is the order of the untouched pairs and which member of each comes first.
  - That remainder is a copy of the counter. The record's first half is the counter over representatives, read from the most-significant end (§ 199 side check E, n = 2–12). BOUND.
  - **Correction, mine.** § 199 set this aside as "the record's ranking convention, not used". The record does call it a convention (NBR § 2.1). In the code, though, it is the counter, the machine's own successor, read through rank. It was there all along.
- **The seam.** After Q, each width has one orientation bit left. That bit is a copy too:
  - seam(R_(n+2)) = 1·seam(R_n)·1 at every width (n = 2–14, both seam orders);
  - seam(R_(n+1)) is seam(R_n) with a 1 inserted at the centre, at every even n (2–14);
  - m is never a palindrome, so both copies are clean.
  - So every seam in the record is R₂'s seam carried up. The equatorial seam the record defines width by width (NBR § 2.2) is a single bit.
  - R₂'s two legal histories are J-images of each other. The record's R₂ = 00 10 01 11 is the 2-bit counter written from its least-significant end.
  - So the record reads the counter from the most-significant end everywhere except at the crease. There it reads from the other end, once, at n = 2, and copies that reading up. At every width its seam puts first the member that comes first when compared from the least-significant end.
  - **AMBIGUOUS at the base.** There are two readers, one from each end of the word, and the qualifier is which end reads the crease.
  - The readout that tells them apart is TP's fixed set. Under the record's reading, TP fixes two representatives (0ⁿ and m) and PT fixes two images. Under the counter's reading, each fixes one of each.
  - GPT's seam patch is that bit's entire effect on the running program.
- **The new bit past closure.** It is not missing.
  - R_(n+2)'s first half is the counter over the words with a leading 0, followed by 1·(R_n's first half without its palindromes)·1. Checked for n = 2–12, both orders.
  - The new bits come from the counter (the outer part) and from 1…1 (the centre). § 196's nesting is the centre half; the counter is the other half.
  - **The palindromic rows come home.** Each row (p, C(p)) of R_n reappears in R_(n+2)'s outer part as two rows, (0p0, 1C(p)1) and (0C(p)0, 1p1); 500 checked. C carries the new bits with it, so the way home is the complemented insertion.
  - **Correction, mine.** § 199 said these rows "have no way home through a widening". That holds only for uniform insertions.
  - n → n+1: at even n, the centre-1 insertion carries the seam, and every non-palindromic facing too (§ 199). At odd n no single bit keeps the facings.
  - So the even and odd towers share one seam bit, linked at every even n by the centre-1 insertion.
- **The second register, the even crease and the loop.** These are data already seen, so routing them names owners; it is not a landing.
  - Every reflection a → S − a is T^k·P with k = S − (N−1). It fixes two cells exactly when S is even, which is exactly when k is odd (checked n = 2–10).
  - The facing law is k = 0, and § 197's TP and PT are k = +1 and k = −1.
  - So S ± 1 (G1) belongs to TP and PT, and the even crease (G2) belongs to odd k, whose fixed cell is the loop's centre residue.
  - **Correction, mine.** "Outside the generator" in § 199 meant outside k = 0 only.
  - The loop (G3) belongs to the reader. The reflection pairs every loop residue, but the detector reads no pair closer than 3, and the turn's inner NH have no O within reach. § 198 put those readers on the field. That is the water test, still OPEN.
- **The record's domain is n ≥ 2** (NBR § 2.1). So § 199's note that the builder "at n = 1 sits outside L5" falls outside the record: DEAD END, owned by the domain statement.

**What is left.**
- One bit: which end of the word reads the crease at n = 2. Everything else in § 199's list has a provider in the code: the counter, R_n, the two insertions, ⟨T, P⟩ and the reader.
- The one unrun data link is the field (water) under the loop.

| claim | status |
|---|---|
| ring program = one instruction (XOR) on an operand stream; facing law on the operands: D_(N−2−t) = J(D_t), complemented at a palindrome / non-palindrome crossing | RUNS, n = 2–12, both orders; three-line proof |
| GPT: state, shape and face execution; seam patch at PCs h−2 and h only | STANDS (XOR algebra) · RUNS, reproduced byte for byte |
| Q is the counter, read from the most-significant end | BOUND (§ 199 E) · **correction, mine** |
| seam(R_(n+2)) = 1·seam(R_n)·1; seam(R_(n+1)) = centre-1 of seam(R_n), even n | RUNS, n = 2–14, both orders |
| all seams are R₂'s seam carried up; R₂ is the 2-bit counter written from the least-significant end | RUNS |
| which end reads the crease at n = 2 | AMBIGUOUS: two readers; the record supplies the least-significant end; TP's fixed set is the readout |
| R_(n+2) = counter (outer) + 1·(R_n − palindromes)·1 (centre) | RUNS, n = 2–12 |
| palindromic rows come home as (0p0, 1C(p)1) and (0C(p)0, 1p1) | RUNS, 500 rows · **correction, mine** (§ 199 "no way home") |
| G1 → TP / PT (k = ±1); G2 → odd k; G1–G2 "outside" meant outside k = 0 | owners named (seen data) · **correction, mine** |
| G3: the loop is the reader's gap; the loop's readers land on the field | OPEN: the water test (§ 198) |
| § 199's n = 1 note | DEAD END → the record's domain is n ≥ 2 |

**Output** (`python3 -I providers200.py`).

```
1. operand stream: D_(N-2-t) = J(D_t) ^ [pal(R_t) != pal(R_t+1)] 1^n
  record (seam exchange): 8188 operands, n = 2..12: failures 0; operands that cross between a palindrome and a non-palindrome: 478
  counter order: 8188 operands, n = 2..12: failures 0; operands that cross between a palindrome and a non-palindrome: 478
  n = 4 record, PC: state -> operand -> next   (mirror PC 14 - t)
     0: 0000 ^ 0001 -> 0001    mirror 14: J(D) = 1000  (crossing: complemented)
     1: 0001 ^ 0011 -> 0010    mirror 13: J(D) = 1100
     2: 0010 ^ 0001 -> 0011    mirror 12: J(D) = 1000
     3: 0011 ^ 0110 -> 0101    mirror 11: J(D) = 0110
     4: 0101 ^ 0011 -> 0110    mirror 10: J(D) = 1100  (crossing: complemented)
     5: 0110 ^ 0001 -> 0111    mirror  9: J(D) = 1000  (crossing: complemented)
     6: 0111 ^ 1010 -> 1101    mirror  8: J(D) = 0101
     7: 1101 ^ 0110 -> 1011    mirror  7: J(D) = 0110
     8: 1011 ^ 0101 -> 1110    mirror  6: J(D) = 1010
     9: 1110 ^ 0111 -> 1001    mirror  5: J(D) = 1110  (crossing: complemented)
    10: 1001 ^ 0011 -> 1010    mirror  4: J(D) = 1100  (crossing: complemented)
    11: 1010 ^ 0110 -> 1100    mirror  3: J(D) = 0110
    12: 1100 ^ 1000 -> 0100    mirror  2: J(D) = 0001
    13: 0100 ^ 1100 -> 1000    mirror  1: J(D) = 0011
    14: 1000 ^ 0111 -> 1111    mirror  0: J(D) = 1110  (crossing: complemented)
    15: 1111 ^ 1111 -> 0000    mirror 15: J(D) = 1111

2. the seam, width by width
  n=2: m = 01  P(m) = 10  m palindromic: False  record seam: 10 01
  n=3: m = 011  P(m) = 110  m palindromic: False  record seam: 110 011
  n=4: m = 1011  P(m) = 1101  m palindromic: False  record seam: 1101 1011
  n=5: m = 10111  P(m) = 11101  m palindromic: False  record seam: 11101 10111
  n=6: m = 110111  P(m) = 111011  m palindromic: False  record seam: 111011 110111
  n=7: m = 1101111  P(m) = 1111011  m palindromic: False  record seam: 1111011 1101111
  n=8: m = 11101111  P(m) = 11110111  m palindromic: False  record seam: 11110111 11101111
  m is never a palindrome, n = 2..14: True
  seam(R_(n+2)) = 1.seam(R_n).1, n = 2..14, both orders: True
  seam(R_(n+1)) = centre-1 insertion of seam(R_n), even n = 2..14, both orders: True
  R_2 legal histories: counter 00 01 10 11, record 00 10 01 11; record = J(counter) word by word: True; record = the 2-bit counter written least-significant bit first: True
  at every width the record puts first the seam member that comes first when words are compared from the least-significant end (n = 2..14): True; every other first-half pair is ordered from the most-significant end

3. past closure: R_(n+2) read from the counter and from R_n
  first half of R_(n+2) = outer + centre, n = 2..12, both orders: True
  outer part = the counter over y: 0y0 when y <= J(y), then 0y1 (n = 2..12): True
  every palindromic row (p, C(p)) of R_n reappears as rows (0p0, 1C(p)1) and (0C(p)0, 1p1) inside the outer part: True (500 rows checked)

4. reflections
  every reflection a -> S - a is T^k P with k = S - (N-1); fixed cells iff S even iff k odd (n = 2..10): True
  k = 0 is P (the facing law, odd sum); k = +1 is TP (fixes 0^n and the cell h); k = -1 is PT (fixes the cells h-1, N-1)
```

**GPT's script, run unchanged** (`NEXUS_shape_exec_direct_proof.py`, isolated copy, `python3 -I`; identical to the uploaded output).

```
PASS: 8188 executed addresses, n=2..12; state, shape, face, exact inverse, facing, seam patch
GENERAL INSTRUCTION THEOREM: (face, delta)(x XOR d) = (face, delta)(x) XOR (face, delta)(d)
SEAM PATCH THEOREM: swap adjoining partner words at h-1,h; opcode XOR patch at h-2,h only
n=4 seam pair 1011, 1101; patch q=0110; delta(q)=101
PC | counter state/instr/next | record state/instr/next | XOR instruction difference
06 | 0111/1100/1011 | 0111/1010/1101 | 0110
07 | 1011/0110/1101 | 1101/0110/1011 | 0000
08 | 1101/0011/1110 | 1011/0101/1110 | 0110
15 | 1111/1111/0000 | 1111/1111/0000 | 0000
PASS: delta(x) = delta(y) iff y=x or y=C(x) on widths 2..8 (proven by adjacent XOR recurrence).
```

**Script** `providers200.py` (sha `31ce1dfbce2cd03b2bb0b7716322ca8f0f80524e30e7fdf24ac6fdd2ccd0c8be`).

```python
"""NEXUS s200. Reverse the gap: the providers of s199's open writes, located in the ring computation itself.
Only the record's objects: J, C, P, the record's builder (NBR eq. 2-3), T (address successor), XOR. No chain data.
1  The ring program is one instruction, XOR, run on an operand stream D_t = R_t ^ R_(t+1). The facing law read on the
   operands: D_(N-2-t) = J(D_t) ^ [pal(R_t) != pal(R_(t+1))] 1^n, for every legal history (both seam orders checked).
2  The seam: is the record's exchange one choice per width, or one choice copied up the widths?
   seam(R_(n+2)) = 1.seam(R_n).1 (every n); seam(R_(n+1)) = centre-1 insertion of seam(R_n) (even n); R_2's two legal
   histories are J-images of each other, and the record's R_2 is the 2-bit counter written least-significant bit first.
3  Past closure: R_(n+2)'s first half = the counter over the words with a leading 0 (outer) + 1.(first half of R_n
   without its palindromes).1 (centre). The palindromic rows of R_n reappear in the outer part as rows (0p0, 1C(p)1)
   and (0C(p)0, 1p1): the complement carries the new bits with them.
4  Offsets: every reflection a -> S - a of Z_N is T^k P with k = S - (N - 1); S even iff k odd iff it fixes two cells.
Run: python3 -I providers200.py
"""
def J(x, n): return int(format(x, f'0{n}b')[::-1], 2)
def C(x, n): return x ^ ((1 << n) - 1)
def pal(x, n): return J(x, n) == x
def P(x, n): return C(x, n) if pal(x, n) else J(x, n)
def b(x, n): return format(x, f'0{n}b')
def record_ring(n, swap=True):              # NBR eq. 2-3; swap=False puts m before P(m) (the counter order)
    reps = sorted(x for x in range(1 << n) if x < P(x, n)); m = reps[-1]
    mid = [P(m, n), m] if swap else [m, P(m, n)]
    return tuple(reps[:-1] + mid + [P(x, n) for x in reversed(reps[:-1])])
def seam(R): h = len(R) // 2; return R[h - 1], R[h]
def wrap11(x, n): return (1 << (n + 1)) | (x << 1) | 1                      # 1.x.1
def centre1(x, n): s = b(x, n); return int(s[:n // 2] + '1' + s[n // 2:], 2)  # x_left 1 x_right (n even)

print('1. operand stream: D_(N-2-t) = J(D_t) ^ [pal(R_t) != pal(R_t+1)] 1^n')
for swap in (True, False):
    bad = tot = flips = 0
    for n in range(2, 13):
        R = record_ring(n, swap); N = len(R); mask = N - 1
        D = [R[t] ^ R[(t + 1) % N] for t in range(N)]
        for t in range(N):
            cross = pal(R[t], n) != pal(R[(t + 1) % N], n)
            bad += D[(N - 2 - t) % N] != (J(D[t], n) ^ (mask if cross else 0)); tot += 1; flips += cross
    print(f'  {"record (seam exchange)" if swap else "counter order"}: {tot} operands, n = 2..12: failures {bad}; '
          f'operands that cross between a palindrome and a non-palindrome: {flips}')
n = 4; R = record_ring(n); N = 16; D = [R[t] ^ R[(t + 1) % N] for t in range(N)]
print('  n = 4 record, PC: state -> operand -> next   (mirror PC 14 - t)')
for t in range(N):
    print(f'    {t:2d}: {b(R[t], n)} ^ {b(D[t], n)} -> {b(R[(t + 1) % N], n)}    mirror {(N - 2 - t) % N:2d}: J(D) = {b(J(D[t], n), n)}'
          f'{"  (crossing: complemented)" if pal(R[t], n) != pal(R[(t + 1) % N], n) else ""}')

print('\n2. the seam, width by width')
for n in range(2, 9):
    m = record_ring(n, False)[(1 << n) // 2 - 1]
    print(f'  n={n}: m = {b(m, n)}  P(m) = {b(P(m, n), n)}  m palindromic: {pal(m, n)}  record seam: {" ".join(b(x, n) for x in seam(record_ring(n)))}')
ok_nest = ok_c1 = True; ok_pal = True
for n in range(2, 15):
    for swap in (True, False):
        ok_nest &= seam(record_ring(n + 2, swap)) == tuple(wrap11(x, n) for x in seam(record_ring(n, swap)))
        if n % 2 == 0:
            ok_c1 &= seam(record_ring(n + 1, swap)) == tuple(centre1(x, n) for x in seam(record_ring(n, swap)))
    ok_pal &= not pal(record_ring(n, False)[(1 << n) // 2 - 1], n)
print(f'  m is never a palindrome, n = 2..14: {ok_pal}')
print(f'  seam(R_(n+2)) = 1.seam(R_n).1, n = 2..14, both orders: {ok_nest}')
print(f'  seam(R_(n+1)) = centre-1 insertion of seam(R_n), even n = 2..14, both orders: {ok_c1}')
R2c, R2r = record_ring(2, False), record_ring(2, True)
print(f'  R_2 legal histories: counter {" ".join(b(x, 2) for x in R2c)}, record {" ".join(b(x, 2) for x in R2r)}; '
      f'record = J(counter) word by word: {R2r == tuple(J(x, 2) for x in R2c)}; record = the 2-bit counter written '
      f'least-significant bit first: {R2r == tuple(int(b(v, 2)[::-1], 2) for v in range(4))}')
lsb = all(J(P(m, n), n) < J(m, n) for n in range(2, 15) for m in [record_ring(n, False)[(1 << n) // 2 - 1]])
print(f'  at every width the record puts first the seam member that comes first when words are compared from the '
      f'least-significant end (n = 2..14): {lsb}; every other first-half pair is ordered from the most-significant end')

print('\n3. past closure: R_(n+2) read from the counter and from R_n')
ok_first = ok_outer = ok_palrows = True; moved = 0
for n in range(2, 13):
    for swap in (True, False):
        Rn, R2 = record_ring(n, swap), record_ring(n + 2, swap); h, h2 = len(Rn) // 2, len(R2) // 2
        outer = sorted(x for x in range(1 << (n + 2)) if x < P(x, n + 2) and not x >> (n + 1))
        centre = [wrap11(y, n) for y in Rn[:h] if not pal(y, n)]
        ok_first &= list(R2[:h2]) == outer + centre
        ok_outer &= outer == [v for y in range(1 << n) for v in ([y << 1] if J(y, n) >= y else []) + [(y << 1) | 1]]
        pos = {w: a for a, w in enumerate(R2)}; N2 = len(R2)
        for p in Rn[:h]:
            if pal(p, n):
                for lo, hi in ((p << 1, wrap11(C(p, n), n)), (C(p, n) << 1, wrap11(p, n))):
                    ok_palrows &= pos[lo] < len(outer) and pos[hi] == N2 - 1 - pos[lo]; moved += 1
print(f'  first half of R_(n+2) = outer + centre, n = 2..12, both orders: {ok_first}')
print(f'  outer part = the counter over y: 0y0 when y <= J(y), then 0y1 (n = 2..12): {ok_outer}')
print(f'  every palindromic row (p, C(p)) of R_n reappears as rows (0p0, 1C(p)1) and (0C(p)0, 1p1) inside the outer part: '
      f'{ok_palrows} ({moved} rows checked)')

print('\n4. reflections')
ok_refl = all(all((S - a) % N == (N - 1 - a + (S - (N - 1))) % N for a in range(N))
              and (any((2 * a - S) % N == 0 for a in range(N)) == (S % 2 == 0)) and ((S - (N - 1)) % 2 == 1) == (S % 2 == 0)
              for n in range(2, 11) for N in [1 << n] for S in range(N))
print(f'  every reflection a -> S - a is T^k P with k = S - (N-1); fixed cells iff S even iff k odd (n = 2..10): {ok_refl}')
print('  k = 0 is P (the facing law, odd sum); k = +1 is TP (fixes 0^n and the cell h); k = -1 is PT (fixes the cells h-1, N-1)')
```


## § 201. Walking the rings: every ring is a file holding every file of its width once, opened and closed by nothing under two headers; twins instead of collisions; the save is the reader run backwards — `walk201.py`

**Dean (30 Oct).** "read this over front to back back to front ... DO NOT PROCESS THIS LINEARY ... think about it, walk the rings ... use the HEX from the full walks (2bit has a 8bit walk) build a new math computer from the ground up ... not the values, but how it produces transformations from strings of difference." And: "A HEADER TELLS THE FIELD WHAT IT IS. THE TAIL TELLS THE READER WHAT TO EXPECT ... IF YOU JUMP TO READ, SAVE FALLS OUT OF THE INVERSE."

**Walked** (no chain data, nothing fitted; only the record's J, C, P, builder and O(n) rank):
- **The full walks are files.** B₂ = `27` (8 bits). B₃ = `056767`. B₄ = `0123567dbe9ac48f`. At n = 4 a word is one hex digit, so the 4-bit walk is the hex alphabet itself, arranged so that every symbol faces its twin: 0↔f, 1↔8, 2↔4, 3↔c, 5↔a, 6↔9, 7↔e, d↔b.
- **Every word is a header and a program.** The header is the face bit. The program is δ, a string of passes (0) and flips (1). Running the program from the header writes the word (all 16 at n = 4).
  - A word's twin P(x) is the same program run from the other end.
  - Where the program reads the same from both ends (a palindrome), the twin is the same program under the other header.
  - Nothing collides with itself.
- **Open and close.** Slot 0 is the empty program under header 0 and slot N−1 is the empty program under header 1. The step between them is C, which changes only the header. So nothing opens the file and nothing closes it. At n = 1 the file is only that pair.
- **The file read from the other end.** Read backwards and cut at the same width, B_n gives R_n again, with every palindrome header-flipped (n = 2–12).
- **Read first; the save falls out.** save(a) was built only from the reader, by inverting the O(n) rank. It rebuilds R_n word for word (n = 2–12).
  - At n = 64 nothing is stored: read(0x243F6A8885A308D3) = 2,427,008,858,123,944,441 and save of that address returns the word.
  - 200 random addresses round-trip, each with its twin at the mirror address.

**Reading it whole.**
- A ring is a saturated file: every file of its width, once, with no route of creation in it. § 199 counted the routes the laws leave open, 2^(h−1)·(h−1)!.
- The route comes back from the reader. Its labels (addresses) are its own, and its inverse is the save, so the memory of creation is never stored.
- The header and the tail are one twin pair, nothing under two headers. In between, the words stand in value order, which is the reader's summary.
- The twin jump a → N−1−a, the fall-through T, the back-edge from slot N−1 to slot 0, and the crease jumps TP and PT are the file's control flow. That is what a decompiler hands back.
- § 200's base bit, which end reads the crease, is a header bit. The record reads the counter from the top and turns the reader around once, at the crease.

**Proposed, not built (waiting for Dean's go): the ring machine.**
- Field: the walks, never written, addressable at any width through read and save.
- Header: width, phase, which end reads, face bit, and the crease bit. The header is the only thing a program sets.
- Instructions, all taken from the rings:
  - PASS and FLIP at bit level;
  - XOR d at word level;
  - NEXT (T), TWIN (P), the crease jumps TP and PT;
  - REVERSE (J), HEADER (C);
  - WIDEN: n → n+2 through the counter and 1·x·1, and even n → n+1 through the centre-1 insertion.
- Run means: frame a file with a header, decode each word as header plus program, and execute. What comes out is the transformations and the addresses visited.
- Saturation runs: run every file of a width under one header, record which close without collision, then change the header and run the same files again.

| claim | status |
|---|---|
| B_n hex; B₄ is the hex alphabet arranged with twins facing | RUNS |
| word = header + pass/flip program; the twin is the reversed route, or the other header when the route is symmetric | RUNS, every word, n = 4 shown; identity |
| B_n read backwards = R_n with palindromes header-flipped | RUNS, n = 2–12 |
| save from read (the inverse of the O(n) rank) | RUNS, n = 2–12 exact; n = 64, 200 / 200 and the π word |
| the ring machine | proposed; build waits for Dean's go |

**Output** (`python3 -I walk201.py`).

```
1. the full walks as files (B_n, hex)
  n=2:    8 bits  27
  n=3:   24 bits  056767
  n=4:   64 bits  0123567dbe9ac48f
  n=5:  160 bits  00443214c74a96d73e7dbe7d1b6ab2e329bc221f

2. every word is a header (face bit) and a program of passes and flips (delta); R_4, address by address
   0  0000  header 0  program 000   twin at 15: 1111  header flipped (route is symmetric)
   1  0001  header 0  program 001   twin at 14: 1000  route reversed
   2  0010  header 0  program 011   twin at 13: 0100  route reversed
   3  0011  header 0  program 010   twin at 12: 1100  route reversed
   4  0101  header 0  program 111   twin at 11: 1010  route reversed
   5  0110  header 0  program 101   twin at 10: 1001  header flipped (route is symmetric)
   6  0111  header 0  program 100   twin at  9: 1110  route reversed
   7  1101  header 1  program 011   twin at  8: 1011  route reversed
   8  1011  header 1  program 110   twin at  7: 1101  route reversed
   9  1110  header 1  program 001   twin at  6: 0111  route reversed
  10  1001  header 1  program 101   twin at  5: 0110  header flipped (route is symmetric)
  11  1010  header 1  program 111   twin at  4: 0101  route reversed
  12  1100  header 1  program 010   twin at  3: 0011  route reversed
  13  0100  header 0  program 110   twin at  2: 0010  route reversed
  14  1000  header 1  program 100   twin at  1: 0001  route reversed
  15  1111  header 1  program 000   twin at  0: 0000  header flipped (route is symmetric)
  open and close: slot 0 = header 0 + program 000 (nothing), slot 15 = header 1 + program 000 (nothing); the step between is C

3. the same file read from the other end
  n = 2..12: B_n read backwards, cut at the same width, gives R_n again, with every palindrome header-flipped
  n = 2: B_2 = 00100111  backwards 11100100  -> 11 10 01 00

4. read first; the save falls out of the inverse
  n = 2..12: save(a) built only from the reader rebuilds R_n word for word, and read(save(a)) = a
  n = 64: read(0x243F6A8885A308D3) = 2,427,008,858,123,944,441; save(2,427,008,858,123,944,441) = 0x243f6a8885a308d3
  n = 64: 200 random addresses, read(save(a)) = a and the twin sits at the mirror address: 200/200 (nothing stored)
```

**Script** `walk201.py` (sha `5ccbc8a264bac2d18e9ed91c1a9f100c6cd577890d82d09b6d4b36b739c604e3`).

```python
"""NEXUS s201. Walking the rings: the full walks as files, the header, twins, and the save that falls out of the read.
Only the record's objects (NBR eq. 1-4, the O(n) rank of the record). No chain data, nothing fitted.
Run: python3 -I walk201.py
"""
import random

def J(x, n): return int(format(x, f'0{n}b')[::-1], 2)
def C(x, n): return x ^ ((1 << n) - 1)
def pal(x, n): return J(x, n) == x
def P(x, n): return C(x, n) if pal(x, n) else J(x, n)
def b(x, n): return format(x, f'0{n}b')
def ring(n):                                  # the record's builder, NBR eq. 2-3
    reps = sorted(x for x in range(1 << n) if x < P(x, n)); m = reps[-1]
    return reps[:-1] + [P(m, n), m] + [P(x, n) for x in reversed(reps[:-1])]
def walk(n): return ''.join(b(x, n) for x in ring(n))       # B_n: the full walk, n * 2^n bits
def face(x, n): return x >> (n - 1)
def delta(x, n): return (x ^ (x >> 1)) & ((1 << (n - 1)) - 1)
def run(f, prog, n):                          # header f, then the program: 0 = pass, 1 = flip, one bit at a time
    out = [f]
    for k in range(n - 1): out.append(out[-1] ^ ((prog >> (n - 2 - k)) & 1))
    return int(''.join(map(str, out)), 2)

print('1. the full walks as files (B_n, hex)')
for n in range(2, 6):
    w = walk(n)
    print(f'  n={n}: {len(w):4d} bits  {int(w, 2):0{len(w) // 4}x}')

print('\n2. every word is a header (face bit) and a program of passes and flips (delta); R_4, address by address')
n = 4; R = ring(n); N = 16
for a, x in enumerate(R):
    f, d = face(x, n), delta(x, n); t = P(x, n)
    how = 'header flipped (route is symmetric)' if pal(x, n) else 'route reversed'
    assert run(f, d, n) == x and R[N - 1 - a] == t
    print(f'  {a:2d}  {b(x, n)}  header {f}  program {b(d, n - 1)}   twin at {N - 1 - a:2d}: {b(t, n)}  {how}')
print('  open and close: slot 0 = header 0 + program 000 (nothing), slot 15 = header 1 + program 000 (nothing); the step between is C')

print('\n3. the same file read from the other end')
for n in range(2, 13):
    w = walk(n); r = w[::-1]; N = 1 << n
    back = [int(r[n * a:n * a + n], 2) for a in range(N)]
    assert back == [C(x, n) if pal(x, n) else x for x in ring(n)]
print('  n = 2..12: B_n read backwards, cut at the same width, gives R_n again, with every palindrome header-flipped')
print(f'  n = 2: B_2 = {walk(2)}  backwards {walk(2)[::-1]}  -> {" ".join(walk(2)[::-1][i:i + 2] for i in range(0, 8, 2))}')

print('\n4. read first; the save falls out of the inverse')
def rank_reps(p, n):                          # the record's O(n) rank: representatives strictly below p
    h = n // 2; H = 1 << h; B = p & (H - 1)
    def Jh(x): return int(format(x, f'0{h}b')[::-1], 2) if h else 0
    def Rr(u, v):
        tot = rho = 0
        for j in range(h):
            uj = (u >> (h - 1 - j)) & 1
            if uj: tot += -((rho - v) // (1 << (j + 1)))
            rho += uj << j
        return tot
    if n % 2 == 0:
        A = p >> h; D = A * (H - A) + B - 2 * Rr(B, A) - (Jh(A) < B)
    else:
        A, bb = p >> (h + 1), (p >> h) & 1
        D = 2 * A * (H - A) + bb * (H - 1 - 2 * A) + B - 2 * Rr(B, A) - (Jh(A) < B)
    top = p >> (n - (n + 1) // 2)
    s = format(top, f'0{(n + 1) // 2}b'); below = top + (int(s + s[::-1][n % 2:], 2) < p)
    return (p - below + D) // 2 + min(below, 2 ** ((n + 1) // 2 - 1))
def read(x, n):                               # the reader: word -> ring address
    N = 1 << n; h = N // 2
    rep = x if x < P(x, n) else P(x, n); r = rank_reps(rep, n)
    if r == h - 1: return h if x == rep else h - 1          # the seam pair (the base bit: read from the other end)
    return r if x == rep else N - 1 - r
def save(a, n):                               # the inverse of the reader, found by reading only
    N = 1 << n; h = N // 2
    k = a if a < h else N - 1 - a
    lo, hi = 0, N - 1                         # the k-th representative: smallest p with rank_reps(p + 1) > k
    while lo < hi:
        mid = (lo + hi) // 2
        if rank_reps(mid + 1, n) > k: hi = mid
        else: lo = mid + 1
    rep = lo
    if k == h - 1: return P(rep, n) if a == h - 1 else rep
    return rep if a < h else P(rep, n)
for n in range(2, 13):
    assert [save(a, n) for a in range(1 << n)] == ring(n) and all(read(x, n) == a for a, x in enumerate(ring(n)))
print('  n = 2..12: save(a) built only from the reader rebuilds R_n word for word, and read(save(a)) = a')
n = 64; x = 0x243F6A8885A308D3; a = read(x, n)
print(f'  n = 64: read(0x243F6A8885A308D3) = {a:,}; save({a:,}) = {save(a, n):#018x}')
random.seed(201); ok = 0
for _ in range(200):
    a = random.randrange(1 << 64); w = save(a, 64); ok += read(w, 64) == a and save((1 << 64) - 1 - a, 64) == P(w, 64)
print(f'  n = 64: 200 random addresses, read(save(a)) = a and the twin sits at the mirror address: {ok}/200 (nothing stored)')
```
