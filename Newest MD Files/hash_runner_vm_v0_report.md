# Hash Runner VM v0 — Multi-Runtime Digest Execution Scan

## Scope

This run treats each SHA-256 digest as a 32-byte program image and executes/decompiles it through the machine structures available in this environment.

This is not a claim that a SHA digest has native executable meaning. It is a controlled shape probe: the digest bytes are interpreted under many runtimes, then the invariant behavior signatures are compared.

The project premise used here is:

$$
H(i)=F_{M(i)}(H(i-1))
$$

meaning the input configures the path through the SHA field, and the digest is the terminal residue of that path.

## Inputs Tested

17 source inputs were tested:

raw_dos_hello_nop55, ascii_bitstring_of_dos, text_plain_hello, instruction_text_print_exit, tone_sine_64, tone_square_64, tone_saw_64, tone_triangle_64, bytes_zero_55, bytes_nop_55, bytes_ff_55, bytes_ascending_55, x86_infinite_loop, x86_ret_nops, x86_int3_nops, text_calm_instruction, text_hard_instruction

These include:
- the raw 55-byte DOS `Hello!$` executable with NOP field,
- the ASCII bitstring description of that binary,
- textual instructions,
- calm/hard instruction tones,
- raw byte fields,
- synthetic PCM-like tones,
- small opcode fragments.

## Runtime Families Scanned

Native architecture/object decoders:
- x86_32
- x86_64
- armv7
- thumbv7 object mode
- aarch64
- riscv32
- riscv64
- mips32 big-endian
- ppc32 big-endian
- AVR

Symbolic / bytecode / small-machine scans:
- JVM bytecode subset
- WASM opcode subset
- CIL bytecode subset
- MOS 6502 subset

## Primary Target: Raw DOS Hello/NOP Program

Input length:

$$
55\text{ bytes}
$$

SHA-256:

```text
e079e052b115f0bd7a1f7e4b76b896ecff094435418389aec7c54e26929a3b27
```

### Runtime score table

| runtime      | runtime_kind     |   instructions |   valid_like |   unknown |   word_data |   control_count |   memory_count |   io_fault_count | first_mnemonic   | top_mnemonics                               |
|:-------------|:-----------------|---------------:|-------------:|----------:|------------:|----------------:|---------------:|-----------------:|:-----------------|:--------------------------------------------|
| x86_32       | native_arch      |             13 |           13 |         0 |           0 |               3 |              7 |                3 | loopne           | loopne:2,movl:2,movb:1,lock:1,jbe:1         |
| x86_64       | native_arch      |             12 |           12 |         0 |           0 |               3 |              6 |                2 | loopne           | loopne:2,movl:2,movb:1,lock:1,jbe:1         |
| armv7        | native_arch      |              8 |            7 |         1 |           0 |               1 |              4 |                1 | rscpl            | rscpl:1,ldcllt:1,blmi:1,ldc:1,strblo:1      |
| thumb        | native_arch      |              8 |            7 |         1 |           0 |               1 |              4 |                1 | rscpl            | rscpl:1,ldcllt:1,blmi:1,ldc:1,strblo:1      |
| aarch64      | native_arch      |              8 |            0 |         0 |           8 |               0 |              0 |                0 | .word            | .word:8                                     |
| riscv32      | native_arch      |             13 |           10 |         3 |           0 |               0 |              7 |                3 | flw              | <unknown>:3,lw:2,fsd:2,flw:1,addi:1         |
| riscv64      | native_arch      |             13 |           10 |         3 |           0 |               0 |              6 |                3 | ld               | <unknown>:3,lw:2,fsd:2,ld:1,addi:1          |
| mips32_be    | native_arch      |              8 |            4 |         4 |           0 |               1 |              2 |                4 | sc               | <unknown>:4,sc:1,jalx:1,lwc1:1,lbu:1        |
| ppc32_be     | native_arch      |              8 |            6 |         2 |           0 |               1 |              2 |                2 | <unknown>        | <unknown>:2,sth:1,rldic.:1,andis.:1,bta:1   |
| avr          | native_arch      |             15 |           14 |         1 |           0 |               0 |              2 |                3 | andi             | out:2,eor:2,andi:1,subi:1,cp:1              |
| jvm_bytecode | bytecode_or_8bit |             32 |            6 |        26 |           0 |               2 |              3 |               26 | ?                | ?:26,return:1,iload:1,iand:1,invokestatic:1 |
| wasm_opcode  | bytecode_or_8bit |             32 |            1 |        31 |           0 |               0 |              1 |               31 | ?                | ?:31,i32.const:1                            |
| cil_bytecode | bytecode_or_8bit |             32 |            3 |        29 |           0 |               0 |              2 |               30 | ?                | ?:29,ldc.i4.m1:1,throw:1,ldloc.3:1          |
| mos6502      | bytecode_or_8bit |             32 |            1 |        31 |           0 |               1 |              0 |               31 | ?                | ?:31,BEQ:1                                  |

## Raw Target: Important Cross-Runtime Shape

### x86 shape

The raw executable hash begins as:

```asm
       0: e0 79                        	loopne	0x7b <_start+0x7b>
       2: e0 52                        	loopne	0x56 <_start+0x56>
       4: b1 15                        	movb	$0x15, %cl
       6: f0                           	lock
       7: bd 7a 1f 7e 4b               	movl	$0x4b7e1f7a, %ebp       # imm = 0x4B7E1F7A
       c: 76 b8                        	jbe	0xffffffc6 <_start+0xffffffffffffffc6>
       e: 96                           	xchgl	%esi, %eax
       f: ec                           	inb	%dx, %al
      10: ff 09                        	decl	(%ecx)
      12: 44                           	incl	%esp
      13: 35 41 83 89 ae               	xorl	$0xae898341, %eax       # imm = 0xAE898341
      18: c7 c5 4e 26 92 9a            	movl	$0x9a92264e, %ebp       # imm = 0x9A92264E
```

Shape:

$$
\boxed{\text{loop gate} \rightarrow \text{counter seed} \rightarrow \text{lock/boundary} \rightarrow \text{memory/I/O probe}}
$$

### Ring-fold branch targets

For the x86 interpretation:

| Source | Instruction | Native target | 32-byte ring target |
|---:|---|---:|---:|
| 0 | `loopne 0x7b` | 123 | 27 |
| 2 | `loopne 0x56` | 86 | 22 |
| 12 | `jbe 0xffffffc6` | -58 / 0xffffffc6 | 6 |

So under a ring VM:

$$
0\to 27,\qquad 2\to22,\qquad 12\to6.
$$

### ARM/RISC/AVR contrast

The same digest under ARM, RISC-V, MIPS, PPC, and AVR does not preserve x86 mnemonics, but it still tends to decode as control/memory/probe structure rather than clean arithmetic-only code.

Examples:

```asm
ARMv7:
       0: 52e079e0     	rscpl	r7, r0, #224, #18
       4: bdf015b1     	ldcllt	p5, c1, [r0, #708]!
       8: 4b7e1f7a     	blmi	0x1f87df8 <_start+0x1f87df8> @ imm = #0x1f87de8
       c: ec96b876     	ldc	p8, c11, [r6], {118}
      10: 354409ff     	strblo	r0, [r4, #-0x9ff]
      14: ae898341     	cdpge	p3, #0x8, c8, c9, c1, #0x2
      18: 264ec5c7     	strbhs	r12, [lr], -r7, asr #11
      1c: 273b9a92     	<unknown>

RISC-V32:
       0: 79e0         	flw	fs0, 0x74(a1)
       2: 52e0         	lw	s0, 0x64(a3)
       4: 15b1         	addi	a1, a1, -0x14
       6: bdf0         	fsd	fa2, 0xf8(a1)
       8: 1f7a         	c.slli	t5, 0x3e
       a: 4b7e         	lw	s6, 0xdc(sp)
       c: b876         	fsd	ft9, 0x30(sp)
       e: ec96         	fsw	ft5, 0x58(sp)

AVR:
       0: e0 79        	andi	r30, 0x90
       2: e0 52        	subi	r30, 0x20
       4: b1 15        	cp	r27, r1
       6: f0 bd        	out	0x20, r31
       8: 7a 1f        	adc	r23, r26
       a: 7e 4b        	sbci	r23, 0xbe
       c: 76 b8        	out	0x6, r7
       e: 96 ec        	ldi	r25, 0xc6
      10: ff 09        	sbc	r31, r15
      12: 44 35        	cpi	r20, 0x54
      14: 41 83        	std	Z+1, r20
      16: 89 ae c7 c5  	<unknown>
```

## Best Runtime by Input

This table chooses the runtime with the highest crude runnable-shape score:

$$
\text{score}=
\text{valid-like}
+0.7\cdot\text{control}
+0.2\cdot\text{memory}
-0.7\cdot\text{unknown}
-0.7\cdot\text{word-data}
-0.3\cdot\text{bad}
$$

| input                       |   input_len | digest                                                           | runtime   | first_mnemonic   |   valid_like |   control_count |   memory_count |   io_fault_count |   runnable_score |
|:----------------------------|------------:|:-----------------------------------------------------------------|:----------|:-----------------|-------------:|----------------:|---------------:|-----------------:|-----------------:|
| ascii_bitstring_of_dos      |         440 | 863a88b5945884e84b6b6bd230b484e6fc73574b5c9fb132a9fb031b03253c89 | x86_32    | xchgb            |           13 |               1 |              7 |                2 |             14.4 |
| bytes_ascending_55          |          55 | 463eb28e72f82e0a96c0a4cc53690c571281131f672aa229e0d45ae59b598b59 | avr       | cpi              |           16 |               1 |              3 |                0 |             17.3 |
| bytes_ff_55                 |          55 | aadaed00a3c5fbb8072ae7f1984ba8199fbe5272de427d11eaf31583af37db51 | avr       | rcall            |           14 |               2 |              1 |                3 |             14.9 |
| bytes_nop_55                |          55 | db045faace9a73f328bb8f7ef1c9f1c2feed0ea65a768ab49f39ea1350774ff5 | x86_32    | fildl            |           15 |               2 |              5 |                3 |             16   |
| bytes_zero_55               |          55 | 02779466cdec163811d078815c633f21901413081449002f24aa3e80f0b88ef7 | avr       | andi             |           14 |               1 |              3 |                2 |             14.6 |
| instruction_text_print_exit |          66 | 8d05612b3145893782a412914b2cf4c45ecfec613eb190db1aeda36e286ddae2 | avr       | cpc              |           14 |               0 |              3 |                2 |             13.9 |
| raw_dos_hello_nop55         |          55 | e079e052b115f0bd7a1f7e4b76b896ecff094435418389aec7c54e26929a3b27 | x86_32    | loopne           |           13 |               3 |              7 |                3 |             16.5 |
| text_calm_instruction       |          36 | 528a7f0c1665b719810202954b30afdf358cb9b71f203cf5d957c8e37718ba63 | avr       | std              |           14 |               1 |              3 |                2 |             14.6 |
| text_hard_instruction       |          42 | cf0a6506ea3e224af377d9301adb13e4ab634904389b925b7f788c07a3b0b614 | avr       | sbc              |           16 |               0 |              1 |                1 |             16.2 |
| text_plain_hello            |           6 | 334d016f755cd6dc58c53a86e183882f8ec14f52fb05345887c8a5edd42c87b7 | avr       | sbci             |           16 |               0 |              5 |                1 |             17   |
| tone_saw_64                 |          64 | 3f9f32d2261ccaa2aff69d8348e605ee3f2d8dd645941592095cc6a6f6729d1f | x86_32    | aas              |           14 |               0 |              3 |                2 |             14.6 |
| tone_sine_64                |          64 | cd03a5f3191cc514a0d8d39b9f08c7ef0059524ab9033db82b51947caab5f68d | x86_32    | int              |           14 |               1 |              5 |                3 |             15   |
| tone_square_64              |          64 | eeaed4f1e83464dc9ce347241abcf3e18d79a91a6ca002412e04816ba994c2d7 | riscv32   | fsd              |           13 |               0 |              8 |                1 |             13.9 |
| tone_triangle_64            |          64 | b897433712909203ca7b12aef52406ee8a12eb5b57ae0a473f88f0e9a402eedd | x86_32    | movl             |           16 |               3 |              4 |                1 |             18.9 |
| x86_infinite_loop           |          55 | de4c5e300d9c98be56fe9369545a4199b0624dc11a55a53db39eca765e5a6627 | riscv64   | lw               |           13 |               1 |              7 |                1 |             14.4 |
| x86_int3_nops               |          55 | bfcf02e2e00b1d0593c559a7cedc65c93024a149f3eac7b4eab8eabf38720eec | avr       | rjmp             |           14 |               0 |              3 |                4 |             13.9 |
| x86_ret_nops                |          55 | c59cc8b9cd05c52da73dccee4d9a1413258be1cad119a29fa0d4e0c9915bde67 | riscv32   | <unknown>        |           14 |               2 |              5 |                1 |             15.7 |

## Observations

### 1. Raw executable digest is not random under x86 shape

The raw executable hash starts with two loop gates and then hits a lock/boundary byte.

$$
\boxed{\text{loop} \oplus \text{counter} \oplus \text{boundary} \oplus \text{probe}}
$$

This echoes the source object:

$$
\boxed{\text{execute} \oplus \text{print} \oplus \text{exit} \oplus \text{NOP field}}
$$

Not as literal text, but as behavior grammar.

### 2. Representation changes the program body

The ASCII bitstring and the raw bytes produce entirely different SHA digests. This confirms:

$$
\boxed{\text{representation is part of the executable shape}}
$$

Raw bytes are not equivalent to ASCII glyphs describing bytes.

### 3. Different inputs choose different “best” runtime surfaces

- Tone / synthetic continuous fields often scored best in x86 or RISC-style surfaces.
- Text and dense byte fields often scored best in AVR because many bytes map to compact 8-bit instructions.
- The raw DOS program specifically scored best on x86_32, matching its source ancestry.

### 4. AArch64 mostly rejects this 32-byte object

For the raw digest, AArch64 emitted 8 `.word` entries and no recognized instructions. That is a rejection boundary: the same byte string does not become lawful code under every fixed-width ISA.

## Stable Collapse

The digest is not a universal executable. It is a frozen 32-byte residue.

When we run it through many machines, the useful object is not any one disassembly. It is:

$$
\boxed{\mathcal B(H)=
(\text{accepted runtimes},\text{control gates},\text{boundary faults},\text{memory probes},\text{ring targets})}
$$

For the raw DOS Hello/NOP input:

$$
\boxed{\mathcal B(H)=\text{loop/counter/boundary/probe}}
$$

That is the behavior signature.

## Next Step

Hash many members of one controlled family:

$$
\text{DOS print/exit/string/NOP variants}
$$

Then train:

$$
\mathcal B(H)\rightarrow\text{source shape class}
$$

not:

$$
H\rightarrow M
$$

This is the proper Hash Runner VM path.
