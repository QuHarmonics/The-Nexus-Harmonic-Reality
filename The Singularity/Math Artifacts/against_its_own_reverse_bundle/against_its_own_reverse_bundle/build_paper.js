// build_paper.js — "Against Its Own Reverse" (Dean A. Kulik, QuHarmonics Research Group)
const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, ImageRun, Table, TableRow, TableCell,
        WidthType, BorderStyle, ShadingType, Footer, Header, PageNumber, PageBreak } = require('docx');

const BODY = 'Cambria', MATH = 'Cambria Math', MONO = 'Consolas';
const INK = '0B0B0B', INK2 = '52514E', MUTED = '898781', RULE = 'C3C2B7';
const W = 9360; // content width in DXA (US Letter, 1" margins)

// ---------- inline markup: **bold** *italic* ^{sup} _{sub} [[status]] ----------
function runs(text, base = {}) {
  const out = []; let i = 0, buf = '';
  let bold = !!base.bold, ital = !!base.italics, sup = false, sub = false, status = false;
  const flush = () => {
    if (!buf) return;
    out.push(new TextRun({ text: buf, bold: bold || status, italics: ital, superScript: sup, subScript: sub,
      font: base.font || BODY, size: status ? (base.size || 21) - 2 : (base.size || 21),
      color: status ? INK2 : (base.color || INK) }));
    buf = '';
  };
  while (i < text.length) {
    const two = text.slice(i, i + 2);
    if (two === '**') { flush(); bold = !bold; i += 2; continue; }
    if (two === '^{') { flush(); sup = true; i += 2; continue; }
    if (two === '_{') { flush(); sub = true; i += 2; continue; }
    if (two === '[[') { flush(); status = true; buf = '['; i += 2; continue; }
    if (two === ']]') { buf += ']'; flush(); status = false; i += 2; continue; }
    const ch = text[i];
    if (ch === '}' && (sup || sub)) { flush(); sup = false; sub = false; i += 1; continue; }
    if (ch === '*') { flush(); ital = !ital; i += 1; continue; }
    buf += ch; i += 1;
  }
  flush();
  return out;
}

const blocks = [];
const sp = (b = 0, a = 120) => ({ before: b, after: a, line: 276 });
function P(text, o = {}) {
  blocks.push(new Paragraph({ children: runs(text, o), alignment: o.align || AlignmentType.JUSTIFIED,
    spacing: o.spacing || sp(0, 120), indent: o.indent, keepNext: o.keepNext }));
}
function ITEM(text) { P(text, { indent: { left: 567, hanging: 340 }, spacing: sp(0, 80) }); }
function H1(text) { blocks.push(new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text, bold: true, font: BODY, size: 26, color: INK })], spacing: { before: 320, after: 140 }, keepNext: true })); }
function H2(text) { blocks.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text, bold: true, font: BODY, size: 22, color: INK })], spacing: { before: 220, after: 100 }, keepNext: true })); }
function EQ(text) {
  blocks.push(new Paragraph({ children: runs(text, { font: MATH, size: 22 }), alignment: AlignmentType.CENTER, spacing: { before: 80, after: 140, line: 276 }, keepNext: false }));
}
function THM(label, text, o = {}) {
  blocks.push(new Paragraph({ children: [new TextRun({ text: label + ' ', bold: true, font: BODY, size: 21, color: INK }), ...runs(text)],
    alignment: AlignmentType.JUSTIFIED, spacing: sp(60, 120), keepNext: o.keepNext }));
}
function PROOF(text) {
  blocks.push(new Paragraph({ children: [new TextRun({ text: 'Proof. ', italics: true, font: BODY, size: 21, color: INK }), ...runs(text)],
    alignment: AlignmentType.JUSTIFIED, spacing: sp(0, 140) }));
}
function pngSize(file) { const b = fs.readFileSync(file); return [b.readUInt32BE(16), b.readUInt32BE(20)]; }
function FIG5(file, caption) { FIG(file, caption, 500); }
function FIG(file, caption, widthPx = 610) {
  const [w, h] = pngSize(file);
  blocks.push(new Paragraph({ children: [new ImageRun({ type: 'png', data: fs.readFileSync(file), transformation: { width: widthPx, height: Math.round(widthPx * h / w) } })],
    alignment: AlignmentType.CENTER, spacing: { before: 160, after: 60 }, keepNext: true }));
  blocks.push(new Paragraph({ children: runs(caption, { size: 18, italics: false, color: INK2 }), alignment: AlignmentType.JUSTIFIED, spacing: { before: 0, after: 220, line: 252 } }));
}
const hair = { style: BorderStyle.SINGLE, size: 4, color: RULE };
function TABLE(widths, rows, o = {}) {
  const sum = widths.reduce((a, b) => a + b, 0);
  const trs = rows.map((row, ri) => new TableRow({ tableHeader: ri === 0 && o.header !== false, cantSplit: true,
    children: row.map((cell, ci) => new TableCell({
      width: { size: widths[ci], type: WidthType.DXA },
      shading: ri === 0 && o.header !== false ? { type: ShadingType.CLEAR, fill: 'F0EFEC', color: 'auto' } : undefined,
      margins: { top: 50, bottom: 50, left: 90, right: 90 },
      children: [new Paragraph({ children: runs(cell, { size: o.size || 18, bold: ri === 0 && o.header !== false, font: (o.mono || []).includes(ci) && ri > 0 ? MONO : BODY }),
        alignment: (o.center || []).includes(ci) ? AlignmentType.CENTER : AlignmentType.LEFT, spacing: { before: 0, after: 0, line: 240 } })] })) }));
  blocks.push(new Table({ width: { size: sum, type: WidthType.DXA }, columnWidths: widths, rows: trs,
    borders: { top: hair, bottom: hair, left: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, right: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, insideHorizontal: hair, insideVertical: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' } } }));
  if (o.caption) blocks.push(new Paragraph({ children: runs(o.caption, { size: 18, color: INK2 }), alignment: AlignmentType.JUSTIFIED, spacing: { before: 80, after: 220, line: 252 } }));
  else blocks.push(new Paragraph({ children: [], spacing: { before: 0, after: 120 } }));
}
function BOX(paras) {
  const kids = paras.map(t => new Paragraph({ children: runs(t, { size: 19 }), alignment: AlignmentType.JUSTIFIED, spacing: { before: 0, after: 90, line: 260 } }));
  blocks.push(new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: [W], rows: [new TableRow({ children: [new TableCell({ width: { size: W, type: WidthType.DXA },
    shading: { type: ShadingType.CLEAR, fill: 'F7F7F5', color: 'auto' }, margins: { top: 140, bottom: 80, left: 200, right: 200 }, children: kids })] })],
    borders: { top: hair, bottom: hair, left: hair, right: hair, insideHorizontal: hair, insideVertical: hair } }));
  blocks.push(new Paragraph({ children: [], spacing: { before: 0, after: 160 } }));
}
function MONOLINES(lines, size = 15) {
  for (const l of lines) blocks.push(new Paragraph({ children: [new TextRun({ text: l.length ? l : ' ', font: MONO, size, color: INK })], spacing: { before: 0, after: 0, line: 228 } }));
  blocks.push(new Paragraph({ children: [], spacing: { before: 0, after: 160 } }));
}
function PAGEBREAK() { blocks.push(new Paragraph({ children: [new PageBreak()] })); }

// ======================================================================= CONTENT
// Title block
blocks.push(new Paragraph({ children: [new TextRun({ text: 'Qu Harmonics – The incomplete Universe', font: BODY, size: 18, color: MUTED, smallCaps: true })], alignment: AlignmentType.CENTER, spacing: { before: 0, after: 360 } }));
blocks.push(new Paragraph({ children: [new TextRun({ text: 'Against Its Own Reverse', font: BODY, size: 44, bold: true, color: INK })], alignment: AlignmentType.CENTER, spacing: { before: 0, after: 160 } }));
blocks.push(new Paragraph({ children: [new TextRun({ text: 'One comparison of each binary word with its reverse builds the ring’s address, its sphere and its waveform', font: BODY, size: 24, italics: true, color: INK2 })], alignment: AlignmentType.CENTER, spacing: { before: 0, after: 280 } }));
blocks.push(new Paragraph({ children: [new TextRun({ text: 'Driven by Dean A. Kulik', font: BODY, size: 22, color: INK })], alignment: AlignmentType.CENTER, spacing: { before: 0, after: 60 } }));
blocks.push(new Paragraph({ children: [new TextRun({ text: 'QuHarmonics Research Group · ORCID 0009-0003-3128-8828', font: BODY, size: 18, color: INK2 })], alignment: AlignmentType.CENTER, spacing: { before: 0, after: 60 } }));
blocks.push(new Paragraph({ children: [new TextRun({ text: 'October 2026', font: BODY, size: 20, color: INK2 })], alignment: AlignmentType.CENTER, spacing: { before: 0, after: 360 } }));

P('**Status words.** A bracket after a statement records how it stands. **proved**: proved in this paper. **STANDS**: established earlier in the series or in the literature. **RUNS**: an exact computation landed where the route put it, with its scope stated; every one is rerun by the scripts of Appendix B. **SEALED**: the prediction was written and its text hashed (SHA-256) before the computation that tests it was run; the texts and digests are in Appendix A. **DEAD END**: the computation ran and landed, and the landing belongs to something else, whose owner is named. **OPEN**: stated and not settled. **PULL**: an interpretive bridge, not a result. Work run in independent AI-assisted audits is marked *independently*.', { size: 19 });

H1('Abstract');
P('Compare every binary word with its own reverse. Write each mirrored pair of bits as a value beside a difference, the butterfly (u, u ⊕ v) taken across the mirror. The comparison is decided by the outermost pair that differs, and the Hamming weight is carried by the pairs that agree. This paper shows that the ring of all binary words is built from those two readers of one lifted word. The partner map reverses the difference half, or complements the value half when there is no difference. The address of a word is half of what lies below it plus half of the reversal pairs its own value separates, rank(p) = ½(p − π(p) + Δ(p)) + π_{c}(p), where Δ(p) = #{x : x < p ≤ J(x)} has a closed digit form and grows by a borrow chain whose cell is the full adder’s carry with one input complemented; the first 64 bits of π land at 2,427,008,858,123,944,441 from one pass over the 32 bits of each half. The route that grows a word one bit at a time is the lift itself: its residual bits are the mirrored differences, innermost first. On the sphere of radius n and latitude z = wt − n/2, latitude reads only the agreeing pairs, so the poles belong to the palindromes and a word with k disagreeing pairs stays within |z| ≤ ⌊n/2⌋ − k + [n odd]/2; the partner is a reflection, and on palindromes a half-turn about the X-axis. On ring addresses the partner is the complement of the address, so the latitude splits into a Walsh-even body and a Walsh-odd palindrome carrier whose energy share is exactly 2^{1−n/2} at even width. Pulled back, each reader is simple in its own coordinates and spread in the other’s: over the bits of a word the comparison needs 2(2^{⌊n/2⌋} − 1) Walsh modes and the latitude n; over ring addresses the comparison is one address bit carrying 99.9% of its energy at n = 20, while the latitude fills 1,036,432 of 1,048,576 modes. The ring is the coordinate system of the comparison.');

H1('How the paper runs');
P('The paper is written from its end. Section 1 states the finished object: a formula that places any word of any width in the ring of all words, and the same formula read as a change of coordinates. Sections 2 to 9 follow that object back along the path that produced it. Each section opens on the hole the previous result left, names what must fill it by its shape and its neighbours, and shows the fill falling out of what was already built; no section found its result by trying candidates against a readout. Section 10 pulls back and reads the whole. Every value was derived before it was computed; the predictions hashed before their runs are in Appendix A, and every statement is rerun by the scripts of Appendix B.');

// ---------------------------------------------------------------- 1
H1('1. The held end');
P('Let x be a word of n bits, x = x_{0}x_{1}…x_{n−1}, read as an integer with x_{0} most significant, and let J reverse it. Write h = ⌊n/2⌋, H = 2^{h}, N = 2^{n} and M = 2^{n−1}. In the ring R_{n} of *Only Addressable* the representatives, the smaller member of each pair {x, P(x)}, ascend on the left face from address 0, and their partners descend on the right.');
THM('Theorem 1 (the address).', 'For every threshold p, the number of representatives below p is', { keepNext: true });
EQ('rank(p) = ½ (p − π(p) + Δ(p)) + π_{c}(p),');
P('where π(p) counts the palindromes below p, π_{c}(p) = min(π(p), 2^{⌈n/2⌉−1}) counts the canonical ones among them, and', { keepNext: true });
EQ('Δ(p) = #{ x : x < p ≤ J(x) }');
P('counts the reversal pairs that the cut at p separates. A canonical word a sits at address rank(a), except the largest, which the seam swap places at M; its partner sits at N − 1 minus that address. [[proved; SEALED, RUNS: every threshold n = 2..20 independently, every position n = 2..14 here, widths to 1,024 against the mirrored-pair dynamic program]]');
P('Nothing in Theorem 1 is counted by enumeration. The palindrome counts are read off the first ⌈n/2⌉ bits of p, and Δ is read off p by a closed digit formula (Section 7). For even n, writing p = AH + B with A and B its halves,', { keepNext: true });
EQ('Δ(p) = A(H − A) + B − 2ℛ_{h}(B, A) − [J_{h}(A) < B],');
P('where ℛ_{h}(B, A), the number of b < B whose h-bit reverse is below A, is a sum of h ceilings. So the address of a word is half of what lies below it, plus half of the reversal pairs its own value separates.');
P('Two readings show the scale. The first 64 bits of π, 0x243F6A8885A308D3, sit at address 2,427,008,858,123,944,441 of the 64-bit ring. *Only Addressable* reached that value with a dynamic program over mirrored pairs; here it comes out of the formula in one pass over the 32 bits of each half. On sixty random words of widths 64, 255, 256, 512 and 1,024 the formula and the dynamic program agree. [[SEALED, RUNS]]', { align: AlignmentType.LEFT });
P('Read from the other side, Theorem 1 says that Δ is the change of coordinates from a word’s value to its place, and Theorem 10.2 says what the place is for: on ring addresses, the comparison of a word with its reverse is one address bit. The rest of the paper follows how that end was reached.');

// ---------------------------------------------------------------- 2
H1('2. The ring and its one comparison');
P('The pairing is P(x) = J(x) when J(x) ≠ x and P(x) = C(x), the complement, when x is a palindrome. P is an involution without fixed points at every length, so the 2^{n} words fall into 2^{n−1} pairs and the palindromes pair among themselves. Place the representatives x < P(x) in increasing order at addresses 0 to M − 1, their partners in decreasing order at M to N − 1, and swap the two words at M − 1 and M. Then R_{n}[N − 1 − i] = P(R_{n}[i]) at every address: the facing law. Every word is located in O(n) arithmetic without building the ring, and Lemma A, the clean cores of Theorem C, the pad law of Theorem D and the witness law of Theorem E describe the top quarter of every ring. [[STANDS: *Only Addressable*; *Decompiling Addressable Binary Rings*]]');
P('All of this rests on one comparison. Define', { keepNext: true });
EQ('c(x) = sgn(J(x) − x) ∈ {−1, 0, +1}.');
P('A word is a representative exactly when c(x) = +1, or when c(x) = 0 and x_{0} = 0, the palindromes that begin with 0. [[proved]] The comparison is the only thing the ring asks of a word. Its running sum over the integers below a cut,', { keepNext: true });
EQ('Δ(p) = Σ_{x < p} c(x),');
P('is the quantity in Theorem 1.');
THM('Proposition 2 (the cut).', 'Δ(p) = #{x : x < p ≤ J(x)}. Hence Δ ≥ 0, Δ(0) = Δ(N) = 0 and Δ(N − p) = Δ(p). [[proved; RUNS: every threshold, n = 2..14]]');
PROOF('A reversal pair {x, J(x)} with x < J(x) contributes +1 at x and −1 at J(x). If both lie below p they cancel, if neither does the pair contributes nothing, and if p separates them it contributes +1. Complementing every word maps reversal pairs to reversal pairs and the cut at p to the cut at N − p. ∎');
P('Δ(p) is the number of reversal relations a reader standing at the value p must carry across it to know how many representatives lie behind it. That is the sense in which it is a carry: what crosses a cut.');

// ---------------------------------------------------------------- 3
H1('3. The hole between L and L + 2');
P('*Only Addressable* left one link of its ledger open: a map from one ring’s words to the next ring’s addresses beyond the pad law. The pad law carries ring L to ring L + 2 and skips the odd ring between them. The shape of the missing piece is fixed by its neighbours: one step of one bit that, done twice, is the pad law.');
P('The middle bit of an odd word is compared only with itself. It is therefore the first free bit of every block of Lemma A, and inserting it is the whole step from even to odd.');
THM('Theorem 3 (even to odd).', 'Let L = 2h and let I_{b} insert the bit b at the middle. The canonical words of width L + 1 are exactly the I_{0}(a) and I_{1}(a) for a canonical of width L, each once. In descending canonical order, with A the left half of a, K = H − 1 − A, D_{K} = K(K − 1)/2 + max(0, K − H/2) and S_{K} = K + [K ≥ H/2], a parent at offset q = D_{K} + i has its children at', { keepNext: true });
EQ('q_{1} = 2D_{K} + i  (middle 1),    q_{0} = 2D_{K} + S_{K} + i  (middle 0).');
P('[[proved; RUNS: every parent, L = 4..16 here; every odd child to width 19 independently]] Before palindromes enter the blocks, K < H/2, these are K(K − 1) + i and K² + i: block K of the odd ring is block K of the even ring twice, middle 1 first.');
P('The pair readout cannot tell the two children apart. x ⊕ P(x) is the same for both: the parent’s readout with a 0 in the middle, or all ones for palindromes. The middle bit is exactly what the readout omits, the value kept beside the difference.');
P('The odd-to-even step then has an obvious half and a homeless half. The children with middle 1 carry forward: drop the middle bit and put a 1 at each end, and the two steps together are the pad law. The children with middle 0 have no place under that carry. That piece with no way home was the next hole.');

// ---------------------------------------------------------------- 4
H1('4. The outer pair, and the gauge the word can read');
P('What must fill the hole is fixed by counting. Ring L + 2 has 2^{L+1} canonical words and ring L + 1 has 2^{L}, so every odd child accounts for two even ones. The outer pair of an even word is either equal, 00 or 11, or mixed, 01; the mixed pair 10 is the partner face. Two independent fills arrived, and both cut the target by that frame. One is', { keepNext: true });
EQ('E_{m}(x) = canon(m x m),    G_{m}(x) = 0 P^{m}(x) 1,');
P('for x canonical of even width L and m the middle bit of the odd child, with canon(z) = min(z, P(z)) and P^{m} meaning P applied m times. E fills the equal frames, including the palindrome exception E_{1}(x) = 0 C(x) 0, G fills the mixed frame, and together they partition every canonical word of width L + 2. [[proved; RUNS: L = 2..14 here; to width 20 independently]] The other fill, a four-family table, binds the same partition with a branch label that has to be stored.');
P('The labeling is forced by readability. In E/G the branch bit is d = x_{0} ⊕ x_{L+1}, the difference of the new outer pair, and the odd child’s middle bit is read off the word: it is the frame bit when d = 0, the palindrome exception aside, and the face of the core when d = 1. [[RUNS: L = 2..16]] Nothing has to be remembered. The four-family label has to be.');
P('So the even-to-odd step inserts a pure value, whose difference is 0, and the odd-to-even step inserts a pair carrying a value and a difference, (m, m ⊕ d). That is the butterfly (u, v) ↦ (u, u ⊕ v), the elementary step of the fast Möbius transform of the Boolean lattice, applied across the mirror instead of across neighbouring indices. [[STANDS: Rota 1964; *Only Addressable*, §2.2]] When d = 1 the frame is canonical by itself and has no room for m, so m moves inward and becomes the face of the core. The homeless middle-0 piece is the value that leaves the frame.');
P('Write that lift for a whole word. Pair j, for j = 0 to h − 1 with j = 0 outermost, has value v_{j} = x_{j} and difference δ_{j} = x_{j} ⊕ x_{n−1−j}; at odd n the middle bit x_{h} stands alone. The map x ↦ (v, δ, x_{h}) is the butterfly on every pair and loses nothing.');
FIG('figs/fig1_lift.png', '**Figure 1.** The mirror lift of the 12-bit word 100110110101. Arcs join mirrored pairs; orange arcs are the pairs that differ. Each pair is a value beside a difference. The latitude reads only the agreeing pairs, +1 for 11 and −1 for 00. The comparison reads only the outermost disagreeing pair, here pair 2, whose 0 on the high side makes the word smaller than its reverse. The route that grows this word records the differences from the inside out.');
THM('Theorem 4 (the route is the mirror lift).', 'Grow every word from the one-bit root 0: the first step chooses 00 or 01, odd steps insert a middle bit, even steps apply E (d = 0) or G (d = 1), and a final side bit ε chooses the canonical word or its partner. This is a bijection between the words of n bits and n − 1 route bits plus ε, and the route’s residual bits, the first choice and every d, are the mirror differences δ_{h−1}, δ_{h−2}, …, δ_{0}, innermost first. [[proved; SEALED, RUNS: every word n = 2..18; round trip n ≤ 12]]');
PROOF('Each even step adds a new outermost pair whose difference is d, since E frames are mm and G frames are 01. Every later operation on the inner word is a reversal or a complement (canonicalization, the partner face of G_{1}, the palindrome exception, the final side), and both preserve every mirrored difference. The middle bit inserted at an odd step leaves the middle at the next even step, into the frame or into the face, so it never becomes a pair. ∎');
P('With the rank of Section 7 the chain closes, each step invertible: from (route, ε) to the word x, to (q, ε), to the address, where q = M − 1 − rank(a) is the descending offset of the canonical member a, its address is M when q = 0 and M − 1 − q otherwise, and its partner sits at N − 1 minus that. [[RUNS: 8,188 words across two independent implementations, n = 2..12; scalar queries at 64, 256 and 512 bits]] From here the address mechanism is a provider, not an open link.');

// ---------------------------------------------------------------- 5
H1('5. The sphere');
P('The rings are planar and each width is its own ring. The next hole was one frame holding every width at once. Its radius is fixed by the route: every step adds one bit, so the radius is the width n. It needs one more coordinate per word that both halves of the partner act on simply, and weight is the only one: reversal keeps it, and complement sends w to n − w. So the coordinates are radius n, latitude z = wt(x) − n/2, and azimuth θ = 2π((i + ½)/2^{n} − ½) for the word at address i, the seam at θ = 0. In Cartesian form Z = 2z and (X, Y) = √(n² − Z²)·(cos θ, sin θ).');
THM('Theorem 5 (the partner on the sphere).', 'P sends (θ, z) to (−θ, z) on non-palindromes and to (−θ, −z) on palindromes; in Cartesian form (X, Y, Z) ↦ (X, −Y, Z) and (X, −Y, −Z). It is a reflection in the XZ-plane, and on the palindromes a half-turn about the X-axis. It is never an azimuthal half-turn. [[proved; RUNS: every word, n = 2..20, all 228 weight bands]]');
PROOF('The facing law sends address i to N − 1 − i, which is θ ↦ −θ. Reversal keeps the weight and complement sends z to −z. An azimuthal half-turn would send i to i + N/2 (mod N); the two agree only if 2i ≡ N/2 − 1 (mod N), whose right side is odd for every n ≥ 2. ∎');
P('The half-turn about the X-axis equals the antipode only at the poles.');
P('Along the route the latitude walks in half-steps. Inserting a middle bit m moves z by m − ½, and the next even step gives z_{child} = τ [z_{odd} + (m − ½)(−1)^{d}], with τ = −1 exactly when the core is a palindrome and m = 1. [[RUNS: 699,048 lift outputs to width 20 independently; L = 2..14 here]] Away from the reflections, two steps move the latitude by (2m − 1)[d = 0]: an agreeing pair adds its value, and a disagreeing pair adds nothing. That is the whole of the next statement.');
THM('Proposition 5.1 (latitude is the value half).', 'z(x) = Σ_{agreeing j} (2v_{j} − 1) + [n odd](x_{h} − ½). A word with k disagreeing pairs therefore satisfies |z| ≤ h − k + [n odd]/2, and every bound is attained. The poles z = ±n/2 belong to the palindromes 0^{n} and 1^{n}, and every word that differs from its reverse lies within |z| ≤ n/2 − 1. The words with k disagreeing pairs and t agreeing pairs of value 1 number C(h, k)·2^{k}·C(h − k, t), doubled at odd n; summed over k they give the binomial C(n, w), and k = 0 gives the palindromes. [[proved; SEALED, RUNS: every word n = 2..18]]');
PROOF('A disagreeing pair holds exactly one 1. Choose the k disagreeing pairs, their orientations, and which of the agreeing pairs are 11. ∎');
P('The more a word differs from its reverse, the nearer the equator it must sit. Here C(n, w) counts the weight-w words, the fixed-weight basis states; it is not the dimension of the symmetric spin sector, which is n + 1. The arithmetic of the latitude walk is exact, and its reading as physical spin is a PULL.');

// ---------------------------------------------------------------- 6
H1('6. The waveform');
P('With the sphere in place, the waveform to look for is the latitude as a function of address, z(i). Its shape is forced before anything is computed. The partner’s address N − 1 − i is i with every bit complemented, and complementing the address multiplies the Walsh coefficient of mode s by (−1)^{|s|}, where |s| is the number of ones in s. Write W[f](s) = Σ_{x} f(x)(−1)^{s·x} for the unnormalized Walsh transform.');
THM('Theorem 6 (the ring turns the partner into parity).', 'For any function g on words, put g_{R}(i) = g(R_{n}[i]). If g∘P = g, then g_{R} has only even-degree Walsh coefficients; if g∘P = −g, only odd ones. Every g splits into a P-even and a P-odd part, and they land on the even and the odd degrees. [[proved; SEALED, RUNS: |z|, the palindrome-masked z and c, n = 2..16; c to n = 20]]');
PROOF('By the facing law g_{R}(N − 1 − i) = (g∘P)(R_{n}[i]), and N − 1 − i is the complement of i. ∎');
P('The latitude is P-even off the palindromes and P-odd on them (Theorem 5). So z(i) splits into a Walsh-even body z_{+} on the non-palindromes and a Walsh-odd carrier z_{−} on the palindromes, with disjoint supports in frequency.');
THM('Corollary 6.1 (the energy law).', 'The share of the latitude’s Walsh energy in odd degrees is 2^{1−n/2} for even n and (4h + 1)/((2h + 1)·2^{h}) for n = 2h + 1. [[proved; SEALED, RUNS exactly in rational arithmetic, n = 2..20]]');
PROOF('The odd energy is the palindromes’ energy. Each mirrored pair of a palindrome is a free bit worth ±2 in 2z, and the middle bit ±1, so the palindromes contribute 4h·2^{h}, or (4h + 1)·2^{h+1} at odd width, against n·2^{n} for all words. ∎');
TABLE([1640, 1100, 1100, 1100, 1100, 1100, 1100, 1120], [
  ['width n', '2', '3', '4', '6', '7', '10', '20'],
  ['odd share', '1', '5/6', '1/2', '1/4', '13/56', '1/16', '1/512']],
  { center: [1, 2, 3, 4, 5, 6, 7], caption: '**Table 1.** Odd-degree share of the latitude’s Walsh energy, exact. At even width it halves with every two bits of radius.' });
FIG('figs/fig2_sphere_waveform.png', '**Figure 2.** Left: all 1,024 words of width 10 on the sphere, at latitude z and at the azimuth of their ring address; orange are the 32 palindromes, which alone reach the poles. Right: the latitude around the ring at n = 12. The body (blue) is the Walsh-even part and the carrier (orange) the Walsh-odd part. The south and north poles sit side by side at the closure, θ = ±π, and that jump belongs entirely to the carrier.');
P('The carrier is a ring of half the width hidden in ring n: there are 2^{⌈n/2⌉} palindromes, one for each half-word. The literal copy of the smaller ring is not there. In ring order the palindromes read their half-words in counting order 0, 1, 2, …, because the canonical palindromes ascend on the left face and their complemented partners continue the count on the right. [[proved; RUNS: n = 2..20]] The order copy is a DEAD END for n ≥ 3, owned by the counting order. Re-addressed through the smaller ring the waveform does survive: for n = 2m, z_{n}(i(R_{m}[j])) = 2z_{m}(j), with a correction ½ − (last bit) at odd width. [[RUNS independently, n = 2..20]]');
P('In its own half-word coordinates the carrier is linear: 2z = −2 Σ_{j} χ_{j}(u), with the middle coordinate weighted −1 at odd width, where χ_{j}(u) = (−1)^{u_j}. That is Proposition 5.1 with every pair agreeing. All of the carrier’s higher odd degrees on the ring come from where the palindromes are put. The placement operator, carried into Walsh coordinates, is an isometry on its image; it keeps parity and mixes degrees within it. [[RUNS independently: complete matrices n = 2..12; the carrier rebuilt from ⌈n/2⌉ transported columns at every width to 20]] The first mixing appears at n = 5, in the address of the palindrome with half-word u = 4u_{2} + 2u_{1} + u_{0}:', { keepNext: true });
EQ('i_{5}(u) = 4u + 2u_{2} + Maj(1 − u_{0}, u_{1}, u_{2}).');
P('[[RUNS: all eight half-words]] A majority with one complemented input is the borrow cell of a subtractor. The placement had to be a comparator.');

// ---------------------------------------------------------------- 7
H1('7. The address is a comparator');
P('The hole was a gate-level description of the palindrome address at every width, and the gate at n = 5 fixed its kind.');
THM('Theorem 7.1 (the palindrome address).', 'A canonical palindrome p with half-word u sits at', { keepNext: true });
EQ('i_{n}(u) = ½ (p + u + Δ(p)),');
P('and the upper half follows by the reflection i_{n}(u) = N − 1 − i_{n}(2^{⌈n/2⌉} − 1 − u). [[proved; SEALED, RUNS: every palindrome n = 2..20]]');
PROOF('p is on the left face away from the seam, so its address is its rank. Below p lie u palindromes and p − u other words, which split into representatives and non-representatives whose difference is Δ(p). ∎');
THM('Theorem 7.2 (the gate).', 'c(x) = β(x − J(x)) − β(J(x) − x), where β is the borrow out of a ripple subtractor whose cell is β′ = Maj(¬a, b, β). [[proved; SEALED, RUNS: every word n = 2..16]]');
P('The cell is the full adder’s carry with one input complemented. The ring computes its own addresses with the adder’s gate, read at a different location: across a word and its own reverse.');
P('Extending Theorem 7.1 from palindromes to every threshold gives Theorem 1. Count the non-palindromes below p, of which ½(p − π(p) + Δ(p)) are representatives, and add only the canonical palindromes. The first form, ½(p + π + Δ), is exact while every palindrome below p is canonical, which is the case Theorem 7.1 needs. Carried to all representatives it is a DEAD END, owned by the non-canonical palindromes below the cut: at n = 4 and p = 1011 it gives 8 against the true 7, and at n = 20 it fails on 130,816 canonical words. π_{c} repairs every one. [[RUNS independently]] The palindrome count needs no search: π(p) = u + [B(u) < p], with u the first ⌈n/2⌉ bits of p and B(u) its palindrome.');
THM('Theorem 7.3 (Δ in closed form).', 'For even n = 2h and p = AH + B,', { keepNext: true });
EQ('Δ(p) = A(H − A) + B − 2ℛ_{h}(B, A) − [J_{h}(A) < B];');
P('for odd n = 2h + 1 and p = (2A + b)H + B, with b the middle bit,', { keepNext: true });
EQ('Δ(p) = 2A(H − A) + b(H − 1 − 2A) + B − 2ℛ_{h}(B, A) − [J_{h}(A) < B].');
P('The rectangle count ℛ_{h}(u, v) = #{b′ < u : J_{h}(b′) < v} is itself a sum of h ceilings. Reading the bits u_{j} of u from the top, with ρ_{0} = 0 and ρ_{j+1} = ρ_{j} + u_{j}2^{j},', { keepNext: true });
EQ('ℛ_{h}(u, v) = Σ_{j=0}^{h−1} u_{j} ⌈(v − ρ_{j}) / 2^{j+1}⌉,    ℛ_{h}(H, v) = v.');
P('[[proved; SEALED, RUNS: every threshold n = 2..20 and 90 scalar queries to width 1,024 independently; every threshold n = 2..14 here]]');
PROOF('In a complete row of left half A, H − 1 − A words lie below their reverse, A lie above, and one equals it, so the row sums to H − 1 − 2A and the complete rows to A(H − A); at odd width each row appears once for each middle bit. In the partial row, the words below p whose reversed right half falls below A are the ones ℛ counts, and the indicator removes the palindrome. Each set bit u_{j} opens one dyadic block of b′ that share the first j bits of u and have a 0 at place j; reversal turns the block’s free suffix into an arithmetic progression of step 2^{j+1} starting at ρ_{j}, which the ceiling counts. ∎');
FIG('figs/fig3_cut.png', '**Figure 3.** Left: Δ(p) at n = 12 (blue) lies on its coarse term A(H − A) (orange), never more than H away. Right: inside one row (A = 21), Δ climbs by the comparator’s steps c(x) = ±1, and the row’s net climb is H − 1 − 2A = 21.');
P('The coarse term A(H − A) is the fold count of the complete rows, and the rectangle term carries the fine placement. What a reader at the cut p must hold, the number of reversal relations crossing it, is computed by a borrow chain cell by cell. In an adder, what crosses a positional cut is the carry; here, what crosses a value cut is Δ, and the same cell produces it. The cut-law series and this ring meet in one gate.');

// ---------------------------------------------------------------- 8
H1('8. The spectra');
P('The comparison generates the address, so its waveform must have a closed spectrum, and two symmetries fix its support before any transform is taken: c(J(x)) = −c(x) and c(C(x)) = −c(x). The second forces odd degree.');
THM('Theorem 8.1 (the comparator spectrum).', 'With χ(b) = (−1)^{b},', { keepNext: true });
EQ('c(x) = Σ_{j=0}^{h−1} 2^{−j−1} (χ(x_{j}) − χ(x_{n−1−j})) Π_{k<j} (1 + χ(x_{k}) χ(x_{n−1−k})).');
P('Its Walsh support is exactly 2(2^{h} − 1) modes: one singleton on a pair j, any set of complete pairs outside j, and nothing inside. The coefficient W[c] is +N/2^{j+1} for the singleton on the high side of pair j and −N/2^{j+1} for the low side, and 2·C(h, k + 1) modes have degree 2k + 1; the middle bit never appears. [[proved; SEALED, RUNS: every mode n = 2..20 independently; n = 2..14 here]]');
P('In lifted coordinates the expansion is a sentence. (1 + χχ)/2 is [δ_{k} = 0], and (χ(x_{j}) − χ(x_{n−1−j}))/2 is ±[δ_{j} = 1] with the sign of the orientation. The comparison is “every outer pair agrees, pair j disagrees, read its orientation”, summed over j, and a deeper deciding pair weighs less because every pair outside it must agree.');
THM('Theorem 8.2 (the spectrum of the address waveform).', 'Δ is the prefix sum of c, and prefix summation acts on Walsh modes by a sparse kernel. For s ≠ 0 with lowest set bit j, writing e_{k} for the mode of the integer bit of weight 2^{k},', { keepNext: true });
EQ('W[Δ](s) = −½ W[c](s)   (|s| odd),');
EQ('2 W[Δ](s) = −2^{j} W[c](s ⊕ e_{j}) + Σ_{k<j} 2^{k} W[c](s ⊕ e_{k})   (|s| even),');
P('and the zero mode is', { keepNext: true });
EQ('W[Δ](0) = N(N − 1)/6 − hN/4  (n even),    N(N − 2)/6 − hN/4  (n odd),');
P('equivalently N(4N − 3n − 4 − (n mod 2))/24; at n = 20 it is 183,249,141,760. [[proved; SEALED, RUNS: every coefficient n = 2..20 and every kernel entry n = 2..8 independently; every mode n = 2..14 here]] A first shortcut that toggled only the lowest bit was a DEAD END: it omits the e_{j} term and every lower correction.');
P('So the whole spectrum of the address waveform is the comparator’s sparse spectrum carried by one fixed kernel. On the n-bit range Δ(N − 1 − p) = Δ(p) + c(p), so the complement-odd part of Δ is exactly −c/2. These spectra are over the bits of the word’s value; the spectra over ring addresses are reached through the placement of Section 6.');

// ---------------------------------------------------------------- 9
H1('9. The body');
P('The last hole was the shape of the Walsh-even body, at its two ends and between them. The first statement put a logarithmic cusp at the seam and a smooth closure at θ = ±π. Both were derived and sealed before they were run, and the runs corrected both.');
THM('Theorem 9.1 (the closure).', 'For 0 ≤ i < H, R_{n}[i] = i, so z(i) = wt(i) − n/2; by reflection, z(N − 1 − i) = z(i) for 1 ≤ i < H. [[proved; SEALED, RUNS: n = 4..20, both ends]]');
PROOF('For 0 < x < H the first h bits of J(x) are nonzero, so J(x) > x; and 0 is the canonical palindrome. ∎');
P('The closure is the digit sum of the address. Smooth closure is a DEAD END. Next to the closure the even body has z_{+}(0) = 0 and z_{+}(1) = 1 − n/2: a normalized jump of 1 − 2/n across one angular slot of 2π/2^{n}, so no family of interpolants that keeps every sample has a uniform Lipschitz bound there. [[RUNS independently]] A smoothed or punctured profile is a different reader, and it is OPEN.');
THM('Theorem 9.2 (the seam).', 'In block K, 1 ≤ K < H/2, order the labels r = 0, …, K − 1 by increasing h-bit reversal and let r_{i} be the i-th. For even n the canonical word at depth q = K(K − 1)/2 + i from the seam is (H − 1 − K)H + (H − 1 − J_{h}(r_{i})), and on both faces its distance below the north pole is', { keepNext: true });
EQ('n/2 − z_{+} = wt(K) + wt(r_{i});');
P('for odd n, at depth q = K(K − 1) + (1 − b)K + i with middle bit b, it is wt(K) + wt(r_{i}) + 1 − b. [[proved; SEALED, RUNS: every block and both faces, n = 4..18 here; to width 20 and scalar to width 1,025 independently]]');
P('The seam is a digital staircase. Its envelope is logarithmic, wt(K) + wt(r) ≤ 2·bitlength(K) − 1 at even width, and its block mean is wt(K) + (1/K)·Σ_{r<K} wt(r), about wt(K) + ½ log_{2} K. But at every K = 2^{t} the first label is r = 0 and the distance returns to exactly 1, at arbitrarily large depth. [[proved; RUNS]] So “a logarithmic cusp” is right for the envelope and the block means and wrong pointwise; the correction is logged. The two- and three-zero cores of Theorem C hold under its parity hypothesis, s and L of opposite parity, and a dyadic depth alone does not suffice: at n = 10 the depth 64 = 2^{6} has the parity of 10, and its word 1110000101 has five zeros.');
FIG('figs/fig5_seam.png', '**Figure 4.** The seam at n = 16: the distance below the north pole at every depth (grey), its block means (blue) and the envelope 2·bitlength(K) − 1 (orange). At every K = 2^{t} the staircase returns to 1 (aqua). The profile depends on n only through its parity: at a fixed depth, ring n + 2 adds a 1 at each end of the word.');
P('The block sums close as well. For K < H/2 the zeros over block K total μ[K·wt(K) + g·2^{g−1} + Σ_{k: v_k = 1} 2^{g−1−k}(1 + o_{k} + (g − 1 − k)/2)] + (μ − 1)K, with K = 2^{g} + v, o_{k} the ones of v above place k, and μ = 1 or 2 by the parity of n. [[SEALED, RUNS: n = 4..20]] Where palindromes enter, K ≥ H/2, the block holds μ(K + 1): one extra label, r = K, which is the palindrome. The term max(0, K − H/2) in D_{K} counts exactly these palindromes, which is why the offsets of Theorem 3 needed it. [[SEALED, RUNS: 3,049 blocks including 1,534 with palindromes, independently]] At a fixed depth the word of ring n + 2 is the word of ring n with a 1 at each end and the same distance below the pole: the pad law at the level of the waveform. [[RUNS: n = 4..16]]');
THM('Theorem 9.3 (the whole body).', 'Let a_{i} be the canonical member of the pair at address i. Then', { keepNext: true });
EQ('z_{+}(i) = [a_{i} ≠ J(a_{i})]·(wt(a_{i}) − n/2),');
P('and a_{i} is read from i by inverting Theorem 1 block by block: K from one integer square root of the depth, the label from at most h binary residue decisions, the word from its halves. [[proved; SEALED, RUNS: every position n = 2..20 and scalar returns to width 1,024, independently]]');
P('The body is one centred digit sum read through the Δ reader and masked at the palindromes. The closure and the seam are its two ends: the digit sum of the address at one end, the digit sum of the block index at the other, and between them the square root of Lemma A’s triangle.');

// ---------------------------------------------------------------- 10
H1('10. Pulling back: what the structure becomes');
P('Hold the sections at once and every result is a statement about one lifted word read by two readers.');
THM('Proposition 10.1 (the lift carries everything).', 'In the coordinates (v_{j}, δ_{j}):', { keepNext: true });
ITEM('(a) The partner preserves δ. If δ ≠ 0 it flips v_{j} exactly on the disagreeing pairs; if δ = 0 it flips every value and the middle bit. Reversal acts on the difference half and complement on the value half: P is the rule “reverse the differences if there are any, otherwise complement the values”.');
ITEM('(b) The comparison reads only the difference half: c(x) = 0 when δ = 0, and otherwise c(x) = +1 when the outermost disagreeing pair has value 0 and −1 when it has value 1. On the route, c(x) = [δ ≠ 0](1 − 2ε).');
ITEM('(c) The latitude reads only the value half (Proposition 5.1).');
ITEM('(d) The two readers are orthogonal over words: Σ_{x} f(wt(x))·c(x) = 0 for every f, because the weight is J-even and the comparison J-odd.');
P('[[proved; SEALED, RUNS: every word n = 2..18]]');
P('The value reader is the sphere’s height: latitude, the carrier, the poles. The difference reader is the ring’s order: the comparison, the representatives, Δ, the address, the borrow gate. The palindromes are the words on which the difference reader reads nothing.');
THM('Theorem 10.2 (the ring makes the comparison one bit).', 'On addresses, c_{R}(i) = c(R_{n}[i]) is', { keepNext: true });
EQ('c_{R}(i) = χ_{top}(i) · (1 − pal(i) − 2[i ∈ {M − 1, M}]),');
P('where χ_{top}(i) = (−1)^{top address bit} and pal marks the palindromes. Its coefficient on χ_{top} is N − 2^{⌈n/2⌉} − 4 and its energy N − 2^{⌈n/2⌉}, so that single mode carries (N − 2^{⌈n/2⌉} − 4)² / (N(N − 2^{⌈n/2⌉})) of the energy: 98.2% at n = 12 and 99.9% at n = 20, tending to 1. [[proved; SEALED, RUNS: n = 2..20]]');
PROOF('Representatives fill the left face, with c = +1 or 0 at a canonical palindrome; partners fill the right, with c = −1 or 0; the seam swap exchanges one of each. ∎');
P('The proof is the construction, and that is the content. The ring is the coordinate system built so that the comparison of a word with its reverse is its top address bit. What the comparison needs 2(2^{h} − 1) Walsh modes to say over the bits of a word, the ring says with one. The complexity did not vanish. It moved into the change of coordinates, and the change of coordinates is Theorem 1: the comparison counted across a value cut.');
FIG5('figs/fig4_two_readers.png', '**Figure 5.** Two readers, two coordinate systems, n = 12. Top: the comparison has 126 Walsh modes over the bits of the word and collapses onto one mode, with 98.2% of its energy, over ring addresses. Bottom: the latitude has 12 equal modes over the word and 3,808 over ring addresses. Each reader is simple in its own coordinates and spread in the other’s. The dust under the single comparator mode is the palindrome mask, where the comparison is silent.');
TABLE([1100, 2065, 2065, 2065, 2065], [
  ['n', 'latitude, word', 'comparison, word', 'latitude, ring', 'comparison, ring'],
  ['8', '8 (8.0)', '30 (6.2)', '211 (9.5)', '100 (1.22)'],
  ['12', '12 (12.0)', '126 (6.8)', '3,808 (14.2)', '1,787 (1.04)'],
  ['16', '16 (16.0)', '510 (6.9)', '63,806 (22.8)', '30,444 (1.01)'],
  ['20', '20 (20.0)', '2,046 (7.0)', '1,036,432 (34.6)', '505,764 (1.00)']],
  { center: [0, 1, 2, 3, 4], caption: '**Table 2.** Nonzero Walsh modes of each reader in each coordinate system, and in brackets the effective number of modes, the participation ratio (Σ W²)² / Σ W⁴. [[computed]]' });
P('The trade is proved for the comparison and measured for the latitude. In ring coordinates the latitude’s support fills almost every mode, but its energy stays in a few dozen effective ones and moves outward in degree as n grows: degree 2 holds 47% at n = 12 and 33% at n = 20, and degree 1, which only the carrier can reach, holds almost none, 0.036% and 8·10^{−7}. [[computed]] A closed form for that side of the trade is the item it leaves open.');
P('Three earlier pieces are the same path at other locations.');
P('**The butterfly.** The step (u, v) ↦ (u, u ⊕ v) of the Möbius transform on the Boolean lattice, applied across the mirror, is what *Only Addressable* meant by keeping the value beside the difference, what the route records one pair at a time, and what Proposition 10.1 reads.');
P('**The facing law.** Over words P is conditional: reverse, or complement when there is nothing to reverse. Over ring addresses it is one unconditional operation, the complement of the address, whose Walsh eigenvalue is (−1)^{|s|}. The facing law R_{n}[N − 1 − i] = P(R_{n}[i]) is the ring diagonalizing P; Theorem 6 and the energy law are that eigenvalue read on the latitude.');
P('**The carry.** Δ(p) is what a reader at the value cut p must hold; its increments are borrows, and the borrow cell is the adder’s carry with one input complemented.');
P('And the palindromes. They carry no comparison of their own, so they are placed by the comparisons of all the other words (Theorem 7.1). They are linear in their own coordinates and take every higher odd degree from that placement. They own the poles, and they are where the partner turns from a reflection into a half-turn. The words without a difference are located by the differences of everything else.');
P('That is what the structure became. The ring of all binary words is the coordinate system of one comparison. Its address is the comparison counted across a value cut, its sphere is the other half of the same lift, and its waveform is the comparison’s involution read as parity.');

// ---------------------------------------------------------------- 11 ledger
H1('11. Ledger');
TABLE([4700, 2060, 2600], [
  ['Statement', 'Status', 'Scope'],
  ['P involution, ring layout, facing law; Lemma A, Theorems C, D, E', 'STANDS', '*Only Addressable*'],
  ['Proposition 2: Δ is the number of pairs the cut separates', 'proved; RUNS', 'every threshold, n = 2..14'],
  ['Theorem 1: the address at every threshold', 'proved; SEALED, RUNS', 'n = 2..20 indep.; to width 1,024; π at 64 bits'],
  ['Theorem 3: even to odd, offsets D_{K}, S_{K}', 'proved; RUNS', 'L = 4..16; to width 19 indep.'],
  ['E/G partition; branch bit d = outer difference', 'proved; RUNS', 'L = 2..14; to width 20 indep.'],
  ['Four-family table', 'RUNS', 'same partition, stored label'],
  ['Theorem 4: the route is the mirror lift', 'proved; SEALED, RUNS', 'every word, n = 2..18'],
  ['Route to rank to address, and back', 'RUNS', '8,188 words, two implementations'],
  ['Theorem 5: reflection; X-axis half-turn; no azimuthal half-turn', 'proved; RUNS', 'n = 2..20, 228 bands'],
  ['Latitude walk along the route', 'RUNS', '699,048 outputs indep.'],
  ['Proposition 5.1: latitude bound, poles, census', 'proved; SEALED, RUNS', 'every word, n = 2..18'],
  ['Theorem 6 and Corollary 6.1: parity transport, energy law', 'proved; SEALED, RUNS', 'exact, n = 2..20'],
  ['Carrier: counting order, linear in its own coordinates, transport, n = 5 majority', 'proved; RUNS', 'n = 2..20'],
  ['Literal half-width order copy', 'DEAD END', 'owned by the counting order'],
  ['Theorems 7.1 and 7.2: palindrome address, borrow gate', 'proved; SEALED, RUNS', 'n = 2..20; n = 2..16'],
  ['½(p + π + Δ) for every representative', 'DEAD END', 'owned by non-canonical palindromes'],
  ['Theorem 7.3: closed Δ, rectangle digit sum', 'proved; SEALED, RUNS', 'n = 2..20; scalar to 1,024'],
  ['Theorems 8.1 and 8.2: comparator and Δ spectra, zero mode', 'proved; SEALED, RUNS', 'every mode, n = 2..20'],
  ['Lowest-bit toggle for even Δ modes', 'DEAD END', 'omits the e_{j} and lower terms'],
  ['Theorem 9.1: the closure is the address digit sum', 'proved; SEALED, RUNS', 'n = 4..20'],
  ['Smooth closure of the exact body', 'DEAD END', 'jump 1 − 2/n in one slot'],
  ['Theorem 9.2: seam staircase, envelope, returns', 'proved; SEALED, RUNS', 'n = 4..18; to 20 indep.'],
  ['Block sums, palindrome blocks, radius invariance', 'SEALED, RUNS', '3,049 blocks indep.'],
  ['Theorem 9.3: the whole body', 'proved; SEALED, RUNS', 'every position, n = 2..20 indep.'],
  ['Proposition 10.1: the lift carries everything', 'proved; SEALED, RUNS', 'every word, n = 2..18'],
  ['Theorem 10.2: the comparison is one address bit', 'proved; SEALED, RUNS', 'n = 2..20'],
  ['The trade for the latitude (Table 2)', 'computed', 'n ≤ 20'],
  ['Physical spin, physical sphere', 'PULL', ''],
  ['Route codes of hash digests', 'DEAD END; parked', 'the codec owns them'],
  ['Regularity of the profile language', 'OPEN', 'at least 312 states'],
  ['Every component of A(q_{D}) as a union over blocks', 'OPEN', ''],
  ['Closed form of the latitude in ring coordinates', 'OPEN', 'Table 2'],
  ['A smoothed or punctured body profile', 'OPEN', '']],
  { size: 17 });
BOX([
  '**Corrections logged on the way**',
  '**Reflection, not half-turn.** The first statement called the partner an azimuthal half-turn and its palindrome action an antipode. It is a reflection, and on palindromes a half-turn about the X-axis; the azimuthal half-turn is impossible at every width (Theorem 5).',
  '**Basis states, not the spin sector.** C(n, w) counts weight-w words; the symmetric sector has dimension n + 1.',
  '**Digit sum, not smooth.** The closure was stated smooth. It is the digit sum of the address (Theorem 9.1).',
  '**Envelope, not cusp.** The seam was stated a logarithmic cusp. It is a staircase under a logarithmic envelope that returns to 1 at every K = 2^{t} (Theorem 9.2).',
  '**Counting order, not the smaller ring’s order.** The palindromes do not copy the half-width ring’s order; they count.',
  '**Canonical palindromes only.** ½(p + π + Δ) does not extend to every representative; π_{c} does (Theorem 1).',
  '**The whole kernel.** A lowest-bit toggle does not give the even Δ modes; the kernel does (Theorem 8.2).',
  '**The parity hypothesis.** Two or three zeros at dyadic depths need the parity condition of Theorem C; depth 64 at n = 10 has five.',
  '**Degree one is not empty.** A first reading of the latitude in ring coordinates put no energy in degree 1. The carrier puts a little there: 0.036% at n = 12.',
  '**Seal bytes.** One independent prediction’s digest matched its text without the final newline. Both digests are recorded in Appendix A, and every later seal hashes literal bytes.']);

H2('What this paper does not claim');
P('Everything here is one finite construction and what its readers return. The sphere is coordinate geometry; nothing is claimed about physical spin, a physical field or a physical sphere, and those readings are PULL. Theorem 1 locates words in a bijection with an exact inverse, so nothing here bears on the preimage or collision resistance of any hash function. Route codes of hash digests belong to the codec that relabels them, a DEAD END for that question, which is parked. Table 2 measures the latitude to n = 20; the comparison’s side of the trade, Theorem 10.2, is proved at every width.');
H2('The next stroke');
P('Three routes are ready. The profile language of *Only Addressable* (311 classes at depth 11, at least 312 states) needs a distinguishability proof, since automaton growth alone cannot settle regularity; every seam block, with its reversal-ordered labels and its palindrome label, is now in closed form, and that is the material such a proof is built from. The full sets A(q_{D}) can be written as unions over those blocks. And the other side of the trade: the comparison is one bit in ring coordinates, while the latitude there is fixed by Theorems 1, 6 and 9.3 but has no closed spectrum yet.');
H2('Conclusion');
P('*Only Addressable* built the ring of all binary words from a pairing. Here it is built from a comparison. Each word is compared with its own reverse, and the comparison is decided by the outermost pair of bits that differ. Its running count across a value cut is the address, closed in a few ceilings and incremented by the adder’s carry cell with one input complemented. The pairs that agree carry the weight, and with it a sphere on which the partner is a reflection, the poles belong to the palindromes, and the latitude splits by Walsh parity into a body and a carrier with energy share 2^{1−n/2}. Each of the two readers is simple where the other is spread, and the ring is the coordinate system in which the comparison is one bit. None of that was put in. It came out of holding the end and reading each hole for what had to be there.');
P('**Acknowledgment.** Computation and drafting were done with Claude (Anthropic) as a working partner. Several results here were first reached or checked in independent AI-assisted runs, each recorded with its seals in the running log: the two-branch and four-family lifts, the route–rank–address closure, the reflection covariance and pole profiles, the half-width placement and its transport, the closed Δ and the comparator spectrum, the Δ kernel and zero mode, the seam profile and the interior reader. Every number quoted was recomputed for this paper by the scripts of Appendix B.', { size: 19 });

H1('References');
for (const r of [
  'Kulik, D. A. (2026). *Only Addressable: The ring of all binary words — exact location without enumeration, a triangular top, and a law in thirds for what one ray reads.* QuHarmonics Research Group.',
  'Kulik, D. A. (2026). *Decompiling Addressable Binary Rings: Forced involutions, the Möbius difference bridge, and radial witness topologies.* QuHarmonics Research Group.',
  'Kulik, D. A. (2026). *I Need That: The way home in a finite scope, and how a reader turns a search into a route.* QuHarmonics Research Group.',
  'Kulik, D. A. (2026). *Two Quotients of One Machine*; *What a Cut Must Do to Make a Thing*; *Carry Capacity and the Conditional Cut Law.* QuHarmonics Research Group.',
  'Kulik, D. A. (2026). Compiler rings running log, §0–§12 (compiler_rings_log.md), 20 October 2026. QuHarmonics Research Group.',
  'Knuth, D. E. (2011). *The Art of Computer Programming, Vol. 4A: Combinatorial Algorithms, Part 1.* Addison-Wesley.',
  'Myhill, J. (1957). Finite automata and the representation of events. WADD Technical Report 57-624, Wright-Patterson Air Force Base.',
  'Nerode, A. (1958). Linear automaton transformations. *Proceedings of the American Mathematical Society*, 9(4), 541–544.',
  'Rota, G.-C. (1964). On the foundations of combinatorial theory I: Theory of Möbius functions. *Zeitschrift für Wahrscheinlichkeitstheorie und verwandte Gebiete*, 2, 340–368.',
  'Walsh, J. L. (1923). A closed set of normal orthogonal functions. *American Journal of Mathematics*, 45(1), 5–24.'])
  P(r, { size: 19, indent: { left: 360, hanging: 360 }, align: AlignmentType.LEFT, spacing: sp(0, 80) });

// ---------------------------------------------------------------- Appendix A
PAGEBREAK();
H1('Appendix A. Sealed predictions');
P('Each prediction below was written, with the reading it predicts and the readout it returns through, and its text hashed before the code that tests it was run. The runner of each recomputes the digest and stops if it does not match. Digests are SHA-256 of the literal file bytes unless stated.');
TABLE([2700, 4160, 2500], [
  ['Prediction', 'SHA-256', 'Result'],
  ['Walsh parity split and energy law (Theorem 6, Corollary 6.1)', 'be9c190152f9d9e0f0cade476691f24aa0153ef9af083dd41e0b30b8fbfa652c', 'RUNS, exact, n = 2..20'],
  ['Palindrome address and borrow gate (Theorems 7.1, 7.2)', '5910642ece837f543f4d363abd5f1951f13c06758be3612dd8e6015712438bfb', 'RUNS, n = 2..20 and 2..16'],
  ['Closure and seam block sums (Theorem 9.1, §9)', '947b3f56802f0cb601cea3fad19cd8fd7075518fe16737f316665105cbe59adb', 'RUNS, n = 4..20'],
  ['What the structure becomes (Theorems 1 at 64 bits, 4; Propositions 5.1, 10.1; Theorems 6, 10.2)', '359b4d3e9e043262928226047a9bed3feb0122a7b5c672464c11909bcd1584bd', 'RUNS, all six parts'],
  ['Comparator imbalance and spectrum (Theorems 7.3, 8.1), independent; text without final newline', '21895d2da4a74d2338d00cfb5e79754ac42091a26262cfb14a5195cae221e0de (literal file c560fad25fe397675b789d10a357ed5fba0320804d62284f1b9a972e4422e393)', 'RUNS; source 5d5583fa…fe86be66'],
  ['Seam profile pointwise (Theorem 9.2), independent', '5ba90e6fdcf1456bcf5033e85f4e43408680f0b406675fdb743d722c3b550219', 'RUNS; source 90f5a9e7…50268317'],
  ['Interior rank and whole body (Theorems 1, 9.3), independent, final', '5cde4126a76c415bd4397164cf1b09b1a07fcdb82f40e140fd539a9f065757a1', 'RUNS; source 756fb657…0b030977'],
  ['Interior rank and block sums, independent, second run', '358e76d2a5d17527d820b78ea0a16baef992e6edf7fb9379ff5bc88aaa0e554a', 'RUNS; source 215b2a8b…5384ac47'],
  ['Δ kernel, nonzero and zero modes (Theorem 8.2), independent', '2f7d21a88107b4147843d550cdd0689f22e197b5760a0fe1050787631fee01c7', 'RUNS; source 982f6838…251bebc2'],
  ['Δ full spectrum and zero mode, independent, second run', 'f3275b7b05c81590907b35f50d7d03843edbb149cfd638b28ef3964646bfa61d', 'RUNS; source 8c866820…821bf7ee'],
  ['Two-branch lift (E/G), independent; source hashed before run', 'ab543c247d2adcfaad114cf45a023697396fac5bb0fd0dc52a573da0b39a7fb0', 'RUNS, to width 20'],
  ['Route–rank and reflection–lift audits, independent; sources', 'ee827844ba91d592c81cb1f6f22f42dc0a2ea97820a3d532e199d6e30803020b; 4277c3f1b18df45ab669f00f75e33596458216d31573983dcec1e2269e607d8f', 'RUNS']],
  { mono: [1], size: 16 });
P('The full text of the sealed prediction for Section 10, as hashed; long lines are wrapped for print, and a wrapped continuation is indented.', { keepNext: true });
MONOLINES(fs.readFileSync('seal_pullback.txt', 'utf8').replace(/\n$/, '').split('\n').flatMap(l => wrap(l, 98)), 14);
P('The other three session seals are reproduced in the companion bundle (seals/), each beside the script that verifies it.');

// ---------------------------------------------------------------- Appendix B
H1('Appendix B. Scripts and their output');
P('paper_checks.py rebuilds every ring from the closed form and rechecks every identity the paper states, in exact integer and rational arithmetic; pullback_run.py verifies the Section 10 seal and runs its six parts; trade_measure.py measures Table 2; figures.py draws the figures. The session scripts walsh_split.py, address_comparator.py and seam_closure.py verify the three earlier seals. Their output follows, unedited.');
MONOLINES(fs.readFileSync('paper_checks_output.txt', 'utf8').replace(/\n$/, '').split('\n').flatMap(l => wrap(l, 98)), 14);
MONOLINES(fs.readFileSync('pullback_output.txt', 'utf8').split('\n').filter(l => /^(seal verified|PB\d|all PB)|n=18|n=20|pi, 64|closed rank|closed position/.test(l)).flatMap(l => wrap(l, 98)), 14);

function wrap(line, width) {
  if (line.length <= width) return [line];
  const out = []; let s = line;
  while (s.length > width) { let k = s.lastIndexOf(' ', width); if (k < 40) k = width; out.push(s.slice(0, k)); s = '    ' + s.slice(k).trimStart(); }
  out.push(s); return out;
}

// ======================================================================= DOCUMENT
const footer = new Footer({ children: [
  new Paragraph({ children: [new TextRun({ text: 'Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828 · Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)', font: BODY, size: 14, color: MUTED })], alignment: AlignmentType.CENTER, spacing: { before: 0, after: 0 } }),
  new Paragraph({ children: [new TextRun({ text: 'github.com/QuHarmonics/The-Nexus-Harmonic-Reality · info@quharmonics.com · Page | ', font: BODY, size: 14, color: MUTED }), new TextRun({ children: [PageNumber.CURRENT], font: BODY, size: 14, color: MUTED })], alignment: AlignmentType.CENTER, spacing: { before: 0, after: 0 } })] });
const header = new Header({ children: [new Paragraph({ children: [new TextRun({ text: 'Against Its Own Reverse · Kulik 2026', font: BODY, size: 15, color: MUTED })], alignment: AlignmentType.RIGHT })] });

const doc = new Document({
  creator: 'Dean A. Kulik', title: 'Against Its Own Reverse', description: 'QuHarmonics Research Group, October 2026',
  styles: { default: { document: { run: { font: BODY, size: 21, color: INK } } },
    paragraphStyles: [
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: BODY, size: 26, bold: true, color: INK }, paragraph: { spacing: { before: 320, after: 140 }, outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: BODY, size: 22, bold: true, color: INK }, paragraph: { spacing: { before: 220, after: 100 }, outlineLevel: 1 } }] },
  sections: [{ properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, bottom: 1300, left: 1440, right: 1440, header: 600, footer: 500 } } },
    headers: { default: header }, footers: { default: footer }, children: blocks }]
});
Packer.toBuffer(doc).then(buf => { fs.writeFileSync('Against_Its_Own_Reverse.docx', buf); console.log('wrote Against_Its_Own_Reverse.docx', buf.length, 'bytes'); });
