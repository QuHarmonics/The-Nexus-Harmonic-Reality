"""Observation (not sealed): the partner as a context bit in a bilevel image coder.
Glyphs rendered 1-bit from DejaVu Sans Bold; a JBIG-style 12-pixel template, with and without the mirror pixels
(columns W-2-x, W-1-x, W-x of the current row, available once x passes the axis). Ideal adaptive code length:
for a binary KT estimator the total depends only on the counts per context, so it is computed exactly from counts."""
import lzma, os, json
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy.special import gammaln
import matplotlib

FONT = ImageFont.truetype(os.path.join(matplotlib.get_data_path(), 'fonts', 'ttf', 'DejaVuSans-Bold.ttf'), 150)
W = 192
SYM, ASYM = 'AHIMOTUVWXY08', 'BCDEFGJKLNPQRSZ'

def glyph(ch):
    im = Image.new('1', (W, W), 0); d = ImageDraw.Draw(im)
    l, t, r, b = d.textbbox((0, 0), ch, font=FONT)
    d.text((round((W - (r - l)) / 2 - l), round((W - (b - t)) / 2 - t)), ch, fill=1, font=FONT)
    return np.array(im, dtype=np.int64)

def kt_bits(n0, n1):
    return float(np.sum(-(gammaln(n0 + 0.5) + gammaln(n1 + 0.5) - gammaln(n0 + n1 + 1) - np.log(np.pi)) / np.log(2)))

def code_length(img, mirror):
    H, Wd = img.shape; P = np.pad(img, ((2, 0), (4, 4)))           # zero padding above and to the sides
    y0, x0 = 2, 4; Y, X = np.mgrid[0:H, 0:Wd]
    g = lambda dy, dx: P[Y + y0 + dy, X + x0 + dx]
    bits = [g(0, -1), g(0, -2), g(0, -3), g(0, -4), g(-1, -2), g(-1, -1), g(-1, 0), g(-1, 1), g(-1, 2), g(-2, -1), g(-2, 0), g(-2, 1)]
    ctx = np.zeros_like(img)
    for b in bits: ctx = (ctx << 1) | b
    if mirror:
        have = np.zeros_like(img)
        for off in (-2, -1, 0):
            m = Wd - 1 - X + off                                     # mirror column about the canvas axis, and its neighbours
            ok = (m >= 0) & (m < X)                                  # already decoded in this row
            v = np.where(ok, img[Y, np.clip(m, 0, Wd - 1)], 0)
            ctx = (ctx << 1) | v; have = have | ok
        ctx = (ctx << 1) | have
    keys = ctx * 2 + img
    cnt = np.bincount(keys.ravel(), minlength=2 * (int(ctx.max()) + 1))
    n0 = cnt[0::2]; n1 = cnt[1::2]; used = (n0 + n1) > 0
    return kt_bits(n0[used], n1[used])

def sheet(chars):
    return np.concatenate([glyph(c) for c in chars], axis=0)

def symmetry(img_rows):
    """share of non-empty rows equal to their own mirror about the best axis (integer or half-integer offset)"""
    rows = [r for r in img_rows if r.any()]; best = 0
    for off in range(-3, 4):
        s = sum(np.array_equal(r, np.roll(r[::-1], off)) for r in rows); best = max(best, s)
    return best / max(len(rows), 1)

out = {}
for name, chars in (('symmetric', SYM), ('asymmetric', ASYM)):
    S = sheet(chars); px = S.size
    plain = code_length(S, False); mir = code_length(S, True)
    raw_lz = len(lzma.compress(np.packbits(S.astype(np.uint8)).tobytes(), preset=9 | lzma.PRESET_EXTREME))
    sym_share = float(np.mean([symmetry(glyph(c)) for c in chars]))
    out[name] = {'glyphs': chars, 'pixels': int(px), 'lzma_bytes': raw_lz, 'template_bits': plain, 'template_plus_mirror_bits': mir,
                 'ratio': mir / plain, 'exactly_symmetric_row_share': sym_share}
    print(f"{name:10s} {chars:16s} {px:7,} px  lzma {raw_lz:6,} B  template {plain/8:8.0f} B  +mirror {mir/8:8.0f} B  ratio {mir/plain:.3f}  "
          f"rows exactly mirror-symmetric (best axis): {sym_share:.3f}")
json.dump(out, open('mirror_context_results.json', 'w'), indent=2)
