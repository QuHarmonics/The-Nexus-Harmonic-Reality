"""
q_D = 100 1^(D-5) 00 : radial profile, one bit per ring, rings 1..D.
Reverse-the-gap: the compiler says q_D exists (shown D=8..16 by the swarm).
Find K_D, an interval given by a formula valid for ALL D, with reading(K_D)=q_D.

Reader (one-ring factorization, exact):
  b_L(u) = word_at( floor(2^L u), L )[ floor(L*{2^L u}) ]
No ring is ever materialised; word_at is O(L).
"""
import math
from fractions import Fraction as F

# ---- compiler anatomy (copied, no import side effects) ----
def rev(x, L):  return int(format(x, f"0{L}b")[::-1], 2)
def comp(x, L): return x ^ ((1 << L) - 1)
def part(x, L):
    r = rev(x, L); return r if r != x else comp(x, L)
is_rep = lambda x, L: x < part(x, L)
def reps_below_nonpal(x, L):
    bx = [(x >> (L - 1 - i)) & 1 for i in range(L)]
    st = {("EQ", "EQ", "U"): 1}
    for j in range(L // 2):
        r = L - 1 - j; nxt = {}
        for (pre, suf, mir), c in st.items():
            for yl in (0, 1):
                if pre == "EQ" and yl > bx[j]: continue
                npre = "LT" if (pre == "LT" or yl < bx[j]) else "EQ"
                for yr in (0, 1):
                    nsuf = suf if yr == bx[r] else ("LT" if yr < bx[r] else "GT")
                    nmir = mir if mir != "U" or yl == yr else ("LT" if yl < yr else "GT")
                    k = (npre, nsuf, nmir); nxt[k] = nxt.get(k, 0) + c
        st = nxt
    total = 0
    for (pre, suf, mir), c in st.items():
        if mir != "LT": continue
        if L % 2:
            mx = bx[L // 2]
            for ym in (0, 1):
                if pre == "LT" or (pre == "EQ" and (ym < mx or (ym == mx and suf == "LT"))): total += c
        else:
            if pre == "LT" or (pre == "EQ" and suf == "LT"): total += c
    return total
def pal_below(x, L):
    h = (L + 1) // 2; p = x >> (L - h)
    mk = lambda q: (q << (L - h)) | int(format(q, f"0{h}b")[:L - h][::-1] or "0", 2) if L - h else q
    return p + (1 if mk(p) < x else 0)
def reps_below(x, L):
    return reps_below_nonpal(x, L) + pal_below(min(x, 1 << (L - 1)), L)
def word_at(p, L):
    N = 1 << L; M = N // 2
    if M > 1 and p in (M - 1, M): k, want_rep = M - 1, (p == M)
    elif p < M: k, want_rep = p, True
    else: k, want_rep = N - 1 - p, False
    lo, hi = 0, (1 << L) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if reps_below(mid + 1, L) >= k + 1: hi = mid
        else: lo = mid + 1
    return format(lo if want_rep else part(lo, L), f"0{L}b")

# ---- reader ----
def bit(L, u):
    """u a Fraction in [0,1). returns the radial bit at ring L."""
    two = 1 << L
    w = (u * two).__floor__()
    frac = u * two - w                      # {2^L u}
    s = (frac * L).__floor__()
    return int(word_at(w, L)[s])

def profile(u, D):
    return "".join(str(bit(L, u)) for L in range(1, D + 1))

def qD(D):
    return "1" + "00" + "1" * (D - 5) + "00"   # 1,0,0, 1^(D-5), 0,0  -> length D

# ---- exact location set A_{q_D}, restricted to a window [lo,hi) ----
def Ibit(L, d, lo, hi):
    """intervals in [lo,hi) where b_L = d, as list of (a,b) Fractions."""
    S = L * (1 << L)
    jlo = (lo * S).__floor__()
    jhi = (hi * S).__ceil__()
    out = []
    for j in range(jlo, jhi):
        w, s = j // L, j % L
        if int(word_at(w, L)[s]) != d: continue
        a = max(lo, F(j, S)); b = min(hi, F(j + 1, S))
        if a < b:
            if out and out[-1][1] == a: out[-1] = (out[-1][0], b)
            else: out.append((a, b))
    return out

def intersect(A, B):
    out = []; i = j = 0
    while i < len(A) and j < len(B):
        a0, a1 = A[i]; b0, b1 = B[j]
        lo, hi = max(a0, b0), min(a1, b1)
        if lo < hi: out.append((lo, hi))
        if a1 < b1: i += 1
        else: j += 1
    return out

def A_profile(prof, D, lo=F(0), hi=F(1)):
    """pruned: at each ring only scan slices overlapping surviving intervals."""
    cur = [(lo, hi)]
    for L in range(1, D + 1):
        d = int(prof[L - 1]); nxt = []
        for a, b in cur:
            nxt.extend(Ibit(L, d, a, b))
        # merge touching
        merged = []
        for a, b in sorted(nxt):
            if merged and merged[-1][1] == a: merged[-1] = (merged[-1][0], b)
            else: merged.append((a, b))
        cur = merged
        if not cur: break
    return cur

if __name__ == "__main__":
    print("== reproduce swarm component counts for A_{q_D} (full domain) ==")
    for D in range(8, 13):
        comps = A_profile(qD(D), D)
        print(f"  D={D}: q_D={qD(D)}  components={len(comps)}")

    print("\n== component of A_{q_D} nearest 1/2 from above (exact endpoints) ==")
    half = F(1, 2)
    for D in range(8, 17):
        win = half + F(1, 1 << 6)            # window just past the seam
        comps = A_profile(qD(D), D, lo=half, hi=win)
        comps = [c for c in comps if c[0] >= half]
        if not comps:
            print(f"  D={D}: none in [1/2, 1/2+2^-6)"); continue
        a, b = comps[0]                       # leftmost = nearest seam
        eps = a - half
        # express eps
        print(f"  D={D}: left={a}  (= 1/2 + {eps})  width={b-a}  log2(eps)={math.log2(float(eps)):.3f}")

def dump_components(Dmax=16):
    print("\n== all components; which ring binds each endpoint ==")
    for D in range(8, Dmax + 1):
        comps = A_profile(qD(D), D)
        print(f"\n  D={D}  ({len(comps)} comps)")
        for a, b in comps[:8]:
            binds = [L for L in range(1, D + 1) if (a * L * (1 << L)).denominator == 1]
            print(f"    [{a}, {b})  w={b-a}  left on ring-boundaries {binds[-3:] if binds else '-'}")
