"""Figures for "Against Its Own Reverse". Static, print-first. Palette validated (blue/orange/aqua, light surface)."""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc
from mpl_toolkits.mplot3d import Axes3D  # noqa
import os
os.makedirs('figs', exist_ok=True)
exec(open('paper_checks.py').read().split('# ---------------------------------------------------------------- 1. ring and pairing')[0])

BLUE, ORANGE, AQUA = '#2a78d6', '#eb6834', '#1baf7a'
INK, INK2, MUTED, GRID, AXIS = '#0b0b0b', '#52514e', '#898781', '#e1e0d9', '#c3c2b7'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 8, 'axes.edgecolor': AXIS, 'axes.labelcolor': INK2,
                     'xtick.color': MUTED, 'ytick.color': MUTED, 'axes.linewidth': 0.6, 'grid.color': GRID,
                     'grid.linewidth': 0.5, 'axes.grid': True, 'axes.axisbelow': True, 'legend.frameon': False,
                     'savefig.dpi': 220, 'savefig.bbox': 'tight', 'figure.facecolor': 'white', 'axes.facecolor': 'white',
                     'axes.titlesize': 8.5, 'axes.titlecolor': INK, 'axes.titleweight': 'regular'})
def clean(ax):
    for s in ('top', 'right'): ax.spines[s].set_visible(False)

# ---------------- Figure 1: the mirror lift of one word
x = '100110110101'; n = 12; h = 6
fig, ax = plt.subplots(figsize=(6.6, 3.15)); ax.set_axis_off(); ax.grid(False)
ax.set_xlim(-0.6, 12.6); ax.set_ylim(-4.6, 2.9)
for j, b in enumerate(x):
    ax.add_patch(Rectangle((j + 0.08, 1.1), 0.84, 0.84, facecolor=BLUE if b == '1' else 'white', edgecolor=BLUE if b == '1' else AXIS, lw=0.8))
    ax.text(j + 0.5, 2.15, str(j), ha='center', va='bottom', color=MUTED, fontsize=6.5)
ax.text(-0.5, 1.52, 'x', ha='right', va='center', color=INK, fontsize=9, style='italic')
for j in range(h):
    a, c = j + 0.5, n - 1 - j + 0.5; wd = c - a
    unequal = x[j] != x[n-1-j]
    ax.add_patch(Arc(((a + c)/2, 1.05), wd, 0.55 + 0.12*(h - j), theta1=180, theta2=360,
                     color=ORANGE if unequal else AXIS, lw=1.1 if unequal else 0.8))
# lifted table
cols = [1.4 + 1.65*j for j in range(h)]
rows = [(-0.55, 'pair j'), (-1.25, 'value  v_j'), (-1.95, 'difference  d_j'), (-2.65, 'latitude part'), (-3.35, 'comparator')]
for y, lab in rows: ax.text(-0.5, y, lab, ha='left', va='center', color=INK2, fontsize=7)
first = next(j for j in range(h) if x[j] != x[n-1-j])
for j in range(h):
    v = int(x[j]); d = int(x[j] != x[n-1-j]); X = cols[j] + 1.2
    ax.text(X, -0.55, str(j), ha='center', va='center', color=MUTED, fontsize=7)
    ax.text(X, -1.25, str(v), ha='center', va='center', color=INK, fontsize=8)
    ax.text(X, -1.95, str(d), ha='center', va='center', color=ORANGE if d else INK, fontsize=8, weight='bold' if d else 'normal')
    ax.text(X, -2.65, ('+1' if v else '−1') if not d else '0', ha='center', va='center', color=INK if not d else MUTED, fontsize=8)
    if j == first:
        ax.text(X, -3.35, 'decides: c = +1', ha='center', va='center', color=ORANGE, fontsize=7)
    elif d:
        ax.text(X, -3.35, 'not read', ha='center', va='center', color=MUTED, fontsize=6.5)
ax.text(-0.5, -4.15, 'Route residual bits, innermost pair first:  1 0 1 1 0 0      z = +1 − 1 + 1 = +1 = wt(x) − n/2', ha='left', va='center', color=INK2, fontsize=7)
fig.savefig('figs/fig1_lift.png'); plt.close(fig)

# ---------------- Figure 2: the sphere and the latitude waveform
fig = plt.figure(figsize=(6.6, 3.1))
ax3 = fig.add_axes([0.0, 0.02, 0.42, 0.92], projection='3d')
n = 10; N = 1 << n; R = ring(n); J = revarr(R, n); pal = J == R
z2 = 2*popc(R, n) - n; i = np.arange(N); th = 2*np.pi*((i + 0.5)/N - 0.5); rho = np.sqrt(np.maximum(n*n - z2.astype(float)**2, 0))
X, Y, Z = rho*np.cos(th), rho*np.sin(th), z2.astype(float)
ax3.scatter(X[~pal], Y[~pal], Z[~pal], s=1.2, c=BLUE, alpha=0.55, depthshade=False, linewidths=0)
ax3.scatter(X[pal], Y[pal], Z[pal], s=9, c=ORANGE, depthshade=False, edgecolors='white', linewidths=0.4)
tt = np.linspace(0, 2*np.pi, 200); ax3.plot(n*np.cos(tt), n*np.sin(tt), 0*tt, color=AXIS, lw=0.5)
ax3.set_box_aspect((1, 1, 1), zoom=1.45);
for zz in (-8, -4, 0, 4, 8):
    rr = np.sqrt(n*n - zz*zz); ax3.plot(rr*np.cos(tt), rr*np.sin(tt), 0*tt + zz, color=GRID, lw=0.4)
ax3.set_xticks([]); ax3.set_yticks([]); ax3.set_zticks([])
ax3.xaxis.pane.set_visible(False); ax3.yaxis.pane.set_visible(False); ax3.zaxis.pane.set_visible(False)
ax3.grid(False); ax3.view_init(elev=18, azim=-60); ax3.set_title('All 1,024 words of width 10 on the sphere', pad=0)
for axis in (ax3.xaxis, ax3.yaxis, ax3.zaxis): axis.line.set_color((1, 1, 1, 0))
ax = fig.add_axes([0.52, 0.30, 0.46, 0.60]); clean(ax)
n = 12; N = 1 << n; R = ring(n); J = revarr(R, n); pal = J == R; z = (2*popc(R, n) - n)/2; i = np.arange(N); t = (i + 0.5)/N - 0.5
ax.plot(t[~pal], z[~pal], color=BLUE, lw=0.35, label='body (Walsh-even part)')
ax.scatter(t[pal], z[pal], s=7, color=ORANGE, zorder=3, edgecolors='white', linewidths=0.4, label='carrier: palindromes (odd part)')
ax.set_xlabel('azimuth θ / 2π   (seam at 0, closure at ±½)'); ax.set_ylabel('latitude z = wt − n/2')
ax.set_xlim(-0.5, 0.5); ax.set_ylim(-6.6, 6.6); ax.set_title('Latitude around the ring, n = 12')
ax.legend(loc='upper center', fontsize=6.8, ncol=2, bbox_to_anchor=(0.45, -0.24), handlelength=1.2, columnspacing=1.0)
fig.savefig('figs/fig2_sphere_waveform.png'); plt.close(fig)

# ---------------- Figure 3: Delta is the count across the cut
n = 12; N = 1 << n; h = 6; H = 64
w = np.arange(N, dtype=np.int64); c = np.sign(revarr(w, n) - w); D = np.concatenate([[0], np.cumsum(c)[:-1]])
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.6, 2.5), gridspec_kw={'width_ratios': [1.6, 1]})
for a in (a1, a2): clean(a)
pp = np.linspace(0, N, 600); A = pp/H
a1.plot(pp, A*(H - A), color=ORANGE, lw=0.9, zorder=2, label='coarse term A(H − A), A = p / 2^h')
a1.plot(w, D, color=BLUE, lw=0.35, zorder=3, label='Δ(p): reversal pairs the cut separates')
a1.set_xlabel('cut p (word value), n = 12'); a1.set_ylabel('pairs crossing the cut'); a1.set_xlim(0, N)
a1.legend(loc='lower center', fontsize=6.8); a1.set_title('Δ over the whole domain')
A0 = 21; lo, hi = A0*H, (A0 + 1)*H; xs = np.arange(lo, hi)
a2.vlines(xs, 0, c[lo:hi], color=AQUA, lw=0.9)
a2.plot(np.arange(lo, hi + 1), D[lo:hi + 1] - D[lo], color=BLUE, lw=1.0, drawstyle='steps-post')
a2.text(lo + 3, (D[hi] - D[lo]) - 2.0, 'Δ(p) − Δ(21·64)', color=BLUE, fontsize=6.8, ha='left')
a2.text(lo + 40, -1.9, 'c(x) = ±1', color=AQUA, fontsize=6.8)
a2.set_xlabel('p inside one row (left half A = 21)'); a2.set_xlim(lo, hi); a2.set_title('One row: steps of c(x)')
fig.tight_layout(); fig.savefig('figs/fig3_cut.png'); plt.close(fig)

# ---------------- Figure 4: two readers, two coordinate systems
n = 12; N = 1 << n; w = np.arange(N, dtype=np.int64); R = ring(n)
cw = np.sign(revarr(w, n) - w); zw = 2*popc(w, n) - n; cr = np.sign(revarr(R, n) - R); zr = 2*popc(R, n) - n
panels = [(cw, 'comparator, word coordinates', BLUE), (cr, 'comparator, ring coordinates', BLUE),
          (zw, 'latitude, word coordinates', ORANGE), (zr, 'latitude, ring coordinates', ORANGE)]
fig, axs = plt.subplots(2, 2, figsize=(6.6, 4.3), sharey=True)
for a, (sig, title, col) in zip(axs.flat, panels):
    clean(a); f = fwht(sig).astype(float); E = f*f; E = E/E.sum(); nzm = E > 0
    a.vlines(np.nonzero(nzm)[0], 1e-9, E[nzm], color=col, lw=0.5)
    a.set_yscale('log'); a.set_ylim(1e-9, 1.5); a.set_xlim(0, N)
    top = E.max(); a.set_title(f'{title}\n{int(nzm.sum()):,} modes, largest carries {top:.1%}')
    a.set_xticks([0, 1024, 2048, 3072, 4096])
for a in axs[1]: a.set_xlabel('Walsh mode s (n = 12)')
for a in axs[:, 0]: a.set_ylabel('share of energy')
fig.tight_layout(); fig.savefig('figs/fig4_two_readers.png'); plt.close(fig)

# ---------------- Figure 5: the seam staircase
n = 16; h = 8; H = 256; qs = []; Ds = []; Ks = []; means = []; env = []; ret = []
for K in range(1, H // 2):
    order = sorted(range(K), key=lambda r: Jint(r, h)); q0 = K*(K-1)//2
    vals = [bin(K).count('1') + bin(r).count('1') for r in order]
    for i, v in enumerate(vals): qs.append(q0 + i + 1); Ds.append(v)
    means.append((q0 + 1 + (K - 1)/2, np.mean(vals))); env.append((q0 + 1, q0 + K, 2*K.bit_length() - 1))
    if K & (K - 1) == 0: ret.append((q0 + 1, vals[0]))
fig, ax = plt.subplots(figsize=(6.6, 2.7)); clean(ax)
ax.scatter(qs, Ds, s=1.0, color=MUTED, alpha=0.5, linewidths=0, label='deficit at each depth: wt(K) + wt(r)')
mx, my = zip(*means); ax.plot(mx, my, color=BLUE, lw=1.0, label='block mean')
ex = []; ey = []
for a, b, e in env: ex += [a, b]; ey += [e, e]
ax.plot(ex, ey, color=ORANGE, lw=1.0, label='envelope 2·bitlength(K) − 1')
rx, ry = zip(*ret); ax.scatter(rx, ry, s=14, color=AQUA, zorder=4, edgecolors='white', linewidths=0.5)
ax.text(rx[-1]*1.08, ry[-1] + 0.1, 'K = 2^t: deficit returns to 1', color=INK2, fontsize=6.8, va='bottom')
ax.set_xscale('log'); ax.set_xlabel('1 + depth q from the seam   (n = 16, blocks K < 128, log scale)'); ax.set_ylabel('zeros below the north pole')
ax.set_title('The seam is a digital staircase under a logarithmic envelope'); ax.legend(loc='upper left', fontsize=6.8)
fig.tight_layout(); fig.savefig('figs/fig5_seam.png'); plt.close(fig)
print('figures written:', sorted(os.listdir('figs')))
