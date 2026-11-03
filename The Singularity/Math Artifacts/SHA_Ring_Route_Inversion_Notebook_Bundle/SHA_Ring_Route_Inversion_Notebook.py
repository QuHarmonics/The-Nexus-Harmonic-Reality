
# Ring-addressed SHA-256 route test

# Run guide

from hashlib import sha256
from functools import lru_cache
from time import perf_counter
import json

MASK = 0xffffffff

# FIPS 180-4 SHA-256 initial state and round constants.
IV = [
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19,
]
K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
    0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
    0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
    0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
    0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
    0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
]
assert len(IV) == 8 and len(K) == 64
print('SHA-256 constants loaded:', len(IV), 'IV words,', len(K), 'round constants')

# 1. Partner map and rule-based ring ordering

# Fast bit-reversal table used by the streaming ring generator.
REV8 = bytes(int(f"{i:08b}"[::-1], 2) for i in range(256))

def reverse_bits_bytes(x: int, L: int) -> int:
    if L % 8:
        return int(format(x, f"0{L}b")[::-1], 2)
    n = L // 8
    out = 0
    for i in range(n):
        out |= REV8[(x >> (8*i)) & 255] << (8*(n-1-i))
    return out

def partner(x: int, L: int) -> int:
    r = reverse_bits_bytes(x, L)
    return r if r != x else x ^ ((1 << L) - 1)

def is_representative(x: int, L: int) -> bool:
    r = reverse_bits_bytes(x, L)
    return x < r or (x == r and ((x >> (L-1)) & 1) == 0)

def ring_stream(L: int):
    """Yield the exact center-twisted ring order, without a stored ring table."""
    if L < 1 or L % 8:
        raise ValueError('SHA-message ring width must be a positive multiple of 8')
    N = 1 << L
    M = N // 2
    max_rep = next(x for x in range(N-1, -1, -1) if is_representative(x, L))
    count = 0
    for x in range(max_rep):
        if is_representative(x, L):
            yield x
            count += 1
    # center twist: swap max representative and its partner across the seam
    yield partner(max_rep, L); count += 1
    yield max_rep; count += 1
    for x in range(max_rep-1, -1, -1):
        if is_representative(x, L):
            yield partner(x, L)
            count += 1
    assert count == N, (L, count, N)

def cmp(a, b):
    return (a > b) - (a < b)

@lru_cache(maxsize=8192)
def representatives_below(t: int, L: int) -> int:
    """Count canonical representatives a with a < t using mirrored-pair digit DP."""
    if t <= 0: return 0
    if t >= (1 << L): return 1 << (L-1)
    bound = format(t-1, f'0{L}b')
    states = {(0, 0, 0, -1): 1}
    for i in range(L//2):
        nxt = {}
        left = int(bound[i]); right = int(bound[L-1-i])
        for (cl, cr, cj, first), n in states.items():
            for a in (0,1):
                for b in (0,1):
                    key = (
                        cl if cl else cmp(a, left),
                        cmp(b, right) or cr,
                        cj if cj else cmp(a, b),
                        a if i == 0 else first,
                    )
                    nxt[key] = nxt.get(key, 0) + n
        states = nxt
    total = 0
    for (cl, cr, cj, first), n in states.items():
        for mid in ((0,1) if L % 2 else (None,)):
            comparison = cl or (cmp(mid, int(bound[L//2])) if mid is not None else 0) or cr
            first_bit = mid if first == -1 else first
            if comparison <= 0 and (cj < 0 or (cj == 0 and first_bit == 0)):
                total += n
    return total

def representative_at(k: int, L: int) -> int:
    if not 0 <= k < (1 << (L-1)):
        raise ValueError('representative rank outside range')
    lo, hi = 0, (1 << L)-1
    while lo < hi:
        mid = (lo+hi)//2
        if representatives_below(mid+1, L) > k:
            hi = mid
        else:
            lo = mid+1
    return lo

def word_at(position: int, L: int) -> int:
    N = 1 << L; M = N//2
    if not 0 <= position < N:
        raise ValueError('ring position outside range')
    p = position
    if M > 1 and p in (M-1, M):
        p = N-1-p
    if p < M:
        return representative_at(p, L)
    return partner(representative_at(N-1-p, L), L)

def location(x: int, L: int) -> int:
    if not 0 <= x < (1 << L):
        raise ValueError('word outside width')
    N = 1 << L; M = N//2
    y = partner(x, L); a = min(x, y)
    k = representatives_below(a, L)
    p = k if x == a else N-1-k
    return N-1-p if M > 1 and p in (M-1, M) else p

# Exhaustive small-width ordering audit, plus larger-width address spot checks.
ring8 = list(ring_stream(8))
assert len(ring8) == 256 and len(set(ring8)) == 256
assert all(ring8[i] == word_at(i, 8) for i in range(256))
for L in (16,):
    for i in (0, 1, 7, (1 << (L-1))-1, (1 << (L-1)), (1 << L)-2, (1 << L)-1):
        # Streaming to a selected position is intentionally a spot-check only.
        got = next(v for j, v in enumerate(ring_stream(L)) if j == i)
        assert got == word_at(i, L), (L, i, got, word_at(i,L))
print('Ring order verified: all 256 width-8 positions; seven width-16 boundary positions.')

# 2. SHA-256 block schedule, forward round, and inverse round

def rotr(x, n):
    return ((x >> n) | (x << (32-n))) & MASK

def big0(x): return rotr(x,2) ^ rotr(x,13) ^ rotr(x,22)
def big1(x): return rotr(x,6) ^ rotr(x,11) ^ rotr(x,25)
def small0(x): return rotr(x,7) ^ rotr(x,18) ^ (x >> 3)
def small1(x): return rotr(x,17) ^ rotr(x,19) ^ (x >> 10)
def ch(x,y,z): return (x & y) ^ ((~x) & z)
def maj(x,y,z): return (x & y) ^ (x & z) ^ (y & z)

def pad_one_block(msg: bytes) -> bytes:
    if len(msg) > 55:
        raise ValueError('This notebook handles messages whose SHA-256 padding fits in one 64-byte block (0–55 bytes).')
    return msg + b'\x80' + bytes(56-len(msg)-1) + (8*len(msg)).to_bytes(8, 'big')

def schedule(block: bytes):
    if len(block) != 64:
        raise ValueError('SHA-256 compression block must be 64 bytes')
    W = [int.from_bytes(block[4*i:4*i+4], 'big') for i in range(16)]
    for t in range(16,64):
        W.append((small1(W[t-2]) + W[t-7] + small0(W[t-15]) + W[t-16]) & MASK)
    return W

def compress_block(block: bytes, state=None):
    if state is None: state = IV
    W = schedule(block)
    a,b,c,d,e,f,g,h = state
    for t in range(64):
        T1 = (h + big1(e) + ch(e,f,g) + K[t] + W[t]) & MASK
        T2 = (big0(a) + maj(a,b,c)) & MASK
        a,b,c,d,e,f,g,h = (T1+T2)&MASK, a,b,c, (d+T1)&MASK, e,f,g
    work = [a,b,c,d,e,f,g,h]
    out = [(x+y)&MASK for x,y in zip(state, work)]
    return out, work, W

def reverse_round(out, Wt, Kt):
    A,B,C,D,E,F,G,H = out
    a,b,c = B,C,D
    e,f,g = F,G,H
    T2 = (big0(a) + maj(a,b,c)) & MASK
    T1 = (A - T2) & MASK
    old_d = (E - T1) & MASK
    old_h = (T1 - big1(e) - ch(e,f,g) - Kt - Wt) & MASK
    return [a,b,c,old_d,e,f,g,old_h]

def inverse_core(terminal_work, W):
    s = list(terminal_work)
    for t in range(63, -1, -1):
        s = reverse_round(s, W[t], K[t])
    return s

def digest_words(digest: bytes):
    if len(digest) != 32: raise ValueError('expected a 32-byte SHA-256 digest')
    return [int.from_bytes(digest[i:i+4], 'big') for i in range(0,32,4)]

def terminal_work_from_digest(digest: bytes):
    # SHA-256 one-block feed-forward: digest word = IV word + final working word mod 2^32.
    return [(h0-iv) & MASK for h0,iv in zip(digest_words(digest), IV)]

def closes_at_iv(candidate_msg: bytes, target_digest: bytes) -> bool:
    W = schedule(pad_one_block(candidate_msg))
    return inverse_core(terminal_work_from_digest(target_digest), W) == IV

print('SHA-256 forward and inverse routines loaded.')

# 3. Arithmetic validation against `hashlib`

validation = []
for msg in (b'', b'\x00', b'\x01', b'A', b'OK', b'ABC', b'\x80', b'\xff'):
    out_words, work, W = compress_block(pad_one_block(msg))
    ours = b''.join(w.to_bytes(4, 'big') for w in out_words)
    standard = sha256(msg).digest()
    assert ours == standard, (msg, ours.hex(), standard.hex())
    assert inverse_core(work, W) == IV, msg
    validation.append({'message_hex': msg.hex(), 'digest_matches_hashlib': True, 'inverse_rounds_return_to_IV': True})
print(json.dumps(validation, indent=2))

# 4. Search function

def search_fixed_length(target_hex: str, nbytes: int, method='inverse', progress_every=1_000_000):
    """Search all nbytes-long messages in ring order; target digest is the search input."""
    if not 1 <= nbytes <= 3:
        raise ValueError('supported candidate lengths are 1, 2, or 3 bytes')
    if method not in ('inverse', 'forward'):
        raise ValueError("method must be 'inverse' or 'forward'")
    target = bytes.fromhex(target_hex)
    target_work = terminal_work_from_digest(target)
    total = 1 << (8*nbytes)
    hits = []
    started = perf_counter()
    inverse_tested = 0
    for pos, word in enumerate(ring_stream(8*nbytes)):
        msg = word.to_bytes(nbytes, 'big')
        if method == 'inverse':
            W = schedule(pad_one_block(msg))
            inverse_tested += 1
            match = inverse_core(target_work, W) == IV
        else:
            match = sha256(msg).digest() == target
        if match:
            # Always verify every returned hit with the exact inverse route.
            W = schedule(pad_one_block(msg))
            closes = inverse_core(target_work, W) == IV
            assert closes, 'digest match did not close through the inverse-round path'
            hits.append({
                'hex': msg.hex(),
                'latin1': msg.decode('latin1'),
                'ring_position': pos,
                'location_reader_agrees': location(word, 8*nbytes) == pos if nbytes <= 2 else None,
                'inverse_route_closes': closes,
            })
        visited = pos + 1
        if progress_every and visited % progress_every == 0:
            print(f'  visited {visited:,}/{total:,} ring addresses; current hits={len(hits)}')
    return {
        'nbytes': nbytes,
        'method': method,
        'target_digest': target.hex(),
        'declared_domain_size': total,
        'addresses_visited': visited,
        'full_domain_visited': visited == total,
        'inverse_route_tests_during_search': inverse_tested,
        'matches': hits,
        'elapsed_seconds': round(perf_counter()-started, 3),
    }

TARGET_A   = '559aead08264d5795d3909718cdd05abd49572e84fe55590eef31a88a08fdffd'
TARGET_OK  = '565339bc4d33d72817b583024112eb7f5cdf3e5eef0252d6ec1b9c9a94e12bb3'
TARGET_ABC = 'b5d4045c3f466fa91fe2cc6abe79232a1a57cdf104f7a26e716e0a1e2789df78'
print('Search function ready. Targets are fixed digests; source bytes are not passed into the search.')

# 5. Full one-byte domain: inverse-route test

result_1byte = search_fixed_length(TARGET_A, nbytes=1, method='inverse', progress_every=0)
assert result_1byte['addresses_visited'] == 256
assert result_1byte['full_domain_visited']
assert result_1byte['matches'] == [{
    'hex':'41', 'latin1':'A', 'ring_position':58,
    'location_reader_agrees':True, 'inverse_route_closes':True
}]
print(json.dumps(result_1byte, indent=2))

# 6. Full two-byte domain: inverse-route test

RUN_TWO_BYTE_TEST = True  # switch off to skip this ~10-second full inverse test
result_2byte = None
if RUN_TWO_BYTE_TEST:
    result_2byte = search_fixed_length(TARGET_OK, nbytes=2, method='inverse', progress_every=0)
    assert result_2byte['addresses_visited'] == 65536
    assert result_2byte['full_domain_visited']
    assert len(result_2byte['matches']) == 1
    assert result_2byte['matches'][0]['hex'] == '4f4b'
    assert result_2byte['matches'][0]['ring_position'] == 17194
    print(json.dumps(result_2byte, indent=2))
else:
    print('Skipped by RUN_TWO_BYTE_TEST=False')

# 7. Optional full three-byte domain

RUN_FULL_THREE_BYTE_DOMAIN = False
result_3byte = None
if RUN_FULL_THREE_BYTE_DOMAIN:
    result_3byte = search_fixed_length(TARGET_ABC, nbytes=3, method='forward', progress_every=2_000_000)
    assert result_3byte['addresses_visited'] == 1 << 24
    assert result_3byte['full_domain_visited']
    assert len(result_3byte['matches']) == 1
    assert result_3byte['matches'][0]['hex'] == '414243'
    assert result_3byte['matches'][0]['ring_position'] == 3_732_208
    print(json.dumps(result_3byte, indent=2))
else:
    print('Skipped. Set RUN_FULL_THREE_BYTE_DOMAIN=True to scan all 16,777,216 addresses.')

# 8. Optional variable-length route: 0–3 bytes

RUN_VARIABLE_LENGTH_0_TO_3 = False
variable_length_result = None
if RUN_VARIABLE_LENGTH_0_TO_3:
    target = bytes.fromhex(TARGET_ABC)
    started = perf_counter()
    layers = []
    recovered = None
    # Layer 0: the empty message has no positive-width ring.
    if sha256(b'').digest() == target:
        recovered = {'nbytes':0, 'hex':'', 'ring_position':None}
    layers.append({'nbytes':0, 'addresses_tested':1, 'match':recovered is not None})
    if recovered is None:
        for nbytes in (1,2,3):
            tested = 0
            for pos, word in enumerate(ring_stream(8*nbytes)):
                tested += 1
                msg = word.to_bytes(nbytes, 'big')
                if sha256(msg).digest() == target:
                    W = schedule(pad_one_block(msg))
                    assert inverse_core(terminal_work_from_digest(target), W) == IV
                    recovered = {'nbytes':nbytes, 'hex':msg.hex(), 'ring_position':pos, 'inverse_route_closes':True}
                    break
            layers.append({'nbytes':nbytes, 'addresses_tested':tested, 'match':recovered is not None})
            if recovered is not None: break
    variable_length_result = {
        'target_digest':target.hex(),
        'declared_domain':'all strings of length 0, 1, 2, or 3 bytes',
        'layers':layers,
        'candidates_tested':sum(x['addresses_tested'] for x in layers),
        'recovered':recovered,
        'elapsed_seconds':round(perf_counter()-started, 3),
        'full_union_exhausted':all(x['addresses_tested'] == (1 << (8*x['nbytes'])) for x in layers),
    }
    assert recovered and recovered['hex'] == '414243'
    print(json.dumps(variable_length_result, indent=2))
else:
    print('Skipped. Set RUN_VARIABLE_LENGTH_0_TO_3=True to run the bounded variable-length search.')

# 9. PQLS / non-enumerative selector extension point

def summarize_results(*results):
    """Compact audit summary for whichever search cells were run."""
    out = []
    for r in results:
        if r is None: continue
        out.append({
            'nbytes': r.get('nbytes'),
            'method': r.get('method', 'layered'),
            'visited': r.get('addresses_visited', r.get('candidates_tested')),
            'full_domain_or_union_exhausted': r.get('full_domain_visited', r.get('full_union_exhausted')),
            'matches': r.get('matches', r.get('recovered')),
            'seconds': r.get('elapsed_seconds'),
        })
    return out

print(json.dumps(summarize_results(result_1byte, result_2byte, result_3byte, variable_length_result), indent=2))

# Interpretation boundary
