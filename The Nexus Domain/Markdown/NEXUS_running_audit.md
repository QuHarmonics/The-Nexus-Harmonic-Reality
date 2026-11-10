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
