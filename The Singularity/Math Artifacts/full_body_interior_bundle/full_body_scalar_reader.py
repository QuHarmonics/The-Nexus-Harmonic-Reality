"""Full original-ring scalar reader and Delta rank. Derived convenience module; the separate audit source is the sealed artifact. body_at returns twice the Walsh-even latitude."""
import math

def reverse_bits(x, h):
    return int(format(x, f'0{h}b')[::-1], 2) if h else 0

def rectangle(u, v, h):
    H = 1 << h
    if u <= 0 or v <= 0:
        return 0
    if u >= H:
        return min(v, H)
    if v >= H:
        return min(u, H)
    total = 0
    rho = 0
    for j in range(h):
        bit = u >> h - 1 - j & 1
        if bit:
            d = 1 << j + 1
            total += (v - rho + d - 1) // d
            rho += 1 << j
    return total

def delta(p, n):
    if p in (0, 1 << n):
        return 0
    h = n // 2
    H = 1 << h
    B = p & H - 1
    if n % 2 == 0:
        A = p >> h
        base = A * (H - A)
    else:
        A = p >> h + 1
        middle = p >> h & 1
        base = 2 * A * (H - A) + middle * (H - 1 - 2 * A)
    return base + B - 2 * rectangle(B, A, h) - int(reverse_bits(A, h) < B)

def palindrome_from_prefix(u, n):
    m = (n + 1) // 2
    return u << m | reverse_bits(u, m) if n % 2 == 0 else u << m - 1 | reverse_bits(u >> 1, m - 1)

def palindrome_count_below(p, n):
    if p <= 0:
        return 0
    if p >= 1 << n:
        return 1 << (n + 1) // 2
    m = (n + 1) // 2
    u = p >> n - m
    return u + int(palindrome_from_prefix(u, n) < p)

def rank_below(p, n):
    pi = palindrome_count_below(p, n)
    T = min(pi, 1 << (n + 1) // 2 - 1)
    value = p - pi + delta(p, n)
    assert value % 2 == 0
    return value // 2 + T

def partner(word, n):
    r = reverse_bits(word, n)
    return r if r != word else word ^ (1 << n) - 1

def location(word, n):
    p = partner(word, n)
    a = min(word, p)
    r = rank_below(a, n)
    N = 1 << n
    M = N // 2
    i = r if a == word else N - 1 - r
    return N - 1 - i if n > 1 and i in (M - 1, M) else i

def reverse_order_select(S, i):
    residue = 0
    for j in range((S - 1).bit_length()):
        count0 = max(0, (S - 1 - residue) // (1 << j + 1) + 1)
        if i >= count0:
            i -= count0
            residue += 1 << j
    assert i == 0 and residue < S
    return residue

def word_at(i, n):
    if n < 1 or not 0 <= i < 1 << n:
        raise ValueError('invalid width or address')
    if n == 1:
        return i
    N = 1 << n
    M = N // 2
    if not 0 <= i < N:
        raise ValueError('ring position out of range')
    q = i - M if i >= M else M - 1 - i
    h = n // 2
    H = 1 << h
    nu = 1 if n % 2 == 0 else 2
    Q = q // nu
    boundary = H // 2 * (H // 2 - 1) // 2
    if Q < boundary:
        K = (1 + math.isqrt(1 + 8 * Q)) // 2
    else:
        K = (math.isqrt(1 + 8 * (Q + H // 2)) - 1) // 2
    e = int(K >= H // 2)
    S = K + e
    D = K * (K - 1) // 2 + max(0, K - H // 2)
    offset = q - nu * D
    if nu == 1:
        middle = None
        inside = offset
    else:
        middle = int(offset < S)
        inside = offset if middle else offset - S
    r = reverse_order_select(S, inside)
    A = H - 1 - K
    B = H - 1 - reverse_bits(r, h)
    a = A << h | B if middle is None else A << h + 1 | middle << h | B
    canonical_on_right = q == 0
    return a if (i >= M) == canonical_on_right else partner(a, n)

def body_at(i, n):
    x = word_at(i, n)
    return 0 if x == reverse_bits(x, n) else 2 * x.bit_count() - n

def popcount_sum(S):
    total = 0
    for j in range(S.bit_length()):
        half = 1 << j
        period = 2 * half
        total += S // period * half + max(0, S % period - half)
    return total

if __name__=='__main__':
    for i in range(16):
        x=word_at(i,4)
        assert location(x,4)==i
        print(i,format(x,'04b'),body_at(i,4)/2)
