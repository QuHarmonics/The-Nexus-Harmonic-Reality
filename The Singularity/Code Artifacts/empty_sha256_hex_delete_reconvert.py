#!/usr/bin/env python3
HEX = "1a14bbc855b4cbea992eaf922d5669309678aede7b2cf38e685211349175cd1d"

def trace(mode):
    s = HEX
    rows = [(0, "", s, int(s, 16))]
    step = 0
    while len(s) > 1:
        n = len(s)
        if mode == "end":
            idx = n - 1
        elif mode == "start":
            idx = 0
        elif mode == "center":
            idx = (n - 1) // 2  # left-of-center when even
        else:
            raise ValueError(mode)

        removed = s[idx]
        s = s[:idx] + s[idx + 1:]
        step += 1
        rows.append((step, removed, s, int(s, 16)))
    return rows

if __name__ == "__main__":
    for mode in ("end", "start", "center"):
        print(f"\n=== {mode} ===")
        for row in trace(mode):
            print(*row, sep="\t")
