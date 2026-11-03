"""Run of seal_witness.txt (W2C): one angle reads q_D at every depth D >= 13, all residues mod 3.
Dean A. Kulik, QuHarmonics Research Group, ORCID 0009-0003-3128-8828."""
import sys, os, json, time, hashlib
from fractions import Fraction
from math import floor
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, '..', 'wheels'))
import wheels as wh

T0 = time.time()
seal = hashlib.sha256(open(os.path.join(here, 'seal_witness.txt'), 'rb').read()).hexdigest()
print('seal', seal, flush=True)
DMAX = int(os.environ.get('DMAX', '400'))
_word_cache = {}


def word(i, L):
    key = (i, L)
    if key not in _word_cache:
        _word_cache[key] = wh.word(i, L)
    return _word_cache[key]


def profile(u, D):
    bits = []
    first_bad = None
    target = '1' + '00' + '1' * (D - 5) + '00'
    for L in range(1, D + 1):
        x = (1 << L) * u
        i = floor(x)
        k = floor(L * (x - i))
        wd = word(i, L)
        b = (wd >> (L - 1 - k)) & 1
        bits.append(str(b))
        if first_bad is None and str(b) != target[L - 1]:
            first_bad = dict(L=L, address_offset=i - (1 << (L - 1)), slice=k, word=format(wd, f'0{L}b'), read=b)
    return ''.join(bits) == target, first_bad


def angle(D, tau):
    t = (D - 2) // 3
    p = 2 * t + 3
    return Fraction(1, 2) + Fraction(1, 1 << p) + tau * Fraction(1, 1 << (D - 1)), p, t


def certificate(u, D):
    lo = Fraction(0)
    hi = Fraction(1)
    for L in range(1, D + 1):
        j = floor(L * (1 << L) * u)
        lo = max(lo, Fraction(j, L << L))
        hi = min(hi, Fraction(j + 1, L << L))
    return lo, hi


res = {'seal': seal, 'by_D': {}}
ok_all = {'left': True, 'centre': True, 'right': True, 'control': True, 'width': True}
fails = {k: [] for k in ok_all}
for D in range(13, DMAX + 1):
    taus = {'left': Fraction(2, 3) + Fraction(1, 6 * D),
            'centre': Fraction(2, 3) + Fraction(1, 4 * D),
            'right': Fraction(2, 3) + Fraction(1, 3 * D) - Fraction(1, 1 << (D + 20))}
    rec = {}
    for name, tau in taus.items():
        u, p, t = angle(D, tau)
        good, bad = profile(u, D)
        rec[name] = dict(ok=good, first_bad=bad)
        if not good:
            ok_all[name] = False
            fails[name].append(D)
    u0, p, t = angle(D, Fraction(2, 3))
    good0, bad0 = profile(u0, D)
    expect0 = (D % 3 != 2)
    rec['control_tau_2_3'] = dict(ok=good0, expected=expect0, first_bad=bad0)
    if good0 != expect0:
        ok_all['control'] = False
        fails['control'].append(D)
    rec['p'] = p
    rec['t'] = t
    if D <= 120:
        u, _, _ = angle(D, taus['centre'])
        lo, hi = certificate(u, D)
        w = hi - lo
        rec['certificate'] = dict(lo=str(lo), hi=str(hi), width=str(w), contains=(lo <= u < hi))
        if not (w > 0 and lo <= u < hi):
            ok_all['width'] = False
            fails['width'].append(D)
    res['by_D'][D] = rec
    if D <= 30 or D % 50 == 0:
        print(f'D={D:3d} (res {D % 3}) p={p:3d} t={t:3d}  left {rec["left"]["ok"]} centre {rec["centre"]["ok"]} right {rec["right"]["ok"]}'
              f'  tau=2/3 control {good0} (expected {expect0})', flush=True)
    if len(_word_cache) > 200000:
        _word_cache.clear()
res['ok'] = ok_all
res['failures'] = fails
res['seconds'] = time.time() - T0
res['seal_after'] = hashlib.sha256(open(os.path.join(here, 'seal_witness.txt'), 'rb').read()).hexdigest()
print('result', ok_all, 'failures', {k: v[:20] for k, v in fails.items()}, 'seconds %.1f' % res['seconds'],
      'seal unchanged', res['seal_after'] == seal)
json.dump(res, open(os.path.join(here, 'witness_results.json'), 'w'), indent=1, default=str)
