# NEXUS running audit — continuation

## Entry C1 · 5 Nov 2026 · catch-up audit of P22–P28 against the Routes addendum (P14–P18) and *The Way Between* Prop. 2.6

**Provenance.** Inputs: *The Center Is the Answer and the Start of Continuation* (P22–P28, docx sha256 `0355153a6310e944…`, identical to the copy inside the bundle); `NEXUS_P22_P28_Reader_Research_Bundle.zip` (both uploads are one file, sha256 `86c9996bc8187cc6…`); `NEXUS_Routes_Addendum_scripts.zip` (`75de4d6247ab2eed…`); the Claude transcript of 25 Oct–5 Nov and the ChatGPT transcript of 5 Nov (P19–P21). *The Way Between* read from the project collection. `catchup_audit.py` re-implements the native ring from the manual's definition (eqs. 2–4, the same construction as `ringops.native_ring`) instead of importing the shipped module.

**Re-execution of the record (no edits).**

| Record | Result |
|---|---|
| P22–P28 sealed audits | all 7 exit 0; each seal hash verified by its own script; live stdout byte-identical to the shipped run logs |
| Routes addendum scripts | `verify_routes`, `addendum_checks`, `direction17`, `programs15`, `programs16`, `successor_center`, `center_motion`, `catalog4`, `addendum_tables`, `fig_fixed`: all exit 0, every assertion holds; the failures-as-sealed (P14.6; the LEN-1 clauses of P17.1 and P17.3) print as recorded |

**Seal.** `catchup_seal.txt`, sha256 `00028084572a1327151024fcceea6c3ea200ba1f94330b2829c19eba339274eb`, hashed 2026-11-05T21:58:05Z before the first run.

```text
NEXUS catch-up audit of P22-P28 against the Routes addendum (P14-P18) and The Way Between Prop. 2.6
Sealed 2026-11-05 before running catchup_audit.py. Native operators only: J reverse, C NOT, s palindrome
selector, P facing, tau twisted clock, R_n native ring (ringops.native_ring). chi = (-1)^s.

S1  P24 from its definition, not from the overlap count. For odd n = 1..17 and every lag t = 0..2n-1,
    sum_x chi(x) chi(tau^t x) = 2^n - 4 (2^ceil(n/2) - 2^ceil(g/2)), g = gcd(n, t), by direct summation over
    all 2^n words. The length-n DFT of A_n(t) equals the Ramanujan form and is >= 0 at every j.

S2  P22.4 executed and sharpened. For m = 1..5 the space {L : L tau_m = tau_(m+1) L}, split into charge
    blocks (C_m = a) -> (C_(m+1) = b), has dimension
      (-,-) = 0                                   [P22.4]
      (+,+) = O_m * O_(m+1)                       [lambda = +1]
      ((-1)^m, (-1)^(m+1)) = O_m * O_(m+1)        [lambda = -1; it always flips the charge]
      the remaining cross block = 0
    with O_m the number of tau_m orbits: O_1..O_6 = 1, 1, 2, 2, 4, 6. Only lambda = +-1 crosses LEN statically.

S3  Phase sectors by LEN (scope of P28's "at p = 2 these are +-i"). For n = 1..12, every eigenvalue of tau_n
    in the C_n = sigma sector satisfies lambda^n = sigma, and
      +-i occur iff n is even; at n = 2 mod 4 only in sigma = -1, at n = 0 mod 4 only in sigma = +1;
      lambda = -1 lies in sigma = -1 iff n is odd; at even n the sigma = -1 sector has no real eigenvalue.
    So on the odd-LEN orbits P27-P28 classify (p odd), +-i never occur; the +-i class lives at the even parent.

S4  Where the P22-P28 OPEN stands once the addendum's address laws are composed with P27. Odd n = 3..17:
    (a) on every active tau_n orbit the two palindromic teeth sit on opposite sides of the R_n seam
        (address < 2^(n-1) and >= 2^(n-1)); the lower one starts with bit 0;
    (b) at every tooth x of an orbit with half-period p, P_n(x) = tau_n^p(x): facing is the half-lap;
    (c) every silent orbit O is chiral (J(O) and O disjoint), P_n maps O onto J(O), and
        P tau P = tau^-1 holds on O; every active orbit is achiral;
    (d) the set where P tau P != tau^-1 equals the negative sector of P21's commutator
        K_n = tau D tau^-1 D, size 2^(ceil(n/2)+1) - 4.
    (e) for every s = 1..12 the map O -> necklace class of (u | C u), u in O, is a bijection from tau_s orbits
        onto the length-2s necklaces of words w with rot_s(w) = C w; the necklace is fixed by cyclic facing
        iff O contains a palindrome (is reader-active). The unmarked circular route is the clock orbit.

No data, no fitting. A failed clause is recorded as failed, not edited.
```

**Status.**

| Item | Status | Content |
|---|---|---|
| S1 | RUNS (odd n ≤ 17, every lag, every word) | ∑ₓ χ(x)χ(τᵗx) = 2ⁿ − 4(2^⌈n/2⌉ − 2^⌈g/2⌉) by direct summation; Ramanujan DFT residual ≤ 2.3e−14; spectrum ≥ 0. P24 unchanged. |
| S2 | STANDS; RUNS m = 1–5 | Common eigenvalues of τₘ and τₘ₊₁ satisfy λ²ᵐ = λ²⁽ᵐ⁺¹⁾ = 1, so λ² = 1. Static intertwiners live only on λ = ±1: (+,+) = OₘOₘ₊₁, the λ = −1 block = OₘOₘ₊₁ and always flips the NOT charge ((−1)ᵐ → (−1)ᵐ⁺¹), (−,−) = 0. Any non-real phase crosses LEN only through the moving seam (P22.2–P22.5). |
| S3 | STANDS; RUNS n = 1–12 | Per orbit of length 2p the spectrum is all 2p-th roots (Way Between 2.6) with sector λᵖ = σ. p carries the 2-adic valuation of n, so ±i occur iff n is even, in C = (−1)^(n/2): C = −1 at n ≡ 2 (mod 4), C = +1 at n ≡ 0 (mod 4). At odd n the C = −1 sector always holds the real phase −1 (once per orbit); at even n it has no real eigenvalue. |
| S4(a) | STANDS (P17.1 ∘ P27); RUNS odd n = 3–17 | On every reader-active orbit the two teeth x, Cx sit on opposite sides of the Rₙ seam; the lower one begins with 0. The ring's top address bit picks the comb's t = 0 tooth with no external start. |
| S4(b) | STANDS; RUNS | At a tooth, Pₙ(x) = Cx = τₙᵖ(x): facing is the half-lap. |
| S4(c) | STANDS; RUNS | At odd n an achiral orbit always holds a tooth: along the orbit Jy = τᵈy with d shifting by 2 per step, and an odd d could be shifted to p, giving Jy = Cy, impossible with a centre bit; so d reaches 0. Silent ⇔ chiral. On a silent orbit P = J, P carries O onto J(O), and PτP = τ⁻¹ holds exactly. Silent orbits: 2, 14, 62, 252, 968, 3600 at n = 7–17; silent share of states 49% (n = 9), 80% (n = 13), 93.4% (n = 17). |
| S4(d) | STANDS; RUNS | {x : PτP(x) ≠ τ⁻¹(x)} = negative sector of P21's Kₙ = τDτ⁻¹D = (S ∪ τS) minus the alternating pair; size 2^(⌈n/2⌉+1) − 4 (4, 12, …, 1020). Facing reverses the clock exactly where clock and centre reader commute. |
| S4(e) | STANDS (odd s), RUNS s = 1–12 | Rotating u‖Cu by one is τₛ on the half-word, so O ↦ necklace(u‖Cu) is a bijection from τₛ-orbits onto the necklaces with rotₛ(w) = Cw; the necklace is fixed by cyclic facing iff the orbit is reader-active. The addendum's fixed circular routes (A3) are P27's active orbits read without a start. |

**Corrections to the P22–P28 note (logged, not applied to the published text).**

- **K1 · scope (§8).** "At p = 2 these are ±i, the same clock response class derived earlier in A14": on the odd-LEN orbits the note classifies, p | n with n/p odd, so p is odd and ±i never occur. ±i live at the even parent (A14 at LEN 2 is correct) and reach odd LEN only through the P22 lift μᵐ⁺¹ = σλᵐ. Their NOT sector is not fixed across even LEN (S3).
- **K2 · ownership (§1, §8).** The per-orbit eigenphase decomposition is *The Way Between* Prop. 2.6 (23 Oct: U_τ = X_last·R, U_τⁿ = X^⊗n, one full set of L-th roots per orbit; τ is the Z₂-twisted translation). It belongs in the source table. P28's own content is the comb's even-harmonic support and the reader's blindness to the odd channel.
- **K3 · audit coverage (P24).** The audit derives Mₙ(t) and Aₙ(t) from the observed overlap through M = 2(p − a), never from the χχ sum. Recomputed directly (S1): every number unchanged.
- **K4 · audit coverage (P22.4).** Printed as STANDS, not executed. Executed and sharpened (S2).
- **K5 · cosmetic.** The evidence table prints the P27 and P28 digests at 15 hex digits, the others at 16.

**OPEN, narrowed.** The note's OPEN (bind an unmarked closed route's clock phase to the ring's addressing without an external start) is closed on reader-active orbits by S4(a)–(b) and (e). What remains is the chiral orbits: no tooth, PτP = τ⁻¹ exactly, facing only pairs each with its mirror twin, and they carry 93.4% of the states at LEN 17. On them the rotations act freely and every reflection lands on the twin, so J, C, τ and P single out no position; the Rₙ address order is the only native handle left, and P15.5 says it follows the clock only on the principal cycle. The next address is the inner reader the P26 gate exposes, sₙ(u‖w‖v) = [u = v]·sₙ₋₂(w).

### Live output

```text
seal 00028084572a1327151024fcceea6c3ea200ba1f94330b2829c19eba339274eb

S1  A_n(t) by direct summation over all words (no overlap count used)
  n= 1: N*A(t), t=0..1: [2, 2]  DFT residual 0.0e+00  min DFT 1.000e+00
  n= 3: N*A(t), t=0..5: [8, 0, 0, 8, 0, 0]  DFT residual 0.0e+00  min DFT 1.000e+00
  n= 5: N*A(t), t=0..9: [32, 8, 8, 8, 8, 32, 8, 8, 8, 8]  DFT residual 3.4e-16  min DFT 7.500e-01
  n= 7: N*A(t), t=0..13: [128, 72, 72, 72, 72, 72, 72, 128, 72, 72] ...  DFT residual 3.0e-15  min DFT 4.375e-01
  n= 9: N*A(t), t=0..17: [512, 392, 392, 400, 392, 392, 400, 392, 392, 512] ...  DFT residual 5.2e-15  min DFT 2.187e-01
  n=11: N*A(t), t=0..21: [2048, 1800, 1800, 1800, 1800, 1800, 1800, 1800, 1800, 1800] ...  DFT residual 7.6e-15  min DFT 1.211e-01
  n=13: N*A(t), t=0..25: [8192, 7688, 7688, 7688, 7688, 7688, 7688, 7688, 7688, 7688] ...  DFT residual 1.3e-14  min DFT 6.152e-02
  n=15: N*A(t), t=0..29: [32768, 31752, 31752, 31760, 31752, 31776, 31760, 31752, 31752, 31760] ...  DFT residual 1.5e-14  min DFT 3.003e-02
  n=17: N*A(t), t=0..33: [131072, 129032, 129032, 129032, 129032, 129032, 129032, 129032, 129032, 129032] ...  DFT residual 2.3e-14  min DFT 1.556e-02
  S1 PASS

S2  static intertwiners L tau_m = tau_(m+1) L, by charge block (direct null spaces)
  orbit counts O_1..O_6 = [1, 1, 2, 2, 4, 6]
  m=1: (++)=1, (+-)=0, (-+)=1, (--)=0; total 2; predicted (++)=1, (-+)=1, others 0
  m=2: (++)=2, (+-)=2, (-+)=0, (--)=0; total 4; predicted (++)=2, (+-)=2, others 0
  m=3: (++)=4, (+-)=0, (-+)=4, (--)=0; total 8; predicted (++)=4, (-+)=4, others 0
  m=4: (++)=8, (+-)=8, (-+)=0, (--)=0; total 16; predicted (++)=8, (+-)=8, others 0
  m=5: (++)=24, (+-)=0, (-+)=24, (--)=0; total 48; predicted (++)=24, (-+)=24, others 0
  S2 PASS

S3  eigenvalues of tau_n by NOT sector (numerical, cross-checked against orbit roots)
  n= 1 (n mod 4 = 1): +-i absent   ; -1 in C=-1: True; any real eigenvalue in C=-1: True  ok
  n= 2 (n mod 4 = 2): +-i in C=-1  ; -1 in C=-1: False; any real eigenvalue in C=-1: False  ok
  n= 3 (n mod 4 = 3): +-i absent   ; -1 in C=-1: True; any real eigenvalue in C=-1: True  ok
  n= 4 (n mod 4 = 0): +-i in C=+1  ; -1 in C=-1: False; any real eigenvalue in C=-1: False  ok
  n= 5 (n mod 4 = 1): +-i absent   ; -1 in C=-1: True; any real eigenvalue in C=-1: True  ok
  n= 6 (n mod 4 = 2): +-i in C=-1  ; -1 in C=-1: False; any real eigenvalue in C=-1: False  ok
  n= 7 (n mod 4 = 3): +-i absent   ; -1 in C=-1: True; any real eigenvalue in C=-1: True  ok
  n= 8 (n mod 4 = 0): +-i in C=+1  ; -1 in C=-1: False; any real eigenvalue in C=-1: False  ok
  n= 9 (n mod 4 = 1): +-i absent   ; -1 in C=-1: True; any real eigenvalue in C=-1: True  ok
  n=10 (n mod 4 = 2): +-i in C=-1  ; -1 in C=-1: False; any real eigenvalue in C=-1: False  ok
  n=11 (n mod 4 = 3): +-i absent   ; -1 in C=-1: True; any real eigenvalue in C=-1: True  ok
  n=12 (n mod 4 = 0): +-i in C=+1  ; -1 in C=-1: False; any real eigenvalue in C=-1: False  ok
  S3 PASS

S4  the OPEN item against the addendum address laws and P27/P21
  n= 3: active    2, silent     0 (0 chiral pairs) | (a) True (b) True (c) True (d) True, |defect| = 4
  n= 5: active    4, silent     0 (0 chiral pairs) | (a) True (b) True (c) True (d) True, |defect| = 12
  n= 7: active    8, silent     2 (1 chiral pairs) | (a) True (b) True (c) True (d) True, |defect| = 28
  n= 9: active   16, silent    14 (7 chiral pairs) | (a) True (b) True (c) True (d) True, |defect| = 60
  n=11: active   32, silent    62 (31 chiral pairs) | (a) True (b) True (c) True (d) True, |defect| = 124
  n=13: active   64, silent   252 (126 chiral pairs) | (a) True (b) True (c) True (d) True, |defect| = 252
  n=15: active  128, silent   968 (484 chiral pairs) | (a) True (b) True (c) True (d) True, |defect| = 508
  n=17: active  256, silent  3600 (1800 chiral pairs) | (a) True (b) True (c) True (d) True, |defect| = 1020
  (e) s = 1..12: orbit -> necklace(u|Cu) bijective onto rot_s(w)=Cw necklaces, fixed by cyclic facing <=> reader-active: True
  S4 PASS

ALL SEALED STATEMENTS PASS
```

### Source (`catchup_audit.py`, reads `catchup_seal.txt` from the same folder)

```python
"""Catch-up audit: P22-P28 recomputed from definitions and composed with the Routes addendum (P14-P18).
Checks the sealed statements S1-S4 in catchup_seal.txt. Standard library + numpy.
Word convention: an n-bit word is an int, position 0 = most significant bit (same as the shipped audits)."""
import sys
from hashlib import sha256
from math import gcd, ceil, cos, sin, pi
from pathlib import Path
import numpy as np

SEAL = Path(__file__).with_name('catchup_seal.txt')
SEAL_SHA = '00028084572a1327151024fcceea6c3ea200ba1f94330b2829c19eba339274eb'
assert sha256(SEAL.read_bytes()).hexdigest() == SEAL_SHA, 'seal changed'

# ------------------------------------------------------------------ native operators (scalar)
def J(x, n):
    r = 0
    for _ in range(n):
        r = (r << 1) | (x & 1); x >>= 1
    return r
def C(x, n): return x ^ ((1 << n) - 1)
def pal(x, n): return J(x, n) == x
def P(x, n): return C(x, n) if pal(x, n) else J(x, n)
def tau(x, n): return ((x << 1) & ((1 << n) - 1)) | (1 ^ (x >> (n - 1)))
def tau_inv(x, n): return (x >> 1) | ((1 ^ (x & 1)) << (n - 1))

def native_ring(n):
    """manual eqs. 2-4: representatives (smaller of each facing pair), seam exchange, partners opposite"""
    N = 1 << n
    reps = sorted(x for x in range(N) if x < P(x, n))
    R = reps[:-1] + [P(reps[-1], n), reps[-1]] + [P(x, n) for x in reversed(reps[:-1])]
    assert sorted(R) == list(range(N))
    return R

def orbits(n, f):
    N = 1 << n; seen = bytearray(N); out = []
    for x in range(N):
        if seen[x]: continue
        orb, y = [], x
        while not seen[y]:
            seen[y] = 1; orb.append(y); y = f(y, n)
        assert y == x
        out.append(orb)
    return out

# ------------------------------------------------------------------ vectorised helpers
def arrays(n):
    N = 1 << n; x = np.arange(N, dtype=np.int64)
    rev = np.zeros(N, dtype=np.int64); y = x.copy()
    for _ in range(n):
        rev = (rev << 1) | (y & 1); y >>= 1
    t = ((x << 1) & (N - 1)) | (1 ^ (x >> (n - 1)))
    chi = np.where(rev == x, -1, 1)
    return t, chi

def mobius(n):
    if n == 1: return 1
    res, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0: return 0
            res = -res
        p += 1
    return -res if n > 1 else res

def divisors(n): return [d for d in range(1, n + 1) if n % d == 0]
def ramanujan(q, j): return sum(d * mobius(q // d) for d in divisors(gcd(q, j)))

ok_all = True
def check(label, cond):
    global ok_all
    ok_all &= bool(cond)
    return 'PASS' if cond else 'FAIL'

print('seal', SEAL_SHA)

# ================================================================== S1
print('\nS1  A_n(t) by direct summation over all words (no overlap count used)')
s1 = True
for n in range(1, 18, 2):
    N = 1 << n; p = 1 << ((n + 1) // 2)
    t_perm, chi = arrays(n)
    cur = np.arange(N, dtype=np.int64); direct = []
    for t in range(2 * n):
        S = int((chi * chi[cur]).sum())
        g = gcd(n, t)
        pred = N - 4 * (p - (1 << ((g + 1) // 2)))
        s1 &= (S == pred); direct.append(S)
        cur = t_perm[cur]
    A = [d / N for d in direct[:n]]
    worst = 0.0; minF = 1e9
    for j in range(n):
        F = sum(A[t] * complex(cos(-2 * pi * j * t / n), sin(-2 * pi * j * t / n)) for t in range(n))
        ram = n * (1 - 4 * p / N) * (j == 0) + (4 / N) * sum((1 << ((d + 1) // 2)) * ramanujan(n // d, j) for d in divisors(n))
        worst = max(worst, abs(F - ram)); minF = min(minF, F.real)
    s1 &= worst < 1e-9 and minF > -1e-12
    print(f'  n={n:2d}: N*A(t), t=0..{2*n-1}: {direct[:min(2*n, 10)]}{" ..." if 2*n > 10 else ""}  DFT residual {worst:.1e}  min DFT {minF:.3e}')
print('  S1', check('S1', s1))

# ================================================================== S2
print('\nS2  static intertwiners L tau_m = tau_(m+1) L, by charge block (direct null spaces)')
def perm_matrix(n, f):
    N = 1 << n; M = np.zeros((N, N))
    for x in range(N): M[f(x, n), x] = 1.0
    return M
def sector_basis(n, sigma):
    N = 1 << n; cols = []
    for x in range(N):
        cx = C(x, n)
        if x < cx:
            v = np.zeros(N); v[x] = 1 / np.sqrt(2); v[cx] = sigma / np.sqrt(2); cols.append(v)
    return np.array(cols).T
def null_dim(Ta, Tb):
    q, p = Ta.shape[0], Tb.shape[0]                 # L is p x q
    Mop = np.kron(Ta.T, np.eye(p)) - np.kron(np.eye(q), Tb)
    sv = np.linalg.svd(Mop, compute_uv=False)
    return int((sv < 1e-9).sum()) + max(0, Mop.shape[1] - len(sv))
O = [len(orbits(m, tau)) for m in range(1, 7)]
s2 = O == [1, 1, 2, 2, 4, 6]
print('  orbit counts O_1..O_6 =', O)
for m in range(1, 6):
    Tm, Tm1 = perm_matrix(m, tau), perm_matrix(m + 1, tau)
    dims = {}
    for a in (1, -1):
        for b in (1, -1):
            Ba, Bb = sector_basis(m, a), sector_basis(m + 1, b)
            dims[(a, b)] = null_dim(Ba.T @ Tm @ Ba, Bb.T @ Tm1 @ Bb)
    full = null_dim(Tm, Tm1)
    oo = O[m - 1] * O[m]
    flip = ((-1) ** m, (-1) ** (m + 1))
    pred = {(1, 1): oo, (-1, -1): 0, flip: oo}
    other = [k for k in dims if k not in pred][0]; pred[other] = 0
    good = dims == pred and full == 2 * oo
    s2 &= good
    fmt = lambda k: ('+' if k[0] > 0 else '-') + ('+' if k[1] > 0 else '-')
    print(f'  m={m}: ' + ', '.join(f'({fmt(k)})={dims[k]}' for k in sorted(dims, reverse=True)) + f'; total {full}; predicted (++)={oo}, ({fmt(flip)})={oo}, others 0')
print('  S2', check('S2', s2))

# ================================================================== S3
print('\nS3  eigenvalues of tau_n by NOT sector (numerical, cross-checked against orbit roots)')
s3 = True
for n in range(1, 13):
    T = perm_matrix(n, tau); flags = {}
    for sigma in (1, -1):
        B = sector_basis(n, sigma)
        ev = np.linalg.eigvals(B.T @ T @ B)
        s3 &= bool(np.all(np.abs(ev ** n - sigma) < 1e-7))
        flags[sigma] = dict(i=bool(np.any(np.abs(ev - 1j) < 1e-7)), mi=bool(np.any(np.abs(ev + 1j) < 1e-7)),
                            m1=bool(np.any(np.abs(ev + 1) < 1e-7)), real=bool(np.any(np.abs(ev.imag) < 1e-7)))
    # exact: each orbit of length L contributes all L-th roots; root e^(2 pi i j / L) has C-value (-1)^j
    ex = {1: set(), -1: set()}
    lab = {(1, 0): '1', (0, 1): 'i', (-1, 0): '-1', (0, -1): '-i'}
    for orb in orbits(n, tau):
        L = len(orb)
        for j in range(L):
            if (4 * j) % L == 0:
                key = (round(cos(2 * pi * j / L)), round(sin(2 * pi * j / L)))
                ex[(-1) ** j].add(lab[key])
    pi_in = [sg for sg in (1, -1) if flags[sg]['i'] and flags[sg]['mi']]
    if n % 2: pred_i = []
    elif n % 4 == 2: pred_i = [-1]
    else: pred_i = [1]
    m1_neg = flags[-1]['m1']; real_neg = flags[-1]['real']
    good = pi_in == pred_i and m1_neg == (n % 2 == 1) and (real_neg == (n % 2 == 1))
    good &= (('i' in ex[1]) == (1 in pred_i)) and (('i' in ex[-1]) == (-1 in pred_i))
    s3 &= good
    where = {(): 'absent', (1,): 'in C=+1', (-1,): 'in C=-1'}[tuple(pi_in)]
    print(f'  n={n:2d} (n mod 4 = {n % 4}): +-i {where:9s}; -1 in C=-1: {m1_neg}; any real eigenvalue in C=-1: {real_neg}  {"ok" if good else "MISMATCH"}')
print('  S3', check('S3', s3))

# ================================================================== S4
print('\nS4  the OPEN item against the addendum address laws and P27/P21')
s4 = True
for n in range(3, 18, 2):
    N = 1 << n; half = N >> 1
    R = native_ring(n); loc = {w: a for a, w in enumerate(R)}
    act = sil = 0; a_ok = b_ok = c_ok = True
    for orb in orbits(n, tau):
        L = len(orb); p = L // 2
        S = set(orb); teeth = [x for x in orb if pal(x, n)]
        if teeth:
            act += 1
            x, y = teeth
            a_ok &= y == C(x, n) and ((loc[x] < half) != (loc[y] < half))
            lower = x if loc[x] < half else y
            a_ok &= (lower >> (n - 1)) == 0
            for z in teeth:
                w = z
                for _ in range(p): w = tau(w, n)
                b_ok &= P(z, n) == w
            c_ok &= {J(z, n) for z in orb} == S                      # active orbits are achiral
        else:
            sil += 1
            JO = {J(z, n) for z in orb}
            c_ok &= not (JO & S) and {P(z, n) for z in orb} == JO
            c_ok &= all(P(tau(P(z, n), n), n) == tau_inv(z, n) for z in orb)
    D1 = {x for x in range(N) if P(tau(P(x, n), n), n) != tau_inv(x, n)}
    D2 = {x for x in range(N) if pal(x, n) != pal(tau_inv(x, n), n)}
    d_ok = D1 == D2 and len(D1) == (1 << ((n + 1) // 2 + 1)) - 4
    s4 &= a_ok and b_ok and c_ok and d_ok and sil % 2 == 0
    print(f'  n={n:2d}: active {act:4d}, silent {sil:5d} ({sil // 2} chiral pairs) | (a) {a_ok} (b) {b_ok} (c) {c_ok} (d) {d_ok}, |defect| = {len(D1)}')

def canon(w, L):
    best, y, m = w, w, (1 << L) - 1
    for _ in range(L - 1):
        y = ((y << 1) & m) | (y >> (L - 1)); best = min(best, y)
    return best
e_ok = True
for s in range(1, 13):
    L = 2 * s
    cls_of_orbit = []
    for orb in orbits(s, tau):
        cl = {canon((u << s) | C(u, s), L) for u in orb}
        e_ok &= len(cl) == 1
        c = cl.pop()
        fixed = canon(J(c, L), L) == c and canon(C(c, L), L) == c
        active = any(pal(u, s) for u in orb)
        e_ok &= fixed == active
        cls_of_orbit.append(c)
    e_ok &= len(set(cls_of_orbit)) == len(cls_of_orbit)
    allc = {canon(w, L) for w in range(1 << L) if (((w << s) | (w >> s)) & ((1 << L) - 1)) == C(w, L)} if L <= 20 else set(cls_of_orbit)
    e_ok &= allc == set(cls_of_orbit)
print(f'  (e) s = 1..12: orbit -> necklace(u|Cu) bijective onto rot_s(w)=Cw necklaces, fixed by cyclic facing <=> reader-active: {e_ok}')
s4 &= e_ok
print('  S4', check('S4', s4))

print('\nALL SEALED STATEMENTS PASS' if ok_all else '\nSOME SEALED STATEMENTS FAILED (recorded as failed)')
```

---

## Entry C2 · 5 Nov 2026 · correction to C1, and the half-lap contract

**Correction (C1 read implementations).** C1 re-ran audits, counted orbits and quoted state shares. That is reading what implementations return, not the domain. Its "OPEN, narrowed" item is superseded by GPT's P29 (a primitive closed route has 0 or 1 reflection axis; origin-free one-bit answer) and P30 (τ = J·B). C1's sealed checks stay as recorded; none of them is a domain result.

**STANDS (contract-side, no run).** Let F be a reversible continuation and σ an involution with σF = Fσ. On any orbit where the half-lap is the involution, F^L = σ, every reading f with f∘σ = f closes at L, and every reading with f∘σ = −f closes only at 2L and lives entirely in the odd harmonics of the 2L lap. Proof: F^(t+L) = σF^t on the orbit. Recovered (cyclic-group representation theory), not new. Implementations of the one contract:

| Implementation | σ | L | reading σ cannot see (closes at L) | reading σ flips (the way home) |
|---|---|---|---|---|
| twisted clock, P27–P28 | C | p | palindrome answer s | the signed centre, C-odd sector |
| v6.2 pair sector | H_1001 | 806 | the reader-frame (ride-along) state | the fixed-frame position bits that 1001 toggles |
| two-lap closure, *Retained Continuation* | half-lap symmetry | 21,577,661 | the field (returns to the mold) | the reader, complemented |

The antiperiodic streams of 27 Oct (second half = NOT of the first) are the σ-odd channel; the twisted clock generates them (z_(t+n) = NOT z_t).

**OPEN (contract-side).** On τ the contract also yields σ and L without a walk, because τ is two reflections (P30): JτJ = τ⁻¹ puts the reversal-fixed points half a lap apart (P27). The retained step is four involutions, F = Move∘Mark∘Turn∘Collide; the 4 Nov algebra (untested) says one bit, plane 2's 1 ⊕ ℓ(x), keeps it from being its own reverse. Derive the involution R with RFR = F⁻¹ that carries that bit, as B carries the boundary NOT, and the σ it forces; or the exact obstruction. This is also the compensating transformation GPT's retained-field OPEN asks for.

---

## Entry C3 · 5 Nov 2026 · P29–P32 and the all-k selector run, read on the contract side

**Inputs.** *The Answer Without an Origin* (P29–P32, docx), and an external notebook run (predictions15 rerun, native-program count, instruction-field saturation, all-k collective selector). Nothing re-measured here; every line below is a one-line identity or an ownership note.

**STANDS (one reading of all of it).** Reversal's fixed point is either a site or a gap, at every level, and the two kinds are facing's two branches.

| Level | Centre on a site (C branch: the site is reversal-fixed, NOT acts there, gated by the whole) | Centre on a gap (J branch: the two sides are a reversal pair; the whole's symmetry is carried by that pair) |
|---|---|---|
| bits in a word | odd LEN: b′ = b ⊕ s | even LEN: the lamp on the two central bits |
| contacts in a chain | odd k: the middle contact holds the centre, so lone seams = 0 | even k: hinge face, c_(m+1) = J(c_m), so lone seams exist |
| positions on a primitive route | axis through a site (odd p; even p site-axis) | even p gap-axis |
| addresses on Rₙ | none (2ⁿ is even) | the seam: r* beside J(r*) |

A whole reads the same both ways while no part does (a lone seam) only when its centre is a gap.

**STANDS (native = two reflections).** P15.1's criterion f = J·g (g an involution, Fix g closed under NOT) is P32 in general: every native program is reversal followed by a second reflection; τ = J·B is the one whose second reflection fixes nothing. In the instruction group (translate by t, rotate by k), native ⇔ σᵏJt = t: the translation word has axis k. So P29's a(w) is the nativeness of "translate by w", and |Native(Gₙ)| = n(p+q)/2 is Burnside's reflection count (recovered).

**Ownership.** The native-program total Σ C(2ⁿ⁻¹,k)(2ⁿ−2k−1)!! is already the Routes addendum's Table E count. The all-k selector law closes the addendum's OPEN item 1 (collective selector upward); the run is the external notebook's.

**OPEN (refined).** The retained step F = Move∘Mark∘Turn∘Collide as a native program: a reading R and an involution G with F = R·G and Fix G closed under the machine's NOT, and whether R's centre is a site (fixed points, so teeth that mark the half-lap from the contract) or a gap (none, as with B). This is the coupled-field OPEN named in P29–P32 §8.

---

## Entry C4 · 5 Nov 2026 · the published collection read against the current line, and the retained write's mirrors

**Input.** The project document *PublishedPaperCollection.docx*, about fifty papers. About a dozen of them carry the current line: *One Inverter*; *The Way Between*; *Against Its Own Reverse*; *The Shape Channel* §3; *Nest* §§7–8; *Survive the Field* §§6–7; *The Reader in the Mirror* §3; *The Interior of a Reader* §§9, 13.2; *Distinction That Must Continue* §§2, 6; *Decompiling Addressable Binary Rings* (the Möbius bridge); *The Inverted Mold* (thesis). The rest are the BBP towers, SHA geometry, the relation layer and token graphs, folding, and ML. Not in the collection: P18–P32, *Two Laps Home*, §181, the Routes addendum, *Exact Algebra of Retained Continuation*.

**Ownership (recovered from the collection, nothing re-run).**

| Current line | Already in the collection |
|---|---|
| τᵏ = rotl_k ⊕ 1_k; τⁿ = C; orbits of length 2p over odd divisors, Möbius/Golomb count (P27 H(p), P30, P31 counts) | *One Inverter* Thm 3.2, Thm 4.1 [STANDS Golomb, A000016], Thm 4.2 (locks) |
| even and odd eigen-sectors (P28) | *The Way Between* Prop 2.6: U_τ = X_last·R, U_τⁿ = X^⊗n |
| half-lap contract (C2 STANDS) | *The Shape Channel* §3.3 (a half-return reads closed under the complementary quotient); *Against Its Own Reverse* Thm 6 (P-even → even Walsh degrees, P-odd → odd; the odd carrier lives on the palindromes); *Nest* Thms 10–12 (odd characters carry the lean; zero needs an inversion); *Survive the Field* Prop 5; *The Way Between* Thms 5.2–5.3 (odd loop exactly where the mirror is reached; shape closes at C(start), frame turned by π) |
| centre on a gap at even n, on a site at odd n; P23 | *One Inverter* Thm 5.1 (centre = innermost lamp), Thm 6.2 (lamps blind to the middle bit at odd n; cone against sphere); *Against Its Own Reverse* §4 (odd steps insert a pure value; at d = 1 the middle bit becomes the core's face); *The Way Between* Thm 4.2 (even centre = middle dihedral) |
| centre trace, holonomy (P25, P29) | *One Inverter* Thm 5.4 (one lap of readings XORs to 1; readings + face return x), Thm 8.1 (even lane count leaves a holonomy no state cancels), Thm 3.5 (inverter parity: odd = clock, even = latch) |
| P20 cross-LEN facing, P26 recursive gate | *Against Its Own Reverse* Thm 3 (even to odd), Thm 4 (the route is the mirror lift; E/G) |
| facing's two branches | *Against Its Own Reverse* Thm 5 (P a reflection off the palindromes, a half-turn on them; never an azimuthal half-turn) |
| native = two reflections (C3 STANDS) | *One Inverter* Prop 2.1(a) PTP = T⁻¹; Prop 8.8(a) (J reverses the port rail); *Nest* §7 (over XOR the Mold's inverse is its swap-conjugate) |
| the retained write | *Nest* §7 and *Survive the Field* §7.1 (the Mold, Fredkin's second-order construction; shears and swaps); *Survive* Thm 7 (a Mold's F reads only retained registers); *The Interior of a Reader* §13.2 (invertibility of a second-order rule holds by construction and is not a finding); *The Reader in the Mirror* Prop 3.4 (the six-fold turn [[1,−1],[1,0]], cube = the half-turn; its mod-2 shadow is the write's [[1,1],[1,0]]) |

**STANDS (one law, from the owners above).** The C2 half-lap table and the C3 site/gap table are one table. A gap centre reads a difference, which C cannot see: under τ it closes at the half-lap, and the twist shows only as the one reading taken across the boundary (*One Inverter* 5.4a). A site centre reads a value, which C flips: its stream is antiperiodic, y_(t+n) = NOT y_t, from τⁿ = C, and closes only at the full lap. Whether a centre is a site or a gap decides which channel it reads.

**STANDS (τ's two mirrors; recovered).** τ = J·B. On positions B's axis runs through site 0 and carries the NOT, so B fixes no word; J's axis is half a step away; the product is the one-step turn, and the NOT on B's axis is the twist it carries round. On a J-symmetric orbit (every τ-orbit has even length) the two symmetric points of the reversible pair must both lie in Fix J, half a lap apart, because Fix B is empty: P27's teeth. Chiral orbits have none. Recovered: the symmetric-orbit lemma for reversible maps (Devaney, *Trans. AMS* 218, 1976; Lamb and Roberts, *Physica D* 112, 1998).

**RUNS (contract checks C4.0–C4.5, every state of each identity's domain).**
- The v6.2 partner (thread code: P(x) = x ⊕ 7 ⊕ 4ℓ(x), ℓ(x) = x₀ ⊕ x₁) is the native facing with its centre on plane 2. The 4 Nov constant 1 ⊕ ℓ(x) is the centre's answer s.
- On one plane the write (cell ← carry ⊕ κ, carry ← collision ⊕ κ) is the Mold, of order 3. It has three mirrors: R1 (swap, turned by κ), SH (the shear: cell ← collision, carry kept; reads no κ), R3 (cell kept, carry ← collision ⊕ κ). Their partners G = R·W keep the carry, the cell and the collision respectively.
- Coupled write, outer planes κ = 1, centre κ = 1 ⊕ ℓ: with ℓ constant all nine plane pairings reverse it. With ℓ live, for every one of the fourteen live ℓ, exactly two survive: (outer R3, centre SH), where the outer mirror keeps what the answer reads and the centre's mirror is blind to it; and (outer R1, centre R3), where the outer swap moves what the answer reads and the centre's mirror carries the answer. The second is the "R that carries that bit, as B carries the boundary NOT" asked for in C2.
- The swap on every plane, (R1, R1), is among the seven the answer kills.
- The half-turn comes back through the answer. Mod 2, the six-fold turn of *The Reader in the Mirror* Prop 3.4 loses its cube: each plane's write has order 3. With the native answer live, the coupled write has order 6. Its cube is an involution that moves the centre plane alone. With the answer held fixed, the cube is the identity. Over one three-write lap, the centre's three answers XOR to 1, as a lap of centre readings does in *One Inverter* Thm 5.4(a). The parity does not make the half-turn by itself: an answer held at 1 has the same parity, and its cube is the identity. What makes it is the answer varying within the lap. So the write carries its own half-lap, F^(t+3) = σF^t with σ the cube, and the C2 contract applies to it with L = 3.

**Corrections.**
- **K6.** The C2 STANDS (half-lap contract) and C3 STANDS (site/gap; native = two reflections) are recoveries from the collection (table above) and should have been attributed there. They are one law, not two.
- **K7.** My unsealed expectation for C4.3 was a single surviving plane pairing, (R3, SH). The first run returned two. That line is kept below, and C4.3 now states the found contract.
- **K8.** The 4 Nov statement that plane 2's bit is "the only thing standing between the machine and a clean time reversal" holds for the swap. On the write, the bit selects which mirrors survive and does not block them. The premise carried in C2/C3 as "untested" is corrected to this.

**OPEN (narrowed to the move).** Every permutation of a finite set is a product of two involutions (reflect each cycle), and a second-order rule is invertible by construction (*Interior of a Reader* §13.2). So the question with content is a local mirror of the whole step, one that also carries the reader back across the cell it wrote. The first form to test is the leapfrog form from *Survive*'s list: one mirror shared by the write and the move. Whichever of (outer R3, centre SH) or (outer R1, centre R3) extends decides whether the step's centre is a site or a gap, and so whether its symmetric points hand over the half-lap the way B's do on τ.

### Live output (`c4_reversor.py`, SHA-256 e81f7f41…; output 4649d991…)

```
PASS  C4.0 facing: centre turns by s at odd n; on 3 bits P(x) = x + (1, s(x), 1)
PASS  C4.1 one plane: W has order 3; R1, SH, R3 each reverse it; SH does not read k
PASS  C4.2 the three reversors' G = R.W keep carry / cell / collision respectively: {'R1': ['carry'], 'SH': ['cell'], 'R3': ['collision']}
PASS  C4.3 coupled write: constant coupling -> all nine plane-wise pairings reverse it; every live coupling -> exactly two: (outer R1, centre R3) and (outer R3, centre SH)
PASS  C4.4 native coupling (centre turns by s = 1 + outer lamp): (R3, SH) reverses the write; the swap (R1, R1) does not
PASS  C4.5 v6.2 partner = native facing conjugated by a plane relabelling; relabellings that do it: [(1, 0, 2), (1, 2, 0)]
PASS  C4.6 native coupling: write order 6; its cube moves the centre plane alone; constant answer -> cube = I; a lap's three answers XOR to 1
```

First-run line kept (K7): `FAIL  C4.3 coupled write, every coupling l: the only plane-wise reversor is (outer R3, centre SH): [('R1', 'R3'), ('R3', 'SH')]`

### Source (`c4_reversor.py`)

```python
# C4 contract checks: the retained write and its reversors (identities only; no walks).
from itertools import product, permutations
def J(x): return x[::-1]
def C(x): return tuple(1-b for b in x)
def P(x): return J(x) if J(x)!=x else C(x)
def s(x): return int(J(x)==x)

# (0) native facing on odd n: middle bit turns by the answer; at n=3, P(x) = x xor (1, s, 1)
ok0 = all(P(x)[len(x)//2] ^ x[len(x)//2] == s(x) for n in (3,5,7,9) for x in product((0,1),repeat=n))
ok0 &= all(tuple(a^b for a,b in zip(P(x),x)) == (1,s(x),1) for x in product((0,1),repeat=3))
print("PASS" if ok0 else "FAIL", " C4.0 facing: centre turns by s at odd n; on 3 bits P(x) = x + (1, s(x), 1)")

# one plane: state (cell c, carry w); write W_k(c,w) = (w+k, w+k+c)
def W(c,w,k): return (w^k, w^k^c)
def Winv(c,w,k): return (c^w, c^k)
R1 = lambda c,w,k: (w^k, c^k)        # swap, complemented by k
SH = lambda c,w,k: (c^w, w)          # shear: cell := collision, keep carry (no k)
R3 = lambda c,w,k: (c, c^w^k)        # keep cell, carry := collision + k
pl = list(product((0,1),repeat=2))
def rev(R,k): return all(R(*W(*R(c,w,k),k),k)==Winv(c,w,k) and R(*R(c,w,k),k)==(c,w) for c,w in pl)
ok1 = all(rev(R,k) for R in (R1,SH,R3) for k in (0,1))
ok1 &= all(W(*W(*W(c,w,k),k),k)==(c,w) for c,w in pl for k in (0,1))
print("PASS" if ok1 else "FAIL", " C4.1 one plane: W has order 3; R1, SH, R3 each reverse it; SH does not read k")
def keeps(R,k,role):
    f={'cell':lambda c,w:c,'carry':lambda c,w:w,'collision':lambda c,w:c^w}[role]
    return all(f(*R(*W(c,w,k),k))==f(c,w) for c,w in pl)
roles={nm:[r for r in ('cell','carry','collision') if keeps(R,1,r)] for nm,R in (('R1',R1),('SH',SH),('R3',R3))}
ok2 = roles=={'R1':['carry'],'SH':['cell'],'R3':['collision']}
print("PASS" if ok2 else "FAIL", " C4.2 the three reversors' G = R.W keep carry / cell / collision respectively:", roles)

# three planes (a, m, b): outer planes k=1, centre plane k = 1 + l(x_a, x_b), any l: F2^2 -> F2
Ls=[(lambda t:(lambda xa,xb:(t>>(2*xa+xb))&1))(t) for t in range(16)]
def Wfull(S,l):
    (ca,wa),(cm,wm),(cb,wb)=S; km=1^l(ca^wa,cb^wb)
    return (W(ca,wa,1),W(cm,wm,km),W(cb,wb,1))
def make_R(ro,rm,rc):
    def R(S,l):
        (ca,wa),(cm,wm),(cb,wb)=S; km=1^l(ca^wa,cb^wb)
        return (ro(ca,wa,1), rm(cm,wm,km), ro(cb,wb,1))
    return R
states=list(product(pl,repeat=3))
def reverses(R,l): return all(R(R(S,l),l)==S and Wfull(R(Wfull(S,l),l),l)==R(S,l) for S in states)
cands={(a,b):make_R(ra,rb,None) for a,ra in (('R1',R1),('SH',SH),('R3',R3)) for b,rb in (('R1',R1),('SH',SH),('R3',R3))}
def survivors(l): return sorted(k for k,R in cands.items() if reverses(R,l))
const=[l for l in Ls if len({l(a,b) for a in (0,1) for b in (0,1)})==1]
live=[l for l in Ls if l not in const]
ok3 = all(len(survivors(l))==9 for l in const) and all(survivors(l)==[('R1','R3'),('R3','SH')] for l in live)
print("PASS" if ok3 else "FAIL", " C4.3 coupled write: constant coupling -> all nine plane-wise pairings reverse it;",
      "every live coupling -> exactly two: (outer R1, centre R3) and (outer R3, centre SH)")
lamp=lambda xa,xb: xa^xb
ok4 = reverses(make_R(R3,SH,None),lamp) and not reverses(make_R(R1,R1,None),lamp)
print("PASS" if ok4 else "FAIL", " C4.4 native coupling (centre turns by s = 1 + outer lamp): (R3, SH) reverses the write; the swap (R1, R1) does not")

# (5) the v6.2 slice's partner (thread code: P(x) = x ^ 7 ^ 4*ell(x), ell(x) = (x ^ (x>>1)) & 1)
#     is the native facing with its centre moved to plane 2 (a plane relabelling)
ell = lambda v: (v ^ (v >> 1)) & 1
Pv = lambda v: v ^ 7 ^ (4 * ell(v))
def to_t(v): return ((v>>2)&1, (v>>1)&1, v&1)            # string x0 x1 x2 = bits 2,1,0
def to_i(t): return (t[0]<<2)|(t[1]<<1)|t[2]
def perm(t,pi): return tuple(t[pi[i]] for i in range(3))
def inv(pi): return tuple(sorted(range(3), key=lambda i: pi[i]))
hits=[pi for pi in permutations(range(3)) if all(to_i(perm(P(perm(to_t(v),inv(pi))),pi))==Pv(v) for v in range(8))]
print("PASS" if hits else "FAIL", " C4.5 v6.2 partner = native facing conjugated by a plane relabelling; relabellings that do it:", hits)

# (6) the half-turn: the coupled write has order 6; its cube is an involution on the centre plane alone;
#     with the answer constant the cube is the identity. Over one three-write lap the centre's answers XOR to 1.
def it(S,k,l):
    for _ in range(k): S=Wfull(S,l)
    return S
cube=lambda S,l: it(S,3,l)
ok6  = all(it(S,6,lamp)==S for S in states) and any(cube(S,lamp)!=S for S in states)
ok6 &= all(cube(S,lamp)[0]==S[0] and cube(S,lamp)[2]==S[2] for S in states)
ok6 &= all(cube(S,l)==S for l in const for S in states)
def answers(S,l):
    out=[]
    for _ in range(3):
        (ca,wa),(cm,wm),(cb,wb)=S; out.append(1^l(ca^wa,cb^wb)); S=Wfull(S,l)
    return out
ok6 &= all(sum(answers(S,lamp))%2==1 for S in states)
print("PASS" if ok6 else "FAIL", " C4.6 native coupling: write order 6; its cube moves the centre plane alone; constant answer -> cube = I; a lap's three answers XOR to 1")
```

---

## Entry C5 · 5 Nov 2026 · GPT's lineage entry, merged (numbered C3 there)

**Numbering, logged (merge).** GPT appended its own entry to a copy of this audit taken after C2 and numbered it C3 (`NEXUS_running_audit_with_C3 (1).md`, supplied 5 Nov). That number collided with C3 here, so the entry is entered as C5. It is entered verbatim below and taken, not re-run. C6 addresses its two OPEN items. Its custody naming, P16X/P16Y in place of the Routes addendum's P16, stands.

> **Provenance.** User-supplied `Pasted text(20261105-224045).txt` and `NEXUS_running_audit.md` Entries C1–C2; source facing manual kept unchanged. Independent checks and exact algebra recorded in the supplemental Appendix D to `Facing_Composition_and_the_Center_in_Native_Binary_Rings_P16X_P16Y_Expanded.docx`.
>
> **CUSTODY.** The original Routes-addendum `predictions16.txt` is the *feedback-shift-program* seal. This continuation is named P16X/P16Y to avoid retroactively changing its owner. P16X seal SHA-256 `cc61a452a973ada25d00a130a426b638c403d4b0cb8ed4faaa5ef63558c226a4`; P16Y seal SHA-256 `766d6ef71b22091057d3711953dfd7aceab180446ebfef20d9712c8b4bbffb3d`.
>
> **STANDS: native programs.** The P15.1 criterion `J f J=f^-1`, with `Fix(Jf)` invariant under complement, gives exact count `Σ_{h=0}^{2^(n-1)} binom(2^(n-1), h) (2^n-2h-1)!!` of reversible native programs.
>
> **STANDS: instruction group.** `<C,σ,τ> = F_2^n ⋊ Z_n` has order `n·2^n`; the table-native subset has cardinality `n(p_n+q_n)/2`, where `p_n=2^ceil(n/2)` and `q_n=2^ceil((n+1)/2)`. The directed Cayley diameter under `{C,σ,τ}` is exactly `2n-2` for `n≥2`: a full traversal can set arbitrary bits, while a target at rotation `n-2` with two unequal untouched bits requires at least that many shifts. This converts the user's observed finite saturation depth to an all-LEN theorem.
>
> **STANDS: composition parity.** At `k=2m+1` the middle *contact* holds the whole palindrome condition, hence `lone_seams=0`. At `k=2m` the middle *joint* may become palindrome without any local palindrome contact. In the §181 block model the collective-only count is `r(N-1)^m` with `N=2^n` and `r=2^ceil(n/2)`. The separate-facing break count is `N^(k+1)-N(N-1)^k-N`; the whole/parts discrepancy at even `k` adds `r(N-1)^m+N-r`.
>
> **STANDS: offset hinge transfer.** In overlapping-window model define adjacency `A_L` from a `(L-1)`-face `v` to `prefix_{L-1}(a|v)` whenever `a|v` is nonpalindromic. With `H` the palindromic hinge faces, `lone_seams(L,2m) = 1_H^T A_L^m 1`. The palindrome whole uniquely inverts by stripping mirror-paired outer bits back to the hinge.
>
> **RUNS: exact independent local audits.** P16X BFS in the affine rotational-coordinate group through LEN 11, complete small-width block-contact and sliding-window path enumeration; P16Y transfer vs independent complete palindrome-word enumeration at `L=2..7,m=1..8` and `L=8..12,m=1..6`. All executed checks pass. Earlier pasted data was known before sealing; those values are not counted as blind landings.
>
> **OPEN, without search.** (1) All-`m` isomorphism responsible for equal adjacent even/odd LEN hinge-transfer rows; (2) retained reader-field reversor `R F R=F^-1` and the plane-2 compensation for `1⊕ell(x)` from Entry C2. Neither a specific return time nor a new physics mapping is asserted by this entry.

---

## Entry C6 · 5 Nov 2026 · faced tables, the centre site, and the retained step's mirrors

**Inputs, all read in full.** *Facing, Composition and the Center in Native Binary Rings* (`902ad2c9015ec5b9…`) and GPT's expanded copy with Appendix D (`a54f0f7be11008ad…`; identical apart from the header and Appendix D); *Routes, Interfaces and Programs on Native Binary Rings* (`e1d0963e4f1afd56…`); *Answer Memory and Reader Memory in Random 3-SAT* (`c039149913fa25ca…`); the external faced-table run; GPT's message and its lineage audit (C5 above); the v6.2 relative machine as written in the 4 Nov thread (`rel_step`). One notebook holds every check: `NEXUS_C6_Faced_Tables_Centre_and_Mirrors.ipynb`, SHA-256 `b7eaec4f828a77ed6b8ee9d2c4f3600afa519898577464fbe8825184e764bb4b`. Seal C5: `c5_seal.txt`, SHA-256 `d6894232eb8e3eed45a2c4b15acbd2bbb46b096dcc2f98c34791a018ecc7daab`, hashed 2026-11-05T23:21:21Z before the first run. Its text is embedded in the notebook and checked there.

**A · Facing a table reads the program backward in time. STANDS; RUNS (external result, re-run here by a different route).** Facing a transition x|f(x) gives J(f x)|J(x) when the transition reads differently backward and its NOT when it reads the same. The faced table is a program exactly when the self-reading set S = {x : f(x) = Jx} is closed under NOT, and that program is J f⁻¹ J, the way home read backward. P15.1 splits into two clauses: the reversed table is a program (NOT-closure), and it is f itself (J f J = f⁻¹). Each x ∈ S with Cx ∉ S tears one hole, at x, and one double, at Cx. The native successor's only self-reading step is the seam edge J(r⋆) → r⋆ (Routes A8; manual Thm 8.3). So its faced table tears once, at the ring's centre, at every LEN. That answers the external run's question about carrying the seam law across LEN offsets: it is already a theorem, and no new run is needed.

**B · Appendix D.5's equal rows. STANDS; RUNS contact LEN 2–11. Closes C5's OPEN (1).** Φ(W) = δ(W) ⊕ W₀·1, with δ(W)ᵢ = Wᵢ ⊕ Wᵢ₊₁, carries the wholes of contact LEN 2j + 1 bijectively onto those of contact LEN 2j, for every m.
1. A window of odd LEN reads the same both ways exactly when its differences do. J commutes with δ, and equal differences leave Jw ∈ {w, Cw}, where Jw = Cw is impossible: the centre would equal its own NOT.
2. An even palindrome has equal middle bits, so Φ(W) is a palindrome whose centre is W₀.
3. The inverse reads W₀ off that centre and integrates.

The even whole's centre site stores the odd whole's face bit. XOR with the alternating word, which is a palindrome at every odd LEN, exchanges palindromic and anti-palindromic wholes and keeps every odd window. That is the same fact read the other way.

**C · The retained write's two mirrors, partner cell included. RUNS every local state.**
- **The partner cell.** It is written by PhiA(P(x)) = NOT x on every plane, so the coupling never reaches it.
- **QA, blind to the answer.** The outer planes keep the cell and set carry := NOT collision. The centre plane shears, cell := collision. The partner's centre plane takes the centre carry.
- **QB, carrying the answer.** The outer planes swap cell and carry, both NOTed. The centre plane sets carry := collision ⊕ answer. The partner cell takes the collision on its outer planes and the answer on its centre plane.
- **The half-reversor identity, STANDS.** For every write mirror Q, (Q·Shift)·F·(Q·Shift) = F⁻¹, since Shift² = I and QWQ = W⁻¹.
- **Why it is not a reversor.** Q·Shift is an involution only if Q commutes with the move. That needs Q to keep the carry, which the move reads, and to act alike on every cell, since the move re-indexes the field. Neither write mirror keeps the carry. No uniform, carry-keeping cell map reverses the write (all 764 involutions of the eight values tried). The leapfrog form, one mirror shared by write and move, is closed.

**D · The full step. RUNS under seal C5 (after K10); measured beyond it.**
- **Under seal.** No form Q, Q·Shift, Shift·Q, Q·Shift·Q, Shift·Q·Shift (Q ∈ {QA, QB}) is a reversor.
- **Measured, beyond the seal.** Three families hold no reversor: 8,192 edge mirrors (relocate across the last move, keep the carry, apply masks or an exchange at the two endpoints and their partners); 2,916 read-back mirrors (the ring's involutive value maps on carry, values and positions, with and without relocation); and the odd powers of Q·Shift.
- **Reading.** In every form built from the step's own verbs, reading the step backward runs a different program. The step behaves like a mirror twin (manual Thm 11.1), not a native program. Its half-lap is carried by the translation H₁₀₀₁, not by a pair of mirrors, which the C2 contract allows. Every permutation of a finite set is a product of two involutions (reflect each cycle), so what remains OPEN is only whether a readable mirror exists.

**Bridge, recovered (3-SAT paper Thm 4; manual Thm 8.1(b); Routes A12).**
- **The selector is a mirrored-equalities function.** The facing selector sₙ is the conjunction of the mirrored equalities Eₙ.
- **The two memories.** Its answer memory is one bit. Read in binary order its reader memory is 2^(n/2). Read in the ring's outside-in mirror order it is at most three states.
- **The centre.** The outside-in reader reaches the centre holding s. The centre never enters s, and it is where facing writes s, b′ = b ⊕ s. In this reading the centre is the end of the question and the start of continuation.

**Corrections.**
- **K9.** Run 1 wrote QB's partner term without its centre plane, and M2 failed as sealed. A search over partner terms found that the answer must also be written on the partner's centre plane. C2 carries the corrected QB, and the run-1 line is kept below.
- **K10.** Run 1 checked M3 as R·F·R = F⁻¹ without R² = I. Q·Shift passes that by the identity above, so run 1 printed FAIL. With the involution required, which is the definition of a reversor, M3 holds.
- **Re-assessed (OPEN premise).** C2–C4 asked for the retained step as two mirrors, F = R·G. On the write that holds, with QB carrying the bit as B carries the boundary NOT. On the full step no readable mirror has been found, and the leapfrog form is provably closed. The premise stands only as an OPEN question, not as an expectation.

**OPEN.** Find the step's twin: the partner P′ for which F_P′, read through a readable relabelling, is the way home of F_P. That is the twin form of Facing Thm 11.1. Otherwise, name what forbids it. Seal the twin's partner before running.

### Live output (notebook, executed 5 Nov)

```
library loaded
PASS  A1 faced table is a program iff the self-reading set is NOT-closed, and then equals J f^-1 J (all programs, n = 2, 3)
PASS  A2 the native successor has one self-reading step, the seam J(r*) -> r*, so its faced table tears once: hole J(r*), double C J(r*) (n = 2-10)
PASS  B1 Phi(W) = delta(W) xor W0 is a bijection odd row -> even row; the even centre is W0 (contact LEN 2-11, every m run)
   counts (L even, L odd, m, wholes): [(2, 3, 1, 2), (2, 3, 2, 2), (2, 3, 3, 2), (2, 3, 4, 2), (2, 3, 5, 2), (2, 3, 6, 2), (2, 3, 7, 2)] ... [(10, 11, 1, 62), (10, 11, 2, 122), (10, 11, 3, 238)]
PASS  C1 the partner cell is written by NOT x on every plane: PhiA(P(x)) = ~x
PASS  C2 QA and QB are involutions and reverse the write on every local state (QA True, QB True)
PASS  C3 (Q.Shift) F (Q.Shift) = F^-1 for both write mirrors
PASS  C4 neither mirror keeps the carry or commutes with the move, so Q.Shift is not an involution
PASS  C5 no uniform cell map with the carry kept reverses the write (764 involutions of the 8 values tried)
C5 seal sha256 d6894232eb8e3eed45a2c4b15acbd2bbb46b096dcc2f98c34791a018ecc7daab
PASS  M0 machine = the thread rel_step: the seed returns to an empty field at t = 806 with e = 0, w = 1
     QA               involution True   R.F.R = F^-1 False
     QA.Shift         involution False  R.F.R = F^-1 True
     Shift.QA         involution False  R.F.R = F^-1 False
     QA.Shift.QA      involution True   R.F.R = F^-1 False
     Shift.QA.Shift   involution True   R.F.R = F^-1 False
     QB               involution True   R.F.R = F^-1 False
     QB.Shift         involution False  R.F.R = F^-1 True
     Shift.QB         involution False  R.F.R = F^-1 False
     QB.Shift.QB      involution True   R.F.R = F^-1 False
     Shift.QB.Shift   involution True   R.F.R = F^-1 False
PASS  M3 no listed map is a reversor (an involution with R.F.R = F^-1) of the full step
measured: edge mirrors 8192 tried, reversors 0; read-back mirrors 2916 tried, reversors 0; odd powers of Q.Shift reversing F: none
```

Run-1 lines kept (K9, K10): `FAIL  M2 the write is reversed by QA (True) and by QB (False) on every local state` · `FAIL  M3 none of the listed mirrors reverses the full step` (Q·Shift passed R·F·R = F⁻¹ and is not an involution)

### Seal C5 (text)

```
NEXUS C5 seal: the retained step's mirrors, write and move. Sealed before running c5_mirror.py.
Machine: the thread's relative v6.2 step (e, w, E[0..7]): x = E[0]^w, y = P(x), E[0]^=y, E[off(e)]^=PhiA(y),
off(e) = 7 if e = 0 else 3, then e ^= ell(x), w = y, E <- E[r ^ x]. P(c) = c^3 if ell(c) else c^7, ell(c) = c0^c1,
PhiA(y) = y ^ 4*ell(y). Planes: bits 0,1 = outer (turn always), bit 2 = centre (turns by 1 ^ ell).
W = the write at the reader (no shift). Shift = re-index by P(w) and e ^= ell(P(w)). F = Shift . W.
M1  The partner cell is written by NOT(x) on every plane (PhiA(P(x)) = ~x): the coupling never reaches it.
M2  W is reversed (Q W Q = W^-1, Q^2 = I, every local state) by
      QA: outer planes R3 (keep cell, carry := NOT collision); centre plane SH (cell := collision, keep carry);
          partner cell's centre plane ^= centre carry.
      QB: outer planes R1 (swap cell and carry, both NOTed) and partner cell's outer planes ^= outer collision;
          centre plane R3 turned by the answer (keep cell, carry := collision ^ (1 ^ ell(x_outer))).
M3  F (the full step) is reversed by none of Q, Q.Shift, Shift.Q, Q.Shift.Q, Shift.Q.Shift for Q in {QA, QB}:
    the move reads the collision, and no local mirror of the write meets the move.
A failed clause is recorded as failed.
```

### Source (the notebook's code cells, in order)

```python
# ---------------------------------------------------------------- library (self-contained)
from itertools import product, permutations
from hashlib import sha256
import random

def J(w): return w[::-1]
def C(w): return tuple(1 - b for b in w)
def pal(w): return J(w) == w
def Pw(w): return C(w) if pal(w) else J(w)               # native facing on a word (tuple of bits)

def native_ring(n):
    words = [tuple(w) for w in product((0, 1), repeat=n)]
    reps = sorted(w for w in words if w < Pw(w))
    return reps[:-1] + [Pw(reps[-1]), reps[-1]] + [Pw(w) for w in reversed(reps[:-1])]

# v6.2 relative machine, exactly as the thread's rel_step (4 Nov): state (e, w, E[0..7]), values 0..7
ell  = lambda c: (c ^ (c >> 1)) & 1                     # outer lamp of a 3-bit heading (bits 0 and 1)
P    = tuple((c ^ 3) if ell(c) else (c ^ 7) for c in range(8))
PhiA = tuple(c ^ (4 * ell(c)) for c in range(8))
off  = lambda e: 3 if e else 7                         # partner cell, relative to the reader

def F(s):                                              # the step: Collide, Turn, Mark (cell and partner), Move
    e, w, E = s; x = E[0] ^ w; y = P[x]
    Ew = list(E); Ew[0] ^= y; Ew[off(e)] ^= PhiA[y]
    return (e ^ ell(x), y, tuple(Ew[r ^ x] for r in range(8)))
def Finv(s):
    e1, y, E1 = s; x = P[y]; Ew = [E1[r ^ x] for r in range(8)]; e = e1 ^ ell(x)
    Ew[0] ^= y; Ew[off(e)] ^= PhiA[y]
    return (e, x ^ Ew[0], tuple(Ew))
def W(s):                                              # the write alone (reader stays)
    e, w, E = s; x = E[0] ^ w; y = P[x]
    Ew = list(E); Ew[0] ^= y; Ew[off(e)] ^= PhiA[y]
    return (e, y, tuple(Ew))
def Winv(s):
    e, y, E1 = s; x = P[y]; Ew = list(E1); Ew[0] ^= y; Ew[off(e)] ^= PhiA[y]
    return (e, x ^ Ew[0], tuple(Ew))
def Shift(s):                                          # the move: re-index the field by P(carry)
    e, w, E = s; x = P[w]
    return (e ^ ell(x), w, tuple(E[r ^ x] for r in range(8)))

bit = lambda v, i: (v >> i) & 1
def QA(s):   # outer planes keep the cell, carry := NOT collision; centre plane cell := collision; partner centre ^= centre carry
    e, w, E = s; c = E[0]; E = list(E); nc = nw = 0
    for i in (0, 1): nc |= bit(c, i) << i; nw |= (bit(c, i) ^ bit(w, i) ^ 1) << i
    nc |= (bit(c, 2) ^ bit(w, 2)) << 2; nw |= bit(w, 2) << 2
    E[0] = nc; E[off(e)] ^= bit(w, 2) << 2
    return (e, nw, tuple(E))
def QB(s):   # outer planes swap cell and carry, both NOTed; centre plane carry := collision ^ answer; partner gets collision (outer) and the answer (centre)
    e, w, E = s; c = E[0]; E = list(E); x = c ^ w; k = 1 ^ ell(x); nc = nw = 0
    for i in (0, 1): nc |= (bit(w, i) ^ 1) << i; nw |= (bit(c, i) ^ 1) << i
    nc |= bit(c, 2) << 2; nw |= (bit(c, 2) ^ bit(w, 2) ^ k) << 2
    E[0] = nc; E[off(e)] ^= (x & 3) | (k << 2)
    return (e, nw, tuple(E))

def local_states():
    for e in (0, 1):
        for w, c0, co in product(range(8), repeat=3):
            E = [0] * 8; E[0] = c0; E[off(e)] = co
            yield (e, w, tuple(E))
rng = random.Random(20261105)
SAMPLE = [(rng.randrange(2), rng.randrange(8), tuple(rng.randrange(8) for _ in range(8))) for _ in range(4000)]
def report(label, ok):
    print(('PASS' if ok else 'FAIL') + '  ' + label)
    return ok
print('library loaded')

ok = True
for n in (2, 3):
    words = [tuple(w) for w in product((0, 1), repeat=n)]
    for perm in permutations(range(2 ** n)):
        f = {words[i]: words[perm[i]] for i in range(2 ** n)}
        S = {x for x in words if f[x] == J(x)}
        faced = {}
        for x in words:
            y = Pw(x + f[x]); faced.setdefault(y[:n], []).append(y[n:])
        program = all(len(v) == 1 for v in faced.values()) and len(faced) == 2 ** n
        ok &= program == all(C(x) in S for x in S)
        if program:
            finv = {v: k for k, v in f.items()}
            ok &= all(faced[u][0] == J(finv[J(u)]) for u in words)
report('A1 faced table is a program iff the self-reading set is NOT-closed, and then equals J f^-1 J (all programs, n = 2, 3)', ok)
ok = True
for n in range(2, 11):
    R = native_ring(n); N = len(R); succ = {R[a]: R[(a + 1) % N] for a in range(N)}
    S = [x for x in R if succ[x] == J(x)]
    rstar = (1,) * (n // 2 - 1) + (0,) + (1,) * (n - n // 2)
    holes = [x for x in S if C(x) not in S]
    ok &= S == [J(rstar)] and holes == [J(rstar)]
report('A2 the native successor has one self-reading step, the seam J(r*) -> r*, so its faced table tears once: hole J(r*), double C J(r*) (n = 2-10)', ok)

def wholes(L, m):
    M = L + 2 * m - 1; h = (M + 1) // 2; out = []
    for left in product((0, 1), repeat=h):
        Wd = left + (left[::-1][1:] if M % 2 else left[::-1])
        if pal(Wd) and all(not pal(Wd[i:i + L]) for i in range(M - L + 1)): out.append(Wd)
    return out
delta = lambda Wd: tuple(a ^ b for a, b in zip(Wd, Wd[1:]))
Phi = lambda Wd: tuple(b ^ Wd[0] for b in delta(Wd))
ok = True; rows = []
for j in range(1, 6):
    for m in range(1, {1: 8, 2: 8, 3: 8, 4: 6, 5: 4}[j]):
        odd, even = wholes(2 * j + 1, m), set(wholes(2 * j, m))
        img = [Phi(Wd) for Wd in odd]; c = len(next(iter(even))) // 2
        ok &= len(set(img)) == len(img) and set(img) == even and all(Wd[0] == Phi(Wd)[c] for Wd in odd)
        rows.append((2 * j, 2 * j + 1, m, len(even)))
report('B1 Phi(W) = delta(W) xor W0 is a bijection odd row -> even row; the even centre is W0 (contact LEN 2-11, every m run)', ok)
print('   counts (L even, L odd, m, wholes):', rows[:7], '...', rows[-3:])

report('C1 the partner cell is written by NOT x on every plane: PhiA(P(x)) = ~x', all(PhiA[P[x]] == x ^ 7 for x in range(8)))
L = list(local_states())
okA = all(QA(QA(s)) == s and QA(W(QA(s))) == Winv(s) for s in L)
okB = all(QB(QB(s)) == s and QB(W(QB(s))) == Winv(s) for s in L)
report(f'C2 QA and QB are involutions and reverse the write on every local state (QA {okA}, QB {okB})', okA and okB)
okH = all(Q(Shift(F(Q(Shift(s))))) == Finv(s) for Q in (QA, QB) for s in SAMPLE)
report('C3 (Q.Shift) F (Q.Shift) = F^-1 for both write mirrors', okH)
keeps = any(all(Q(s)[1] == s[1] for s in SAMPLE) for Q in (QA, QB))
comm = any(all(Q(Shift(s)) == Shift(Q(s)) for s in SAMPLE) for Q in (QA, QB))
report('C4 neither mirror keeps the carry or commutes with the move, so Q.Shift is not an involution', not keeps and not comm)
def involutions8():
    def rec(rest, f):
        if not rest: yield dict(f); return
        a = rest[0]
        f[a] = a; yield from rec(rest[1:], f); del f[a]
        for b in rest[1:]:
            f[a], f[b] = b, a; yield from rec([r for r in rest[1:] if r != b], f); del f[a], f[b]
    yield from rec(list(range(8)), {})
none = True; count = 0
for phi in involutions8():
    count += 1
    Qp = lambda s, phi=phi: (s[0], s[1], tuple(phi[v] for v in s[2]))
    if all(Qp(W(Qp(s))) == Winv(s) for s in SAMPLE[:200]): none = False
report(f'C5 no uniform cell map with the carry kept reverses the write ({count} involutions of the 8 values tried)', none)

SEAL_TEXT = "NEXUS C5 seal: the retained step's mirrors, write and move. Sealed before running c5_mirror.py.\nMachine: the thread's relative v6.2 step (e, w, E[0..7]): x = E[0]^w, y = P(x), E[0]^=y, E[off(e)]^=PhiA(y),\noff(e) = 7 if e = 0 else 3, then e ^= ell(x), w = y, E <- E[r ^ x]. P(c) = c^3 if ell(c) else c^7, ell(c) = c0^c1,\nPhiA(y) = y ^ 4*ell(y). Planes: bits 0,1 = outer (turn always), bit 2 = centre (turns by 1 ^ ell).\nW = the write at the reader (no shift). Shift = re-index by P(w) and e ^= ell(P(w)). F = Shift . W.\nM1  The partner cell is written by NOT(x) on every plane (PhiA(P(x)) = ~x): the coupling never reaches it.\nM2  W is reversed (Q W Q = W^-1, Q^2 = I, every local state) by\n      QA: outer planes R3 (keep cell, carry := NOT collision); centre plane SH (cell := collision, keep carry);\n          partner cell's centre plane ^= centre carry.\n      QB: outer planes R1 (swap cell and carry, both NOTed) and partner cell's outer planes ^= outer collision;\n          centre plane R3 turned by the answer (keep cell, carry := collision ^ (1 ^ ell(x_outer))).\nM3  F (the full step) is reversed by none of Q, Q.Shift, Shift.Q, Q.Shift.Q, Shift.Q.Shift for Q in {QA, QB}:\n    the move reads the collision, and no local mirror of the write meets the move.\nA failed clause is recorded as failed.\n"
print('C5 seal sha256', sha256(SEAL_TEXT.encode()).hexdigest())
assert sha256(SEAL_TEXT.encode()).hexdigest() == 'd6894232eb8e3eed45a2c4b15acbd2bbb46b096dcc2f98c34791a018ecc7daab'
s, t = (0, 1, (0,) * 8), 0
while True:
    s = F(s); t += 1
    if s[2] == (0,) * 8: break
report(f'M0 machine = the thread rel_step: the seed returns to an empty field at t = {t} with e = {s[0]}, w = {s[1]}', (t, s[0], s[1]) == (806, 0, 1))
comp = lambda *fs: (lambda x: _ap(fs, x))
def _ap(fs, x):
    for f in reversed(fs): x = f(x)
    return x
cands = {}
for nm, Q in (('QA', QA), ('QB', QB)):
    cands[nm] = Q; cands[nm + '.Shift'] = comp(Q, Shift); cands['Shift.' + nm] = comp(Shift, Q)
    cands[nm + '.Shift.' + nm] = comp(Q, Shift, Q); cands['Shift.' + nm + '.Shift'] = comp(Shift, Q, Shift)
S2 = SAMPLE[:2000]
res = {nm: (all(R(R(x)) == x for x in S2), all(R(F(R(x))) == Finv(x) for x in S2)) for nm, R in cands.items()}
for nm, (iv, rv) in res.items(): print(f'     {nm:16s} involution {str(iv):5s}  R.F.R = F^-1 {rv}')
report('M3 no listed map is a reversor (an involution with R.F.R = F^-1) of the full step', not any(iv and rv for iv, rv in res.values()))

# measured, unsealed: edge mirrors and read-back mirrors
fs = {'0': lambda w: 0, 'w': lambda w: w, 'Pw': lambda w: P[w], '7': lambda w: 7, 'w7': lambda w: w ^ 7,
      'Pw7': lambda w: P[w] ^ 7, 'wPw': lambda w: w ^ P[w], 'wPw7': lambda w: w ^ P[w] ^ 7}
def edge(f0, f1, f2, f3, swap):
    def R(s):
        e, w, E = s; x = P[w]; e2 = e ^ ell(x); E2 = [E[r ^ x] for r in range(8)]
        a, b, pa, pb = 0, x, off(e2), x ^ off(e)
        if swap: E2[a], E2[b] = E2[b], E2[a]; E2[pa], E2[pb] = E2[pb], E2[pa]
        E2[a] ^= fs[f0](w); E2[b] ^= fs[f1](w); E2[pa] ^= fs[f2](w); E2[pb] ^= fs[f3](w)
        return (e2, w, tuple(E2))
    return R
def holds(R, states): return all(R(R(x)) == x and R(F(R(x))) == Finv(x) for x in states)
edge_hits = [c for c in product(fs, fs, fs, fs, (0, 1)) if holds(edge(*c), SAMPLE[:40]) and holds(edge(*c), S2)]
J3 = tuple(((c & 1) << 2) | (c & 2) | (c >> 2) for c in range(8))
vm = {'I': tuple(range(8)), 'J3': J3, 'C3': tuple(c ^ 7 for c in range(8)), 'P': P, 'J3C3': tuple(J3[c] ^ 7 for c in range(8)),
      'PhJ': tuple(c ^ (3 if ell(c) else 0) for c in range(8)), 'PhA': PhiA, 'PhA0': tuple(c ^ (7 if ell(c) else 0) for c in range(8)),
      'C3PhA': tuple(PhiA[c] ^ 7 for c in range(8))}
def readback(a, b, g, fe, rl):
    A, B, G = vm[a], vm[b], vm[g]
    def R(s):
        e, w, E = s; E2 = [B[E[G[r]]] for r in range(8)]; e2 = e ^ fe
        if rl: x = P[w]; E2 = [E2[r ^ x] for r in range(8)]; e2 ^= ell(x)
        return (e2, A[w], tuple(E2))
    return R
rb_hits = [c for c in product(vm, vm, vm, (0, 1), (0, 1)) if holds(readback(*c), SAMPLE[:30]) and holds(readback(*c), S2)]
def powers_ok():
    for Q in (QA, QB):
        R0 = lambda s, Q=Q: Q(Shift(s))
        for k in (3, 5, 7, 9):
            def Rk(s, k=k, R0=R0):
                for _ in range(k): s = R0(s)
                return s
            if holds(Rk, SAMPLE[:100]): return False
    return True
print(f'measured: edge mirrors {8**4 * 2} tried, reversors {len(edge_hits)}; read-back mirrors {len(vm)**3 * 4} tried, reversors {len(rb_hits)}; '
      f'odd powers of Q.Shift reversing F: {"none" if powers_ok() else "some"}')
```

---

## Entry C7 · 5 Nov 2026 · where the line stands

**Reproduction (RUNS, second environment).** The C6 notebook came back, SHA-256 `f9346ddb61cdc40d1222ed190b20c306f5e2f8252baeefc95a031828e79a9132`, executed under Python 3.11.14. Every output line is identical to the delivered run under Python 3.13.18. The only difference is that two stdout chunks of cell 9 were merged into one. C6 now stands on two environments.

**State of the line.** No new run beyond the reproduction above.

| Address | What stands | Status |
|---|---|---|
| the clock | τ = J·B: two mirrors half a step apart, the NOT on B's site axis, carried round as the twist (τⁿ = C) | STANDS (C4; published core) |
| the half-lap | what σ cannot see closes at L, what σ flips needs 2L; a gap centre reads a difference, a site centre a value | STANDS, one law (C2–C4) |
| teeth | two palindromes half a lap apart on every J-symmetric orbit, because B fixes nothing | STANDS (recovered: symmetric-orbit lemma) |
| tables | facing runs a program backward, J f⁻¹ J, when the self-reading steps pair under NOT; the native successor tears only at the seam | STANDS (C6 A) |
| chains | odd chain: the centre is a contact; even chain: the joint; the equal hinge rows are the centre storing the face bit | STANDS (C5; C6 B) |
| the question | the selector holds one bit of answer, needs three reader states outside-in, and lands on the centre, where facing writes it | recovered (C6 bridge) |
| the write | the coupling bit is the centre's answer; two mirrors, one blind to it and one carrying it; the live answer gives the write its own half-turn | RUNS (C4, C6 C) |
| the step | no readable mirror: the shared write-and-move form is closed by proof; edge and read-back families are empty; the step reads as a mirror twin, with its half-lap on the translation H₁₀₀₁ | STANDS / measured (C6 D) |

**Closed this session.** GPT's two OPEN items: the hinge rows (by Φ), and the plane-2 compensation on the write (by QB). The seam law across LEN (by A8 with A1). Ownership of C2–C3 (recovered, C4).

**OPEN.** One item on the main line: the step's twin. That is the partner P′ whose retained step, under a readable relabelling, is the way home of the v6.2 step, or what forbids one. Off the main line and still standing: the boundary-driven compiler (bind, compose, close) from the facing manual, and the 3-SAT paper's open reader.

---

## Entry C8 · 5 Nov 2026 · built: the boundary compiler (bind, compose, close)

**What was built.** `NEXUS_C8_Boundary_Compiler.ipynb` (SHA-256 `f7d7fd4c3b49bfd7295b2b468def3fd1b1940cb383290d51234f9cf13f3a1b80`), a working compiler for native reversible programs on LEN n. It is the PULL item of the facing manual §14 and Routes B4. You hand it a boundary, the contacts x|y a program must contain, and it runs three stages:
- **BIND** closes the boundary under facing and marks every input face BOUND, UNBOUND (a hole) or AMBIGUOUS (a tear).
- **COMPOSE** counts every native fill of the holes and builds one: at random, or in *rings* mode, with the fewest closed routes.
- **CLOSE** cuts the program into routes and names each route's two centres, a site (a palindrome) or a gap (a self-reading step).

A text front end, `compile_boundary(n, "0001>0010 ...")`, runs all three. Seal C8, `c8_seal.txt`, SHA-256 `4f6485809cde2d790eb88b0adbcd0ee3a3e1092df84ae5381b4866e51c8d9d9b`, was hashed 2026-11-06T00:53:18Z, before the compiler was run. Its text is embedded in the notebook and checked there.

**The one law it runs on.** A program is native exactly when facing carries its table onto itself (C6 A). So a native program is two mirrors, f = J·h.

**Results.**

| Clause | Content | Status |
|---|---|---|
| K1 BIND | a boundary completes natively iff its facing closure is a partial bijection; every conflict is a tear | STANDS; RUNS every boundary at n = 2, 6000 at n = 3 |
| K2 COMPOSE | the fills are f = J·h on the holes, h an involution with a NOT-closed fixed set; there are Σₖ C(c,k)(u−2k−1)!! of them | STANDS (Routes A6); RUNS against brute force |
| K3 CLOSE | each achiral route has two centres where J's axis meets it: one site and one gap if the route is odd, two of one kind half a route apart if even; chiral routes come in mirror pairs with none; #achiral routes = (#palindromes + \|S\|)/2 | STANDS (recovered: symmetric-orbit lemma); RUNS every native at n ≤ 3, random natives to n = 12 |
| K4(a) | no native program at n ≥ 3 is a single ring | STANDS (K3); RUNS |
| K4(b) | the twisted clock has 2^(⌈n/2⌉−1) achiral routes at every n (recovers P30's active orbits) | STANDS; RUNS n = 1–12 |
| K4(c) | bound as a boundary, the native successor tears at 2·2^⌈n/2⌉ input faces | RUNS n = 4–12; **FAILED at n = 3** |
| K5 RINGS | joining open segments and closing only at centres reaches the fewest routes | STANDS (argument); RUNS n = 2, 3, no mismatch in any case |
| fewest routes | every native program has at least 2^(⌈n/2⌉−1) routes; the compiler reaches it with one ring through every non-palindrome, centred on two palindromes, the rest closed in pairs | STANDS (K3 with the construction); RUNS n = 3–12 |
| the repaired successor | keep the successor's facing-carried transitions and fill in rings mode: fewest routes, the long ring through every non-palindrome | measured n = 3–12 |

**Discrepancy (K4(c) at n = 3).** At LEN 3, two of the eight transitions facing does not carry face onto the same input, 001: the seam's NOT face C(110) and the face of 101 → 100, J(100). That leaves seven torn input faces, one of them carrying three outputs. From LEN 4 on, the faced inputs are distinct and the clause holds. It is recorded as failed at n = 3, as sealed.

**Reading.** The successor tears because a single ring is the one thing a native program cannot be. Every palindrome is a centre and a ring has only two. Its tears sit where the palindromes and the seam would have to be centres.

**OPEN.** Unchanged on the main line: the retained step's twin (C7). The compiler binds programs on words, and the step's state space needs its own reading before the compiler can bind it.

### Live output (notebook, executed 5 Nov)

```
compiler loaded
LEN 4: boundary 4 contacts -> closure 8; BOUND 8, UNBOUND 8, AMBIGUOUS 0
  native completions: 120
  routes: 2 (2 achiral, 0 chiral)
   achiral length  14: site 0000, site 1001
   achiral length   2: site 0110, site 1111

LEN 4: boundary 2 contacts -> closure 4; BOUND 4, UNBOUND 12, AMBIGUOUS 0
  native completions: 16336
  routes: 3 (3 achiral, 0 chiral)
   achiral length  11: site 0000, gap 0010->0100
   achiral length   2: site 0110, site 1001
   achiral length   3: site 1111, gap 1101->1011

LEN 4: boundary 2 contacts -> closure 4; BOUND 2, UNBOUND 13, AMBIGUOUS 1
  tears at input faces: ['0100'] 
C8 seal sha256 4f6485809cde2d790eb88b0adbcd0ee3a3e1092df84ae5381b4866e51c8d9d9b
native programs, n = 1, 2, 3: [2, 6, 188]
PASS  K1 a boundary completes natively iff its facing closure is tear-free (every boundary at n = 2; 6000 at n = 3)
PASS  K2 the count formula equals the brute-force count; every compiled fill is native and keeps the boundary
PASS  K3 two centres per achiral route, placed by parity; none on chiral routes; #achiral = (#palindromes + |S|)/2 (every native at n <= 3; random natives to n = 12)
PASS  K4(a) no native program at n = 3 is fewer than two routes
PASS  K4(b) the twisted clock has 2^(ceil(n/2)-1) achiral routes, n = 1-12
FAIL  K4(c) successor tears = transitions facing does not carry = 2*2^ceil(n/2): [(3, 7), (4, 8), (5, 16), (6, 16), (7, 32), (8, 32), (9, 64), (10, 64), (11, 128), (12, 128)]
PASS  K5 rings reaches the fewest routes and makes no mirror pair when a loop-ended segment is free (n = 2, 3; all cases: 0 mismatches)
n= 3: fewest routes   2 | empty boundary ->   2, longest ring 6 (non-palindromes + 2: True) | successor core kept    0, tear-free True, rings ->   2 routes, longest 6, mirror pairs 0
n= 4: fewest routes   2 | empty boundary ->   2, longest ring 14 (non-palindromes + 2: True) | successor core kept    8, tear-free True, rings ->   2 routes, longest 14, mirror pairs 0
n= 5: fewest routes   4 | empty boundary ->   4, longest ring 26 (non-palindromes + 2: True) | successor core kept   16, tear-free True, rings ->   4 routes, longest 26, mirror pairs 0
n= 6: fewest routes   4 | empty boundary ->   4, longest ring 58 (non-palindromes + 2: True) | successor core kept   48, tear-free True, rings ->   4 routes, longest 58, mirror pairs 0
n= 7: fewest routes   8 | empty boundary ->   8, longest ring 114 (non-palindromes + 2: True) | successor core kept   96, tear-free True, rings ->   8 routes, longest 114, mirror pairs 0
n= 8: fewest routes   8 | empty boundary ->   8, longest ring 242 (non-palindromes + 2: True) | successor core kept  224, tear-free True, rings ->   8 routes, longest 242, mirror pairs 0
n= 9: fewest routes  16 | empty boundary ->  16, longest ring 482 (non-palindromes + 2: True) | successor core kept  448, tear-free True, rings ->  16 routes, longest 482, mirror pairs 0
n=10: fewest routes  16 | empty boundary ->  16, longest ring 994 (non-palindromes + 2: True) | successor core kept  960, tear-free True, rings ->  16 routes, longest 994, mirror pairs 0
n=11: fewest routes  32 | empty boundary ->  32, longest ring 1986 (non-palindromes + 2: True) | successor core kept 1920, tear-free True, rings ->  32 routes, longest 1986, mirror pairs 0
n=12: fewest routes  32 | empty boundary ->  32, longest ring 4034 (non-palindromes + 2: True) | successor core kept 3968, tear-free True, rings ->  32 routes, longest 4034, mirror pairs 0

LEN 5: boundary 32 contacts -> closure 48; BOUND 16, UNBOUND 0, AMBIGUOUS 16
  tears at input faces: ['00000', '00010', '00011', '00100', '01001', '01010', '01101', '01110', '10000', '10001', '10100', '10101'] ...
```

### Seal C8 (text)

```
NEXUS C8 seal: the boundary compiler (bind, compose, close). Sealed before the compiler is run.
Words X_n (N = 2^n), J reverse, C NOT. A contact is x|y (LEN 2n); facing P on contacts: (Jy, Jx) if y != Jx,
else (Cx, Cy). A boundary B is a set of required contacts. A program is native iff its table is facing-closed.
K1 BIND. B has a native completion iff its facing closure B u P(B) is a partial bijection (no input face with two
   outputs, no output face with two inputs). Every conflict is a tear.
K2 COMPOSE. For a tear-free boundary with free inputs U: |U| is even, the free outputs are J(U), and the native
   completions are exactly f = J.h on U with h an involution of U whose fixed set is closed under NOT.
   Their number is sum_k binom(c, k) (u - 2k - 1)!!, u = |U|, c = NOT-pairs inside U, (-1)!! = 1.
K3 CLOSE. Every closed route of a native program is achiral or chiral. An achiral route has exactly two centres,
   where its mirror axis J meets it: a site (a palindrome) or a gap (a self-reading step x -> Jx). Odd routes: one
   of each. Even routes: two of one kind, half a route apart. Chiral routes come in mirror pairs and have no centre.
   Hence #achiral routes = (2^ceil(n/2) + |S|)/2, S the self-reading set.
K4 (a) For n >= 3 no native program is a single ring: it has at least 2^(ceil(n/2)-1) routes.
   (b) The twisted clock tau_n has exactly 2^(ceil(n/2)-1) achiral routes, at every n.
   (c) Bound as a boundary, the native successor T_n (n >= 3) has exactly 2*2^ceil(n/2) ambiguous input faces,
       one for each transition that facing does not carry.
K5 RINGS. The threading completion (join open segments, close only at centres) never makes a chiral route when the
   boundary leaves a loop-ended open segment, and then reaches the fewest routes any native completion has.
A failed clause is recorded as failed.
```

### Source (the notebook's code cells, in order)

```python
# ---------------------------------------------------------------- the boundary compiler: bind, compose, close
from itertools import permutations
from math import comb
from collections import defaultdict
import random

class Ring:
    """Words of LEN n as integers, position 0 = most significant bit. J reverse, C NOT, P facing."""
    def __init__(self, n):
        self.n, self.N = n, 1 << n
        self.mask = self.N - 1
        self.Jt = [self._rev(x) for x in range(self.N)]
    def _rev(self, x):
        r = 0
        for _ in range(self.n):
            r = (r << 1) | (x & 1); x >>= 1
        return r
    def J(self, x): return self.Jt[x]
    def C(self, x): return x ^ self.mask
    def pal(self, x): return self.Jt[x] == x
    def P(self, x): return self.C(x) if self.pal(x) else self.J(x)
    def face(self, x, y):
        """facing of the contact x|y (a word of LEN 2n): read backward, or NOT where it reads the same"""
        return (self.C(x), self.C(y)) if y == self.J(x) else (self.J(y), self.J(x))
    def w(self, x): return format(x, f'0{self.n}b')
    def native_ring(self):
        reps = sorted(x for x in range(self.N) if x < self.P(x))
        return reps[:-1] + [self.P(reps[-1]), reps[-1]] + [self.P(x) for x in reversed(reps[:-1])]

class Bound:
    """BIND: close a boundary under facing; every input face is BOUND, UNBOUND (a hole) or AMBIGUOUS (a tear)."""
    def __init__(self, R, contacts):
        self.R = R
        self.boundary = set(contacts)
        self.closure = self.boundary | {R.face(x, y) for x, y in self.boundary}
        outs, ins = defaultdict(set), defaultdict(set)
        for x, y in self.closure: outs[x].add(y); ins[y].add(x)
        self.status = {x: ('BOUND' if len(outs[x]) == 1 else 'UNBOUND' if not outs[x] else 'AMBIGUOUS') for x in range(R.N)}
        self.in_tears = sorted(x for x in range(R.N) if len(outs[x]) > 1)
        self.out_tears = sorted(y for y in range(R.N) if len(ins[y]) > 1)
        self.ok = not self.in_tears and not self.out_tears
        self.table = {x: next(iter(outs[x])) for x in range(R.N) if len(outs[x]) == 1}
        self.free = sorted(x for x in range(R.N) if not outs[x])

def dfact(k):
    r = 1
    while k > 1: r *= k; k -= 2
    return r

def count(b):
    """COMPOSE, counted: native completions = involutions of the holes with a NOT-closed fixed set"""
    assert b.ok
    U = set(b.free); u = len(U); c = sum(1 for x in U if b.R.C(x) in U) // 2
    return sum(comb(c, k) * dfact(u - 2 * k - 1) for k in range(c + 1) if u - 2 * k >= 0)

def segments(b):
    """the alternating J/h graph of the bound part: h = J.f on bound inputs; ends are loops (L) or holes (O)"""
    R = b.R; U = set(b.free); h = {x: R.J(y) for x, y in b.table.items()}
    def slot(v, kind):
        if kind == 'J': return ('L', None) if R.pal(v) else ('E', R.J(v))
        if v in U: return ('O', None)
        return ('L', None) if h[v] == v else ('E', h[v])
    seen, segs = set(), []
    def walk(v0, out_kind):
        verts, v, kind = [v0], v0, out_kind
        while True:
            t, nxt = slot(v, kind)
            if t != 'E': return verts, t, v
            v = nxt; verts.append(v); kind = 'h' if kind == 'J' else 'J'
    for v0 in range(R.N):
        if v0 in seen: continue
        for kind in ('J', 'h'):
            t, _ = slot(v0, kind)
            if t != 'E':                                       # v0 is an end; walk out of its other slot
                other = 'h' if kind == 'J' else 'J'
                verts, t_end, v_end = walk(v0, other)
                seen.update(verts)
                segs.append({'verts': verts, 'start': (t, v0), 'end': (t_end, v_end)})
                break
    cycles = []
    for v0 in range(R.N):
        if v0 in seen: continue
        verts, v, kind = [v0], v0, 'J'
        while True:
            _, nxt = slot(v, kind); kind = 'h' if kind == 'J' else 'J'
            if nxt == v0: break
            verts.append(nxt); v = nxt
        seen.update(verts); cycles.append(verts)
    return segs, cycles, h

def complete(b, mode='rings', rng=None):
    """COMPOSE: give every hole an h-partner. 'rings' joins open segments and closes only at centres."""
    R = b.R; U = b.free; rng = rng or random.Random(0)
    segs, cycles, h = segments(b)
    hh = dict(h)
    def pair(a, c): hh[a] = c; hh[c] = a
    if mode == 'random':
        Us = list(U); rng.shuffle(Us); left = set(Us)
        for x in Us:
            if x in left and R.C(x) in left and rng.random() < 0.3:
                hh[x] = x; hh[R.C(x)] = R.C(x); left -= {x, R.C(x)}
        rest = [x for x in Us if x in left]
        for i in range(0, len(rest), 2): pair(rest[i], rest[i + 1])
    else:
        LO = [s for s in segs if {s['start'][0], s['end'][0]} == {'L', 'O'}]
        OO = [s for s in segs if s['start'][0] == 'O' and s['end'][0] == 'O']
        hole = lambda s: s['start'][1] if s['start'][0] == 'O' else s['end'][1]
        ends = lambda s: (s['start'][1], s['end'][1])
        rest = LO
        if OO:
            if LO:
                cur = hole(LO[0])
                for s in OO:
                    a, c = ends(s); pair(cur, a); cur = c
                pair(cur, hole(LO[1])); rest = LO[2:]
            else:
                where = {}
                for i, s in enumerate(OO):
                    for v in ends(s): where[v] = i
                choice = None
                for x, i in where.items():
                    j = where.get(R.C(x))
                    if j is not None and (j != i or len(OO) == 1): choice = (x, i, R.C(x), j); break
                if choice:
                    x, i, cx, j = choice
                    order = [i] + [k for k in range(len(OO)) if k not in (i, j)] + ([j] if j != i else [])
                    oriented = []
                    for k in order:
                        a, c = ends(OO[k])
                        if k == i and a != x: a, c = c, a
                        if k == j and k != i and c != cx: a, c = c, a
                        oriented.append((a, c))
                    hh[x] = x; hh[cx] = cx                      # a NOT pair of self-reading steps: two gap centres
                    for (a1, c1), (a2, c2) in zip(oriented, oriented[1:]): pair(c1, a2)
                else:
                    oriented = [ends(s) for s in OO]
                    for (a1, c1), (a2, c2) in zip(oriented, oriented[1:]): pair(c1, a2)
                    pair(oriented[-1][1], oriented[0][0])       # no loop end anywhere: close a mirror pair
                rest = []
        for i in range(0, len(rest), 2): pair(hole(rest[i]), hole(rest[i + 1]))
    f = [None] * R.N
    for x, y in b.table.items(): f[x] = y
    for x in U: f[x] = R.J(hh[x])
    return f

def native(R, f):
    """native = the faced table is the table itself (P15.1)"""
    T = {(x, f[x]) for x in range(R.N)}
    return {R.face(x, y) for x, y in T} == T

def close(R, f):
    """CLOSE: every route, achiral or chiral, with its centres (sites = palindromes, gaps = self-reading steps)"""
    seen, routes = [False] * R.N, []
    for x0 in range(R.N):
        if seen[x0]: continue
        cyc, x = [], x0
        while not seen[x]: seen[x] = True; cyc.append(x); x = f[x]
        S = set(cyc)
        routes.append({'cycle': cyc, 'achiral': R.J(cyc[0]) in S,
                       'sites': [i for i, v in enumerate(cyc) if R.pal(v)],
                       'gaps': [i for i, v in enumerate(cyc) if f[v] == R.J(v)]})
    return routes

def centre_law(R, f):
    """K3 on one program: two centres per achiral route, placed by the parity rule; none on chiral routes"""
    rs = close(R, f); S = sum(1 for x in range(R.N) if f[x] == R.J(x)); ok = True
    for r in rs:
        L, s, g = len(r['cycle']), r['sites'], r['gaps']
        if not r['achiral']: ok &= not s and not g; continue
        ok &= len(s) + len(g) == 2
        if L % 2: ok &= len(s) == 1 and len(g) == 1 and (g[0] - s[0]) % L in ((L - 1) // 2,)
        else:
            two = s if len(s) == 2 else g
            ok &= len(two) == 2 and (two[1] - two[0]) % L == L // 2
    ach = sum(1 for r in rs if r['achiral'])
    pal = sum(1 for x in range(R.N) if R.pal(x))
    ok &= 2 * ach == pal + S
    ok &= sum(1 for r in rs if not r['achiral']) % 2 == 0
    return ok, rs

def report(b, f=None, show=12):
    R = b.R; st = b.status
    print(f"LEN {R.n}: boundary {len(b.boundary)} contacts -> closure {len(b.closure)}; "
          f"BOUND {sum(v == 'BOUND' for v in st.values())}, UNBOUND {sum(v == 'UNBOUND' for v in st.values())}, "
          f"AMBIGUOUS {sum(v == 'AMBIGUOUS' for v in st.values())}")
    if not b.ok:
        print('  tears at input faces:', [R.w(x) for x in b.in_tears[:show]], '...' if len(b.in_tears) > show else '')
        return
    print(f"  native completions: {count(b)}")
    if f is not None:
        rs = close(R, f)
        print(f"  routes: {len(rs)} ({sum(r['achiral'] for r in rs)} achiral, {sum(not r['achiral'] for r in rs)} chiral)")
        for r in rs[:show]:
            cyc = r['cycle']
            cen = [f"site {R.w(cyc[i])}" for i in r['sites']] + [f"gap {R.w(cyc[i])}->{R.w(f[cyc[i]])}" for i in r['gaps']]
            print(f"   {'achiral' if r['achiral'] else 'chiral '} length {len(cyc):3d}: " + (', '.join(cen) if cen else 'no centre (mirror twin elsewhere)'))

def parse(n, text):
    """boundary from text: '0001>0010, 0010>0011' (input>output, words of LEN n)"""
    out = []
    for tok in text.replace(',', ' ').split():
        a, c = tok.split('>'); assert len(a) == len(c) == n
        out.append((int(a, 2), int(c, 2)))
    return out

def compile_boundary(n, text_or_contacts, mode='rings', show=12):
    """bind, compose, close in one call; returns (Bound, program or None)"""
    R = Ring(n)
    B = parse(n, text_or_contacts) if isinstance(text_or_contacts, str) else list(text_or_contacts)
    b = Bound(R, B)
    f = complete(b, mode) if b.ok else None
    report(b, f, show)
    if f is not None: assert native(R, f) and all(f[x] == y for x, y in B)
    return b, f

print('compiler loaded')

# ---- next cell ----
compile_boundary(4, '0001>0010 0010>0011 0011>0101 1000>1001'); print()
compile_boundary(4, '0001>0010 0010>0100'); print()
compile_boundary(4, '0001>0010 0100>1001')

# ---- next cell ----
SEAL_TEXT = 'NEXUS C8 seal: the boundary compiler (bind, compose, close). Sealed before the compiler is run.\nWords X_n (N = 2^n), J reverse, C NOT. A contact is x|y (LEN 2n); facing P on contacts: (Jy, Jx) if y != Jx,\nelse (Cx, Cy). A boundary B is a set of required contacts. A program is native iff its table is facing-closed.\nK1 BIND. B has a native completion iff its facing closure B u P(B) is a partial bijection (no input face with two\n   outputs, no output face with two inputs). Every conflict is a tear.\nK2 COMPOSE. For a tear-free boundary with free inputs U: |U| is even, the free outputs are J(U), and the native\n   completions are exactly f = J.h on U with h an involution of U whose fixed set is closed under NOT.\n   Their number is sum_k binom(c, k) (u - 2k - 1)!!, u = |U|, c = NOT-pairs inside U, (-1)!! = 1.\nK3 CLOSE. Every closed route of a native program is achiral or chiral. An achiral route has exactly two centres,\n   where its mirror axis J meets it: a site (a palindrome) or a gap (a self-reading step x -> Jx). Odd routes: one\n   of each. Even routes: two of one kind, half a route apart. Chiral routes come in mirror pairs and have no centre.\n   Hence #achiral routes = (2^ceil(n/2) + |S|)/2, S the self-reading set.\nK4 (a) For n >= 3 no native program is a single ring: it has at least 2^(ceil(n/2)-1) routes.\n   (b) The twisted clock tau_n has exactly 2^(ceil(n/2)-1) achiral routes, at every n.\n   (c) Bound as a boundary, the native successor T_n (n >= 3) has exactly 2*2^ceil(n/2) ambiguous input faces,\n       one for each transition that facing does not carry.\nK5 RINGS. The threading completion (join open segments, close only at centres) never makes a chiral route when the\n   boundary leaves a loop-ended open segment, and then reaches the fewest routes any native completion has.\nA failed clause is recorded as failed.\n'
from hashlib import sha256
print('C8 seal sha256', sha256(SEAL_TEXT.encode()).hexdigest())
assert sha256(SEAL_TEXT.encode()).hexdigest() == '4f6485809cde2d790eb88b0adbcd0ee3a3e1092df84ae5381b4866e51c8d9d9b'
import random
def natives_of(n):
    R = Ring(n); return R, [p for p in permutations(range(R.N)) if native(R, p)]
NAT = {n: natives_of(n) for n in (1, 2, 3)}
print('native programs, n = 1, 2, 3:', [len(NAT[n][1]) for n in (1, 2, 3)])
ok1 = ok2 = True
R2, N2 = NAT[2]; contacts2 = [(x, y) for x in range(4) for y in range(4)]
for m in range(1 << 16):                                   # every boundary at n = 2
    B = [contacts2[i] for i in range(16) if m >> i & 1]; b = Bound(R2, B)
    cons = [f for f in N2 if all(f[x] == y for x, y in B)]
    ok1 &= b.ok == bool(cons)
    if b.ok: ok2 &= count(b) == len(cons)
R3, N3 = NAT[3]; rng = random.Random(5)
for trial in range(6000):                                  # n = 3: arbitrary contacts and pieces of native tables
    if trial % 2: B = [(rng.randrange(8), rng.randrange(8)) for _ in range(rng.randint(1, 10))]
    else:
        f = rng.choice(N3); B = [(x, f[x]) for x in rng.sample(range(8), rng.randint(0, 8))]
    b = Bound(R3, B); cons = [f for f in N3 if all(f[x] == y for x, y in B)]
    ok1 &= b.ok == bool(cons)
    if b.ok:
        ok2 &= count(b) == len(cons)
        for mode in ('random', 'rings'):
            g = complete(b, mode, rng); ok2 &= native(R3, g) and all(g[x] == y for x, y in B)
print(('PASS' if ok1 else 'FAIL') + '  K1 a boundary completes natively iff its facing closure is tear-free (every boundary at n = 2; 6000 at n = 3)')
print(('PASS' if ok2 else 'FAIL') + '  K2 the count formula equals the brute-force count; every compiled fill is native and keeps the boundary')
ok3 = all(centre_law(NAT[n][0], f)[0] for n in (1, 2, 3) for f in NAT[n][1])
for n in range(4, 13):
    R = Ring(n)
    for t in range(6):
        g = complete(Bound(R, []), 'random', random.Random(100 * n + t)); ok3 &= native(R, g) and centre_law(R, g)[0]
print(('PASS' if ok3 else 'FAIL') + '  K3 two centres per achiral route, placed by parity; none on chiral routes; #achiral = (#palindromes + |S|)/2 (every native at n <= 3; random natives to n = 12)')
ok4a = min(len(close(R3, f)) for f in N3) >= 2
ok4b = True
for n in range(1, 13):
    R = Ring(n); tau = [((x << 1) & R.mask) | (1 ^ (x >> (n - 1))) for x in range(R.N)]
    ok4b &= native(R, tau) and sum(r['achiral'] for r in close(R, tau)) == 2 ** ((n + 1) // 2 - 1)
amb = []
for n in range(3, 13):
    R = Ring(n); ring = R.native_ring(); T = {ring[a]: ring[(a + 1) % R.N] for a in range(R.N)}
    b = Bound(R, list(T.items()))
    carried = sum(1 for x, y in T.items() if T.get(R.face(x, y)[0]) == R.face(x, y)[1])
    amb.append((n, len(b.in_tears), R.N - carried, 2 * 2 ** ((n + 1) // 2)))
ok4c = all(a == c == d for _, a, c, d in amb)
print(('PASS' if ok4a else 'FAIL') + '  K4(a) no native program at n = 3 is fewer than two routes')
print(('PASS' if ok4b else 'FAIL') + '  K4(b) the twisted clock has 2^(ceil(n/2)-1) achiral routes, n = 1-12')
print(('PASS' if ok4c else 'FAIL') + '  K4(c) successor tears = transitions facing does not carry = 2*2^ceil(n/2):', [(n, a) for n, a, c, d in amb])
ok5 = True; mism = 0
for (R, NL) in (NAT[2], NAT[3]):
    for trial in range(3000):
        f = rng.choice(NL); B = [(x, f[x]) for x in rng.sample(range(R.N), rng.randint(0, R.N))]
        b = Bound(R, B); best = min(len(close(R, g)) for g in NL if all(g[x] == y for x, y in B))
        g = complete(b, 'rings'); got = len(close(R, g)); segs, cyc, _ = segments(b)
        has_LO = any({s['start'][0], s['end'][0]} == {'L', 'O'} for s in segs)
        if has_LO: ok5 &= got == best and sum(not r['achiral'] for r in close(R, g)) == 2 * len(cyc)
        mism += got != best
print(('PASS' if ok5 else 'FAIL') + f'  K5 rings reaches the fewest routes and makes no mirror pair when a loop-ended segment is free (n = 2, 3; all cases: {mism} mismatches)')

# ---- next cell ----
for n in range(3, 13):
    R = Ring(n)
    g = complete(Bound(R, []), 'rings'); rs = close(R, g); longest = max(len(r['cycle']) for r in rs)
    ring = R.native_ring(); T = {ring[a]: ring[(a + 1) % R.N] for a in range(R.N)}
    core = [(x, y) for x, y in T.items() if T.get(R.face(x, y)[0]) == R.face(x, y)[1]]
    b = Bound(R, core); gr = complete(b, 'rings'); rr = close(R, gr)
    print(f"n={n:2d}: fewest routes {2 ** ((n + 1) // 2 - 1):3d} | empty boundary -> {len(rs):3d}, longest ring {longest} "
          f"(non-palindromes + 2: {longest == R.N - 2 ** ((n + 1) // 2) + 2}) | successor core kept {len(core):4d}, "
          f"tear-free {b.ok}, rings -> {len(rr):3d} routes, longest {max(len(r['cycle']) for r in rr)}, mirror pairs {sum(not r['achiral'] for r in rr) // 2}")
print(); compile_boundary(5, [(x, y) for x, y in (lambda R: (lambda ring: [(ring[a], ring[(a + 1) % R.N]) for a in range(R.N)])(R.native_ring()))(Ring(5))])
```
