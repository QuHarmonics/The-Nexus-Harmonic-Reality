"""Exact unnormalized comparator and cumulative-imbalance Walsh coefficients. Scalar queries only; no full arrays required."""
def comparator_from_reversed_mode(s, rs, n):
    d = s ^ rs
    if d.bit_count() != 2:
        return 0
    j = (d & -d).bit_length() - 1
    width = n - 2 * j - 2
    if width and s >> j + 1 & (1 << width) - 1:
        return 0
    sign = 1 if s >> n - 1 - j & 1 else -1
    return sign * (1 << n - j - 1)

def comparator_coefficient(s, n):
    if not 0 <= s < 1 << n:
        raise ValueError('mode outside word width')
    rs = int(format(s, f'0{n}b')[::-1], 2)
    return comparator_from_reversed_mode(s, rs, n)

def delta_coefficient(s, n):
    if n < 1 or not 0 <= s < 1 << n:
        raise ValueError('invalid mode or width')
    N = 1 << n
    if s == 0:
        numerator = N * (4 * N - 3 * n - 4 - (n & 1))
        assert numerator % 24 == 0
        return numerator // 24
    rs = int(format(s, f'0{n}b')[::-1], 2)
    if s.bit_count() % 2:
        value = -comparator_from_reversed_mode(s, rs, n)
        assert value % 2 == 0
        return value // 2
    j = (s & -s).bit_length() - 1
    value = -(1 << j) * comparator_from_reversed_mode(s ^ 1 << j, rs ^ 1 << n - 1 - j, n)
    for k in range(j):
        value += (1 << k) * comparator_from_reversed_mode(s ^ 1 << k, rs ^ 1 << n - 1 - k, n)
    assert value % 2 == 0
    return value // 2

if __name__=='__main__':
    for n in (2,3,4):
        print(n,[delta_coefficient(s,n) for s in range(1<<n)])
