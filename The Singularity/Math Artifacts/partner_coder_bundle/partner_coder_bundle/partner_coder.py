"""partner_coder.py - an LZ pre-pass whose extra match type is the partner (reverse complement), then lzma.
Way home for seal_partner_coder.txt (P1-P5). Dean A. Kulik, QuHarmonics Research Group, ORCID 0009-0003-3128-8828."""
import hashlib, json, lzma, os, random, subprocess, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SEAL = open(os.path.join(HERE, 'seal_partner_coder.txt'), 'rb').read()
assert hashlib.sha256(SEAL).hexdigest() == '88618d1325d650d7c9e82dd9cf6c6dd0a2ce8ade3aae42d298bbf91290d10c0d', 'seal mismatch'
K, LMIN = 24, 32
LZ = lambda b: len(lzma.compress(b, preset=9 | lzma.PRESET_EXTREME))
COMP = str.maketrans('ACGT', 'TGCA')
def rc(s): return s.translate(COMP)[::-1]

def fetch(acc, url):
    d = os.path.join(HERE, f'data_{acc}')          # data lives in its own directory
    os.makedirs(d, exist_ok=True); p = os.path.join(d, f'{acc}.gb')
    if not os.path.exists(p):
        subprocess.run(['curl', '-sS', '--fail', '--max-time', '120', '-o', p, url], check=True)
    txt = open(p, encoding='ascii', errors='replace').read()
    seq = txt.split('\nORIGIN', 1)[1].split('\n//', 1)[0]
    return ''.join(ch for ch in seq if ch.isalpha()).upper(), hashlib.sha256(open(p, 'rb').read()).hexdigest()

def varints(nums):
    out = bytearray()
    for v in nums:
        while True:
            b = v & 0x7F; v >>= 7
            out.append(b | (0x80 if v else 0))
            if not v: break
    return bytes(out)

def encode(S, mode):
    """greedy parse; mode 'rc' (partner copies) or 'fwd' (forward copies, control)"""
    N = len(S); base = np.frombuffer(S.encode(), dtype=np.uint8).astype(np.int64)
    lut = np.full(256, -1, dtype=np.int64)
    for ch, v in zip(b'ACGT', range(4)): lut[ch] = v
    b = lut[base]; bad = (b < 0).astype(np.int64)
    W = N - K + 1
    if W <= 0: return S, [], []
    code = np.zeros(W, dtype=np.uint64); rcode = np.zeros(W, dtype=np.uint64)
    for t in range(K):
        code = (code << np.uint64(2)) | (b[t:t + W] & 3).astype(np.uint64)
        rcode = (rcode << np.uint64(2)) | ((3 - b[K - 1 - t:K - 1 - t + W]) & 3).astype(np.uint64)
    cb = np.concatenate([[0], np.cumsum(bad)]); valid = (cb[K:K + W] - cb[:W]) == 0
    pos = np.flatnonzero(valid); uniq, fi = np.unique(code[pos], return_index=True); first = pos[fi]
    key = rcode if mode == 'rc' else code
    j = np.searchsorted(uniq, key); jc = np.minimum(j, len(uniq) - 1)
    hit = valid & (j < len(uniq)) & (uniq[jc] == key)
    src = np.where(hit, first[jc], -1)
    i_all = np.arange(W)
    ok = (src >= 0) & ((src + K <= i_all) if mode == 'rc' else (src < i_all))
    cands = np.flatnonzero(ok); src = src.tolist()
    lits, tokens, spans = [], [], []
    i = 0; ci = 0; nc = len(cands)
    while True:
        while ci < nc and cands[ci] < i: ci += 1
        if ci >= nc: break
        p = int(cands[ci]); s = src[p]; L = K
        if mode == 'rc':
            while p + L < N and s - 1 >= 0 and b[p + L] >= 0 and b[p + L] == 3 - b[s - 1]:
                L += 1; s -= 1
        else:
            while p + L < N and b[p + L] >= 0 and b[p + L] == b[s + L]:
                L += 1
        if L < LMIN:
            ci += 1; continue
        lits.append(S[i:p]); tokens.append((p - i, p - s, L)); spans.append((p, p + L, s, s + L if mode == 'rc' else s + L))
        i = p + L
    lits.append(S[i:])
    return ''.join(lits), tokens, spans

def decode(lit, tokens, mode):
    out = bytearray(); lp = 0; litb = lit.encode()
    for lr, dist, L in tokens:
        out += litb[lp:lp + lr]; lp += lr
        i = len(out)
        if mode == 'rc':
            s = i - dist; out += rc(out[s:s + L].decode()).encode()      # the partner of an earlier stretch
        else:
            j = i - dist
            for t in range(L): out.append(out[j + t])                    # forward copy, overlap allowed
    out += litb[lp:]
    return out.decode()

def size(lit, tokens):
    tb = varints([v for t in tokens for v in t])
    return LZ(lit.encode()) + (LZ(tb) if tokens else 0), len(tb)

def run(name, S):
    raw = LZ(S.encode()); res = {'length': len(S), 'non_ACGT': sum(1 for c in S if c not in 'ACGT'), 'lzma_raw': raw}
    for mode in ('rc', 'fwd'):
        t0 = time.time(); lit, tok, spans = encode(S, mode)
        back = decode(lit, tok, mode); exact = back == S
        sz, tb = size(lit, tok); cov = sum(L for _, _, L in tok) / len(S)
        res[mode] = {'size': sz, 'ratio': sz / raw, 'tokens': len(tok), 'token_bytes_raw': tb, 'coverage': cov,
                     'longest': max([L for _, _, L in tok], default=0), 'exact_decode': exact, 'seconds': time.time() - t0,
                     'top_copies': sorted([{'at': a, 'to': e, 'from': s0, 'from_end': s1, 'length': e - a} for a, e, s0, s1 in spans],
                                          key=lambda d: -d['length'])[:5]}
    return res

if __name__ == '__main__':
    T = time.time(); print('seal verified 88618d13...0d10c0d')
    S, digest = fetch('NC_000932', 'https://raw.githubusercontent.com/biopython/biopython/master/Tests/GenBank/NC_000932.gb')
    print(f'NC_000932: {len(S):,} bases, record sha256 {digest[:16]}...')
    R = ''.join(random.Random(20261020).choices('ACGT', k=len(S)))
    out = {'seal': hashlib.sha256(SEAL).hexdigest(), 'record_sha256': digest,
           'NC_000932': run('NC_000932', S), 'RANDOM': run('RANDOM', R)}
    g, r = out['NC_000932'], out['RANDOM']
    for nm, d in (('NC_000932', g), ('RANDOM', r)):
        print(f"\n{nm}: lzma raw {d['lzma_raw']:,} bytes ({8*d['lzma_raw']/d['length']:.3f} bits/base)")
        for mode in ('rc', 'fwd'):
            m = d[mode]
            print(f"  {mode:3s} pass: {m['size']:,} bytes  ratio {m['ratio']:.4f}  copies {m['tokens']}  coverage {m['coverage']:.4f}  "
                  f"longest {m['longest']:,}  exact {m['exact_decode']}  ({m['seconds']:.1f}s)")
        for c in d['rc']['top_copies'][:3]:
            print(f"     partner copy: [{c['at']:,}, {c['to']:,}) = RC of [{c['from']:,}, {c['from_end']:,})  length {c['length']:,}")
    P = {'P1': g['rc']['coverage'] >= 0.15 and g['rc']['longest'] >= 20000,
         'P2': g['rc']['ratio'] <= 0.87,
         'P3': g['fwd']['ratio'] >= 0.99,
         'P4': r['rc']['tokens'] == 0 and 0.995 <= r['rc']['ratio'] <= 1.01,
         'P5': all(d[m]['exact_decode'] for d in (g, r) for m in ('rc', 'fwd'))}
    print()
    for k, v in P.items(): print(f'{k}: {"RUNS" if v else "DEAD END"}')
    out['P'] = P; out['seconds'] = time.time() - T
    json.dump(out, open(os.path.join(HERE, 'partner_coder_results.json'), 'w'), indent=2, default=lambda o: int(o) if isinstance(o, np.integer) else float(o))
    print(f"({out['seconds']:.1f}s)")
