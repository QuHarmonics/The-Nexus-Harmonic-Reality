"""Figures for the structural map paper. Dean A. Kulik, QuHarmonics Research Group."""
import sys, os, json
sys.path.insert(0, '/home/claude/wheels'); sys.path.insert(0, '/home/claude/atlas')
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from fractions import Fraction
from math import floor
import wheels as wh

BLUE, ORANGE, AQUA, GREY = '#2a78d6', '#eb6834', '#1baf7a', '#9a9890'
INK, INK2, MUTED, GRID, AXIS = '#0b0b0b', '#52514e', '#898781', '#e1e0d9', '#c3c2b7'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 8, 'axes.edgecolor': AXIS, 'axes.labelcolor': INK2,
                     'xtick.color': MUTED, 'ytick.color': MUTED, 'axes.linewidth': 0.6, 'grid.color': GRID,
                     'grid.linewidth': 0.5, 'axes.grid': True, 'axes.axisbelow': True, 'legend.frameon': False,
                     'savefig.dpi': 220, 'savefig.bbox': 'tight', 'figure.facecolor': 'white', 'axes.facecolor': 'white',
                     'axes.titlesize': 8.5, 'axes.titlecolor': INK, 'axes.titleweight': 'regular'})
def clean(ax):
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)

# ---------------- Figure 1: frame losses
fr = json.load(open('/home/claude/atlas/frame_results.json'))['by_L']
fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.5), sharey=True)
for ax, par, title in ((axes[0], 0, 'even widths'), (axes[1], 1, 'odd widths')):
    Ls = [L for L in range(10, 23) if L % 2 == par]
    cmap = plt.get_cmap('Blues')
    for idx, L in enumerate(Ls):
        P = 2 ** ((L + 1) // 2)
        loss = np.array(fr[str(L)]['loss']) / P
        law = np.array(fr[str(L)]['law']) / P
        s = np.arange(L)
        col = cmap(0.35 + 0.6 * idx / max(1, len(Ls) - 1))
        ax.plot(s, law, color=col, lw=0.9)
        ax.plot(s, loss, 'o', ms=2.4, color=col, mec='none', label=f'L = {L}' if idx in (0, len(Ls) - 1) else None)
    ax.set_title(f'Missing words / palindromes, {title}')
    ax.set_xlabel('frame offset s (bits)')
    ax.set_ylim(-0.05, 1.05)
    ax.axhline(1, color=AXIS, lw=0.6, ls=':')
    clean(ax)
    ax.legend(loc='lower center', fontsize=7)
axes[0].set_ylabel('loss / 2^⌈L/2⌉')
fig.tight_layout()
fig.savefig('figs/fig1_frames.png')
plt.close(fig)

# ---------------- Figure 2: readers
rr = json.load(open('/home/claude/atlas/reader_results.json'))['by_n']
re = json.load(open('/home/claude/atlas/reader_extend_results.json'))['by_n']
ns = list(range(4, 17))
def series(name, mode='per_bit'):
    return [rr[str(n)][name][mode]['min_mean_float'] for n in ns]
fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.6), gridspec_kw={'width_ratios': [1.25, 1]})
ax = axes[0]
ax.plot(ns, series('face'), '-o', ms=2.5, lw=1, color=BLUE, label='face')
ax.plot(ns, [rr[str(n)]['c']['whole']['min_mean_float'] for n in ns], '-s', ms=2.3, lw=1, color=AQUA, label='comparator, palindrome flag')
ax.plot(ns, series('partner'), '-^', ms=2.5, lw=1, color=GREY, label='partner bits')
ax.plot(ns, series('successor'), '-v', ms=2.5, lw=1, color=ORANGE, label='successor bits')
ax.plot(ns, series('address'), '-D', ms=2.2, lw=1, color=INK, label='address bits')
ax.plot(ns, [rr[str(n)]['address']['per_bit']['reference']['MSB'] for n in ns], ':', lw=1, color=INK, label='address bits, value order')
ax.plot(ns, [rr[str(n)]['face']['per_bit']['reference']['MSB'] for n in ns], ':', lw=1, color=BLUE, label='face, value order')
ax.set_xlabel('word width n'); ax.set_ylabel('mean arrivals until ready')
ax.set_title('Best of all n! orders (solid), value order (dotted)')
ax.legend(fontsize=6.2, loc='upper left', ncol=1)
clean(ax)
ax = axes[1]
nk = list(range(7, 20))
k = [2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6]
core = [n - 2 * kk for n, kk in zip(nk, k)]
ax.bar(nk, [2 * kk for kk in k], color=BLUE, width=0.7, label='outer pairs, outside-in')
ax.bar(nk, core, bottom=[2 * kk for kk in k], color=ORANGE, width=0.7, label='core, by value')
for n, kk, c in zip(nk, k, core):
    ax.text(n, n + 0.3, str(kk), ha='center', va='bottom', fontsize=6, color=INK2)
ax.set_xlabel('word width n'); ax.set_ylabel('bits')
ax.set_title('Optimal address reader; k outer pairs on top')
ax.legend(fontsize=6.2, loc='upper left')
ax.set_ylim(0, 23)
clean(ax)
fig.tight_layout()
fig.savefig('figs/fig2_readers.png')
plt.close(fig)

# ---------------- Figure 3: witness at D = 32 and the preimage shells
D = 32
t = (D - 2) // 3; p = 2 * t + 3
u = Fraction(1, 2) + Fraction(1, 1 << p) + (Fraction(2, 3) + Fraction(1, 4 * D)) * Fraction(1, 1 << (D - 1))
fig, axes = plt.subplots(1, 2, figsize=(6.6, 3.2), gridspec_kw={'width_ratios': [1.35, 1]})
ax = axes[0]; ax.grid(False)
target = '1' + '00' + '1' * (D - 5) + '00'
for L in range(1, D + 1):
    x = (1 << L) * u
    i = floor(x); kk = floor(L * (x - i))
    wd = wh.word(i, L)
    y = D - L
    for b in range(L):
        bit = (wd >> (L - 1 - b)) & 1
        ax.add_patch(Rectangle((b, y), 0.92, 0.82, facecolor='white' if bit else INK2, edgecolor=AXIS if bit else INK2, lw=0.3))
    rb = (wd >> (L - 1 - kk)) & 1
    ax.add_patch(Rectangle((kk - 0.12, y - 0.12), 1.16, 1.06, facecolor='none', edgecolor=ORANGE, lw=1.1))
    ax.text(-0.8, y + 0.4, str(L), ha='right', va='center', fontsize=4.6, color=MUTED)
    ax.text(L + 0.6, y + 0.4, target[L - 1], ha='left', va='center', fontsize=4.6, color=ORANGE if rb == 0 else MUTED)
ax.axhline(D - p + 0.91, color=BLUE, lw=0.6, ls='--')
ax.text(D - 0.5, D - p + 1.25, f'first offset, ring p = {p}', ha='right', va='bottom', fontsize=5.5, color=BLUE)
ax.set_xlim(-2.5, D + 2.5); ax.set_ylim(-0.6, D + 0.4)
ax.set_xticks([]); ax.set_yticks([])
for s_ in ax.spines.values():
    s_.set_visible(False)
ax.set_title(f'D = {D}: word read on each ring (dark = 0), slice boxed')
ax = axes[1]
src = open('/home/claude/atlas/preimage_map.py').read().split('T0 = time.time()')[0]
ns_ = {'__file__': '/home/claude/atlas/preimage_map.py'}
exec(src, ns_)
for Dq, col in ((20, GREY), (24, BLUE), (28, ORANGE)):
    tq = '1' + '00' + '1' * (Dq - 5) + '00'
    A = [(Fraction(0), Fraction(1))]
    for L in range(1, Dq + 1):
        A = ns_['refine'](A, L, int(tq[L - 1]))
    tot = sum(b - a for a, b in A)
    shells = {}
    for a, b in A:
        d = a - Fraction(1, 2); kq = 0
        while d < Fraction(1, 1 << kq) and kq < 90:
            kq += 1
        shells[kq] = shells.get(kq, 0) + (b - a)
    ks = sorted(shells)
    ax.plot(ks, [float(shells[q] / tot) for q in ks], '-o', ms=2.4, lw=0.9, color=col, label=f'D = {Dq}')
    pD = 2 * ((Dq - 2) // 3) + 3
    ax.axvline(pD, color=col, lw=0.6, ls=':')
ax.set_yscale('log')
ax.set_xlabel('shell k:  u − 1/2 in [2^−k, 2^−k+1)')
ax.set_ylabel('share of the preimage measure')
ax.set_title('Preimage of q_D by shell (dotted: p_D)')
ax.legend(fontsize=6.5)
clean(ax)
fig.tight_layout()
fig.savefig('figs/fig3_witness.png')
plt.close(fig)
print('figures written')
