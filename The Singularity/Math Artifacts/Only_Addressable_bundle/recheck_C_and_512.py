"""Theorem C with the corrected hypothesis (s >= 2 for the 2^s+1 case, both parities), and the
512-bit round trip + pi-64 location with this session's O(L) rank/unrank."""
import sys, time, math, hashlib, random
sys.path.insert(0, "/home/claude/space/rings")
from witness_Kd import word_at, reps_below, part, is_rep
def zeros(w): return {i for i, c in enumerate(w) if c == "0"}
t0 = time.time(); ok = n = 0
for L in list(range(6, 81)) + [128, 129, 160, 161, 200, 201]:
    h, cl = L // 2, (L + 1) // 2; M = 1 << (L - 1)
    srange = range(0, L // 2 - 1) if L <= 80 else [s for s in range(0, L // 2 - 1) if s % 7 in (0, 1)]
    for s in srange:
        if (s - L) % 2 == 0: continue
        k = (s + 1) // 2
        if k > h - 2: break
        n += 1; ok += zeros(word_at(M + (1 << s), L)) == {cl - 1, cl + k}
        if s >= 2:
            n += 1; ok += zeros(word_at(M + (1 << s) + 1, L)) == {h - k, cl - 1, cl + k}
print(f"THEOREM C (s>=2 for 2^s+1): {ok}/{n} exact   ({time.time()-t0:.0f}s)", flush=True)

def location(x, L):
    N = 1 << L; M = N // 2
    rep = x if is_rep(x, L) else part(x, L); k = reps_below(rep, L)
    if M > 1 and k == M - 1: return M if x == rep else M - 1
    return k if x == rep else N - 1 - k
pi64 = 0x243F6A8885A308D3
pos = location(pi64, 64)
print(f"pi first 64 bits 0x243F6A8885A308D3 at position {pos:,};  word_at(pos)==x: {int(word_at(pos,64),2)==pi64};"
      f"  partner at N-1-pos: {location(part(pi64,64),64)==(1<<64)-1-pos}")
random.seed(20261019)
x = random.getrandbits(512) | (1 << 511)
t1 = time.time(); p = location(x, 512); back = int(word_at(p, 512), 2)
print(f"512-bit word (seeded 20261019): location computed; word_at(location)==x: {back==x};"
      f"  partner at N-1-pos: {location(part(x,512),512)==(1<<512)-1-p};  ({time.time()-t1:.1f}s)")
print(f"  sha256(x) {hashlib.sha256(x.to_bytes(64,'big')).hexdigest()[:16]}...   position has {p.bit_length()} bits")
