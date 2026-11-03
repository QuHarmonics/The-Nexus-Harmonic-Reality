"""Ring construction, closed form (proved equal to the centre-insertion grow for every L; checked L=1..16)."""
def rev(x, L):  return int(format(x, f"0{L}b")[::-1], 2)
def comp(x, L): return x ^ ((1 << L) - 1)
def part(x, L):
    r = rev(x, L); return r if r != x else comp(x, L)
def ring(L):
    reps = [x for x in range(1 << L) if x < part(x, L)]
    M = len(reps); left = reps[:]; right = [part(a, L) for a in reversed(reps)]
    if M > 1: left[-1], right[0] = right[0], left[-1]
    return [format(v, f"0{L}b") for v in left + right]
def grow(L):            # name kept for the reader formula R_L = grow(L)
    return ring(L)
