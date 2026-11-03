"""Independent check of the tilted-section reader example: r=1, a=4/5, beta=pi/3, gamma=0, rho=3/5.
Points alpha=0 and alpha=pi share global longitude 0 (4-bit prefix 0000); after alpha -> alpha+pi/2 they
read different prefixes, so the quarter-turn has no induced action on 4-bit longitude-prefix classes."""
import math
a, beta, rho = 0.8, math.pi / 3, 0.6
def lon(alpha):
    x = a * math.sin(beta) + rho * math.cos(beta) * math.cos(alpha); y = rho * math.sin(alpha)
    return (math.atan2(y, x) / (2 * math.pi)) % 1.0
pre = lambda u: format(int(u * 16), "04b")
for al in (0.0, math.pi):
    print(f"alpha={al:.4f}: longitude u={lon(al):.6f} prefix {pre(lon(al))}  ->  after quarter-turn u={lon(al+math.pi/2):.6f} prefix {pre(lon(al+math.pi/2))}")
print("same class before, different classes after:", pre(lon(0)) == pre(lon(math.pi)) and pre(lon(math.pi/2)) != pre(lon(3*math.pi/2)))
