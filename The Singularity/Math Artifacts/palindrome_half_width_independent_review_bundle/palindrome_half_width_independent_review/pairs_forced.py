"""Compatibility adapter used only to rerun the archived audit.

The uploaded bundle references an external pairs_forced.py that it does not
contain. This adapter reconstructs the stated partner/grow ordering from the
partner definition and the canonical-first/reversed-partner-second ring rule.
It is not asserted to be the missing upstream source file.
"""
def partner(word):
    r = word[::-1]
    if r != word:
        return r
    return ''.join('1' if b == '0' else '0' for b in word)

def grow(n):
    if n < 1:
        raise ValueError('width must be >= 1')
    words = [format(i, f'0{n}b') for i in range(1 << n)]
    first = [w for w in words if w < partner(w)]
    out = first + [partner(w) for w in reversed(first)]
    if n > 1:
        mid = len(out) // 2
        out[mid - 1], out[mid] = out[mid], out[mid - 1]
    return out
