import hashlib

def partner(x):
    r = x[::-1]
    return r if r != x else ''.join(('1' if c == '0' else '0' for c in x))

def grow(L):
    seen, pairs = (set(), [])
    for w in range(1 << L):
        x = format(w, f'0{L}b')
        if x in seen:
            continue
        p = partner(x)
        seen |= {x, p}
        pairs.append((x, p))
    seq = []
    for i, (a, b) in enumerate(pairs):
        if i == len(pairs) - 1 and len(pairs) > 1:
            a, b = (b, a)
        m = len(seq) // 2
        seq = seq[:m] + [a, b] + seq[m:]
    return seq

def unfold(left_half):
    return list(left_half)+[partner(x) for x in reversed(left_half)]

def center_out(bits):
    m=len(bits)//2
    return [(bits[m-1-j],bits[m+j]) for j in range(m)]

def decode_center_out(pairs):
    return ''.join(a for a,b in reversed(pairs))+''.join(b for a,b in pairs)

if __name__=='__main__':
    for L in range(1,11):
        ring=grow(L)
        assert unfold(ring[:len(ring)//2])==ring
    for message in (b'',b'abc'):
        digest=hashlib.sha256(message).hexdigest()
        bits=format(int(digest,16),'0256b')
        pairs=center_out(bits)
        assert decode_center_out(pairs)==bits
        predicted=partner(bits[:128])
        print(message,digest)
        print('128-bit partner prediction mismatches:',sum(a!=b for a,b in zip(predicted,bits[128:])))
        print('Generated complementary 256-bit face:',format(int(partner(bits),2),'064x'))
