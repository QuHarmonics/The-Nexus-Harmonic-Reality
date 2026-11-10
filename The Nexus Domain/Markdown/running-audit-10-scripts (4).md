# NEXUS running audit 10: scripts

The scripts for §§ 202–223, printed in full, each with the sha256 of the file as run. `build_notebook.py` assembles `ring_machine.ipynb` from `ring_machine.py` and `test_ring_machine.py` and executes it. `checks202.py` checks the sealed predictions in `seal202/predictions.txt`. `checks203.py` reads the one stored byte; `msm203.py` checks the write-up's reconstruction matrix; `checks204.py` reads words of LEN 2ᵏ as commands; `head205.py` is the read head; `bbp206.py` reads π with it; `lane208.py` runs it as lane motion.

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

## `bbp206.py` (sha `1c0fe1c0a1df1df5b799cb3cf1543af147815dd7f5c8d0cb7186b19b803b941f`)

Requires mpmath (reference only).

```python
"""NEXUS s206: read pi with the s205 head, and BBP is the head. mpmath is used only as the independent reference."""
from fractions import Fraction
import mpmath

def pi_hex(N):                                    # reference: first N hex digits of pi after the point (mpmath)
    mpmath.mp.prec = 4 * N + 64
    return format(int(mpmath.floor((mpmath.pi - 3) * mpmath.mpf(16) ** N)), f'0{N}x')

# B1: the s205 head parked at angle frac(pi): eye k reads the one difference 2^k times as fast
M = 512; mpmath.mp.prec = M + 64
theta = int(mpmath.floor((mpmath.pi - 3) * mpmath.mpf(2) ** M))     # the angle, as a position on a 2^M-slot circle
eye = lambda k: int(((theta << k) % (1 << M)) >= (1 << (M - 1)))    # "something" iff 2^k * angle lands in the far half
ref_bits = ''.join(format(int(c, 16), '04b') for c in pi_hex(64))
eyes = ''.join(str(eye(k)) for k in range(256))
print(f'B1  head at angle frac(pi), eyes 0..255 = binary digits of pi: {eyes == ref_bits}')
print(f'    eyes 0..31: {eyes[:32]}  = hex {format(int(eyes[:32], 2), "08x")}')

# B2: BBP as heads. Term (k, j) is a head on a circle of 8k+j slots; jumping n hex digits = one modular power.
TERMS = ((1, 4), (4, -2), (5, -1), (6, -1))
def heads(n):
    return [(k, j, w, pow(16, n - k, 8 * k + j)) for k in range(n + 1) for j, w in TERMS]   # (where each head sits)
def digit_exact(n, tail=40):
    s = sum(w * Fraction(pos, 8 * k + j) for k, j, w, pos in heads(n))
    s += sum(w * Fraction(1, 16 ** (k - n) * (8 * k + j)) for k in range(n + 1, n + 1 + tail) for j, w in TERMS)
    return int(16 * (s - (s.numerator // s.denominator)))           # floor(16 * frac(sum))
got = ''.join(format(digit_exact(n), 'x') for n in range(64))
print(f'\nB2  hex digits 1..64 of pi from the heads alone: {got}')
print(f'    mpmath:                                    {pi_hex(64)}   match: {got == pi_hex(64)}')
print('    heads for digit 6 (n = 5): ' + ', '.join(f'{pos}/{8 * k + j}' for k, j, w, pos in heads(5)[:12]) + ', ...')

# B3: far out, double precision, no earlier digit read
def digits_float(n, m=8):
    s = 0.0
    for j, w in TERMS:
        t = 0.0
        for k in range(n + 1): d = 8 * k + j; t = (t + pow(16, n - k, d) / d) % 1.0
        k, p = n + 1, 1.0 / 16
        while p > 1e-17: t += p / (8 * k + j); k += 1; p /= 16
        s = (s + w * t) % 1.0
    out = ''
    for _ in range(m): s *= 16; out += format(int(s), 'x'); s -= int(s)
    return out
n = 100_000; far = digits_float(n); ref = pi_hex(n + 8)[n:]
ok = next((i for i in range(8) if far[i] != ref[i]), 8)
print(f'\nB3  hex digits {n + 1:,}..{n + 8:,} from the heads: {far}   mpmath: {ref}   leading digits that match: {ok}')

# B4: the one-circle case, the stored walk
print(f'\nB4  one head on 255 slots at x16, seeded 39: ' +
      ''.join(format(16 * (39 * pow(16, n, 255) % 255) // 255, 'x') for n in range(16)) + '  (39/255 = 0x0.2727...)')
```

## `seal206/predictions.txt` (sha `5e09f4dcff18fd306cf63228f09e0af546c088fb5c07c79c4d99c6364b66101c`)

```text
s206 sealed predictions (written before bbp206.py is run).
B1  The s205 head parked at angle frac(pi) on the one-difference circle: eye k reads binary digit k+1 of pi (k = 0..255),
    matching mpmath's pi.
B2  BBP's term 16^(n-k) mod (8k+j) is a head on a circle of 8k+j slots, jumped n hex digits by one modular power
    (the s203 jump = multiplication mod the circle). Hex digit n+1 of pi is where the weighted heads 4,-2,-1,-1
    (j = 1,4,5,6), summed over k, point: floor(16 * frac(sum)). Exact rational arithmetic, n = 0..63: every digit
    matches mpmath.
B3  The same heads in double precision at n = 100,000 give at least 6 correct hex digits there, without reading any
    earlier digit; checked against mpmath's pi to 400,016+ bits.
B4  The 0x27 circle is the one-circle case: one head on 255 slots read at x16 gives the hex digits of 39/255 (2727...).
```

## `lane208.py` (sha `af1020f883919428be1d84010b9ad9ec4ce64915c627e1a4f5eb275bc5298315`)

```python
"""NEXUS s208: the s205 head run as the October lane motion. One lane, base 2: 2r = d*q + r'. The crossing q leaves
(the measurement); the remainder r' persists (the shape). The head uses nothing else: no ring, sort, list or builder.
The s202 ring() is imported only afterwards, to compare."""
import sys; from fractions import Fraction
sys.path.insert(0, '/home/claude/w203/src')

def step(r, d):                        # one motion of the lane: what crosses, and what stays
    q, r2 = divmod(2 * r, d); return q, r2
def wind(seed, d, n):                  # run the lane n steps: the crossings measured, and the shape it carried
    r, qs, shape = seed, [], [seed]
    for _ in range(n): q, r = step(r, d); qs.append(q); shape.append(r)
    return qs, shape
def unwind(r_end, qs, d):              # run it backwards from where it ended: each crossing is given back, last first
    r, out = r_end, []
    for q in reversed(qs): r = (r + d * q) // 2; out.append(q)
    return out, r

def lane_head(n):
    d = 1 << n; slots = [None] * d; seen = set(); near = 0
    for t in range(d):                                      # the head goes round: tick t seeds the lane
        qs, shape = wind(t, d, n); w = tuple(qs)
        if w in seen: continue
        back, _ = unwind(shape[-1], qs, d)                  # across: give the crossings back by unwinding
        a = tuple(back) if tuple(back) != w else tuple(wind(d - 1 - t, d, n)[0])   # same both ways: other side
        slots[near], slots[d - 1 - near] = w, a; seen |= {w, a}; near += 1
    return slots

# ---------------------------------------------------------------- checks (the record enters only here)
from ring_machine import ring
def s205_eyes(t, n):                    # the s205 head's eyes, copied exactly (eye k reads the difference 2^k as fast)
    N = 1 << n; return tuple(1 if (t << k) % N >= N // 2 else 0 for k in range(n))
val = lambda qs: int(''.join(map(str, qs)), 2) if qs else 0

print('L0  a literal d = 2 lane:', [(r, wind(r, 2, 3)) for r in (0, 1)], ' -> empty after one step')

L1 = {}
for n in range(1, 17):
    d = 1 << n; ok_eye = ok_shape = ok_F = True
    for t in range(d):
        qs, shape = wind(t, d, n)
        ok_eye &= tuple(qs) == s205_eyes(t, n)
        ok_shape &= all(shape[k] == (t << k) % d for k in range(n + 1)) and shape[-1] == 0
        F = Fraction(t, d)
        for q in qs:
            F = 2 * F - q; ok_F &= 0 <= F < 1
    L1[n] = (ok_eye, ok_shape, ok_F)
print('L1  eyes = crossings | shape r_k = t*2^k mod 2^n, empty at the end | F_(k+1) = 2F_k - q_k stays in [0,1):')
print('    ' + ' '.join(f'n={n}:{"".join("T" if x else "F" for x in v)}' for n, v in L1.items()))
qs, shape = wind(5, 8, 3)
print(f'    tick 5 on 8 slots: shape {shape}, crossings {qs} = eyes {s205_eyes(5, 3)}')

L2 = {}
for n in range(1, 17):
    d = 1 << n; ok_back = ok_side = ok_home = True
    for t in range(d):
        qs, shape = wind(t, d, n); back, home = unwind(shape[-1], qs, d)
        ok_back &= tuple(back) == tuple(qs)[::-1]; ok_home &= home == t
        ok_side &= tuple(wind(d - 1 - t, d, n)[0]) == tuple(1 - q for q in qs)
    L2[n] = (ok_back, ok_side, ok_home)
print('\nL2  unwinding gives the crossings back in reverse | mirror seed crosses where t does not | unwinding returns to t:')
print('    ' + ' '.join(f'n={n}:{"".join("T" if x else "F" for x in v)}' for n, v in L2.items()))

print('\nL3  the lane head\'s layout = R_n (counter crease):')
print('    ' + ' '.join(f'n={n}:{[val(w) for w in lane_head(n)] == ring(n, 0)}' for n in range(1, 17)))
print('    n=4:', ' '.join(''.join(map(str, w)) for w in lane_head(4)))

print('\nL4  crossings weighted by 2^(n-1-k) return the seed, every tick:',
      all(sum(q << (n - 1 - k) for k, q in enumerate(wind(t, 1 << n, n)[0])) == t for n in range(1, 17) for t in range(1 << n)))
```

## `seal208/predictions.txt` (sha `284244ce4a7b0f229a47794303f6f0115e2971acb98611ed73a303cedbc98325`)

```text
s208 sealed predictions (written before lane208.py is run). The lane is the October motion with base 2:
2r = d*q + r', q = the crossing (it leaves), r' = the remainder (it persists, the shape). No ring, sort, list or builder.
L0  A literal d = 2 lane empties after one step (r' = 0 for r in {0,1}); the 2 that carries the head is the base.
L1  The s205 head's eyes at tick t are the crossings q_0..q_{n-1} of the lane seeded r_0 = t on d = 2^n, n = 1..16, every t.
    The shape after k steps is r_k = (t * 2^k) mod 2^n (what is not yet crossed); r_n = 0. The October recurrence
    F_{k+1} = 2 F_k - q_k, F_0 = t / 2^n, holds exactly and keeps 0 <= F < 1.
L2  "Across" from lane motion alone: unwinding the lane from its end (r_k = (r_{k+1} + d*q_k) / 2) emits the crossings in
    reverse order = the s205 back-reading; the lane seeded at the mirror slot d-1-t crosses where t does not = the s205
    other side.
L3  Placing each crossing word at first meeting, its across (unwind order, or the mirror seed where unwinding measures
    the same as winding) at the facing slot, gives R_n with the counter crease, n = 1..16, identical to the s205 head.
L4  The crossings weighted by 2^(n-1-k) return the seed t for every tick: the measurement integrates back to where the
    lane started (save from read).
```

## `dis209.py` (sha `37b96f526bde9cb5b4d483968f8aaf2e0c2922a9820e8f5db0c1bac4836f36f8`)

```python
"""NEXUS s209: Dean's three x86 listings of ring walks. Recover the bits, identify which reading of which walk each is,
re-decode with capstone, and separate what the decoder imposes from what the walk carries."""
import re, sys, random, collections; sys.path.insert(0, '/home/claude/w203/src')
from ring_machine import walk, ring, P, pal, bits
import capstone as cs
X = cs.Cs(cs.CS_ARCH_X86, cs.CS_MODE_32)
FLIP = str.maketrans('01', '10')
HEAD = {'drawn': lambda s: s, 'J': lambda s: s[::-1], 'C': lambda s: s.translate(FLIP), 'sheet': lambda s: s[::-1].translate(FLIP)}

def listing_bits(path):
    rows = [re.match(r'\s*[0-9a-f]+:\s+((?:[0-9a-f]{2} )+)\s+(\w+)\s+(.*)', l) for l in open(path)]
    rows = [r for r in rows if r]
    hexbytes = [b for r in rows for b in r.group(1).split()]
    assert set(hexbytes) <= {'00', '01', '10', '11'}
    return ''.join(hexbytes), [(r.group(2), r.group(3).strip()) for r in rows]

def identify(b):
    """Which walk B_n, reading, width w, read at every start (stride 1), concatenated, gives exactly these bits?"""
    hits = []
    for n in (2, 3, 4):
        for h, f in HEAD.items():
            s = f(walk(n)); L = len(s)
            for w in range(1, L + 1):
                for o in range(L):
                    rows = [(s * 3)[o + t: o + t + w] for t in range(L)]
                    if ''.join(rows) == b: hits.append((n, h, w, o, L))
    return hits

def decode(b):
    data = bytes(int(b[i:i + 2], 16) for i in range(0, len(b), 2))   # one bit per hex digit, as in the listings
    return [(i.mnemonic, i.op_str) for i in X.disasm(data, 0)]

for name in ('listing2', 'listing3', 'listing4'):
    b, mn = listing_bits(f'dis209/{name}.txt')
    hits = identify(b)
    dec = decode(b)
    print(f'{name}: {len(b)} bits, {len(mn)} instructions; re-decoded identically: {dec == mn}; '
          f'mnemonics {dict(collections.Counter(m for m, _ in mn))}')
    for n, h, w, o, L in hits[:3]:
        print(f'   = walk B_{n} ({L} bits), {h} reading, width {w} = {"full circle" if w == L else str(w) + " bits"}, '
              f'every start, first row starting at bit {o}')
    if not hits: print('   no single reading of B_2..B_4 at stride 1 matches')

print('\ncontrol: 10,000 random bit strings of 64 bits, one bit per hex digit, through the same decoder:')
random.seed(209); ms = collections.Counter()
for _ in range(10000):
    ms.update(m for m, _ in decode(''.join(random.choice('01') for _ in range(64))))
print('   mnemonics:', dict(ms))

print('\nthe decoder\'s layout: 4 bits = 2 hex digits = one instruction [opcode digit][operand digit]')
for x in range(16):
    s = bits(x, 4); (m, op), = decode(s)
    print(f'   {s}  {m} {op:22}', end='\n' if x % 2 else ' | ')

print('\nthe 4-bit ring R_4 as these instructions, each facing its twin:')
R4 = ring(4)
for a in range(8):
    x, y = R4[a], R4[15 - a]
    (m1, o1), = decode(bits(x, 4)); (m2, o2), = decode(bits(y, 4))
    print(f'   {bits(x, 4)} {m1} {o1:22} <-> {bits(y, 4)} {m2} {o2}')
print('   R_4 walk decodes to all 16 distinct instructions, once each:',
      len(set(decode(walk(4)))) == 16 and len(decode(walk(4))) == 16)
```

## `att209_check.py` (sha `b862dab74e39812d363303b3297e6bb7901233806a8aa0d66dd029aa389b0679`)

```python
"""Check the pasted stack-climb rule (up_from_stack / down_to_prev) against the s202 ring, n = 2..14, both creases."""
import sys, runpy
sys.path.insert(0, '/home/claude/w203/src'); from ring_machine import ring
g = runpy.run_path('/home/claude/w203/att209/tower_rule.py')
up, down = g['up_from_stack'], g['down_to_prev']
S = lambda n, c: [format(x, f'0{n}b').replace('0', 'o').replace('1', '#') for x in ring(n, c)]
for c in (1, 0):
    R = [w for w in [ 'oo#oo###'[2*k:2*k+2] for k in range(4)]] if c else S(2, 0)
    tower = {2: R}; okup = True
    for n in range(2, 14): tower[n + 1] = up(tower[n], c); okup &= tower[n + 1] == S(n + 1, c)
    okdn = all(down(tower[n + 1], c) == tower[n] for n in range(13, 1, -1))
    print(f'crease {c}: up 2->14 matches ring(): {okup} | down 14->2 matches: {okdn}')
```

## `acc210.py` (sha `5d2cba8242daa882e938075ee6b117158c42bd7eac94962d64f1cec45d3d0c48`)

```python
"""NEXUS s210: accumulation is what the code does. Every command is an XOR-accumulation of AND-terms (Zhegalkin), with
coefficients from the Boolean Moebius transform; the adder splits into pure accumulation (sum) and AND-terms (carry)."""
from itertools import combinations

def table(x, k): L = 1 << k; return [(x >> (L - 1 - i)) & 1 for i in range(L)]      # bit i, left to right = f(input i)
def moebius(t):                                    # ANF coefficients: c[S] = XOR of f(T) over T inside S
    c = t[:]; L = len(c); s = 1
    while s < L:
        for i in range(L):
            if i & s: c[i] ^= c[i ^ s]
        s <<= 1
    return c
def accumulate(c, k):                              # read back: f(x) = XOR over terms S inside x of c[S]
    return [sum(c[S] for S in range(1 << k) if S & x == S) & 1 for x in range(1 << k)]
def terms(c, k, names='xyz'):
    out = []
    for S in range(1 << k):
        if c[S]:
            v = ''.join(names[j] for j in range(k) if S >> (k - 1 - j) & 1)
            out.append(v or '1')
    return ' + '.join(out) or '0'

for k in (1, 2, 3):
    ok = all(accumulate(moebius(table(x, k)), k) == table(x, k) for x in range(1 << (1 << k)))
    print(f'A1  k={k}: all {1 << (1 << k):3d} commands = XOR-accumulation of AND-terms, coefficients = Moebius: {ok}')
for name, x in (('sum   0x69', 0x69), ('carry 0x17', 0x17), ('walk  0x27', 0x27), ('sheet 0x1b', 0x1b)):
    print(f'A2  {name} = {terms(moebius(table(x, 3)), 3)}   (mod 2)')
print('    the 16 two-input gates:', ', '.join(f'{x:04b}={terms(moebius(table(x, 2)), 2, "ab")}' for x in range(16)))
```

## `seal210/predictions.txt` (sha `87e76bd5c1dfca5789f4ed8858f57d7738d7cde5aaa8492d9497d2ff03b494cc`)

```text
s210 sealed predictions (written before acc210.py is run).
A1  Every k-input command (k = 1, 2, 3; all 4, 16, 256 words) is an accumulation without carry (XOR) of AND-terms
    (Zhegalkin / algebraic normal form), and the coefficients are the Boolean Moebius transform of the word (the
    s203 write-up's M matrix): reading the accumulation back gives the word, every word.
A2  The full adder splits exactly: the sum (0x69) is pure accumulation (x + y + z mod 2, no AND-term); the carry (0x17)
    is AND-terms only (xy + xz + yz mod 2). The stored walk 0x27 accumulates to at most three terms.
A3  The pasted base-16 lane run (lane209.py, extracted unchanged) prints P1, P2a, P3, P4, P5 all True and P2b = [5, 17].
```

## `angles211.py` (sha `9d0ec083d34481501be777125477869956019295dd8d3912e1a513b9d62f144d`)

```python
"""§ 211: every angle of the 2-bit circle, keeping only what is not the same (XOR = the cells where two readings differ).
Usage: python3 -I angles211.py two_bit_circle.xlsx nested_ring_beyond_2bit.xlsx"""
import sys
from collections import Counter
import openpyxl
sys.path.insert(0, '/home/claude/w203/src')
import ring_machine as rm

# ---- bit strings -------------------------------------------------------------------------------------------
def rot(s, d): d %= len(s); return s[d:] + s[:d]                  # start the read d slices later
def rev(s): return s[::-1]
def comp(s): return s.translate(str.maketrans('01', '10'))
def xor(a, b): return ''.join('1' if x != y else '0' for x, y in zip(a, b))
def wt(s): return s.count('1')
def hx(s): return format(int(s, 2), f'0{len(s) // 4}X') if len(s) % 4 == 0 else s
def runs(s, ch):                                                  # cyclic run lengths of ch
    if ch not in s: return []
    if all(c == ch for c in s): return [len(s)]
    k = next(i for i in range(len(s)) if s[i] != ch); t = s[k:] + s[:k]
    return sorted(len(r) for r in t.replace('1' if ch == '0' else '0', ' ').split())
def one_block(m): return 0 < wt(m) < len(m) and len(runs(m, '1')) == 1
def rclosed(s): return rev(s) in {rot(s, d) for d in range(len(s))}

def check(tag, ok, note=''):
    print(f"{tag}: {'PASS' if ok else 'FAIL'}{('  ' + note) if note else ''}")
    return ok

# ---- workbook reader: every 'Sample size' block of one sheet -----------------------------------------------
def read_sheet(ws):
    col = lambda r, c: ws.cell(r, c).value
    lab = {}
    for r in range(1, ws.max_row + 1):
        a = col(r, 1)
        if isinstance(a, str):
            for key in ('Circle as drawn', 'Reading', 'Cycle sampled', 'Slices N', 'Counter-clockwise start offset'):
                if a.startswith(key) and key not in lab: lab[key] = col(r, 2)
    N, blocks = lab['Slices N'], {}
    hdr = {}
    for r in range(1, ws.max_row + 1):
        a = col(r, 1)
        if isinstance(a, str) and a.startswith('Sample size'):
            L = col(r, 2)
            if not hdr:
                hdr = {str(col(r + 1, c)).strip(): c for c in range(1, ws.max_column + 1) if col(r + 1, c) is not None}
            rows = range(r + 2, r + 2 + N)
            g = lambda name: [col(i, hdr[name]) for i in rows]
            blocks[L] = {'A': g(next(h for h in hdr if h.startswith('Reading Clockwise'))),
                         'G': g('Counter Clockwise'), 'M': g('Not')}
    return lab, N, blocks, hdr

def nib_cols(ws, hdr):                                            # the two 'Hex nib' columns (clockwise, counter-clockwise)
    r = next(r for r in range(1, ws.max_row + 1) if isinstance(ws.cell(r, 1).value, str) and ws.cell(r, 1).value.startswith('Reading Clockwise'))
    return [c for c in range(1, ws.max_column + 1) if ws.cell(r, c).value == 'Hex nib']

wbA = openpyxl.load_workbook(sys.argv[1], data_only=True); wsA = wbA['2-bit circle']
wbB = openpyxl.load_workbook(sys.argv[2], data_only=True)
lab, N, B, hdr = read_sheet(wsA)
s, drawn = lab['Cycle sampled'], lab['Circle as drawn']
T, G, M = B[8]['A'], B[8]['G'], B[8]['M']
n = N
print(f"ring 2 file: drawn {drawn}  reading {lab['Reading']}  sheet cycle s = {s}  N = {N}  offset = {lab['Counter-clockwise start offset']}")
print('L = 8 table (A81:A88):', ' '.join(T))
res = {}

# ---- Q1 ------------------------------------------------------------------------------------------------------
cols = [''.join(T[i][j] for i in range(n)) for j in range(n)]
res['Q1'] = check('Q1', T == [rot(s, k) for k in range(n)] and cols == T
                  and all(wt(r) == 4 for r in T) and all(wt(c) == 4 for c in cols)
                  and all(G[k] == rev(T[-k % n]) == T[(k + 3) % n] for k in range(n)),
                  'rotation table; down = across; four 1s per row/col; G_k = rev(A_-k) = A_k+3')
H = lambda w: rev(w[:len(w) // 2]) + rev(w[len(w) // 2:])
print('    (unsealed, Dean\'s observation) reverse-each-half: row k -> row', [T.index(H(T[k])) for k in range(n)],
      '; whole reverse: row k -> row', [T.index(rev(T[k])) for k in range(n)])

# ---- Q2 ------------------------------------------------------------------------------------------------------
res['Q2'] = check('Q2', all(wt(xor(T[k], cols[k])) == 0 for k in range(n)) and all(xor(T[k], M[k]) == '1' * n for k in range(n)),
                  'rows vs columns: 0 differ; row vs Not: all 8 differ')

# ---- Q3 ------------------------------------------------------------------------------------------------------
m3 = [xor(T[k], G[k]) for k in range(n)]
print('    A xor G:', ' '.join(m3))
res['Q3'] = check('Q3', all(one_block(m) and wt(m) == 4 for m in m3) and all(m3[k] == rot(m3[0], k) for k in range(n)),
                  'one contiguous half per row, moving one slice per row')

# ---- Q4 ------------------------------------------------------------------------------------------------------
md = {d: xor(s, rot(s, d)) for d in range(n)}
same_mask = all(xor(T[k], T[(k + d) % n]) == rot(md[d], k) for d in range(n) for k in range(n))
words = [s[i:i + 2] for i in range(0, n, 2)]
carry = all(md[2 * t] == ''.join(format(w ^ ((w + t) % 4), '02b') for w in range(4)) for t in range(4))
print('    masks s xor rot(s,d):', '  '.join(f'd={d}:{md[d]}={hx(md[d])}(w{wt(md[d])})' for d in range(n)))
print('    2-bit words of s:', words, '; even d = 2t is "+t on every count":', carry)
exp = {0: '00', 1: '2D', 7: '96', 2: '77', 6: 'DD', 4: 'AA', 3: 'C3', 5: '78'}
res['Q4'] = check('Q4', same_mask and carry and words == ['00', '01', '10', '11']
                  and all(hx(md[d]) == exp[d] for d in range(n)) and comp('01101001') == md[7]
                  and {d for d in range(n) if wt(md[d]) > 4} == {2, 6},
                  'rows d apart = one mask rotated; 0x96 = complement of 0x69; only d = 2, 6 exceed four')

# ---- Q5 ------------------------------------------------------------------------------------------------------
X = lambda f: [[f(i, j) for j in range(n)] for i in range(n)]
Tm = X(lambda i, j: T[i][j])
sym = {'identity': lambda i, j: Tm[i][j], 'transpose': lambda i, j: Tm[j][i],
       'quarter turn cw': lambda i, j: Tm[n - 1 - j][i], 'half turn': lambda i, j: Tm[n - 1 - i][n - 1 - j],
       'quarter turn ccw': lambda i, j: Tm[j][n - 1 - i], 'mirror left-right': lambda i, j: Tm[i][n - 1 - j],
       'mirror top-bottom': lambda i, j: Tm[n - 1 - i][j], 'anti-transpose': lambda i, j: Tm[n - 1 - j][n - 1 - i]}
q5 = True
for name, f in sym.items():
    D = X(lambda i, j: Tm[i][j] != f(i, j)); cnt = sum(map(sum, D)); per = [sum(r) for r in D]
    cb = all(D[i][j] == ((i + j) % 2 == 0) for i in range(n) for j in range(n))
    print(f'    {name:18s} differ {cnt:2d}/64  per row {per}  checkerboard {cb}  | with complement {64 - cnt}')
    want = {'identity': 0, 'transpose': 0}.get(name, 32)
    q5 &= cnt == want and (name not in ('half turn', 'anti-transpose') or cb) and (want == 0 or per == [4] * n)
res['Q5'] = check('Q5', q5, 'transpose 0; half turn / anti-transpose: checkerboard; turns and mirrors: 4 per row')

# ---- Q6 ------------------------------------------------------------------------------------------------------
dg = [''.join(T[i][(i + c) % n] for i in range(n)) for c in range(n)]
ad = [''.join(T[i][(c - i) % n] for i in range(n)) for c in range(n)]
print('    diagonals  :', ' '.join(f'{d}={hx(d)}' for d in dg))
print('    anti-diags :', ' '.join(ad), '-> first bits spell', ''.join(a[0] for a in ad))
res['Q6'] = check('Q6', [hx(d) for d in dg] == ['33', '55', '66', 'AA', 'CC', '55', '99', 'AA']
                  and all(len(set(a)) == 1 for a in ad) and ''.join(a[0] for a in ad) == s,
                  'down-right: 0x33 family (even), 0x55/0xAA (odd); down-left: constant, spelling s')

# ---- Q7 ------------------------------------------------------------------------------------------------------
print(f"    s {s}: 0-runs {runs(s, '0')} 1-runs {runs(s, '1')} | drawn {drawn}: 0-runs {runs(drawn, '0')} 1-runs {runs(drawn, '1')}")
res['Q7'] = check('Q7', all(wt(r) == 4 for r in T) and runs(s, '0') == [1, 3] and runs(s, '1') == [2, 2]
                  and runs(drawn, '0') == [2, 2] and runs(drawn, '1') == [1, 3], 'equal counts, unequal runs')

# ---- Q8 ------------------------------------------------------------------------------------------------------
q8 = True; ncA, ncK = nib_cols(wsA, hdr)
for L in sorted(B):
    A_ = B[L]['A']; distinct = len(set(A_))
    pairs = [A_[k] + A_[(k + 1) % n] for k in range(0, n, 2)]
    closed = {rev(p) for p in pairs} == set(pairs)
    r0 = next(r for r in range(1, wsA.max_row + 1) if wsA.cell(r, 1).value and str(wsA.cell(r, 1).value).startswith('Sample size') and wsA.cell(r, 2).value == L) + 2
    fileE = [wsA.cell(r0 + k, ncA).value for k in range(0, n, 2)]
    fileK = [wsA.cell(r0 + k, ncK).value for k in range(1, n, 2)]
    mine = [format(int(A_[k], 2), 'X') + format(int(A_[k + 1], 2), 'X') for k in range(0, n, 2)]
    print(f'    L={L}: distinct windows {distinct}/8  nib pairs {pairs}  reversal-closed {closed}  file E {fileE} K {fileK}  E=hex(A_k)&hex(A_k+1) {fileE == mine}')
    q8 &= (distinct == 8) == (L >= 5) and closed == (L % 2 == 0) and fileE == mine and set(fileK) == set(fileE)
res['Q8'] = check('Q8', q8, 'distinct from L = 5; nib pairs reversal-closed exactly at even L')

# ---- Q9: rings 3 and 4 ---------------------------------------------------------------------------------------
print('\nrings from the nested workbook (L = N):')
q9 = True
for name, k in (('Ring 2', 2), ('Ring 3', 3), ('Ring 4', 4)):
    labk, Nk, Bk, _ = read_sheet(wbB[name])
    sk, dk, off = labk['Cycle sampled'], labk['Circle as drawn'], labk['Counter-clockwise start offset']
    Tk = [rot(sk, d) for d in range(Nk)]
    rows_cols = all(''.join(Tk[i][j] for i in range(Nk)) == Tk[j] for j in range(Nk))
    filetab = Bk.get(Nk, {}).get('A')
    mask = xor(sk, rot(sk, off))
    print(f'  {name}: drawn = walk({k}) {dk == rm.walk(k)}; sheet = comp(rev(drawn)) {sk == comp(rev(dk))}; N {Nk}; offset {off}; '
          f'rows = cols {rows_cols}; 1s per row {wt(sk)}/{Nk}; file L=N block present {filetab is not None}'
          f'{" and equal" if filetab == Tk else ""}; reversal-closed {rclosed(sk)}; '
          f'A xor G mask weight {wt(mask)}, 1-runs {runs(mask, "1")}, one block {one_block(mask)}')
    if k > 2:
        q9 &= rows_cols and wt(sk) == Nk // 2 and not rclosed(sk) and not one_block(mask)
res['Q9'] = check('Q9', q9, 'rings 3, 4: rows = cols, half 1s, NOT reversal-closed, A xor G not one half')

# ---- Q10: nested Ring 2 against the original -----------------------------------------------------------------
_, _, B2, _ = read_sheet(wbB['Ring 2'])
res['Q10'] = check('Q10', all(B2[L][c] == B[L][c] for L in B for c in 'AGM') and set(B2) == set(B),
                   'clockwise, counter-clockwise and Not words match at L = 2..8')
wsN = wbB['Ring 2']; diff = Counter(); eq = 0
for r in range(1, max(wsA.max_row, wsN.max_row) + 1):
    for c in range(1, max(wsA.max_column, wsN.max_column) + 1):
        a, b = wsA.cell(r, c).value, wsN.cell(r, c).value
        if a == b: eq += a is not None
        else: diff[openpyxl.utils.get_column_letter(c)] += 1
print(f'    (unsealed) cell for cell: {eq} equal non-empty cells; differing cells by column {dict(sorted(diff.items()))}')

print('\nsealed:', ' '.join(f'{q} {"PASS" if v else "FAIL"}' for q, v in res.items()))
```

## `explore211.py` (sha `25accdd40e25b5fd4d495512ee240527c1f3110321c361186148385cfd2bb1bb`)

```python
"""§ 211, unsealed follow-up: which ring-2 facts survive at higher rings? Sheet reading s_n = comp(rev(walk(n))), table at L = N."""
import sys
sys.path.insert(0, '/home/claude/w203/src')
import ring_machine as rm

def rot(s, d): d %= len(s); return s[d:] + s[:d]
def rev(s): return s[::-1]
def comp(s): return s.translate(str.maketrans('01', '10'))
def xor(a, b): return ''.join('1' if x != y else '0' for x, y in zip(a, b))
def wt(s): return s.count('1')
def rclosed(s): return rev(s) in {rot(s, d) for d in range(len(s))}
def runs(s, ch):
    if ch not in s: return []
    k = next(i for i in range(len(s)) if s[i] != ch); t = s[k:] + s[:k]
    return sorted((len(r) for r in t.replace('1' if ch == '0' else '0', ' ').split()), reverse=True)

print('reversal-closed sheet circle, n = 1..12:', {n: rclosed(comp(rev(rm.walk(n)))) for n in range(1, 13)})
for n in (2, 3, 4, 5):
    s = comp(rev(rm.walk(n))); N = len(s); T = [rot(s, k) for k in range(N)]
    H = lambda w: rev(w[:N // 2]) + rev(w[N // 2:])
    half = sum(T[i][j] != T[N - 1 - i][N - 1 - j] for i in range(N) for j in range(N))
    quarter = sum(T[i][j] != T[N - 1 - j][i] for i in range(N) for j in range(N))
    mw = {d: wt(xor(s, rot(s, d))) for d in range(1, N)}
    big = [d for d in mw if mw[d] > N // 2]
    Lu = next(L for L in range(1, N + 1) if len({(s + s)[k:k + L] for k in range(N)}) == N)
    print(f'n={n} N={N}: first/last rows split-reverse {H(T[0]) == T[-1]}; half turn differs {half}/{N * N}; quarter turn {quarter}/{N * N}; '
          f'rows d apart: max differ {max(mw.values())}/{N}, more than half at d = {big}; windows all distinct from L = {Lu}; '
          f'0-runs {runs(s, "0")} 1-runs {runs(s, "1")}')
```

## `pal211.py` (sha `ae8eb3cbb0896928d7aa9743b0e97f3ca837db73d58ca58c2833b363da99fa50`)

```python
"""§ 211 Q11: clockwise xor its mirror (slice p against slice N-1-p) = the palindrome slices, every ring."""
import sys
sys.path.insert(0, '/home/claude/w203/src')
import ring_machine as rm

def comp(s): return s.translate(str.maketrans('01', '10'))
def runs1(m):
    if '0' not in m: return 1
    k = m.index('0'); t = m[k:] + m[:k]
    return len(t.replace('0', ' ').split())
ok = True
for n in range(1, 11):
    d = rm.walk(n); N = len(d)
    mask = ''.join('1' if d[p] != d[N - 1 - p] else '0' for p in range(N))
    sheet = comp(d[::-1]); mask_s = ''.join('1' if sheet[p] != sheet[N - 1 - p] else '0' for p in range(N))
    pals = ''.join(('1' if rm.pal(x, n) else '0') * n for x in rm.ring(n))
    share = mask.count('1') / N; want = 2.0 ** -(n // 2)
    good = mask == pals == mask_s and mask.count('1') == n * 2 ** ((n + 1) // 2) and share == want
    ok &= good and ((runs1(mask) == 1) == (n == 2) or n == 1)
    print(f'n={n:2d} N={N:5d}: mask = palindrome slices {mask == pals}; sheet gives the same mask {mask_s == mask}; '
          f'differ {mask.count("1")}/{N} = {share} (2^-floor(n/2) = {want}); separate pieces {runs1(mask)}'
          + (f'; mask {mask}' if N <= 24 else ''))
print('Q11:', 'PASS' if ok else 'FAIL')
```

## `dump211.py` (sha `13485db3fb197e27681c01cbf2f4da58d4341faa98c1ba610ec8a81e61129f77`)

```python
"""Dump every sheet of an .xlsx: formula, cached value and fill colour of each non-empty cell.
Usage: python3 -I dump211.py <path.xlsx>"""
import sys
import openpyxl

path = sys.argv[1]
wf = openpyxl.load_workbook(path, data_only=False)
wv = openpyxl.load_workbook(path, data_only=True)
for name in wf.sheetnames:
    sf, sv = wf[name], wv[name]
    print(f"=== sheet {name!r}  dims {sf.dimensions}  max_row {sf.max_row}  max_col {sf.max_column}")
    for row in sf.iter_rows():
        out = []
        for c in row:
            f = c.value
            if f is None:
                continue
            v = sv[c.coordinate].value
            fill = c.fill.fgColor.rgb if c.fill and c.fill.fill_type else None
            tag = c.coordinate
            if isinstance(f, str) and f.startswith('='):
                tag += f"={v!r} <{f}>"
            else:
                tag += f"={v!r}"
            if fill and fill not in ('00000000',):
                tag += f" [{fill}]"
            out.append(tag)
        if out:
            print(' | '.join(out))
```

## `seal211/predictions.txt` (sha `bc246c5905e78020f3bcc320688cf4bffe11a76c46772e7db9e81c5f91bc5a55`)

```text
§ 211 predictions, sealed before the run. "Not the same" = XOR: the cells where two readings differ.
Table T = two_bit_circle.xlsx, sheet '2-bit circle', column A rows 81-88 (L = 8); s = B9 = 00011011; rows k = 0..7.

Q1 File. A_k is the rotation table of s: reading down column j gives row j exactly; every row and column has four 1s.
   Column G (L = 8) is the true counter-clockwise read: G_k = reverse(A_{-k}) = A_{k+3}.
Q2 Rows vs columns differ nowhere. Each row vs its Not (column M) differs everywhere.
Q3 Clockwise vs counter-clockwise: A_k xor G_k is, for every k, one contiguous run of four 1s (a rotation of 00001111).
   The two directions agree on one half of the circle and disagree on the other half; that half moves one slice per row.
Q4 Rows d apart differ by one mask, rotated to the start:
   d = 1, 7: the parity word (0x2D, 0x96 = complement of the § 204 adder sum 0x69);
   d = 2: 0x77 = 01 11 01 11 (the +1 carry mask on each 2-bit count); d = 6: 0xDD (-1);
   d = 4: 0xAA = 10 10 10 10 (+2, the high bit of each count); d = 3, 5: a contiguous half (0xC3, 0x78).
   Only d = 2 and 6 differ in more than four slices (six).
Q5 T against its 8 square symmetries: transpose 0 cells differ; 180-degree turn and anti-transpose 32 cells,
   a checkerboard (cells with i + j even); both quarter turns and both mirror flips 32 cells, four in every row.
   With complement: 64, 32, 32. No turn of the grid changes more than half except the complement.
Q6 Lines through T that are not the circle: down-right diagonals read 0x33, 0x66, 0xCC, 0x99 at even offsets and
   0x55 / 0xAA at odd offsets; down-left anti-diagonals are constant and, in order, spell 00011011.
Q7 0 vs 1: four of each in every row; the 0s run 3 + 1 and the 1s run 2 + 2 (cyclic).
   In the drawn circle 00100111 the 0s run 2 + 2 and the 1s 1 + 3.
Q8 Window size L = 2..8 on the same circle: all eight windows are distinct only from L = 5.
   The hex-nib pairs (window k with window k+1, k even) are closed under bit reversal at even L (2, 4, 6, 8)
   and not at odd L (3, 5, 7).
Q9 Rings 3 and 4 (nested_ring_beyond_2bit.xlsx), L = N: rows = columns and four-of-each balance (half 1s) hold;
   the sheet circle is NOT reversal-closed at ring 3 or ring 4 (ring 2 is), so the 'Counter Clockwise' column there
   is a forward read at an offset, and A xor G at L = N is not one contiguous half.
Q10 Nested 'Ring 2' vs two_bit_circle.xlsx: the window words (clockwise, counter-clockwise, Not) match at every sample size.
```

## `seal211b/predictions.txt` (sha `525f1bd8a40753bd64f3cecc0ecf17f1ceb60f8bbf3f8b4950afb147b0ff94e4`)

```text
§ 211 Q11, sealed after the Q1-Q10 run and before this check.
For every ring n = 1..10 (drawn circle d = walk(n), N = n * 2^n slices), read it clockwise and counter-clockwise
with the counter-clockwise read mirrored about the ring's fold (the reader at slice p meets slice N-1-p).
XOR of the two reads is 1 exactly on the slices of palindromic words and 0 on every other slice:
the J-twins read the same both ways; the C-twins (palindromes) flip completely.
It covers n * 2^ceil(n/2) of the N slices, a share of 2^-floor(n/2) (n = 1: all; n = 2, 3: half; n = 4, 5: a quarter; ...).
The same mask comes out of the sheet reading comp(rev(d)). It is one contiguous block only at n = 2 (00 and 11 meet at the seam).
In two_bit_circle.xlsx, A_0 xor G_0 = 11000011 is this mask: the slices of 00 and 11.
```

## `check223.py` (sha `fd3d7ff840e8fb635def0b062c7ed97b53565d9ea4e26ff1e86af3ed28baf7aa`)

```python
"""§ 223 independent check: the § 202 library against the pasted generator's outputs.
Naming: § 202 library read(word) -> address, save(address) -> word; the pasted § 223 names them the other way round."""
import sys, hashlib
sys.path.insert(0, '/home/claude/w203/src')
import ring_machine as rm
print('walk(2) =', rm.walk(2), '; walk_hex(4) =', rm.walk_hex(4))
for n in range(2, 13):
    R = rm.ring(n)
    assert all(rm.save(a, n) == R[a] and rm.read(R[a], n) == a for a in range(len(R)))
print('library: save(a) = ring[a] and read(ring[a]) = a for n = 2..12, every address')
sig = b''.join(rm.save(a, 16).to_bytes(2, 'big') for a in range(1 << 16))
print('library R16 regenerated address by address: bytes', len(sig), 'sha256', hashlib.sha256(sig).hexdigest())
print('equals pasted file:', sig == open(sys.argv[1], 'rb').read())
word, addr = 0x243f6a8885a308d3, 2427008858123944441
print('library save(addr, 64) =', hex(rm.save(addr, 64)), '; read(word, 64) =', rm.read(word, 64))
print('round trip:', rm.save(addr, 64) == word and rm.read(word, 64) == addr)
```

## `section223_address_generator.py` (pasted, run unchanged; sha `f040dc85aa3690b45f3df526ccad035241fc1df65d7557d5c9674e560178adad`)

```python
#!/usr/bin/env python3
"""NEXUS §223: regenerate the complete R_n signature by address, without a ring table.

The reader's only data-dependent selection is a count of addresses whose word prefix
belongs to the canonical partner representative set. It does not enumerate candidates.
The conventional ring builder below is imported nowhere and called ONLY after sealing
and executing the generator, as an independent regression oracle.
"""
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from time import perf_counter

SEAL = '33c2bb8283516406e5e9f5b53e8511e98a7854b762d8e59d16697af95211ef72'
sealfile=Path(__file__).with_name('seal223_predictions.txt')
if sealfile.exists():
    assert sha256(sealfile.read_bytes()).hexdigest()==SEAL

def J(x,n):
    r=0
    for _ in range(n):
        r=(r<<1)|(x&1); x >>= 1
    return r

def C(x,n): return x ^ ((1<<n)-1)
def P(x,n): return C(x,n) if J(x,n)==x else J(x,n)
def is_rep(x,n): return x<P(x,n)

@lru_cache(maxsize=None)
def prefix_reps(n, bits, length):
    """Number of representatives beginning with `length` bits `bits`.
    Count outer symmetric pairs by DP, not by trying full words.
    Comparison with reversal is determined by first asymmetric mirror pair.
    The equal-to-reversal branch belongs to reps iff the leading bit is 0.
    """
    assert 1 <= n <= 64 and 0 <= length <= n and 0 <= bits < (1<<length)
    def allowed(i):
        if i < length:
            return ((bits >> (length-1-i)) & 1,)
        return (0,1)
    # (comparison to own reversal: 0 equal so far / 1 smaller, most-significant bit)
    states={(0,-1):1}
    for i in range(n//2):
        nxt={}
        for (less,msb),ways in states.items():
            for left in allowed(i):
                for right in allowed(n-1-i):
                    if not less and left>right: continue
                    cless=less or (left<right)
                    first=left if i==0 else msb
                    key=(int(cless),first)
                    nxt[key]=nxt.get(key,0)+ways
        states=nxt
    if n%2:
        mid=n//2; nxt={}
        for (less,msb),ways in states.items():
            for b in allowed(mid):
                nxt[(less, b if msb<0 else msb)]=nxt.get((less,b if msb<0 else msb),0)+ways
        states=nxt
    return sum(ways for (less,first),ways in states.items() if less or first==0)

def representative(rank, n):
    """Unrank directly via branch counts, not candidate search."""
    h=1<<(n-1)
    if not 0<=rank<h: raise ValueError('rank outside near half')
    prefix=0
    for length in range(n):
        n0=prefix_reps(n,prefix<<1,length+1)
        if rank>=n0:
            rank-=n0
            prefix=(prefix<<1)|1
        else:
            prefix<<=1
    assert rank==0 and is_rep(prefix,n)
    return prefix

def representative_rank(x,n):
    if not is_rep(x,n): raise ValueError('not representative')
    rank=0
    prefix=0
    for length in range(n):
        bit=(x>>(n-length-1))&1
        if bit: rank+=prefix_reps(n,prefix<<1,length+1)
        prefix=(prefix<<1)|bit
    return rank

def read(n,address,record=True):
    """One G(n,address,crease) reads one word; no ring buffer, builder or sort."""
    N=1<<n;h=N>>1
    if not 0<=address<N: raise ValueError('address outside circle')
    if record and n>=2 and address==h-1: return P(representative(h-1,n),n)
    if record and n>=2 and address==h: return representative(h-1,n)
    if address<h: return representative(address,n)
    return P(representative(N-1-address,n),n)

def save(n,word,record=True):
    """Exact inverse: derive address from a word by rank of its representative."""
    N=1<<n;h=N>>1
    if not 0<=word<N: raise ValueError('word outside width')
    rep=word if is_rep(word,n) else P(word,n)
    r=representative_rank(rep,n)
    if r==h-1 and record and n>=2:
        return h if word==rep else h-1
    return r if word==rep else N-1-r

def crossings(word,n):
    """Base-2 lane, 2r=dq+r', d=2^n, emits the n bits."""
    d=1<<n; r=word;out=[];remain=[word]
    for _ in range(n):
        q,r=divmod(2*r,d)
        out.append(q);remain.append(r)
    return out,remain

def unwrite(bits):
    x=0
    for q in bits: x=2*x+q
    return x

# Only independent comparison oracle, deliberately segregated from read/save.
def regression_ring(n,record=True):
    reps=[x for x in range(1<<n) if is_rep(x,n)]
    h=len(reps)
    if record and n>=2:
        return reps[:-1]+[P(reps[-1],n),reps[-1]]+[P(x,n) for x in reversed(reps[:-1])]
    return reps+[P(x,n) for x in reversed(reps)]

print('§223: ADDRESS + UNIVERSAL READER = REGENERATED SIGNATURE')
print('PREDICTION SEAL:',SEAL)
print('STATUS: route on known underlying ring; no blind/novel-data landing')
print('Count of representatives at each n is 2^(n-1):',all(prefix_reps(n,0,0)==(1<<(n-1)) for n in range(1,17)))

for n in range(1,13):
    N=1<<n
    t=perf_counter()
    for record in (False,True):
        words=[read(n,a,record) for a in range(N)]
        assert set(words)==set(range(N))
        assert words==regression_ring(n,record)
        assert all(save(n,words[a],record)==a for a in range(N))
        assert all(words[N-1-a]==P(words[a],n) for a in range(N))
        assert all(unwrite(crossings(words[a],n)[0])==words[a] for a in range(N))
        assert all(crossings(words[a],n)[1][-1]==0 for a in range(N))
    print(f'R{n:02d} : {N:5d} slots x 2 crease contracts; no stored ring in read/save; read→save, lane, facing, oracle ALL RUN; elapsed {perf_counter()-t:.3f}s')

# Explicit full 65536-slot walk / 131072-byte signature from random-access reads.
n=16;N=1<<n;t=perf_counter();seen=bytearray(N//8)
walk_sha=sha256();words=[]
produced_path=Path(__file__).with_name('R16_signature_regenerated.bin')
output_file=produced_path.open('wb')
for a in range(N):
    x=read(n,a,True)
    assert 0<=x<N
    assert save(n,x,True)==a
    mask=1<<(x&7);ix=x>>3
    assert not (seen[ix]&mask)
    seen[ix]|=mask
    if a<16 or a>=N-16: words.append((a,x))
    bx=x.to_bytes(2,'big')
    walk_sha.update(bx)
    output_file.write(bx)
output_file.close()
assert sha256(produced_path.read_bytes()).hexdigest()==walk_sha.hexdigest()
assert all(c==255 for c in seen)
# Regression builder invoked only AFTER random-access machine generated the full signature.
assert all(read(n,a,True)==v for a,v in enumerate(regression_ring(n,True)))
assert all(read(n,N-1-a,True)==P(read(n,a,True),n) for a in range(N//2))
assert read(n,N//2-1,True)==P(read(n,N//2,True),n)
print('\nONE THING: complete R16 binary signature, record crease')
print('signature length:', N*n, 'bits =', N*2,'bytes')
print('regenerated with n=16 + shared G(n,a,c) + 16-bit address for any word')
print('SHA-256 of complete regenerated signature:',walk_sha.hexdigest())
print('16 first and 16 last addresses:',[(a,f'{x:04x}') for a,x in words])
print('every address unrank→rank, every n-bit word once, no stored lookup:',True)
print('full written binary file:',produced_path.name)
print('independent conventional ring comparison AFTER execution:',True)
print('facing law on all 32768 address pairs:',True)
print('full walk execution elapsed',f'{perf_counter()-t:.3f}s')

# A single 64-bit object, known from §202, recovered through address + reader alone.
known_word=0x243f6a8885a308d3
known_address=2427008858123944441
address_from_word=save(64,known_word,True)
back_from_address=read(64,known_address,True)
print('\nONE PREVIOUSLY RECORDED 64-BIT WORD (provenance regression)')
print('recorded word:',f'0x{known_word:016x}')
print('recorded address:',known_address,'bit length',known_address.bit_length())
print('computed save(word):',address_from_word)
print('read(address) without storing the word:',f'0x{back_from_address:016x}')
print('known address agrees:',address_from_word==known_address)
print('known word recovered:',back_from_address==known_word)
if address_from_word != known_address or back_from_address != known_word:
    print('WARNING: old source §202 64-bit example is not this crease-orientation convention; preserve discrepancy')

print('\nLOWER BOUND IN STATED MODEL')
print('For fixed n,c, G visits 2^n distinct words; any fixed-length address needs ≥ n bits. This G uses n bits.')
print('Shared generator code cost excluded from that address bound; no universal shortest-program claim.')
```

## `seal223_predictions.txt` (pasted; sha `33c2bb8283516406e5e9f5b53e8511e98a7854b762d8e59d16697af95211ef72`)

```text
§223 — PREDICTION SEAL BEFORE RUN
Date: 2026-10-31
Source: existing NEXUS lane/head/ring record §§202-208; prior published reference outputs already known.
This is a route regression, not a blind landing on novel data.
P1. For every tested n, the fixed address reader G(n,a,c) returns each n-bit word exactly once, with no stored ring, list, sort or scanning candidate words.
P2. For fixed n and crease c, the exact inverse recovers address a from G(n,a,c).
P3. Word at address a, when emitted as base-2 lane crossings, reconstructs the word and recovers the seed by weighted crossings.
P4. At n=2 record, concatenating G(2,a,1) for all a yields binary 00100111 (0x27); at n=4 record yields hex 0123567dbe9ac48f.
P5. At n=16 record, concatenating words yields 131072 bytes; independent conventional builder agrees; every address round-trips and facing holds.
P6. Under a shared fixed lossless generator covering all 2^n possible n-bit values, addresses require at least n bits and the ring uses exactly n. Not a claim of shortest total program or Kolmogorov complexity.
P7. For prior source 64-bit signature 0x243f6a8885a308d3, the generator may reconstruct from the previously recorded ring address without storing the signature; this is a provenance regression, not unseen-data prediction.
```
