// build_map.js — "Mapping the Nested Partner Ring" (Dean A. Kulik, QuHarmonics Research Group)
const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, ImageRun, Table, TableRow, TableCell,
        WidthType, BorderStyle, ShadingType, Footer, Header, PageNumber, PageBreak } = require('docx');

const BODY = 'Cambria', MATH = 'Cambria Math', MONO = 'Consolas';
const INK = '0B0B0B', INK2 = '52514E', MUTED = '898781', RULE = 'C3C2B7';
const W = 9360;
const TITLE = 'Mapping the Nested Partner Ring';

// inline markup: **bold** *italic* ^{sup} _{sub} [[status]]
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
function H1(text) { blocks.push(new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text, bold: true, font: BODY, size: 26, color: INK })], spacing: { before: 320, after: 140 }, keepNext: true })); }
function H2(text) { blocks.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text, bold: true, font: BODY, size: 22, color: INK })], spacing: { before: 220, after: 100 }, keepNext: true })); }
function EQ(text) {
  blocks.push(new Paragraph({ children: runs(text, { font: MATH, size: 22 }), alignment: AlignmentType.CENTER, spacing: { before: 80, after: 140, line: 276 } }));
}
function THM(label, text, o = {}) {
  blocks.push(new Paragraph({ children: [new TextRun({ text: label + ' ', bold: true, font: BODY, size: 21, color: INK }), ...runs(text)],
    alignment: AlignmentType.JUSTIFIED, spacing: sp(60, 120), keepNext: o.keepNext }));
}
function PROOF(text, first = true) {
  const kids = first ? [new TextRun({ text: 'Proof. ', italics: true, font: BODY, size: 21, color: INK }), ...runs(text)] : runs(text);
  blocks.push(new Paragraph({ children: kids, alignment: AlignmentType.JUSTIFIED, spacing: sp(0, 120) }));
}
function pngSize(file) { const b = fs.readFileSync(file); return [b.readUInt32BE(16), b.readUInt32BE(20)]; }
function FIG(file, caption, widthPx = 620) {
  const [w, h] = pngSize(file);
  blocks.push(new Paragraph({ children: [new ImageRun({ type: 'png', data: fs.readFileSync(file), transformation: { width: widthPx, height: Math.round(widthPx * h / w) } })],
    alignment: AlignmentType.CENTER, spacing: { before: 160, after: 60 }, keepNext: true }));
  blocks.push(new Paragraph({ children: runs(caption, { size: 18, color: INK2 }), alignment: AlignmentType.JUSTIFIED, spacing: { before: 0, after: 220, line: 252 } }));
}
const hair = { style: BorderStyle.SINGLE, size: 4, color: RULE };
const none = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
function TABLE(widths, rows, o = {}) {
  const sum = widths.reduce((a, b) => a + b, 0);
  const trs = rows.map((row, ri) => new TableRow({ tableHeader: ri === 0, cantSplit: true,
    children: row.map((cell, ci) => new TableCell({
      width: { size: widths[ci], type: WidthType.DXA },
      shading: ri === 0 ? { type: ShadingType.CLEAR, fill: 'F0EFEC', color: 'auto' } : undefined,
      margins: { top: 50, bottom: 50, left: 90, right: 90 },
      children: [new Paragraph({ children: runs(cell, { size: o.size || 17, bold: ri === 0, font: (o.mono || []).includes(ci) && ri > 0 ? MONO : BODY }),
        alignment: (o.center || []).includes(ci) ? AlignmentType.CENTER : AlignmentType.LEFT, spacing: { before: 0, after: 0, line: 240 } })] })) }));
  if (o.title) blocks.push(new Paragraph({ children: runs(o.title, { size: 18, color: INK2, bold: true }), alignment: AlignmentType.LEFT, spacing: { before: 120, after: 60 }, keepNext: true }));
  blocks.push(new Table({ width: { size: sum, type: WidthType.DXA }, columnWidths: widths, rows: trs,
    borders: { top: hair, bottom: hair, left: none, right: none, insideHorizontal: hair, insideVertical: none } }));
  if (o.caption) blocks.push(new Paragraph({ children: runs(o.caption, { size: 18, color: INK2 }), alignment: AlignmentType.JUSTIFIED, spacing: { before: 80, after: 220, line: 252 } }));
  else blocks.push(new Paragraph({ children: [], spacing: { before: 0, after: 120 } }));
}
function MONOLINES(lines, size = 15) {
  for (const l of lines) blocks.push(new Paragraph({ children: [new TextRun({ text: l.length ? l : ' ', font: MONO, size, color: INK })], spacing: { before: 0, after: 0, line: 228 } }));
  blocks.push(new Paragraph({ children: [], spacing: { before: 0, after: 160 } }));
}
function PAGEBREAK() { blocks.push(new Paragraph({ children: [new PageBreak()] })); }
function wrap(line, width) {
  if (line.length <= width) return [line];
  const out = []; let s = line;
  while (s.length > width) { let k = s.lastIndexOf(' ', width); if (k < 40) k = width; out.push(s.slice(0, k)); s = '    ' + s.slice(k).trimStart(); }
  out.push(s); return out;
}

// ======================================================================= TITLE
blocks.push(new Paragraph({ children: [new TextRun({ text: TITLE, font: BODY, size: 44, bold: true, color: INK })], alignment: AlignmentType.CENTER, spacing: { before: 240, after: 160 } }));
blocks.push(new Paragraph({ children: [new TextRun({ text: 'Reading orders, tape frames and a uniform profile witness', font: BODY, size: 26, italics: true, color: INK2 })], alignment: AlignmentType.CENTER, spacing: { before: 0, after: 300 } }));
blocks.push(new Paragraph({ children: [new TextRun({ text: 'Dean A. Kulik', font: BODY, size: 23, color: INK })], alignment: AlignmentType.CENTER, spacing: { before: 0, after: 60 } }));
blocks.push(new Paragraph({ children: [new TextRun({ text: 'QuHarmonics Research Group · ORCID 0009-0003-3128-8828', font: BODY, size: 18, color: INK2 })], alignment: AlignmentType.CENTER, spacing: { before: 0, after: 60 } }));
blocks.push(new Paragraph({ children: [new TextRun({ text: 'October 2026', font: BODY, size: 20, color: INK2 })], alignment: AlignmentType.CENTER, spacing: { before: 0, after: 360 } }));

H1('Abstract');
P('The nested partner ring R_{n} lists every n-bit word exactly once. Each word is paired with its reversal, or with its complement when it is a palindrome; the smaller member of every pair ascends on one face of the ring, its partner faces it on the other, and the two words at the centre seam are exchanged. Earlier papers in this series made the ring addressable in both directions in O(n) operations and closed its geometry. This paper begins a map of the finished object and settles three questions about reading it.');
P('First, for every output the ring computes, the order in which the bits of a word should arrive so that the output is ready soonest, computed exactly over all n! arrival orders for n up to 19. Reflection decisions are read from the outermost mirror pair inward: the face (n ≥ 6) and the comparator have exactly 2^{h} optimal orders and mean readiness 4 − 5·2^{−h} and 4 − 4·2^{−h} arrivals. The palindrome flag and the partner are read one complete mirror pair at a time, in any order of the pairs. An adder is read along its carry. The ring’s successor map is read along the carry with each position followed by its mirror, in exactly six optimal orders at every width from 8 to 19. The address reads about two thirds of the word from the outside in and the remaining core by value.');
P('Second, every L-bit window of the ring’s bit stream at every bit offset. The number of words a frame misses has a closed form in the number of palindromes, every collision is owned by a palindromic word, and the frame at offset 2 is complete for L ≥ 6 because every palindrome on the partner face begins with 1. Third, one angle that reads the radial profile q_{D} = 1 00 1^{D−5} 00 at every depth D ≥ 13. It closes the residue class D ≡ 2 (mod 3), which earlier work left open, with a single dyadic offset.');

P('**Status words.** A bracket after a statement records how it stands. **proved**: proved here. **STANDS**: established earlier in this series or in the literature. **RUNS**: an exact computation landed where a prediction sealed before the run placed it; the range is stated. **measured**: an exact computation reported without a sealed prediction. **DEAD END**: the computation ran and landed, and the landing belongs to a different structure, which is named. **OPEN**: stated and not settled. Sealed predictions were hashed with SHA-256 before the code that tests them was run; the digests are listed in Appendix A.', { size: 19 });

// ======================================================================= 1
H1('1. Introduction');
P('A finite structure that is already complete leaves one kind of question open: how it is read. The nested partner ring is such a structure. Its address is a count of comparisons between words and their reversals [6], its location and its inverse cost O(n) [1, 2], and its geometry folds into a unit square whose diagonal carries the palindromes [5]. What remains is a map: which coordinates exist, which exact maps join them, and how each output is read. This paper draws the first layer of that map (Section 2) and adds three results to it.');
P('Each result was reached the same way. The finished state is held first; the gap is named by what has to fill it; what the existing structure already accounts for is subtracted; and the remainder is read as a copy of a structure already in the corpus. The prediction is then sealed and run. In Section 3 the held state is an output and the gap is its reading order: an output can be ready only when the chain that decides it has arrived, so the order that makes it ready soonest is the direction of that chain. In Section 4 the held state is the ring’s bit stream: a window that straddles two words differs from a rotated ring word only where a partner is a complement, so every word a window misses is owned by a palindrome. In Section 5 the held state is the profile q_{D}: its last two readings must land on zeros that the rank laws of [3] place, and solving for those two readings fixes the angle.');

// ======================================================================= 2
H1('2. The object and its coordinates');
P('Fix n ≥ 2 and put N = 2^{n}, M = N/2 and h = ⌊n/2⌋. Bit i of a word x is the coefficient of 2^{i}. Mirror pair j is the pair of positions {n−1−j, j}, j = 0, …, h−1; when n is odd the middle position h is unpaired. J reverses the bits of a word and C complements them. The partner is P(x) = J(x) when J(x) ≠ x and P(x) = C(x) when x is a palindrome; P is a fixed-point-free involution [[STANDS [1]]]. The representatives are the words with x < P(x). R_{n} lists them in increasing order in slots 0, …, M − 1, places P(R_{n}[i]) in slot N − 1 − i, and exchanges slots M − 1 and M [[STANDS [1]]]. The slot of x is its address.');
P('The tape T_{n} is R_{n}[0] R_{n}[1] … R_{n}[N − 1], each word written from its most significant bit, read cyclically. The radial reader of an angle u ∈ [0, 1) reads, on ring L, bit ⌊L·{2^{L}u}⌋ of the word R_{L}[⌊2^{L}u⌋], bits counted from the most significant end; the D readings for L = 1, …, D are the profile of u at depth D [[STANDS [2, 3]]].');
TABLE([2050, 2900, 3010, 1400], [
  ['Coordinate', 'What it records', 'Exact map from the word', 'Status'],
  ['value x', 'the word as an integer; the counter’s order', 'identity', 'definition'],
  ['address a', 'the slot on R_{n}', 'rank: palindrome count plus a closed comparator digit sum; inverse: one integer square root and one count per bit; both O(n)', 'STANDS [1, 6]; RUNS to 4096 bits'],
  ['face, depth', 'side of the seam; distance from it', 'a ↦ ([a ≥ M], M − 1 − a or a − M)', 'STANDS'],
  ['folded square', 'front half f; reversed back half J(g)', 'split the word at its centre', 'STANDS [5]'],
  ['mirror lift', 'value and difference of each mirror pair', '(x_{j}, x_{j} ⊕ x_{n−1−j}) per pair', 'STANDS [6]'],
  ['sphere', 'radius n, latitude wt(x) − n/2, azimuth of the address', 'weight and address', 'STANDS [6]'],
  ['route code', 'root, then the middle bit on odd steps and the outer-pair difference on even steps, then the side', 'the two-branch lift, ring L → L+1 → L+2', 'RUNS to width 20 [7]'],
  ['tape offset', 'position iL + s in the bit stream', 'concatenation of R_{L}', 'definition; Section 4'],
  ['radial angle u', 'one bit per ring', 'slice ⌊L{2^{L}u}⌋ of R_{L}[⌊2^{L}u⌋]', 'STANDS [3]; Section 5']],
  { title: 'Table 1. Coordinates of the ring and the exact maps that join them.', caption: 'Three operators act on every coordinate at once. The partner is the address reflection a ↦ N − 1 − a, which complements every address bit. The successor T moves one slot, a ↦ a + 1; in word coordinates it has algebraic degree n − 1 while the partner has degree ⌊n/2⌋, and P T P = T^{−1} [[RUNS, n ≤ 16 [7]]]. The lift joins ring L to rings L + 1 and L + 2 by inserting a middle bit, then an outer pair.' });

// ======================================================================= 3
H1('3. The native reading order of each output');
H2('3.1 Readiness and the exact optimum');
P('Let the bits of a word x arrive one at a time in a fixed arrival order σ, a permutation of the n positions. An output f is ready after t arrivals when every word that agrees with x on the arrived positions has the same value of f. The readiness time of f at x is the least such t; for an output made of several bits it is taken bit by bit and averaged. The cost of σ is the mean readiness time over all 2^{n} words. This is the cost of a non-adaptive sequential evaluation in the sense of decision-tree and sequential-testing theory [9, 10].');
P('The minimum over all n! orders is exact and inexpensive. For every set S of arrived positions the number of words whose output is not ready is obtained by folding the truth table along every unarrived position, which costs 3^{n} operations for all 2^{n} sets together. A dynamic programme over the sets then gives the optimal cost, the exact number of optimal orders, and the orders themselves. Table 2 lists the outcome for every output tested.');
TABLE([2150, 3560, 1150, 1250, 1250], [
  ['Output', 'Optimal orders: the complete set', 'Count', 'Optimum, n = 16', 'Status'],
  ['face [x > P(x)]', 'mirror pairs from the outermost inward, either member first, middle bit last', '2^{h}', '4 − 5·2^{−h} = 3.9805', 'RUNS, n = 6–19'],
  ['comparator sgn(J(x) − x)', 'the same set', '2^{h}', '4 − 4·2^{−h} = 3.9844', 'RUNS, n = 4–16'],
  ['palindrome flag', 'one complete mirror pair at a time, any order of the pairs, either member first, middle last', 'h!·2^{h}', '4 − 4·2^{−h}', 'RUNS, n = 4–16; proved'],
  ['partner P(x)', 'the same set as the palindrome flag', 'h!·2^{h}', '9.1064', 'RUNS, n = 4–19'],
  ['successor T(x)', 'positions 0, 1, n−1 in any order, then n−2, then (2, n−3), (3, n−4), …, low member first, middle last', '6', '9.5179', 'RUNS, n = 8–19'],
  ['address', 'k outer pairs from the outside in, either member first, then every remaining position by value', '2^{k}', '12.7183', 'measured, n ≤ 19'],
  ['decompile: word from address', 'address bits by value, the top three in any order with the top bit not last, one adjacent exchange', '4', '11.0010', 'measured, n ≤ 16'],
  ['8-bit adder', 'a_{j}, b_{j} adjacent in either order, ascending j', '256', '175/18 = 9.7222', 'RUNS, 16! orders'],
  ['any bijection, read whole', 'every order', 'n!', 'n', 'measured']],
  { title: 'Table 2. The native reading order of each output.', caption: 'Positions are bit significances; mirror pair j is {n−1−j, j}. The optimum is the mean number of arrivals until ready, per output bit where the output has several bits; the adder’s optimum is per output over its nine outputs. Counts are exact; the n = 16 counts are 256, 256, 10,321,920, 10,321,920, 6, 32, 4, 256. k is listed in Figure 2.' });

H2('3.2 Reflection is read from above');
P('The face and the comparator are decided at the outermost mirror pair whose two bits differ. Their optimal orders are exactly the 2^{h} orders that read the pairs from the outermost inward, either member first, with the middle bit last, with means 4 − 5·2^{−h} and 4 − 4·2^{−h} [[RUNS: face n = 15–19 on fresh widths, n = 6–14 earlier; comparator n = 4–16]]. The face needs slightly less than the comparator because the face of a palindrome is its top bit, which arrives with the first pair: when every outer pair agrees, the face is known one arrival before the last pair closes. At n = 4 and 5 the face has twelve optimal orders, not four; the excess is owned by the single exceptional pattern of the three bits beside the top bit at h = 2 [7, §22]. Read in value order the same decisions wait to the end: 14.97 arrivals against 3.98 at n = 16.');
H2('3.3 Pair completeness is order-free');
P('The palindrome flag depends on the mirror pairs only through which pairs are complete and whether a complete pair differs. The partner is the reversal or the complement according to that flag, and each of its bits is fixed once its mirror pair is complete and the flag is known. Both are read optimally one complete pair at a time, in any order of the pairs [[RUNS: flag n = 4–16; partner n = 4–19, 185,794,560 optimal orders at n = 18 and 19]].');
THM('Proposition 1.', 'For every n ≥ 2 the least mean readiness of the palindrome flag over all arrival orders is 4 − 4·2^{−h}, and the orders attaining it are exactly the h!·2^{h} orders that complete one mirror pair at a time, with the middle bit last. [[proved]]');
PROOF('After t arrivals let c(t) be the number of complete mirror pairs. The flag is not ready exactly when every complete pair agrees and at least one pair is incomplete, because an incomplete pair can still differ and the middle bit never matters. Pairs agree independently with probability 1/2, so the probability of not being ready after t arrivals is 2^{−c(t)} while c(t) < h and 0 afterwards, and the mean readiness is the sum of these probabilities over t. Since c(t) ≤ ⌊t/2⌋, each term is at least 2^{−⌊t/2⌋}, and the sum of those bounds over t = 0, …, 2h − 1 is 4 − 4·2^{−h}. Equality at every t requires c(t) = ⌊t/2⌋ for all t ≤ 2h, which holds exactly when each pair is completed before the next is begun and the middle bit, if any, comes last. There are h! orders of the pairs and two orders inside each pair. ∎');
H2('3.4 The adder is read along its carry, the successor along both chains');
P('For two 8-bit operands, over all 16! orders of their bits, the optimum is 175/18 arrivals per output, attained by exactly the 256 orders that read a_{j} and b_{j} together in ascending significance [[RUNS]]. Read from the top it costs 11.0022. Sum bit j is ready at arrival 2j + 2, and the final carry is ready at arrival 15 whenever a_{7} equals the incoming carry. The adder’s deciding chain is the carry, which runs from the bottom [8].');
P('The successor map T, which takes the word in slot a to the word in slot a + 1, has exactly six optimal orders at every n = 8–19: positions 0, 1 and n − 1 in any order, then n − 2, then the pairs (2, n − 3), (3, n − 4), … with the low member first, the middle bit last [[RUNS: sealed at n = 17–19, measured at n = 8–16]]. Both chains are present in this order. On the representative face the successor is an increment, whose carry runs up from position 0; the face of the word is decided by the comparator, which runs in from the outer pair. Every low position j is at once a carry position and a member of mirror pair j, and the optimal reader takes each low position and then its mirror.');
H2('3.5 The address is read by two wheels');
P('The address is the comparator count of [6]: its top bit is the face, its upper bits follow the front half of the canonical word, and its lower bits follow the reversed back half. Its optimal reader therefore cannot be a single direction. It takes k outer mirror pairs from the outside in, either member first, and then every remaining position by value; the number of optimal orders is exactly 2^{k} [[measured, n ≤ 19]]. The core is read by value at n = 7 and n = 11–19, except that n = 17 exchanges its last two core positions; at n = 8, 9 and 10 the cores are read in the orders (5, 4, 2, 3), (4, 5, 3) and (6, 5, 3, 4). The outside-in stretch covers about two thirds of the word, k = 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6 at n = 7–19 (k = ⌊n/3⌋ at every listed n except 11). At n = 16 the optimum is 12.7183 arrivals per address bit, against 12.7423 outside-in and 14.8903 in value order.');
P('Two sealed forms of this law failed and are recorded as such. A core of three bits at odd n and four bits at even n is a DEAD END from n = 13: the core widens to five, six and seven bits. The fit k = 2 + ⌊log_{2}(n − 7)⌋ is a DEAD END at n = 18, where k = 6. The owner in both cases is the switch point itself, the width at which resolving the face for half of the remaining words no longer pays for delaying the counter on the core. Its law is OPEN.');
P('The inverse direction, recovering the word while the address arrives, is read by value: the optimal orders take the top three address bits in any order with the top bit not last, and then the rest by value with one adjacent exchange whose place moves with n. Value order itself is optimal at n = 8, 9 and 16 and within 0.03 arrivals per bit at every n from 8 to 16 [[measured; the sealed claim that value order is optimal at every n is a DEAD END]]. Every output that is a bijection of the word, read as a whole, waits for all n arrivals under every order, since its value determines the word; readiness is a property of single output bits.');
FIG('figs/fig2_readers.png', 'Figure 2. Left: the least mean readiness over all n! arrival orders for five outputs (solid), and the cost of value order for the address and the face (dotted). Reflection decisions saturate below four arrivals at every width; the address grows with n but stays well below value order. Right: the optimal address reader, k outer pairs read from the outside in (blue, number of pairs above the bar) followed by the core (orange), which is read by value at n = 7 and 11–19, with the last two core positions exchanged at n = 17.', 600);
H2('3.6 What the table records');
P('Across every output tested, the optimal order is the direction in which the output’s deciding chain runs. The comparator runs in from the outer pair, so reflection is read from above. The palindrome flag and the partner need complete pairs and nothing else, so the order of the pairs is free. The adder’s chain is its carry, so it is read from the bottom. The successor needs the carry and the comparator, and its reader interleaves them. The address is both a reflection count and a value, and its reader changes direction once. The general statement that every output’s native order is the direction of its chain is OPEN; Table 2 is the evidence for it so far.');

// ======================================================================= 4
H1('4. The tape at every offset');
P('Read the tape T_{L} in windows of L bits that start s bits into each word, 0 ≤ s < L. The window that starts in slot i is');
EQ('w_{i}(s) = (R_{L}[i] mod 2^{L−s})·2^{s} + ⌊R_{L}[i + 1] / 2^{L−s}⌋,');
P('the tail of one word followed by the head of the next. Frame s is complete when its N windows are N distinct words; its loss is the number of words it misses. Frames 0 and 1 are complete at every width [7, §20].');
THM('Frame law.', 'With h = ⌊L/2⌋ and P = 2^{⌈L/2⌉}, the number of palindromes of width L, the loss of frame s is 0 for s ≤ 1; P(1 − 2^{2−s}) for 2 ≤ s ≤ h − 1; P − 2 at s = h for even L and P − 6 for odd L; P − 2 − 2^{s−h+1} for h + 1 ≤ s ≤ L − 2; and P − 2 at s = L − 1. [[RUNS: sealed on the cells measured at L = 2–16; all 117 cells of the fresh widths L = 17–22 land]]');
FIG('figs/fig1_frames.png', 'Figure 1. Words missed by each frame, as a fraction of the number of palindromes, for L = 10–22 (points: exact counts; lines: the frame law). The rising branch 1 − 2^{2−s} is the same at every width; the falling branch and the dips at s = h and s = L − 1 depend on L. No frame misses as many words as there are palindromes.', 600);
P('The losses are owned by the twist. Every collision between windows is a pair, and every pair joins one window that starts or ends at a palindrome on the partner face with one window that touches no palindrome. A palindrome window escapes collision exactly when the palindrome begins with 1^{s−1} on the rising branch, or with exactly 1^{L−s−1}0 on the falling branch, the all-ones word escaping on its entry side; at s = h, and at s = h + 1 for odd L, the seam pair adds collisions of its own [[measured: checked at every cell of its domain for L = 6–20]]. Counting the escapes gives the law. There are P/2 palindromes on the partner face, each with two windows, and on the rising branch a fraction 2^{2−s} of them begin with 1^{s−1}, so the loss is 2·(P/2)·(1 − 2^{2−s}).');
THM('Corollary (frame 2).', 'For every L ≥ 6 the frame at offset 2 is complete. Every palindrome on the partner face is the complement of a palindrome with leading bit 0, so it begins with 1; at s = 2 the escape condition reads only that leading bit, and no palindrome window collides. The rising branch, which contains s = 2, exists exactly when h ≥ 3. [[follows from the owner; checked at L = 6–20]]');
P('This replaces an explanation proposed in an earlier exchange, that the zero of the seam word leaves the two-bit prefix clear from L = 6 on [[DEAD END: the seam takes no part in any frame below h]]. The pairing itself, which non-palindromic window each palindrome window meets, is the link that turns the frame law into a theorem; it is OPEN.');

// ======================================================================= 5
H1('5. One angle for every depth');
P('The profile q_{D} = 1 ∥ 00 ∥ 1^{D−5} ∥ 00 is read by the radial reader of [3]. *The Geometry of a Readout* proved a single witness angle for every D ≥ 13 with D ≡ 0 or 1 (mod 3), and a two-offset angle for D = 3m + 2 with m ≥ 8 and m ≡ 0 or 1 (mod 4); the depths D = 3m + 2 with m = 4–7 or m ≡ 2, 3 (mod 4) remained open [3].');
P('Hold the finished profile and read back what it needs. Two rank laws of [3] place the zeros. **Law 4.1**: for odd p ≥ 5, t = (p − 3)/2 and L = p + r with r ≥ 0, the word R_{L}[M + 2^{r}] has zeros exactly at positions ⌈L/2⌉ − 1 and L − 1 − t. **Law 4.2**: for odd p ≥ 9 and r ≥ 4, the word R_{L}[M + 2^{r} + 1] has zeros exactly at ⌈L/2⌉ − 1, L − 1 − t and t + 1. The seam word R_{L}[M] is 1^{⌊L/2⌋−1} 0 1^{⌈L/2⌉}. The last two readings of q_{D} must be the zero L − 1 − t on ring D − 1 and the zero t + 1 on ring D, and both laws need p = 2t + 3 odd. The earlier single angle took p = ⌊2D/3⌋ + 1, which is even exactly when D ≡ 2 (mod 3). Its tail of 2/3 forces the last two slices onto (2m, m) at D = 3m + 2, and no odd p puts zeros at both: t = m places the zero 2m but leaves the last slice one short of t + 1, and t = m − 1 places t + 1 = m but misses 2m. With p odd the slices must be (D − 2 − t, t + 1). Solving ⌊(D − 1)τ⌋ = D − 2 − t and ⌊D(2τ − 1)⌋ = t + 1 for the tail τ gives t = ⌊(D − 2)/3⌋ and a window for τ just above 2/3. No second offset is needed.');
THM('Theorem 2.', 'Let D ≥ 13, t = ⌊(D − 2)/3⌋ and p = 2t + 3. For every τ in [2/3 + 1/(6D), 2/3 + 1/(3D)) the angle');
EQ('u_{D} = 1/2 + 2^{−p} + τ·2^{−(D−1)}');
P('reads the profile q_{D}. [[proved for D ≠ 14; D = 14 by exact computation; RUNS: sealed, D = 13–400 at three tails]]', { align: AlignmentType.LEFT });
PROOF('Write D = 3t + 2 + ρ with ρ ∈ {0, 1, 2}, so p − D = 1 − t − ρ, and 2^{L}u_{D} = 2^{L−1} + δ_{L} with δ_{L} = 2^{L−p} + τ·2^{L−D+1}.');
PROOF('*Rings L < p.* Here δ_{L} < 1, so the reader is at the seam word, slice ⌊Lδ_{L}⌋. For L ≤ 3 the slice is 0 and the seam words 1, 01, 011 give 1, 0, 0. For 4 ≤ L ≤ p − 3, δ_{L} = 2^{L−p}(1 + τ·2^{p−D+1}) ≤ 1.35 × 2^{L−p} ≤ 0.17, so ⌊Lδ_{L}⌋ < ⌊L/2⌋ − 1, the seam word’s only zero. For L = p − 2 = 2t + 1, δ_{L} = 1/4 + τ·2^{−t−ρ}, and ⌊Lδ_{L}⌋ < t − 1 = ⌊L/2⌋ − 1 follows from δ_{L} ≤ 1/4 + 0.69/8 for t ≥ 5 and is read directly at t = 3, 4 (slices 1 and 2 against zeros at 2 and 3). At L = p − 1 = 2t + 2, δ_{L} = 1/2 + τ·2^{p−D} and the excess (2t + 2)τ·2^{1−t−ρ} is below 1 for every D ≥ 13 (its largest value is 0.86, at D = 14), so the slice is t + 1, one past the zero at t. All these rings read 1.', false);
PROOF('*Rings p ≤ L ≤ D − 2.* The address is M + 2^{L−p} and the fractional part is τ·2^{L−D+1} < 1/2. By Law 4.1 the word has zeros at ⌈L/2⌉ − 1 and L − 1 − t, the first being the smaller. The slice is at most ⌊Lτ/2⌋, and since Lτ/2 < L/3 + 1/6 and L/3 has fractional part 0, 1/3 or 2/3, the slice is at most ⌊L/3⌋ < ⌈L/2⌉ − 1. These rings read 1.', false);
PROOF('*Ring D − 1.* The address is M + 2^{D−1−p} with D − 1 − p = t − 2 + ρ ≥ 1, the fraction is τ, and (D − 1)τ lies in [2D/3 − 1/2 − 1/(6D), 2D/3 − 1/3 − 1/(3D)). For ρ = 0, 1, 2 this interval lies in [2t, 2t + 1), [2t + 1, 2t + 2) and [2t + 2, 2t + 3), so the slice is D − 2 − t = L − 1 − t, a zero of Law 4.1.', false);
PROOF('*Ring D.* Here 2^{D}u_{D} − 2^{D−1} = 2^{D−p} + 2τ with 2τ ∈ [1, 2), so the address is M + 2^{D−p} + 1 and the fraction 2τ − 1 lies in [1/3 + 1/(3D), 1/3 + 2/(3D)). Then D(2τ − 1) lies in [(D + 1)/3, (D + 2)/3), whose floor is t + 1 for each ρ. Law 4.2 applies when D − p = t − 1 + ρ ≥ 4, which fails only at D = 14, and puts a zero at t + 1. At D = 14 the profile is read directly. ∎', false);
P('The control predicted by the same derivation lands as well: with τ = 2/3 and the same p the profile fails at every D ≡ 2 (mod 3) and holds at every D ≡ 0, 1 [[RUNS, D = 13–400]]. For D ≡ 0 and 1 the theorem’s angle and the earlier single angle share p, so Theorem 2 extends that angle rather than replacing it. Each angle sits in a half-open certificate interval of positive width, the intersection of the cells it occupies on rings 1 to D: 1/159,744 at D = 13, the width published for that depth, 5/2,981,888 at D = 14, and 11/4,260,607,557,632 at D = 32 [[RUNS, every D = 13–120]].');
FIG('figs/fig3_witness.png', 'Figure 3. Left: the angle of Theorem 2 at D = 32, a depth the earlier constructions did not reach. Each row is the word read on ring L (dark cells are zeros), the boxed cell is the slice read, and the reading is printed at the right. Below ring p = 23 the reader sits on the seam word; from ring 23 on it sits on the two-zero words of Law 4.1, and the slices reach the zero L − 1 − t on ring 31 and the zero t + 1 of the adjacent word on ring 32. Right: the complete set of angles that read q_{D}, by dyadic distance from the seam, for D = 20, 24, 28. The witness lies in the deepest shell (dotted).', 610);
P('The witness is one point of a large set. The complete preimage A(q_{D}) of the profile, computed by exact interval refinement ring by ring, has 41 intervals at D = 13 and 49,580 at D = 30, about 1.45 times as many at each further depth; its measure is 2.62·2^{−13} at D = 13 and 1617·2^{−30} at D = 30; and every interval lies in [1/2, 277/512) [[measured, D = 13–30]]. About a quarter of the measure sits between 2^{−5} and 2^{−4} to the right of the seam, while the witness family occupies the shell at distance 2^{−p}. A closed description of A(q_{D}) is OPEN.');

// ======================================================================= 6
H1('6. The frontier');
P('The map now carries the coordinates of Table 1, the readers of Table 2, the frame law and the witness family. Each item below is stated with the link it is missing.');
P('**The pairing behind the frame law.** Write, for each palindrome window, the one non-palindromic window it meets; the frame law then follows as a theorem rather than a checked owner.', { indent: { left: 360 } });
P('**The address switch point.** Derive k(n) from the trade between resolving the face, which an outer pair does for half of the remaining words, and starting the value count on the core; the data k = ⌊n/3⌋ with one exception at n = 11 fixes what the law has to produce.', { indent: { left: 360 } });
P('**The native-order statement.** Prove that an output’s optimal order follows its deciding chain, beginning with the families in Table 2 whose optima are exact.', { indent: { left: 360 } });
P('**The radial language.** The set of all radial profiles is not regular if its density R_{D}/2^{D} tends to 0 while R_{D}^{1/D} tends to 2, because a regular language with growth rate 2 has a simple pole at 1/2 in its generating function, and its density cannot vanish [11]. The measured density is 0.81 at D = 20; both limits are OPEN.', { indent: { left: 360 } });
P('**The preimage of q_{D}.** Describe A(q_{D}) in closed form from the seam blocks; Section 5 gives its first measured shape.', { indent: { left: 360 } });
P('**Spectral and arithmetic links.** A compact evaluator for the corrected block sums of the latitude spectrum, and the map from the adder’s cut states to its homological rank, both recorded as open in [7, §16], remain open.', { indent: { left: 360 } });

P('**Acknowledgment.** Computation and drafting were assisted by Claude (Anthropic). Results quoted from earlier independent runs are recorded with their seals in the running log [7]. Every number in this paper was produced by the scripts listed in Appendix B.', { size: 19 });

// ======================================================================= References
H1('References');
for (const r of [
  '[1] Kulik, D. A. (2026). *Only Addressable: The ring of all binary words — exact location without enumeration, a triangular top, and a law in thirds for what one ray reads.* QuHarmonics Research Group.',
  '[2] Kulik, D. A. (2026). *Decompiling Addressable Binary Rings: Forced involutions, the Möbius difference bridge, and radial witness topologies.* QuHarmonics Research Group.',
  '[3] Kulik, D. A. (2026). *The Geometry of a Readout.* QuHarmonics Research Group.',
  '[4] Kulik, D. A. (2026). *Algebraic Routing.* QuHarmonics Research Group.',
  '[5] Kulik, D. A. (2026). *Where Yes and No Become Maybe.* QuHarmonics Research Group.',
  '[6] Kulik, D. A. (2026). *Against Its Own Reverse.* QuHarmonics Research Group.',
  '[7] Kulik, D. A. (2026). Compiler rings running log, §0–§26 (compiler_rings_log.md). QuHarmonics Research Group.',
  '[8] Brent, R. P., & Kung, H. T. (1982). A regular layout for parallel adders. *IEEE Transactions on Computers*, C-31(3), 260–264.',
  '[9] Buhrman, H., & de Wolf, R. (2002). Complexity measures and decision tree complexity: a survey. *Theoretical Computer Science*, 288(1), 21–43.',
  '[10] Ünlüyurt, T. (2004). Sequential testing of complex systems: a review. *Discrete Applied Mathematics*, 142(1–3), 189–205.',
  '[11] Flajolet, P., & Sedgewick, R. (2009). *Analytic Combinatorics.* Cambridge University Press.'])
  P(r, { size: 19, indent: { left: 360, hanging: 360 }, align: AlignmentType.LEFT, spacing: sp(0, 80) });

// ======================================================================= Appendix A
PAGEBREAK();
H1('Appendix A. Sealed predictions');
P('Each prediction was written, with the reading it predicts and the readout it returns through, and its text hashed before the code that tests it was run. Each runner recomputes the digest before it starts and again after it finishes; all four were unchanged.');
TABLE([2300, 4660, 2400], [
  ['Prediction', 'SHA-256 of the seal file', 'Result'],
  ['Frame law, every offset (FA1)', 'deea12785b7254d12f0414692e6c76a887a6206b23f59f880e9abacd36459775', 'RUNS, 117 fresh cells'],
  ['Reader atlas RA1–RA6', 'b41403660526c910f6e1b560a378d43446fac013b748c20f61794b4e50961623', 'RA1, RA2, RA3, RA6 RUN; RA4, RA5 DEAD END'],
  ['Reader atlas, widths 17–19 (RA7)', 'acb799a49ce209b0b62b8534364795ff5c3faca34480d13c60b0e50b8a40d626', 'face, successor, partner RUN; switch-point fit DEAD END'],
  ['One angle for every depth (W2C)', '1d41cd5f68cd320b9e058d795931050624b7e3d12d6f75b064df2907636e6ede', 'RUNS, D = 13–400, three tails and the control']],
  { mono: [1], size: 16 });
P('Two scoring errors in the reader programme were found and corrected before the results were read; neither changed a sealed claim. The first scored the comparator’s two indicator bits separately where the seal defines it as one value; the second compared only the first 64 enumerated optimal orders with the 2^{h} outside-in orders, which made the face and comparator claims read false at n ≥ 14. Both are logged in [7, §23].', { size: 19 });

// ======================================================================= Appendix B
H1('Appendix B. Scripts and their output');
P('All scripts use exact integer and rational arithmetic. frame_atlas.py runs the frame law; frame_owner_check.py checks its owner; reader_atlas.py and reader_extend.py run the reader atlas; witness_run.py runs Theorem 2 and its control; preimage_map.py computes A(q_{D}); figures.py draws the figures. Summary lines of their output follow, unedited. In the reader lines, “two-wheel” and “core” report the sealed form with a three- or four-bit core, which is the DEAD END of Section 3.5; the measured cores are given there.');
const pick = (file, re) => fs.readFileSync(file, 'utf8').split('\n').filter(l => re.test(l));
MONOLINES([
  ...pick('/home/claude/atlas/frame_output.txt', /^L=(1[6-9]|2[0-2]) |^seen widths/),
  ...pick('/home/claude/atlas/reader_output.txt', /^n=1[3-6] |^adder|^claims/),
  ...pick('/home/claude/atlas/reader_extend_output.txt', /^n=1[7-9] face|^claims/),
  ...pick('/home/claude/atlas/witness_output.txt', /^D= (1[3-9]|2[0-3]) |^D=(100|200|300|400) |^result/),
].flatMap(l => wrap(l, 104)), 13);

// ======================================================================= DOCUMENT
const footer = new Footer({ children: [
  new Paragraph({ children: [new TextRun({ text: 'Copyright Dean A. Kulik – ORCID 0009-0003-3128-8828 · Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)', font: BODY, size: 14, color: MUTED })], alignment: AlignmentType.CENTER, spacing: { before: 0, after: 0 } }),
  new Paragraph({ children: [new TextRun({ text: 'github.com/QuHarmonics/The-Nexus-Harmonic-Reality · info@quharmonics.com · Page ', font: BODY, size: 14, color: MUTED }), new TextRun({ children: [PageNumber.CURRENT], font: BODY, size: 14, color: MUTED })], alignment: AlignmentType.CENTER, spacing: { before: 0, after: 0 } })] });
const header = new Header({ children: [new Paragraph({ children: [new TextRun({ text: TITLE + ' · Kulik 2026', font: BODY, size: 15, color: MUTED })], alignment: AlignmentType.RIGHT })] });

const doc = new Document({
  creator: 'Dean A. Kulik', title: TITLE, subject: 'Reading orders, tape frames and a uniform profile witness', description: 'QuHarmonics Research Group, October 2026',
  styles: { default: { document: { run: { font: BODY, size: 21, color: INK } } },
    paragraphStyles: [
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: BODY, size: 26, bold: true, color: INK }, paragraph: { spacing: { before: 320, after: 140 }, outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: BODY, size: 22, bold: true, color: INK }, paragraph: { spacing: { before: 220, after: 100 }, outlineLevel: 1 } }] },
  sections: [{ properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, bottom: 1300, left: 1440, right: 1440, header: 600, footer: 500 } } },
    headers: { default: header }, footers: { default: footer }, children: blocks }]
});
Packer.toBuffer(doc).then(buf => { fs.writeFileSync('Mapping_the_Nested_Partner_Ring.docx', buf); console.log('wrote', buf.length, 'bytes'); });
