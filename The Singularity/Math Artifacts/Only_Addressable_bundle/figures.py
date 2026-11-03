"""Figures for 'Only Addressable'. Palette validated (dataviz validator, light, white surface, all-pairs):
blue #2a78d6, orange #eb6834 (aqua unused). Ink #0b0b0b / secondary #52514e / muted #898781,
grid #e1e0d9, baseline #c3c2b7."""
import sys, json, math
from fractions import Fraction as F
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
sys.path.insert(0, "/home/claude/space/paper3"); sys.path.insert(0, "/home/claude/space/rings")
from ringlib import ring
from witness_Kd import word_at

BLUE, ORANGE = "#2a78d6", "#eb6834"
INK, SEC, MUTED, GRID, BASE, OFF = "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7", "#e4e3dd"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": BASE,
                     "axes.labelcolor": SEC, "xtick.color": MUTED, "ytick.color": MUTED,
                     "axes.titlecolor": INK, "text.color": INK, "axes.linewidth": 0.8,
                     "savefig.dpi": 300, "savefig.bbox": "tight", "savefig.facecolor": "white"})
OUT = "/home/claude/space/paper3/figs/"
import os; os.makedirs(OUT, exist_ok=True)
half = F(1, 2)

def tidy(ax, grid_y=True):
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    if grid_y: ax.grid(axis="y", color=GRID, linewidth=0.6); ax.set_axisbelow(True)

# ---------------- Fig 1: rings 1..8, seam ray and the D=8 witness ray -----------------
cert = json.load(open("/home/claude/space/rings/Kd_certificate.json"))
w8 = next(c for c in cert["per_D_witness_8_40"] if c["D"] == 8)
u8 = F(w8["u"]); read8 = w8["reads"]
fig = plt.figure(figsize=(6.3, 6.3))
ax = fig.add_subplot(projection="polar")
ax.set_theta_zero_location("N"); ax.set_theta_direction(-1)
gap = 0.12
for L in range(1, 9):
    bits = "".join(ring(L)); S = len(bits)
    th = (np.arange(S) + 0.5) * 2 * np.pi / S
    col = [BLUE if b == "1" else OFF for b in bits]
    ax.bar(th, 1 - 2 * gap, width=2 * np.pi / S, bottom=L - 1 + gap, color=col, linewidth=0, align="center")
for u, lab, ls in ((half, "seam, u = 1/2", "-"), (u8, f"witness ray, u = {u8.numerator}/{u8.denominator}", "-")):
    t = 2 * np.pi * float(u)
    ax.plot([t, t], [0, 8.35], color=INK, linewidth=1.1, linestyle=ls)
t8 = 2 * np.pi * float(u8)
ax.annotate("seam\nu = 1/2", xy=(np.pi, 8.35), xytext=(np.pi - 0.16, 9.25), ha="center", va="center", fontsize=8.5, color=INK)
ax.annotate(f"u = {u8.numerator}/{u8.denominator}\nreads {' '.join(read8)}\n(rings 1 → 8)", xy=(t8, 8.35),
            xytext=(t8 + 0.20, 9.55), ha="center", va="center", fontsize=8.5, color=INK)
ax.set_ylim(0, 8.4); ax.set_axis_off()
fig.savefig(OUT + "fig1_rings.png"); plt.close(fig)

# ---------------- Fig 2: the triangular top, words past the seam, L = 40 -----------------
L = 40; h = L // 2; M = 1 << (L - 1)
xs = np.linspace(0, 17, 240)
js = sorted(set(max(1, int(round(2 ** x))) for x in xs))
img = np.array([[0 if c == "0" else 1 for c in word_at(M + j, L)] for j in js])
fig, ax = plt.subplots(figsize=(6.3, 4.1))
y = np.log2(js)
# draw rows as horizontal segments so the log-spaced rows keep their true positions
for row, yy in zip(img, y):
    zx = np.where(row == 0)[0]
    ax.scatter(zx, np.full(len(zx), yy), marker="s", s=7.5, color=INK, linewidths=0)
def core(j):
    K = 1
    while K * (K + 1) // 2 <= j: K += 1
    n = int(math.floor(math.log2(K))); t = h - 1 - n
    return t, L - 1 - t
cj = np.unique(np.round(2 ** np.linspace(0, 17, 400)).astype(int))
cl = [core(j) for j in cj]
ax.plot([c[0] - 0.5 for c in cl], np.log2(cj), color=ORANGE, linewidth=1.6, drawstyle="steps-post")
ax.plot([c[1] + 0.5 for c in cl], np.log2(cj), color=ORANGE, linewidth=1.6, drawstyle="steps-post")
for frac, lab in ((1 / 3, "L/3"), (2 / 3, "2L/3")):
    ax.axvline(L * frac, color=MUTED, linestyle=(0, (3, 3)), linewidth=1)
    ax.text(L * frac, 17.55, lab, ha="center", va="bottom", fontsize=8.5, color=SEC)
ax.text(0.3, 6.5, "orange: the core\npredicted by the\nblock law,\n[t, L−1−t] with\nt = h−1−⌊log₂K⌋,\nK ≈ √(2j)", fontsize=8, color=SEC, va="center", linespacing=1.35)
ax.set_xlim(-0.5, L - 0.5); ax.set_ylim(-0.3, 17.4)
ax.set_xlabel("bit index in the word, L = 40 (zeros shown as dark squares; all other bits are 1)")
ax.set_ylabel("log₂ j   (word sits j places past the seam)")
tidy(ax, grid_y=False)
fig.savefig(OUT + "fig2_triangular_top.png"); plt.close(fig)

# ---------------- Fig 3: the reader's path for the D = 40 witness ---------------------
def law(D):
    p = 2 * ((D + 1) // 3) + 1
    f = F(2, 3) + (F(1, 6 * D) if D % 3 == 2 else 0)
    return half + F(1, 1 << p) + f * F(1, 1 << (D - 1)), p
D = 40; u, p = law(D)
fig, ax = plt.subplots(figsize=(6.3, 3.9))
for Lr in range(1, D + 1):
    y2 = u * (1 << Lr); i = math.floor(y2); k = math.floor(Lr * (y2 - i))
    w = word_at(i, Lr); z = [q for q, c in enumerate(w) if c == "0"]
    ax.scatter([Lr] * len(z), [(q + 0.5) / Lr for q in z], marker="_", s=38, color=MUTED, linewidths=1.2, zorder=2)
    b = w[k]
    ax.scatter([Lr], [(k + 0.5) / Lr], s=34, color=BLUE if b == "1" else ORANGE, zorder=3,
               edgecolors="white", linewidths=0.8)
for frac, lab in ((1 / 3, "1/3"), (2 / 3, "2/3")):
    ax.axhline(frac, color=MUTED, linestyle=(0, (3, 3)), linewidth=0.9, zorder=1)
    ax.text(0.2, frac + 0.012, lab, fontsize=8, color=SEC, va="bottom")
ax.axvline(p, color=BASE, linewidth=1, zorder=1)
ax.text(p - 0.4, 0.97, f"address bit enters at p = {p}", fontsize=8, color=SEC, va="top", ha="right")
ax.annotate("ring D−1 lands on\nits outer zero (2/3)", xy=(D - 1, (2 * (D - 1) // 3 + 0.5) / (D - 1)), xytext=(D - 12.5, 0.86),
            fontsize=8, color=INK, arrowprops=dict(arrowstyle="-", color=SEC, linewidth=0.8))
ax.annotate("ring D lands on\nits inner zero (1/3)", xy=(D, (D // 3 + 0.5) / D), xytext=(D - 12.5, 0.12),
            fontsize=8, color=INK, arrowprops=dict(arrowstyle="-", color=SEC, linewidth=0.8))
h1 = ax.scatter([], [], s=34, color=BLUE, label="bit read = 1"); h0 = ax.scatter([], [], s=34, color=ORANGE, label="bit read = 0")
hz = ax.scatter([], [], marker="_", s=38, color=MUTED, linewidths=1.2, label="zeros of the word under the ray")
ax.legend(handles=[h1, h0, hz], loc="upper left", bbox_to_anchor=(0.0, -0.17), ncol=3, frameon=False, fontsize=8)
ax.set_xlim(0, D + 1); ax.set_ylim(0, 1)
ax.set_xlabel("ring L"); ax.set_ylabel("position in the word (fraction of L)")
tidy(ax)
fig.savefig(OUT + "fig3_reader_path.png"); plt.close(fig)

# ---------------- Fig 4: how the witness scales -----------------------------------------
uc = json.load(open("/home/claude/space/paper3/unified_certificate.json"))["unified"]
Ds = [c["D"] for c in uc]
lK = [math.log2(float(F(c["K_D"][1]) - F(c["K_D"][0]))) for c in uc]
ld = [math.log2(float(law(Dd)[0] - half)) for Dd in Ds]
lx = [-(Dd - 2) for Dd in Ds]
fig, ax = plt.subplots(figsize=(6.3, 3.6))
ax.plot(Ds, ld, color=BLUE, linewidth=2)
ax.plot(Ds, lx, color=MUTED, linewidth=1.4, linestyle=(0, (4, 3)))
ax.plot(Ds, lK, color=ORANGE, linewidth=2)
ax.text(Ds[-1] + 1.5, ld[-1], "witness offset\n$\\delta_D = u_D - 1/2$, slope $-2/3$", fontsize=8, color=INK, va="center")
ax.text(Ds[-1] + 1.5, lx[-1] + 4, "excluded zone edge\n$2^{-(D-2)}$, slope $-1$", fontsize=8, color=INK, va="center")
ax.text(Ds[-1] + 1.5, lK[-1] - 4, "width of $K_D$\n(about one ring-$D$ slice)", fontsize=8, color=INK, va="center")
ax.set_xlim(12, 120); ax.set_xlabel("depth D"); ax.set_ylabel("log₂ (fraction of the circle)")
tidy(ax)
fig.savefig(OUT + "fig4_scaling.png"); plt.close(fig)

# ---------------- Fig 5: the language, small multiples -----------------------------------
R = {1: 2, 2: 4, 3: 8, 4: 16, 5: 31, 6: 62, 7: 123, 8: 239, 9: 469, 10: 924, 11: 1827, 12: 3606, 13: 7122, 14: 14087, 15: 27819, 16: 55122}
dfa = {8: 29, 9: 49, 10: 76, 11: 111, 12: 186, 13: 322, 14: 519, 15: 914, 16: 1451}
c11 = {11: 1, 12: 3, 13: 14, 14: 51, 15: 175, 16: 311}
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.3, 2.9))
dd = sorted(R); a1.plot(dd, [R[d] / 2 ** d for d in dd], color=BLUE, linewidth=2, marker="o", markersize=4)
a1.set_xlabel("depth $d$"); a1.set_ylabel("reachable fraction $R_d/2^d$"); a1.set_ylim(0.8, 1.01); tidy(a1)
a1.set_xticks([1, 4, 8, 12, 16])
a1.text(16, R[16] / 2 ** 16 - 0.012, f"{R[16]/2**16:.3f}", ha="center", va="top", fontsize=8, color=INK)
hh = sorted(dfa); a2.plot(hh, [dfa[x] for x in hh], color=BLUE, linewidth=2, marker="o", markersize=4)
cc = sorted(c11); a2.plot(cc, [c11[x] for x in cc], color=ORANGE, linewidth=2, marker="o", markersize=4)
a2.set_yscale("log"); a2.set_xlabel("horizon H"); a2.set_ylabel("count (log scale)")
a2.text(16.3, dfa[16], "minimal DFA\nstates, horizon $H$", fontsize=8, color=INK, va="center")
a2.text(16.3, c11[16], "classes among\ndepth-11 prefixes", fontsize=8, color=INK, va="center")
a2.set_xlim(7.5, 19.8); a2.set_xticks([8, 10, 12, 14, 16]); a2.set_xlabel("horizon $H$"); tidy(a2)
fig.tight_layout(w_pad=2.5)
fig.savefig(OUT + "fig5_language.png"); plt.close(fig)
print("figures written:", sorted(os.listdir(OUT)))
