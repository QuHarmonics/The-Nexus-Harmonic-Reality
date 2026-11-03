#!/usr/bin/env python3
"""
Persistent pending-field reader for the hex digits of pi.

STATE
  n      output position: digits emitted so far
  K      resolution frontier: lanes opened for k = 0..K   (moves only by OPEN)
  P      precision frontier: hex places held below the read point (moves only by WIDEN)
  lanes  one per opened (k, j), j in {1,4,5,6}:
           D      = (8k + j) * 16^s, with s = k - n at the moment of opening
           c      = weight 4, -2, -1, -1
           r_top  = top cursor: the lane's unread contribution is c * r_top / D
           r_bot  = bottom cursor: the remainder P places below the top
  S      field accumulator = sum of c * floor(16^P * r_top / D)
         Its integer part (above 16^P) is the carry register. It is never removed.

OPERATIONS -- the only three the machine has
  OPEN   K <- K+1. Four lanes enter at their own scale 16^(K-n), r_top = 1.
         The output position n does not move.
  WIDEN  P <- P+1. Every lane takes one long-division step at its bottom cursor.
         The output position n does not move.
  EMIT   only when CERTIFY succeeds. Every lane takes one step at both cursors:
             (q, r_top) = divmod(16 r_top, D)      top crossing leaves
             (g, r_bot) = divmod(16 r_bot, D)      one new place enters below
         S <- 16 S - 16^P * sum(c q) + sum(c g)    and n <- n+1

CERTIFY
  The unopened lanes (k > K) are never evaluated. They enter only through the bound
      |unopened| <= 16^(n-K-1) * (16/15) * 8 / (8K+9)
  Field truncation is below one place per lane: S - 4(K+1) < 16^P * field < S + 4(K+1).
  The digit is certified when both ends of the interval give the same floor(16 x) mod 16,
  and only once the lane at the read point is open (K >= n), so lanes never enter behind it.
"""
from fractions import Fraction

WEIGHTS = {1: 4, 4: -2, 5: -1, 6: -1}
POS = sum(c for c in WEIGHTS.values() if c > 0)       # 4
NEG = -sum(c for c in WEIGHTS.values() if c < 0)      # 4
ABS = POS + NEG                                        # 8


class PendingField:
    def __init__(self, P=4):
        self.n, self.K, self.P = 0, -1, P              # empty field
        self.D, self.c, self.rt, self.rb = [], [], [], []
        self.S = 0
        self.opened_ahead = 0

    # ---- OPEN: resolve one more layer of the unread value at the current address
    def open_layer(self):
        k = self.K + 1
        s = k - self.n
        assert s >= 0, "a lane may not open behind the read point"
        for j, c in WEIGHTS.items():
            D = (8 * k + j) * 16 ** s
            r = 1 % D
            w, rb = divmod(r << (4 * self.P), D)
            self.D.append(D); self.c.append(c); self.rt.append(r); self.rb.append(rb)
            self.S += c * w
        if s > 0:
            self.opened_ahead += 4
        self.K = k

    # ---- WIDEN: hold one more place below the read point, for every lane
    def widen(self):
        add = 0
        for i in range(len(self.D)):
            g, self.rb[i] = divmod(16 * self.rb[i], self.D[i])
            add += self.c[i] * g
        self.S = 16 * self.S + add
        self.P += 1

    # ---- the unopened part enters only as a bound, in units of 16^-P
    def tail_ulps(self):
        b = Fraction(16, 15) * Fraction(ABS, 8 * self.K + 9) * Fraction(16) ** (self.P + self.n - self.K - 1)
        return -(-b.numerator // b.denominator)

    def interval(self):
        T = self.tail_ulps()
        L = self.K + 1
        return self.S - NEG * L - T, self.S + POS * L + T, T

    def certify(self):
        if self.K < self.n:                 # the lane at the read point must be open
            return None
        lo, hi, T = self.interval()
        a = (16 * lo) >> (4 * self.P)
        b = (16 * hi) >> (4 * self.P)
        return (a % 16) if a == b else None

    def carry_register(self):
        lo, hi, _ = self.interval()
        a, b = lo >> (4 * self.P), hi >> (4 * self.P)
        return a if a == b else None

    # ---- EMIT: the certified digit leaves; both cursors of every lane step once
    def emit(self):
        C = G = 0
        for i in range(len(self.D)):
            q, self.rt[i] = divmod(16 * self.rt[i], self.D[i])
            g, self.rb[i] = divmod(16 * self.rb[i], self.D[i])
            C += self.c[i] * q
            G += self.c[i] * g
        self.S = 16 * self.S - (C << (4 * self.P)) + G
        self.n += 1
        return C, G

    def storage_bits(self):
        return (sum(d.bit_length() + r.bit_length() + b.bit_length() + 3
                    for d, r, b in zip(self.D, self.rt, self.rb))
                + abs(self.S).bit_length() + 1)

    def lanes(self):
        return len(self.D)
