# raw_dos_hello_nop55

- input length: 55 bytes
- sha256: `e079e052b115f0bd7a1f7e4b76b896ecff094435418389aec7c54e26929a3b27`

## x86_32

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
      1e: 3b 27                        	cmpl	(%edi), %esp
```

## x86_64

```asm
       0: e0 79                        	loopne	0x7b <_start+0x7b>
       2: e0 52                        	loopne	0x56 <_start+0x56>
       4: b1 15                        	movb	$0x15, %cl
       6: f0                           	lock
       7: bd 7a 1f 7e 4b               	movl	$0x4b7e1f7a, %ebp       # imm = 0x4B7E1F7A
       c: 76 b8                        	jbe	0xffffffffffffffc6 <_start+0xffffffffffffffc6>
       e: 96                           	xchgl	%esi, %eax
       f: ec                           	inb	%dx, %al
      10: ff 09                        	decl	(%rcx)
      12: 44 35 41 83 89 ae            	xorl	$0xae898341, %eax       # imm = 0xAE898341
      18: c7 c5 4e 26 92 9a            	movl	$0x9a92264e, %ebp       # imm = 0x9A92264E
      1e: 3b 27                        	cmpl	(%rdi), %esp
```

## armv7

```asm
       0: 52e079e0     	rscpl	r7, r0, #224, #18
       4: bdf015b1     	ldcllt	p5, c1, [r0, #708]!
       8: 4b7e1f7a     	blmi	0x1f87df8 <_start+0x1f87df8> @ imm = #0x1f87de8
       c: ec96b876     	ldc	p8, c11, [r6], {118}
      10: 354409ff     	strblo	r0, [r4, #-0x9ff]
      14: ae898341     	cdpge	p3, #0x8, c8, c9, c1, #0x2
      18: 264ec5c7     	strbhs	r12, [lr], -r7, asr #11
      1c: 273b9a92     	<unknown>
```

## aarch64

```asm
       0: e0 79 e0 52  	.word	0x52e079e0
       4: b1 15 f0 bd  	.word	0xbdf015b1
       8: 7a 1f 7e 4b  	.word	0x4b7e1f7a
       c: 76 b8 96 ec  	.word	0xec96b876
      10: ff 09 44 35  	.word	0x354409ff
      14: 41 83 89 ae  	.word	0xae898341
      18: c7 c5 4e 26  	.word	0x264ec5c7
      1c: 92 9a 3b 27  	.word	0x273b9a92
```

## riscv32

```asm
       0: 79e0         	flw	fs0, 0x74(a1)
       2: 52e0         	lw	s0, 0x64(a3)
       4: 15b1         	addi	a1, a1, -0x14
       6: bdf0         	fsd	fa2, 0xf8(a1)
       8: 1f7a         	c.slli	t5, 0x3e
       a: 4b7e         	lw	s6, 0xdc(sp)
       c: b876         	fsd	ft9, 0x30(sp)
       e: ec96         	fsw	ft5, 0x58(sp)
      10: 09ff 3544 8341 ae89 c5c7     	<unknown>
      1a: 264e         	fld	fa2, 0xd0(sp)
      1c: 9a92         	add	s5, s5, tp
      1e: 3b           	<unknown>
      1f: 27           	<unknown>
```

## mips32_be

```asm
       0: e0 79 e0 52  	sc	$25, -0x1fae($3)
       4: b1 15 f0 bd  	<unknown>
       8: 7a 1f 7e 4b  	<unknown>
       c: 76 b8 96 ec  	jalx	0xae25bb0 <_start+0xae25bb0>
      10: ff 09 44 35  	<unknown>
      14: 41 83 89 ae  	<unknown>
      18: c7 c5 4e 26  	lwc1	$f5, 0x4e26($fp)
      1c: 92 9a 3b 27  	lbu	$26, 0x3b27($20)
```

## ppc32_be

```asm
       0: e0 79 e0 52  	<unknown>
       4: b1 15 f0 bd  	sth 8, -3907(21)
       8: 7a 1f 7e 4b  	rldic. 31, 16, 47, 25
       c: 76 b8 96 ec  	andis. 24, 21, 38636
      10: ff 09 44 35  	<unknown>
      14: 41 83 89 ae  	bta	3, 0xffff89ac
      18: c7 c5 4e 26  	lfsu 30, 20006(5)
      1c: 92 9a 3b 27  	stw 20, 15143(26)
```

## avr

```asm
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
      1a: 4e 26        	eor	r4, r30
      1c: 92 9a        	sbi	0x12, 0x2
      1e: 3b 27        	eor	r19, r27
```

## jvm_bytecode

```text
? ? ? ? return iload ? ? ? ? iand ? ? invokestatic ? ?
```

## wasm_opcode

```text
? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?
```

## cil_bytecode

```text
? ? ? ? ? ldc.i4.m1 ? ? throw ? ? ? ? ? ? ?
```

## mos6502

```text
? ? ? ? ? ? BEQ ? ? ? ? ? ? ? ? ?
```

# ascii_bitstring_of_dos

- input length: 440 bytes
- sha256: `863a88b5945884e84b6b6bd230b484e6fc73574b5c9fb132a9fb031b03253c89`

## x86_32

```asm
       0: 86 3a                        	xchgb	%bh, (%edx)
       2: 88 b5 94 58 84 e8            	movb	%dh, -0x177ba76c(%ebp)
       8: 4b                           	decl	%ebx
       9: 6b 6b d2 30                  	imull	$0x30, -0x2e(%ebx), %ebp
       d: b4 84                        	movb	$-0x7c, %ah
       f: e6 fc                        	outb	%al, $0xfc
      11: 73 57                        	jae	0x6a <_start+0x6a>
      13: 4b                           	decl	%ebx
      14: 5c                           	popl	%esp
      15: 9f                           	lahf
      16: b1 32                        	movb	$0x32, %cl
      18: a9 fb 03 1b 03               	testl	$0x31b03fb, %eax        # imm = 0x31B03FB
      1d: 25                           	<unknown>
      1e: 3c 89                        	cmpb	$-0x77, %al
```

## x86_64

```asm
       0: 86 3a                        	xchgb	%bh, (%rdx)
       2: 88 b5 94 58 84 e8            	movb	%dh, -0x177ba76c(%rbp)
       8: 4b 6b 6b d2 30               	imulq	$0x30, -0x2e(%r11), %rbp
       d: b4 84                        	movb	$-0x7c, %ah
       f: e6 fc                        	outb	%al, $0xfc
      11: 73 57                        	jae	0x6a <_start+0x6a>
      13: 4b 5c                        	popq	%r12
      15: 9f                           	lahf
      16: b1 32                        	movb	$0x32, %cl
      18: a9 fb 03 1b 03               	testl	$0x31b03fb, %eax        # imm = 0x31B03FB
      1d: 25                           	<unknown>
      1e: 3c 89                        	cmpb	$-0x77, %al
```

## armv7

```asm
       0: b5883a86     	strlt	r3, [r8, #0xa86]
       4: e8845894     	stm	r4, {r2, r4, r7, r11, r12, lr}
       8: d26b6b4b     	rsble	r6, r11, #76800
       c: e684b430     	<unknown>
      10: 4b5773fc     	blmi	0x15dd008 <_start+0x15dd008> @ imm = #0x15dcff0
      14: 32b19f5c     	adcslo	r9, r1, #92, #30
      18: 1b03fba9     	blne	0xfeec4 <_start+0xfeec4> @ imm = #0xfeea4
      1c: 893c2503     	ldmdbhi	r12!, {r0, r1, r8, r10, sp}
```

## aarch64

```asm
       0: 86 3a 88 b5  	.word	0xb5883a86
       4: 94 58 84 e8  	.word	0xe8845894
       8: 4b 6b 6b d2  	.word	0xd26b6b4b
       c: 30 b4 84 e6  	.word	0xe684b430
      10: fc 73 57 4b  	.word	0x4b5773fc
      14: 5c 9f b1 32  	.word	0x32b19f5c
      18: a9 fb 03 1b  	.word	0x1b03fba9
      1c: 03 25 3c 89  	.word	0x893c2503
```

## riscv32

```asm
       0: 3a86         	fld	fs5, 0x60(sp)
       2: b588         	fsd	fa0, 0x28(a1)
       4: 5894         	lw	a3, 0x30(s1)
       6: e884         	fsw	fs1, 0x10(s1)
       8: d26b6b4b     	<unknown>
       c: b430         	fsd	fa2, 0x68(s0)
       e: e684         	fsw	fs1, 0x8(a3)
      10: 73fc         	flw	fa5, 0x64(a5)
      12: 9f5c4b57     	<unknown>
      16: 32b1         	jal	0xfffff962 <_start+0xfffffffffffff962>
      18: fba9         	bnez	a5, 0xffffff6a <_start+0xffffffffffffff6a>
      1a: 25031b03     	lh	s6, 0x250(t1)
      1e: 893c         	<unknown>
```

## mips32_be

```asm
       0: 86 3a 88 b5  	lh	$26, -0x774b($17)
       4: 94 58 84 e8  	lhu	$24, -0x7b18($2)
       8: 4b 6b 6b d2  	<unknown>
       c: 30 b4 84 e6  	andi	$20, $5, 0x84e6 <_start+0x84e6>
      10: fc 73 57 4b  	<unknown>
      14: 5c 9f b1 32  	<unknown>
      18: a9 fb 03 1b  	swl	$27, 0x31b($15)
      1c: 03 25 3c 89  	<unknown>
```

## ppc32_be

```asm
       0: 86 3a 88 b5  	lwzu 17, -30539(26)
       4: 94 58 84 e8  	stwu 2, -31512(24)
       8: 4b 6b 6b d2  	ba 0xff6b6bd0
       c: 30 b4 84 e6  	addic 5, 20, -31514
      10: fc 73 57 4b  	<unknown>
      14: 5c 9f b1 32  	rlwnm 31, 4, 22, 4, 25
      18: a9 fb 03 1b  	lha 15, 795(27)
      1c: 03 25 3c 89  	<unknown>
```

## avr

```asm
       0: 86 3a        	cpi	r24, 0xa6
       2: 88 b5        	in	r24, 0x28
       4: 94 58        	subi	r25, 0x84
       6: 84 e8        	ldi	r24, 0x84
       8: 4b 6b        	ori	r20, 0xbb
       a: 6b d2        	rcall	.+1238
       c: 30 b4        	in	r3, 0x20
       e: 84 e6        	ldi	r24, 0x64
      10: fc 73        	andi	r31, 0x3c
      12: 57 4b        	sbci	r21, 0xb7
      14: 5c 9f b1 32  	<unknown>
      18: a9 fb 03 1b  	<unknown>
      1c: 03 25        	eor	r16, r3
      1e: 3c 89        	ldd	r19, Y+4
```

## jvm_bytecode

```text
? ? ? ? ? ? iinc ? ? ? ? ? ? ? iinc ?
```

## wasm_opcode

```text
? ? ? ? ? ? ? ? ? i32.sub i32.sub ? ? ? ? ?
```

## cil_bytecode

```text
? ? ? ? ? add ? ? ? ? ? ? bgt.s ? ? ?
```

## mos6502

```text
? ? DEY ? ? ? ? INX ? ? ? ? BMI ? ? ?
```

# text_plain_hello

- input length: 6 bytes
- sha256: `334d016f755cd6dc58c53a86e183882f8ec14f52fb05345887c8a5edd42c87b7`

## x86_32

```asm
       0: 33 4d 01                     	xorl	0x1(%ebp), %ecx
       3: 6f                           	outsl	(%esi), %dx
       4: 75 5c                        	jne	0x62 <_start+0x62>
       6: d6                           	salc
       7: dc 58 c5                     	fcompl	-0x3b(%eax)
       a: 3a 86 e1 83 88 2f            	cmpb	0x2f8883e1(%esi), %al
      10: 8e c1                        	movl	%ecx, %es
      12: 4f                           	decl	%edi
      13: 52                           	pushl	%edx
      14: fb                           	sti
      15: 05 34 58 87 c8               	addl	$0xc8875834, %eax       # imm = 0xC8875834
      1a: a5                           	movsl	(%esi), %es:(%edi)
      1b: ed                           	inl	%dx, %eax
      1c: d4 2c                        	aam	$0x2c
      1e: 87 b7                        	<unknown>
```

## x86_64

```asm
       0: 33 4d 01                     	xorl	0x1(%rbp), %ecx
       3: 6f                           	outsl	(%rsi), %dx
       4: 75 5c                        	jne	0x62 <_start+0x62>
       6: d6                           	<unknown>
       7: dc 58 c5                     	fcompl	-0x3b(%rax)
       a: 3a 86 e1 83 88 2f            	cmpb	0x2f8883e1(%rsi), %al
      10: 8e c1                        	movl	%ecx, %es
      12: 4f 52                        	pushq	%r10
      14: fb                           	sti
      15: 05 34 58 87 c8               	addl	$0xc8875834, %eax       # imm = 0xC8875834
      1a: a5                           	movsl	(%rsi), %es:(%rdi)
      1b: ed                           	inl	%dx, %eax
      1c: d4                           	<unknown>
      1d: 2c 87                        	subb	$-0x79, %al
      1f: b7                           	<unknown>
```

## armv7

```asm
       0: 6f014d33     	svcvs	#0x14d33
       4: dcd65c75     	ldclle	p12, c5, [r6], {117}
       8: 863ac558     	shsaxhi	r12, r10, r8
       c: 2f8883e1     	svchs	#0x8883e1
      10: 524fc18e     	subpl	r12, pc, #-2147483613
      14: 583405fb     	ldmdapl	r4!, {r0, r1, r3, r4, r5, r6, r7, r8, r10}
      18: eda5c887     	stc	p8, c12, [r5, #540]!
      1c: b7872cd4     	<unknown>
```

## aarch64

```asm
       0: 33 4d 01 6f  	.word	0x6f014d33
       4: 75 5c d6 dc  	.word	0xdcd65c75
       8: 58 c5 3a 86  	.word	0x863ac558
       c: e1 83 88 2f  	.word	0x2f8883e1
      10: 8e c1 4f 52  	.word	0x524fc18e
      14: fb 05 34 58  	.word	0x583405fb
      18: 87 c8 a5 ed  	.word	0xeda5c887
      1c: d4 2c 87 b7  	.word	0xb7872cd4
```

## riscv32

```asm
       0: 6f014d33     	<unknown>
       4: 5c75         	li	s8, -0x3
       6: dcd6         	sw	s5, 0x78(sp)
       8: c558         	sw	a4, 0xc(a0)
       a: 863a         	mv	a2, a4
       c: 83e1         	srli	a5, a5, 0x18
       e: 2f88         	fld	fa0, 0x18(a5)
      10: c18e         	sw	gp, 0xc0(sp)
      12: 05fb524f     	<unknown>
      16: 5834         	lw	a3, 0x70(s0)
      18: eda5c887     	<unknown>
      1c: 2cd4         	fld	fa3, 0x98(s1)
      1e: 87           	<unknown>
      1f: b7           	<unknown>
```

## mips32_be

```asm
       0: 33 4d 01 6f  	andi	$13, $26, 0x16f <_start+0x16f>
       4: 75 5c d6 dc  	jalx	0x5735b70 <_start+0x5735b70>
       8: 58 c5 3a 86  	<unknown>
       c: e1 83 88 2f  	sc	$3, -0x77d1($12)
      10: 8e c1 4f 52  	lw	$1, 0x4f52($22)
      14: fb 05 34 58  	sdc2	$5, 0x3458($24)
      18: 87 c8 a5 ed  	lh	$8, -0x5a13($fp)
      1c: d4 2c 87 b7  	ldc1	$f12, -0x7849($1)
```

## ppc32_be

```asm
       0: 33 4d 01 6f  	addic 26, 13, 367
       4: 75 5c d6 dc  	andis. 28, 10, 55004
       8: 58 c5 3a 86  	<unknown>
       c: e1 83 88 2f  	<unknown>
      10: 8e c1 4f 52  	lbzu 22, 20306(1)
      14: fb 05 34 58  	std 24, 13400(5)
      18: 87 c8 a5 ed  	lwzu 30, -23059(8)
      1c: d4 2c 87 b7  	stfsu 1, -30793(12)
```

## avr

```asm
       0: 33 4d        	sbci	r19, 0xd3
       2: 01 6f        	ori	r16, 0xf1
       4: 75 5c        	subi	r23, 0xc5
       6: d6 dc        	rcall	.-1620
       8: 58 c5        	rjmp	.+2736
       a: 3a 86        	std	Y+2, r3
       c: e1 83        	std	Z+1, r30
       e: 88 2f        	mov	r24, r24
      10: 8e c1        	rjmp	.+796
      12: 4f 52        	subi	r20, 0x2f
      14: fb 05        	cpc	r31, r11
      16: 34 58        	subi	r19, 0x84
      18: 87 c8        	rjmp	.-3826
      1a: a5 ed        	ldi	r26, 0xd5
      1c: d4 2c        	mov	r13, r4
      1e: 87 b7        	in	r24, 0x37
```

## jvm_bytecode

```text
? ? aconst_null ? ? ? ? ? ? ? ? ? ? ? ? ?
```

## wasm_opcode

```text
? ? nop i32.rem_u ? ? ? ? ? ? ? ? ? ? ? ?
```

## cil_bytecode

```text
? ? break ? ? ? ? ? add ? ? ? ? ? ? bge.s
```

## mos6502

```text
? ? ? ? ? ? ? ? ? ? ? ? ? ? DEY ?
```

# instruction_text_print_exit

- input length: 66 bytes
- sha256: `8d05612b3145893782a412914b2cf4c45ecfec613eb190db1aeda36e286ddae2`

## x86_32

```asm
       0: 8d 05 61 2b 31 45            	leal	0x45312b61, %eax
       6: 89 37                        	movl	%esi, (%edi)
       8: 82 a4 12 91 4b 2c f4 c4      	andb	$-0x3c, -0xbd3b46f(%edx,%edx)
      10: 5e                           	popl	%esi
      11: cf                           	iretl
      12: ec                           	inb	%dx, %al
      13: 61                           	popal
      14: 3e b1 90                     	movb	$-0x70, %cl
      17: db 1a                        	fistpl	(%edx)
      19: ed                           	inl	%dx, %eax
      1a: a3 6e 28 6d da               	movl	%eax, 0xda6d286e
      1f: e2                           	<unknown>
```

## x86_64

```asm
       0: 8d 05 61 2b 31 45            	leal	0x45312b61(%rip), %eax  # 0x45312b67 <_start+0x45312b67>
       6: 89 37                        	movl	%esi, (%rdi)
       8: 82                           	<unknown>
       9: a4                           	movsb	(%rsi), %es:(%rdi)
       a: 12 91 4b 2c f4 c4            	adcb	-0x3b0bd3b5(%rcx), %dl
      10: 5e                           	popq	%rsi
      11: cf                           	iretl
      12: ec                           	inb	%dx, %al
      13: 61                           	<unknown>
      14: 3e b1 90                     	movb	$-0x70, %cl
      17: db 1a                        	fistpl	(%rdx)
      19: ed                           	inl	%dx, %eax
      1a: a3                           	<unknown>
      1b: 6e                           	outsb	(%rsi), %dx
      1c: 28 6d da                     	subb	%ch, -0x26(%rbp)
      1f: e2                           	<unknown>
```

## armv7

```asm
       0: 2b61058d     	blhs	0x184163c <_start+0x184163c> @ imm = #0x1841634
       4: 37894531     	<unknown>
       8: 9112a482     	tstls	r2, r2, lsl #9
       c: c4f42c4b     	ldrbtgt	r2, [r4], #3147
      10: 61eccf5e     	mvnvs	r12, lr, asr pc
      14: db90b13e     	blle	0xfe42c514 <_start+0xfffffffffe42c514> @ imm = #-0x1bd3b08
      18: 6ea3ed1a     	mcrvs	p13, #0x5, lr, c3, c10, #0x0
      1c: e2da6d28     	sbcs	r6, r10, #40, #26
```

## aarch64

```asm
       0: 8d 05 61 2b  	.word	0x2b61058d
       4: 31 45 89 37  	.word	0x37894531
       8: 82 a4 12 91  	.word	0x9112a482
       c: 4b 2c f4 c4  	.word	0xc4f42c4b
      10: 5e cf ec 61  	.word	0x61eccf5e
      14: 3e b1 90 db  	.word	0xdb90b13e
      18: 1a ed a3 6e  	.word	0x6ea3ed1a
      1c: 28 6d da e2  	.word	0xe2da6d28
```

## riscv32

```asm
       0: 058d         	addi	a1, a1, 0x3
       2: 2b61         	jal	0x59a <_start+0x59a>
       4: 4531         	li	a0, 0xc
       6: 3789         	jal	0xffffff48 <_start+0xffffffffffffff48>
       8: a482         	fsd	ft0, 0x48(sp)
       a: 9112         	add	sp, sp, tp
       c: c4f42c4b     	<unknown>
      10: cf5e         	sw	s7, 0x9c(sp)
      12: 61ec         	flw	fa1, 0x44(a1)
      14: b13e         	fsd	fa5, 0xa0(sp)
      16: db90         	sw	a2, 0x30(a5)
      18: ed1a         	fsw	ft6, 0x98(sp)
      1a: 6d286ea3     	<unknown>
      1e: e2da         	fsw	fs6, 0x44(sp)
```

## mips32_be

```asm
       0: 8d 05 61 2b  	lw	$5, 0x612b($8)
       4: 31 45 89 37  	andi	$5, $10, 0x8937 <_start+0x8937>
       8: 82 a4 12 91  	lb	$4, 0x1291($21)
       c: 4b 2c f4 c4  	<unknown>
      10: 5e cf ec 61  	<unknown>
      14: 3e b1 90 db  	<unknown>
      18: 1a ed a3 6e  	<unknown>
      1c: 28 6d da e2  	slti	$13, $3, -0x251e <_start+0xffffffffffffdae2>
```

## ppc32_be

```asm
       0: 8d 05 61 2b  	lbzu 8, 24875(5)
       4: 31 45 89 37  	addic 10, 5, -30409
       8: 82 a4 12 91  	lwz 21, 4753(4)
       c: 4b 2c f4 c4  	b 0xff2cf4d0 <_start+0xffffffffff2cf4d0>
      10: 5e cf ec 61  	rlwnm. 15, 22, 29, 17, 16
      14: 3e b1 90 db  	addis 21, 17, -28453
      18: 1a ed a3 6e  	<unknown>
      1c: 28 6d da e2  	<unknown>
```

## avr

```asm
       0: 8d 05        	cpc	r24, r13
       2: 61 2b        	or	r22, r17
       4: 31 45        	sbci	r19, 0x51
       6: 89 37        	cpi	r24, 0x79
       8: 82 a4 12 91  	<unknown>
       c: 4b 2c        	mov	r4, r11
       e: f4 c4        	rjmp	.+2536
      10: 5e cf        	rjmp	.-324
      12: ec 61        	ori	r30, 0x1c
      14: 3e b1        	in	r19, 0xe
      16: 90 db        	rcall	.-2272
      18: 1a ed        	ldi	r17, 0xda
      1a: a3 6e        	ori	r26, 0xe3
      1c: 28 6d        	ori	r18, 0xd8
      1e: da e2        	ldi	r29, 0x2a
```

## jvm_bytecode

```text
? iconst_2 ? aload_1 ? ? ? ? ixor ? ldc ? ? ? ? ?
```

## wasm_opcode

```text
? else ? ? ? i32.eqz ? ? ? ? ? ? ? ? ? ?
```

## cil_bytecode

```text
? ldarg.3 xor br.s ble.s ? ? ? ? ? ? ? ? brfalse.s ? ?
```

## mos6502

```text
STA ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?
```

# tone_sine_64

- input length: 64 bytes
- sha256: `cd03a5f3191cc514a0d8d39b9f08c7ef0059524ab9033db82b51947caab5f68d`

## x86_32

```asm
       0: cd 03                        	int	$0x3
       2: a5                           	movsl	(%esi), %es:(%edi)
       3: f3 19 1c c5 14 a0 d8 d3      	rep		sbbl	%ebx, -0x2c275fec(,%eax,8)
       b: 9b                           	wait
       c: 9f                           	lahf
       d: 08 c7                        	orb	%al, %bh
       f: ef                           	outl	%eax, %dx
      10: 00 59 52                     	addb	%bl, 0x52(%ecx)
      13: 4a                           	decl	%edx
      14: b9 03 3d b8 2b               	movl	$0x2bb83d03, %ecx       # imm = 0x2BB83D03
      19: 51                           	pushl	%ecx
      1a: 94                           	xchgl	%esp, %eax
      1b: 7c aa                        	jl	0xffffffc7 <_start+0xffffffffffffffc7>
      1d: b5 f6                        	movb	$-0xa, %ch
      1f: 8d                           	<unknown>
```

## x86_64

```asm
       0: cd 03                        	int	$0x3
       2: a5                           	movsl	(%rsi), %es:(%rdi)
       3: f3 19 1c c5 14 a0 d8 d3      	rep		sbbl	%ebx, -0x2c275fec(,%rax,8)
       b: 9b                           	wait
       c: 9f                           	lahf
       d: 08 c7                        	orb	%al, %bh
       f: ef                           	outl	%eax, %dx
      10: 00 59 52                     	addb	%bl, 0x52(%rcx)
      13: 4a b9 03 3d b8 2b 51 94 7c aa	movabsq	$-0x55836baed447c2fd, %rcx # imm = 0xAA7C94512BB83D03
      1d: b5 f6                        	movb	$-0xa, %ch
      1f: 8d                           	<unknown>
```

## armv7

```asm
       0: f3a503cd     	<unknown>
       4: 14c51c19     	strbne	r1, [r5], #3097
       8: 9bd3d8a0     	blls	0xff4f6290 <_start+0xffffffffff4f6290> @ imm = #-0xb09d80
       c: efc7089f     	svc	#0xc7089f
      10: 4a525900     	bmi	0x1496418 <_start+0x1496418> @ imm = #0x1496400
      14: b83d03b9     	ldmdalt	sp!, {r0, r3, r4, r5, r7, r8, r9}
      18: 7c94512b     	ldcvc	p1, c5, [r4], {43}
      1c: 8df6b5aa     	ldclhi	p5, c11, [r6, #680]!
```

## aarch64

```asm
       0: cd 03 a5 f3  	.word	0xf3a503cd
       4: 19 1c c5 14  	.word	0x14c51c19
       8: a0 d8 d3 9b  	.word	0x9bd3d8a0
       c: 9f 08 c7 ef  	.word	0xefc7089f
      10: 00 59 52 4a  	.word	0x4a525900
      14: b9 03 3d b8  	.word	0xb83d03b9
      18: 2b 51 94 7c  	.word	0x7c94512b
      1c: aa b5 f6 8d  	.word	0x8df6b5aa
```

## riscv32

```asm
       0: 03cd         	addi	t2, t2, 0x13
       2: f3a5         	bnez	a5, 0xffffff62 <_start+0xffffffffffffff62>
       4: 1c19         	addi	s8, s8, -0x1a
       6: 14c5         	addi	s1, s1, -0xf
       8: d8a0         	sw	s0, 0x70(s1)
       a: 089f9bd3     	fsub.s	fs7, ft11, fs1, rtz
       e: 5900efc7     	<unknown>
      12: 4a52         	lw	s4, 0x14(sp)
      14: 03b9         	addi	t2, t2, 0xe
      16: b83d         	j	0xfffff854 <_start+0xfffffffffffff854>
      18: 7c94512b     	<unknown>
      1c: b5aa         	fsd	fa0, 0xe8(sp)
      1e: 8df6         	mv	s11, t4
```

## mips32_be

```asm
       0: cd 03 a5 f3  	pref	0x3, -0x5a0d($8) <_start+0x3>
       4: 19 1c c5 14  	<unknown>
       8: a0 d8 d3 9b  	sb	$24, -0x2c65($6)
       c: 9f 08 c7 ef  	<unknown>
      10: 00 59 52 4a  	<unknown>
      14: b9 03 3d b8  	swr	$3, 0x3db8($8)
      18: 2b 51 94 7c  	slti	$17, $26, -0x6b84 <_start+0xffffffffffff947c>
      1c: aa b5 f6 8d  	swl	$21, -0x973($21)
```

## ppc32_be

```asm
       0: cd 03 a5 f3  	lfdu 8, -23053(3)
       4: 19 1c c5 14  	<unknown>
       8: a0 d8 d3 9b  	lhz 6, -11365(24)
       c: 9f 08 c7 ef  	stbu 24, -14353(8)
      10: 00 59 52 4a  	<unknown>
      14: b9 03 3d b8  	lmw 8, 15800(3)
      18: 2b 51 94 7c  	<unknown>
      1c: aa b5 f6 8d  	lha 21, -2419(21)
```

## avr

```asm
       0: cd 03 a5 f3  	<unknown>
       4: 19 1c        	adc	r1, r9
       6: c5 14        	cp	r12, r5
       8: a0 d8        	rcall	.-3776
       a: d3 9b        	sbis	0x1a, 0x3
       c: 9f 08        	sbc	r9, r15
       e: c7 ef        	ldi	r28, 0xf7
      10: 00 59        	subi	r16, 0x90
      12: 52 4a        	sbci	r21, 0xa2
      14: b9 03 3d b8  	<unknown>
      18: 2b 51        	subi	r18, 0x1b
      1a: 94 7c        	andi	r25, 0xc4
      1c: aa b5        	in	r26, 0x2a
      1e: f6 8d        	ldd	r31, Z+6
```

## jvm_bytecode

```text
? iconst_0 ? ? aload iload_2 ? ? if_icmpne ? ? iflt if_icmpeq iconst_5 ? ?
```

## wasm_opcode

```text
? loop ? ? ? ? ? ? ? ? ? ? ? ? ? ?
```

## cil_bytecode

```text
? ldarg.1 ? ? ldc.i4.3 ldc.i4.6 ? ldnull ? ? ? ? ? ldloc.2 ? ?
```

## mos6502

```text
? ? LDAz ? ? ? ? ? ? ? ? ? ? ? ? ?
```

# tone_square_64

- input length: 64 bytes
- sha256: `eeaed4f1e83464dc9ce347241abcf3e18d79a91a6ca002412e04816ba994c2d7`

## x86_32

```asm
       0: ee                           	outb	%al, %dx
       1: ae                           	scasb	%es:(%edi), %al
       2: d4 f1                        	aam	$-0xf
       4: e8 34 64 dc 9c               	calll	0x9cdc643d <_start+0xffffffff9cdc643d>
       9: e3 47                        	jecxz	0x52 <_start+0x52>
       b: 24 1a                        	andb	$0x1a, %al
       d: bc f3 e1 8d 79               	movl	$0x798de1f3, %esp       # imm = 0x798DE1F3
      12: a9 1a 6c a0 02               	testl	$0x2a06c1a, %eax        # imm = 0x2A06C1A
      17: 41                           	incl	%ecx
      18: 2e 04 81                     	addb	$-0x7f, %al
      1b: 6b a9                        	<unknown>
      1d: 94                           	xchgl	%esp, %eax
      1e: c2                           	<unknown>
      1f: d7                           	xlatb
```

## x86_64

```asm
       0: ee                           	outb	%al, %dx
       1: ae                           	scasb	%es:(%rdi), %al
       2: d4                           	<unknown>
       3: f1                           	<unknown>
       4: e8 34 64 dc 9c               	callq	0xffffffff9cdc643d <_start+0xffffffff9cdc643d>
       9: e3 47                        	jrcxz	0x52 <_start+0x52>
       b: 24 1a                        	andb	$0x1a, %al
       d: bc f3 e1 8d 79               	movl	$0x798de1f3, %esp       # imm = 0x798DE1F3
      12: a9 1a 6c a0 02               	testl	$0x2a06c1a, %eax        # imm = 0x2A06C1A
      17: 41 2e                        	cs
      19: 04 81                        	addb	$-0x7f, %al
      1b: 6b a9                        	<unknown>
      1d: 94                           	xchgl	%esp, %eax
      1e: c2                           	<unknown>
      1f: d7                           	xlatb
```

## armv7

```asm
       0: f1d4aeee     	<unknown>
       4: dc6434e8     	stclle	p4, c3, [r4], #-928
       8: 2447e39c     	strbhs	lr, [r7], #-924
       c: e1f3bc1a     	mvns	r11, r10, lsl r12
      10: 1aa9798d     	bne	0xfea5e64c <_start+0xfffffffffea5e64c> @ imm = #-0x15a19cc
      14: 4102a06c     	<unknown>
      18: 6b81042e     	blvs	0xfe0410d8 <_start+0xfffffffffe0410d8> @ imm = #-0x1fbef48
      1c: d7c294a9     	strble	r9, [r2, r9, lsr #9]
```

## aarch64

```asm
       0: ee ae d4 f1  	.word	0xf1d4aeee
       4: e8 34 64 dc  	.word	0xdc6434e8
       8: 9c e3 47 24  	.word	0x2447e39c
       c: 1a bc f3 e1  	.word	0xe1f3bc1a
      10: 8d 79 a9 1a  	.word	0x1aa9798d
      14: 6c a0 02 41  	.word	0x4102a06c
      18: 2e 04 81 6b  	.word	0x6b81042e
      1c: a9 94 c2 d7  	.word	0xd7c294a9
```

## riscv32

```asm
       0: aeee         	fsd	fs11, 0x158(sp)
       2: f1d4         	fsw	fa3, 0x24(a1)
       4: 34e8         	fld	fa0, 0xe8(s1)
       6: dc64         	sw	s1, 0x7c(s0)
       8: e39c         	fsw	fa5, 0x0(a5)
       a: bc1a2447     	<unknown>
       e: 798de1f3     	csrrsi	gp, 0x798, 0x1b
      12: 1aa9         	addi	s5, s5, -0x16
      14: a06c         	fsd	fa1, 0xc0(s0)
      16: 4102         	lw	sp, 0x0(sp)
      18: 042e         	slli	s0, s0, 0xb
      1a: 6b81         	lui	s7, 0x0
      1c: 94a9         	c.srai	s1, 0x2a
      1e: d7c2         	sw	a6, 0xec(sp)
```

## mips32_be

```asm
       0: ee ae d4 f1  	<unknown>
       4: e8 34 64 dc  	swc2	$20, 0x64dc($1)
       8: 9c e3 47 24  	<unknown>
       c: 1a bc f3 e1  	<unknown>
      10: 8d 79 a9 1a  	lw	$25, -0x56e6($11)
      14: 6c a0 02 41  	<unknown>
      18: 2e 04 81 6b  	sltiu	$4, $16, -0x7e95 <_start+0xffffffffffff816b>
      1c: a9 94 c2 d7  	swl	$20, -0x3d29($12)
```

## ppc32_be

```asm
       0: ee ae d4 f1  	<unknown>
       4: e8 34 64 dc  	ld 1, 25820(20)
       8: 9c e3 47 24  	stbu 7, 18212(3)
       c: 1a bc f3 e1  	stxvp 52, -3104(28)
      10: 8d 79 a9 1a  	lbzu 11, -22246(25)
      14: 6c a0 02 41  	xoris 0, 5, 577
      18: 2e 04 81 6b  	cmpwi 4, 4, -32405
      1c: a9 94 c2 d7  	lha 12, -15657(20)
```

## avr

```asm
       0: ee ae d4 f1  	<unknown>
       4: e8 34        	cpi	r30, 0x48
       6: 64 dc        	rcall	.-1848
       8: 9c e3        	ldi	r25, 0x3c
       a: 47 24        	eor	r4, r7
       c: 1a bc        	out	0x2a, r1
       e: f3 e1        	ldi	r31, 0x13
      10: 8d 79        	andi	r24, 0x9d
      12: a9 1a        	sub	r10, r25
      14: 6c a0 02 41  	<unknown>
      18: 2e 04        	cpc	r2, r14
      1a: 81 6b        	ori	r24, 0xb1
      1c: a9 94 c2 d7  	<unknown>
```

## jvm_bytecode

```text
? ? ? ? ? ? isub ? ifge ? ? ? iload_0 ? ? ?
```

## wasm_opcode

```text
? ? ? ? ? ? ? ? ? ? i32.ne global.set ? ? ? ?
```

## cil_bytecode

```text
? ? ? ? ? ? ? ? ? ? ? ? ldc.i4.4 ? ? ?
```

## mos6502

```text
? ? ? ? INX ? ? ? ? ? ? ? ? ? ? ?
```

# tone_saw_64

- input length: 64 bytes
- sha256: `3f9f32d2261ccaa2aff69d8348e605ee3f2d8dd645941592095cc6a6f6729d1f`

## x86_32

```asm
       0: 3f                           	aas
       1: 9f                           	lahf
       2: 32 d2                        	xorb	%dl, %dl
       4: 26 1c ca                     	sbbb	$-0x36, %al
       7: a2 af f6 9d 83               	movb	%al, 0x839df6af
       c: 48                           	decl	%eax
       d: e6 05                        	outb	%al, $0x5
       f: ee                           	outb	%al, %dx
      10: 3f                           	aas
      11: 2d 8d d6 45 94               	subl	$0x9445d68d, %eax       # imm = 0x9445D68D
      16: 15 92 09 5c c6               	adcl	$0xc65c0992, %eax       # imm = 0xC65C0992
      1b: a6                           	cmpsb	%es:(%edi), (%esi)
      1c: f6 72 9d                     	divb	-0x63(%edx)
      1f: 1f                           	popl	%ds
```

## x86_64

```asm
       0: 3f                           	<unknown>
       1: 9f                           	lahf
       2: 32 d2                        	xorb	%dl, %dl
       4: 26 1c ca                     	sbbb	$-0x36, %al
       7: a2 af f6 9d 83 48 e6 05 ee   	movabsb	%al, -0x11fa19b77c620951
      10: 3f                           	<unknown>
      11: 2d 8d d6 45 94               	subl	$0x9445d68d, %eax       # imm = 0x9445D68D
      16: 15 92 09 5c c6               	adcl	$0xc65c0992, %eax       # imm = 0xC65C0992
      1b: a6                           	cmpsb	%es:(%rdi), (%rsi)
      1c: f6 72 9d                     	divb	-0x63(%rdx)
      1f: 1f                           	<unknown>
```

## armv7

```asm
       0: d2329f3f     	eorsle	r9, r2, #63, #30
       4: a2ca1c26     	sbcge	r1, r10, #9728
       8: 839df6af     	orrshi	pc, sp, #183500800
       c: ee05e648     	cdp	p6, #0x0, c14, c5, c8, #0x2
      10: d68d2d3f     	<unknown>
      14: 92159445     	andsls	r9, r5, #1157627904
      18: a6c65c09     	strbge	r5, [r6], r9, lsl #24
      1c: 1f9d72f6     	svcne	#0x9d72f6
```

## aarch64

```asm
       0: 3f 9f 32 d2  	.word	0xd2329f3f
       4: 26 1c ca a2  	.word	0xa2ca1c26
       8: af f6 9d 83  	.word	0x839df6af
       c: 48 e6 05 ee  	.word	0xee05e648
      10: 3f 2d 8d d6  	.word	0xd68d2d3f
      14: 45 94 15 92  	.word	0x92159445
      18: 09 5c c6 a6  	.word	0xa6c65c09
      1c: f6 72 9d 1f  	.word	0x1f9d72f6
```

## riscv32

```asm
       0: d2329f3f a2ca1c26    	<unknown>
       8: 839df6af     	<unknown>
       c: e648         	fsw	fa0, 0xc(a2)
       e: ee05         	bnez	a2, 0x46 <_start+0x46>
      10: d68d2d3f 92159445    	<unknown>
      18: 5c09         	li	s8, -0x1e
      1a: a6c6         	fsd	fa7, 0x148(sp)
      1c: 72f6         	flw	ft5, 0x7c(sp)
      1e: 1f9d         	addi	t6, t6, -0x19
```

## mips32_be

```asm
       0: 3f 9f 32 d2  	<unknown>
       4: 26 1c ca a2  	addiu	$gp, $16, -0x355e <_start+0xffffffffffffcaa2>
       8: af f6 9d 83  	sw	$22, -0x627d($ra)
       c: 48 e6 05 ee  	<unknown>
      10: 3f 2d 8d d6  	<unknown>
      14: 45 94 15 92  	<unknown>
      18: 09 5c c6 a6  	j	0x5731a98 <_start+0x5731a98>
      1c: f6 72 9d 1f  	sdc1	$f18, -0x62e1($19)
```

## ppc32_be

```asm
       0: 3f 9f 32 d2  	addis 28, 31, 13010
       4: 26 1c ca a2  	<unknown>
       8: af f6 9d 83  	lhau 31, -25213(22)
       c: 48 e6 05 ee  	ba 0xe605ec
      10: 3f 2d 8d d6  	addis 25, 13, -29226
      14: 45 94 15 92  	sc 44
      18: 09 5c c6 a6  	tdi 10, 28, -14682
      1c: f6 72 9d 1f  	stxssp 19, -25316(18)
```

## avr

```asm
       0: 3f 9f 32 d2  	<unknown>
       4: 26 1c        	adc	r2, r6
       6: ca a2 af f6  	<unknown>
       a: 9d 83        	std	Y+5, r25
       c: 48 e6        	ldi	r20, 0x68
       e: 05 ee        	ldi	r16, 0xe5
      10: 3f 2d        	mov	r19, r15
      12: 8d d6        	rcall	.+3354
      14: 45 94        	asr	r4
      16: 15 92 09 5c  	<unknown>
      1a: c6 a6 f6 72  	<unknown>
      1e: 9d 1f        	adc	r25, r29
```

## jvm_bytecode

```text
? if_icmpeq ? ? ? iload_2 ? ? ? ? ifgt ? ? ? iconst_2 ?
```

## wasm_opcode

```text
? ? ? ? ? ? ? ? ? ? ? ? ? ? else ?
```

## cil_bytecode

```text
? ? blt.s ? ? ldc.i4.6 ? ? ? ? ? ? ? ? ldarg.3 ?
```

## mos6502

```text
? ? ? ? ? ? DEX ? ? ? ? ? ? ? ? ?
```

# tone_triangle_64

- input length: 64 bytes
- sha256: `b897433712909203ca7b12aef52406ee8a12eb5b57ae0a473f88f0e9a402eedd`

## x86_32

```asm
       0: b8 97 43 37 12               	movl	$0x12374397, %eax       # imm = 0x12374397
       5: 90                           	nop
       6: 92                           	xchgl	%edx, %eax
       7: 03 ca                        	addl	%edx, %ecx
       9: 7b 12                        	jnp	0x1d <_start+0x1d>
       b: ae                           	scasb	%es:(%edi), %al
       c: f5                           	cmc
       d: 24 06                        	andb	$0x6, %al
       f: ee                           	outb	%al, %dx
      10: 8a 12                        	movb	(%edx), %dl
      12: eb 5b                        	jmp	0x6f <_start+0x6f>
      14: 57                           	pushl	%edi
      15: ae                           	scasb	%es:(%edi), %al
      16: 0a 47 3f                     	orb	0x3f(%edi), %al
      19: 88 f0                        	movb	%dh, %al
      1b: e9 a4 02 ee dd               	jmp	0xddee02c4 <_start+0xffffffffddee02c4>
```

## x86_64

```asm
       0: b8 97 43 37 12               	movl	$0x12374397, %eax       # imm = 0x12374397
       5: 90                           	nop
       6: 92                           	xchgl	%edx, %eax
       7: 03 ca                        	addl	%edx, %ecx
       9: 7b 12                        	jnp	0x1d <_start+0x1d>
       b: ae                           	scasb	%es:(%rdi), %al
       c: f5                           	cmc
       d: 24 06                        	andb	$0x6, %al
       f: ee                           	outb	%al, %dx
      10: 8a 12                        	movb	(%rdx), %dl
      12: eb 5b                        	jmp	0x6f <_start+0x6f>
      14: 57                           	pushq	%rdi
      15: ae                           	scasb	%es:(%rdi), %al
      16: 0a 47 3f                     	orb	0x3f(%rdi), %al
      19: 88 f0                        	movb	%dh, %al
      1b: e9 a4 02 ee dd               	jmp	0xffffffffddee02c4 <_start+0xffffffffddee02c4>
```

## armv7

```asm
       0: 374397b8     	<unknown>
       4: 03929012     	orrseq	r9, r2, #18
       8: ae127bca     	vnmlage.f64	d7, d18, d10
       c: ee0624f5     	mcr	p4, #0x0, r2, c6, c5, #0x7
      10: 5beb128a     	blpl	0xffac4a40 <_start+0xffffffffffac4a40> @ imm = #-0x53b5d8
      14: 470aae57     	smlsdmi	r10, r7, lr, r10
      18: e9f0883f     	ldmib	r0!, {r0, r1, r2, r3, r4, r5, r11, pc} ^
      1c: ddee02a4     	stclle	p2, c0, [lr, #656]!
```

## aarch64

```asm
       0: b8 97 43 37  	.word	0x374397b8
       4: 12 90 92 03  	.word	0x03929012
       8: ca 7b 12 ae  	.word	0xae127bca
       c: f5 24 06 ee  	.word	0xee0624f5
      10: 8a 12 eb 5b  	.word	0x5beb128a
      14: 57 ae 0a 47  	.word	0x470aae57
      18: 3f 88 f0 e9  	.word	0xe9f0883f
      1c: a4 02 ee dd  	.word	0xddee02a4
```

## riscv32

```asm
       0: 97b8         	<unknown>
       2: 90123743     	fmadd.s	fa4, ft4, ft1, fs2, rup
       6: 0392         	slli	t2, t2, 0x4
       8: 7bca         	flw	fs7, 0xb0(sp)
       a: ae12         	fsd	ft4, 0x118(sp)
       c: 24f5         	jal	0x2f8 <_start+0x2f8>
       e: ee06         	fsw	ft1, 0x1c(sp)
      10: 128a         	c.slli	t0, 0x22
      12: ae575beb     	<unknown>
      16: 470a         	lw	a4, 0x80(sp)
      18: e9f0883f ddee02a4    	<unknown>
```

## mips32_be

```asm
       0: b8 97 43 37  	swr	$23, 0x4337($4)
       4: 12 90 92 03  	beq	$20, $16, 0xfffe4814 <_start+0xfffffffffffe4814>
       8: ca 7b 12 ae  	lwc2	$27, 0x12ae($19)
       c: f5 24 06 ee  	sdc1	$f4, 0x6ee($9)
      10: 8a 12 eb 5b  	lwl	$18, -0x14a5($16)
      14: 57 ae 0a 47  	bnel	$sp, $14, 0x2934 <_start+0x2934>
      18: 3f 88 f0 e9  	<unknown>
      1c: a4 02 ee dd  	sh	$2, -0x1123($zero)
```

## ppc32_be

```asm
       0: b8 97 43 37  	lmw 4, 17207(23)
       4: 12 90 92 03  	<unknown>
       8: ca 7b 12 ae  	lfd 19, 4782(27)
       c: f5 24 06 ee  	stxsd 9, 1772(4)
      10: 8a 12 eb 5b  	lbz 16, -5285(18)
      14: 57 ae 0a 47  	rlwinm. 14, 29, 1, 9, 3
      18: 3f 88 f0 e9  	addis 28, 8, -3863
      1c: a4 02 ee dd  	lhzu 0, -4387(2)
```

## avr

```asm
       0: b8 97 43 37  	<unknown>
       4: 12 90        	ld	r1, -Z
       6: 92 03 ca 7b  	<unknown>
       a: 12 ae f5 24  	<unknown>
       e: 06 ee        	ldi	r16, 0xe6
      10: 8a 12        	cpse	r8, r26
      12: eb 5b        	subi	r30, 0xbb
      14: 57 ae 0a 47  	<unknown>
      18: 3f 88        	ldd	r3, Y+7
      1a: f0 e9        	ldi	r31, 0x90
      1c: a4 02 ee dd  	<unknown>
```

## jvm_bytecode

```text
invokestatic ? ? ? ldc ? ? iconst_0 ? ? ldc ? ? ? iconst_3 ?
```

## wasm_opcode

```text
? ? ? ? ? ? ? loop ? ? ? ? ? global.set ? ?
```

## cil_bytecode

```text
? ? ? ? ? ? ? ldarg.1 ? ? ? ? ? ? ldloc.0 ?
```

## mos6502

```text
? ? ? ? ? ? ? ? DEX ? ? ? ? ? ? ?
```

# bytes_zero_55

- input length: 55 bytes
- sha256: `02779466cdec163811d078815c633f21901413081449002f24aa3e80f0b88ef7`

## x86_32

```asm
       0: 02 77 94                     	addb	-0x6c(%edi), %dh
       3: 66 cd ec                     	int	$0xec
       6: 16                           	pushl	%ss
       7: 38 11                        	cmpb	%dl, (%ecx)
       9: d0 78 81                     	sarb	-0x7f(%eax)
       c: 5c                           	popl	%esp
       d: 63 3f                        	arpl	%di, (%edi)
       f: 21 90 14 13 08 14            	andl	%edx, 0x14081314(%eax)
      15: 49                           	decl	%ecx
      16: 00 2f                        	addb	%ch, (%edi)
      18: 24 aa                        	andb	$-0x56, %al
      1a: 3e 80 f0 b8                  	xorb	$-0x48, %al
      1e: 8e f7                        	<unknown>
```

## x86_64

```asm
       0: 02 77 94                     	addb	-0x6c(%rdi), %dh
       3: 66 cd ec                     	int	$0xec
       6: 16                           	<unknown>
       7: 38 11                        	cmpb	%dl, (%rcx)
       9: d0 78 81                     	sarb	-0x7f(%rax)
       c: 5c                           	popq	%rsp
       d: 63 3f                        	movslq	(%rdi), %edi
       f: 21 90 14 13 08 14            	andl	%edx, 0x14081314(%rax)
      15: 49 00 2f                     	addb	%bpl, (%r15)
      18: 24 aa                        	andb	$-0x56, %al
      1a: 3e 80 f0 b8                  	xorb	$-0x48, %al
      1e: 8e f7                        	<unknown>
```

## armv7

```asm
       0: 66947702     	ldrvs	r7, [r4], r2, lsl #14
       4: 3816eccd     	ldmdalo	r6, {r0, r2, r3, r6, r7, r10, r11, sp, lr, pc}
       8: 8178d011     	cmnhi	r8, r1, lsl r0
       c: 213f635c     	teqhs	pc, r12, asr r3
      10: 08131490     	ldmdaeq	r3, {r4, r7, r10, r12}
      14: 2f004914     	svchs	#0x4914
      18: 803eaa24     	eorshi	r10, lr, r4, lsr #20
      1c: f78eb8f0     	<unknown>
```

## aarch64

```asm
       0: 02 77 94 66  	.word	0x66947702
       4: cd ec 16 38  	.word	0x3816eccd
       8: 11 d0 78 81  	.word	0x8178d011
       c: 5c 63 3f 21  	.word	0x213f635c
      10: 90 14 13 08  	.word	0x08131490
      14: 14 49 00 2f  	.word	0x2f004914
      18: 24 aa 3e 80  	.word	0x803eaa24
      1c: f0 b8 8e f7  	.word	0xf78eb8f0
```

## riscv32

```asm
       0: 7702         	flw	fa4, 0x20(sp)
       2: 6694         	flw	fa3, 0x8(a3)
       4: eccd         	bnez	s1, 0xbe <_start+0xbe>
       6: 3816         	fld	fa6, 0x160(sp)
       8: d011         	beqz	s0, 0xffffff0c <_start+0xffffffffffffff0c>
       a: 8178         	<unknown>
       c: 635c         	flw	fa5, 0x4(a4)
       e: 1490213f 49140813    	<unknown>
      16: 2f00         	fld	fs0, 0x18(a4)
      18: aa24         	fsd	fs1, 0x50(a2)
      1a: 803e         	c.mv	zero, a5
      1c: b8f0         	fsd	fa2, 0xf0(s1)
      1e: f78e         	fsw	ft3, 0xec(sp)
```

## mips32_be

```asm
       0: 02 77 94 66  	<unknown>
       4: cd ec 16 38  	pref	0xc, 0x1638($15) <_start+0xc>
       8: 11 d0 78 81  	beq	$14, $16, 0x1e210 <_start+0x1e210>
       c: 5c 63 3f 21  	<unknown>
      10: 90 14 13 08  	lbu	$20, 0x1308($zero)
      14: 14 49 00 2f  	bne	$2, $9, 0xd4 <_start+0xd4>
      18: 24 aa 3e 80  	addiu	$10, $5, 0x3e80 <_start+0x3e80>
      1c: f0 b8 8e f7  	<unknown>
```

## ppc32_be

```asm
       0: 02 77 94 66  	<unknown>
       4: cd ec 16 38  	lfdu 15, 5688(12)
       8: 11 d0 78 81  	<unknown>
       c: 5c 63 3f 21  	rlwnm. 3, 3, 7, 28, 16
      10: 90 14 13 08  	stw 0, 4872(20)
      14: 14 49 00 2f  	<unknown>
      18: 24 aa 3e 80  	<unknown>
      1c: f0 b8 8e f7  	xxsel 37, 56, 49, 27
```

## avr

```asm
       0: 02 77        	andi	r16, 0x72
       2: 94 66        	ori	r25, 0x64
       4: cd ec        	ldi	r28, 0xcd
       6: 16 38        	cpi	r17, 0x86
       8: 11 d0        	rcall	.+34
       a: 78 81        	ldd	r23, Y+0
       c: 5c 63        	ori	r21, 0x3c
       e: 3f 21        	and	r19, r15
      10: 90 14        	cp	r9, r0
      12: 13 08        	sbc	r1, r3
      14: 14 49        	sbci	r17, 0x94
      16: 00 2f        	mov	r16, r16
      18: 24 aa 3e 80  	<unknown>
      1c: f0 b8        	out	0x0, r15
      1e: 8e f7        	brtc	.-30
```

## jvm_bytecode

```text
iconst_m1 ? ? ? ? ? lload ? sipush ? ? ? ? ? ? ?
```

## wasm_opcode

```text
block ? ? ? ? ? ? ? ? ? ? ? ? ? ? local.set
```

## cil_bytecode

```text
ldarg.0 ? ? ? ? ? ldc.i4.0 br ldloc.s ? ? ? ? ? ? ?
```

## mos6502

```text
? ? ? ? ? ? ? ? ? BNE ? ? ? ? ? ?
```

# bytes_nop_55

- input length: 55 bytes
- sha256: `db045faace9a73f328bb8f7ef1c9f1c2feed0ea65a768ab49f39ea1350774ff5`

## x86_32

```asm
       0: db 04 5f                     	fildl	(%edi,%ebx,2)
       3: aa                           	stosb	%al, %es:(%edi)
       4: ce                           	into
       5: 9a 73 f3 28 bb 8f 7e         	lcalll	$0x7e8f, $0xbb28f373    # imm = 0x7E8F
       c: f1                           	<unknown>
       d: c9                           	leave
       e: f1                           	<unknown>
       f: c2 fe ed                     	retl	$-0x1202                # imm = 0xEDFE
      12: 0e                           	pushl	%cs
      13: a6                           	cmpsb	%es:(%edi), (%esi)
      14: 5a                           	popl	%edx
      15: 76 8a                        	jbe	0xffffffa1 <_start+0xffffffffffffffa1>
      17: b4 9f                        	movb	$-0x61, %ah
      19: 39 ea                        	cmpl	%ebp, %edx
      1b: 13 50 77                     	adcl	0x77(%eax), %edx
      1e: 4f                           	decl	%edi
      1f: f5                           	cmc
```

## x86_64

```asm
       0: db 04 5f                     	fildl	(%rdi,%rbx,2)
       3: aa                           	stosb	%al, %es:(%rdi)
       4: ce                           	<unknown>
       5: 9a                           	<unknown>
       6: 73 f3                        	jae	0xfffffffffffffffb <_start+0xfffffffffffffffb>
       8: 28 bb 8f 7e f1 c9            	subb	%bh, -0x360e8171(%rbx)
       e: f1                           	<unknown>
       f: c2 fe ed                     	retq	$-0x1202                # imm = 0xEDFE
      12: 0e                           	<unknown>
      13: a6                           	cmpsb	%es:(%rdi), (%rsi)
      14: 5a                           	popq	%rdx
      15: 76 8a                        	jbe	0xffffffffffffffa1 <_start+0xffffffffffffffa1>
      17: b4 9f                        	movb	$-0x61, %ah
      19: 39 ea                        	cmpl	%ebp, %edx
      1b: 13 50 77                     	adcl	0x77(%rax), %edx
      1e: 4f f5                        	cmc
```

## armv7

```asm
       0: aa5f04db     	bge	0x17c1374 <_start+0x17c1374> @ imm = #0x17c136c
       4: f3739ace     	<unknown>
       8: 7e8fbb28     	vdivvc.f64	d11, d15, d24
       c: c2f1c9f1     	rscsgt	r12, r1, #3948544
      10: a60eedfe     	<unknown>
      14: b48a765a     	strlt	r7, [r10], #1626
      18: 13ea399f     	<unknown>
      1c: f54f7750     	<unknown>
```

## aarch64

```asm
       0: db 04 5f aa  	.word	0xaa5f04db
       4: ce 9a 73 f3  	.word	0xf3739ace
       8: 28 bb 8f 7e  	.word	0x7e8fbb28
       c: f1 c9 f1 c2  	.word	0xc2f1c9f1
      10: fe ed 0e a6  	.word	0xa60eedfe
      14: 5a 76 8a b4  	.word	0xb48a765a
      18: 9f 39 ea 13  	.word	0x13ea399f
      1c: 50 77 4f f5  	.word	0xf54f7750
```

## riscv32

```asm
       0: aa5f04db     	<unknown>
       4: 9ace         	add	s5, s5, s3
       6: bb28f373     	csrrci	t1, 0xbb2, 0x11
       a: c9f17e8f     	<unknown>
       e: c2f1         	beqz	a3, 0xd2 <_start+0xd2>
      10: edfe         	fsw	ft11, 0xd8(sp)
      12: a60e         	fsd	ft3, 0x108(sp)
      14: 765a         	flw	fa2, 0xb4(sp)
      16: b48a         	fsd	ft2, 0x68(sp)
      18: 399f 13ea 7750       	<unknown>
      1e: 4f           	<unknown>
      1f: f5           	<unknown>
```

## mips32_be

```asm
       0: db 04 5f aa  	ldc2	$4, 0x5faa($24)
       4: ce 9a 73 f3  	pref	0x1a, 0x73f3($20) <_start+0x1a>
       8: 28 bb 8f 7e  	slti	$27, $5, -0x7082 <_start+0xffffffffffff8f7e>
       c: f1 c9 f1 c2  	<unknown>
      10: fe ed 0e a6  	<unknown>
      14: 5a 76 8a b4  	<unknown>
      18: 9f 39 ea 13  	<unknown>
      1c: 50 77 4f f5  	beql	$3, $23, 0x13ff4 <_start+0x13ff4>
```

## ppc32_be

```asm
       0: db 04 5f aa  	stfd 24, 24490(4)
       4: ce 9a 73 f3  	lfdu 20, 29683(26)
       8: 28 bb 8f 7e  	cmpldi 1, 27, 36734
       c: f1 c9 f1 c2  	xsdivdp 14, 9, 62
      10: fe ed 0e a6  	<unknown>
      14: 5a 76 8a b4  	<unknown>
      18: 9f 39 ea 13  	stbu 25, -5613(25)
      1c: 50 77 4f f5  	rlwimi. 23, 3, 9, 31, 26
```

## avr

```asm
       0: db 04        	cpc	r13, r11
       2: 5f aa ce 9a  	<unknown>
       6: 73 f3        	brvs	.-36
       8: 28 bb        	out	0x18, r18
       a: 8f 7e        	andi	r24, 0xef
       c: f1 c9        	rjmp	.-3102
       e: f1 c2        	rjmp	.+1506
      10: fe ed        	ldi	r31, 0xde
      12: 0e a6 5a 76  	<unknown>
      16: 8a b4        	in	r8, 0x2a
      18: 9f 39        	cpi	r25, 0x9f
      1a: ea 13        	cpse	r30, r26
      1c: 50 77        	andi	r21, 0x70
      1e: 4f f5        	brid	.+82
```

## jvm_bytecode

```text
? iconst_1 ? ? ? ifne ? ? ? new ? iand ? ? ? ?
```

## wasm_opcode

```text
? if ? ? ? ? i32.xor ? i32.load ? ? ? ? ? ? ?
```

## cil_bytecode

```text
? ldarg.2 and ? ? ? newobj ? ? ? ? ? ? ? ? ?
```

## mos6502

```text
? ? ? ? ? ? ? ? ? ? ? ? ? CMP# ? ?
```

# bytes_ff_55

- input length: 55 bytes
- sha256: `aadaed00a3c5fbb8072ae7f1984ba8199fbe5272de427d11eaf31583af37db51`

## x86_32

```asm
       0: aa                           	stosb	%al, %es:(%edi)
       1: da ed                        	<unknown>
       3: 00 a3 c5 fb b8 07            	addb	%ah, 0x7b8fbc5(%ebx)
       9: 2a e7                        	subb	%bh, %ah
       b: f1                           	<unknown>
       c: 98                           	cwtl
       d: 4b                           	decl	%ebx
       e: a8 19                        	testb	$0x19, %al
      10: 9f                           	lahf
      11: be 52 72 de 42               	movl	$0x42de7252, %esi       # imm = 0x42DE7252
      16: 7d 11                        	jge	0x29 <_start+0x29>
      18: ea f3 15 83 af 37 db         	ljmpl	$-0x24c9, $0xaf8315f3   # imm = 0xDB37
      1f: 51                           	pushl	%ecx
```

## x86_64

```asm
       0: aa                           	stosb	%al, %es:(%rdi)
       1: da ed                        	<unknown>
       3: 00 a3 c5 fb b8 07            	addb	%ah, 0x7b8fbc5(%rbx)
       9: 2a e7                        	subb	%bh, %ah
       b: f1                           	<unknown>
       c: 98                           	cwtl
       d: 4b a8 19                     	testb	$0x19, %al
      10: 9f                           	lahf
      11: be 52 72 de 42               	movl	$0x42de7252, %esi       # imm = 0x42DE7252
      16: 7d 11                        	jge	0x29 <_start+0x29>
      18: ea                           	<unknown>
      19: f3 15 83 af 37 db            	rep		adcl	$0xdb37af83, %eax # imm = 0xDB37AF83
      1f: 51                           	pushq	%rcx
```

## armv7

```asm
       0: 00eddaaa     	rsceq	sp, sp, r10, lsr #21
       4: b8fbc5a3     	ldmlt	r11!, {r0, r1, r5, r7, r8, r10, lr, pc} ^
       8: f1e72a07     	<unknown>
       c: 19a84b98     	stmibne	r8!, {r3, r4, r7, r8, r9, r11, lr}
      10: 7252be9f     	subsvc	r11, r2, #2544
      14: 117d42de     	ldrsbne	r4, [sp, #-46]!
      18: 8315f3ea     	tsthi	r5, #-1476395005
      1c: 51db37af     	bicspl	r3, r11, pc, lsr #15
```

## aarch64

```asm
       0: aa da ed 00  	.word	0x00eddaaa
       4: a3 c5 fb b8  	.word	0xb8fbc5a3
       8: 07 2a e7 f1  	.word	0xf1e72a07
       c: 98 4b a8 19  	.word	0x19a84b98
      10: 9f be 52 72  	.word	0x7252be9f
      14: de 42 7d 11  	.word	0x117d42de
      18: ea f3 15 83  	.word	0x8315f3ea
      1c: af 37 db 51  	.word	0x51db37af
```

## riscv32

```asm
       0: daaa         	sw	a0, 0x74(sp)
       2: 00ed         	addi	ra, ra, 0x1b
       4: b8fbc5a3     	<unknown>
       8: f1e72a07     	flw	fs4, -0xe2(a4)
       c: 4b98         	lw	a4, 0x10(a5)
       e: 19a8         	addi	a0, sp, 0xf8
      10: be9f 7252 42de       	<unknown>
      16: 117d         	addi	sp, sp, -0x1
      18: f3ea         	fsw	fs10, 0xe4(sp)
      1a: 8315         	srli	a4, a4, 0x5
      1c: 51db37af     	<unknown>
```

## mips32_be

```asm
       0: aa da ed 00  	swl	$26, -0x1300($22)
       4: a3 c5 fb b8  	sb	$5, -0x448($fp)
       8: 07 2a e7 f1  	tlti	$25, -0x180f <_start+0xffffffffffffe7f1>
       c: 98 4b a8 19  	lwr	$11, -0x57e7($2)
      10: 9f be 52 72  	<unknown>
      14: de 42 7d 11  	<unknown>
      18: ea f3 15 83  	swc2	$19, 0x1583($23)
      1c: af 37 db 51  	sw	$23, -0x24af($25)
```

## ppc32_be

```asm
       0: aa da ed 00  	lha 22, -4864(26)
       4: a3 c5 fb b8  	lhz 30, -1096(5)
       8: 07 2a e7 f1  	<unknown>
       c: 98 4b a8 19  	stb 2, -22503(11)
      10: 9f be 52 72  	stbu 29, 21106(30)
      14: de 42 7d 11  	stfdu 18, 32017(2)
      18: ea f3 15 83  	<unknown>
      1c: af 37 db 51  	lhau 25, -9391(23)
```

## avr

```asm
       0: aa da        	rcall	.-2732
       2: ed 00 a3 c5  	<unknown>
       6: fb b8        	out	0xb, r15
       8: 07 2a        	or	r0, r23
       a: e7 f1        	brie	.+120
       c: 98 4b        	sbci	r25, 0xb8
       e: a8 19        	sub	r26, r8
      10: 9f be        	out	0x3f, r9
      12: 52 72        	andi	r21, 0x22
      14: de 42        	sbci	r29, 0x2e
      16: 7d 11        	cpse	r23, r13
      18: ea f3        	brmi	.-6
      1a: 15 83        	std	Z+5, r17
      1c: af 37        	cpi	r26, 0x7f
      1e: db 51        	subi	r29, 0x1b
```

## jvm_bytecode

```text
? ? ? nop ? ? ? invokestatic iconst_4 aload_0 ? ? ? ? ? aload
```

## wasm_opcode

```text
? ? ? unreachable ? ? ? ? ? ? ? ? ? ? ? ?
```

## cil_bytecode

```text
? ? ? nop ? ? ? ? ldloc.1 ret ? ? ? ? ? ldc.i4.3
```

## mos6502

```text
? ? ? BRK ? ? ? ? ? ? ? ? ? ? ? ?
```

# bytes_ascending_55

- input length: 55 bytes
- sha256: `463eb28e72f82e0a96c0a4cc53690c571281131f672aa229e0d45ae59b598b59`

## x86_32

```asm
       0: 46                           	incl	%esi
       1: 3e b2 8e                     	movb	$-0x72, %dl
       4: 72 f8                        	jb	0xfffffffe <_start+0xfffffffffffffffe>
       6: 2e 0a 96 c0 a4 cc 53         	orb	%cs:0x53cca4c0(%esi), %dl
       d: 69 0c 57 12 81 13 1f         	imull	$0x1f138112, (%edi,%edx,2), %ecx # imm = 0x1F138112
      14: 67 2a a2 29 e0               	subb	-0x1fd7(%bp,%si), %ah
      19: d4 5a                        	aam	$0x5a
      1b: e5 9b                        	inl	$0x9b, %eax
      1d: 59                           	popl	%ecx
      1e: 8b 59                        	<unknown>
```

## x86_64

```asm
       0: 46 3e                        	ds
       2: b2 8e                        	movb	$-0x72, %dl
       4: 72 f8                        	jb	0xfffffffffffffffe <_start+0xfffffffffffffffe>
       6: 2e 0a 96 c0 a4 cc 53         	orb	%cs:0x53cca4c0(%rsi), %dl
       d: 69 0c 57 12 81 13 1f         	imull	$0x1f138112, (%rdi,%rdx,2), %ecx # imm = 0x1F138112
      14: 67 2a a2 29 e0 d4 5a         	subb	0x5ad4e029(%edx), %ah
      1b: e5 9b                        	inl	$0x9b, %eax
      1d: 59                           	popq	%rcx
      1e: 8b 59                        	<unknown>
```

## armv7

```asm
       0: 8eb23e46     	cdphi	p14, #0xb, c3, c2, c6, #0x2
       4: 0a2ef872     	beq	0xbbe1d4 <_start+0xbbe1d4> @ imm = #0xbbe1c8
       8: cca4c096     	stcgt	p0, c12, [r4], #600
       c: 570c6953     	smlsdpl	r12, r3, r9, r6
      10: 1f138112     	svcne	#0x138112
      14: 29a22a67     	stmibhs	r2!, {r0, r1, r2, r5, r6, r9, r11, sp}
      18: e55ad4e0     	ldrb	sp, [r10, #-0x4e0]
      1c: 598b599b     	stmibpl	r11, {r0, r1, r3, r4, r7, r8, r11, r12, lr}
```

## aarch64

```asm
       0: 46 3e b2 8e  	.word	0x8eb23e46
       4: 72 f8 2e 0a  	.word	0x0a2ef872
       8: 96 c0 a4 cc  	.word	0xcca4c096
       c: 53 69 0c 57  	.word	0x570c6953
      10: 12 81 13 1f  	.word	0x1f138112
      14: 67 2a a2 29  	.word	0x29a22a67
      18: e0 d4 5a e5  	.word	0xe55ad4e0
      1c: 9b 59 8b 59  	.word	0x598b599b
```

## riscv32

```asm
       0: 3e46         	fld	ft8, 0x70(sp)
       2: 8eb2         	mv	t4, a2
       4: f872         	fsw	ft8, 0x30(sp)
       6: 0a2e         	slli	s4, s4, 0xb
       8: c096         	sw	t0, 0x40(sp)
       a: cca4         	sw	s1, 0x58(s1)
       c: 570c6953     	<unknown>
      10: 8112         	mv	sp, tp
      12: 2a671f13     	<unknown>
      16: 29a2         	fld	fs3, 0x8(sp)
      18: d4e0         	sw	s0, 0x6c(s1)
      1a: e55a         	fsw	fs6, 0x88(sp)
      1c: 598b599b     	<unknown>
```

## mips32_be

```asm
       0: 46 3e b2 8e  	<unknown>
       4: 72 f8 2e 0a  	<unknown>
       8: 96 c0 a4 cc  	lhu	$zero, -0x5b34($22)
       c: 53 69 0c 57  	beql	$27, $9, 0x316c <_start+0x316c>
      10: 12 81 13 1f  	beq	$20, $1, 0x4c90 <_start+0x4c90>
      14: 67 2a a2 29  	<unknown>
      18: e0 d4 5a e5  	sc	$20, 0x5ae5($6)
      1c: 9b 59 8b 59  	lwr	$25, -0x74a7($26)
```

## ppc32_be

```asm
       0: 46 3e b2 8e  	sc 20
       4: 72 f8 2e 0a  	andi. 24, 23, 11786
       8: 96 c0 a4 cc  	stwu 22, -23348(0)
       c: 53 69 0c 57  	rlwimi. 9, 27, 1, 17, 11
      10: 12 81 13 1f  	vextddvrx 20, 1, 2, 12
      14: 67 2a a2 29  	oris 10, 25, 41513
      18: e0 d4 5a e5  	<unknown>
      1c: 9b 59 8b 59  	stb 26, -29863(25)
```

## avr

```asm
       0: 46 3e        	cpi	r20, 0xe6
       2: b2 8e        	std	Z+2, r11
       4: 72 f8        	bld	r7, 0x2
       6: 2e 0a        	sbc	r2, r30
       8: 96 c0        	rjmp	.+300
       a: a4 cc        	rjmp	.-1720
       c: 53 69        	ori	r21, 0x93
       e: 0c 57        	subi	r16, 0x7c
      10: 12 81        	ldd	r17, Z+2
      12: 13 1f        	adc	r17, r19
      14: 67 2a        	or	r6, r23
      16: a2 29        	or	r26, r2
      18: e0 d4        	rcall	.+2496
      1a: 5a e5        	ldi	r21, 0x5a
      1c: 9b 59        	subi	r25, 0x9b
      1e: 8b 59        	subi	r24, 0x9b
```

## jvm_bytecode

```text
? istore_3 getstatic ? ? ? ? ? ? ? ? ? ? ? ? pop
```

## wasm_opcode

```text
i32.eq ? ? ? i32.or ? ? ? ? ? ? ? ? ? br ?
```

## cil_bytecode

```text
? ? ? ? ldstr ? beq.s stloc.0 ? ? ? ? ? ? stloc.2 ?
```

## mos6502

```text
? ? ? ? ? ? ? ? ? ? ? ? ? ADC# ? ?
```

# x86_infinite_loop

- input length: 55 bytes
- sha256: `de4c5e300d9c98be56fe9369545a4199b0624dc11a55a53db39eca765e5a6627`

## x86_32

```asm
       0: de 4c 5e 30                  	fimuls	0x30(%esi,%ebx,2)
       4: 0d 9c 98 be 56               	orl	$0x56be989c, %eax       # imm = 0x56BE989C
       9: fe 93 69 54 5a 41            	<unknown>
       f: 99                           	cltd
      10: b0 62                        	movb	$0x62, %al
      12: 4d                           	decl	%ebp
      13: c1 1a 55                     	rcrl	$0x55, (%edx)
      16: a5                           	movsl	(%esi), %es:(%edi)
      17: 3d b3 9e ca 76               	cmpl	$0x76ca9eb3, %eax       # imm = 0x76CA9EB3
      1c: 5e                           	popl	%esi
      1d: 5a                           	popl	%edx
      1e: 66 27                        	daa
```

## x86_64

```asm
       0: de 4c 5e 30                  	fimuls	0x30(%rsi,%rbx,2)
       4: 0d 9c 98 be 56               	orl	$0x56be989c, %eax       # imm = 0x56BE989C
       9: fe 93 69 54 5a 41            	<unknown>
       f: 99                           	cltd
      10: b0 62                        	movb	$0x62, %al
      12: 4d c1 1a 55                  	rcrq	$0x55, (%r10)
      16: a5                           	movsl	(%rsi), %es:(%rdi)
      17: 3d b3 9e ca 76               	cmpl	$0x76ca9eb3, %eax       # imm = 0x76CA9EB3
      1c: 5e                           	popq	%rsi
      1d: 5a                           	popq	%rdx
      1e: 66 27                        	<unknown>
```

## armv7

```asm
       0: 305e4cde     	ldrsblo	r4, [lr], #-206
       4: be989c0d     	cdplt	p12, #0x9, c9, c8, c13, #0x0
       8: 6993fe56     	ldmibvs	r3, {r1, r2, r4, r6, r9, r10, r11, r12, sp, lr, pc}
       c: 99415a54     	stmdbls	r1, {r2, r4, r6, r9, r11, r12, lr} ^
      10: c14d62b0     	strhgt	r6, [sp, #-32]
      14: 3da5551a     	stclo	p5, c5, [r5, #104]!
      18: 76ca9eb3     	<unknown>
      1c: 27665a5e     	<unknown>
```

## aarch64

```asm
       0: de 4c 5e 30  	.word	0x305e4cde
       4: 0d 9c 98 be  	.word	0xbe989c0d
       8: 56 fe 93 69  	.word	0x6993fe56
       c: 54 5a 41 99  	.word	0x99415a54
      10: b0 62 4d c1  	.word	0xc14d62b0
      14: 1a 55 a5 3d  	.word	0x3da5551a
      18: b3 9e ca 76  	.word	0x76ca9eb3
      1c: 5e 5a 66 27  	.word	0x27665a5e
```

## riscv32

```asm
       0: 4cde         	lw	s9, 0xd4(sp)
       2: 305e         	fld	ft0, 0x1f0(sp)
       4: 9c0d         	<unknown>
       6: be98         	fsd	fa4, 0x38(a3)
       8: fe56         	fsw	fs5, 0x3c(sp)
       a: 5a546993     	ori	s3, s0, 0x5a5
       e: 9941         	andi	a0, a0, -0x10
      10: 62b0         	flw	fa2, 0x40(a3)
      12: c14d         	beqz	a0, 0xb4 <_start+0xb4>
      14: 551a         	lw	a0, 0xa4(sp)
      16: 3da5         	jal	0xfffffe8e <_start+0xfffffffffffffe8e>
      18: 76ca9eb3     	<unknown>
      1c: 5a5e         	lw	s4, 0xf4(sp)
      1e: 2766         	fld	fa4, 0x58(sp)
```

## mips32_be

```asm
       0: de 4c 5e 30  	<unknown>
       4: 0d 9c 98 be  	jal	0x67262f8 <_start+0x67262f8>
       8: 56 fe 93 69  	bnel	$23, $fp, 0xfffe4db0 <_start+0xfffffffffffe4db0>
       c: 54 5a 41 99  	bnel	$2, $26, 0x10674 <_start+0x10674>
      10: b0 62 4d c1  	<unknown>
      14: 1a 55 a5 3d  	<unknown>
      18: b3 9e ca 76  	<unknown>
      1c: 5e 5a 66 27  	<unknown>
```

## ppc32_be

```asm
       0: de 4c 5e 30  	stfdu 18, 24112(12)
       4: 0d 9c 98 be  	twi 12, 28, -26434
       8: 56 fe 93 69  	rlwinm. 30, 23, 18, 13, 20
       c: 54 5a 41 99  	rlwinm. 26, 2, 8, 6, 12
      10: b0 62 4d c1  	sth 3, 19905(2)
      14: 1a 55 a5 3d  	<unknown>
      18: b3 9e ca 76  	sth 28, -13706(30)
      1c: 5e 5a 66 27  	rlwnm. 26, 18, 12, 24, 19
```

## avr

```asm
       0: de 4c        	sbci	r29, 0xce
       2: 5e 30        	cpi	r21, 0xe
       4: 0d 9c 98 be  	<unknown>
       8: 56 fe        	sbrs	r5, 0x6
       a: 93 69        	ori	r25, 0x93
       c: 54 5a        	subi	r21, 0xa4
       e: 41 99        	sbic	0x8, 0x1
      10: b0 62        	ori	r27, 0x20
      12: 4d c1        	rjmp	.+666
      14: 1a 55        	subi	r17, 0x5a
      16: a5 3d        	cpi	r26, 0xd5
      18: b3 9e ca 76  	<unknown>
      1c: 5e 5a        	subi	r21, 0xae
      1e: 66 27        	clr	r22
```

## jvm_bytecode

```text
? ? ? ? ? ifge ? ? ? ? ? ? ? ? ? ifeq
```

## wasm_opcode

```text
? ? ? ? br_if ? ? ? ? ? ? ? ? ? i32.const ?
```

## cil_bytecode

```text
? ? ? bgt.s stloc.3 ? ? ? ? ? ? ? ? mul ? ?
```

## mos6502

```text
? JMP ? BMI ? ? ? ? ? ? ? ADC# ? ? ? ?
```

# x86_ret_nops

- input length: 55 bytes
- sha256: `c59cc8b9cd05c52da73dccee4d9a1413258be1cad119a29fa0d4e0c9915bde67`

## x86_32

```asm
       0: c5 9c c8 b9 cd 05 c5         	ldsl	-0x3afa3247(%eax,%ecx,8), %ebx
       7: 2d a7 3d cc ee               	subl	$0xeecc3da7, %eax       # imm = 0xEECC3DA7
       c: 4d                           	decl	%ebp
       d: 9a 14 13 25 8b e1 ca         	lcalll	$-0x351f, $0x8b251314   # imm = 0xCAE1
      14: d1 19                        	rcrl	(%ecx)
      16: a2 9f a0 d4 e0               	movb	%al, 0xe0d4a09f
      1b: c9                           	leave
      1c: 91                           	xchgl	%ecx, %eax
      1d: 5b                           	popl	%ebx
      1e: de 67                        	<unknown>
```

## x86_64

```asm
       0: c5 9c c8                     	<unknown>
       3: b9 cd 05 c5 2d               	movl	$0x2dc505cd, %ecx       # imm = 0x2DC505CD
       8: a7                           	cmpsl	%es:(%rdi), (%rsi)
       9: 3d cc ee 4d 9a               	cmpl	$0x9a4deecc, %eax       # imm = 0x9A4DEECC
       e: 14 13                        	adcb	$0x13, %al
      10: 25 8b e1 ca d1               	andl	$0xd1cae18b, %eax       # imm = 0xD1CAE18B
      15: 19 a2 9f a0 d4 e0            	sbbl	%esp, -0x1f2b5f61(%rdx)
      1b: c9                           	leave
      1c: 91                           	xchgl	%ecx, %eax
      1d: 5b                           	popq	%rbx
      1e: de 67                        	<unknown>
```

## armv7

```asm
       0: b9c89cc5     	stmiblt	r8, {r0, r2, r6, r7, r10, r11, r12, pc} ^
       4: 2dc505cd     	stclhs	p5, c0, [r5, #820]
       8: eecc3da7     	cdp	p13, #0xc, c3, c12, c7, #0x5
       c: 13149a4d     	tstne	r4, #315392
      10: cae18b25     	bgt	0xff862cac <_start+0xffffffffff862cac> @ imm = #-0x79d36c
      14: 9fa219d1     	svcls	#0xa219d1
      18: c9e0d4a0     	stmibgt	r0!, {r5, r7, r10, r12, lr, pc} ^
      1c: 67de5b91     	bfivs	r5, r1, #23, #8
```

## aarch64

```asm
       0: c5 9c c8 b9  	.word	0xb9c89cc5
       4: cd 05 c5 2d  	.word	0x2dc505cd
       8: a7 3d cc ee  	.word	0xeecc3da7
       c: 4d 9a 14 13  	.word	0x13149a4d
      10: 25 8b e1 ca  	.word	0xcae18b25
      14: d1 19 a2 9f  	.word	0x9fa219d1
      18: a0 d4 e0 c9  	.word	0xc9e0d4a0
      1c: 91 5b de 67  	.word	0x67de5b91
```

## riscv32

```asm
       0: 9cc5         	<unknown>
       2: b9c8         	fsd	fa0, 0xb0(a1)
       4: 05cd         	addi	a1, a1, 0x13
       6: 2dc5         	jal	0x6f6 <_start+0x6f6>
       8: eecc3da7     	fsd	fa2, -0x105(s8)
       c: 9a4d         	andi	a2, a2, -0xd
       e: 1314         	addi	a3, sp, 0x1a0
      10: 8b25         	andi	a4, a4, 0x9
      12: cae1         	beqz	a3, 0xe2 <_start+0xe2>
      14: 19d1         	addi	s3, s3, -0xc
      16: 9fa2         	add	t6, t6, s0
      18: d4a0         	sw	s0, 0x68(s1)
      1a: c9e0         	sw	s0, 0x54(a1)
      1c: 5b91         	li	s7, -0x1c
      1e: 67de         	flw	fa5, 0xd4(sp)
```

## mips32_be

```asm
       0: c5 9c c8 b9  	lwc1	$f28, -0x3747($12)
       4: cd 05 c5 2d  	pref	0x5, -0x3ad3($8) <_start+0x5>
       8: a7 3d cc ee  	sh	$sp, -0x3312($25)
       c: 4d 9a 14 13  	<unknown>
      10: 25 8b e1 ca  	addiu	$11, $12, -0x1e36 <_start+0xffffffffffffe1ca>
      14: d1 19 a2 9f  	<unknown>
      18: a0 d4 e0 c9  	sb	$20, -0x1f37($6)
      1c: 91 5b de 67  	lbu	$27, -0x2199($10)
```

## ppc32_be

```asm
       0: c5 9c c8 b9  	lfsu 12, -14151(28)
       4: cd 05 c5 2d  	lfdu 8, -15059(5)
       8: a7 3d cc ee  	lhzu 25, -13074(29)
       c: 4d 9a 14 13  	<unknown>
      10: 25 8b e1 ca  	<unknown>
      14: d1 19 a2 9f  	stfs 8, -23905(25)
      18: a0 d4 e0 c9  	lhz 6, -7991(20)
      1c: 91 5b de 67  	stw 10, -8601(27)
```

## avr

```asm
       0: c5 9c c8 b9  	<unknown>
       4: cd 05        	cpc	r28, r13
       6: c5 2d        	mov	r28, r5
       8: a7 3d        	cpi	r26, 0xd7
       a: cc ee        	ldi	r28, 0xec
       c: 4d 9a        	sbi	0x9, 0x5
       e: 14 13        	cpse	r17, r20
      10: 25 8b        	std	Z+5, r18
      12: e1 ca        	rjmp	.-2622
      14: d1 19        	sub	r29, r1
      16: a2 9f a0 d4  	<unknown>
      1a: e0 c9        	rjmp	.-3136
      1c: 91 5b        	subi	r25, 0xb1
      1e: de 67        	ori	r29, 0x7e
```

## jvm_bytecode

```text
? ifge ? ? ? iconst_2 ? ? goto istore_2 ? ? ? ifne ? ?
```

## wasm_opcode

```text
? ? ? ? ? else ? ? ? ? ? ? ? ? ? ?
```

## cil_bytecode

```text
? ? ? ? ? ldarg.3 ? brtrue.s ? ? ? ? ? ? ldnull stloc.s
```

## mos6502

```text
? ? INY ? ? ? ? ? ? ? ? ? ? ? ? ?
```

# x86_int3_nops

- input length: 55 bytes
- sha256: `bfcf02e2e00b1d0593c559a7cedc65c93024a149f3eac7b4eab8eabf38720eec`

## x86_32

```asm
       0: bf cf 02 e2 e0               	movl	$0xe0e202cf, %edi       # imm = 0xE0E202CF
       5: 0b 1d 05 93 c5 59            	orl	0x59c59305, %ebx
       b: a7                           	cmpsl	%es:(%edi), (%esi)
       c: ce                           	into
       d: dc 65 c9                     	fsubl	-0x37(%ebp)
      10: 30 24 a1                     	xorb	%ah, (%ecx,%eiz,4)
      13: 49                           	decl	%ecx
      14: f3 ea c7 b4 ea b8 ea bf      	rep		ljmpl	$-0x4016, $0xb8eab4c7 # imm = 0xBFEA
      1c: 38 72 0e                     	cmpb	%dh, 0xe(%edx)
      1f: ec                           	inb	%dx, %al
```

## x86_64

```asm
       0: bf cf 02 e2 e0               	movl	$0xe0e202cf, %edi       # imm = 0xE0E202CF
       5: 0b 1d 05 93 c5 59            	orl	0x59c59305(%rip), %ebx  # 0x59c59310 <_start+0x59c59310>
       b: a7                           	cmpsl	%es:(%rdi), (%rsi)
       c: ce                           	<unknown>
       d: dc 65 c9                     	fsubl	-0x37(%rbp)
      10: 30 24 a1                     	xorb	%ah, (%rcx,%riz,4)
      13: 49 f3                        	rep
      15: ea                           	<unknown>
      16: c7 b4 ea b8 ea bf 38         	<unknown>
      1d: 72 0e                        	jb	0x2d <_start+0x2d>
      1f: ec                           	inb	%dx, %al
```

## armv7

```asm
       0: e202cfbf     	and	r12, r2, #764
       4: 051d0be0     	ldreq	r0, [sp, #-0xbe0]
       8: a759c593     	<unknown>
       c: c965dcce     	stmdbgt	r5!, {r1, r2, r3, r6, r7, r10, r11, r12, lr, pc} ^
      10: 49a12430     	stmibmi	r1!, {r4, r5, r10, sp}
      14: b4c7eaf3     	strblt	lr, [r7], #2803
      18: bfeab8ea     	svclt	#0xeab8ea
      1c: ec0e7238     	<unknown>
```

## aarch64

```asm
       0: bf cf 02 e2  	.word	0xe202cfbf
       4: e0 0b 1d 05  	.word	0x051d0be0
       8: 93 c5 59 a7  	.word	0xa759c593
       c: ce dc 65 c9  	.word	0xc965dcce
      10: 30 24 a1 49  	.word	0x49a12430
      14: f3 ea c7 b4  	.word	0xb4c7eaf3
      18: ea b8 ea bf  	.word	0xbfeab8ea
      1c: 38 72 0e ec  	.word	0xec0e7238
```

## riscv32

```asm
       0: e202cfbf 051d0be0    	<unknown>
       8: a759c593     	xori	a1, s3, -0x58b
       c: dcce         	sw	s3, 0x78(sp)
       e: c965         	beqz	a0, 0xfe <_start+0xfe>
      10: 2430         	fld	fa2, 0x48(s0)
      12: 49a1         	li	s3, 0x8
      14: b4c7eaf3     	csrrsi	s5, 0xb4c, 0xf
      18: b8ea         	fsd	fs10, 0x70(sp)
      1a: bfea         	fsd	fs10, 0x1f8(sp)
      1c: 7238         	flw	fa4, 0x60(a2)
      1e: ec0e         	fsw	ft3, 0x18(sp)
```

## mips32_be

```asm
       0: bf cf 02 e2  	cache	0xf, 0x2e2($fp) <_start+0xf>
       4: e0 0b 1d 05  	sc	$11, 0x1d05($zero)
       8: 93 c5 59 a7  	lbu	$5, 0x59a7($fp)
       c: ce dc 65 c9  	pref	0x1c, 0x65c9($22) <_start+0x1c>
      10: 30 24 a1 49  	andi	$4, $1, 0xa149 <_start+0xa149>
      14: f3 ea c7 b4  	<unknown>
      18: ea b8 ea bf  	swc2	$24, -0x1541($21)
      1c: 38 72 0e ec  	xori	$18, $3, 0xeec <_start+0xeec>
```

## ppc32_be

```asm
       0: bf cf 02 e2  	stmw 30, 738(15)
       4: e0 0b 1d 05  	<unknown>
       8: 93 c5 59 a7  	stw 30, 22951(5)
       c: ce dc 65 c9  	lfdu 22, 26057(28)
      10: 30 24 a1 49  	addic 1, 4, -24247
      14: f3 ea c7 b4  	xxsel 31, 42, 24, 30
      18: ea b8 ea bf  	<unknown>
      1c: 38 72 0e ec  	addi 3, 18, 3820
```

## avr

```asm
       0: bf cf        	rjmp	.-130
       2: 02 e2        	ldi	r16, 0x22
       4: e0 0b        	sbc	r30, r16
       6: 1d 05        	cpc	r17, r13
       8: 93 c5        	rjmp	.+2854
       a: 59 a7 ce dc  	<unknown>
       e: 65 c9        	rjmp	.-3382
      10: 30 24        	eor	r3, r0
      12: a1 49        	sbci	r26, 0x91
      14: f3 ea        	ldi	r31, 0xa3
      16: c7 b4        	in	r12, 0x27
      18: ea b8        	out	0xa, r14
      1a: ea bf        	out	0x3a, r30
      1c: 38 72        	andi	r19, 0x28
      1e: 0e ec        	ldi	r16, 0xce
```

## jvm_bytecode

```text
athrow ? iconst_m1 ? ? ? iload_3 iconst_2 ? ? dup goto ? ? ? ?
```

## wasm_opcode

```text
? ? block ? ? end ? else ? ? ? ? ? ? ? ?
```

## cil_bytecode

```text
? ? ldarg.0 ? ? stloc.1 ldc.i4.7 ldarg.3 ? ? sub ? ? ? ? ?
```

## mos6502

```text
? ? ? ? ? ? ? ? ? ? ? ? ? ? ? CMP#
```

# text_calm_instruction

- input length: 36 bytes
- sha256: `528a7f0c1665b719810202954b30afdf358cb9b71f203cf5d957c8e37718ba63`

## x86_32

```asm
       0: 52                           	pushl	%edx
       1: 8a 7f 0c                     	movb	0xc(%edi), %bh
       4: 16                           	pushl	%ss
       5: 65 b7 19                     	movb	$0x19, %bh
       8: 81 02 02 95 4b 30            	addl	$0x304b9502, (%edx)     # imm = 0x304B9502
       e: af                           	scasl	%es:(%edi), %eax
       f: df 35 8c b9 b7 1f            	fbstp	0x1fb7b98c
      15: 20 3c f5 d9 57 c8 e3         	andb	%bh, -0x1c37a827(,%esi,8)
      1c: 77 18                        	ja	0x36 <_start+0x36>
      1e: ba                           	<unknown>
      1f: 63                           	<unknown>
```

## x86_64

```asm
       0: 52                           	pushq	%rdx
       1: 8a 7f 0c                     	movb	0xc(%rdi), %bh
       4: 16                           	<unknown>
       5: 65 b7 19                     	movb	$0x19, %bh
       8: 81 02 02 95 4b 30            	addl	$0x304b9502, (%rdx)     # imm = 0x304B9502
       e: af                           	scasl	%es:(%rdi), %eax
       f: df 35 8c b9 b7 1f            	fbstp	0x1fb7b98c(%rip)        # 0x1fb7b9a1 <_start+0x1fb7b9a1>
      15: 20 3c f5 d9 57 c8 e3         	andb	%bh, -0x1c37a827(,%rsi,8)
      1c: 77 18                        	ja	0x36 <_start+0x36>
      1e: ba                           	<unknown>
      1f: 63                           	<unknown>
```

## armv7

```asm
       0: 0c7f8a52     	<unknown>
       4: 19b76516     	ldmibne	r7!, {r1, r2, r4, r8, r10, sp, lr}
       8: 95020281     	strls	r0, [r2, #-0x281]
       c: dfaf304b     	svcle	#0xaf304b
      10: b7b98c35     	<unknown>
      14: f53c201f     	<unknown>
      18: e3c857d9     	bic	r5, r8, #56885248
      1c: 63ba1877     	<unknown>
```

## aarch64

```asm
       0: 52 8a 7f 0c  	.word	0x0c7f8a52
       4: 16 65 b7 19  	.word	0x19b76516
       8: 81 02 02 95  	.word	0x95020281
       c: 4b 30 af df  	.word	0xdfaf304b
      10: 35 8c b9 b7  	.word	0xb7b98c35
      14: 1f 20 3c f5  	.word	0xf53c201f
      18: d9 57 c8 e3  	.word	0xe3c857d9
      1c: 77 18 ba 63  	.word	0x63ba1877
```

## riscv32

```asm
       0: 8a52         	mv	s4, s4
       2: 0c7f 6516 19b7 0281 9502     	<unknown>
       c: dfaf304b     	<unknown>
      10: 8c35         	xor	s0, s0, a3
      12: b7b9         	j	0xffffff60 <_start+0xffffffffffffff60>
      14: 201f f53c 57d9       	<unknown>
      1a: e3c8         	fsw	fa0, 0x4(a5)
      1c: 63ba1877     	<unknown>
```

## mips32_be

```asm
       0: 52 8a 7f 0c  	beql	$20, $10, 0x1fc34 <_start+0x1fc34>
       4: 16 65 b7 19  	bne	$19, $5, 0xfffedc6c <_start+0xfffffffffffedc6c>
       8: 81 02 02 95  	lb	$2, 0x295($8)
       c: 4b 30 af df  	<unknown>
      10: 35 8c b9 b7  	ori	$12, $12, 0xb9b7 <_start+0xb9b7>
      14: 1f 20 3c f5  	bgtz	$25, 0xf3ec <_start+0xf3ec>
      18: d9 57 c8 e3  	ldc2	$23, -0x371d($10)
      1c: 77 18 ba 63  	jalx	0xc62e98c <_start+0xc62e98c>
```

## ppc32_be

```asm
       0: 52 8a 7f 0c  	rlwimi 10, 20, 15, 28, 6
       4: 16 65 b7 19  	<unknown>
       8: 81 02 02 95  	lwz 8, 661(2)
       c: 4b 30 af df  	bla 0xff30afdc
      10: 35 8c b9 b7  	addic. 12, 12, -17993
      14: 1f 20 3c f5  	mulli 25, 0, 15605
      18: d9 57 c8 e3  	stfd 10, -14109(23)
      1c: 77 18 ba 63  	andis. 24, 24, 47715
```

## avr

```asm
       0: 52 8a        	std	Z+2, r5
       2: 7f 0c        	add	r7, r15
       4: 16 65        	ori	r17, 0x56
       6: b7 19        	sub	r27, r7
       8: 81 02 02 95  	<unknown>
       c: 4b 30        	cpi	r20, 0xb
       e: af df        	rcall	.-162
      10: 35 8c        	ldd	r3, Z+5
      12: b9 b7        	in	r27, 0x39
      14: 1f 20        	and	r1, r15
      16: 3c f5        	brge	.+78
      18: d9 57        	subi	r29, 0x79
      1a: c8 e3        	ldi	r28, 0x38
      1c: 77 18        	sub	r7, r7
      1e: ba 63        	ori	r27, 0x3a
```

## jvm_bytecode

```text
? ? ? ? lload ? invokespecial aload ? iconst_m1 iconst_m1 ? ? ? ? ?
```

## wasm_opcode

```text
? ? ? br ? ? ? ? ? block block ? ? ? ? ?
```

## cil_bytecode

```text
? ? ? stloc.2 ldc.i4.0 ? ? ldc.i4.3 ? ldarg.0 ldarg.0 ? ? bgt.s ? ?
```

## mos6502

```text
? ? ? ? ? ? ? ? ? ? ? ? ? BMI ? ?
```

# text_hard_instruction

- input length: 42 bytes
- sha256: `cf0a6506ea3e224af377d9301adb13e4ab634904389b925b7f788c07a3b0b614`

## x86_32

```asm
       0: cf                           	iretl
       1: 0a 65 06                     	orb	0x6(%ebp), %ah
       4: ea 3e 22 4a f3 77 d9         	ljmpl	$-0x2689, $0xf34a223e   # imm = 0xD977
       b: 30 1a                        	xorb	%bl, (%edx)
       d: db 13                        	fistl	(%ebx)
       f: e4 ab                        	inb	$0xab, %al
      11: 63 49 04                     	arpl	%cx, 0x4(%ecx)
      14: 38 9b 92 5b 7f 78            	cmpb	%bl, 0x787f5b92(%ebx)
      1a: 8c 07                        	movw	%es, (%edi)
      1c: a3                           	<unknown>
      1d: b0 b6                        	movb	$-0x4a, %al
      1f: 14                           	<unknown>
```

## x86_64

```asm
       0: cf                           	iretl
       1: 0a 65 06                     	orb	0x6(%rbp), %ah
       4: ea                           	<unknown>
       5: 3e 22 4a f3                  	andb	%ds:-0xd(%rdx), %cl
       9: 77 d9                        	ja	0xffffffffffffffe4 <_start+0xffffffffffffffe4>
       b: 30 1a                        	xorb	%bl, (%rdx)
       d: db 13                        	fistl	(%rbx)
       f: e4 ab                        	inb	$0xab, %al
      11: 63 49 04                     	movslq	0x4(%rcx), %ecx
      14: 38 9b 92 5b 7f 78            	cmpb	%bl, 0x787f5b92(%rbx)
      1a: 8c 07                        	movw	%es, (%rdi)
      1c: a3                           	<unknown>
      1d: b0 b6                        	movb	$-0x4a, %al
      1f: 14                           	<unknown>
```

## armv7

```asm
       0: 06650acf     	strbteq	r0, [r5], -pc, asr #21
       4: 4a223eea     	bmi	0x88fbb4 <_start+0x88fbb4> @ imm = #0x88fba8
       8: 30d977f3     	ldrshlo	r7, [r9], #115
       c: e413db1a     	ldr	sp, [r3], #-2842
      10: 044963ab     	strbeq	r6, [r9], #-939
      14: 5b929b38     	blpl	0xfe4a6cfc <_start+0xfffffffffe4a6cfc> @ imm = #-0x1b59320
      18: 078c787f     	<unknown>
      1c: 14b6b0a3     	ldrtne	r11, [r6], #163
```

## aarch64

```asm
       0: cf 0a 65 06  	.word	0x06650acf
       4: ea 3e 22 4a  	.word	0x4a223eea
       8: f3 77 d9 30  	.word	0x30d977f3
       c: 1a db 13 e4  	.word	0xe413db1a
      10: ab 63 49 04  	.word	0x044963ab
      14: 38 9b 92 5b  	.word	0x5b929b38
      18: 7f 78 8c 07  	.word	0x078c787f
      1c: a3 b0 b6 14  	.word	0x14b6b0a3
```

## riscv32

```asm
       0: 06650acf     	<unknown>
       4: 3eea         	fld	ft9, 0xb8(sp)
       6: 4a22         	lw	s4, 0x8(sp)
       8: 30d977f3     	csrrci	a5, mstateen1, 0x12
       c: db1a         	sw	t1, 0xb4(sp)
       e: 63abe413     	ori	s0, s7, 0x63a
      12: 0449         	addi	s0, s0, 0x12
      14: 9b38         	<unknown>
      16: 5b92         	lw	s7, 0x24(sp)
      18: 7f           	<unknown>
      19: 8c78         	<unknown>
      1b: b6b0a307     	flw	ft6, -0x495(ra)
      1f: 14           	<unknown>
```

## mips32_be

```asm
       0: cf 0a 65 06  	pref	0xa, 0x6506($24) <_start+0xa>
       4: ea 3e 22 4a  	swc2	$30, 0x224a($17)
       8: f3 77 d9 30  	<unknown>
       c: 1a db 13 e4  	<unknown>
      10: ab 63 49 04  	swl	$3, 0x4904($27)
      14: 38 9b 92 5b  	xori	$27, $4, 0x925b <_start+0x925b>
      18: 7f 78 8c 07  	<unknown>
      1c: a3 b0 b6 14  	sb	$16, -0x49ec($sp)
```

## ppc32_be

```asm
       0: cf 0a 65 06  	lfdu 24, 25862(10)
       4: ea 3e 22 4a  	lwa 17, 8776(30)
       8: f3 77 d9 30  	xxsel 27, 23, 27, 4
       c: 1a db 13 e4  	<unknown>
      10: ab 63 49 04  	lha 27, 18692(3)
      14: 38 9b 92 5b  	addi 4, 27, -28069
      18: 7f 78 8c 07  	<unknown>
      1c: a3 b0 b6 14  	lhz 29, -18924(16)
```

## avr

```asm
       0: cf 0a        	sbc	r12, r31
       2: 65 06        	cpc	r6, r21
       4: ea 3e        	cpi	r30, 0xea
       6: 22 4a        	sbci	r18, 0xa2
       8: f3 77        	andi	r31, 0x73
       a: d9 30        	cpi	r29, 0x9
       c: 1a db        	rcall	.-2508
       e: 13 e4        	ldi	r17, 0x43
      10: ab 63        	ori	r26, 0x3b
      12: 49 04        	cpc	r4, r9
      14: 38 9b        	sbis	0x7, 0x0
      16: 92 5b        	subi	r25, 0xb2
      18: 7f 78        	andi	r23, 0x8f
      1a: 8c 07        	cpc	r24, r28
      1c: a3 b0        	in	r10, 0x3
      1e: b6 14        	cp	r11, r6
```

## jvm_bytecode

```text
? ? ? iconst_3 ? istore_3 ? ? ? ? ? ? iload_0 ? ? ?
```

## wasm_opcode

```text
? ? ? ? ? ? local.tee ? ? ? ? ? ? ? ? ?
```

## cil_bytecode

```text
? stloc.0 ? ldloc.0 ? ? ? ? ? ? ? bgt.s ldc.i4.4 ? stloc.s ?
```

## mos6502

```text
? ? ? ? NOP ? ? ? ? ? ? BMI ? ? ? ?
```

