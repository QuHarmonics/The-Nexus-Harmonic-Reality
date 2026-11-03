"""Generated ring runtime; Boolean arithmetic is XOR and AND."""

def _check_state(x, width):
    if type(x) is not int:
        raise TypeError("state must be a Python integer")
    if not 0 <= x < (1 << width):
        raise ValueError("state outside runtime width")

def R3_forward(x):
    _check_state(x, 3)
    a = (x >> 2) & 1
    b = (x >> 1) & 1
    c = (x >> 0) & 1
    g0 = a & b
    y0 = b ^ a
    y1 = c ^ b ^ a ^ g0
    y2 = 1 ^ c ^ b ^ g0
    return (y0 << 2) | (y1 << 1) | (y2 << 0)

def R3_inverse(x):
    _check_state(x, 3)
    a = (x >> 2) & 1
    b = (x >> 1) & 1
    c = (x >> 0) & 1
    g0 = a & c
    g1 = a & b
    y0 = 1 ^ c ^ b
    y1 = 1 ^ c ^ b ^ a
    y2 = 1 ^ c ^ g0 ^ g1
    return (y0 << 2) | (y1 << 1) | (y2 << 0)

