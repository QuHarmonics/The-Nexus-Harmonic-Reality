"""Run of seal_frames.txt (FA1): the frame-s readings of the ring tape at every offset.
Dean A. Kulik, QuHarmonics Research Group, ORCID 0009-0003-3128-8828."""
import sys, os, json, time, hashlib
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, '..', 'wheels'))
import numpy as np
import wheels as wh

T0 = time.time()
seal = hashlib.sha256(open(os.path.join(here, 'seal_frames.txt'), 'rb').read()).hexdigest()
print('seal', seal)


def law(L, s):
    h = L // 2
    P = 1 << ((L + 1) // 2)
    if s <= 1:
        return 0
    if s == L - 1:
        return P - 2
    if s <= h - 1:
        return P - (P >> (s - 2))
    if s == h:
        return P - 2 if L % 2 == 0 else P - 6
    return P - 2 - (1 << (s - h + 1))


def frame_words(R, L, s):
    Rn = np.roll(R, -1)
    lo = R & ((1 << (L - s)) - 1)
    return (lo << s) | (Rn >> (L - s))


out = {'seal': seal, 'by_L': {}}
seen_ok = fresh_ok = True
seen_cells = fresh_cells = 0
for L in range(2, 23):
    _, _, _, R, _ = wh.ring_arrays(L)
    N = 1 << L
    losses = []
    for s in range(L):
        w = frame_words(R, L, s)
        d = int(np.count_nonzero(np.bincount(w, minlength=N)))
        losses.append(N - d)
    pred = [law(L, s) for s in range(L)]
    ok = losses == pred
    if L <= 16:
        seen_ok &= ok
        seen_cells += L
    else:
        fresh_ok &= ok
        fresh_cells += L
    out['by_L'][L] = dict(loss=losses, law=pred, ok=ok)
    print(f'L={L:2d} {"fresh" if L > 16 else "seen "} law {"holds" if ok else "FAILS"}  loss ' + ' '.join(map(str, losses)))
    if not ok:
        print('      predicted ' + ' '.join(map(str, pred)))
out['seen'] = dict(cells=seen_cells, ok=seen_ok)
out['fresh'] = dict(cells=fresh_cells, ok=fresh_ok)
out['seconds'] = time.time() - T0
out['seal_after'] = hashlib.sha256(open(os.path.join(here, 'seal_frames.txt'), 'rb').read()).hexdigest()
print('seen widths 2-16:', seen_cells, 'cells, law', seen_ok, '| fresh widths 17-22:', fresh_cells, 'cells, law', fresh_ok,
      '| seconds %.1f' % out['seconds'], '| seal unchanged', out['seal_after'] == seal)
json.dump(out, open(os.path.join(here, 'frame_results.json'), 'w'), indent=1)
