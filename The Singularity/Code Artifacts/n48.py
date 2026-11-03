"""The directional test at n=48.

(16,48) = octal seed subdivided by q=6.  6 | 48, so this is OCTAL-descended with a
          6-compatible period.  Rule predicts twisted classes close: Delta > 0.
(64,48) = hex seed subdivided by q=8.  8 | 48, so this is HEX-descended with an
          8-compatible period.  Rule predicts principal class only: Delta = 0.

These are the first frames where BOTH directions of the cross-divisibility exist,
so they test the asymmetry itself rather than a local feature.
"""
from class_probe import class_probe
from valcor import valuation_corank

for name, b, n, q, pred in [
    ("octal q=6 -> (16,48)  [C8 into C6 territory]", 16, 48, 6, "Delta > 0"),
    ("hex   q=8 -> (64,48)  [C6 into C8 territory]", 64, 48, 8, "Delta = 0"),
]:
    res = class_probe(b, n, q, dps=320, maxcoeff=10**12)
    carry = sorted(c for c, (v_, ok, _) in res.items() if ok)
    cor, _, _ = valuation_corank(b, n)
    print(f"{name}", flush=True)
    print(f"   predicted: {pred}", flush=True)
    print(f"   classes carrying relations (mod {q}): {carry}", flush=True)
    print(f"   corank={cor}   class-count={len(carry)}   "
          f"implied Delta={len(carry)-cor}", flush=True)
    for c in sorted(res):
        v_, ok, _ = res[c]
        if ok:
            print(f"      class {c}: maxc={max(abs(x) for x in v_):>6}  {v_}", flush=True)
    print(flush=True)
