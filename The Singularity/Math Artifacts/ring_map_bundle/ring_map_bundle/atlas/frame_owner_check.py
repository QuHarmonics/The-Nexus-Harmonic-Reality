"""Owner of the frame law (derived after FA1 ran; a check, not a landing).
Every collision pairs one window that starts or ends at a palindrome on the right face with one window that touches
no palindrome. A palindrome window escapes collision exactly when the palindrome begins with 1^(s-1) (2 <= s <= h-1),
or begins with exactly 1^(L-s-1) 0 (h+1 <= s <= L-2; h+2 at odd L), the all-ones word 1^L also escaping on its entry side.
At s = h (and s = h+1 at odd L) the seam pair adds its own collisions; those cells are covered by FA1's values only.
Dean A. Kulik, QuHarmonics Research Group, ORCID 0009-0003-3128-8828."""
import sys, os, json
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, '..', 'wheels'))
import numpy as np
import wheels as wh


def J_arr(x, n):
    r = np.zeros_like(x); y = x.copy()
    for _ in range(n):
        r = (r << 1) | (y & 1); y >>= 1
    return r


out = {}
allok = True
for L in range(6, 21):
    _, _, Pw, R, loc = wh.ring_arrays(L)
    N = 1 << L; M = N // 2; h = L // 2
    idx = np.arange(N)
    ispal = J_arr(idx, L) == idx
    Rn = np.roll(R, -1)
    rows = []
    for s in list(range(2, h)) + list(range(h + 1 + (L % 2), L - 1)):   # s = h, and s = h+1 at odd L, carry seam collisions
        v = ((Rn >> (L - s)) << (L - s)) | (R & ((1 << (L - s)) - 1))
        c = np.bincount(v, minlength=N)
        coll = c[v] > 1
        if s <= h - 1:
            esc = lambda q: (q >> (L - s + 1)) == (1 << (s - 1)) - 1
        else:
            esc = lambda q: (q >> s) == ((1 << (L - s)) - 2)
        allones = (1 << L) - 1
        tRP = (idx >= M) & (idx <= N - 2) & ispal[R]
        tRp = (idx >= M) & (idx <= N - 2) & ispal[Rn]
        pred = (tRP & ~esc(R)) | (tRp & ~esc(Rn) & (Rn != allones))
        partners = coll & ~pred
        ok = bool(c.max() <= 2 and np.all(coll[pred]) and int(partners.sum()) == int(pred.sum())
                  and not np.any((tRP | tRp)[partners]) and int(pred.sum()) == N - int(np.count_nonzero(c)))
        allok &= ok
        rows.append((s, int(pred.sum()), ok))
    out[L] = rows
    print(L, ' '.join(f's{s}:{k}{"" if ok else "!"}' for s, k, ok in rows))
print('owner holds at every checked cell:', allok)
json.dump({'all_ok': allok, 'by_L': out}, open(os.path.join(here, 'frame_owner_results.json'), 'w'), indent=1)
