"""Scalar position map: no ring arrays or candidate enumeration. Derived from the separately sealed audit."""
def reverse(x, L):
    return int(format(x, f'0{L}b')[::-1], 2)

def partner(x, L):
    r = reverse(x, L)
    return r if r != x else x ^ (1 << L) - 1

def rectangle(u, v, h):
    H = 1 << h
    if u <= 0 or v <= 0:
        return 0
    if u >= H:
        return min(v, H)
    if v >= H:
        return min(u, H)
    U = format(u - 1, f'0{h}b')
    V = format(v - 1, f'0{h}b')
    states = {(0, 0): 1}
    cmp = lambda a, b: (a > b) - (a < b)
    for j in range(h):
        new = {}
        for (left, right), count in states.items():
            for bit in (0, 1):
                key = (left or cmp(bit, int(U[j])), cmp(bit, int(V[h - 1 - j])) or right)
                new[key] = new.get(key, 0) + count
        states = new
    return sum((n for (left, right), n in states.items() if left <= 0 and right <= 0))

def Q(z, L):
    h = L // 2
    H = 1 << h
    A = z >> h
    B = z & H - 1
    K1 = 2 * H - 1 - A
    D1 = K1 * (K1 - 1) // 2 + (H - 1 - A)
    return D1 + 2 * (H - 1 - B) - A + rectangle(B + 1, A, h)

def physical_position(q, n):
    M = 1 << n - 1
    return M if q == 0 else M - 1 - q

def _offsets_given_j(x, L, j):
    assert L % 2 == 0 and x < partner(x, L)
    h = L // 2
    H = 1 << h
    A = x >> h
    B = x & H - 1
    K = H - 1 - A
    s = max(0, K - H // 2) + int(A < H // 2 and reverse(A, h) > B)
    p = partner(x, L)
    qx = Q(x, L)
    qp = Q(p, L)
    return {'E0': qx + 1, 'G0': qx, 'E1': j - s if x != reverse(x, L) else qp + 1, 'G1': qp}

def rank_below(t, L):
    if t <= 0:
        return 0
    if t >= 1 << L:
        return 1 << L - 1
    b = format(t - 1, f'0{L}b')
    states = {(0, 0, 0, -1): 1}
    cmp = lambda a, b: (a > b) - (a < b)
    for i in range(L // 2):
        new = {}
        for (cl, cr, cj, first), n in states.items():
            for a in (0, 1):
                for c in (0, 1):
                    key = (cl or cmp(a, int(b[i])), cmp(c, int(b[L - 1 - i])) or cr, cj or cmp(a, c), a if i == 0 else first)
                    new[key] = new.get(key, 0) + n
        states = new
    return sum((n for (cl, cr, cj, first), n in states.items() if (cl or cr) <= 0 and (cj < 0 or (cj == 0 and first == 0))))

def target_positions(x,L):
    if L<2 or L%2 or not 0<=x<1<<L or not x<partner(x,L):
        raise ValueError('canonical representative of positive even width required')
    j=(1<<(L-1))-1-rank_below(x,L)
    offsets=_offsets_given_j(x,L,j)
    raw=(1<<(L+1))|(x<<1)|1
    words={'E0':x<<1,'G0':(x<<1)|1,'E1':min(raw,partner(raw,L+2)),'G1':(partner(x,L)<<1)|1}
    return {name:{'word':words[name],'descending_offset':q,'absolute_position':physical_position(q,L+2),'partner_position':(1<<(L+2))-1-physical_position(q,L+2)} for name,q in offsets.items()}

if __name__=='__main__':
    import json
    print(json.dumps(target_positions(0b1011,4),indent=2))
