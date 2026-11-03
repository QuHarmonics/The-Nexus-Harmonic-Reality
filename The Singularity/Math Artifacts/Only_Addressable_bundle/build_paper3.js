const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, ImageRun,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle, Footer, PageNumber,
} = require('docx');

const FONT = 'Cambria', MONO = 'Consolas';
const INK = '1F2933', SUB = '2D3748', GREY = '4A5568';
const STAT = { proved: '2B6CB0', computed: '2F855A', sealed: '553C9A', cited: '4A5568', open: 'C05621' };

// ---------- rich text: ^{..} superscript, _{..} subscript ----------
function R(text, o = {}) {
  const out = [];
  String(text).split(/(\^\{[^}]*\}|_\{[^}]*\})/).forEach(seg => {
    if (!seg) return;
    const base = { font: o.font || FONT, size: o.size || 22, italics: !!o.italics, bold: !!o.bold, color: o.color };
    if (seg.startsWith('^{')) out.push(new TextRun({ ...base, text: seg.slice(2, -1), superScript: true }));
    else if (seg.startsWith('_{')) out.push(new TextRun({ ...base, text: seg.slice(2, -1), subScript: true }));
    else out.push(new TextRun({ ...base, text: seg }));
  });
  return out;
}
const flat = parts => { const f = []; parts.forEach(p => (typeof p === 'string') ? f.push(...R(p)) : Array.isArray(p) ? f.push(...p) : f.push(p)); return f; };
const it = t => R(t, { italics: true });
const bd = t => R(t, { bold: true });
function tag(kind, scope) {
  const out = [new TextRun({ text: ' [', font: FONT, size: 18, color: GREY }),
    new TextRun({ text: kind, font: FONT, size: 18, bold: true, color: STAT[kind] })];
  if (scope) out.push(...R('; ' + scope, { size: 18, color: GREY }));
  out.push(new TextRun({ text: ']', font: FONT, size: 18, color: GREY }));
  return out;
}
const P = (...parts) => new Paragraph({ children: flat(parts), spacing: { after: 140, line: 288 }, alignment: AlignmentType.JUSTIFIED });
const PK = (...parts) => new Paragraph({ children: flat(parts), spacing: { after: 140, line: 288 }, alignment: AlignmentType.JUSTIFIED, keepNext: true });
function Q(text) {
  return new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 80, after: 160 }, keepLines: true,
    children: R(text, { italics: false, size: 23, color: INK }) });
}
const H1 = t => new Paragraph({ heading: HeadingLevel.HEADING_1, keepNext: true,
  children: [new TextRun({ text: t, font: FONT, size: 28, bold: true, color: INK })], spacing: { before: 360, after: 160 } });
const H2 = t => new Paragraph({ heading: HeadingLevel.HEADING_2, keepNext: true,
  children: [new TextRun({ text: t, font: FONT, size: 24, bold: true, color: SUB })], spacing: { before: 240, after: 120 } });
function STATE(label, ...parts) {     // a lemma / theorem statement, set off by a left rule
  return new Paragraph({ children: [...R(label + ' ', { bold: true }), ...flat(parts)], spacing: { before: 60, after: 140, line: 288 },
    alignment: AlignmentType.JUSTIFIED, indent: { left: 240 },
    border: { left: { style: BorderStyle.SINGLE, size: 12, color: '90CDF4', space: 8 } } });
}
function pngSize(file) { const b = fs.readFileSync(file); return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) }; }
function FIG(file, n, note, W = 600) {
  const { w, h } = pngSize(file); const H = Math.round(W * h / w);
  return [new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 120, after: 60 }, keepNext: true,
      children: [new ImageRun({ type: 'png', data: fs.readFileSync(file), transformation: { width: W, height: H } })] }),
    new Paragraph({ alignment: AlignmentType.LEFT, spacing: { after: 220 },
      children: [...R(`Figure ${n}. `, { bold: true, size: 18, color: GREY }), ...R(note, { italics: true, size: 18, color: GREY })] })];
}
const border = { style: BorderStyle.SINGLE, size: 4, color: 'A0AEC0' };
const borders = { top: border, bottom: border, left: border, right: border };
function cell(text, w, o = {}) {
  return new TableCell({ borders, width: { size: w, type: WidthType.DXA },
    shading: o.fill ? { fill: o.fill, type: ShadingType.CLEAR, color: 'auto' } : undefined,
    margins: { top: 45, bottom: 45, left: 80, right: 80 },
    children: [new Paragraph({ keepNext: !!o.keepNext, keepLines: true, alignment: o.align || AlignmentType.LEFT,
      children: R(String(text), { size: o.size || 17, bold: !!o.bold, color: o.color }) })] });
}
function table(headers, rows, widths, o = {}) {
  const W = widths.reduce((a, c) => a + c, 0);
  return new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: widths,
    rows: [new TableRow({ tableHeader: true, cantSplit: true, children: headers.map((h, i) => cell(h, widths[i], { bold: true, fill: 'EDF2F7', size: o.size, keepNext: true, align: o.align && o.align[i] })) }),
      ...rows.map((r, ri) => new TableRow({ cantSplit: true, children: r.map((c, i) => {
        const key = String(c).split(/[ ;,]/)[0];
        return cell(c, widths[i], { size: o.size, color: STAT[key], bold: !!STAT[key], keepNext: o.keep !== false && ri < rows.length - 1, align: o.align && o.align[i] });
      }) }))] });
}
const tcap = t => new Paragraph({ spacing: { before: 200, after: 80 }, keepNext: true, children: R(t, { bold: true, size: 19, color: SUB }) });
const after = () => new Paragraph({ spacing: { after: 120 }, children: [] });
function box(title, paras, color = '9C4221', fill = 'FFFAF0') {
  const W = 9360, rb = { style: BorderStyle.SINGLE, size: 8, color };
  return new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: [W],
    rows: [new TableRow({ children: [new TableCell({ borders: { top: rb, bottom: rb, left: rb, right: rb },
      width: { size: W, type: WidthType.DXA }, shading: { fill, type: ShadingType.CLEAR, color: 'auto' },
      margins: { top: 120, bottom: 120, left: 160, right: 160 },
      children: [new Paragraph({ spacing: { after: 100 }, children: R(title, { bold: true, size: 22, color }) }),
        ...paras.map(p => new Paragraph({ spacing: { after: 90, line: 270 }, alignment: AlignmentType.JUSTIFIED,
          children: p.flatMap(x => typeof x === 'string' ? R(x, { size: 19 }) : [x]) }))] })] })] });
}
const sm = t => R(t, { size: 19 });
const smb = t => R(t, { size: 19, bold: true });
const mono = (line, o = {}) => new Paragraph({ spacing: { after: 0, line: 220 }, keepLines: true,
  children: [new TextRun({ text: line.length ? line : ' ', font: MONO, size: o.size || 13, color: o.color || '1A202C', bold: !!o.bold })] });

const C = [];
// ================= front matter =================
C.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 200, after: 80 },
  children: [new TextRun({ text: 'Only Addressable', font: FONT, size: 48, bold: true, color: INK })] }));
C.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 240 },
  children: R('The ring of all binary words: exact location without enumeration, a triangular top, and a law in thirds for what one ray reads', { size: 24, italics: true, color: SUB }) }));
C.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 }, children: R('Dean A. Kulik', { size: 24, bold: true }) }));
C.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 }, children: R('QuHarmonics Research Group  ·  ORCID 0009-0003-3128-8828', { size: 20 }) }));
C.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 300 }, children: R('19 October 2026  ·  CC BY-NC 4.0', { size: 20 }) }));
C.push(new Paragraph({ spacing: { after: 200, line: 276 }, alignment: AlignmentType.JUSTIFIED, border: { top: border, bottom: border }, children: [
  ...smb('Status words. '),
  ...sm('A bracket after a statement records how it stands. '), new TextRun({ text: 'proved', font: FONT, size: 19, bold: true, color: STAT.proved }),
  ...sm(': proved in this paper. '), new TextRun({ text: 'computed', font: FONT, size: 19, bold: true, color: STAT.computed }),
  ...sm(': an exact computation, its range stated; every one is reproduced by the scripts of Appendix B. '),
  new TextRun({ text: 'sealed', font: FONT, size: 19, bold: true, color: STAT.sealed }),
  ...sm(': a prediction whose text was hashed (SHA-256) before the computation that tests it was run. '),
  new TextRun({ text: 'cited', font: FONT, size: 19, bold: true, color: STAT.cited }), ...sm(': an established result. '),
  new TextRun({ text: 'open', font: FONT, size: 19, bold: true, color: STAT.open }), ...sm(': stated here and not settled.'),
] }));

// ================= abstract =================
C.push(H1('Abstract'));
C.push(P('Pair each binary word of length L with its reverse, or with its complement when it is a palindrome, and lay the pairs out from the centre of a ring. Every word appears once and faces its partner across the ring. At L = 64 the ring has 2^{64} words and at L = 512 it has 2^{512}. Neither can be written down; both can be read, because the position of any word and the word at any position follow from O(L) arithmetic. Stack the rings and read one ray: ring L contributes the bit its tape holds at the ray’s angle.'));
C.push(P('Three results fall out. First, near the seam the order of representatives is triangular: exactly μ(2^{h} − 1 − ℓ) of them share a left half ℓ, so the word j places past the seam is all ones outside a central core about log_{2} j bits wide, and ring L + 2 carries that core unchanged with one more 1 at each end. Second, the radial profile 100 1^{D−5} 00, which no angle within 2^{−(D−2)} of the seam can read, is read at every depth D ≥ 8, and for D ≥ 13 on an explicit interval around u_{D} = ½ + 2^{−p} + f·2^{−(D−1)}, with p = 2⌊(D + 1)/3⌋ + 1 and f = ⅔, plus 1/(6D) when D ≡ 2 (mod 3). The last two rings read through the doubling map’s only 2-cycle, {⅓, ⅔}; the core under the ray reaches ⅓ and ⅔ when the ray sits 2^{D/3} words past the seam, which puts the one address bit near depth 2D/3; and the residue split modulo 3 is the parity that keeps the core clean. The residue-2 address was hashed before it was run and holds at all 36 depths tested; the unified law holds at every depth from 13 to 119. Third, the readable profiles form a language whose finite-horizon automata grow from 29 to 1,451 states between horizons 8 and 16, and whose depth-11 prefixes alone fall into 311 classes.'));

C.push(H1('How the paper runs'));
C.push(P('The paper is written from its end. Section 1 states the finished object: an interval that reads a prescribed 119-bit profile through rings no computer could store. Sections 2 to 5 build only what that object needs. Sections 6 and 7 walk back from its last two bits, because the end of the profile is what fixes everything before it, and Section 8 proves what the walk found. Where a step needed a value, the value was derived from the constraints around it and then checked; the few scans that were run were over a family already derived, and each is recorded where it occurs.'));

// ================= 1 =================
C.push(H1('1. The held end'));
C.push(PK('Let D = 119. The angle'));
C.push(Q('u_{119} = ½ + 2^{−81} + (⅔ + 1/714)·2^{−118}'));
C.push(PK('lies in a half-open interval K_{119} of width about 2^{−127.5}, given exactly in Appendix A. Every angle in K_{119}, read through the concentric rings of lengths 1 to 119, returns'));
C.push(Q('1 0 0 1^{114} 0 0.'));
C.push(P('The outermost of those rings holds 2^{119} ≈ 6.6 × 10^{35} words. No ring longer than 18 was built for this paper. The interval was written down from a formula, and the formula was checked by reading its 119 bits one ring at a time, each by arithmetic on the angle.'));
C.push(P('The same holds at every depth D ≥ 8 for the family q_{D} = 100 1^{D−5} 00, and the family is held here for one reason. Its opening bits are what the seam of the rings reads, and an argument at the seam shows that its closing 00 cannot be read there. The profile is impossible where it starts and present elsewhere. The rest of the paper finds where, and why there.'));

// ================= 2 =================
C.push(H1('2. The ring'));
C.push(H2('2.1 The pairing'));
C.push(PK('For a word x = x_{0}x_{1}…x_{L−1}, let J reverse it and C complement it, and set'));
C.push(Q('P(x) = J(x) if J(x) ≠ x,   P(x) = C(x) if J(x) = x.'));
C.push(P('P is an involution with no fixed point at every length. On non-palindromes it is reversal, and the reverse of a non-palindrome is a non-palindrome. On palindromes it is complement, which fixes no word and sends palindromes to palindromes.', tag('proved'), ' So the 2^{L} words fall into 2^{L−1} pairs, and the 2^{⌈L/2⌉} palindromes pair among themselves.'));
C.push(P('Two neighbouring involutions must be kept apart from P. Reversal J fixes the palindromes, and the half-turn H, which rotates a word of even length by L/2 places, fixes the words uu with two equal halves. Both fixed sets have 2^{L/2} members at even L, and they are different sets: 0101 is fixed by H and not by J, and 0110 by J and not by H. P fixes nothing, so every orbit of P is a 2-cycle and P has no transient states at any length.', tag('proved')));
C.push(H2('2.2 The layout'));
C.push(P('Call x a representative when x < P(x), comparing as integers with x_{0} the most significant bit. Each pair has exactly one. Place the representatives in increasing order in positions 0 to M − 1 of a ring of N = 2^{L} positions, M = 2^{L−1}; place their partners in decreasing order in positions M to N − 1; then swap the two words at positions M − 1 and M. Positions i and N − 1 − i hold partners for every i.', tag('proved'), ' This is the ring obtained by inserting the pairs one at a time into the middle of a growing list with the last pair turned round, which is the construction this study began from; the two descriptions agree word for word for L = 1 to 16.', tag('computed')));
C.push(PK('The swap leaves the largest representative at position M, just clockwise of the seam, and its partner at M − 1. For L ≥ 4 the largest representative is'));
C.push(Q('C_{L} = 1^{⌊L/2⌋−1} 0 1^{⌈L/2⌉},'));
C.push(P('and for j ≥ 1 the word at M + j is the partner of the j-th largest representative, counting the largest as j = 0. Figure 1 shows the rings for L = 1 to 8.'));
C.push(...FIG('figs/fig1_rings.png', 1, 'The rings for L = 1 to 8, read clockwise from the top; blue is 1. Every word of each length appears once, and opposite positions hold partners. The seam at u = ½ is where the representatives (first half of each ring) meet their partners. The second ray reads 1 0 0 1 1 1 0 0 on rings 1 to 8, the depth-8 member of the family studied here; no angle within 2^{−6} clockwise of the seam reads it.', 470));
C.push(P('The pair readout x ⊕ P(x) is a palindrome for every x and equals 1^{L} exactly when x is a palindrome; both partners give the same readout.', tag('proved'), ' The difference alone is therefore many-to-one. The step that keeps the value beside the difference, (u, v) → (u, u ⊕ v), applied at every scale of a table of 2^{n} values, is the fast Möbius transform of the Boolean lattice: its output is the algebraic normal form and it is its own inverse.', tag('cited', 'Rota 1964'), ' Kept beside the value, the difference loses nothing.'));

// ================= 3 =================
C.push(H1('3. Only addressable'));
C.push(P('A ring of 2^{64} words cannot be stored, and a ring of 2^{512} words cannot be stored by anything. Neither has to be.'));
C.push(P('To locate a word x, take its representative r and count the representatives below r. Scanning mirrored pairs (x_{j}, x_{L−1−j}) from the outside in, a word is a representative exactly when its first unequal pair is (0, 1), or when it is a palindrome with x_{0} = 0. Counting the words below r with that property is a digit computation over the mirrored pairs, outside in, carrying three small comparisons (the prefix against r, the suffix against r, and the word against its own reverse), plus a direct count of palindromes. It takes O(L) steps. The position is the count when x = r and N − 1 minus the count when x is the partner, with the swap at the seam applied.', tag('proved'), ' The word at a given position is recovered by binary search on the same count: O(L) counts of O(L) steps each.'));
C.push(P('Two readings show the scale. The first 64 bits of π, 0x243F6A8885A308D3, sit at position 2,427,008,858,123,944,441 of the 64-bit ring, and their partner at 2^{64} − 1 minus that. A 512-bit word drawn from a fixed seed goes from word to position to word in about a second, and its partner sits at 2^{512} − 1 minus its position.', tag('computed'), ' In both cases the ring was never built. Everything that follows uses only this: any word at any position, on demand.'));

// ================= 4 =================
C.push(H1('4. The triangular top'));
C.push(P('The ray of Section 1 never strays far from the seam, so every word it reads is one of the largest representatives or the partner of one. Their order has a closed form. Write h = ⌊L/2⌋, μ = 1 for even L and μ = 2 for odd L, and let the left half of x be the h-bit integer ℓ = x_{0}…x_{h−1}.'));
C.push(STATE('Lemma A (the triangular count).', 'If ℓ ≥ 2^{h−1}, exactly μ(2^{h} − 1 − ℓ) representatives have left half ℓ.', tag('proved'), tag('computed', 'exhaustively for L = 3 to 20')));
C.push(P(it('Proof. '), 'Write ℓ = 1^{t} 0 w with t ≥ 1 and w of length n = h − t − 1. The first t mirrored pairs have left bit 1. None of them can be the deciding (0, 1) pair, and a (1, 0) among them would make x larger than its reverse, so all t are (1, 1). Pair t has left bit 0. If its right bit is 1, the pair decides, x is a representative, and the right bits of the remaining n pairs are free: 2^{n} completions. If its right bit is 0, the pair is equal and the decision moves inward: the first unequal pair among the remaining n must be (0, 1), which needs a 0 of w, and a 0 of w at place k (from the outside, counting from 0) leaves 2^{n−1−k} free completions after it. These sum to the complement of w, 2^{n} − 1 − w. A completion with every pair equal is a palindrome beginning with 1, which is not a representative. The middle bit of an odd word is compared only with itself and is free. The total is μ(2^{n} + 2^{n} − 1 − w) = μ(2^{h} − 1 − ℓ). ∎'));
C.push(P('Counting down from the largest representative, then, the left halves arrive in blocks K = 2^{h} − 1 − ℓ = 0, 1, 2, …, and block K holds μK representatives. The j-th largest lies in the block with μK(K − 1)/2 ≤ j < μK(K + 1)/2: a triangular stack, with K ≈ √(2j/μ). Within a block the order is the order of the completions read as a binary number, the middle bit first and then the right bits of the inner pairs from the innermost out. The blocks cover the top quarter of the representatives, which with their partners fill the quarter of the ring centred on the seam.'));
C.push(P('The word at M + j is the reverse of the j-th largest representative. Reversal turns 1^{t} 0 w … into a word that is 1 in its first t and last t places, with everything else in a central core of 2⌊log_{2} K⌋ + 2 + (L mod 2) places. That is the core law: the word j places past the seam is all ones outside a core about log_{2} j wide. Rebuilding the words from the blocks alone reproduces the O(L) reader at every offset in the top quarter of every ring from L = 4 to 18.', tag('computed'), ' Figure 2 shows the core for L = 40.'));
C.push(...FIG('figs/fig2_triangular_top.png', 2, 'The triangular top, L = 40. Each row is the word j places past the seam, rows placed by log_{2} j; dark squares are zeros and all other bits are 1. The orange staircase is the core predicted by Lemma A, [t, L − 1 − t] with t = h − 1 − ⌊log_{2} K⌋. The core gains one place on each side each time the block index K doubles, that is each time j quadruples, and reaches L/3 and 2L/3 near j = 2^{11}.'));
C.push(STATE('Theorem C (clean cores).', 'Let s and L have opposite parity, so that the block containing offset 2^{s} is K = 2^{n} with n = ⌈s/2⌉. Then the word at M + 2^{s} has its zeros exactly at ⌈L/2⌉ − 1 and ⌈L/2⌉ + n, and for s ≥ 2 the word at M + 2^{s} + 1 has its zeros exactly at ⌊L/2⌋ − n, ⌈L/2⌉ − 1 and ⌈L/2⌉ + n.', tag('proved'), tag('computed', '1,579 of 1,579 cases')));
C.push(P(it('Proof. '), 'With K = 2^{n} the left half is 1^{t} 0 1^{n}. Since w has no 0, every completion in the block decides at pair t, and the block is the μ2^{n} settings of its n + (L mod 2) free bits in decreasing order. When s and L have opposite parity, the triangular count below the block is μ2^{n}(2^{n} − 1)/2 = 2^{s} − μ2^{n−1}, so offset 2^{s} is place μ2^{n−1} of its block and its free bits read μ2^{n−1} − 1, a 0 followed by 1s. Offset 2^{s} + 1 reads μ2^{n−1} − 2, a 0, then 1s, then a final 0, and needs s ≥ 2 to stay inside the block. Reversal puts the free bits leftward from index ⌈L/2⌉ − 1 and the fixed 0 of pair t at L − 1 − t = ⌈L/2⌉ + n. ∎ The zero sets agree with the reader in all 1,579 admissible cases checked: every s for L = 6 to 80, and sampled s for L = 128, 129, 160, 161, 200 and 201.'));
C.push(P('The closed forms found earlier near the seam are the first blocks of this stack. C_{L} is block K = 1 at j = 0, and the words at M + 1, M + 2 and M + 3, first read off the rings and fitted in each parity, are the next places in it.'));
C.push(STATE('Theorem D (the pad law).', 'For every j in the top quarter of ring L, the word at M + j in ring L + 2 is the word at M + j in ring L with a 1 added at each end.', tag('proved'), tag('computed', 'L = 4 to 16')));
C.push(P(it('Proof. '), 'The offset j and the parity μ fix the block, the place in it and the free bits. Two more letters add one (1, 1) pair on the outside, so t grows by one and nothing inside moves. ∎ At a fixed distance from the seam the core is carried from ring to ring unchanged, and the longer word only adds ones around it. It is the same core at a different location. That is the one exact statement this paper makes about how a ring relates to the ring two lengths before it.'));

// ================= 5 =================
C.push(H1('5. One ray'));
C.push(PK('Give ring L a tape of S_{L} = L·2^{L} slices, its words laid end to end around the circle. A ray at angle u ∈ [0, 1), measured clockwise from the top, reads on ring L'));
C.push(Q('b_{L}(u) = R_{L}[⌊2^{L}u⌋][⌊L·{2^{L}u}⌋],'));
C.push(P('where R_{L} is the ring and {·} is the fractional part. The first index picks the word and the second the bit within it. One u addresses every ring at once. In binary, u = 0.c_{1}c_{2}c_{3}…, the word index on ring L is the integer c_{1}…c_{L}, so each ring outward appends one bit of the angle to the address, and the bit index is set by what remains. The profile of u to depth D is b_{1}(u)…b_{D}(u).'));
C.push(P('The angles that read a profile p of length k form a finite union A_{p} of half-open intervals, and A_{pb} = A_{p} ∩ {u : b_{k+1}(u) = b}.', tag('proved'), ' The two children of a parent partition it, so a readable parent never loses both. A child is unreadable exactly when the parent’s set lies inside the region where ring k + 1 reads the other bit. That region is a union of runs of slices, and a parent’s set can meet several of them: of the 101 minimal unreadable extensions through depth 12, 25 have parents that meet more than one run.', tag('computed')));
C.push(P('Table 1 gives the number R_{d} of readable profiles of depth d and the number E_{d} = 2R_{d−1} − R_{d} that become unreadable at depth d, from the 1,825,792 atoms of the common refinement of all slice boundaries through ring 16.', tag('computed')));
const Rd = [2, 4, 8, 16, 31, 62, 123, 239, 469, 924, 1827, 3606, 7122, 14087, 27819, 55122];
const rowsT1 = [];
for (let i = 0; i < 8; i++) {
  const r = [];
  [i, i + 8].forEach(k => { const d = k + 1, R_ = Rd[k], E = k ? 2 * Rd[k - 1] - R_ : 0;
    r.push(String(d), R_.toLocaleString('en-US'), (R_ / 2 ** d).toFixed(3), String(E)); });
  rowsT1.push(r);
}
C.push(tcap('Table 1. Readable radial profiles by depth'));
C.push(table(['d', 'R_{d}', 'R_{d}/2^{d}', 'E_{d}', 'd', 'R_{d}', 'R_{d}/2^{d}', 'E_{d}'], rowsT1, [700, 1340, 1300, 1340, 700, 1340, 1300, 1340],
  { size: 17, align: Array(8).fill(AlignmentType.RIGHT) }));
C.push(after());
C.push(P('The fraction of all 2^{d} profiles that some ray reads falls slowly, to 0.841 at d = 16 (Figure 3). As a language the readable profiles are harder than that fraction suggests. The minimal automaton accepting exactly the readable profiles up to horizon H has 29, 49, 76, 111, 186, 322, 519, 914 and 1,451 states for H = 8 to 16, and the readable depth-11 prefixes split into 1, 3, 14, 51, 175 and 311 classes as the horizon runs from 11 to 16.', tag('computed'), ' The 311 classes are pairwise separated by actual continuations, so an exact finite automaton for the unbounded language, if there is one, has at least 312 states. Whether there is one is', tag('open'), ': the class count has not stopped growing.'));
C.push(P('The swap at the seam is not cosmetic. Without it R_{10} = 947 and R_{12} = 3,710, instead of 924 and 3,606.', tag('computed'), ' These counts were first obtained in independent runs; the numbers here come from a separate computation and agree with every one of them.'));
C.push(...FIG('figs/fig5_language.png', 3, 'Left: the fraction of all 2^{d} profiles that some ray reads. Right: states of the minimal automaton for the readable profiles up to horizon H (blue), and the number of classes into which those continuations split the readable depth-11 prefixes (orange). Exact counts, recomputed for this paper.'));

// ================= 6 =================
C.push(H1('6. A profile the seam cannot finish'));
C.push(P('Let q_{D} = 100 1^{D−5} 00 for D ≥ 8. Ring 1 is 01, so every angle that reads q_{D} lies clockwise of the seam, u ≥ ½; write u = ½ + δ.'));
C.push(P('The seam reads the opening of q_{D}. While 2^{L}δ < 1, ring L reads its centre word C_{L} at bit ⌊L·2^{L}δ⌋. The centre words C_{1}, C_{2}, C_{3} = 1, 01, 011 read 1, 0, 0 at bit 0, and C_{L} for L ≥ 4 reads 1 until the bit index reaches its only zero, at ⌊L/2⌋ − 1.'));
C.push(P('The seam cannot read the close. The ray reaches the zero of C_{L} when δ is near 2^{−(L+1)}, a window that halves with every ring, so two consecutive rings never meet their zeros at one angle: on the centre line, rings D − 1 and D never both read 0. That is the reason behind the exclusion of the cell [½, ½ + 2^{−D}), proved in independent work. The exclusion is four times wider. Within 2^{−(D−2)} of the seam the ray meets only C_{L} and the words one, two and three places past it, and by Lemma A each of these has its zeros within two places of its middle and 1s at both ends. Ring D reads its word at the fraction {2f}, where f is the fraction at which ring D − 1 reads; a zero near the middle of ring D − 1 (f near ½) sends ring D to an edge of its word, which reads 1. No angle in [½, ½ + 2^{−(D−2)}) reads q_{D}.', tag('proved', 'for large D'), tag('computed', 'D = 8 to 22')));
C.push(P('The members of the family are pairwise disjoint: for E > D, q_{D} has 0 at place D − 1 where q_{E} has 1. Each depth needs its own location.'));
C.push(P('That is the held end. The profile closes with zeros on two consecutive rings, and the seam, where it opens, cannot supply them.'));

// ================= 7 =================
C.push(H1('7. The route back'));
C.push(H2('7.1 The last two rings'));
C.push(P('Ring D − 1 reads its word at the fraction f = {2^{D−1}u}, and ring D reads at {2f}. For both to read a zero away from the edges, f and {2f} must both fall in cores, and cores sit around the middle of a word. The doubling map f → {2f} has exactly one orbit of period two, {⅓, ⅔}: a ray reading ring D − 1 near ⅔ reads ring D near ⅓.'));
C.push(P('The data said so before the argument did. Taking the component of A(q_{D}) nearest the seam at each depth, at depths 9, 11 and 13 to 18 every one reads ring D − 1 between 0.63 and 0.69 of its word and ring D between 0.27 and 0.38.', tag('computed'), ' Depth 12 sits looser, at 0.72 and 0.44. Depth 10 leaves by a different door: a middle zero at ring D − 1 doubles to a zero near the right edge of a word 32 places out, where the core has already reached the edge.'));
C.push(H2('7.2 The address'));
C.push(P('The cores under the last two rings must therefore reach ⅓ and ⅔ of their words. By the core law the core of the word j places past the seam spans about ½ ± (log_{2} j)/(2L) of the word. Reaching ⅓ and ⅔ needs (log_{2} j)/2 ≈ L/6, so j ≈ 2^{L/3}: at ring D the ray must sit about 2^{D/3} words past the seam. In angle that is δ ≈ 2^{D/3}·2^{−D} = 2^{−2D/3}, one address bit near depth 2D/3.'));
C.push(PK('So the address has three parts: the seam bit, one bit near depth 2D/3, and a tail that holds f at ⅔ from depth D on. In binary,'));
C.push(Q('u_{D} = 0.1 0⋯0 1 0⋯0 1 0 1 0 …,'));
C.push(P('with 1s at place 1, at place p, and at every second place from D. The tail is the 2-cycle written out, and it is the same tail at every depth. What changes with D is only where it starts, and the single bit at p is what puts it there. The family is one path read at different locations, and the address shows it bit by bit.'));
C.push(H2('7.3 Parity'));
C.push(PK('A core is clean, with two or three isolated zeros at the places Theorem C names, when the block under the ray is a power of two, and at offset 2^{s} that happens exactly when s and L have opposite parity. On rings L ≥ p the ray sits 2^{L−p} words past the seam, so every ring from p outward is clean exactly when p is odd. With p = ⌊2D/3⌋ + 1, p is odd for D ≡ 0 or 1 (mod 3) and even for D ≡ 2. That is the residue split the computations kept showing. Moving p to ⌊2D/3⌋ + 2 when D ≡ 2 makes it odd again, and one formula covers all three classes:'));
C.push(Q('p = 2⌊(D + 1)/3⌋ + 1.'));
C.push(P('For D = 3m + 2 the move costs one place at the last ring: its inner zero now sits at m + 1, while a ray at phase exactly ⅔ reads place m. Ring D reads place ⌊D·{2f}⌋, so the phase has to rise by at least 1/(6D), and by less than 1/(3(D − 1)), the most that ring D − 1 tolerates. The least rise, one third of a ring-D slice, gives f = ⅔ + 1/(6D). This address was derived, written down with the reading it predicts and the control it predicts to fail, hashed (SHA-256 60a2aad0…12fd65fd; the full text is Appendix C), and only then run.', tag('sealed')));

// ================= 8 =================
C.push(H1('8. The theorem'));
C.push(STATE('Theorem E.', 'For D ≥ 13 let p = 2⌊(D + 1)/3⌋ + 1; let f = ⅔, or ⅔ + 1/(6D) when D ≡ 2 (mod 3); and let u_{D} = ½ + 2^{−p} + f·2^{−(D−1)}. Let K_{D} be the intersection, over rings L = 1 to D, of the half-open slice [j_{L}/S_{L}, (j_{L} + 1)/S_{L}) that contains u_{D}, where j_{L} = ⌊S_{L}u_{D}⌋. Then K_{D} has positive width, and every angle in K_{D} reads q_{D} = 100 1^{D−5} 00.', tag('proved')));
C.push(PK(it('Proof. ')));
const steps = [
  ['(a) Width. ', 'u_{D} lies in each of the D slices, so the largest left end is at most u_{D} and the smallest right end exceeds it. Every point of K_{D} shares all D slices with u_{D} and so reads what u_{D} reads.'],
  ['(b) Addresses. ', 'For L < p, 2^{L}u_{D} = 2^{L−1} + δ_{L} with δ_{L} = 2^{L−p} + f·2^{L−D+1} in (0, 1), so ring L reads C_{L} at bit ⌊Lδ_{L}⌋. For p ≤ L ≤ D − 2 the bit at p has moved into the integer part: ring L reads the word at M + 2^{L−p} at bit ⌊L·f·2^{L−D+1}⌋. Ring D − 1 reads the word at M + 2^{D−1−p} at bit ⌊(D − 1)f⌋. Ring D reads the word at M + 2^{D−p} + 1 at bit ⌊D·{2f}⌋, the extra 1 being the carry from f > ½.'],
  ['(c) Rings 1 to 3 ', 'read C_{1}, C_{2}, C_{3} at bit 0: 1, 0, 0.'],
  ['(d) Rings 4 to p − 2 read 1. ', 'Here δ_{L} ≤ 2^{L−p}(1 + ε) with ε = f·2^{p−D+1}, which keeps the bit index below the only zero of C_{L}, at ⌊L/2⌋ − 1. The tightest ring is L = p − 2, where the condition is (p − 2)(1 + ε) < 4(⌊(p − 2)/2⌋ − 1). It holds for every D ≥ 13 and fails at D = 12, which is why the law starts at 13.'],
  ['(e) Ring p − 1 reads 1. ', 'There δ_{p−1} = ½ + f·2^{p−D}, so the bit index is ⌊(p − 1)/2⌋ plus fewer than (p − 1)/2 further places: past the zero of C_{p−1}, in its trailing run of ones.'],
  ['(f) Rings p to D − 2 read 1. ', 'Since p is odd these rings are clean (Theorem C) and have no zero before index ⌈L/2⌉ − 1. The bit index is at most ⌊Lf/2⌋ ≤ ⌊L/3 + L/(12D)⌋, which is smaller.'],
  ['(g) Ring D − 1 reads 0. ', 'By Theorem C its outer zero is at ⌈(D − 1)/2⌉ + ⌈(D − 1 − p)/2⌉, and Table 2 shows that this equals ⌊(D − 1)f⌋ in each residue.'],
  ['(h) Ring D reads 0. ', 'By Theorem C its inner zero is at ⌊D/2⌋ − ⌈(D − p)/2⌉, which equals ⌊D·{2f}⌋ in each residue (Table 2). ∎'],
];
steps.forEach(([a, b]) => C.push(new Paragraph({ children: [...R(a, { bold: true }), ...R(b)], spacing: { after: 100, line: 288 },
  alignment: AlignmentType.JUSTIFIED, indent: { left: 360 } })));
C.push(tcap('Table 2. Where the last two rings read, by residue (D = 3m, 3m + 1, 3m + 2)'));
C.push(table(['D', 'p', 'f', 'ring D − 1: outer zero', 'ring D − 1 reads', 'ring D: inner zero', 'ring D reads'],
  [['3m', '2m + 1', '⅔', '2m − 1', '⌊(3m − 1)·⅔⌋ = 2m − 1', 'm', '⌊3m·⅓⌋ = m'],
   ['3m + 1', '2m + 1', '⅔', '2m', '⌊3m·⅔⌋ = 2m', 'm', '⌊(3m + 1)·⅓⌋ = m'],
   ['3m + 2', '2m + 3', '⅔ + 1/(6D)', '2m', '⌊(3m + 1)f⌋ = 2m', 'm + 1', '⌊D(⅓ + 1/(3D))⌋ = m + 1']],
  [820, 900, 1300, 1560, 1840, 1300, 1640], { size: 17 }));
C.push(after());
C.push(P('The law reads q_{D} at every depth from 13 to 119, all 107 of them. In residue 2 the sealed address reads q_{D} at all 36 depths 14, 17, …, 119, and the control with f = ⅔ differs from q_{D} at ring D and nowhere else at all 36, as sealed.', tag('computed'), ' For D = 8 to 12, explicit witnesses are listed in Appendix A. Figure 4 follows one ray, D = 40, ring by ring.'));
C.push(STATE('Corollary.', 'For every D ≥ 8 the profile 100 1^{D−5} 00 is read on an interval of positive width.', tag('proved', 'D ≥ 13'), tag('computed', 'D = 8 to 12')));
C.push(...FIG('figs/fig3_reader_path.png', 4, 'The ray of the depth-40 witness, ring by ring. Grey ticks are the zeros of the word under the ray, as fractions of its length; the dot is the bit the ray reads. Up to ring p − 1 the ray sits in the leading ones of the centre word, then just past its only zero. The address bit enters at p = 27; from there each ring doubles the ray’s position while the word’s outer zero climbs toward ⅔. They meet once: ring 39 reads its outer zero at ⅔, and ring 40 its inner zero at ⅓.'));

// ================= 9 =================
C.push(H1('9. What the arithmetic chose'));
C.push(P('Three features of the result were not put in. They came out of holding the end.'));
C.push(P('The witness approaches the seam as 2^{−2D/3}, while the region where the profile is impossible shrinks as 2^{−D} and the witness interval like a single ring-D slice, 2^{−D}/D, within a small factor (Figure 5). The profile is never where an argument at the seam looks for it, and it is always at the same fraction of the address depth.'));
C.push(P('The 3 in “modulo 3” is ½ ± ⅙. The doubling 2-cycle reads at ⅓ and ⅔, and cores are centred at ½. A core that reaches ⅓ and ⅔ has a half-width of one sixth of its word, and the square root in the triangular count turns that half-width into an address depth of one third. The three residues are the three ways ⌊2D/3⌋ can fall against the parity that keeps a core clean.'));
C.push(P('One condition appears in two places. A reader that sorts prefixes into classes can predict the next ring only if two prefixes in one class stay in one class under every extension. That is the Myhill–Nerode condition', tag('cited', 'Myhill 1957; Nerode 1958'), ', and the growth of the class counts in Section 5 is that condition failing for every small reader. In a separate computation the planar ring was treated as one section of a family of concentric shells, and a reader that records only the four-bit longitude prefix of a tilted section put two points in one class, 0000, that a quarter-turn of the section sends to 0001 and 1110.', tag('computed', 'reproduced by section_check.py'), ' The turn is reversible on the section and has no action on the reader’s classes. Both are the same requirement, that equivalence under the reader survive the operation, met once along a ray and once across sections. Nothing here extends the rings to a field in three dimensions; the section computation is coordinate geometry, and what is identified is the condition, not the objects.'));
C.push(...FIG('figs/fig4_scaling.png', 5, 'Scale of the witness, D = 13 to 119. The offset of u_{D} from the seam falls as 2^{−2D/3}, the edge of the excluded zone as 2^{−D}, and the width of K_{D} like one ring-D slice. The witness approaches the seam and never enters the zone where the profile is impossible.', 500));

// ================= 10 =================
C.push(H1('10. Ledger'));
C.push(tcap('Table 3. What stands, and on what'));
C.push(table(['Statement', 'Status', 'Scope'], [
  ['P is a fixed-point-free involution; 2^{L−1} pairs; 2^{⌈L/2⌉} palindromes', 'proved', 'every L'],
  ['Facing law P(r_{i}) = r_{N−1−i}; closed form equals centre insertion', 'proved; computed', 'every L; L = 1 to 16'],
  ['The pair readout x ⊕ P(x) is a palindrome', 'proved', 'every L'],
  ['Location in O(L), word at a position in O(L^{2})', 'proved; computed', 'L = 64 (π), L = 512'],
  ['Lemma A, the triangular count', 'proved; computed', 'every L; exhaustive L = 3 to 20'],
  ['Order within blocks (block law)', 'proved; computed', 'top quarter, L = 4 to 18'],
  ['Theorem C, clean cores', 'proved; computed', '1,579 of 1,579; L = 6 to 80, samples to 201'],
  ['Theorem D, the pad law', 'proved; computed', 'top quarter, L = 4 to 16'],
  ['No witness within 2^{−(D−2)} of the seam', 'proved; computed', 'large D; D = 8 to 22'],
  ['Theorem E, the witness law', 'proved; computed', 'every D ≥ 13; 107 of 107, D = 13 to 119'],
  ['Residue-2 address and its control', 'sealed; computed', '36 of 36, and 36 of 36'],
  ['q_{D} readable at every D ≥ 8', 'proved; computed', 'D ≥ 13; D = 8 to 12'],
  ['R_{d}, E_{d}, automaton sizes, 311 depth-11 classes', 'computed', 'd, H ≤ 16'],
  ['Regularity of the unbounded profile language', 'open', 'lower bound 312 and rising'],
  ['Every component of A(q_{D}) (2, 5, 5, 14, 22, 41, 66, 94, 160 for D = 8 to 16) by formula', 'open', 'one witness per depth is proved'],
  ['A map from a ring’s pair readouts to the next ring’s addresses, beyond the pad law', 'open', ''],
  ['The self-location window (5, 11, 13, 16, 25, 27, 32 for L = 2 to 8)', 'open', ''],
], [5160, 1700, 2500], { size: 17, keep: false }));
C.push(after());
C.push(box('Corrections logged on the way', [
  [...smb('One bit region, not one run. '), ...sm('An earlier statement put every unreadable extension’s parent inside one run of slices. The correct statement is that it lies inside the other bit’s region; 25 of 101 parents meet more than one run.')],
  [...smb('One address bit is enough in residue 2. '), ...sm('Depths 20 and 23 were reported to need a second address bit. They have no one-bit witness at phase exactly ⅓ or ⅔, which was all the scan tried; raised by a third of a ring-D slice, one bit carries every depth.')],
  [...smb('The nearest component is not the route. '), ...sm('Choosing the component of A(q_{D}) nearest the seam at each depth gave incoherent endpoints. The family is a route through the address, not a nearest point.')],
  [...smb('Half-open slices. '), ...sm('An interior test rejected witnesses that sit on the left end of a slice. Slices are half-open, so such a point is inside.')],
  [...smb('The hypothesis of Theorem C. '), ...sm('The second statement was first run with s = 0 at odd L, where offset 2 falls into the next block, and 40 checks failed. The hypothesis is s ≥ 2 in both parities; with it, 1,579 of 1,579.')],
  [...smb('Halving does not carry a witness. '), ...sm('Replacing δ by δ/2 does not carry a witness from depth D to depth D + 1. The tape has L·2^{L} slices, not 2^{L}, and the factor L breaks dyadic self-similarity.')],
  [...smb('Fourfold, not eightfold. '), ...sm('The excluded zone was first reported as eight times the centre cell, counting both sides of the seam. Ring 1 alone excludes the anticlockwise side, so the substantive widening is fourfold.')],
  [...smb('Tails belong to other maps. '), ...sm('A first-repeat scale of 2^{n/2} belongs to random maps that are not invertible. P is an involution and has no tails at any length. (Received from an independent review.)')],
]));
C.push(after());
C.push(H2('What this paper does not claim'));
C.push(P('Everything here is about one finite construction and what a ray reads from it. The ring is a bijection with an exact inverse, so locating a word in it is not inverting a one-way function, and nothing here bears on the preimage or collision resistance of any hash function. The planar ring is not claimed to be a section of any physical field; the shells-and-sections computation of Section 9 is coordinate geometry. Theorem E gives one interval per depth; the sets A(q_{D}) have many other components that it does not describe.'));
C.push(H2('The next stroke'));
C.push(P('Two routes are ready. The triangular law gives every word in the top quarter of every ring in closed form, so the full sets A(q_{D}), not one interval of each, can now be written as unions over blocks, and the component counts 2, 5, 5, 14, 22, 41, 66, 94, 160 are the first test of such a formula. And the class counts 1, 3, 14, 51, 175, 311 are the first test of whether the profile language is regular; an infinite family of pairwise separated prefixes, if there is one, will be built from the same blocks.'));
C.push(H2('Conclusion'));
C.push(P('No ring longer than 18 was built for this paper, and every number in it was read. A space of 2^{L} words cannot be held at any length that matters. It can be addressed, and addressing is enough. The top quarter of each ring is a triangular stack whose blocks are counted by the complement of a half-word; the core of each word widens as the logarithm of its distance from the seam and is carried unchanged into the ring two lengths on; and one ray, aimed by a single bit at two-thirds depth and a tail that cycles ⅔, ⅓, ⅔, reads at every depth a profile that the seam itself cannot. The thirds were not put in. They are ½ ± ⅙, and they came out of holding the end.'));
C.push(new Paragraph({ spacing: { before: 200, after: 140 }, alignment: AlignmentType.JUSTIFIED, children: [
  ...smb('Acknowledgment. '),
  ...sm('Computation and drafting were done with Claude (Anthropic) as a working partner. Several results here were first reached or checked in independent AI-assisted runs: the centre-cell exclusion, reachability of q_{D} through depth 16, the language counts at depths 13 and 14, the automaton sizes and the 311-class bound, the positive width of K_{D} and the address identities of Theorem E, a 512-bit round trip, and the tilted-section reader. Every number quoted was recomputed for this paper by the scripts of Appendix B.'),
] }));

// ================= references =================
C.push(H1('References'));
[
  'Flajolet, P., & Odlyzko, A. M. (1990). Random mapping statistics. In Advances in Cryptology: EUROCRYPT ’89, Lecture Notes in Computer Science 434 (pp. 329–354). Springer.',
  'Knuth, D. E. (2011). The Art of Computer Programming, Vol. 4A: Combinatorial Algorithms, Part 1. Addison-Wesley.',
  'Kulik, D. A. (2026). I Need That: The way home in a finite scope, and how a reader turns a search into a route. QuHarmonics Research Group.',
  'Kulik, D. A. (2026). Research record, § 135: Alternate routes in the nested-ring address. QuHarmonics Research Group, 19 October 2026.',
  'Myhill, J. (1957). Finite automata and the representation of events. WADD Technical Report 57-624, Wright-Patterson Air Force Base.',
  'Nerode, A. (1958). Linear automaton transformations. Proceedings of the American Mathematical Society, 9(4), 541–544.',
  'Rota, G.-C. (1964). On the foundations of combinatorial theory I: Theory of Möbius functions. Zeitschrift für Wahrscheinlichkeitstheorie und verwandte Gebiete, 2, 340–368.',
].forEach(r => C.push(new Paragraph({ spacing: { after: 80, line: 260 }, indent: { left: 360, hanging: 360 }, children: R(r, { size: 18 }) })));

// ================= appendix A =================
C.push(H1('Appendix A. Witnesses and intervals'));
C.push(P('Witnesses for D = 8 to 12, each checked by reading every ring at the stated angle. ATOM marks the midpoint of an exactly computed component of A(q_{D}); BIT and J2 mark addresses of the forms ½ + 2^{−p} + φ·2^{−(D−1)} and ½ + 2^{−(D−1)}(J + φ).'));
C.push(table(['D', 'method', 'angle u', 'profile read'], [
  ['8', 'ATOM', '15329/28672', '10011100'], ['9', 'ATOM', '4739/9216', '100111100'], ['10', 'ATOM', '98081/184320', '1001111100'],
  ['11', 'BIT, p = 8, φ = 1/3', '1549/3072', '10011111100'], ['12', 'J2, J = 10, φ = 1/3', '3103/6144', '100111111100']],
  [700, 2600, 2700, 3360], { size: 17 }));
C.push(after());
C.push(P('Intervals K_{D} from Theorem E, exact.'));
const KD = [
  ['13', '9', '2/3', '3085/6144', '26737/53248', '−17.29'],
  ['14', '11', '19/28', '114819/229376', '53309/106496', '−19.19'],
  ['15', '11', '2/3', '12301/24576', '82007/163840', '−18.91'],
  ['40', '27', '2/3', '412316866561/824633720832', '10995116441627/21990232555520', '−45.91'],
];
C.push(table(['D', 'p', 'f', 'left end', 'right end', 'log_{2} width'], KD, [600, 600, 800, 3100, 3260, 1000], { size: 16 }));
C.push(after());
C.push(P('For D = 119 (p = 81, f = 159/238 = ⅔ + 1/714):'));
C.push(mono('left  = 39544532874601247218888292753811177631 / 79089065749202494437776520086680502272', { size: 15 }));
C.push(mono('right = 19606112937827509125331170356931592271 / 39212225875655018250662308278270164992', { size: 15 }));
C.push(mono('log2 width = -127.46', { size: 15 }));
C.push(after());
C.push(P('Every K_{D} for D = 13 to 119 is in unified_certificate.json.'));

// ================= appendix B =================
C.push(H1('Appendix B. Scripts and their output'));
C.push(P('The scripts read the rings only through the O(L) location and word functions, except where a small ring is built for comparison. ringlib.py builds rings by the closed form. top_block_law.py checks Lemma A and the block law; theorem_C_D.py and recheck_C_and_512.py check Theorems C and D and run the π and 512-bit round trips; across_language.py recomputes the language through depth 16, and parent_runs.py counts the runs met by each unreadable extension’s parent; residue2_run.py verifies the seal, runs the sealed residue-2 law and its control, and runs Theorem E at every depth from 13 to 119; section_check.py reproduces the tilted-section reader; figures.py draws the figures. The earlier scripts witness_Kd.py, Kd_law.py, Kd_certificate.py and obstruction_check.py supply the reader, the residue-0 and residue-1 law, the witnesses for D = 8 to 40 and the excluded zone. Their output follows, unedited except for headings.'));
fs.readFileSync('appendix_outputs.txt', 'utf8').split('\n').forEach(line => {
  C.push(mono(line, { size: 12, color: line.startsWith('==') ? '2B6CB0' : '1A202C', bold: line.startsWith('==') }));
});

// ================= appendix C =================
C.push(H1('Appendix C. The sealed prediction'));
C.push(P('The text below was written after the derivation of Section 7.3 and before any computation of the residue-2 address. Its SHA-256 digest is'));
C.push(mono(fs.readFileSync('residue2_prediction.sha256', 'utf8').split(/\s+/)[0], { size: 15, bold: true }));
C.push(after());
fs.readFileSync('residue2_prediction.txt', 'utf8').split('\n').forEach(line => C.push(mono(line, { size: 13 })));
C.push(after());
C.push(P('residue2_run.py recomputes the digest and stops if it does not match before it runs the check.'));

const doc = new Document({
  creator: 'Dean A. Kulik', title: 'Only Addressable',
  description: 'The ring of all binary words: exact location without enumeration, a triangular top, and a law in thirds for what one ray reads',
  styles: { default: { document: { run: { font: FONT, size: 22 } } } },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [
      new TextRun({ text: 'Kulik · Only Addressable · ', font: FONT, size: 16, color: '718096' }),
      new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 16, color: '718096' })] })] }) },
    children: C,
  }],
});
Packer.toBuffer(doc).then(buf => { fs.writeFileSync('Only_Addressable_Kulik_2026.docx', buf); console.log('written', buf.length); });
