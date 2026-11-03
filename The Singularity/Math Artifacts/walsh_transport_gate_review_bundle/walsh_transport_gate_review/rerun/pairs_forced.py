def partner(word):
    r = word[::-1]
    if r != word:
        return r
    return ''.join('1' if b == '0' else '0' for b in word)

def grow(n):
    if n < 1:
        raise ValueError('width must be >=1')
    words = [format(i, f'0{n}b') for i in range(1 << n)]
    first = [w for w in words if w < partner(w)]
    out = first + [partner(w) for w in reversed(first)]
    if n > 1:
        m = len(out) // 2
        out[m-1], out[m] = out[m], out[m-1]
    return out
