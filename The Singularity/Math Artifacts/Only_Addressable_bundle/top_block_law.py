"""Top-of-order law for the nested-ring representatives.
Representative: x < P(x), P = reverse unless palindrome, then complement.
L bits, h = floor(L/2), mu = 1 (L even) or 2 (L odd).
LEMMA A (count):  for left half l >= 2^(h-1),  #reps with left half l  =  mu * (2^h - 1 - l).
COROLLARY (blocks): descending from the top, block K (K = 2^h-1-l = 0,1,2,..) holds mu*K reps;
   rep_(j) (j-th largest, 0-indexed) lies in block K with mu*K(K-1)/2 <= j < mu*K(K+1)/2.
LEMMA B (power-of-two block): K = 2^n has only completions with pair t = (0,1); offset r -> code v = mu*2^n-1-r;
   word(M+j) = reverse(rep_(j)) = 1^(t+1) [code read leftward from index ceil(L/2)-1] 1^n 0 1^t,  t = h-n-1.
THEOREM C (seam offsets 2^s, s != L mod 2):
   Z(word(M+2^s))   = { ceil(L/2)-1,               ceil(L/2)+ceil(s/2) }
   Z(word(M+2^s+1)) = { floor(L/2)-ceil(s/2), ceil(L/2)-1, ceil(L/2)+ceil(s/2) }   (s>=2 if L even)
THEOREM D (pad): word(M+j, L+2) = '1' + word(M+j, L) + '1'  throughout the top quarter.
"""
import sys, math, time
sys.path.insert(0, "/home/claude/space/rings")
from witness_Kd import word_at, part, is_rep

def zeros(w): return {i for i, c in enumerate(w) if c == "0"}
t0 = time.time()

# ---- Lemma A, exhaustive -------------------------------------------------
print("LEMMA A  #reps with left half l  ==  mu*(2^h-1-l)   for all l >= 2^(h-1)")
okA = True
for L in range(3, 21):
    h, mu = L // 2, 1 + (L & 1)
    cnt = {}
    for x in range(1 << L):
        if x >> (L - 1) and is_rep(x, L):          # x0 = 1
            l = x >> (L - h); cnt[l] = cnt.get(l, 0) + 1
    bad = [l for l in range(1 << (h - 1), 1 << h) if cnt.get(l, 0) != mu * ((1 << h) - 1 - l)]
    okA &= not bad
    if L in (3, 4, 9, 10, 15, 16, 19, 20) or bad:
        print(f"  L={L:2d}  left halves checked {1 << (h-1):6d}   {'holds' if not bad else 'FAILS '+str(bad[:5])}")
print(f"  Lemma A, L = 3..20 exhaustive: {'holds' if okA else 'FAILS'}   ({time.time()-t0:.0f}s)")

# ---- block-law word, vs the O(L) reader -------------------------------------
def block_word(j, L):
    """word at ring position M+j (j>=1) from the block law alone (no ring, no DP)."""
    h, mu = L // 2, 1 + (L & 1)
    K = 1
    while mu * K * (K + 1) // 2 <= j: K += 1
    r = j - mu * K * (K - 1) // 2                     # offset in block
    assert K < (1 << (h - 1)), "outside the top region"
    l = (1 << h) - 1 - K                              # left half
    lbits = format(l, f"0{h}b"); t = lbits.index("0"); w = lbits[t + 1:]; n = len(w)
    # completions in descending order: code c = (mid, rho_{h-1} .. rho_{t+1}), then rho_t in (1,0)
    comps = []
    for c in range(mu * (1 << n) - 1, -1, -1):
        cb = format(c, f"0{n + (L & 1)}b") if n + (L & 1) else ""
        mid = cb[0] if L & 1 else ""
        rho_hi = cb[1:] if L & 1 else cb             # rho_{h-1} .. rho_{t+1}
        inner = rho_hi[::-1]                          # rho_{t+1} .. rho_{h-1}
        for rt in "10":
            if rt == "0":                             # first asymmetric inner pair must be (0,1)
                good = False
                for wk, rk in zip(w, inner):
                    if wk != rk: good = (wk == "0"); break
                if not good: continue
            comps.append(mid + rho_hi + rt)
    rest = comps[r]
    rep = lbits + rest + "1" * t
    return rep[::-1]

print("\nBLOCK LAW  word(M+j) from blocks == word_at(M+j)  (exhaustive top region, L = 4..18)")
okB = True
for L in range(4, 19):
    h, mu = L // 2, 1 + (L & 1); M = 1 << (L - 1)
    jmax = mu * ((1 << (h - 1)) - 1) * (1 << (h - 1)) // 2      # rows in blocks K < 2^(h-1)
    bad = [j for j in range(1, jmax) if block_word(j, L) != word_at(M + j, L)]
    okB &= not bad
    if L in (4, 5, 10, 11, 17, 18) or bad:
        print(f"  L={L:2d}  offsets 1..{jmax-1:6d}  ({100*jmax/M:4.1f}% of the half-ring)  {'match' if not bad else 'FAIL '+str(bad[:4])}")
print(f"  block law: {'matches' if okB else 'FAILS'}   ({time.time()-t0:.0f}s)")

# ---- Theorem C at large L via the O(L) reader -----------------------------
print("\nTHEOREM C  zero sets at seam offsets 2^s and 2^s+1 (s != L mod 2), L = 6..160")
okC = 0; nC = 0
for L in range(6, 161):
    h, cl = L // 2, (L + 1) // 2; M = 1 << (L - 1)
    for s in range(0, L // 2 - 1):
        if (s - L) % 2 == 0: continue
        n = (s + 1) // 2
        if n > h - 2: break
        z1 = zeros(word_at(M + (1 << s), L))
        nC += 1; okC += z1 == {cl - 1, cl + n}
        if s >= 2 or L & 1:
            z2 = zeros(word_at(M + (1 << s) + 1, L))
            nC += 1; okC += z2 == {h - n, cl - 1, cl + n}
print(f"  {okC}/{nC} zero sets exact   ({time.time()-t0:.0f}s)")

# ---- Theorem D: pad law ---------------------------------------------------
print("\nTHEOREM D  word(M+j, L+2) == 1 + word(M+j, L) + 1   across the top region of ring L")
okD = True
for L in range(4, 17):
    h, mu = L // 2, 1 + (L & 1)
    jmax = mu * ((1 << (h - 1)) - 1) * (1 << (h - 1)) // 2
    bad = [j for j in range(1, jmax) if word_at((1 << (L + 1)) + j, L + 2) != "1" + word_at((1 << (L - 1)) + j, L) + "1"]
    okD &= not bad
    if bad: print(f"  L={L}: FAIL at {bad[:5]}")
print(f"  pad law L = 4..16 -> L+2: {'holds' if okD else 'FAILS'}   ({time.time()-t0:.0f}s)")
