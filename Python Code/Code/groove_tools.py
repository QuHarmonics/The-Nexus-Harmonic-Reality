
import math

PI = math.pi
H = PI / 9.0  # ~0.3490658503988659

def _dist_to_family(x: float, anchor: float, period: float = 1.0):
    k = round((x - anchor) / period)
    target = k * period + anchor
    return abs(x - target), int(k), target

def in_wh_plus_H(x: float, tol: float = 0.02):
    """Is x within tol of some k + H ?  Returns (hit, distance, k, nearest_value)."""
    d, k, target = _dist_to_family(x, anchor=H, period=1.0)
    return d < tol, d, k, target

def mantissa10(x: float) -> float:
    """Fractional part of log10(|x|) in [0,1)."""
    if x <= 0:
        return float('nan')
    lx = math.log10(x)
    return lx - math.floor(lx)

def _circ_dist01(y: float) -> float:
    y = y - math.floor(y)
    return min(y, 1.0 - y)

ANCHOR_M = mantissa10(0.35)

def in_point35_family(x: float, eps: float = 0.02):
    """Decade-invariant '.35' family (0.35, 3.5, 35, 0.0035, ...). Returns (hit, circular_distance)."""
    if x <= 0:
        return False, float('nan')
    m = mantissa10(x)
    d = _circ_dist01(m - ANCHOR_M)
    return d < eps, d
