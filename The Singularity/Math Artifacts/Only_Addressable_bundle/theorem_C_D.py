"""THEOREM C (seam offsets 2^s, s != L mod 2), checked against the O(L) reader:
   Z(word(M+2^s))   = { ceil(L/2)-1,               ceil(L/2)+ceil(s/2) }
   Z(word(M+2^s+1)) = { floor(L/2)-ceil(s/2), ceil(L/2)-1, ceil(L/2)+ceil(s/2) }   (s>=2 if L even)
THEOREM D (pad): word(M+j, L+2) = '1' + word(M+j, L) + '1' throughout the top quarter of ring L."""
import sys, time
sys.path.insert(0, "/home/claude/space/rings")
from witness_Kd import word_at
def zeros(w): return {i for i, c in enumerate(w) if c == "0"}
t0 = time.time()

print("THEOREM C  zero sets at seam offsets 2^s and 2^s+1 (s != L mod 2)")
okC = nC = 0; fails = []
Ls = list(range(6, 81)) + [128, 129, 160, 161, 200, 201]
for L in Ls:
    h, cl = L // 2, (L + 1) // 2; M = 1 << (L - 1)
    srange = range(0, L // 2 - 1) if L <= 80 else [s for s in range(0, L // 2 - 1) if s % 7 in (0, 1)]
    for s in srange:
        if (s - L) % 2 == 0: continue
        n = (s + 1) // 2
        if n > h - 2: break
        z1 = zeros(word_at(M + (1 << s), L)); nC += 1
        if z1 == {cl - 1, cl + n}: okC += 1
        else: fails.append((L, s, "2^s"))
        if s >= 2 or L & 1:
            z2 = zeros(word_at(M + (1 << s) + 1, L)); nC += 1
            if z2 == {h - n, cl - 1, cl + n}: okC += 1
            else: fails.append((L, s, "2^s+1"))
print(f"  {okC}/{nC} zero sets exact  (L = 6..80 every admissible s; L = 128,129,160,161,200,201 sampled s)"
      f"  fails: {fails[:6] if fails else 'none'}   ({time.time()-t0:.0f}s)", flush=True)

print("\nTHEOREM D  word(M+j, L+2) == 1 + word(M+j, L) + 1  across the top quarter of ring L")
okD = True
for L in range(4, 17):
    h, mu = L // 2, 1 + (L & 1)
    jmax = mu * ((1 << (h - 1)) - 1) * (1 << (h - 1)) // 2
    bad = [j for j in range(1, jmax) if word_at((1 << (L + 1)) + j, L + 2) != "1" + word_at((1 << (L - 1)) + j, L) + "1"]
    okD &= not bad
    print(f"  L={L:2d} -> {L+2:2d}: offsets 1..{jmax-1:6d}  {'holds' if not bad else 'FAIL at '+str(bad[:5])}", flush=True)
print(f"  pad law: {'holds' if okD else 'FAILS'}   ({time.time()-t0:.0f}s)")
