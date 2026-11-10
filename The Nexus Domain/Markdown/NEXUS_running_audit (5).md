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

## Entry C9 · 6 Nov 2026 · Gemini's *Native Facing* manuscript checked against the record

**Inputs.** `Native_Facing.docx` (SHA-256 `aee10315d690c7c8…`) and its LaTeX source (`6ee6c68d-attachment.txt`), read in full; every flagged line below is present in the source, so none of them is a rendering artifact. Also the other AI's source-level errata (6 Nov). The record: Facing manual, Routes addendum, Appendix D (P16X/P16Y), the 3-SAT paper, the thread, and C1–C8. Seal C9 (`c9_seal.txt`, SHA-256 `1dcc48fe54c9d1f0a601c869b5a047cc4a3598ffa65ff8c3fa251b8b70c924ca`) was hashed at 2026-11-06T08:00:27Z, before the checks ran. Fifteen of the sixteen sealed items landed. N10's twin count at LEN 1 was sealed as 1 and is 0, because Theorem 11.1 starts at LEN 3; that slip in the seal is recorded as failed. N8 and N9's listed values were measured without a prediction and equal the paper's. Part C (whole-vs-parts tables, Page average, degree ≤ 3 invariants) is measured and unsealed. The paper's own appendix script runs and passes.

**Holds (re-run, or equal to the record).**
- **Section 1.** The facing law, the NOT share and the degree law: the operator, not the printed P₃ polynomial. The ring seam J(r⋆)|r⋆. PTP = T⁻¹. The 2·2^⌈n/2⌉ contact exceptions (n = 2–12). The Page tent, 5.2789 bits and the 0.7211 shortfall. The centre |+⟩. The clock carrying the centre one site per tick. The 1−2⁻ᵏ / 2⁻ᵏ split. The comb table's spacings, offsets and σ distances.
- **Section 2.** The exchange law and hinge chaining (F4, F5). The G1 counts. The k = 2 offset rows. The all-k chaining criterion, the emergent-seam formula, odd-k locking and the Δ pullback.
- **Section 3.** The closed-route table, which equals Routes Table A1 and was re-run to n = 10. The necklace counts, re-run to L = 20. Theorem 3.3, which is C6 A's faced-table law: exhaustive at n = 2, 3, and T_n tears once at n = 2–12.
- **Section 4.** The native criterion and count to n = 5. The program-survey pattern. The 570, 470 and 414 native words. |G_n| = n2ⁿ and the two BFS diameter lists. The copy law. The AGL catalog at LEN 1–4 (2, 5, 11 and 25 interfaces; the LEN-3 and LEN-4 tables equal the computed classes). The predictions12 numbers.
- **Section 5.1–5.2.** The sector, the step and the Fibonacci planes. Burnside: 131,072 / 4,096 / 2,048 / 2,048 fixed points, giving 8,704 classes and orbit sizes 256 × 4, 640 × 8, 7,808 × 16. Twisted Burnside at 22 depths. The eR ledger. The owner (I, 4) = H₁₀₀₁ at t = 806. Rung sizes and locks, and the long families by rung. The degree climb 4, 6, 8, 10, 11, 12, 14, 15, and degree 16 for the vacuum cycle. The move letter counts. The 9-move collapse. The section returns (13 values, never 10), the hits 6, 18, 16, 44, 90, and M₀ of degree 9.

**Wrong.**
1. **§5.3 3-SAT (contradicts the record).**
   - The 3-SAT paper's Theorem 3 says no fixed order is privileged on random 3-SAT; its fixed orders, mirror included, all read at 2^0.43n.
   - 2^0.28n is the per-instance best route (last three sizes), not value-order reading. 2.4 clauses per variable is the best order's worst cut.
   - F_m is the four-clause block family, not an odd mirror family.
   - E_n read in mirror order has width 3 (false, need-0, need-1), not 2.
   - The memory columns evaluate fitted curves; they are not the measured medians.
   - The midpoint cuts at n = 6, 8, 10 are 23.4, 29.1 and 35.8.
   - "Theorems 1.3 and 4.1 explain the exact mechanism" is false: mirror order closes the carry only on mirror-structured webs.
2. **§3.3 "boundary-driven compiler".**
   - The manual's bind/compose/close (item 14.6, built in C8) is replaced by the v3 lazy-frame engine and the v4.1 goal resolver.
   - The record's 30,844 are v3's built-in checks and its 25,204 are Gemma tool-call pair checks; 10,803 appears nowhere in the record.
   - "A reader must exist" does not follow: T_n is a bijection, and the tear belongs to the faced table only.
3. **§5.2 ladder table.**
   - The true rung split is: rung 2 {2:128, 4:64, 6:64, 12:8} plus five long families × 8; rung 3 {2:432, 4:192, 6:1200, 12:288, 14:72, 18:256} plus five × 8.
   - The quotient classes by rung are 24, 504 and 8,176. The rung-1 quotient is 6 × 1 + 3 × 6; the paper's 8 × 1 + 8 × 3 is the C = s count.
   - The totals are 2,816 cycles (not 2,744) and 342 quotient cycles (not 289; the record has 342).
   - The printed rung-2 row holds 10,176 states against 7,936.
4. **Theorem 1.3(iii).** P14.6 failed as sealed (Routes Note A3), yet the paper files the result as "P14.6 STANDS". Its proof also repeats the error that Routes correction 6 removed. The 2⁻ᵏ comes from the poles 0ⁿ and 1ⁿ stepping to 0ⁿ⁻¹1 and 0ⁿ; the disturbed pair spreads over k sites.
5. **Labels.**
   - In the record, P16.1–16.4 are native shift programs, and Appendix D keeps P16X and P16Y separate. The paper reuses P16.1–16.5 for other content.
   - F1 is Theorem 5.1. Theorems 6.1 and 6.2 are F4 and F5, and Theorem 7.1 is K1. F3b and F6 do not exist.
   - C2 is the pairing one offset later, not the even seam.
   - R1 collides with the manual's R1. H1–H4 are the ringdown items. W5 is the value-pair distance.
6. **Smaller, all checked.**
   - The P₃ polynomial is wrong on 6 of 8 words and is not an involution (agrees with the errata).
   - "S_inc = {r⋆}" is false: S_inc = ∅ for n ≥ 3 (Table A5 gives 0 at n = 4). {J(r⋆)} is T's set, not inc's.
   - All-k table, L = 4, 5 at k = 3, 4: the all-direction counts are 26, 38 and 52, 76, the breaks 36, 88 and 72, 176, and the totals 36, 98 and 72, 188. The printed rows grow by a constant 5/3, so they were extrapolated.
   - At χ = 0.68, MΩ_H = 0.196168 and Mκ = 0.211518. The printed 0.196390 and 0.211820 would put the binary line at +1.72%.
   - Laghi et al. used events to 1 Oct 2019, not GWTC-1. The binary comb is survival, not support. P13.4 is a retrodiction ("no grid signature reported").
   - The group is mis-named as hyperoctahedral (agrees with the errata). "Diameter 2(n−1)" is D.2's value for the directed set {C, σ, τ} at n ≥ 2. With {σ, τ} the diameter is 2n−1.
   - The 64-seed split is 8, 4, 4, 4, not 5 each.
   - The second provider at C(x) comes from f⁻¹(CJx).
   - Q_eR flips every step. It is the unique degree ≤ 3 alternating charge, up to complement; no nonconstant invariant of degree ≤ 3 exists.
   - R2's dimension needs the wheel to stay connected without its palindromic contacts; the record states it on that condition.
   - The 3,460,368 native programs at n = 4 are not the 64-element instruction group, which has 24 native elements.
   - Uniqueness on palindromes (agrees with the errata). The hinge axis runs through two bits, so it is not inter-bit.
   - The appendix script checks a subset of what its PASS lines name.
   - No references: 4 ln 2 is Bekenstein–Mukhanov (1995), and Page, Mead, Burnside, Singer, de Bruijn and Kac are recovered.

**Missing (in the record, absent here).**
- C8's BIND/COMPOSE/CLOSE: K1–K5, fewest routes 2^(⌈n/2⌉−1), τ's achiral routes, and K4(c) failing at n = 3.
- The half-lap contract (C2).
- The reader at the centre (Routes A12–A15, P18): b′ = b ⊕ s, signed amplitudes read by squares, ±i at LEN 2, and the sign readout.
- Native shift programs (A9): 2^(2^(n−2)), and maximal-length registers are never native.
- The reading direction as the top address bit (A11, P17).
- C6 B: Φ closes D.5's equal rows. The Δ pullback is 2-to-1 and does not.
- C6 C/D: QA and QB with the plane-2 compensation, the half-reversor identity, the leapfrog route closed, and the step as a mirror twin with half-lap H₁₀₀₁.
- D.2/D.3: the native elements of G_n, (n/2)(2^⌈n/2⌉ + 2^⌈(n+1)/2⌉), checked n = 1–8, and the §181 all-k formulas.
- Seals and hashes, so that sealed landings can be told from post-hoc results.

**On the errata.** Its three text fixes reproduce here, and its coverage and interface notes stand. It stops at §§1 and 4 and misses §3.3, §5.2, §5.3 and the ledger. "The central construction survives" holds for the ring algebra of §§1–4, not for §3.3 or §5.3.

### Live output

```text
# paper appendix script (python3 -I, extracted from the docx)
PASS: Section 1 (F1-F6, C1-C4, P14.4-P14.7, P15.4, GW250114 Comb)
PASS: Section 2 (Theorems 5.1, 6.1, 6.2, G1, G2, P16.3-P16.5)
PASS: Section 3 (R1-R3 Closed Routes, Necklaces, Seam Obstruction)
PASS: Section 4 (P15.1-P15.5, P16.1-P16.2, Two-Address Copy Law, AGL Catalog)
PASS: Section 5 (17-Bit Fixed-Charge Sector, G16 8,704 Classes, 9-Move Collapse, 3-SAT Bridge)

ALL SECTIONS 1-5 VERIFIED: 0 MISMATCHES.
# c9_checks_a.py
N1  true formula (1+w0, 1+w0+w1+w2, 1+w2) equals P3 on all 8 words: True
N1  paper formula differs from P3 on 6/8 words ['001', '011', '100', '101', '110', '111']; paper formula is an involution: False
N2  n= 2: S_inc = ['01']   r* = 01
N2  n= 3: S_inc = []   r* = 011
N2  n= 4: S_inc = []   r* = 1011
N2  n=12: S_inc = []   r* = 111110111111
N2  S_inc is empty for every n = 3..12 (and {01} at n = 2)
N3  faced table: UNBOUND = S - C(S), AMBIGUOUS = C(S) - S, and = J f^-1 J when S is NOT-closed (all 24 + 40,320 bijections): True
N3  second provider of each AMBIGUOUS address C(x) comes from f^-1(C J x): True (34576 cases); paper's "from J(f^-1(C J x))" always a provider: False
N3  native successor n=2..12: S_T = {J(r*)}, hole J(r*), double C J(r*); contact exceptions 2*2^ceil(n/2): True
N4  n= 1: dimZ dimZJ t r defects dimZP tP rP dim(ZP)P = 3 3 3 0 0 3 1 1 2  formula =  paper =
N4  n= 2: dimZ dimZJ t r defects dimZP tP rP dim(ZP)P = 5 5 5 0 0 5 1 2 3  formula =  paper =
N4  n= 3: dimZ dimZJ t r defects dimZP tP rP dim(ZP)P = 9 8 7 1 1 8 4 2 6  formula =  paper =
N4  n= 4: dimZ dimZJ t r defects dimZP tP rP dim(ZP)P = 17 14 11 3 2 15 5 5 10  formula =  paper =
N4  n= 5: dimZ dimZJ t r defects dimZP tP rP dim(ZP)P = 33 24 15 9 3 30 10 10 20  formula =  paper =
N4  n= 6: dimZ dimZJ t r defects dimZP tP rP dim(ZP)P = 65 44 23 21 6 59 13 23 36  formula =  paper =
N4  n= 7: dimZ dimZJ t r defects dimZP tP rP dim(ZP)P = 129 80 31 49 7 122 22 50 72  formula =  paper =
N4  n= 8: dimZ dimZJ t r defects dimZP tP rP dim(ZP)P = 257 152 47 105 14 243 29 107 136  formula =  paper =
N4  n= 9: dimZ dimZJ t r defects dimZP tP rP dim(ZP)P = 513 288 63 225 15 498 46 226 272  formula =  paper n/a
N4  n=10: dimZ dimZJ t r defects dimZP tP rP dim(ZP)P = 1025 560 95 465 30 995 61 467 528  formula =  paper n/a
N4  every closed-route entry equals the GF(2) computation and the formulas: True
N5  L= 1: necklaces 2, achiral 2 (=(p+q)/2: True), seam 2, hinge-only 0, fixed 0 (formula 0)
N5  L= 2: necklaces 3, achiral 3 (=(p+q)/2: True), seam 2, hinge-only 1, fixed 1 (formula 1)
N5  L= 8: necklaces 36, achiral 24 (=(p+q)/2: True), seam 9, hinge-only 15, fixed 4 (formula 4)
N5  L=12: necklaces 352, achiral 96 (=(p+q)/2: True), seam 34, hinge-only 62, fixed 6 (formula 6)
N5  L=16: necklaces 4116, achiral 384 (=(p+q)/2: True), seam 129, hinge-only 255, fixed 12 (formula 12)
N5  L=17: necklaces 7712, achiral 512 (=(p+q)/2: True), seam 512, hinge-only 0, fixed 0 (formula 0)
N5  L=18: necklaces 14602, achiral 768 (=(p+q)/2: True), seam 272, hinge-only 496, fixed 16 (formula 16)
N5  L=19: necklaces 27596, achiral 1024 (=(p+q)/2: True), seam 1024, hinge-only 0, fixed 0 (formula 0)
N5  L=20: necklaces 52488, achiral 1536 (=(p+q)/2: True), seam 516, hinge-only 1020, fixed 20 (formula 20)
N5  achiral count and fixed-necklace formula hold L = 1..20; paper values L = 2..16 match: True
N6  Native(n), n = 1..5: [2, 6, 188, 3460368, 321626829363798272]   (paper/record n=5: 321,626,829,363,798,272 -> True)
N7  NOT   native n=1..12: YYYYYYYYYYYY
N7  sigma native n=1..12: YYYYYYYYYYYY
N7  tau   native n=1..12: YYYYYYYYYYYY
N7  inc   native n=1..12: Y...........
N7  CNOT  native n=1..12: -...........
N7  Gray  native n=1..12: YY..........
N7  |S_tau| at n = 2..12: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];  |S_inc| at n=4: 0
N8  n=3: 1092 words; native 570; reversed word same map 570; palindromic words 78
N8  n=4: 1092 words; native 470; reversed word same map 470; palindromic words 78
N8  n=5: 1092 words; native 414; reversed word same map 414; palindromic words 78
N9  n=1: |G| = 2 (n 2^n = 2); diam directed{C,s,t} = 1 (2n-2 = 0); directed{s,t} = 1; undirected{s,t} = 1; native elements 2 (record D.2 formula 2)
N9  n=2: |G| = 8 (n 2^n = 8); diam directed{C,s,t} = 2 (2n-2 = 2); directed{s,t} = 3; undirected{s,t} = 3; native elements 6 (record D.2 formula 6)
N9  n=3: |G| = 24 (n 2^n = 24); diam directed{C,s,t} = 4 (2n-2 = 4); directed{s,t} = 5; undirected{s,t} = 4; native elements 12 (record D.2 formula 12)
N9  n=4: |G| = 64 (n 2^n = 64); diam directed{C,s,t} = 6 (2n-2 = 6); directed{s,t} = 7; undirected{s,t} = 6; native elements 24 (record D.2 formula 24)
N9  n=5: |G| = 160 (n 2^n = 160); diam directed{C,s,t} = 8 (2n-2 = 8); directed{s,t} = 9; undirected{s,t} = 7; native elements 40 (record D.2 formula 40)
N9  n=6: |G| = 384 (n 2^n = 384); diam directed{C,s,t} = 10 (2n-2 = 10); directed{s,t} = 11; undirected{s,t} = 9; native elements 72 (record D.2 formula 72)
N9  n=7: |G| = 896 (n 2^n = 896); diam directed{C,s,t} = 12 (2n-2 = 12); directed{s,t} = 13; undirected{s,t} = 10; native elements 112 (record D.2 formula 112)
N9  n=8: |G| = 2048 (n 2^n = 2048); diam directed{C,s,t} = 14 (2n-2 = 14); directed{s,t} = 15; undirected{s,t} = 12; native elements 192 (record D.2 formula 192)
N10 L=1: |AGL| = 2, interfaces 2, self-inverse 2, twin pairs 0, signature values 2 (cycles(g) alone 2), GL classes 1
N10 L=2: |AGL| = 24, interfaces 5, self-inverse 5, twin pairs 0, signature values 5 (cycles(g) alone 5), GL classes 3
N10 L=3: |AGL| = 1344, interfaces 11, self-inverse 9, twin pairs 1, signature values 10 (cycles(g) alone 8), GL classes 6
N10 L=4: |AGL| = 322560, interfaces 25, self-inverse 19, twin pairs 3, signature values 22 (cycles(g) alone 19), GL classes 14
N10 L=3: paper table equals computed catalog as a multiset: True
N10 L=4: paper table equals computed catalog as a multiset: True
N15 chi=0.68: M Omega_H = 0.196168, M kappa = 0.211518  (paper quotes 0.196390, 0.211820)
N15 4 ln 2 : spacing 4.45%, N* 5.64, N 6, offset +1.60% (0.33 sigma) | with the paper's quoted constants: N* 5.61, offset +1.72%
N15 4 ln 3 : spacing 7.06%, N* 3.56, N 4, offset +3.11% (0.91 sigma) | with the paper's quoted constants: N* 3.54, offset +3.24%
N15 8 pi   : spacing 40.37%, N* 0.62, N 1, offset +15.24% (10.89 sigma) | with the paper's quoted constants: N* 0.62, offset +15.39%
N15 15.6   : spacing 25.06%, N* 1.00, N 1, offset -0.07% (1.70 sigma) | with the paper's quoted constants: N* 1.00, offset +0.05%
N16 n= 6: m=26, expected crossing clauses 23.4  (paper 21.6)
N16 n= 8: m=34, expected crossing clauses 29.1  (paper 27.6)
N16 n=10: m=43, expected crossing clauses 35.8  (paper 34.4)
N16 n=12: m=51, expected crossing clauses 41.7  (paper 41.7)
N16 n=13: m=55, expected crossing clauses 44.4  (paper 44.4)
N16 n=14: m=60, expected crossing clauses 48.5  (paper 48.5)
N16 n=15: m=64, expected crossing clauses 51.2  (paper 51.2)
N16 n=16: m=68, expected crossing clauses 54.4  (paper 54.4)
N16 E_4: binary peak 4 (2^(n/2) = 4), mirror peak 3, mirror profile [1, 2, 2, 3, 2]
N16 E_6: binary peak 8 (2^(n/2) = 8), mirror peak 3, mirror profile [1, 2, 2, 3, 2, 3, 2]
N16 E_8: binary peak 16 (2^(n/2) = 16), mirror peak 3, mirror profile [1, 2, 2, 3, 2, 3, 2, 3, 2]
N16 E_10: binary peak 32 (2^(n/2) = 32), mirror peak 3, mirror profile [1, 2, 2, 3, 2, 3, 2, 3, 2, 3, 2]
N16 E_12: binary peak 64 (2^(n/2) = 64), mirror peak 3, mirror profile [1, 2, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2]
# c9_checks_b.py
sector states 131072
F is a bijection on the sector and keeps the charge: True
G16 commutes with F: True
fixed points: (I,0)=131072, (I,3)=0, (I,4)=0, (I,7)=0, (J,0)=4096, (J,3)=0, (J,4)=0, (J,7)=0, (A,0)=2048, (A,3)=0, (A,4)=0, (A,7)=0, (A0,0)=2048, (A0,3)=0, (A0,4)=0, (A0,7)=0
Burnside classes 8704; orbit-size distribution {4: 256, 8: 640, 16: 7808}; classes counted 8704
full sector: 2816 cycles over 16 lengths: {2: 576, 4: 256, 6: 1280, 12: 296, 14: 72, 18: 256, 30: 8, 94: 8, 98: 8, 132: 8, 212: 8, 434: 8, 1612: 8, 2260: 8, 3948: 8, 5186: 8}
quotient: 8704 classes, 342 cycles: {1: 96, 2: 4, 3: 96, 4: 16, 6: 65, 7: 1, 12: 18, 14: 4, 15: 1, 18: 32, 47: 1, 49: 1, 66: 1, 106: 1, 217: 1, 806: 1, 1130: 1, 1974: 1, 2593: 1}
|R| = 4096, |L| = 4096, |R & L| = 128, R invariant True, L invariant True
rung 1: 128 states, 32 cycles {2: 16, 6: 16}
        quotient 24 classes, 9 cycles {1: 6, 6: 3}
rung 2: 7936 states, 304 cycles {2: 128, 4: 64, 6: 64, 12: 8, 30: 8, 94: 8, 98: 8, 212: 8, 434: 8}
        quotient 504 classes, 31 cycles {1: 14, 2: 2, 4: 4, 6: 6, 15: 1, 47: 1, 49: 1, 106: 1, 217: 1}
rung 3: 123008 states, 2480 cycles {2: 432, 4: 192, 6: 1200, 12: 288, 14: 72, 18: 256, 132: 8, 1612: 8, 2260: 8, 3948: 8, 5186: 8}
        quotient 8176 classes, 302 cycles {1: 76, 2: 2, 3: 96, 4: 12, 6: 56, 7: 1, 12: 18, 14: 4, 18: 32, 66: 1, 806: 1, 1130: 1, 1974: 1, 2593: 1}
paper rung-2 table holds 10176 states (rung 2 has 7936); paper rung-3 table holds 120768 (rung 3 has 123008)
indicator degrees: R 5, L 5, R^L 5, R&L 10, unlocked 10
degree of F^t (lab, 17 bits): {1: 4, 2: 6, 3: 8, 4: 10, 5: 11, 6: 12, 8: 14, 12: 15}
vacuum seed cycle length 1612; indicator degree 16
F^806(seed) = g . seed for g in [('I', 4)]; moves letter counts [89, 132, 114, 66, 107, 114, 108, 76]
cyclic factor complexity L=1..5: [8, 64, 327, 562, 689]; zlib(level 9) 351 bytes
cylinder sizes under the first 9 moves: [16384, 2048, 256, 32, 32, 4, 4, 4, 4, 1]
Q_eR flips every step: True; Q_eR(g.s) = Q_eR(s) ^ h0 for all g: True
twisted Burnside #Fix(Q^t) = (1/16) sum_g #{F^t s = g s} at 22 depths: True
|S| = 1024; return times {1: 256, 2: 160, 3: 192, 4: 88, 5: 56, 6: 56, 7: 80, 8: 32, 9: 32, 11: 32, 12: 16, 13: 8, 14: 16}
R cycles (length, hits on S): count {(2, 2): 80, (4, 2): 32, (6, 2): 48, (12, 2): 4, (30, 6): 4, (94, 18): 4, (98, 16): 4, (212, 44): 4, (434, 90): 4}
degree of the first-return map M0 on 10 bits: 9
64-seed index: 20 seeds fixed by some tau; per phi {'I': 8, 'J': 4, 'A': 4, 'A0': 4}
witness seed A=(0,eR), B=(u,u^eL): tau = H_u Phi_A J_swap fixes it: True
# c9_checks_c.py
G1 n=2: whole != parts on 32 paths; formula 2N(N-1)+r(N-1)+(N-r) = 32
G1 n=3: whole != parts on 144 paths; formula 2N(N-1)+r(N-1)+(N-r) = 144
G1 n=4: whole != parts on 552 paths; formula 2N(N-1)+r(N-1)+(N-r) = 552
allk L=3 k=2: (all-dir, all-pal, breaks, emergent, lone, total) = (4, 4, 8, 2, 2, 12)  paper (4, 4, 8, 2, 2, 12)  =
allk L=3 k=3: (all-dir, all-pal, breaks, emergent, lone, total) = (4, 4, 24, 0, 0, 24)  paper (4, 4, 24, 0, 0, 24)  =
allk L=3 k=4: (all-dir, all-pal, breaks, emergent, lone, total) = (4, 4, 56, 2, 2, 60)  paper (4, 4, 56, 2, 2, 60)  =
allk L=4 k=2: (all-dir, all-pal, breaks, emergent, lone, total) = (18, 2, 12, 6, 0, 18)  paper (18, 2, 12, 6, 0, 18)  =
allk L=4 k=3: (all-dir, all-pal, breaks, emergent, lone, total) = (26, 2, 36, 0, 0, 36)  paper (30, 2, 32, 0, 0, 32)  DIFFERS
allk L=4 k=4: (all-dir, all-pal, breaks, emergent, lone, total) = (38, 2, 88, 10, 0, 98)  paper (50, 2, 76, 10, 0, 86)  DIFFERS
allk L=5 k=2: (all-dir, all-pal, breaks, emergent, lone, total) = (36, 4, 24, 6, 2, 32)  paper (36, 4, 24, 6, 2, 32)  =
allk L=5 k=3: (all-dir, all-pal, breaks, emergent, lone, total) = (52, 4, 72, 0, 0, 72)  paper (60, 4, 64, 0, 0, 64)  DIFFERS
allk L=5 k=4: (all-dir, all-pal, breaks, emergent, lone, total) = (76, 4, 176, 10, 2, 188)  paper (100, 4, 152, 10, 2, 164)  DIFFERS
Page average for a 64x64 split: 5.2789 bits; shortfall from 6: 0.7211
degree<=3 invariants of F: 834 monomials, rank 833, invariant space dimension 1 (1 = constants only)
```

### Seal C9 (text)

```text
NEXUS C9 seal: checks on Native_Facing.docx (Gemini's unified manuscript). Written before any of these checks ran.
Record = Facing manual, Routes addendum, Expanded P16X/P16Y with Appendix D, 3-SAT paper, thread, running audit C1-C8.

N1  P3 coordinates. True P3(w0,w1,w2) = (1+w0, 1+w0+w1+w2, 1+w2). The paper's (1+w0+w2, 1+w0+w1+w2, 1+w0)
    disagrees with P3 on 6 of 8 words and is not an involution.
N2  Self-reading set of the increment x -> x+1: S = {} for every n = 3..12 (and {01} at n = 2). The paper's
    "S_inc = {r*} at n >= 3" is false; the singleton {J(r*)} belongs to the native successor T.
N3  Faced-table law (paper Thm 3.3): holds on every bijection at n = 2, 3 (exhaustive), with UNBOUND set S - C(S)
    and AMBIGUOUS set C(S) - S; for T_n: S_T = {J(r*)}, hole J(r*), double C J(r*), n = 2..12.
N4  Closed routes: every entry of the paper's R1/R2 table equals a direct GF(2) computation, n = 1..8
    (dim Z, dim Z^J, t, r, dim Z^P, t^P, r^P, dim (Z^P)^P).
N5  Necklaces: achiral count (p+q)/2 and the fixed-necklace formula hold for L = 1..20.
N6  Native count n = 5 equals 321,626,829,363,798,272.
N7  Program survey (P15.2) agrees with the record's Table A5 pattern for n = 1..12: NOT, sigma, tau native at
    every n; increment only n = 1; Gray only n = 1, 2; CNOT never (n >= 2); |S_tau| = 0.
N8  P15.3 native words among the 1,092 words of length 1..6 over {C, sigma, tau}: counts at n = 3, 4, 5 are
    measured here; no prediction of the numbers 570 / 470 / 414.
N9  Group <C, sigma, tau> has order n 2^n (n = 1..8). Directed Cayley diameter with {C, sigma, tau} is 1 at n = 1
    and 2n - 2 for n >= 2 (record D.2). The paper's "diameter 2(n-1)" is stated for a set without C; its listed
    BFS values (1,3,4,6,7,9 undirected {s^+-1, t^+-1}; 1,3,5,7,9,11 directed {s, t}) are measured here, no prediction.
N10 AGL(L,2) interfaces 2, 5, 11, 25 at L = 1..4; 1, 0, 1, 3 twin pairs; motion signature 2, 5, 10, 22 values.
    The paper's LEN-3 and LEN-4 tables equal the computed classes as a multiset of (size, order, cycles g, cycles Dg).
N11 Two-reader sector (17 bits, C = u): F is a bijection that conserves the charge and commutes with G16.
    Burnside fixed counts are 131072, 4096, 2048, 2048 and twelve zeros; 8,704 classes; orbit sizes 256 x 4,
    640 x 8, 7,808 x 16. The quotient has 342 cycles (record), not 289. The vacuum seed lies on a 1,612-cycle and
    F^806(seed) = g . seed with g a pure translation (record owner H1001).
N12 Rungs: |R| = |L| = 4096, |R n L| = 128, rung 2 = 7,936 states. The paper's rung-2 and rung-3 full-sector
    cycle multiplicities do not sum to their rung sizes; the computed spectra differ from the paper's table.
N13 The 64-seed count: 20 of 64 seeds are fixed by some reader-exchange tau; split 8, 4, 4, 4 over I, J, A, A0
    (not 5 each).
N14 Degree: F has algebraic degree 4 on 17 bits; the vacuum 1,612-cycle indicator has degree 16; move-letter counts
    on the 806 route are measured here (paper: 89, 132, 114, 66, 107, 114, 108, 76).
N15 Comb: at chi = 0.68, M Omega_H = 0.196168 and M kappa = 0.211518; the paper's quoted 0.196390 and 0.211820
    do not belong to chi = 0.68 and, used as quoted, put the binary N = 6 line near +1.72%, not +1.60%.
N16 3-SAT midpoint-cut column: exact expectations at n = 6, 8, 10 are 23.4, 29.1, 35.8 (paper: 21.6, 27.6, 34.4);
    n = 12..16 rows match. E_n in mirror order has width 3 (false, need-0, need-1), not 2.
```

### Source (`c9_checks_a.py`)

```python
# C9 checks, part A: words, rings, programs, closed routes, necklaces, groups, AGL catalog, comb, 3-SAT table.
# Independent of the paper's appendix script. Sealed predictions: work/referee/nf-r1/c9/c9_seal.txt.
import itertools, math, sys
from collections import Counter

out = []
def say(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)

def J(x, n): return int(format(x, f'0{n}b')[::-1], 2) if n else 0
def C(x, n): return x ^ ((1 << n) - 1)
def pal(x, n): return J(x, n) == x
def P(x, n): return C(x, n) if pal(x, n) else J(x, n)
def bits(x, n): return [(x >> (n - 1 - i)) & 1 for i in range(n)]       # w0 = MSB
def unbits(b): return int(''.join(map(str, b)), 2)

def native_ring(n):
    reps = sorted(w for w in range(1 << n) if w < P(w, n))
    reps[-1] = P(reps[-1], n)
    return reps + [P(r, n) for r in reversed(reps)]
def rstar(n): return int('1' * (n // 2 - 1) + '0' + '1' * ((n + 1) // 2), 2)

# ---------------------------------------------------------------- N1  P3 coordinates
true_ok = all(unbits([1 ^ b[0], 1 ^ b[0] ^ b[1] ^ b[2], 1 ^ b[2]]) == P(w, 3) for w in range(8) for b in [bits(w, 3)])
gem = {w: unbits([1 ^ b[0] ^ b[2], 1 ^ b[0] ^ b[1] ^ b[2], 1 ^ b[0]]) for w in range(8) for b in [bits(w, 3)]}
diff = [format(w, '03b') for w in range(8) if gem[w] != P(w, 3)]
inv = all(gem[gem[w]] == w for w in range(8))
say(f'N1  true formula (1+w0, 1+w0+w1+w2, 1+w2) equals P3 on all 8 words: {true_ok}')
say(f'N1  paper formula differs from P3 on {len(diff)}/8 words {diff}; paper formula is an involution: {inv}')

# ---------------------------------------------------------------- N2  self-reading set of the increment
for n in range(2, 13):
    S = [x for x in range(1 << n) if (x + 1) % (1 << n) == J(x, n)]
    if n <= 4 or n == 12: say(f'N2  n={n:2d}: S_inc = {[format(x, f"0{n}b") for x in S]}   r* = {format(rstar(n), f"0{n}b")}')
    assert (S == [1] if n == 2 else S == [])
say('N2  S_inc is empty for every n = 3..12 (and {01} at n = 2)')

# ---------------------------------------------------------------- N3  faced-table law
def faced_table(f, n):
    addr = {}
    for x in range(1 << n):
        y = f[x]
        if y == J(x, n): a, v = C(x, n), C(y, n)
        else: a, v = J(y, n), J(x, n)
        addr.setdefault(a, []).append((v, x))
    return addr
ok = True; src_ok = True; src_paper = True; checked = 0
for n in (2, 3):
    N = 1 << n
    for f in itertools.permutations(range(N)):
        S = {x for x in range(N) if f[x] == J(x, n)}
        CS = {C(x, n) for x in S}
        ft = faced_table(f, n)
        unb = {z for z in range(N) if z not in ft}
        amb = {z for z, v in ft.items() if len(v) == 2}
        ok &= unb == (S - CS) and amb == (CS - S) and all(len(v) <= 2 for v in ft.values())
        finv = {f[x]: x for x in range(N)}
        if S == CS:
            ok &= all(len(ft[z]) == 1 and ft[z][0][0] == J(finv[J(z, n)], n) for z in range(N))
        for x in S - {C(z, n) for z in S}:              # uncompensated: C(x) not in S
            provs = sorted(src for (v, src) in ft[C(x, n)])
            src_ok &= provs == sorted([x, finv[C(J(x, n), n)]])
            src_paper &= J(finv[C(J(x, n), n)], n) in provs
            checked += 1
say(f'N3  faced table: UNBOUND = S - C(S), AMBIGUOUS = C(S) - S, and = J f^-1 J when S is NOT-closed (all 24 + 40,320 bijections): {ok}')
say(f'N3  second provider of each AMBIGUOUS address C(x) comes from f^-1(C J x): {src_ok} ({checked} cases); paper\'s "from J(f^-1(C J x))" always a provider: {src_paper}')
ok = True
for n in range(2, 13):
    R = native_ring(n); N = 1 << n; T = [0] * N
    for i in range(N): T[R[i]] = R[(i + 1) % N]
    S = {x for x in range(N) if T[x] == J(x, n)}
    ft = faced_table(T, n)
    ok &= S == {J(rstar(n), n)} and [z for z in range(N) if z not in ft] == [J(rstar(n), n)] \
        and [z for z, v in ft.items() if len(v) == 2] == [C(J(rstar(n), n), n)]
    # contact-level exceptions (P15.4)
    E = {(R[i] << n) | R[(i + 1) % N] for i in range(N)}
    exc = [i for i in range(N) if P((R[i] << n) | R[(i + 1) % N], 2 * n) not in E]
    ok &= len(exc) == 2 * 2 ** ((n + 1) // 2)
say(f'N3  native successor n=2..12: S_T = {{J(r*)}}, hole J(r*), double C J(r*); contact exceptions 2*2^ceil(n/2): {ok}')

# ---------------------------------------------------------------- N4  closed routes (GF(2) ranks)
def rank_gf2(rows):
    basis = {}
    r = 0
    for v in rows:
        while v:
            lb = v.bit_length() - 1
            if lb in basis: v ^= basis[lb]
            else: basis[lb] = v; r += 1; break
    return r
paper_tab = {1: (3, 2, 2, 3, 3, 0, 0, 3, 1, 1, 2), 2: (5, 2, 4, 5, 5, 0, 0, 5, 1, 2, 3), 3: (9, 4, 4, 8, 7, 1, 1, 8, 4, 2, 6),
             4: (17, 4, 8, 14, 11, 3, 2, 15, 5, 5, 10), 5: (33, 8, 8, 24, 15, 9, 3, 30, 10, 10, 20),
             6: (65, 8, 16, 44, 23, 21, 6, 59, 13, 23, 36), 7: (129, 16, 16, 80, 31, 49, 7, 122, 22, 50, 72),
             8: (257, 16, 32, 152, 47, 105, 14, 243, 29, 107, 136)}
all_ok = True
for n in range(1, 11):
    NE = 1 << (n + 1); NV = 1 << n; mask = NV - 1
    # each matrix given as rows over the edge index (bit e = coefficient of edge e)
    d_rows = [0] * NV
    for e in range(NE):
        d_rows[e >> 1] ^= 1 << e; d_rows[e & mask] ^= 1 << e
    Jp = [J(e, n + 1) for e in range(NE)]; Pp = [P(e, n + 1) for e in range(NE)]
    def perm_rows(pm):          # rows of (I + M) where M is the permutation matrix of pm (z -> z o pm^-1 as chains)
        return [(1 << e) ^ (1 << pm[e]) for e in range(NE) if pm[e] != e]
    dP_rows = [0] * NV         # rows of d . P : edge e contributes to vertices of P(e)
    for e in range(NE):
        f = Pp[e]
        dP_rows[f >> 1] ^= 1 << e; dP_rows[f & mask] ^= 1 << e
    rk_d = rank_gf2(d_rows)
    dimZ = NE - rk_d
    dimZJ = NE - rank_gf2(d_rows + perm_rows(Jp))
    dimZP = NE - rank_gf2(d_rows + dP_rows)
    dimZPP = NE - rank_gf2(d_rows + perm_rows(Pp))
    p = 2 ** ((n + 1) // 2); q = 2 ** ((n + 2) // 2); ev = 1 if n % 2 == 0 else 0
    rJ = dimZ - dimZJ; tJ = dimZJ - rJ; rP = dimZP - dimZPP; tP = dimZP - 2 * rP
    # disjoint 4-face defects
    defects = []
    for e in range(NE):
        if pal(e, n + 1) and e < C(e, n + 1):
            u = e >> 1; s = {u} ^ {J(u, n)} if False else None
            pts = Counter([u, J(u, n), C(u, n), C(J(u, n), n)])
            supp = frozenset(x for x, c in pts.items() if c % 2)
            if supp: defects.append(supp)
    nd = len(defects)
    row = (dimZ, p, q, dimZJ, tJ, rJ, nd, dimZP, tP, rP, dimZPP)
    form = (2 ** n + 1, p, q, (2 ** n + p + q) // 2, p + q - 1, (2 ** n + 2 - p - q) // 2, q // 2 - 1 - ev,
            2 ** n - q // 2 + 2 + ev, p + q // 2 - 2 - ev, (2 ** n + 2 - p - q) // 2 + 1 + ev, (2 ** n + p) // 2)
    okrow = row == form and (n not in paper_tab or paper_tab[n] == row)
    all_ok &= okrow
    say(f'N4  n={n:2d}: dimZ dimZJ t r defects dimZP tP rP dim(ZP)P = {row[0]} {row[3]} {row[4]} {row[5]} {row[6]} {row[7]} {row[8]} {row[9]} {row[10]}'
        f'  formula {"=" if row == form else "!="}  paper {"=" if paper_tab.get(n) == row else ("n/a" if n not in paper_tab else "!=")}')
say(f'N4  every closed-route entry equals the GF(2) computation and the formulas: {all_ok}')

# ---------------------------------------------------------------- N5  necklaces L = 1..20 (numpy)
import numpy as np
def neck_stats(L):
    N = 1 << L; w = np.arange(N, dtype=np.int64); m = N - 1
    def canon(a):
        best = a.copy(); cur = a.copy()
        for _ in range(L - 1):
            cur = ((cur << 1) & m) | (cur >> (L - 1)); np.minimum(best, cur, out=best)
        return best
    # reversal of every word
    rev = np.zeros(N, dtype=np.int64)
    for i in range(L): rev |= ((w >> i) & 1) << (L - 1 - i)
    cw = canon(w); cr = canon(rev); cc = canon(w ^ m)
    reps = (cw == w)
    achiral = reps & (cr == w)
    ispal = (rev == w)
    has_pal = np.zeros(N, dtype=bool); has_pal[cw[ispal]] = True
    fixed = achiral & (cc == w)
    return int(reps.sum()), int(achiral.sum()), int((achiral & has_pal).sum()), int((achiral & ~has_pal).sum()), int(fixed.sum())
def fixed_formula(L):
    if L % 2: return 0
    a, k = 0, L
    while k % 2 == 0: a += 1; k //= 2
    return sum(2 ** (-(-(2 ** b * k) // 2) - 1) for b in range(a))
paper_fix = {2: 1, 4: 2, 6: 2, 8: 4, 10: 4, 12: 6, 14: 8, 16: 12}
ok = True
for L in range(1, 21):
    nk, ach, seam, hinge, fx = neck_stats(L)
    p = 2 ** ((L + 1) // 2); q = 2 ** ((L + 2) // 2)
    good = ach == (p + q) // 2 and fx == fixed_formula(L) and (L % 2 == 0 or hinge == 0) and (L not in paper_fix or paper_fix[L] == fx)
    ok &= good
    if L in (1, 2, 8, 12, 16, 17, 18, 19, 20): say(f'N5  L={L:2d}: necklaces {nk}, achiral {ach} (=(p+q)/2: {ach == (p + q) // 2}), seam {seam}, hinge-only {hinge}, fixed {fx} (formula {fixed_formula(L)})')
say(f'N5  achiral count and fixed-necklace formula hold L = 1..20; paper values L = 2..16 match: {ok}')

# ---------------------------------------------------------------- N6  native count
def dfact(m):
    r = 1
    while m > 1: r *= m; m -= 2
    return r
cnt = [sum(math.comb(2 ** (n - 1), k) * dfact(2 ** n - 2 * k - 1) for k in range(2 ** (n - 1) + 1)) for n in range(1, 6)]
say(f'N6  Native(n), n = 1..5: {cnt}   (paper/record n=5: 321,626,829,363,798,272 -> {cnt[4] == 321626829363798272})')

# ---------------------------------------------------------------- N7  program survey
def native_map(f, n):
    N = 1 << n
    finv = [0] * N
    for x in range(N): finv[f[x]] = x
    jfj = all(J(f[J(x, n)], n) == finv[x] for x in range(N))
    S = {x for x in range(N) if f[x] == J(x, n)}
    return jfj and all(C(x, n) in S for x in S), len(S)
def progs(n):
    N = 1 << n; m = N - 1
    sig = [((x << 1) & m) | (x >> (n - 1)) for x in range(N)]
    tau = [((x << 1) & m) | (1 ^ (x >> (n - 1))) for x in range(N)]
    inc = [(x + 1) % N for x in range(N)]
    cnot = [x ^ ((x & 1) << (n - 1)) for x in range(N)]
    gray = [0] * N
    for i in range(N): gray[i ^ (i >> 1)] = ((i + 1) % N) ^ (((i + 1) % N) >> 1)
    nt = [C(x, n) for x in range(N)]
    return {'NOT': nt, 'sigma': sig, 'tau': tau, 'inc': inc, 'CNOT': cnot, 'Gray': gray}
pattern = {k: '' for k in ('NOT', 'sigma', 'tau', 'inc', 'CNOT', 'Gray')}
for n in range(1, 13):
    for k, f in progs(n).items():
        if len(set(f)) < len(f): pattern[k] += '-'; continue
        pattern[k] += 'Y' if native_map(f, n)[0] else '.'
for k, v in pattern.items(): say(f'N7  {k:5s} native n=1..12: {v}')
say(f'N7  |S_tau| at n = 2..12: {[native_map(progs(n)["tau"], n)[1] for n in range(2, 13)]};  |S_inc| at n=4: {native_map(progs(4)["inc"], 4)[1]}')

# ---------------------------------------------------------------- N8  P15.3 instruction words
def compose_word(word, gens, N):
    f = list(range(N))
    for g in word: f = [gens[g][y] for y in f]        # g1 applied first
    return tuple(f)
for n in (3, 4, 5):
    N = 1 << n; pr = progs(n); gens = {'C': pr['NOT'], 's': pr['sigma'], 't': pr['tau']}
    words = [w for L in range(1, 7) for w in itertools.product('Cst', repeat=L)]
    nat = sum(1 for w in words if native_map(compose_word(w, gens, N), n)[0])
    revsame = sum(1 for w in words if compose_word(w, gens, N) == compose_word(w[::-1], gens, N))
    pals = sum(1 for w in words if w == w[::-1])
    say(f'N8  n={n}: {len(words)} words; native {nat}; reversed word same map {revsame}; palindromic words {pals}')

# ---------------------------------------------------------------- N9  group <C, sigma, tau>, diameters
def bfs_diam(gens, N):
    start = tuple(range(N)); dist = {start: 0}; frontier = [start]; d = 0
    while frontier:
        nxt = []
        for f in frontier:
            for g in gens:
                h = tuple(g[y] for y in f)
                if h not in dist: dist[h] = d + 1; nxt.append(h)
        if nxt: d += 1
        frontier = nxt
    return len(dist), d, dist
for n in range(1, 9):
    N = 1 << n; pr = progs(n)
    inv = lambda f: tuple(sorted(range(N), key=lambda x: f[x]))
    c, s, t = tuple(pr['NOT']), tuple(pr['sigma']), tuple(pr['tau'])
    o1, dCst, dist = bfs_diam([c, s, t], N)
    o2, dst, _ = bfs_diam([s, t], N)
    o3, dpm, _ = bfs_diam([s, t, inv(s), inv(t)], N)
    natG = sum(1 for f in dist if native_map(f, n)[0])
    formG = (n * (2 ** ((n + 1) // 2) + 2 ** ((n + 2) // 2))) // 2
    say(f'N9  n={n}: |G| = {o1} (n 2^n = {n * 2 ** n}); diam directed{{C,s,t}} = {dCst} (2n-2 = {2 * n - 2}); '
        f'directed{{s,t}} = {dst}; undirected{{s,t}} = {dpm}; native elements {natG} (record D.2 formula {formG})')

# ---------------------------------------------------------------- N10 AGL(L,2) catalog
def cyc_type(perm):
    seen = [False] * len(perm); t = []
    for i in range(len(perm)):
        if not seen[i]:
            l = 0; j = i
            while not seen[j]: seen[j] = True; j = perm[j]; l += 1
            t.append(l)
    return tuple(sorted(t))
def order(perm):
    return math.lcm(*cyc_type(perm))
def gl_elements(L):
    N = 1 << L; els = []
    for cols in itertools.product(range(1, N), repeat=L):
        # linear map with A e_i = cols[i], e_i = bit (L-1-i)?  use integer bit i -> cols[i]
        img = [0] * N
        for x in range(N):
            v = 0
            for i in range(L):
                if (x >> i) & 1: v ^= cols[i]
            img[x] = v
        if len(set(img)) == N: els.append(tuple(img))
    return els
def comp(f, g): return tuple(f[g[x]] for x in range(len(g)))   # f o g
def pinv(f):
    r = [0] * len(f)
    for x, y in enumerate(f): r[y] = x
    return tuple(r)
cat = {}
for L in range(1, 5):
    N = 1 << L; G = gl_elements(L); Gi = {g: pinv(g) for g in G}
    seen = set(); classes = []
    for A in G:
        if A in seen: continue
        orbit = {}; cent = []
        for g in G:
            B = comp(comp(g, A), Gi[g])
            if B == A: cent.append(g)
            orbit.setdefault(B, g)
        seen |= set(orbit); classes.append((A, orbit, cent))
    inter = []
    for A, orbit, cent in classes:
        im = {A[x] ^ x for x in range(N)}
        left = set(range(N)); borbs = []
        while left:
            b0 = min(left); orb = set(); stack = [b0]
            while stack:
                b = stack.pop()
                if b in orb: continue
                orb.add(b)
                for g in cent: stack.append(g[b])
                for v in im: stack.append(b ^ v)
            left -= orb; borbs.append(orb)
        for orb in borbs:
            b = min(orb); g = tuple(A[x] ^ b for x in range(N))
            inter.append({'A': A, 'b': b, 'orb': orb, 'orbit': orbit, 'size': len(orbit) * len(orb), 'g': g,
                          'order': order(g), 'cg': cyc_type(g), 'cd': cyc_type(A), 'gl': len(orbit)})
    # self-inverse test: g^-1 conjugate to g in AGL
    def class_of(g):
        b = g[0]; A = tuple(g[x] ^ b for x in range(N))
        for k, it in enumerate(inter):
            if A in it['orbit']:
                h = it['orbit'][A]                    # h A_rep h^-1 = A  -> conjugate g by h^-1
                hi = Gi[h]
                g2 = comp(comp(hi, g), h)             # linear part A_rep
                b2 = g2[0]
                if b2 in it['orb']: return k
        return None
    twins = 0; selfinv = 0
    for k, it in enumerate(inter):
        kk = class_of(pinv(it['g']))
        if kk == k: selfinv += 1
        else: twins += 1
    sig = len({(it['cg'], it['cd']) for it in inter}); sig_g = len({it['cg'] for it in inter})
    say(f'N10 L={L}: |AGL| = {sum(it["size"] for it in inter)}, interfaces {len(inter)}, self-inverse {selfinv}, twin pairs {twins // 2}, '
        f'signature values {sig} (cycles(g) alone {sig_g}), GL classes {len(classes)}')
    cat[L] = inter
def ct(s):   # parse "(1^4, 2^2)" style into sorted tuple
    s = s.strip().strip('()').replace('{', '').replace('}', '')
    outl = []
    for part in [p.strip() for p in s.split(',') if p.strip()]:
        if '^' in part: a, e = part.split('^'); outl += [int(a)] * int(e)
        else: outl.append(int(part))
    return tuple(sorted(outl))
paper3 = [(1, 1, '(1^8)', '(1^8)'), (7, 2, '(2^4)', '(1^8)'), (42, 2, '(1^4, 2^2)', '(1^4, 2^2)'), (42, 2, '(2^4)', '(1^4, 2^2)'),
          (84, 4, '(4^2)', '(1^4, 2^2)'), (168, 4, '(1^2, 2, 4)', '(1^2, 2, 4)'), (168, 4, '(4^2)', '(1^2, 2, 4)'),
          (224, 3, '(1^2, 3^2)', '(1^2, 3^2)'), (224, 6, '(2, 6)', '(1^2, 3^2)'), (192, 7, '(1, 7)', '(1, 7)'), (192, 7, '(1, 7)', '(1, 7)')]
paper4 = [(1, 1, '(1^16)', '(1^16)'), (15, 2, '(2^8)', '(1^16)'), (210, 2, '(1^8, 2^4)', '(1^8, 2^4)'), (630, 2, '(2^8)', '(1^8, 2^4)'),
          (840, 4, '(4^4)', '(1^8, 2^4)'), (840, 2, '(1^4, 2^6)', '(1^4, 2^6)'), (2520, 4, '(4^4)', '(1^4, 2^6)'),
          (5040, 4, '(1^4, 2^2, 4^2)', '(1^4, 2^2, 4^2)'), (5040, 4, '(2^4, 4^2)', '(1^4, 2^2, 4^2)'), (10080, 4, '(4^4)', '(1^4, 2^2, 4^2)'),
          (4480, 3, '(1^4, 3^4)', '(1^4, 3^4)'), (13440, 6, '(2^2, 6^2)', '(1^4, 3^4)'), (20160, 4, '(1^2, 2, 4^3)', '(1^2, 2, 4^3)'),
          (20160, 8, '(8^2)', '(1^2, 2, 4^3)'), (26880, 6, '(1^2, 2, 3^2, 6)', '(1^2, 2, 3^2, 6)'), (26880, 12, '(4, 12)', '(1^2, 2, 3^2, 6)'),
          (23040, 7, '(1^2, 7^2)', '(1^2, 7^2)'), (23040, 7, '(1^2, 7^2)', '(1^2, 7^2)'), (23040, 14, '(2, 14)', '(1^2, 7^2)'), (23040, 14, '(2, 14)', '(1^2, 7^2)'),
          (1792, 3, '(1, 3^5)', '(1, 3^5)'), (26880, 6, '(1, 3, 6^2)', '(1, 3, 6^2)'), (21504, 15, '(1, 15)', '(1, 15)'), (21504, 15, '(1, 15)', '(1, 15)'),
          (21504, 5, '(1, 5^3)', '(1, 5^3)')]
for L, pt in ((3, paper3), (4, paper4)):
    mine = Counter((it['size'], it['order'], it['cg'], it['cd']) for it in cat[L])
    theirs = Counter((a, b, ct(c), ct(d)) for a, b, c, d in pt)
    say(f'N10 L={L}: paper table equals computed catalog as a multiset: {mine == theirs}' + ('' if mine == theirs else f'  diff {mine - theirs} / {theirs - mine}'))

# ---------------------------------------------------------------- N15 comb constants
chi = 0.68; rp = 1 + math.sqrt(1 - chi * chi)
Om = chi / (2 * rp); ka = math.sqrt(1 - chi * chi) / (2 * rp); w220 = 0.523975
def line(alpha, Omv, kav):
    step = kav * alpha / (8 * math.pi); Ns = (w220 - 2 * Omv) / step; Nn = max(1, round(Ns))
    return step / w220, Ns, Nn, 100 * (2 * Omv + Nn * step - w220) / w220
sig = 2.0 / 1.6448536269514722
say(f'N15 chi=0.68: M Omega_H = {Om:.6f}, M kappa = {ka:.6f}  (paper quotes 0.196390, 0.211820)')
for name, a in (('4 ln 2', 4 * math.log(2)), ('4 ln 3', 4 * math.log(3)), ('8 pi', 8 * math.pi), ('15.6', 15.6)):
    sp, Ns, Nn, off = line(a, Om, ka); sp2, Ns2, Nn2, off2 = line(a, 0.196390, 0.211820)
    say(f'N15 {name:7s}: spacing {100 * sp:.2f}%, N* {Ns:.2f}, N {Nn}, offset {off:+.2f}% ({abs(off - 2) / sig:.2f} sigma) | with the paper\'s quoted constants: N* {Ns2:.2f}, offset {off2:+.2f}%')

# ---------------------------------------------------------------- N16 3-SAT midpoint table, E_n widths
paper_cut = {6: 21.6, 8: 27.6, 10: 34.4, 12: 41.7, 13: 44.4, 14: 48.5, 15: 51.2, 16: 54.4}
for n in sorted(paper_cut):
    m = int(4.267 * n + 0.5); a = n // 2; b = n - a
    frac = 1 - (math.comb(a, 3) + math.comb(b, 3)) / math.comb(n, 3)
    say(f'N16 n={n:2d}: m={m}, expected crossing clauses {m * frac:.1f}  (paper {paper_cut[n]})')
def width_profile(n, order):
    # E_n = AND_i (x_i == x_{n-1-i}); count distinct residuals at every cut in the given order
    N = 1 << n; tt = []
    for xv in range(N):
        b = [(xv >> (n - 1 - i)) & 1 for i in range(n)]
        tt.append(all(b[i] == b[n - 1 - i] for i in range(n // 2)))
    prof = []
    for k in range(n + 1):
        pre, suf = order[:k], order[k:]
        rows = set()
        for a in range(1 << k):
            row = []
            for s_ in range(1 << (n - k)):
                b = [0] * n
                for i, v in enumerate(pre): b[v] = (a >> i) & 1
                for i, v in enumerate(suf): b[v] = (s_ >> i) & 1
                row.append(tt[int(''.join(map(str, b)), 2)])
            rows.add(tuple(row))
        prof.append(len(rows))
    return prof
for n in (4, 6, 8, 10, 12):
    binary = list(range(n)); mirror = [x for i in range(n // 2) for x in (i, n - 1 - i)]
    pb, pm = width_profile(n, binary), width_profile(n, mirror)
    say(f'N16 E_{n}: binary peak {max(pb)} (2^(n/2) = {2 ** (n // 2)}), mirror peak {max(pm)}, mirror profile {pm}')

open('/home/claude/work/referee/nf-r1/c9/c9_checks_a.out', 'w').write('\n'.join(out) + '\n')
```

### Source (`c9_checks_b.py`)

```python
# C9 checks, part B: the two-reader 17-bit fixed-charge sector (C = u), built from the two-reader rule.
# Independent of the paper's appendix script. Sealed predictions: work/referee/nf-r1/c9/c9_seal.txt.
import numpy as np, itertools, zlib
from collections import Counter

out = []
def say(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)

# 3-bit codes x = x0 eR + x1 eL + x2 s (bit i = plane i); ell = x0 ^ x1 is "reads differently backward"
ell = lambda x: (x ^ (x >> 1)) & 1
Pc  = np.array([(c ^ 3) if ell(c) else (c ^ 7) for c in range(8)])     # native facing on the carrier K
Phi = {'I': lambda x: x, 'J': lambda x: x ^ (3 * ell(x)), 'A': lambda x: x ^ (4 * ell(x)), 'A0': lambda x: x ^ (7 * ell(x))}
PHI = {k: np.array([f(c) for c in range(8)]) for k, f in Phi.items()}
A = PHI['A']; U = 7
T4 = [h for h in range(8) if ell(h) == 0]
REPS = [0, 1, 3, 5]
ORB = np.array([0, 1, 1, 2, 2, 3, 3, 0]); ISP = np.array([0, 0, 1, 0, 1, 0, 1, 1])
assert all(A[r] ^ U in (7, 2, 4, 6) for r in REPS) and [ORB[A[r] ^ U] for r in REPS] == [0, 1, 2, 3]

# state = (p, w, d0..d3); raw 18-bit index; sector = charge ell(p)^sum ell(d_r) == 0
raw = np.arange(1 << 18)
w_ = raw & 7; p_ = (raw >> 3) & 7; d_ = np.stack([(raw >> (6 + 3 * r)) & 7 for r in range(4)], axis=1)
ELL = np.array([ell(c) for c in range(8)])
valid = (ELL[p_] ^ ELL[d_[:, 0]] ^ ELL[d_[:, 1]] ^ ELL[d_[:, 2]] ^ ELL[d_[:, 3]]) == 0
S_raw = raw[valid]; NS = len(S_raw)
idx = -np.ones(1 << 18, dtype=np.int64); idx[S_raw] = np.arange(NS)
w = w_[valid]; p = p_[valid]; d = d_[valid]
def pack(p, w, d): return w | (p << 3) | (d[:, 0] << 6) | (d[:, 1] << 9) | (d[:, 2] << 12) | (d[:, 3] << 15)
say(f'sector states {NS}')

# the coupled step: reader A at p; reader B at A(p)^u carries A(w); both write; both move
o = ORB[p]; part = ISP[p]
dp = np.where(part == 0, d[np.arange(NS), o], A[d[np.arange(NS), o]])
x = dp ^ w; y = Pc[x]
dn = d.copy(); dn[np.arange(NS), o] = d[np.arange(NS), o] ^ np.where(part == 0, y, A[y])
F = idx[pack(p ^ x, y, dn)]
assert (F >= 0).all() and len(np.unique(F)) == NS
say('F is a bijection on the sector and keeps the charge: True')
X = x                                       # move letter at each state

# G16 = V4 x T4 acting by p -> phi(p)^h, w -> phi(w), D'[phi(k)^h] = phi(D[k])
def D_at(dd, k):                            # field value at address k (vectorised over states)
    v = dd[:, ORB[k]]
    return A[v] if ISP[k] else v
def act(ph, h):
    f = PHI[ph]
    nd = np.zeros_like(d)
    for r, kp in enumerate(REPS):
        k = f[kp ^ h]
        nd[:, r] = f[D_at(d, k)]
    return idx[pack(f[p] ^ h, f[w], nd)]
G = [(ph, h) for ph in ('I', 'J', 'A', 'A0') for h in T4]
GA = {g: act(*g) for g in G}
assert all((GA[g] >= 0).all() for g in G)
comm = all(np.array_equal(F[GA[g]], GA[g][F]) for g in G)
fix = {g: int((GA[g] == np.arange(NS)).sum()) for g in G}
say(f'G16 commutes with F: {comm}')
say('fixed points: ' + ', '.join(f'({g[0]},{g[1]})={v}' for g, v in fix.items()))
ncls = sum(fix.values()) // 16
canon = np.min(np.stack([GA[g] for g in G]), axis=0)
sizes = Counter(Counter(canon.tolist()).values())
say(f'Burnside classes {ncls}; orbit-size distribution {dict(sorted(sizes.items()))}; classes counted {len(set(canon.tolist()))}')

# full-sector cycles
def cycles(perm, members=None):
    n = len(perm); seen = np.zeros(n, dtype=bool); cyc = []
    for s in (range(n) if members is None else members):
        if seen[s]: continue
        c = [s]; seen[s] = True; t = perm[s]
        while t != s: c.append(t); seen[t] = True; t = perm[t]
        cyc.append(c)
    return cyc
cyc = cycles(F)
cl = Counter(len(c) for c in cyc)
say(f'full sector: {len(cyc)} cycles over {len(cl)} lengths: {dict(sorted(cl.items()))}')

# quotient
reps = np.unique(canon); rid = {int(r): i for i, r in enumerate(reps)}
Q = np.array([rid[int(canon[F[r]])] for r in reps])
qc = cycles(Q); qcl = Counter(len(c) for c in qc)
say(f'quotient: {len(reps)} classes, {len(qc)} cycles: {dict(sorted(qcl.items()))}')

# rungs
Rm = ((w & 1) == 0) & np.all((d & 1) == 1, axis=1)
Lm = ((w & 2) == 0) & np.all((d & 2) == 2, axis=1)
say(f'|R| = {Rm.sum()}, |L| = {Lm.sum()}, |R & L| = {(Rm & Lm).sum()}, R invariant {np.array_equal(Rm[F], Rm)}, L invariant {np.array_equal(Lm[F], Lm)}')
rung = np.where(Rm & Lm, 1, np.where(Rm ^ Lm, 2, 3))
for k in (1, 2, 3):
    cs = [c for c in cyc if rung[c[0]] == k]
    sc = Counter(len(c) for c in cs)
    qs = [c for c in qc if rung[reps[c[0]]] == k]
    qsc = Counter(len(c) for c in qs)
    nq = sum(len(c) for c in qs)
    say(f'rung {k}: {sum(len(c) for c in cs)} states, {len(cs)} cycles {dict(sorted(sc.items()))}')
    say(f'        quotient {nq} classes, {len(qs)} cycles {dict(sorted(qsc.items()))}')
paper_r2 = {2: 352, 4: 128, 6: 288, 12: 24, 30: 8, 94: 8, 98: 8, 212: 8, 434: 8}
paper_r3 = {2: 208, 4: 128, 6: 976, 12: 272, 14: 72, 18: 256, 132: 8, 1612: 8, 2260: 8, 3948: 8, 5186: 8}
say(f'paper rung-2 table holds {sum(k * v for k, v in paper_r2.items())} states (rung 2 has {int((rung == 2).sum())}); paper rung-3 table holds {sum(k * v for k, v in paper_r3.items())} (rung 3 has {int((rung == 3).sum())})')

# indicator degrees of R, L
def anf_deg_tt(tt_bits):                     # tt over 17 coordinates (state index order = sector order mapped to 17 bits)
    f = tt_bits.astype(np.uint8).copy(); nvar = int(np.log2(len(f)))
    for i in range(nvar):
        f = f.reshape(-1, 2, 1 << i); f[:, 1, :] ^= f[:, 0, :]; f = f.reshape(-1)
    nz = np.nonzero(f)[0]
    return 0 if len(nz) == 0 else int(max(bin(int(v)).count('1') for v in nz))
# 17 free coordinates: w(3) p(3) d0 d1 d2 (9) d3 planes 0 and 2 (2); d3 plane 1 fixed by the charge
key17 = w | (p << 3) | (d[:, 0] << 6) | (d[:, 1] << 9) | (d[:, 2] << 12) | ((d[:, 3] & 1) << 15) | (((d[:, 3] >> 2) & 1) << 16)
assert len(np.unique(key17)) == NS
pos = np.empty(NS, dtype=np.int64); pos[key17] = np.arange(NS)   # pos[k] = state with key k
def deg_of_set(mask):
    tt = np.zeros(NS, dtype=np.uint8); tt[key17[mask]] = 1; return anf_deg_tt(tt)
def deg_of_map(Fm):
    img = key17[Fm[pos]]                     # map on keys: key -> key of image
    return max(anf_deg_tt(((img >> b) & 1).astype(np.uint8)) for b in range(17))
say(f'indicator degrees: R {deg_of_set(Rm)}, L {deg_of_set(Lm)}, R^L {deg_of_set(Rm ^ Lm)}, R&L {deg_of_set(Rm & Lm)}, unlocked {deg_of_set(~(Rm | Lm))}')
Ft = np.arange(NS); degs = {}
for t in range(1, 13):
    Ft = F[Ft]
    if t in (1, 2, 3, 4, 5, 6, 8, 12): degs[t] = deg_of_map(Ft)
say(f'degree of F^t (lab, 17 bits): {degs}')

# vacuum seed: p = 0, w = eR (code 1), empty field
seed = int(idx[pack(np.array([0]), np.array([1]), np.zeros((1, 4), dtype=np.int64))[0]])
vc = next(c for c in cyc if seed in c)
say(f'vacuum seed cycle length {len(vc)}; indicator degree {deg_of_set(np.isin(np.arange(NS), vc))}')
s = seed; moves = []
for t in range(806): moves.append(int(X[s])); s = F[s]
owners = [g for g in G if GA[g][seed] == s]
say(f'F^806(seed) = g . seed for g in {owners}; moves letter counts {[moves.count(k) for k in range(8)]}')
def cyc_factors(seq, L):
    n = len(seq); return len({tuple(seq[(i + j) % n] for j in range(L)) for i in range(n)})
say(f'cyclic factor complexity L=1..5: {[cyc_factors(moves, L) for L in range(1, 6)]}; zlib(level 9) {len(zlib.compress(bytes(moves), 9))} bytes')
cyl = np.nonzero(p == 0)[0]; sz = [len(cyl)]
for m in moves[:9]:
    cyl = F[cyl[X[cyl] == m]]; sz.append(len(cyl))
say(f'cylinder sizes under the first 9 moves: {sz}')

# eR ledger
Qe = (p & 1) ^ (d[:, 0] & 1) ^ (d[:, 1] & 1) ^ (d[:, 2] & 1) ^ (d[:, 3] & 1)
say(f'Q_eR flips every step: {bool(np.all(Qe[F] ^ Qe == 1))}; Q_eR(g.s) = Q_eR(s) ^ h0 for all g: '
    f'{all(np.all(Qe[GA[g]] ^ Qe == (g[1] & 1)) for g in G)}')

# twisted Burnside return operator, all depths that are quotient cycle lengths and a few others
tw_ok = True; depths = sorted(set(qcl) | {5, 10, 11})
Fpow = {}
for t in depths:
    # F^t via cycles
    Ft = np.empty(NS, dtype=np.int64)
    for c in cyc:
        L = len(c); arr = np.array(c); Ft[arr] = arr[(np.arange(L) + t) % L]
    lhs = sum(1 for c in qc for _ in [0] if len(c) and t % len(c) == 0 for _ in c)
    rhs = sum(int((Ft == GA[g]).sum()) for g in G) // 16
    tw_ok &= lhs == rhs
say(f'twisted Burnside #Fix(Q^t) = (1/16) sum_g #{{F^t s = g s}} at {len(depths)} depths: {tw_ok}')

# rung-2 section S = R & {w = 0}: first returns
Sm = Rm & (w == 0)
Sidx = np.nonzero(Sm)[0]
ret = {}; M0 = {}
for s0 in Sidx:
    t = 1; s1 = F[s0]
    while not Sm[s1]: s1 = F[s1]; t += 1
    ret[int(s0)] = t; M0[int(s0)] = int(s1)
say(f'|S| = {len(Sidx)}; return times {dict(sorted(Counter(ret.values()).items()))}')
hits = Counter()
for c in cyc:
    if Rm[c[0]]:
        hits[(len(c), int(Sm[np.array(c)].sum()))] += 1
say(f'R cycles (length, hits on S): count {dict(sorted(hits.items()))}')
# degree of M0 on the 10 free bits of S
free = [3, 4, 5, 7, 8, 10, 11, 13, 14, 16]
def k10(i): k = int(key17[i]); return sum(((k >> b) & 1) << j for j, b in enumerate(free))
tt = {k10(s0): k10(M0[s0]) for s0 in M0.keys()}
assert len(tt) == 1024
degM0 = max(anf_deg_tt(np.array([(tt[k] >> b) & 1 for k in range(1024)], dtype=np.uint8)) for b in range(10))
say(f'degree of the first-return map M0 on 10 bits: {degM0}')

# the 64 seeds: A = (0, eR) on an empty field, B = (pB, wB) in K x K; tau = H_h Phi_phi J_swap, h in K
fixed_by = Counter(); any_fixed = 0
for pB, wB in itertools.product(range(8), repeat=2):
    hit = False
    for ph, f in Phi.items():
        for h in range(8):
            if (f(pB) ^ h, f(wB)) == (0, 1) and (f(0) ^ h, f(1)) == (pB, wB):
                fixed_by[ph] += 1; hit = True
    any_fixed += hit
say(f'64-seed index: {any_fixed} seeds fixed by some tau; per phi {dict(fixed_by)}')
f = Phi['A']; say(f'witness seed A=(0,eR), B=(u,u^eL): tau = H_u Phi_A J_swap fixes it: {(f(7) ^ 7, f(5)) == (0, 1) and (f(0) ^ 7, f(1)) == (7, 5)}')

open('/home/claude/work/referee/nf-r1/c9/c9_checks_b.out', 'w').write('\n'.join(out) + '\n')
```

### Source (`c9_checks_c.py`)

```python
# C9 checks, part C: whole-vs-parts tables (G1, G2, all-k), Page average, degree-<=3 invariants of the sector step.
import itertools, math
import numpy as np
from collections import Counter
out = []
def say(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)
def J(x, n): return int(format(x, f'0{n}b')[::-1], 2) if n else 0
def C(x, n): return x ^ ((1 << n) - 1)
def pal(x, n): return J(x, n) == x
def P(x, n): return C(x, n) if pal(x, n) else J(x, n)

# G1: Section-181 two-step paths a|b, b|c (whole word a|b|b|c at LEN 4n)
for n in range(2, 5):
    N = 1 << n; mism = 0
    for a, b, c in itertools.product(range(N), repeat=3):
        e1, e2 = (a << n) | b, (b << n) | c
        W = (((a << n | b) << n | b) << n) | c
        f2, f1 = P(e2, 2 * n), P(e1, 2 * n)
        chained = (f2 & (N - 1)) == (f1 >> n)
        if not chained: mism += 1; continue
        partwise = (((f2 >> n) << n | (f2 & (N - 1))) << 2 * n) | f1      # P(e2) then P(e1), repeated middle face
        if partwise != P(W, 4 * n): mism += 1
    r = 2 ** ((n + 1) // 2)
    say(f'G1 n={n}: whole != parts on {mism} paths; formula 2N(N-1)+r(N-1)+(N-r) = {2 * N * (N - 1) + r * (N - 1) + (N - r)}')

# all-k table, offset model
paper = {(3, 2): (4, 4, 8, 2, 2, 12), (3, 3): (4, 4, 24, 0, 0, 24), (3, 4): (4, 4, 56, 2, 2, 60),
         (4, 2): (18, 2, 12, 6, 0, 18), (4, 3): (30, 2, 32, 0, 0, 32), (4, 4): (50, 2, 76, 10, 0, 86),
         (5, 2): (36, 4, 24, 6, 2, 32), (5, 3): (60, 4, 64, 0, 0, 64), (5, 4): (100, 4, 152, 10, 2, 164)}
for (L, k), pv in paper.items():
    W = L + k - 1; alld = allp = brk = em = lone = 0
    for w in range(1 << W):
        cs = [(w >> (W - L - i)) & ((1 << L) - 1) for i in range(k)]
        sv = [pal(c, L) for c in cs]
        if not any(sv): alld += 1
        if all(sv): allp += 1
        pcs = [P(c, L) for c in reversed(cs)]
        ok = all((pcs[i] & ((1 << (L - 1)) - 1)) == (pcs[i + 1] >> 1) for i in range(k - 1))
        if not ok: brk += 1; continue
        pw = pcs[0]
        for i in range(1, k): pw = (pw << 1) | (pcs[i] & 1)
        if pw != P(w, W):
            if pal(w, W): em += 1
            else: lone += 1
    mine = (alld, allp, brk, em, lone, brk + em + lone)
    say(f'allk L={L} k={k}: (all-dir, all-pal, breaks, emergent, lone, total) = {mine}  paper {pv}  {"=" if mine == pv else "DIFFERS"}')

# Page's average entropy for 2^6 x 2^6
m = 64; nn = 64
S = sum(1 / j for j in range(nn + 1, m * nn + 1)) - (m - 1) / (2 * nn)
say(f'Page average for a 64x64 split: {S / math.log(2):.4f} bits; shortfall from 6: {6 - S / math.log(2):.4f}')

# degree-<=3 functions f on the sector with f(F s) = f(s): nullity of the GF(2) system (constants always included)
ell = lambda x: (x ^ (x >> 1)) & 1
Pc = np.array([(c ^ 3) if ell(c) else (c ^ 7) for c in range(8)]); A = np.array([c ^ (4 * ell(c)) for c in range(8)])
ORB = np.array([0, 1, 1, 2, 2, 3, 3, 0]); ISP = np.array([0, 0, 1, 0, 1, 0, 1, 1])
raw = np.arange(1 << 18); w_ = raw & 7; p_ = (raw >> 3) & 7; d_ = np.stack([(raw >> (6 + 3 * r)) & 7 for r in range(4)], axis=1)
ELL = np.array([ell(c) for c in range(8)])
valid = (ELL[p_] ^ ELL[d_[:, 0]] ^ ELL[d_[:, 1]] ^ ELL[d_[:, 2]] ^ ELL[d_[:, 3]]) == 0
S_raw = raw[valid]; NS = len(S_raw); idx = -np.ones(1 << 18, dtype=np.int64); idx[S_raw] = np.arange(NS)
w = w_[valid]; p = p_[valid]; d = d_[valid]; o = ORB[p]; part = ISP[p]; ar = np.arange(NS)
dp = np.where(part == 0, d[ar, o], A[d[ar, o]]); x = dp ^ w; y = Pc[x]
dn = d.copy(); dn[ar, o] = d[ar, o] ^ np.where(part == 0, y, A[y])
def pack(p, w, d): return w | (p << 3) | (d[:, 0] << 6) | (d[:, 1] << 9) | (d[:, 2] << 12) | (d[:, 3] << 15)
F = idx[pack(p ^ x, y, dn)]
key = w | (p << 3) | (d[:, 0] << 6) | (d[:, 1] << 9) | (d[:, 2] << 12) | ((d[:, 3] & 1) << 15) | (((d[:, 3] >> 2) & 1) << 16)
bitsv = [((key >> b) & 1).astype(bool) for b in range(17)]
monos = [()] + [(i,) for i in range(17)] + list(itertools.combinations(range(17), 2)) + list(itertools.combinations(range(17), 3))
def colint(arr_bool): return int.from_bytes(np.packbits(arr_bool, bitorder='little').tobytes(), 'little')
cols = []
for mo in monos:
    v = np.ones(NS, dtype=bool)
    for i in mo: v &= bitsv[i]
    cols.append(colint(v ^ v[F]))       # f(s) + f(F s) for this monomial
basis = {}; rank = 0
for c in cols:
    while c:
        lb = c.bit_length() - 1
        if lb in basis: c ^= basis[lb]
        else: basis[lb] = c; rank += 1; break
say(f'degree<=3 invariants of F: {len(monos)} monomials, rank {rank}, invariant space dimension {len(monos) - rank} (1 = constants only)')
open('/home/claude/work/referee/nf-r1/c9/c9_checks_c.out', 'w').write('\n'.join(out) + '\n')
```

## Entry C10 · 6 Nov 2026 · *Native Facing*, corrected edition, built from the LaTeX source

**Inputs.** The source `6ee6c68d-attachment.txt` (SHA-256 `ef7d800b…`), the other AI's errata, C8, C9 and the record.

**Method.** Each change is an exact replacement at an anchor that occurs once in the source; the builder stops if an anchor is missing or repeated. Each change is logged in the paper's Section 7 with its place, the old text, the correction and the evidence: 91 changes, plus one row per re-set table. Two checks that nothing correct was removed:
- Prose: with the replaced passages and table spans taken out, all 120 remaining source pieces occur verbatim in the corrected text.
- Tables: a digit diff of each source table against its re-set table leaves only logged corrections (Tables 1.4, 2.3, 5.2, 5.3) and alignment artifacts checked by eye. Table 1.1's seam notation moved into its caption. Each table span ends on its last row, so no prose was swallowed.

**What changed.**
- C9's Wrong items 1–6 are applied in place.
- §3.3 holds Theorem 3.3 as the seam obstruction (the faced-table law, C6 A). The second provider's origin is corrected, and "a reader must exist" is removed.
- New §3.4 is C8's compiler: Theorems 3.4–3.7 (BIND, COMPOSE, CLOSE, route bounds), K1–K5, the fewest routes 2^(⌈n/2⌉−1), K4(c) failing at n = 3, and Table 3.4 for n = 3–12.
- The v3–v5.8 machine paragraph moved to §3.5 with the record's numbers: v3's 30,844 built-in checks and 25,200 comparisons, and the local model's 25,204 pair checks. The 10,803 is dropped, and the goal resolver is told apart from the compiler verb.
- §5.3 follows the 3-SAT paper.
  - Table 5.3a keeps its exact columns, with the midpoint cuts corrected and E_n's mirror width at 3. The fitted-curve columns are removed.
  - Tables 5.3b–e reproduce [4] Tables 1, 2, 3 and 7.
  - Theorems 1–6 of [4] are stated, then the bridge exactly and what it does not claim.
  - Figure 2 plots [4]'s medians.
- Added from the record:
  - §1.5: Theorems 1.5–1.9, the half-lap contract and the reader at the centre.
  - §2.3: Theorems 2.4–2.5, the §181 all-k counts and the hinge bijection Φ.
  - §4.4 native shift programs (A9) and §4.5 the reading direction (A11).
  - §5.4: the retained step's mirrors and its twin (C4, C6 C/D).
  - Table 4.1 with D.2's native elements, ledger Table 6.1 with record labels, and References [1]–[52].
  - Appendices B (C9 seal and checks) and C (C8 compiler).
- Figure 1 shows the ring R_4 with its facing chords, palindromes and seam.
- Appendix A's script has its docstring and PASS lines narrowed to what it asserts. Its assertions are unchanged, and it passes.

**Render.** In LibreOffice the file comes to 65 pages, with 22 tables and 2 figures. The equations are native Word math. LibreOffice misdraws "|" and "#" inside equations as ∨ or ¿; the file holds the right characters, but it was not opened in Word here. Set-minus is written as U+2216, which every reader draws.

**Files** (`work/nf_fix/out`):
- `Native_Facing_corrected.docx`: f9ce05c926b7cc2ea880c70478aeaed7a4f1802ead73d4c211e0d2153fafc237
- `Native_Facing_corrected.md` (the master): 687cb53f47745d4af80fd27de341039be0c23f86e91c9465f8c267a6ac1966f3
- `master_verify_corrected.py`: a2fb470c6085fe8c0336b40638f1c75adef03e5a1594ecef2309dcac9a7c2709

### Live output

```text
# nf_build.py
built 236782 chars; 91 logged corrections
# nf_coverage.py
120 source pieces checked; 0 not found verbatim
# table digit diff, source vs re-set (T4, T5 against the whole text)
T1 src digits 238 unmatched 1 ['1']            <- header R_n[m-1], now in the caption
T2 src digits 264 unmatched 0 []
T3 src digits 118 unmatched 5 ['220', '6', '8'] <- omega_220 header present; chi 0.68 / 8pi labels corrected (logged)
T4 src digits 134 unmatched 12 ['30', '2', '2', '50', '76', '6', '256']  <- L = 4, 5 rows at k = 3, 4 (logged)
T5 src digits 149 unmatched 0 []
T6 src digits 752 unmatched 2 ['10']           <- '10 (112)' present at #21
T7 src digits 223 unmatched 58 [...]           <- ladder multiplicities and totals (logged)
# nf_docx.py
set-minus glyphs: 6
tables styled: 22
# master_verify_corrected.py (python3 -I, fresh directory, 0.9 s)
PASS: Section 1 (facing involution and degrees n=1-12; ring seam, PTP=T^-1, successor exceptions n=2-12; Page tent n=12,13; successor center split n=5-11; binary comb line)
PASS: Section 2 (all-k chaining criterion, emergent and lone seams L=2-6, k=2-5; Delta pullback r=1-6)
PASS: Section 3 (dim Z = 2^n + 1 and disjoint four-face defects n=1-7; fixed-necklace formula L=1-14)
PASS: Section 4 (native count by exhaustion n=1-3; principal-cycle contact addresses n=2-9)
PASS: Section 5 (e_R ledger flips on all 131,072 states; 9-move cylinder collapse)

ALL ASSERTIONS IN THIS SCRIPT PASS (coverage: Appendix A).
```

## Entry C11 · 6 Nov 2026 · looking out from the centre: two collisions run

**Native count.** Σₖ C(c,k)(2c−2k−1)!! is OEIS A084262, the binomial transform of the double factorials (EGF eˣ/√(1−2x), recurrence a(c) = 2c·a(c−1) − 2(c−1)·a(c−2)). It is recovered, not new. The native programs at LEN n are the term at c = 2ⁿ⁻¹, which gives 2, 6, 188, 3,460,368 and 321,626,829,363,798,272. Read on the contract: each of the c NOT-pairs is either kept as a pair or opened, and the opened points are perfectly matched. A guess that it was A000898, the symmetric involutions given by Hermite at i, failed: the two agree at 1, 2, 6 and part at 28 vs 20. Brute force confirms that A000898 counts involutions commuting with NOT (2, 6, 20, 76). The native count is a different object.

**Gray code.** The collision I asserted in conversation without running it fails as stated. The native ring is not a Gray code: at n = 10, 410 of its 1,024 steps flip one bit, and the mean is 2.18 flips. The two reflection laws are disjoint at n = 2–10: the reflected Gray code obeys facing at 0 addresses, and the ring obeys top-bit reflection at 0. What they share is only the generic shape "second half = an involution of the first half, reversed". Facing is not an implementation of Gray reflection.

### Live output

```text
c : [0, 1, 2, 3, 4, 5, 6, 7, 8]
native formula Sum C(c,k)(2c-2k-1)!!: [1, 2, 6, 28, 188, 1656, 17992, 232016, 3460368]
recurrence 2a(c-1)+2(c-1)a(c-2)      : [1, 2, 6, 20, 76, 312, 1384, 6512, 32400]
(-i)^c H_c(i), Hermite               : [1, 2, 6, 20, 76, 312, 1384, 6512, 32400]
equal for c = 0..32: False
Native(n) = value at c = 2^(n-1), n=1..5: [2, 6, 188, 3460368, 321626829363798272]
brute: involutions commuting with a fixed-point-free involution, c=1..4: [2, 6, 20, 76]
# OEIS (web): A084262 = 1, 2, 6, 28, 188, 1656, 17992, 232016, 3460368, ...  "Binomial transform of double factorials", e.g.f. exp(x)/(1-2x)^(1/2)
n= 2  ring steps that flip one bit:    2/4  mean flips 1.50 | BRGC obeys facing at    0/4 | ring obeys top-bit reflection at 0/4
n= 6  ring steps that flip one bit:   22/64  mean flips 2.22 | BRGC obeys facing at    0/64 | ring obeys top-bit reflection at 0/64
n=10  ring steps that flip one bit:  410/1024  mean flips 2.18 | BRGC obeys facing at    0/1024 | ring obeys top-bit reflection at 0/1024
```

## Entry C12 · 6 Nov 2026 · routes from the centre, interface first

The runs were unsealed: measured, not predicted. Notebook: `kramers_reversal_of_the_clock.ipynb` (self-contained).

| route | interface (forced) | implementation | status |
|---|---|---|---|
| R-a half lap | τⁿ = NOT, τ²ⁿ = I, NOT central, JτJ = τ⁻¹ (RUNS n = 1–12) | the Johnson / twisted-ring counter; the binary cyclic group (the preimage of an axis's rotations in SU(2)), with NOT as −1 | FOUND (recovered) |
| R-b spectrum | NOT-odd states carry only odd k in e^(iπk/n), half-integer frequencies; NOT-even states carry only even k (RUNS n = 3–5) | spinor vs integer characters of the double cover on one axis; §1.5's half-lap contract read on the spectrum | FOUND (recovered) |
| R-c Kramers | a reversal b of the clock with bτb⁻¹ = τ⁻¹ and b² = NOT, so T = bK has T² = −1 on the odd sector | Kramers/Wigner time reversal for half-integer spin | FOUND on the ring exactly at n ≡ 0 (mod 4), n ≤ 20; see below |

**R-c in full.** A Kramers reversal exists iff every τ-cycle length occurs an even number of times.
- *Only if* is proved: b² = NOT fixes every cycle, and a self-mapped cycle would carry a reflection, which squares to I.
- *If* is proved: pair the cycles and set b(τᵏx) = τ⁻ᵏy and b(τᵏy) = τ⁻ᵏNOT x.
- n odd fails on its unique alternating 2-cycle; n ≡ 2 (mod 4) fails on its unique 4-cycle; n ≡ 0 (mod 4) passes at 4, 8, 12, 16, 20.
- Exhaustive search at n = 1–6 gives 8 reversals at n = 4, 2 of them native, and 0 elsewhere.
- The plain reversal J has J² = I, the integer-spin kind.

OPEN:
- evenness for every n ≡ 0 (mod 4);
- native Kramers reversals at n ≥ 8;
- whether n ≡ 0 (mod 4) meets §1.8's ±i at even LEN.

### Live output

```text
n= 3 {2: 1, 6: 1}  all even: False
n= 4 {8: 2}  all even: True
n= 6 {4: 1, 12: 5}  all even: False
n= 8 {16: 16}  all even: True
n=12 {8: 2, 24: 170}  all even: True
n=15 {2: 1, 6: 1, 10: 3, 30: 1091}  all even: False
n=18 {4: 1, 12: 5, 36: 7280}  all even: False
n=20 {8: 2, 40: 26214}  all even: True
Kramers possible at n = [4, 8, 12, 16, 20]
n=4: Kramers reversals 8, native 2        (n = 1, 2, 3, 5, 6: 0)
n=4, 8, 12, 16, 20: constructed b is a bijection with b^2 = NOT and b tau = tau^-1 b: True
n=3 odd  k: [1, 3, 3, 5]            n=3 even k: [0, 0, 2, 4]
n=4 odd  k: [1, 1, 3, 3, 5, 5, 7, 7] n=4 even k: [0, 0, 2, 2, 4, 4, 6, 6]
```

## Entry C13 · 6 Nov 2026 · sealed: native Kramers reversals at LEN 8 and 12, and the mod-4 rule against Theorem 1.8

**Seal.** `work/seal_c13/c13_seal.txt`, SHA-256 `1ae84e137dcce1f437551b6bd0ae9199cb1812a9ddb2a0fc9af7b95394b7b45c`, written at 2026-11-06T09:20:18Z, before any C13 code ran. All six sealed items landed (K1–K6). The counts at 8 and 12 were reported, not predicted. Script: `tools/c13_kramers.py`. The notebook `kramers_reversal_of_the_clock.ipynb` now carries the section, executed.

- **K1 lands.** S_b is NOT-closed for every Kramers reversal, because b and J commute with NOT. So native ⇔ JbJ = b⁻¹ ⇔ bJb⁻¹ = J·NOT.
- **K2, K3 land.** There are native Kramers reversals at LEN 8 (6,478,080 of 8,706,006,083,174,400 = 15!!·16⁸) and at LEN 12 (a 115-digit count). One native b was built and checked directly at each.
- **K4 lands.** The orbit method gives 8 Kramers reversals at LEN 4, 2 of them native, equal to the exhaustive search.
- **Count shape.** Each block of ⟨τ, J⟩-orbits is either paired (weight w) or kept (weight s), so the count is Σⱼ C(m,2j)(2j−1)!! wʲ s^(m−2j). This is the native program count's kept-or-opened shape (A084262, C11) at a new address. At LEN 8 the blocks are 8 J-symmetric 16-cycles (w = 2, s = 0: 7!!·2⁴ = 1,680) and 4 J-swapped pairs of 16-cycles (w = 32, s = 2: 3,856).
- **K5 lands, and the answer is no.** Theorem 1.8's Q = τ^(n/2) squares to NOT at every even n = 2–12, including n = 2, 6 and 10, where no Kramers reversal exists. The mod-4 rule is not the ±i.
- **K6 lands.** Every Kramers b checked satisfies bQb⁻¹ = NOT·Q (all 8 at n = 4, the constructed ones at n = 8–20, and the native ones at 8 and 12). So on NOT-odd states Q² = b² = (Qb)² = −1, which are the quaternion relations. Theorem 1.8 gives *i* at every even LEN, Kramers gives *j* only at n ≡ 0 (mod 4), and the mod-4 rule is the condition for a quaternionic structure on the clock's odd sector. Collision, recovered: the quaternionic (T² = −1) class of Dyson's threefold way.

OPEN:
- evenness of the cycle multiplicities for all n ≡ 0 (mod 4) (run to 20);
- whether the w and s of each block have a closed form in n (w = 2 on J-symmetric cycles and w = L on J-swapped pairs so far).

### Live output

```text
n= 2  Q^2 = NOT: True      (n = 4, 6, 8, 10, 12: True)
n= 4  Kramers total 8   native 2
n= 6  Kramers total 0   native 0
n= 8  Kramers total 8,706,006,083,174,400   native 6,478,080
        native block: 8 orbits of size 16, pair weight 2, self weight 0, count 1,680
        native block: 4 orbits of size 32, pair weight 32, self weight 2, count 3,856
        one native b found: Kramers True, S_b NOT-closed True, native criterion True, bQ = NOT Qb True, quaternion True, |S_b| = 64
n=12  native 5,318,206,758,990,508,381,096,428,668,543,428,213,388,628,851,092,653,407,852,404,185,661,630,691,732,364,629,329,842,325,348,931,231,030,519,839,810,825,448,671,150,080,000
        native block: 30 orbits of size 24, pair weight 2, self weight 0, count 202,843,204,931,727,360,000
        native block: 70 orbits of size 48, pair weight 48, self weight 2, count 13,109,156,...,078,464
        native block: 2 orbits of size 8, pair weight 2, self weight 0, count 2
        one native b found: Kramers True, S_b NOT-closed True, native criterion True, bQ = NOT Qb True, quaternion True, |S_b| = 1680
n=4: 8 Kramers; S_b NOT-closed in all: True; native: 2; bQ = NOT Qb in all: True; quaternion in all: True
n=8, 12, 16, 20: constructed b: Kramers True, S_b NOT-closed True, native False, bQ = NOT Qb True, quaternion True
```
