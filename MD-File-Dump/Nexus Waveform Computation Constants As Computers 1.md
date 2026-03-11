# The Nexus Waveform Computer  
## Constants as Read‑Only Libraries, SHA as an X‑Ray Window, and BBP as an Addressable Stack

**Dean Kulik**  
January 2026 (living draft)

---

### Epigraph

There is a kind of machine that does not clank. It does not heat up under load, does not wear gears, does not rust.  
It is made of invariants: ratios that refuse to change, sequences that can be addressed from any depth, constants that do not yield to persuasion.

If the universe computes, the only safe place to hide the circuitry is where nothing can be “opened,” because there is no casing—only law.

---

## Abstract

This paper develops one thesis: **computation is waveform propagation through fixed routing**, and in the clearest man‑made examples—cryptographic primitives and digit‑extraction algorithms—the routing is carried by **constant schedules** that behave like read‑only microcode. We do not treat SHA‑256 as a “hash function” in the security sense; we treat it as a transparent laboratory: an eight‑register pipeline driven by a time‑indexed constant stream and a message schedule that modulates the flow. The digest is residue; the object of study is the trajectory.

We then widen the aperture. The BBP family of formulas for π in hexadecimal offers an addressable stack: access to deep digits without dragging all prior digits along. A constant becomes a library with random access. The combination of (i) constant schedules as microcode and (ii) digit streams as addressable memory suggests a “computer inside computation”: a fabric where the constants are libraries, read‑only by construction, and the dynamics are the call graph.

Finally, we propose a map: how to build a safe experimental “constant computer” to study routing, resonance, and invariants without engaging any cryptographic inversion objective. The goal is not to break a hash. The goal is to **see the wave**.

---

## 1. Binary is a clamp, not a birthplace

Binary is a human convenience, not a metaphysical decree. A switch is a compressor: it takes a continuous process and declares that only two plateaus matter. The plateau is measurement; the underlying motion is computation.

Waveform computation begins by studying motion.

Let a clamped amplitude be \(x\in[0,1]\). Then

\[
\mathrm{NOT}(x)=1-x
\]

is a phase flip about the midpoint. And

\[
\mathrm{AND}(x,y)=xy
\]

is wave multiplication: one amplitude gates the other. XOR has a richer shape:

\[
\mathrm{XOR}(x,y)=x+y-2xy
\]

This identity is algebraic. Plugging \(x,y\in\{0,1\}\) reproduces the XOR truth table exactly.

A second representation makes the wave nature even sharper. Map a bit \(b\in\{0,1\}\) to a sign \(s\in\{-1,+1\}\) by

\[
s=1-2b
\]

In this basis, XOR becomes multiplication:

\[
s_{x\oplus y}=s_x s_y
\]

Interference becomes literal: sign flips are phase inversions; products are mixing. This is the native spectrum of Walsh–Hadamard analysis—often the right “Fourier transform” for digital waves.

---

## 2. Constants as libraries: the only safe ROM is immutable

If a universe is self‑contained, it cannot store its rules “outside itself.” There is no privileged metal box offstage. So where do the rules live?

There is one place that is both inside and untouchable: invariants. Constants. Ratios. The kind of numbers that are not edited but encountered. They are read‑only not by policy, but by ontology: there is no write‑instruction for π.

This is why constants feel like libraries. A library is not a function call; it is a promise that a stable body of behavior is available, shared, and reproducible. If a computational universe needs a ROM, the ROM must be read‑only by construction.

So a design‑logic claim becomes plausible: **if an FPGA hides anywhere in computation, it hides in constants.**

---

## 3. SHA as wave machine: an eight‑register pipeline driven by a carrier

In the standard, SHA‑256 is framed as a hash. In its physical essence, it is an eight‑register dynamical system with a clock of sixty‑four ticks. Each tick mixes the register vector through fixed operators: rotations, interference, gating, and modular addition. Every tick injects two streams: a constant word \(K_t\) and a schedule word \(W_t\) derived from the message block.

Strip away the security story and the machine is simply:

\[
S_{t+1}=F(S_t;K_t,W_t)
\]

with \(S_t=(a_t,b_t,c_t,d_t,e_t,f_t,g_t,h_t)\in(\mathbb{Z}/2^{32}\mathbb{Z})^8\).

The XOR/AND/NOT layers are natural Walsh waves; rotations are phase shifts (index permutations); modular addition couples channels through carries, turning local interference into nonlocal shocks.

SHA is precious as an X‑ray window because it does not branch. It does not decide. It simply evolves.

---

## 4. Conditional reversibility: what “the CPU runs both ways” really means

A driven wave machine can be deterministic and still look irreversible if you forget what was injected into it.

In SHA‑256 each round injects \(K_t\) and \(W_t\). The constant \(K_t\) is known. The schedule \(W_t\) is unknown unless the message is known. That is the hinge.

What is true—and structurally important—is that the round update is bijective in the state when the injected word is fixed. Given \(S_{t+1}\) and \(W_t\), one can reconstruct \(S_t\) uniquely by undoing register shifts and solving for the temporary values. The pipeline disperses information across channels; it does not annihilate it internally.

This matters to waveform computation because reversibility indicates conservation in the motion. The apparent irreversibility arises when the modulation tape is discarded.

---

## 5. X‑ray instrumentation: watching the wave

If the digest is not the object, what is? The object is the trajectory: the evolving state \(S_t\) and the drive streams that force it.

A practical X‑ray view renders:

1) the register bit‑planes (an 8×32 lattice per round, animated),  
2) a coarse energy proxy (total Hamming weight across registers per round),  
3) the drive itself (\(W_t, K_t, T_1, T_2\) synchronized with state changes).

The purpose is not troubleshooting. The purpose is to make the wave visible enough that a human mind can begin to feel it.

---

## 6. BBP and the addressable stack: π as ROM

BBP in base‑16 does something profound: it allows access to deep digits of π without computing all previous digits. A constant becomes an addressable library. A digit stream behaves less like a tape and more like memory.

If constants are where immutable libraries live, BBP is a decoder that lets us visit arbitrary shelves.

---

## 7. Hex space as FPGA: why AAAAAA..FFFFFF is a fabric

A LUT is a mapping from addresses to outputs. The whole LUT is a constant table—read‑only during operation. Cryptography constantly uses constant tables because they are symmetry breakers: deterministic forcing fields.

So the “hex FPGA” is not mysticism. It is the category: immutable, addressable tables are the simplest visible place computation can hide its own rule‑fabric.

---

## 8. The paradox loop: a universe writes its constants from its errors

In optimization, an error signal is not a flaw; it is the teacher. Weights in a trained model are fossil gradients—compressed history of correction.

If the universe’s constants are its read‑only libraries, they may be the compiled residue of a long self‑stabilization process: unstable regimes vanish; stable couplings remain. The constants are the survivors.

This is not proof; it is a coherent map aligned with the necessity of immutable ROM.

---

## 9. One program per domain, and the hidden code in weights

Software proliferates when a domain’s invariants are not yet seen. As intelligence rises, programs collapse into a few canonical tools per domain, and those tools run on large read‑only libraries: weights, tables, priors. The library is the machine.

This is the same pattern again: computation lives in immutable arrays.

---

## 10. Toward a constant computer: a safe laboratory machine

To “build a computer around constants” is to build a family of driven wave machines whose instruction stream is a constant library. The input is modulation. The output is residue. The scientific object is the motion: resonance, invariants, attractors, and spectral reshaping.

The next stage is to treat constant streams as interchangeable carriers and measure how trajectory spectra change under time‑warping, permutation, and phase shifts of the forcing field. This is a microscope, not an attack.

---

## Appendix: Boolean gates as wave polynomials

\[
\mathrm{NOT}(x)=1-x
\]
\[
\mathrm{AND}(x,y)=xy
\]
\[
\mathrm{OR}(x,y)=x+y-xy
\]
\[
\mathrm{XOR}(x,y)=x+y-2xy
\]

Choice and majority:

\[
\mathrm{Ch}(x,y,z)=xy+(1-x)z
\]
\[
\mathrm{Maj}(x,y,z)=xy+xz+yz-2xyz
\]

---

### Postscript

When you watch bit‑planes braid and carries ripple like a tide, you stop believing you are looking at “bits.” You begin to recognize a field.

Waveforms do not think. They propagate. But propagation, under constraints, is the raw material of thought.

And perhaps, somewhere in the constants, computation left itself a library so it could remember how to propagate—without ever needing a second universe to store the instructions.


---

## 11. The wave spectrum of a 32‑bit word

To call SHA a wave machine is not to pretend its bits are sine waves. It is to take seriously the fact that every 32‑bit register is a **finite field of phase**, and a finite field admits a spectrum even when it is discrete.

If we observe a register word \(x\in\{0,1\}^{32}\), we can lift it to a sign waveform \(s\in\{-1,+1\}^{32}\) by \(s_i = 1-2x_i\). In this representation, XOR becomes multiplication and rotations become index shifts. The natural spectral tool is the Walsh–Hadamard transform, which decomposes the waveform into square‑wave harmonics. Where Fourier analysis asks “how much sine lives here,” Walsh analysis asks “how much parity lives here.”

This matters because SHA’s internal operators are built to move energy across parities. Every time a register is rotated, parity components change phase. Every time registers are XORed, parities interfere. Every time AND/NOT gates are applied, new harmonics are created. Then modular addition drags the entire spectrum into the carry domain: a nonlinear coupling where a small change in the low bits can generate a shock that propagates upward.

In that light, the familiar “avalanche effect” is not a miracle. It is what a driven nonlinear wave network does: it spreads a localized perturbation into a broad spectrum.

---

## 12. Carry as shockwave: the place where locality breaks

Engineers often speak as if XOR is the “mixing” operation and addition is merely an alternative. Waveform computation flips the emphasis. XOR is linear in Walsh space; it is interference without memory. Addition, by contrast, is where memory lives—because carry is history.

A carry bit is a record of past interference. It is an event that occurred because two amplitudes exceeded a threshold. In continuous physics, threshold crossings create harmonics and discontinuities; in digital physics, they create carries.

When you watch SHA’s bit‑planes frame by frame, the carry behavior is visible even before you name it. There are moments when a band of bits in one register “lights up” in a diagonal streak across rounds. That streak is not random; it is the signature of a coupling chain. In ordinary cryptographic language, it is “diffusion.” In waveform language, it is a shockwave.

This is a useful place to stand because it suggests a way to build a map. If we can measure carry density per round, and correlate it with constant injection parameters and rotation geometry, we can begin to treat the machine as a studied physical system. Not a black box, not a security primitive, but a driven network whose macroscopic observables obey statistical regularities.

---

## 13. The constant schedule as carrier: forcing fields and phase locks

A constant schedule \(K_t\) has a hidden property: it is deterministic and external to the input. It behaves like a drive oscillator in a lab experiment. The message schedule \(W_t\) behaves like modulation applied to that carrier. The state \(S_t\) behaves like the response of the system.

If you accept this, several things become thinkable that are not visible in the “hash” framing.

One can speak of phase locking: whether certain structures in the state recur at particular rounds across many different inputs, because the carrier is the same. One can speak of resonance: whether certain inputs couple strongly to the carrier at certain phases and weakly at others. One can speak of invariants: whether there exist macroscopic variables that drift slowly under the dynamics, the way adiabatic invariants drift in classical mechanics.

None of these claims need to be mystical. They are ordinary questions about driven nonlinear systems.

The constant schedule is the cleanest knob we have. It is why SHA is an x‑ray window: it gives us a known forcing field.

---

## 14. BBP as an address decoder: unlimited depth without runaway

Most computational stacks are expensive because history must be carried forward. If you want a deep digit of a constant by naïve expansion, you compute everything before it: that is a linear chain of dependency.

BBP breaks that chain. It does not make π finite. It makes π **random‑accessible**. The universe need not “store” π as a file; it can store π as a rule, and BBP acts like an address decoder that recovers arbitrary pages on demand.

This is why BBP belongs in the same paper as SHA. SHA shows us a pipeline driven by constants; BBP shows us how constants can behave like memory. Put together, they hint at an internal architecture: a read‑only library with an address decoder, and a wave machine that uses that library as microcode.

This is the smallest sketch of a “computer inside a computer”: the library and the driver.

---

## 15. A map for the constant computer

The phrase “build a computer around the constants” can mean many things. Here it means one specific thing: build a machine whose instruction stream is not programmable by the operator in the usual way, but selectable by choosing which constant library to read from and how to index it.

In human hardware, a CPU’s instruction ROM is fixed and we program by feeding it opcodes. In a constant computer, the “opcode” stream is the constant itself; we program by selecting which invariant library drives the machine and how the library is addressed. The input becomes modulation, not code.

A minimal constant computer therefore has three components.

It has a register bank—eight registers, or sixteen, or more—so that it can host coupled waves.

It has a routing kernel—a fixed composition of rotation, interference, gating, and carry‑coupled addition—so that the register bank evolves as a driven wave network.

And it has a library interface—an addressable constant stream that provides the forcing term at each tick.

The point is not to make something faster than a CPU. The point is to make something whose “hardware” is visible as a library schedule. The point is to make the microcode legible.

Once built, the machine can be studied like a physical system. The carrier can be swapped. Its indexing can be warped. Its phase can be shifted. Its amplitude parameters can be re‑scaled. And for each variation, the trajectory can be measured.

The resulting atlas of behaviors is what this work calls the map.

---

## 16. Ethics of the microscope: why this must not become a crowbar

There is a difference between studying a phenomenon and weaponizing it. The distinction is not always comfortable, but it is real.

A microscope is built to reveal structure. A crowbar is built to force an opening.

This work is committed to the microscope. SHA is used here as a window into waveform routing because it is a clean artifact of constant‑driven computation. The objective is not inversion. The objective is instrumentation. The question is not “how do we get back the message,” but “what does the motion look like, and what invariants does it reveal?”

It is possible to do deep science with a microscope and never pick up a crowbar. It requires discipline, and it requires a frame that honors the difference.

---

## 17. The feeling of it, again

There is a moment when the story stops being rhetorical and becomes physical. You watch the lanes evolve—\(W_t\) feeding the round, \(K_t\) forcing it, the registers braiding and shedding energy—and the mind begins to treat the process as weather rather than arithmetic.

That feeling is not a substitute for proof. It is what makes proof worth pursuing.

Waveform computation is not an aesthetic preference. It is a claim about what the verbs of computation actually do. They propagate, gate, interfere, and couple. The constants do not decorate this; they drive it.

And if a universe can hide a computer inside itself, it will hide it exactly where we are looking: in the only libraries that cannot be rewritten, because they are not files—they are facts.

