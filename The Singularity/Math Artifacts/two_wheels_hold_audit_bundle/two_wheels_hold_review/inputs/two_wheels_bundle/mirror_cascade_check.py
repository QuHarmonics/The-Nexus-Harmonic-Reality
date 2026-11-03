"""Derived after the W4 run (not sealed): at t = 2^L the hold of ring L+k is 2^L - (2^(L-k) - 2^ceil((L-k)/2)), 1 <= k <= L.
Owner: Route 3's 00 frame. Below 2^L a partner of ring L+k must be 0^k m 0^k with m a non-palindromic partner of ring L-k."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wheels as wh
bad = 0; n_checks = 0
for L in range(2, 41):
    for k in range(1, L + 1):
        n = L + k; w = L - k
        pred = (1 << L) - ((1 << w) - (1 << ((w + 1) // 2)))
        got = wh.hold(1 << L, n)
        n_checks += 1
        if got != pred:
            bad += 1; print('miss', L, k, got, pred)
print('mirror cascade checks', n_checks, 'misses', bad)
