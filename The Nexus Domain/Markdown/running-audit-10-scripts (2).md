# NEXUS running audit 10: scripts

The scripts for §§ 202–205, printed in full, each with the sha256 of the file as run. `build_notebook.py` assembles `ring_machine.ipynb` from `ring_machine.py` and `test_ring_machine.py` and executes it. `checks202.py` checks the sealed predictions in `seal202/predictions.txt`. `checks203.py` reads the one stored byte; `msm203.py` checks the write-up's reconstruction matrix; `checks204.py` reads words of LEN 2ᵏ as commands; `head205.py` is the read head.

## `ring_machine.py` (sha `a6e94897e76ef7d34989f9f7b8fe9b1124fd792c4b5b3ae0843688f8cedc73e7`)

```python
"""The ring machine (NEXUS s202): field, header, ring instructions, run, save-from-read.
Every operation is one the record already has: J, C, P (NBR eq. 1), the builder (eq. 2-3), the address successor T
and its facing jump (eq. 4), the O(n) rank, XOR, and the widenings of s196 / s200. Nothing is fitted."""
import collections, math

# ---------------------------------------------------------------- primitives (NBR eq. 1)
def J(x, n): return int(format(x, f'0{n}b')[::-1], 2) if n else 0          # read the word from the other end
def C(x, n): return x ^ ((1 << n) - 1)                                       # flip every bit
def pal(x, n): return J(x, n) == x
def P(x, n): return C(x, n) if pal(x, n) else J(x, n)                        # twin
def bits(x, n): return format(x, f'0{n}b') if n else ''

# ---------------------------------------------------------------- field: the walks, never written
def ring(n, crease=1):
    """R_n, NBR eq. 2-3. crease=1 is the record (P(m) before m); crease=0 reads the crease the counter's way."""
    reps = sorted(x for x in range(1 << n) if x < P(x, n)); m = reps[-1]
    mid = [P(m, n), m] if crease else [m, P(m, n)]
    return reps[:-1] + mid + [P(x, n) for x in reversed(reps[:-1])]
def walk(n, crease=1): return ''.join(bits(x, n) for x in ring(n, crease))  # B_n, n * 2^n bits
def walk_hex(n, crease=1): w = walk(n, crease); return format(int(w, 2), f'0{len(w) // 4}x')
def seam(R): h = len(R) // 2; return R[h - 1], R[h]

# ---------------------------------------------------------------- reader and save (the save is the reader inverted)
def rank_reps(p, n):
    """The record's O(n) rank: number of representatives (x < P(x)) strictly below p."""
    h = n // 2; H = 1 << h; B = p & (H - 1)
    def Jh(x): return int(format(x, f'0{h}b')[::-1], 2) if h else 0
    def rect(u, v):
        tot = rho = 0
        for j in range(h):
            uj = (u >> (h - 1 - j)) & 1
            if uj: tot += -((rho - v) // (1 << (j + 1)))
            rho += uj << j
        return tot
    if n % 2 == 0:
        A = p >> h; D = A * (H - A) + B - 2 * rect(B, A) - (Jh(A) < B)
    else:
        A, bb = p >> (h + 1), (p >> h) & 1
        D = 2 * A * (H - A) + bb * (H - 1 - 2 * A) + B - 2 * rect(B, A) - (Jh(A) < B)
    top = p >> (n - (n + 1) // 2)
    s = format(top, f'0{(n + 1) // 2}b'); below = top + (int(s + s[::-1][n % 2:], 2) < p)
    return (p - below + D) // 2 + min(below, 2 ** ((n + 1) // 2 - 1))

def read(x, n, crease=1):
    """word -> ring address, by reading only."""
    N = 1 << n; h = N // 2
    rep = x if x < P(x, n) else P(x, n); r = rank_reps(rep, n)
    if r == h - 1:
        at_h = (x == rep) if crease else (x != rep)
        return h if at_h else h - 1
    return r if x == rep else N - 1 - r

def save(a, n, crease=1):
    """ring address -> word: the reader run backwards (bisection on the rank); nothing stored."""
    N = 1 << n; h = N // 2; k = a if a < h else N - 1 - a
    lo, hi = 0, N - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if rank_reps(mid + 1, n) > k: hi = mid
        else: lo = mid + 1
    rep = lo
    if k == h - 1:
        first = P(rep, n) if crease else rep
        return first if a == h - 1 else P(first, n)
    return rep if a < h else P(rep, n)

# ---------------------------------------------------------------- ring instructions (each carries its inverse)
def split(x, n): return x >> (n - 1), (x ^ (x >> 1)) & ((1 << (n - 1)) - 1)   # header bit, program (0 pass, 1 flip)
def run_prog(face, prog, n):                                                     # PASS / FLIP, bit by bit; inverse: split
    x = face
    for k in range(n - 1): x = (x << 1) | ((x & 1) ^ ((prog >> (n - 2 - k)) & 1))
    return x
def NEXT(a, N): return (a + 1) % N                                               # T
def BACK(a, N): return (a - 1) % N                                               # T^-1
def TWIN(a, N): return N - 1 - a                                                 # P on addresses (its own inverse)
def TP(a, N): return NEXT(TWIN(a, N), N)                                         # fixes 0 and N/2
def PT(a, N): return TWIN(NEXT(a, N), N)                                         # fixes N/2 - 1 and N - 1
def widen(y, n, fr): return (int(fr[0]) << (n + 1)) | (y << 1) | int(fr[1])     # n -> n+2: frame around y
def narrow(x, n): return str(x >> (n - 1)) + str(x & 1), (x >> 1) & ((1 << (n - 2)) - 1)   # inverse: frame, middle
def centre1(x, n): s = bits(x, n); return int(s[:n // 2] + '1' + s[n // 2:], 2)   # even n -> n+1
def uncentre(x, n): s = bits(x, n); c = (n - 1) // 2; return int(s[:c] + s[c + 1:], 2)

# ---------------------------------------------------------------- header: how a reader cuts a stored circle into words
_FLIP = str.maketrans('01', '10')
OPS = {'drawn': lambda s: s,                                  # as stored
       'J': lambda s: s[::-1],                                # read from the other end
       'C': lambda s: s.translate(_FLIP),                     # header bit flipped everywhere
       'sheet': lambda s: s[::-1].translate(_FLIP)}           # the workbook's Reading switch: backwards, 0/1 swapped
def apply_op(s, op): return OPS[op](s)

def frame(s, w, phase=0, stride=None):
    """Cut the circle s into w-bit words from bit `phase`, stepping `stride` bits (w = cut, 1 = slide), until the
    reader is back at its first cut."""
    stride = w if stride is None else stride; L = len(s); K = L // math.gcd(L, stride)
    ss = s * (1 + (phase + (K - 1) * stride + w) // L)
    return [int(ss[phase + k * stride: phase + k * stride + w], 2) for k in range(K)]

# ---------------------------------------------------------------- run: the two readings of a framed file
def run_states(words, w):
    """The words are the states visited. Closes = every word once and every slot faces its twin, so the last word is
    the first word's twin."""
    N = 1 << w; K = len(words); cnt = collections.Counter(words)
    full = K == N and len(cnt) == N
    facing = full and all(words[K - 1 - a] == P(words[a], w) for a in range(K))
    first = words[0]
    if full and facing and first == 0: cls = 'ring'
    elif full and facing and first == N - 1: cls = 'twin ring'
    elif full and facing: cls = 'ring, other start'
    elif full: cls = 'every word once, not facing'
    elif len(cnt) == N and len(set(cnt.values())) == 1: cls = 'every word, equal copies'
    elif len(cnt) == N: cls = 'every word, unequal copies'
    elif max(cnt.values()) == 1: cls = 'some words, no copies'
    else: cls = 'some words, copies'
    return dict(K=K, distinct=len(cnt), copies=K - len(cnt), cls=cls, closes=full and facing,
                collide=K > len(cnt), first=first, last=words[-1])

def run_operands(words, w):
    """The words are XOR operands executed on a w-bit register that starts on nothing."""
    s = 0; route = []
    for d in words:
        route.append(s); s ^= d
    return dict(closes=s == 0, route=route, distinct=len(set(route)), collide=len(set(route)) < len(route))
```

## `test_ring_machine.py` (sha `6e897b9b8f01eb34794b1bac5b91fde85b4624656a88d93d33751079cfa01f1a`)

```python
"""Tests for the ring machine (NEXUS s202). Each test names the behaviour the machine must have, taken from the record
(NBR eq. 1-4, s196, s199-s201) or from the uploads it answers; none of them uses chain data."""
import ring_machine as rm


def test_two_bit_walk_is_byte_27():
    assert rm.walk_hex(2) == '27'


def test_walk_length_is_width_times_words():
    for n in range(2, 9):
        assert len(rm.walk(n)) == n * 2 ** n


def test_every_word_faces_its_twin():
    for n in range(2, 9):
        for crease in (0, 1):
            R = rm.ring(n, crease); N = len(R)
            assert sorted(R) == list(range(N))
            assert all(R[N - 1 - a] == rm.P(R[a], n) for a in range(N))


def test_word_is_its_program_run_from_its_header():
    for n in range(2, 9):
        for x in range(2 ** n):
            assert rm.run_prog(*rm.split(x, n), n) == x


def test_twin_is_reversed_route_or_other_header():
    for n in range(2, 9):
        for x in range(2 ** n):
            f, prog = rm.split(x, n)
            if rm.pal(x, n):
                assert rm.P(x, n) == rm.run_prog(1 - f, prog, n)
            else:
                assert rm.P(x, n) == rm.run_prog(x & 1, rm.J(prog, n - 1), n)


def test_save_is_the_inverse_of_read():
    for n in range(2, 9):
        for crease in (0, 1):
            R = rm.ring(n, crease)
            assert [rm.save(a, n, crease) for a in range(len(R))] == R
            assert all(rm.read(x, n, crease) == a for a, x in enumerate(R))


def test_read_and_save_at_width_64_store_nothing():
    a = rm.read(0x243F6A8885A308D3, 64)
    assert a == 2427008858123944441 and rm.save(a, 64) == 0x243F6A8885A308D3


def test_address_jumps_are_the_dihedral_relations():
    for N in (4, 8, 16, 256):
        for a in range(N):
            assert rm.TWIN(rm.TWIN(a, N), N) == a
            assert rm.TP(a, N) == rm.NEXT(rm.TWIN(a, N), N) and rm.PT(a, N) == rm.TWIN(rm.NEXT(a, N), N)
            assert rm.TWIN(rm.NEXT(rm.TWIN(a, N), N), N) == rm.BACK(a, N)


def test_widen_puts_the_narrow_ring_at_the_centre():
    for n in range(2, 7):
        R, R2 = rm.ring(n), rm.ring(n + 2); h, h2 = len(R) // 2, len(R2) // 2
        centre = [rm.widen(y, n, '11') for y in R[:h] if not rm.pal(y, n)]
        assert R2[h2 - len(centre):h2] == centre
        for y in range(2 ** n):
            for fr in ('00', '01', '10', '11'):
                assert rm.narrow(rm.widen(y, n, fr), n + 2) == (fr, y)


def test_centre_bit_carries_the_seam_at_even_width():
    for n in (2, 4, 6):
        assert rm.seam(rm.ring(n + 1)) == tuple(rm.centre1(x, n) for x in rm.seam(rm.ring(n)))
        assert all(rm.uncentre(rm.centre1(x, n), n + 1) == x for x in range(2 ** n))


def test_native_header_reads_the_ring():
    for n in range(2, 9):
        assert rm.frame(rm.walk(n), n) == rm.ring(n)


def test_four_header_operations_at_native_width():
    for n in range(2, 9):
        got = {op: rm.run_states(rm.frame(rm.apply_op(rm.walk(n), op), n), n)['cls'] for op in rm.OPS}
        assert got == {'drawn': 'ring', 'J': 'twin ring', 'C': 'twin ring', 'sheet': 'ring'}


def test_sheet_reading_of_the_two_bit_walk_is_the_counter_ring():
    assert rm.frame(rm.apply_op(rm.walk(2), 'sheet'), 2) == rm.ring(2, crease=0)


def test_workbook_windows_two_bits_stride_one():
    assert rm.frame('00100111', 2, stride=1) == [0b00, 0b01, 0b10, 0b00, 0b01, 0b11, 0b11, 0b10]
    assert rm.frame(rm.apply_op('00100111', 'sheet'), 2, stride=1) == [0b00, 0b00, 0b01, 0b11, 0b10, 0b01, 0b11, 0b10]


def test_walk_read_backwards_flips_only_palindromes():
    for n in range(2, 9):
        assert rm.frame(rm.walk(n)[::-1], n) == [rm.C(x, n) if rm.pal(x, n) else x for x in rm.ring(n)]


def test_operand_reading_of_27_returns_home():
    r = rm.run_operands(rm.frame(rm.walk(2), 2), 2)
    assert r['closes'] and r['route'] == [0b00, 0b00, 0b10, 0b11]
```

## `build_notebook.py` (sha `b67044ee1b0af5925cf1fa303cf9273170d0256fc1def3f23d8c99209bf69d21`)

```python
"""Assemble ring_machine.ipynb: one self-contained notebook (its own library cell), then execute it."""
import nbformat as nbf, re
from nbclient import NotebookClient

lib = open('ring_machine.py').read().rstrip('\n')
tests = open('test_ring_machine.py').read()
tests = tests.split('import ring_machine as rm', 1)[1].strip('\n')
md, code = nbf.v4.new_markdown_cell, nbf.v4.new_code_cell
cells = []

cells.append(md("""# The ring machine
NEXUS § 202 · Dean A. Kulik, QuHarmonics Research Group (ORCID 0009-0003-3128-8828) · built with Claude, 30 Oct 2026

Nothing is written into this machine. Its field is the ring walks themselves, from B₂ = `27` to the 256-byte walk of R₈. A program sets only a header: how a reader cuts the stored circle into words. The instructions are the rings' own operations, each carrying its way home: pass and flip, XOR, next, twin, the two crease jumps, reverse, header flip and widen. Saving is not a separate act. The save is the reader run backwards. Only the record's J, C and P, its builder, and its O(n) rank are used, and nothing is fitted."""))

cells.append(code("# ---- the machine: library cell (self-contained) ----\n" + lib))

cells.append(code("""# ---- self-checks: what the machine must do, from the record (16 checks) ----
import __main__ as rm
""" + tests + """

checks = [v for k, v in sorted(globals().items()) if k.startswith('test_') and callable(v)]
for t in checks: t()
print(f'{len(checks)} / {len(checks)} checks pass')"""))

cells.append(md("""## The field
Each walk B_n is every n-bit word once, in the record's order, written end to end: n·2ⁿ bits. At n = 4 a word is one hex digit, so B₄ is the hex alphabet itself, arranged so that every symbol faces its twin. At n = 8 a word is one byte, so B₈ is the byte alphabet arranged the same way."""))

cells.append(code("""import collections, hashlib, random
for n in range(2, 9):
    hx = walk_hex(n)
    print(f'B_{n}: {n * 2 ** n:5d} bits = {n * 2 ** n // 8:4d} bytes  {hx if len(hx) <= 64 else hx[:64] + "..."}  '
          f'sha256 {hashlib.sha256(bytes.fromhex(hx)).hexdigest()[:16]}')
R4 = ring(4)
print('\\nB_4 as hex digits, each facing its twin across the crease:')
print('  ' + ' '.join(format(x, 'x') for x in R4[:8]) + '  |  ' + ' '.join(format(x, 'x') for x in R4[8:]))
print('  twins: ' + '  '.join(f'{x:x}<->{P(x, 4):x}' for x in R4[:8]))"""))

cells.append(md("""## Instructions
Nothing new is added. Every instruction is an operation the rings already perform, and each has its inverse. On the 2-bit ring (the byte `27`) the address jumps give four routes from address 0. Each word of R₄ is a header bit followed by a program of passes and flips. WIDEN puts a frame around a word, and its inverse returns the frame, the middle, and the middle's address one ring down. That is the construction memory a saturated field would otherwise lose."""))

cells.append(code("""R2 = ring(2); N2 = 4
for name, f in (('NEXT (T)', NEXT), ('TWIN (P)', TWIN), ('TP', TP), ('PT', PT)):
    route, a = [0], f(0, N2)
    while a != 0: route.append(a); a = f(a, N2)
    fixed = [a for a in range(N2) if f(a, N2) == a]
    print(f'{name:9}: from address 0: {" -> ".join(map(str, route + [0]))}   fixed addresses {fixed}   '
          f'words {" ".join(bits(R2[a], 2) for a in route)}')
inv = all(J(J(x, n), n) == x and C(C(x, n), n) == x and all((x ^ d) ^ d == x for d in range(0, 2 ** n, 7))
          for n in range(1, 9) for x in range(2 ** n))
inv &= all(BACK(NEXT(a, N), N) == a and TWIN(TWIN(a, N), N) == a and TP(TP(a, N), N) == a and PT(PT(a, N), N) == a
           for N in (4, 16, 256) for a in range(N))
print(f'inverses (NEXT/BACK, TWIN, TP, PT, REVERSE J, HEADER C, XOR d), every word and address n = 1..8: {inv}')

print('\\nR_4, word by word: header bit, program (0 pass, 1 flip), twin; frame, middle, middle address one ring down (WIDEN undone)')
h = 8
for a, x in enumerate(R4):
    f, prog = split(x, 4); fr, mid = narrow(x, 4)
    twin_how = 'other header' if pal(x, 4) else 'reversed route'
    centre = '  centre block (follows R_2)' if a < h and fr == '11' and not pal(mid, 2) else ''
    print(f'  {a:2d} {bits(x, 4)}  header {f} program {bits(prog, 3)}  twin {bits(P(x, 4), 4)} ({twin_how:14})  '
          f'frame {fr} middle {bits(mid, 2)} -> R_2 address {read(mid, 2)}{centre}')
print('\\nthe seam carried up by the centre-1 insertion:', [tuple(bits(v, n + 1) for v in seam(ring(n + 1))) for n in (2, 4, 6)])"""))

cells.append(md("""## Save from read
`read` gives a word's address through the record's O(n) rank. `save` is that reader inverted by bisection: there is no table and nothing is stored. It rebuilds every field word for word, and it works at 64 bits, where no field could be written out."""))

cells.append(code("""for n in range(2, 9):
    for crease in (1, 0):
        assert [save(a, n, crease) for a in range(2 ** n)] == ring(n, crease)
print('n = 2..8, both crease bits: save(a) rebuilds every word of the field from the reader alone')
x = 0x243F6A8885A308D3; a = read(x, 64)
print(f'n = 64: read(0x243F6A8885A308D3) = {a:,}   save({a:,}) = {save(a, 64):#018x}')
random.seed(202); ok = 0
for _ in range(200):
    a = random.randrange(2 ** 64); w = save(a, 64); ok += read(w, 64) == a and save(2 ** 64 - 1 - a, 64) == P(w, 64)
print(f'n = 64: {ok}/200 random addresses round-trip, each twin at the mirror address')
b4 = bytes.fromhex(walk_hex(4))
print('B_4 saved as addresses in the byte ring R_8:', [read(v, 8) for v in b4], ' -> read back:', bytes(save(read(v, 8), 8) for v in b4).hex())"""))

cells.append(md("""## The header
A header is the reader's frame, and it can set seven things:
- which end it reads from (J);
- whether it flips the header bit (C);
- both together, which is the workbook's *sheet* reading;
- which way the crease is read (the crease bit);
- the word width;
- where the first cut falls: the phase inside a word, and the start address (which word is read first);
- whether it cuts the circle into words or slides along it.

The stored bits never change. First comes the workbook's own header on the 2-bit circle, then what each walk becomes at its own width under the four readings."""))

cells.append(code("""s = walk(2)
print('workbook circle', s, ' sheet reading', apply_op(s, 'sheet'))
for op in ('drawn', 'sheet'):
    win = frame(apply_op(s, op), 2, stride=1)
    off = frame(apply_op(s, op), 2, phase=3, stride=1)
    print(f'  {op:5} sample 2, stride 1: {" ".join(bits(v, 2) for v in win)}   offset 3: {" ".join(bits(v, 2) for v in off)}'
          f'   (offset 3 = the same windows rotated by 3: {off == win[3:] + win[:3]})')
print()
for n in range(2, 9):
    for crease in (1, 0):
        out = []
        for op in OPS:
            words = frame(apply_op(walk(n, crease), op), n)
            st = run_states(words, n)
            ident = ' (= R_n, record crease)' if words == ring(n, 1) else ' (= R_n, counter crease)' if words == ring(n, 0) else ''
            out.append(f'{op}: {st["cls"]}{ident}')
        print(f'B_{n} crease {crease}:  ' + ' | '.join(out))
print('\\nB_3, the four readings word by word:')
for op in OPS:
    print(f'  {op:5}', ' '.join(bits(v, 3) for v in frame(apply_op(walk(3), op), 3)))
MAPS = {'drawn': lambda x, n: x, 'J': lambda x, n: C(x, n) if pal(x, n) else x,
        'C': lambda x, n: C(x, n), 'sheet': lambda x, n: x if pal(x, n) else C(x, n)}
ok = all(frame(apply_op(walk(n, c), op), n) == [MAPS[op](x, n) for x in ring(n, c)]
         for n in range(2, 9) for c in (1, 0) for op in OPS)
comm = all(MAPS[op](P(x, n), n) == P(MAPS[op](x, n), n) for n in range(2, 9) for op in OPS for x in range(1 << n))
print('\\nwhat each reading does to the word at every address, n = 2..8, both creases:')
print('  drawn: nothing | J: complements the palindromes | C: complements every word | sheet: complements the non-palindromes ->', ok)
print('  each of the four commutes with the twin map P on every word ->', comm)
print('  n = 2: the non-palindromes are 01 and 10, the seam pair; complementing them swaps them, sheet(R_2) = counter crease ->',
      [MAPS['sheet'](x, 2) for x in ring(2, 1)] == ring(2, 0))"""))

cells.append(md("""## Saturation run 1: every word is a file
Every n-bit word is a header bit followed by a program of passes and flips. Under the four readings (as stored, from the other end, header flipped, and both) one file becomes up to four files. The table counts how many files fall into reading orbits of size 2 and size 4. It also counts how many files have their twin inside their own orbit, and how many programs end on the bit they started from."""))

cells.append(code("""for n in range(2, 9):
    N = 2 ** n; orbit = collections.Counter(); home = 0; twin_in = 0
    for x in range(N):
        o = {x, J(x, n), C(x, n), C(J(x, n), n)}; orbit[len(o)] += 1
        home += bin(split(x, n)[1]).count('1') % 2 == 0; twin_in += P(x, n) in o
    print(f'n={n}: {N:3d} files  orbit size 2: {orbit[2]:3d} (palindromes {sum(pal(x, n) for x in range(N)):2d} + anti-palindromes '
          f'{sum(J(x, n) == C(x, n) for x in range(N)):2d})  orbit size 4: {orbit[4]:3d}  twin in its own orbit {twin_in}/{N}  '
          f'programs ending on their header bit {home}  two files read into one under a single header: '
          f'{sum(len({h(x) for x in range(N)}) < N for h in (lambda x: x, lambda x: J(x, n), lambda x: C(x, n), lambda x: C(J(x, n), n)))}')"""))

cells.append(md("""## Saturation run 2: every walk under every header
This is 2,464 runs: 7 walks × 2 crease bits × 4 readings × reader widths 1–8 × (every cut phase plus the slide).
- **State reading:** the words are the states visited. A run *closes* when every word appears exactly once and every slot faces its twin.
- **Operand reading:** the words are XOR operands on a register that starts on nothing. A run *returns home* when the register ends where it began.

Each cell of the matrices below is a count over that walk's headers at that reader width. The start address is held at the first word here; at the end, every list that holds every word once is turned through every start."""))

cells.append(code("""RUNS = []
for n in range(2, 9):
    for crease in (1, 0):
        for op in OPS:
            sop = apply_op(walk(n, crease), op)
            for w in range(1, 9):
                for kind, p in [('cut', p) for p in range(w)] + [('slide', 0)]:
                    words = frame(sop, w, phase=p, stride=(w if kind == 'cut' else 1))
                    RUNS.append(dict(n=n, crease=crease, op=op, w=w, kind=kind, phase=p, st=run_states(words, w), od=run_operands(words, w)))
print(len(RUNS), 'runs')
def matrix(title, key):
    print(title); print('       ' + ''.join(f'w={w:<6}' for w in range(1, 9)))
    for n in range(2, 9):
        cells_ = []
        for w in range(1, 9):
            sel = [r for r in RUNS if r['n'] == n and r['w'] == w]
            cells_.append(f'{sum(key(r) for r in sel):>2}/{len(sel):<5}')
        print(f'  B_{n}  ' + ''.join(cells_))
matrix('state reading: closes', lambda r: r['st']['closes'])
matrix('state reading: no word repeated (no collision)', lambda r: not r['st']['collide'])
matrix('operand reading: returns home', lambda r: r['od']['closes'])
matrix('operand reading: returns home without revisiting a state', lambda r: r['od']['closes'] and not r['od']['collide'])
print('\\nevery closing run:')
for r in RUNS:
    if r['st']['closes'] and not (r['w'] == r['n'] and r['kind'] == 'cut' and r['phase'] == 0):
        print(f"  B_{r['n']} crease {r['crease']} {r['op']:5} w={r['w']} {r['kind']} phase {r['phase']}: {r['st']['cls']}")
print('  plus, for every walk, the 8 headers at its own width cut at phase 0 (4 readings x 2 crease bits)')
print('\\nwhat the runs become, by reader width w against walk width n:')
for rel, f in (('w < n, w divides n', lambda r: r['w'] < r['n'] and r['n'] % r['w'] == 0),
               ('w < n, w does not divide n', lambda r: r['w'] < r['n'] and r['n'] % r['w']),
               ('w = n', lambda r: r['w'] == r['n']), ('w > n', lambda r: r['w'] > r['n'])):
    sel = [r for r in RUNS if f(r)]
    print(f'  {rel:27} {len(sel):5d} runs  ' + ', '.join(f'{k} {v}' for k, v in collections.Counter(r['st']['cls'] for r in sel).most_common()))
print('\\nown width, cut late: the phases at which the walk is still every word once (reading/crease)')
for n in range(2, 9):
    hits = collections.defaultdict(list)
    for r in RUNS:
        if r['n'] == n and r['w'] == n and r['kind'] == 'cut' and r['phase'] > 0 and not r['st']['collide']:
            hits[r['phase']].append(f"{r['op']}/{r['crease']}")
    print(f'  B_{n}: ' + '; '.join(f'phase {p}: {" ".join(v)}' for p, v in sorted(hits.items())))
def column_parity_even(t, stride):
    g = math.gcd(len(t), stride); return all(t[r::g].count('1') % 2 == 0 for r in range(g))
agree = sum(r['od']['closes'] == column_parity_even(apply_op(walk(r['n'], r['crease']), r['op']), r['w'] if r['kind'] == 'cut' else 1)
            for r in RUNS)
print('\\noperand reading: the register comes home iff every residue class of the read string mod gcd(length, stride) has even weight')
print(f'  agrees on {agree} / {len(RUNS)} runs; slides come home {sum(r["od"]["closes"] for r in RUNS if r["kind"] == "slide")}'
      f' / {sum(r["kind"] == "slide" for r in RUNS)}')
def faces(ws, w): N = len(ws); return all(ws[N - 1 - a] == P(ws[a], w) for a in range(N))
def starts(ks, N): return 'starts 0 and N/2 (the seam)' if ks == (0, N // 2) else 'starts ' + ', '.join(map(str, ks)) if ks else 'no start'
tally = collections.Counter()
for r in RUNS:
    w = r['w']; N = 1 << w
    if not (r['st']['K'] == N and r['st']['distinct'] == N): continue
    ws = frame(apply_op(walk(r['n'], r['crease']), r['op']), w, phase=r['phase'], stride=w if r['kind'] == 'cut' else 1)
    ks = tuple(k for k in range(N) if faces(ws[k:] + ws[:k], w))
    tally[('B_2' if r['n'] == 2 else 'B_3..B_8', 'closes from start 0' if r['st']['closes'] else 'every word once, not facing', starts(ks, N))] += 1
print('\\nstart address: every list that holds every word once, turned by k words, k = 0..N-1')
for (grp, cls, where), v in sorted(tally.items()):
    print(f'  {grp:9} {cls:28} {v:3d} runs  face from {where}')
s2 = walk(2)
print('  the 8-bit circle read from the other end is itself turned by', [k for k in range(8) if s2[k:] + s2[:k] == s2[::-1]], 'bits')"""))

cells.append(md("""## What the run shows
**Where a walk closes.** A walk closes only at its own width, cut where it was written. That is 8 of its 352 headers for every walk from B₃ to B₈. Each of those also closes when the list starts at its middle address N/2, the seam, and from no other start. B₂ has 12, because cutting the byte `27` one bit late also gives facing rings that start on a middle word (`01` as stored). The other four one-bit-late cuts of `27` close too, once the list starts one word later or earlier, because read from the other end the circle `00100111` is itself turned by five bits. From n = 3 on, a cut that holds every word once without facing does not face from any start. Every other header opens the same bits onto something that does not close.

**What only the header changes.** At its own width the header does one thing to the word at every address, and nothing else.
- As stored: nothing. The walk reads as R_n.
- From the other end: it complements the palindromes and leaves the rest.
- Header bit flipped: it complements every word.
- Sheet: it complements the non-palindromes and leaves the palindromes.

All four commute with the twin map, so every reading of a ring is a ring. As stored and as sheet it opens on nothing; from the other end and flipped it opens on everything (1ⁿ), which is the twin file. At n = 2 the only non-palindromes are the seam pair `01` and `10`, so complementing them swaps them. That is why the workbook's sheet reading is the counter's crease, the one bit § 200 left open.

**Cut late, the alphabet survives.** From n = 6 to 8, the walk cut one or two bits late (as stored or flipped) still holds every word exactly once, and so does the walk cut one or two bits early (from the other end, or as sheet). It is the whole alphabet in another arrangement, and it does not face. Cuts further from the written phase bring copies, and at n = 3–5 the crease bit decides some of the late cuts.

**Other widths.** Read at a smaller width that divides n, under every header, the walk holds every smaller word in equal copies, so saturation carries down. Read at a larger width it is a partial file, and for the short walks it is often a partial file with no word repeated.

**Collisions are twins.** Under one header, two files never become the same file, because every reading is a bijection on words. A file meets another file only across headers, and what it meets is one of its own readings; its twin is always among them. Inside a run, a repeated word is a copy at another address.

**Operands.** Whether the register comes home is column parity. It comes home when every bit column of the read string, taken mod gcd(length, stride), has even weight, and that holds on all 2,464 runs. So coming home counts the 1s in each column and never sees the order. Every slide comes home, because each walk has even weight. Order shows only in revisiting: a run comes home without revisiting a state only for short walks read wide.

**Memory.** The field is the only thing built, and `save()` rebuilds all of it from the reader alone. At 64 bits, where no field can be written out, every address comes from reading and every word from the read inverted."""))

nb = nbf.v4.new_notebook(); nb.cells = cells
nb.metadata['kernelspec'] = {'name': 'python3', 'display_name': 'Python 3', 'language': 'python'}
NotebookClient(nb, timeout=600, kernel_name='python3').execute()
nbf.write(nb, 'ring_machine.ipynb')
errs = [o for c in nb.cells if c.cell_type == 'code' for o in c.outputs if o.output_type == 'error']
print('cells', len(nb.cells), 'errors', len(errs))
```

## `checks202.py` (sha `9b36bc1e2dc585ad190c9eed05e60c8c7021b47228ebc869aa4a97d906c2c31b`)

```python
"""§202 checks of the sealed predictions P1-P5 (seal202/predictions.txt, sha256 90723023...b14f)."""
import collections, math, sys
from ring_machine import J, C, P, pal, ring, walk, frame, apply_op, OPS, run_states, run_operands

MAPS = {'drawn': lambda x, n: x,
        'J':     lambda x, n: C(x, n) if pal(x, n) else x,
        'C':     lambda x, n: C(x, n),
        'sheet': lambda x, n: x if pal(x, n) else C(x, n)}

# P1: at own width, cut phase 0, each reading is an address-wise map on the ring
p1 = all(frame(apply_op(walk(n, c), op), n) == [MAPS[op](x, n) for x in ring(n, c)]
         for n in range(2, 13) for c in (1, 0) for op in OPS)
print('P1 header = address-wise map (drawn id, J flips palindromes, C flips all, sheet flips non-palindromes), n=2..12 both creases:', p1)

# P2: the four maps commute with the twin map P
p2 = all(MAPS[op](P(x, n), n) == P(MAPS[op](x, n), n) for n in range(2, 13) for op in OPS for x in range(1 << n))
print('P2 each map commutes with P on every word, n=2..12:', p2)

# the notebook's 2,464 runs, rebuilt the same way
RUNS = []
for n in range(2, 9):
    for c in (1, 0):
        for op in OPS:
            s = apply_op(walk(n, c), op)
            for w in range(1, 9):
                for kind, p in [('cut', p) for p in range(w)] + [('slide', 0)]:
                    stride = w if kind == 'cut' else 1
                    words = frame(s, w, phase=p, stride=stride)
                    RUNS.append(dict(n=n, c=c, op=op, w=w, kind=kind, p=p, s=s, stride=stride, words=words,
                                     st=run_states(words, w), od=run_operands(words, w)))
print('runs rebuilt:', len(RUNS))

# P3: register returns home <=> every residue class of the read string mod gcd(L, stride) has even weight
def column_parity_even(s, stride):
    g = math.gcd(len(s), stride)
    return all(sum(int(b) for b in s[r::g]) % 2 == 0 for r in range(g))
mism = [r for r in RUNS if r['od']['closes'] != column_parity_even(r['s'], r['stride'])]
print('P3 home <=> column parity mod gcd(L, stride) even: mismatches', len(mism), 'of', len(RUNS))
print('   slides returning home:', sum(r['od']['closes'] for r in RUNS if r['kind'] == 'slide'), 'of', sum(r['kind'] == 'slide' for r in RUNS))

# P4: start address = rotation of the word list by k words
def faces(words, w):
    N = len(words)
    return all(words[N - 1 - a] == P(words[a], w) for a in range(N))
full = [r for r in RUNS if r['st']['K'] == 1 << r['w'] and r['st']['distinct'] == 1 << r['w']]
rot_close = collections.Counter()
nonfacing_that_face = 0
for r in full:
    N = 1 << r['w']; ws = r['words']
    ks = tuple(k for k in range(N) if faces(ws[k:] + ws[:k], r['w']))
    if r['st']['closes']:
        rot_close[ks == (0, N // 2)] += 1
    else:
        nonfacing_that_face += bool(ks)
print('P4 runs reading every word once:', len(full), ' closing at k=0:', sum(r['st']['closes'] for r in full))
print('   closing runs whose closing rotations are exactly {0, N/2}:', rot_close[True], ' other sets:', rot_close[False])
print('   non-facing full runs that face at some rotation:', nonfacing_that_face)

# P5: drawn walk cut at own width, phases holding every word once, n = 6..14
p5 = {}
for n in range(6, 15):
    for c in (1, 0):
        s = walk(n, c); N = 1 << n
        p5[(n, c)] = tuple(p for p in range(n) if len(set(frame(s, n, phase=p))) == N)
print('P5 phases with every word once (drawn, own width):')
for (n, c), ph in p5.items():
    print(f'   n={n:2d} crease {c}: {ph}')
print('P5 holds (all = (0, 1, 2)):', all(ph == (0, 1, 2) for ph in p5.values()))
```

## `seal202/predictions.txt` (sha `90723023128a7e061dce33226eb725b1d7d9a3225e2fe584d60ad9fb59e6b14f`)

```text
§202 sealed predictions (written before checks202.py is run)
P1  At own width, cut phase 0, every n = 2..12 and both creases: the word a reading puts at address a is f(R[a]), with
    drawn = identity, J = complement iff R[a] is a palindrome, C = complement, sheet = complement iff R[a] is not a palindrome.
P2  Each of the four maps commutes with P on every word, n = 2..12. (So every reading of a ring is a ring; drawn/sheet start on 0, J/C on 1^n.)
P3  For all 2,464 runs of the notebook, the operand register returns home  <=>  every residue class of the read string
    mod gcd(L, stride) has even weight (L = string length). Slide: gcd = 1, the walk's parity, always even.
P4  Start address (rotating the word list by k words, k = 0..N-1): a run that closes at k = 0 closes at exactly k in {0, N/2}.
    No run that reads every word once without facing faces at any rotation.
P5  Drawn walk, both creases, cut at own width: every word once exactly at phases {0, 1, 2} for every n = 6..14.
```

## `checks203.py` (sha `4e9d5be19626bf69739429fc74c2d5cbcaa1809c7a794277bd94fac2a7f06e47`)

```python
"""NEXUS s203 checks: one stored byte, read. The field is B_2 = 00100111 (0x27), stored once. Every reading is the
workbook's reader contract W_{h,o,w}(t) = (h(S)_{(t+o+j) mod 8})_{j<w}. Nothing is built per width."""
import collections

S = '00100111'                                            # the 2-bit walk, the only thing stored
FLIP = str.maketrans('01', '10')
HEAD = {'drawn': lambda s: s,                             # as stored
        'J':     lambda s: s[::-1],                       # read from the other end
        'C':     lambda s: s.translate(FLIP),             # header bit flipped everywhere
        'sheet': lambda s: s[::-1].translate(FLIP)}       # the workbook's Reading switch
def W(h, o, w, t):
    s = HEAD[h](S); return int(''.join(s[(t + o + j) % 8] for j in range(w)), 2)
def loop(s): return ''.join(str(int(s[k]) ^ int(s[(k + 1) % 8])) for k in range(8))   # (I+T)s: the step loop
def turn(s, k): return s[k:] + s[:k]                                                     # T^k: start k bits later
def mask(w): return (1 << w) - 1
s0 = int(S, 2)

print('1. the header is a jump: each reading\'s step loop is the drawn loop entered somewhere else')
for h in HEAD:
    L = loop(HEAD[h](S)); ks = [k for k in range(8) if turn(loop(S), k) == L]
    print(f'   {h:5} circle {HEAD[h](S)}  step loop {L}  = drawn loop {loop(S)} entered at bit {ks}')

print('\n2. at full width, reading is multiplication mod 255 (2^8 - 1)')
ok = all(W('drawn', 0, 8, t) == s0 * pow(2, t, 255) % 255 for t in range(8))
print(f'   window t of the stored circle = 39 * 2^t mod 255 for every t: {ok}   '
      f'({" ".join(format(W("drawn", 0, 8, t), "02x") for t in range(8))})')
print(f'   complement = -x mod 255 for every byte (0x00 and 0xff are the same residue): '
      f'{all((x ^ 255) % 255 == (-x) % 255 for x in range(256))}')
for h in HEAD:
    v = int(HEAD[h](S), 2)
    hits = [(sg, k) for sg in (1, -1) for k in range(8) if v == sg * pow(2, k, 255) * s0 % 255]
    print(f'   {h:5} = 0x{v:02x} = ' + ' or '.join(f'{"-" if sg < 0 else "+"}2^{k} * 39 mod 255' for sg, k in hits))
orbit = sorted({sg * pow(2, k, 255) * s0 % 255 for sg in (1, -1) for k in range(8)})
reads = sorted({int(turn(HEAD[h](S), o), 2) for h in HEAD for o in range(8)})
print(f'   all 4 headers x 8 starts give {len(reads)} bytes; the orbit of 39 under x2 and x(-1) has {len(orbit)}: '
      f'same set {reads == orbit}')

print('\n3. every window at every width is a digit read: W = floor(2^w * frac(2^(t+o) * v / 255)), v = the header\'s own byte')
tot = good = 0
for h in HEAD:
    v = int(HEAD[h](S), 2)
    for o in range(8):
        for w in range(1, 9):
            for t in range(8):
                tot += 1; good += W(h, o, w, t) == (2 ** w * ((v * pow(2, t + o, 255)) % 255)) // 255
print(f'   {good} / {tot} windows   (drawn 39/255 = 13/85, J 228/255 = 76/85, C 216/255 = 72/85 = 1 - 13/85, '
      f'sheet 27/255 = 9/85 = 1 - 76/85)')
n = 10 ** 18 + 3
print(f'   jump to bit {n:,} without walking: 2^n mod 255 = {pow(2, n, 255)}, window there = '
      f'{format((2 ** 8 * (s0 * pow(2, n, 255) % 255)) // 255, "08b")} = window at bit {n % 8}: '
      f'{format(W("drawn", 0, 8, n % 8), "08b")}')

print('\n4. a window is a run: header bit, step program, tail; stepping the reader pops the header and pushes a tail')
ok_tail = ok_step = ok_shape = ok_save = True
for h in HEAD:
    for o in range(8):
        for w in range(2, 9):
            for t in range(8):
                x = W(h, o, w, t); head = x >> (w - 1); tail = x & 1
                shape = (x >> 1) ^ (x & mask(w - 1))                       # adjacent XOR inside the window
                ok_tail &= tail == head ^ (bin(shape).count('1') & 1)       # tail = header + the whole program
                nxt = W(h, o, w, (t + 1) % 8)
                ok_step &= nxt == 2 * x - (head << w) + (nxt & 1)           # pop header, double, push tail
                ok_shape &= shape == W(h, o, w - 1, t) ^ W(h, o, w - 1, (t + 1) % 8)   # shape at w = step at w-1
            acc = W(h, o, w - 1, 0)                                         # save from read: one opening word,
            for t in range(8):                                              # then integrate the width-w shapes
                ok_save &= acc == W(h, o, w - 1, t)
                x = W(h, o, w, t); acc ^= (x >> 1) ^ (x & mask(w - 1))
print(f'   tail = header XOR (parity of the step program): {ok_tail}')
print(f'   next window = 2 * window - 2^w * header + new tail: {ok_step}')
print(f'   shape inside each width-w window = XOR of the two width-(w-1) windows it covers: {ok_shape}')
print(f'   width-(w-1) table = its opening word + running XOR of the width-w shapes: {ok_save}')

print('\n5. the library is bounded by the file: every word each width can show, under all 4 headers x 8 starts')
for w in range(1, 9):
    seen = collections.Counter(W(h, o, w, t) for h in HEAD for o in range(8) for t in range(8))
    by = {h: len({W(h, 0, w, t) for t in range(8)}) for h in ('drawn', 'sheet')}
    miss = [format(x, f'0{w}b') for x in range(2 ** w) if x not in seen]
    print(f'   w={w}: {len(seen):3d} / {2 ** w:3d} words  (drawn alone {by["drawn"]}, sheet alone {by["sheet"]})'
          + (f'  missing {" ".join(miss)}' if 0 < len(miss) <= 8 else ''))
```

## `msm203.py` (sha `d1cd0a3ce17145a8c60a62ed7f1719568ed7c5ac4cbc7f168810c39039ad9389`)

```python
"""NEXUS s203: the write-up's reconstruction matrix M S^T M is the running XOR (strictly lower all-ones)."""
import numpy as np
idx = np.arange(8)
M = ((idx[:, None] & idx[None, :]) == idx[None, :]).astype(int)          # the write-up's M_8
S = np.zeros((8, 8), int); S[np.arange(7), np.arange(1, 8)] = 1           # superdiagonal shift
R = (M @ S.T @ M) % 2
L = np.tril(np.ones((8, 8), int), -1)                                      # row t = XOR of rows u < t
print('M S^T M:\n', R)
print('equals the strictly-lower all-ones matrix (running XOR of the rows above):', np.array_equal(R, L))
```

The write-up's verification suite was run exactly as extracted from the attachment (sha `f37930e968ff7334e61b342d51189a97435da2bf7958917a5a511b3c5bda6fdc`). It is printed there and not repeated here.

## `checks204.py` (sha `4d1953fe532c43a3b330b1b9803f54372916044cddddad4ab44f62779f654496`)

Run with capstone 5.0.7 installed (`pip install capstone`).

```python
"""NEXUS s204 checks: binary is the constraint, LEN is the field. A word of LEN = 2^k bits has 2^k bit addresses, and
those are exactly the k-bit inputs. Read address by address, the word IS a k-input command: the input is where you
read, the bit there is the output. Nothing is decoded and nothing is invented. Uses only the s202 library."""
import sys; sys.path.insert(0, '/home/claude/w203/src')
from ring_machine import J, C, P, pal, ring, walk, bits, read      # s202 library, sha a6e94897e76ef7d3...

def tab(f, k):                     # the word of a k-input command: bit i, left to right, = f(input i)
    return int(''.join(str(f(*[(i >> (k - 1 - j)) & 1 for j in range(k)]) & 1) for i in range(2 ** k)), 2)
def run(x, k, *inp):               # execute the word x: read the bit at the input's address
    i = 0
    for u in inp: i = 2 * i + u
    return (x >> (2 ** k - 1 - i)) & 1
def ins(k): return [[(i >> (k - 1 - j)) & 1 for j in range(k)] for i in range(2 ** k)]
def turn(x, L, s): return ((x << s) | (x >> (L - s))) & ((1 << L) - 1) if s % L else x   # start the read s bits later
def diff(x, L): return x ^ turn(x, L, 1)                                                 # (I + T)x: the step loop
def integ(d, L, start=0):                                                               # save: running XOR from one bit
    b = [start]; db = bits(d, L)
    for k in range(L - 1): b.append(b[-1] ^ int(db[k]))
    return int(''.join(map(str, b)), 2)

ONE = {'CLEAR': lambda a: 0, 'NOT': lambda a: 1 - a, 'PASS': lambda a: a, 'SET': lambda a: 1}
TWO = {'FALSE': lambda a, b: 0, 'AND': lambda a, b: a & b, 'A&~B': lambda a, b: a & (1 - b), 'A': lambda a, b: a,
       '~A&B': lambda a, b: (1 - a) & b, 'B': lambda a, b: b, 'XOR': lambda a, b: a ^ b, 'OR': lambda a, b: a | b,
       'NOR': lambda a, b: 1 - (a | b), 'XNOR': lambda a, b: 1 - (a ^ b), '~B': lambda a, b: 1 - b,
       'A|~B': lambda a, b: a | (1 - b), '~A': lambda a, b: 1 - a, '~A|B': lambda a, b: (1 - a) | b,
       'NAND': lambda a, b: 1 - (a & b), 'TRUE': lambda a, b: 1}
N1 = {tab(f, 1): n for n, f in ONE.items()}; N2 = {tab(f, 2): n for n, f in TWO.items()}
print(f'every LEN-2 word is a distinct 1-input command: {sorted(N1) == list(range(4))};  '
      f'every LEN-4 word a distinct 2-input command: {sorted(N2) == list(range(16))}')

print('\n1. LEN 2: the stored byte 0x27 = R_2 read as commands, in ring order (slot: word command | twin)')
R2 = ring(2)
print('   ' + '   '.join(f'{a}: {bits(x, 2)} {N1[x]}' for a, x in enumerate(R2)))
print('   twins: ' + ', '.join(f'{N1[x]}<->{N1[P(x, 2)]}' for x in R2[:2]) + '   crease between slots 1 and 2')

print('\n2. LEN 4: R_4 read as commands, in ring order, each facing its twin across the crease')
R4 = ring(4); h = 8
for a in range(h):
    x, y = R4[a], R4[15 - a]
    print(f'   {a:2d} {bits(x, 4)} {N2[x]:5} {"(pal)" if pal(x, 4) else "     "} <-> {15 - a:2d} {bits(y, 4)} {N2[y]}')

print('\n3. the ring\'s operations are the logic designer\'s, for every command with k = 1, 2, 3 inputs')
for k in (1, 2, 3):
    L = 2 ** k; ok = dict(J=True, C=True, sheet=True, pal=True, slide=True)
    for x in range(2 ** L):
        f = lambda *v, x=x: run(x, k, *v)
        ok['J'] &= J(x, L) == tab(lambda *v: f(*[1 - u for u in v]), k)                 # flip every input
        ok['C'] &= C(x, L) == tab(lambda *v: 1 - f(*v), k)                              # flip the output
        ok['sheet'] &= C(J(x, L), L) == tab(lambda *v: 1 - f(*[1 - u for u in v]), k)   # De Morgan dual
        ok['pal'] &= pal(x, L) == all(f(*v) == f(*[1 - u for u in v]) for v in ins(k))
        ok['slide'] &= turn(x, L, 1) == tab(lambda *v: f(*ins(k)[(int(''.join(map(str, v)), 2) + 1) % L]), k)
    print(f'   k={k}: {2 ** L:3d} commands  J = flip every input {ok["J"]} | C = flip the output {ok["C"]} | '
          f'sheet = De Morgan dual {ok["sheet"]} | palindrome = unchanged by flipping all inputs {ok["pal"]} | '
          f'one-bit slide = add 1 to the input {ok["slide"]}')
print('   sheet pairs at LEN 4: ' + ', '.join(f'{N2[x]}<->{N2[C(J(x, 4), 4)]}' for x in (1, 14, 6, 3, 5)))

print('\n4. stacking two commands adds one input, and the new bit chooses which half runs (a MUX, Ch)')
for k in (1, 2):
    L = 2 ** k
    ok = all(run((f0 << L) | f1, k + 1, s, *v) == run(f1 if s else f0, k, *v)
             for f0 in range(2 ** L) for f1 in range(2 ** L) for s in (0, 1) for v in ins(k))
    print(f'   every pair of {k}-input commands, stacked: a {k + 1}-input command that runs the first if the new bit '
          f'is 0, the second if 1: {ok}')
B2 = int(walk(2), 2); B4 = int(walk(4), 2)
ok2 = all(run(B2, 3, a1, a0, x) == run(R2[2 * a1 + a0], 1, x) for a1 in (0, 1) for a0 in (0, 1) for x in (0, 1))
ok4 = all(run(B4, 6, *ins(4)[a], *v) == run(R4[a], 2, *v) for a in range(16) for v in ins(2))
print(f'   the walk 0x27 as a 3-input command = R_2[a](x): opcode = the 2-bit ring address a, operand x: {ok2}')
print(f'   the walk B_4 as a 6-input command = R_4[a](x1, x0): all 16 gates by 4-bit ring address: {ok4}')
print('   0x27 as the 1-bit computer: ' + '  '.join(f'op {a:02b} {N1[R2[a]]:5}: 0->{run(B2, 3, a >> 1, a & 1, 0)} '
                                                  f'1->{run(B2, 3, a >> 1, a & 1, 1)}' for a in range(4)))
CH, MAJ, X3 = (tab(lambda x, y, z: (x & y) | ((1 - x) & z), 3), tab(lambda x, y, z: (x & y) | (x & z) | (y & z), 3),
               tab(lambda x, y, z: x ^ y ^ z, 3))
print(f'   Ch  = 0x{CH:02x} = stack(B, A) {CH == (5 << 4 | 3)}   Maj = 0x{MAJ:02x} = stack(AND, OR) '
      f'{MAJ == (1 << 4 | 7)}   XOR3 = 0x{X3:02x} = stack(XOR, XNOR) {X3 == (6 << 4 | 9)}')
print(f'   OR = sheet(AND) {C(J(1, 4), 4) == 7};  XNOR = sheet(XOR) {C(J(6, 4), 4) == 9}:  '
      f'sum and carry are each a gate stacked with its own sheet reading')

print('\n5. addition falls out of 0x27: its difference is the sum, its save is the carry')
print(f'   difference of 0x27 (as stored)       = {bits(diff(B2, 8), 8)} = 0x{diff(B2, 8):02x}; '
      f'full-adder sum (XOR3) = 0x{X3:02x}: {diff(B2, 8) == X3}')
print(f'   difference of the carry (Maj, 0x{MAJ:02x}) = {bits(diff(MAJ, 8), 8)} = 0x27 turned 3 bits '
      f'({bits(turn(B2, 8, 3), 8)}): {diff(MAJ, 8) == turn(B2, 8, 3)}')
print(f'   save of 0x27 read 3 bits in, from 0  = {bits(integ(turn(B2, 8, 3), 8), 8)} = 0x{integ(turn(B2, 8, 3), 8):02x}'
      f' = the carry: {integ(turn(B2, 8, 3), 8) == MAJ}')
SUM, CAR = diff(B2, 8), integ(turn(B2, 8, 3), 8)       # the only two commands the adder uses
def add(a, b, n):
    c = 0; s = 0
    for j in range(n):
        x, y = (a >> j) & 1, (b >> j) & 1
        s |= run(SUM, 3, x, y, c) << j; c = run(CAR, 3, x, y, c)
    return s, c
ok = all(add(a, b, 8) == ((a + b) & 255, (a + b) >> 8) for a in range(256) for b in range(256))
print(f'   ripple adder whose only commands are those two words, on every pair of bytes (65,536): {ok}')
x, y = 0x243F6A8885A308D3, 0x13198A2E03707344
print(f'   at 64 bits: 0x{x:016x} + 0x{y:016x} = 0x{add(x, y, 64)[0]:016x}, carry {add(x, y, 64)[1]}; '
      f'Python: 0x{(x + y) & (2 ** 64 - 1):016x}, carry {(x + y) >> 64}')

print('\n6. no true collision, just twins: the ring writes a command left to right, LUT tools right to left (J)')
for name, v in (('sum XOR3', X3), ('carry Maj', MAJ), ('Ch', CH)):
    print(f'   {name:9} ring 0x{v:02x} at R_8 slot {read(v, 8):3d}  |  LUT spelling 0x{J(v, 8):02x} at slot '
          f'{read(J(v, 8), 8):3d}  = its twin: {P(v, 8) == J(v, 8)}, mirror slots: {read(v, 8) + read(J(v, 8), 8) == 255}')

print('\n7. the same bytes through real decoders (capstone 5): collisions, not derivations')
import capstone as cs
dec = {'x86-32': cs.Cs(cs.CS_ARCH_X86, cs.CS_MODE_32), '6502': cs.Cs(cs.CS_ARCH_MOS65XX, cs.CS_MODE_MOS65XX_6502)}
for b, what in ((0x27, 'the stored walk'), (0x69, 'its difference (sum)'), (0x17, 'the carry')):
    out = []
    for nm, d in dec.items():
        i = next(d.disasm(bytes([b, 0x10, 0x20, 0x30, 0x40, 0x50, 0x60, 0x70]), 0), None)   # room for operands
        out.append(f'{nm}: {i.mnemonic} {i.op_str}'.rstrip() if i else f'{nm}: (not a documented opcode)')
    print(f'   0x{b:02x} {what:22} ' + ' | '.join(out))
```

## `head205.py` (sha `37efc0b688ccfee47a73bc9bd6e98815a52a6be7c8b2ccc798c6304e57fae04e`)

```python
"""NEXUS s205: the read head makes the rings. The only object is ONE difference on a circle (half nothing, half
something). The head stores nothing and never sees a ring, a list of words, a sort or the builder. The s202 ring()
is imported only afterwards, to compare against."""
import sys, collections; sys.path.insert(0, '/home/claude/w203/src')

NOTHING, SOMETHING = 'o', '#'                      # two names for the one difference; swap them and nothing changes

def eyes(t, n):
    """The head at tick t of its lap (N = 2^n ticks): eye k reads the one difference 2^k times as fast."""
    N = 1 << n
    return ''.join(SOMETHING if (t << k) % N >= N // 2 else NOTHING for k in range(n))

back = lambda w: w[::-1]                                                        # read from the other end
side = lambda w: w.translate(str.maketrans(NOTHING + SOMETHING, SOMETHING + NOTHING))   # the other side
ACROSS = {'back': back, 'side': side, 'back+side': lambda w: side(back(w)),
          'native': lambda w: back(w) if back(w) != w else side(w)}   # go back; if that's no difference, other side

def head(n, across):
    """Go round once. Each reading met for the first time goes to the next near slot, its across-reading to the
    facing far slot. Returns the layout, or the first reading that faces itself (the layout breaks)."""
    N = 1 << n; slots = [None] * N; seen = set(); near = 0
    for t in range(N):
        w = eyes(t, n)
        if w in seen: continue
        a = across(w)
        if a == w: return ('breaks', w)
        slots[near], slots[N - 1 - near] = w, a; seen |= {w, a}; near += 1
    return slots

# ---------------------------------------------------------------- checks (the record enters only here)
from ring_machine import ring, P
val = lambda w: int(w.replace(NOTHING, '0').replace(SOMETHING, '1'), 2) if w else 0
print('H1  one lap of the head reads every n-bit word once, in counting order:')
print('    ' + ' '.join(f'n={n}:{all(val(eyes(t, n)) == t for t in range(1 << n))}' for n in range(1, 17)))
print('    n=3 lap:', ' '.join(eyes(t, 3) for t in range(8)))

print('\nH2  head with "across" = go back, or the other side if going back shows no difference:')
res = {}
for n in range(1, 17):
    L = head(n, ACROSS['native']); v = [val(w) for w in L]; N = 1 << n; h = N // 2
    rec = v[:h - 1] + [v[h], v[h - 1]] + v[h + 1:]
    res[n] = (v == ring(n, 0), rec == ring(n, 1), sorted(v) == list(range(N)),
              all(v[N - 1 - a] == P(v[a], n) for a in range(N)))
print('    n : = R_n (counter crease) | = R_n (record crease, middle pair swapped) | every word once | faces its twin')
for n, r in res.items(): print(f'    {n:2d}: {r[0]} | {r[1]} | {r[2]} | {r[3]}')
for n in (2, 3, 4):
    print(f'    n={n} head layout:', ' '.join(head(n, ACROSS['native'])))

print('\nH3  other meanings of "across":')
for name in ('side', 'back', 'back+side'):
    row = []
    for n in range(2, 17):
        L = head(n, ACROSS[name])
        if L[0] == 'breaks': row.append(f'n={n}: breaks at {L[1]}' if n <= 6 else f'n={n}: breaks')
        else: row.append(f'n={n}: ' + ('counter' if [val(w) for w in L] == list(range(1 << n)) else
                                        'native ring' if [val(w) for w in L] == ring(n, 0) else 'other layout'))
    print(f'    {name:9} ' + '; '.join(row))

print('\nH4  width 2, native vs side:', head(2, ACROSS['native']), head(2, ACROSS['side']),
      head(2, ACROSS['native']) == head(2, ACROSS['side']))
print('    stored walk, read off the width-2 head: ' + ''.join(head(2, ACROSS['native'])).replace(NOTHING, '0').replace(SOMETHING, '1'),
      '| record crease:', ''.join(format(x, '02b') for x in ring(2, 1)))
```

## `seal205/predictions.txt` (sha `3be3aafed660f3e6132ce8a930e4907c48de08fabf25ac12d8b30afd856a4b11`)

```text
s205 sealed predictions (written before head205.py is run). No ring, no list of words, no builder is used by the head.
The only object is one difference on a circle: half nothing, half something.
H1  A head going round that circle with n eyes, eye k reading the same difference 2^k times as fast (k = 0 slowest),
    reads every n-bit word exactly once per lap, in counting order. n = 1..16.
H2  Let the head, at each step, read its eyes forward (what it is) and across the circle (what it is from the other
    end: eyes read fast-to-slow; if that is no different, from the other side). Place each reading the first time
    it is met: forward at the next near slot, across at the facing far slot. The result, n = 1..16, is the ring R_n
    with the counter crease, exactly; the record's crease is the other order of the one middle pair.
H3  If "across" is only the other side (no going back), the head lays out the plain counter (each word facing its
    complement). If "across" is only going back, or going back on the other side, the layout breaks: some readings
    face themselves. n = 2..16 (J and back-on-other-side break for every n >= 2 where such fixed words exist).
H4  At width 2 the native ring and the counter are the same layout (going back and the other side agree on 01, 10).
```
