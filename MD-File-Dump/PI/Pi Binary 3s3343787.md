17ded6e69bc62c7196b1e93a4b3713243767de04ab0367fe35e18d358206c55f
0:  17                      pop    ss
1:  de d6                   (bad)
3:  e6 9b                   out    0x9b,al
5:  c6                      (bad)
6:  2c 71                   sub    al,0x71
8:  96                      xchg   esi,eax
9:  b1 e9                   mov    cl,0xe9
b:  3a 4b 37                cmp    cl,BYTE PTR [ebx+0x37]
e:  13 24 37                adc    esp,DWORD PTR [edi+esi*1]
11: 67 de 04                fiadd  WORD PTR [si]
14: ab                      stos   DWORD PTR es:[edi],eax
15: 03 67 fe                add    esp,DWORD PTR [edi-0x2]
18: 35 e1 8d 35 82          xor    eax,0x82358de1
1d: 06                      push   es
1e: c5                      .byte 0xc5
1f: 5f                      pop    edi
Now we convert the Hash. we treat it as Text and convert it to hex to get this value
31376465643665363962633632633731393662316539336134623337313332343337363764653034616230333637666533356531386433353832303663353566

Now since the hash is circular, we fold it.  
31 37 64 65 64 36 65 36 39 62 63 36 32 63 37 31 39 36 62 31 65 39 33 61 34 62 33 37 31 33 32 34  first half
66 53 53 36 63 03 23 83 53 33 46 83 13 56 53 33 56 66 73 63 33 03 26 16 43 03 56 46 73 63 73 33  second half reversed (reflected)

Then we add it to get this number.

9791180227398919929610194619906496033594984259777765898404970567  (add the first to the second) Then Text to Binary.
Then we convert it to Binary.
1001011110010001000110000000001000100111001110011000100100011001100100101001011000010000000110010100011000011001100100000110010010010110000000110011010110010100100110000100001001011001011101110111011101100101100010011000010000000100100101110000010101100111

Then we treat that as text and convert it to Hex:
31303031303131313130303130303031303030313130303030303030303031303030313030313131303031313130303131303030313030313030303131303031313030313030313031303031303131303030303130303030303030313130303130313030303131303030303131303031313030313030303030313130303130303130303130313130303030303030313130303131303130313130303130313030313030313130303030313030303031303031303131303031303131313031313130313131303131313031313030313031313030303130303131303030303130303030303030313030313030313031313130303030303130313031313030313131

Now if we remove the 3's we get the original binary back.
1001011110010001000110000000001000100111001110011000100100011001100100101001011000010000000110010100011000011001100100000110010010010110000000110011010110010100100110000100001001011001011101110111011101100101100010011000010000000100100101110000010101100111

SO there is something going on here. a hidden code that were seeing.  Converting 'binary' (that is, it's binary becuase it was the output of a Text to Binary function) to HEX, the hex knows what im sending it for some reason. becuase all it did was ADD what was missing, NOT convert the data.  THIS IS CRACK IN THE SYSTEM.

Raw Hex (zero bytes in bold):

31376465643665363962633632633731393662316539336134623337313332343337363764653034616230333637666533356531386433353832303663353566   

String Literal:

"\x31\x37\x64\x65\x64\x36\x65\x36\x39\x62\x63\x36\x32\x63\x37\x31\x39\x36\x62\x31\x65\x39\x33\x61\x34\x62\x33\x37\x31\x33\x32\x34\x33\x37\x36\x37\x64\x65\x30\x34\x61\x62\x30\x33\x36\x37\x66\x65\x33\x35\x65\x31\x38\x64\x33\x35\x38\x32\x30\x36\x63\x35\x35\x66"

Array Literal:

{ 0x31, 0x37, 0x64, 0x65, 0x64, 0x36, 0x65, 0x36, 0x39, 0x62, 0x63, 0x36, 0x32, 0x63, 0x37, 0x31, 0x39, 0x36, 0x62, 0x31, 0x65, 0x39, 0x33, 0x61, 0x34, 0x62, 0x33, 0x37, 0x31, 0x33, 0x32, 0x34, 0x33, 0x37, 0x36, 0x37, 0x64, 0x65, 0x30, 0x34, 0x61, 0x62, 0x30, 0x33, 0x36, 0x37, 0x66, 0x65, 0x33, 0x35, 0x65, 0x31, 0x38, 0x64, 0x33, 0x35, 0x38, 0x32, 0x30, 0x36, 0x63, 0x35, 0x35, 0x66 }

Disassembly:
0:  31 37                   xor    DWORD PTR [edi],esi
2:  64 65 64 36 65 36 39    fs gs fs ss gs cmp DWORD PTR ss:[edx+0x63],esp
9:  62 63
b:  36 32 63 37             xor    ah,BYTE PTR ss:[ebx+0x37]
f:  31 39                   xor    DWORD PTR [ecx],edi
11: 36 62 31                bound  esi,QWORD PTR ss:[ecx]
14: 65 39 33                cmp    DWORD PTR gs:[ebx],esi
17: 61                      popa
18: 34 62                   xor    al,0x62
1a: 33 37                   xor    esi,DWORD PTR [edi]
1c: 31 33                   xor    DWORD PTR [ebx],esi
1e: 32 34 33                xor    dh,BYTE PTR [ebx+esi*1]
21: 37                      aaa
22: 36 37                   ss aaa
24: 64 65 30 34 61          fs xor BYTE PTR gs:[ecx+eiz*2],dh
29: 62 30                   bound  esi,QWORD PTR [eax]
2b: 33 36                   xor    esi,DWORD PTR [esi]
2d: 37                      aaa
2e: 66 65 33 35 65 31 38    xor    si,WORD PTR gs:0x64383165
35: 64
36: 33 35 38 32 30 36       xor    esi,DWORD PTR ds:0x36303238
3c: 63                      .byte 0x63
3d: 35                      .byte 0x35
3e: 35                      .byte 0x35
3f: 66                      data16Raw Hex (zero bytes in bold):

9791180227398919929610194619906496033594984259777765898404970567   

String Literal:

"\x97\x91\x18\x02\x27\x39\x89\x19\x92\x96\x10\x19\x46\x19\x90\x64\x96\x03\x35\x94\x98\x42\x59\x77\x77\x65\x89\x84\x04\x97\x05\x67"

Array Literal:

{ 0x97, 0x91, 0x18, 0x02, 0x27, 0x39, 0x89, 0x19, 0x92, 0x96, 0x10, 0x19, 0x46, 0x19, 0x90, 0x64, 0x96, 0x03, 0x35, 0x94, 0x98, 0x42, 0x59, 0x77, 0x77, 0x65, 0x89, 0x84, 0x04, 0x97, 0x05, 0x67 }

Disassembly:
0:  97                      xchg   edi,eax
1:  91                      xchg   ecx,eax
2:  18 02                   sbb    BYTE PTR [edx],al
4:  27                      daa
5:  39 89 19 92 96 10       cmp    DWORD PTR [ecx+0x10969219],ecx
b:  19 46 19                sbb    DWORD PTR [esi+0x19],eax
e:  90                      nop
f:  64 96                   fs xchg esi,eax
11: 03 35 94 98 42 59       add    esi,DWORD PTR ds:0x59429894
17: 77 77                   ja     0x90
19: 65                      gs
1a: 89                      .byte 0x89
1b: 84 04 97                test   BYTE PTR [edi+edx*4],al
1e: 05                      .byte 0x5
1f: 67                      addr16Raw Hex (zero bytes in bold):

31303031303131313130303130303031303030313130303030303030303031303030313030313131303031313130303131303030313030313030303131303031313030313030313031303031303131303030303130303030303030313130303130313030303131303030303131303031313030313030303030313130303130303130303130313130303030303030313130303131303130313130303130313030313030313130303030313030303031303031303131303031303131313031313130313131303131313031313030313031313030303130303131303030303130303030303030313030313030313031313130303030303130313031313030313131   

String Literal:

"\x31\x30\x30\x31\x30\x31\x31\x31\x31\x30\x30\x31\x30\x30\x30\x31\x30\x30\x30\x31\x31\x30\x30\x30\x30\x30\x30\x30\x30\x30\x31\x30\x30\x30\x31\x30\x30\x31\x31\x31\x30\x30\x31\x31\x31\x30\x30\x31\x31\x30\x30\x30\x31\x30\x30\x31\x30\x30\x30\x31\x31\x30\x30\x31\x31\x30\x30\x31\x30\x30\x31\x30\x31\x30\x30\x31\x30\x31\x31\x30\x30\x30\x30\x31\x30\x30\x30\x30\x30\x30\x30\x31\x31\x30\x30\x31\x30\x31\x30\x30\x30\x31\x31\x30\x30\x30\x30\x31\x31\x30\x30\x31\x31\x30\x30\x31\x30\x30\x30\x30\x30\x31\x31\x30\x30\x31\x30\x30\x31\x30\x30\x31\x30\x31\x31\x30\x30\x30\x30\x30\x30\x30\x31\x31\x30\x30\x31\x31\x30\x31\x30\x31\x31\x30\x30\x31\x30\x31\x30\x30\x31\x30\x30\x31\x31\x30\x30\x30\x30\x31\x30\x30\x30\x30\x31\x30\x30\x31\x30\x31\x31\x30\x30\x31\x30\x31\x31\x31\x30\x31\x31\x31\x30\x31\x31\x31\x30\x31\x31\x31\x30\x31\x31\x30\x30\x31\x30\x31\x31\x30\x30\x30\x31\x30\x30\x31\x31\x30\x30\x30\x30\x31\x30\x30\x30\x30\x30\x30\x30\x31\x30\x30\x31\x30\x30\x31\x30\x31\x31\x31\x30\x30\x30\x30\x30\x31\x30\x31\x30\x31\x31\x30\x30\x31\x31\x31"

Array Literal:

{ 0x31, 0x30, 0x30, 0x31, 0x30, 0x31, 0x31, 0x31, 0x31, 0x30, 0x30, 0x31, 0x30, 0x30, 0x30, 0x31, 0x30, 0x30, 0x30, 0x31, 0x31, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x31, 0x30, 0x30, 0x30, 0x31, 0x30, 0x30, 0x31, 0x31, 0x31, 0x30, 0x30, 0x31, 0x31, 0x31, 0x30, 0x30, 0x31, 0x31, 0x30, 0x30, 0x30, 0x31, 0x30, 0x30, 0x31, 0x30, 0x30, 0x30, 0x31, 0x31, 0x30, 0x30, 0x31, 0x31, 0x30, 0x30, 0x31, 0x30, 0x30, 0x31, 0x30, 0x31, 0x30, 0x30, 0x31, 0x30, 0x31, 0x31, 0x30, 0x30, 0x30, 0x30, 0x31, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x31, 0x31, 0x30, 0x30, 0x31, 0x30, 0x31, 0x30, 0x30, 0x30, 0x31, 0x31, 0x30, 0x30, 0x30, 0x30, 0x31, 0x31, 0x30, 0x30, 0x31, 0x31, 0x30, 0x30, 0x31, 0x30, 0x30, 0x30, 0x30, 0x30, 0x31, 0x31, 0x30, 0x30, 0x31, 0x30, 0x30, 0x31, 0x30, 0x30, 0x31, 0x30, 0x31, 0x31, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x31, 0x31, 0x30, 0x30, 0x31, 0x31, 0x30, 0x31, 0x30, 0x31, 0x31, 0x30, 0x30, 0x31, 0x30, 0x31, 0x30, 0x30, 0x31, 0x30, 0x30, 0x31, 0x31, 0x30, 0x30, 0x30, 0x30, 0x31, 0x30, 0x30, 0x30, 0x30, 0x31, 0x30, 0x30, 0x31, 0x30, 0x31, 0x31, 0x30, 0x30, 0x31, 0x30, 0x31, 0x31, 0x31, 0x30, 0x31, 0x31, 0x31, 0x30, 0x31, 0x31, 0x31, 0x30, 0x31, 0x31, 0x31, 0x30, 0x31, 0x31, 0x30, 0x30, 0x31, 0x30, 0x31, 0x31, 0x30, 0x30, 0x30, 0x31, 0x30, 0x30, 0x31, 0x31, 0x30, 0x30, 0x30, 0x30, 0x31, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x31, 0x30, 0x30, 0x31, 0x30, 0x30, 0x31, 0x30, 0x31, 0x31, 0x31, 0x30, 0x30, 0x30, 0x30, 0x30, 0x31, 0x30, 0x31, 0x30, 0x31, 0x31, 0x30, 0x30, 0x31, 0x31, 0x31 }

Disassembly:
0:  31 30                   xor    DWORD PTR [eax],esi
2:  30 31                   xor    BYTE PTR [ecx],dh
4:  30 31                   xor    BYTE PTR [ecx],dh
6:  31 31                   xor    DWORD PTR [ecx],esi
8:  31 30                   xor    DWORD PTR [eax],esi
a:  30 31                   xor    BYTE PTR [ecx],dh
c:  30 30                   xor    BYTE PTR [eax],dh
e:  30 31                   xor    BYTE PTR [ecx],dh
10: 30 30                   xor    BYTE PTR [eax],dh
12: 30 31                   xor    BYTE PTR [ecx],dh
14: 31 30                   xor    DWORD PTR [eax],esi
16: 30 30                   xor    BYTE PTR [eax],dh
18: 30 30                   xor    BYTE PTR [eax],dh
1a: 30 30                   xor    BYTE PTR [eax],dh
1c: 30 30                   xor    BYTE PTR [eax],dh
1e: 31 30                   xor    DWORD PTR [eax],esi
20: 30 30                   xor    BYTE PTR [eax],dh
22: 31 30                   xor    DWORD PTR [eax],esi
24: 30 31                   xor    BYTE PTR [ecx],dh
26: 31 31                   xor    DWORD PTR [ecx],esi
28: 30 30                   xor    BYTE PTR [eax],dh
2a: 31 31                   xor    DWORD PTR [ecx],esi
2c: 31 30                   xor    DWORD PTR [eax],esi
2e: 30 31                   xor    BYTE PTR [ecx],dh
30: 31 30                   xor    DWORD PTR [eax],esi
32: 30 30                   xor    BYTE PTR [eax],dh
34: 31 30                   xor    DWORD PTR [eax],esi
36: 30 31                   xor    BYTE PTR [ecx],dh
38: 30 30                   xor    BYTE PTR [eax],dh
3a: 30 31                   xor    BYTE PTR [ecx],dh
3c: 31 30                   xor    DWORD PTR [eax],esi
3e: 30 31                   xor    BYTE PTR [ecx],dh
40: 31 30                   xor    DWORD PTR [eax],esi
42: 30 31                   xor    BYTE PTR [ecx],dh
44: 30 30                   xor    BYTE PTR [eax],dh
46: 31 30                   xor    DWORD PTR [eax],esi
48: 31 30                   xor    DWORD PTR [eax],esi
4a: 30 31                   xor    BYTE PTR [ecx],dh
4c: 30 31                   xor    BYTE PTR [ecx],dh
4e: 31 30                   xor    DWORD PTR [eax],esi
50: 30 30                   xor    BYTE PTR [eax],dh
52: 30 31                   xor    BYTE PTR [ecx],dh
54: 30 30                   xor    BYTE PTR [eax],dh
56: 30 30                   xor    BYTE PTR [eax],dh
58: 30 30                   xor    BYTE PTR [eax],dh
5a: 30 31                   xor    BYTE PTR [ecx],dh
5c: 31 30                   xor    DWORD PTR [eax],esi
5e: 30 31                   xor    BYTE PTR [ecx],dh
60: 30 31                   xor    BYTE PTR [ecx],dh
62: 30 30                   xor    BYTE PTR [eax],dh
64: 30 31                   xor    BYTE PTR [ecx],dh
66: 31 30                   xor    DWORD PTR [eax],esi
68: 30 30                   xor    BYTE PTR [eax],dh
6a: 30 31                   xor    BYTE PTR [ecx],dh
6c: 31 30                   xor    DWORD PTR [eax],esi
6e: 30 31                   xor    BYTE PTR [ecx],dh
70: 31 30                   xor    DWORD PTR [eax],esi
72: 30 31                   xor    BYTE PTR [ecx],dh
74: 30 30                   xor    BYTE PTR [eax],dh
76: 30 30                   xor    BYTE PTR [eax],dh
78: 30 31                   xor    BYTE PTR [ecx],dh
7a: 31 30                   xor    DWORD PTR [eax],esi
7c: 30 31                   xor    BYTE PTR [ecx],dh
7e: 30 30                   xor    BYTE PTR [eax],dh
80: 31 30                   xor    DWORD PTR [eax],esi
82: 30 31                   xor    BYTE PTR [ecx],dh
84: 30 31                   xor    BYTE PTR [ecx],dh
86: 31 30                   xor    DWORD PTR [eax],esi
88: 30 30                   xor    BYTE PTR [eax],dh
8a: 30 30                   xor    BYTE PTR [eax],dh
8c: 30 30                   xor    BYTE PTR [eax],dh
8e: 31 31                   xor    DWORD PTR [ecx],esi
90: 30 30                   xor    BYTE PTR [eax],dh
92: 31 31                   xor    DWORD PTR [ecx],esi
94: 30 31                   xor    BYTE PTR [ecx],dh
96: 30 31                   xor    BYTE PTR [ecx],dh
98: 31 30                   xor    DWORD PTR [eax],esi
9a: 30 31                   xor    BYTE PTR [ecx],dh
9c: 30 31                   xor    BYTE PTR [ecx],dh
9e: 30 30                   xor    BYTE PTR [eax],dh
a0: 31 30                   xor    DWORD PTR [eax],esi
a2: 30 31                   xor    BYTE PTR [ecx],dh
a4: 31 30                   xor    DWORD PTR [eax],esi
a6: 30 30                   xor    BYTE PTR [eax],dh
a8: 30 31                   xor    BYTE PTR [ecx],dh
aa: 30 30                   xor    BYTE PTR [eax],dh
ac: 30 30                   xor    BYTE PTR [eax],dh
ae: 31 30                   xor    DWORD PTR [eax],esi
b0: 30 31                   xor    BYTE PTR [ecx],dh
b2: 30 31                   xor    BYTE PTR [ecx],dh
b4: 31 30                   xor    DWORD PTR [eax],esi
b6: 30 31                   xor    BYTE PTR [ecx],dh
b8: 30 31                   xor    BYTE PTR [ecx],dh
ba: 31 31                   xor    DWORD PTR [ecx],esi
bc: 30 31                   xor    BYTE PTR [ecx],dh
be: 31 31                   xor    DWORD PTR [ecx],esi
c0: 30 31                   xor    BYTE PTR [ecx],dh
c2: 31 31                   xor    DWORD PTR [ecx],esi
c4: 30 31                   xor    BYTE PTR [ecx],dh
c6: 31 31                   xor    DWORD PTR [ecx],esi
c8: 30 31                   xor    BYTE PTR [ecx],dh
ca: 31 30                   xor    DWORD PTR [eax],esi
cc: 30 31                   xor    BYTE PTR [ecx],dh
ce: 30 31                   xor    BYTE PTR [ecx],dh
d0: 31 30                   xor    DWORD PTR [eax],esi
d2: 30 30                   xor    BYTE PTR [eax],dh
d4: 31 30                   xor    DWORD PTR [eax],esi
d6: 30 31                   xor    BYTE PTR [ecx],dh
d8: 31 30                   xor    DWORD PTR [eax],esi
da: 30 30                   xor    BYTE PTR [eax],dh
dc: 30 31                   xor    BYTE PTR [ecx],dh
de: 30 30                   xor    BYTE PTR [eax],dh
e0: 30 30                   xor    BYTE PTR [eax],dh
e2: 30 30                   xor    BYTE PTR [eax],dh
e4: 30 31                   xor    BYTE PTR [ecx],dh
e6: 30 30                   xor    BYTE PTR [eax],dh
e8: 31 30                   xor    DWORD PTR [eax],esi
ea: 30 31                   xor    BYTE PTR [ecx],dh
ec: 30 31                   xor    BYTE PTR [ecx],dh
ee: 31 31                   xor    DWORD PTR [ecx],esi
f0: 30 30                   xor    BYTE PTR [eax],dh
f2: 30 30                   xor    BYTE PTR [eax],dh
f4: 30 31                   xor    BYTE PTR [ecx],dh
f6: 30 31                   xor    BYTE PTR [ecx],dh
f8: 30 31                   xor    BYTE PTR [ecx],dh
fa: 31 30                   xor    DWORD PTR [eax],esi
fc: 30 31                   xor    BYTE PTR [ecx],dh
fe: 31 31                   xor    DWORD PTR [ecx],esi3515887098665847137083468093160217301131676392550841230942304099
This value is subtracting the inintal convereted hash text to hex instead of adding.
Disassembly
Raw Hex (zero bytes in bold):

3515887098665847137083468093160217301131676392550841230942304099   

String Literal:

"\x35\x15\x88\x70\x98\x66\x58\x47\x13\x70\x83\x46\x80\x93\x16\x02\x17\x30\x11\x31\x67\x63\x92\x55\x08\x41\x23\x09\x42\x30\x40\x99"

Array Literal:

{ 0x35, 0x15, 0x88, 0x70, 0x98, 0x66, 0x58, 0x47, 0x13, 0x70, 0x83, 0x46, 0x80, 0x93, 0x16, 0x02, 0x17, 0x30, 0x11, 0x31, 0x67, 0x63, 0x92, 0x55, 0x08, 0x41, 0x23, 0x09, 0x42, 0x30, 0x40, 0x99 }

Disassembly:
0:  35 15 88 70 98          xor    eax,0x98708815
5:  66 58                   pop    ax
7:  47                      inc    edi
8:  13 70 83                adc    esi,DWORD PTR [eax-0x7d]
b:  46                      inc    esi
c:  80 93 16 02 17 30 11    adc    BYTE PTR [ebx+0x30170216],0x11
13: 31 67 63                xor    DWORD PTR [edi+0x63],esp
16: 92                      xchg   edx,eax
17: 55                      push   ebp
18: 08 41 23                or     BYTE PTR [ecx+0x23],al
1b: 09 42 30                or     DWORD PTR [edx+0x30],eax
1e: 40                      inc    eax
1f: 99                      cdqFIRST 1000 digits of pi without 3.  converted from text to hex and dissasembled 

Disassembly
Raw Hex (zero bytes in bold):

34313539323635333520383937393332333834362032363433333833323739203530323838343139373120363933393933373531302035383230393734393434203539323330373831363420303632383632303839392038363238303334383235203334323131373036373920383231343830383635312033323832333036363437203039333834343630393520353035383232333137322035333539343038313238203438313131373435303220383431303237303139332038353231313035353539203634343632323934383920353439333033383139362034343238383130393735203636353933333434363120323834373536343832332033373836373833313635203237313230313930393120343536343835363639322033343630333438363130203435343332363634383220   

String Literal:

"\x34\x31\x35\x39\x32\x36\x35\x33\x35\x20\x38\x39\x37\x39\x33\x32\x33\x38\x34\x36\x20\x32\x36\x34\x33\x33\x38\x33\x32\x37\x39\x20\x35\x30\x32\x38\x38\x34\x31\x39\x37\x31\x20\x36\x39\x33\x39\x39\x33\x37\x35\x31\x30\x20\x35\x38\x32\x30\x39\x37\x34\x39\x34\x34\x20\x35\x39\x32\x33\x30\x37\x38\x31\x36\x34\x20\x30\x36\x32\x38\x36\x32\x30\x38\x39\x39\x20\x38\x36\x32\x38\x30\x33\x34\x38\x32\x35\x20\x33\x34\x32\x31\x31\x37\x30\x36\x37\x39\x20\x38\x32\x31\x34\x38\x30\x38\x36\x35\x31\x20\x33\x32\x38\x32\x33\x30\x36\x36\x34\x37\x20\x30\x39\x33\x38\x34\x34\x36\x30\x39\x35\x20\x35\x30\x35\x38\x32\x32\x33\x31\x37\x32\x20\x35\x33\x35\x39\x34\x30\x38\x31\x32\x38\x20\x34\x38\x31\x31\x31\x37\x34\x35\x30\x32\x20\x38\x34\x31\x30\x32\x37\x30\x31\x39\x33\x20\x38\x35\x32\x31\x31\x30\x35\x35\x35\x39\x20\x36\x34\x34\x36\x32\x32\x39\x34\x38\x39\x20\x35\x34\x39\x33\x30\x33\x38\x31\x39\x36\x20\x34\x34\x32\x38\x38\x31\x30\x39\x37\x35\x20\x36\x36\x35\x39\x33\x33\x34\x34\x36\x31\x20\x32\x38\x34\x37\x35\x36\x34\x38\x32\x33\x20\x33\x37\x38\x36\x37\x38\x33\x31\x36\x35\x20\x32\x37\x31\x32\x30\x31\x39\x30\x39\x31\x20\x34\x35\x36\x34\x38\x35\x36\x36\x39\x32\x20\x33\x34\x36\x30\x33\x34\x38\x36\x31\x30\x20\x34\x35\x34\x33\x32\x36\x36\x34\x38\x32\x20"

Array Literal:

{ 0x34, 0x31, 0x35, 0x39, 0x32, 0x36, 0x35, 0x33, 0x35, 0x20, 0x38, 0x39, 0x37, 0x39, 0x33, 0x32, 0x33, 0x38, 0x34, 0x36, 0x20, 0x32, 0x36, 0x34, 0x33, 0x33, 0x38, 0x33, 0x32, 0x37, 0x39, 0x20, 0x35, 0x30, 0x32, 0x38, 0x38, 0x34, 0x31, 0x39, 0x37, 0x31, 0x20, 0x36, 0x39, 0x33, 0x39, 0x39, 0x33, 0x37, 0x35, 0x31, 0x30, 0x20, 0x35, 0x38, 0x32, 0x30, 0x39, 0x37, 0x34, 0x39, 0x34, 0x34, 0x20, 0x35, 0x39, 0x32, 0x33, 0x30, 0x37, 0x38, 0x31, 0x36, 0x34, 0x20, 0x30, 0x36, 0x32, 0x38, 0x36, 0x32, 0x30, 0x38, 0x39, 0x39, 0x20, 0x38, 0x36, 0x32, 0x38, 0x30, 0x33, 0x34, 0x38, 0x32, 0x35, 0x20, 0x33, 0x34, 0x32, 0x31, 0x31, 0x37, 0x30, 0x36, 0x37, 0x39, 0x20, 0x38, 0x32, 0x31, 0x34, 0x38, 0x30, 0x38, 0x36, 0x35, 0x31, 0x20, 0x33, 0x32, 0x38, 0x32, 0x33, 0x30, 0x36, 0x36, 0x34, 0x37, 0x20, 0x30, 0x39, 0x33, 0x38, 0x34, 0x34, 0x36, 0x30, 0x39, 0x35, 0x20, 0x35, 0x30, 0x35, 0x38, 0x32, 0x32, 0x33, 0x31, 0x37, 0x32, 0x20, 0x35, 0x33, 0x35, 0x39, 0x34, 0x30, 0x38, 0x31, 0x32, 0x38, 0x20, 0x34, 0x38, 0x31, 0x31, 0x31, 0x37, 0x34, 0x35, 0x30, 0x32, 0x20, 0x38, 0x34, 0x31, 0x30, 0x32, 0x37, 0x30, 0x31, 0x39, 0x33, 0x20, 0x38, 0x35, 0x32, 0x31, 0x31, 0x30, 0x35, 0x35, 0x35, 0x39, 0x20, 0x36, 0x34, 0x34, 0x36, 0x32, 0x32, 0x39, 0x34, 0x38, 0x39, 0x20, 0x35, 0x34, 0x39, 0x33, 0x30, 0x33, 0x38, 0x31, 0x39, 0x36, 0x20, 0x34, 0x34, 0x32, 0x38, 0x38, 0x31, 0x30, 0x39, 0x37, 0x35, 0x20, 0x36, 0x36, 0x35, 0x39, 0x33, 0x33, 0x34, 0x34, 0x36, 0x31, 0x20, 0x32, 0x38, 0x34, 0x37, 0x35, 0x36, 0x34, 0x38, 0x32, 0x33, 0x20, 0x33, 0x37, 0x38, 0x36, 0x37, 0x38, 0x33, 0x31, 0x36, 0x35, 0x20, 0x32, 0x37, 0x31, 0x32, 0x30, 0x31, 0x39, 0x30, 0x39, 0x31, 0x20, 0x34, 0x35, 0x36, 0x34, 0x38, 0x35, 0x36, 0x36, 0x39, 0x32, 0x20, 0x33, 0x34, 0x36, 0x30, 0x33, 0x34, 0x38, 0x36, 0x31, 0x30, 0x20, 0x34, 0x35, 0x34, 0x33, 0x32, 0x36, 0x36, 0x34, 0x38, 0x32, 0x20 }

Disassembly:
0:  34 31                   xor    al,0x31
2:  35 39 32 36 35          xor    eax,0x35363239
7:  33 35 20 38 39 37       xor    esi,DWORD PTR ds:0x37393820
d:  39 33                   cmp    DWORD PTR [ebx],esi
f:  32 33                   xor    dh,BYTE PTR [ebx]
11: 38 34 36                cmp    BYTE PTR [esi+esi*1],dh
14: 20 32                   and    BYTE PTR [edx],dh
16: 36 34 33                ss xor al,0x33
19: 33 38                   xor    edi,DWORD PTR [eax]
1b: 33 32                   xor    esi,DWORD PTR [edx]
1d: 37                      aaa
1e: 39 20                   cmp    DWORD PTR [eax],esp
20: 35 30 32 38 38          xor    eax,0x38383230
25: 34 31                   xor    al,0x31
27: 39 37                   cmp    DWORD PTR [edi],esi
29: 31 20                   xor    DWORD PTR [eax],esp
2b: 36 39 33                cmp    DWORD PTR ss:[ebx],esi
2e: 39 39                   cmp    DWORD PTR [ecx],edi
30: 33 37                   xor    esi,DWORD PTR [edi]
32: 35 31 30 20 35          xor    eax,0x35203031
37: 38 32                   cmp    BYTE PTR [edx],dh
39: 30 39                   xor    BYTE PTR [ecx],bh
3b: 37                      aaa
3c: 34 39                   xor    al,0x39
3e: 34 34                   xor    al,0x34
40: 20 35 39 32 33 30       and    BYTE PTR ds:0x30333239,dh
46: 37                      aaa
47: 38 31                   cmp    BYTE PTR [ecx],dh
49: 36 34 20                ss xor al,0x20
4c: 30 36                   xor    BYTE PTR [esi],dh
4e: 32 38                   xor    bh,BYTE PTR [eax]
50: 36 32 30                xor    dh,BYTE PTR ss:[eax]
53: 38 39                   cmp    BYTE PTR [ecx],bh
55: 39 20                   cmp    DWORD PTR [eax],esp
57: 38 36                   cmp    BYTE PTR [esi],dh
59: 32 38                   xor    bh,BYTE PTR [eax]
5b: 30 33                   xor    BYTE PTR [ebx],dh
5d: 34 38                   xor    al,0x38
5f: 32 35 20 33 34 32       xor    dh,BYTE PTR ds:0x32343320
65: 31 31                   xor    DWORD PTR [ecx],esi
67: 37                      aaa
68: 30 36                   xor    BYTE PTR [esi],dh
6a: 37                      aaa
6b: 39 20                   cmp    DWORD PTR [eax],esp
6d: 38 32                   cmp    BYTE PTR [edx],dh
6f: 31 34 38                xor    DWORD PTR [eax+edi*1],esi
72: 30 38                   xor    BYTE PTR [eax],bh
74: 36 35 31 20 33 32       ss xor eax,0x32332031
7a: 38 32                   cmp    BYTE PTR [edx],dh
7c: 33 30                   xor    esi,DWORD PTR [eax]
7e: 36 36 34 37             ss ss xor al,0x37
82: 20 30                   and    BYTE PTR [eax],dh
84: 39 33                   cmp    DWORD PTR [ebx],esi
86: 38 34 34                cmp    BYTE PTR [esp+esi*1],dh
89: 36 30 39                xor    BYTE PTR ss:[ecx],bh
8c: 35 20 35 30 35          xor    eax,0x35303520
91: 38 32                   cmp    BYTE PTR [edx],dh
93: 32 33                   xor    dh,BYTE PTR [ebx]
95: 31 37                   xor    DWORD PTR [edi],esi
97: 32 20                   xor    ah,BYTE PTR [eax]
99: 35 33 35 39 34          xor    eax,0x34393533
9e: 30 38                   xor    BYTE PTR [eax],bh
a0: 31 32                   xor    DWORD PTR [edx],esi
a2: 38 20                   cmp    BYTE PTR [eax],ah
a4: 34 38                   xor    al,0x38
a6: 31 31                   xor    DWORD PTR [ecx],esi
a8: 31 37                   xor    DWORD PTR [edi],esi
aa: 34 35                   xor    al,0x35
ac: 30 32                   xor    BYTE PTR [edx],dh
ae: 20 38                   and    BYTE PTR [eax],bh
b0: 34 31                   xor    al,0x31
b2: 30 32                   xor    BYTE PTR [edx],dh
b4: 37                      aaa
b5: 30 31                   xor    BYTE PTR [ecx],dh
b7: 39 33                   cmp    DWORD PTR [ebx],esi
b9: 20 38                   and    BYTE PTR [eax],bh
bb: 35 32 31 31 30          xor    eax,0x30313132
c0: 35 35 35 39 20          xor    eax,0x20393535
c5: 36 34 34                ss xor al,0x34
c8: 36 32 32                xor    dh,BYTE PTR ss:[edx]
cb: 39 34 38                cmp    DWORD PTR [eax+edi*1],esi
ce: 39 20                   cmp    DWORD PTR [eax],esp
d0: 35 34 39 33 30          xor    eax,0x30333934
d5: 33 38                   xor    edi,DWORD PTR [eax]
d7: 31 39                   xor    DWORD PTR [ecx],edi
d9: 36 20 34 34             and    BYTE PTR ss:[esp+esi*1],dh
dd: 32 38                   xor    bh,BYTE PTR [eax]
df: 38 31                   cmp    BYTE PTR [ecx],dh
e1: 30 39                   xor    BYTE PTR [ecx],bh
e3: 37                      aaa
e4: 35 20 36 36 35          xor    eax,0x35363620
e9: 39 33                   cmp    DWORD PTR [ebx],esi
eb: 33 34 34                xor    esi,DWORD PTR [esp+esi*1]
ee: 36 31 20                xor    DWORD PTR ss:[eax],esp
f1: 32 38                   xor    bh,BYTE PTR [eax]
f3: 34 37                   xor    al,0x37
f5: 35 36 34 38 32          xor    eax,0x32383436
fa: 33 20                   xor    esp,DWORD PTR [eax]
fc: 33 37                   xor    esi,DWORD PTR [edi]
fe: 38 36                   cmp    BYTE PTR [esi],dh
100:    37                      aaa
101:    38 33                   cmp    BYTE PTR [ebx],dh
103:    31 36                   xor    DWORD PTR [esi],esi
105:    35 20 32 37 31          xor    eax,0x31373220
10a:    32 30                   xor    dh,BYTE PTR [eax]
10c:    31 39                   xor    DWORD PTR [ecx],edi
10e:    30 39                   xor    BYTE PTR [ecx],bh
110:    31 20                   xor    DWORD PTR [eax],esp
112:    34 35                   xor    al,0x35
114:    36 34 38                ss xor al,0x38
117:    35 36 36 39 32          xor    eax,0x32393636
11c:    20 33                   and    BYTE PTR [ebx],dh
11e:    34 36                   xor    al,0x36
120:    30 33                   xor    BYTE PTR [ebx],dh
122:    34 38                   xor    al,0x38
124:    36 31 30                xor    DWORD PTR ss:[eax],esi
127:    20 34 35 34 33 32 36    and    BYTE PTR [esi*1+0x36323334],dh
12e:    36 34 38                ss xor al,0x38
131:    32 20                   xor    ah,BYTE PTR [eax]first 1000 digits of PI as decimal DISASSEMBLED
Disassembly
Raw Hex (zero bytes in bold):

1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989   

String Literal:

"\x14\x15\x92\x65\x35\x89\x79\x32\x38\x46\x26\x43\x38\x32\x79\x50\x28\x84\x19\x71\x69\x39\x93\x75\x10\x58\x20\x97\x49\x44\x59\x23\x07\x81\x64\x06\x28\x62\x08\x99\x86\x28\x03\x48\x25\x34\x21\x17\x06\x79\x82\x14\x80\x86\x51\x32\x82\x30\x66\x47\x09\x38\x44\x60\x95\x50\x58\x22\x31\x72\x53\x59\x40\x81\x28\x48\x11\x17\x45\x02\x84\x10\x27\x01\x93\x85\x21\x10\x55\x59\x64\x46\x22\x94\x89\x54\x93\x03\x81\x96\x44\x28\x81\x09\x75\x66\x59\x33\x44\x61\x28\x47\x56\x48\x23\x37\x86\x78\x31\x65\x27\x12\x01\x90\x91\x45\x64\x85\x66\x92\x34\x60\x34\x86\x10\x45\x43\x26\x64\x82\x13\x39\x36\x07\x26\x02\x49\x14\x12\x73\x72\x45\x87\x00\x66\x06\x31\x55\x88\x17\x48\x81\x52\x09\x20\x96\x28\x29\x25\x40\x91\x71\x53\x64\x36\x78\x92\x59\x03\x60\x01\x13\x30\x53\x05\x48\x82\x04\x66\x52\x13\x84\x14\x69\x51\x94\x15\x11\x60\x94\x33\x05\x72\x70\x36\x57\x59\x59\x19\x53\x09\x21\x86\x11\x73\x81\x93\x26\x11\x79\x31\x05\x11\x85\x48\x07\x44\x62\x37\x99\x62\x74\x95\x67\x35\x18\x85\x75\x27\x24\x89\x12\x27\x93\x81\x83\x01\x19\x49\x12\x98\x33\x67\x33\x62\x44\x06\x56\x64\x30\x86\x02\x13\x94\x94\x63\x95\x22\x47\x37\x19\x07\x02\x17\x98\x60\x94\x37\x02\x77\x05\x39\x21\x71\x76\x29\x31\x76\x75\x23\x84\x67\x48\x18\x46\x76\x69\x40\x51\x32\x00\x05\x68\x12\x71\x45\x26\x35\x60\x82\x77\x85\x77\x13\x42\x75\x77\x89\x60\x91\x73\x63\x71\x78\x72\x14\x68\x44\x09\x01\x22\x49\x53\x43\x01\x46\x54\x95\x85\x37\x10\x50\x79\x22\x79\x68\x92\x58\x92\x35\x42\x01\x99\x56\x11\x21\x29\x02\x19\x60\x86\x40\x34\x41\x81\x59\x81\x36\x29\x77\x47\x71\x30\x99\x60\x51\x87\x07\x21\x13\x49\x99\x99\x98\x37\x29\x78\x04\x99\x51\x05\x97\x31\x73\x28\x16\x09\x63\x18\x59\x50\x24\x45\x94\x55\x34\x69\x08\x30\x26\x42\x52\x23\x08\x25\x33\x44\x68\x50\x35\x26\x19\x31\x18\x81\x71\x01\x00\x03\x13\x78\x38\x75\x28\x86\x58\x75\x33\x20\x83\x81\x42\x06\x17\x17\x76\x69\x14\x73\x03\x59\x82\x53\x49\x04\x28\x75\x54\x68\x73\x11\x59\x56\x28\x63\x88\x23\x53\x78\x75\x93\x75\x19\x57\x78\x18\x57\x78\x05\x32\x17\x12\x26\x80\x66\x13\x00\x19\x27\x87\x66\x11\x19\x59\x09\x21\x64\x20\x19\x89"

Array Literal:

{ 0x14, 0x15, 0x92, 0x65, 0x35, 0x89, 0x79, 0x32, 0x38, 0x46, 0x26, 0x43, 0x38, 0x32, 0x79, 0x50, 0x28, 0x84, 0x19, 0x71, 0x69, 0x39, 0x93, 0x75, 0x10, 0x58, 0x20, 0x97, 0x49, 0x44, 0x59, 0x23, 0x07, 0x81, 0x64, 0x06, 0x28, 0x62, 0x08, 0x99, 0x86, 0x28, 0x03, 0x48, 0x25, 0x34, 0x21, 0x17, 0x06, 0x79, 0x82, 0x14, 0x80, 0x86, 0x51, 0x32, 0x82, 0x30, 0x66, 0x47, 0x09, 0x38, 0x44, 0x60, 0x95, 0x50, 0x58, 0x22, 0x31, 0x72, 0x53, 0x59, 0x40, 0x81, 0x28, 0x48, 0x11, 0x17, 0x45, 0x02, 0x84, 0x10, 0x27, 0x01, 0x93, 0x85, 0x21, 0x10, 0x55, 0x59, 0x64, 0x46, 0x22, 0x94, 0x89, 0x54, 0x93, 0x03, 0x81, 0x96, 0x44, 0x28, 0x81, 0x09, 0x75, 0x66, 0x59, 0x33, 0x44, 0x61, 0x28, 0x47, 0x56, 0x48, 0x23, 0x37, 0x86, 0x78, 0x31, 0x65, 0x27, 0x12, 0x01, 0x90, 0x91, 0x45, 0x64, 0x85, 0x66, 0x92, 0x34, 0x60, 0x34, 0x86, 0x10, 0x45, 0x43, 0x26, 0x64, 0x82, 0x13, 0x39, 0x36, 0x07, 0x26, 0x02, 0x49, 0x14, 0x12, 0x73, 0x72, 0x45, 0x87, 0x00, 0x66, 0x06, 0x31, 0x55, 0x88, 0x17, 0x48, 0x81, 0x52, 0x09, 0x20, 0x96, 0x28, 0x29, 0x25, 0x40, 0x91, 0x71, 0x53, 0x64, 0x36, 0x78, 0x92, 0x59, 0x03, 0x60, 0x01, 0x13, 0x30, 0x53, 0x05, 0x48, 0x82, 0x04, 0x66, 0x52, 0x13, 0x84, 0x14, 0x69, 0x51, 0x94, 0x15, 0x11, 0x60, 0x94, 0x33, 0x05, 0x72, 0x70, 0x36, 0x57, 0x59, 0x59, 0x19, 0x53, 0x09, 0x21, 0x86, 0x11, 0x73, 0x81, 0x93, 0x26, 0x11, 0x79, 0x31, 0x05, 0x11, 0x85, 0x48, 0x07, 0x44, 0x62, 0x37, 0x99, 0x62, 0x74, 0x95, 0x67, 0x35, 0x18, 0x85, 0x75, 0x27, 0x24, 0x89, 0x12, 0x27, 0x93, 0x81, 0x83, 0x01, 0x19, 0x49, 0x12, 0x98, 0x33, 0x67, 0x33, 0x62, 0x44, 0x06, 0x56, 0x64, 0x30, 0x86, 0x02, 0x13, 0x94, 0x94, 0x63, 0x95, 0x22, 0x47, 0x37, 0x19, 0x07, 0x02, 0x17, 0x98, 0x60, 0x94, 0x37, 0x02, 0x77, 0x05, 0x39, 0x21, 0x71, 0x76, 0x29, 0x31, 0x76, 0x75, 0x23, 0x84, 0x67, 0x48, 0x18, 0x46, 0x76, 0x69, 0x40, 0x51, 0x32, 0x00, 0x05, 0x68, 0x12, 0x71, 0x45, 0x26, 0x35, 0x60, 0x82, 0x77, 0x85, 0x77, 0x13, 0x42, 0x75, 0x77, 0x89, 0x60, 0x91, 0x73, 0x63, 0x71, 0x78, 0x72, 0x14, 0x68, 0x44, 0x09, 0x01, 0x22, 0x49, 0x53, 0x43, 0x01, 0x46, 0x54, 0x95, 0x85, 0x37, 0x10, 0x50, 0x79, 0x22, 0x79, 0x68, 0x92, 0x58, 0x92, 0x35, 0x42, 0x01, 0x99, 0x56, 0x11, 0x21, 0x29, 0x02, 0x19, 0x60, 0x86, 0x40, 0x34, 0x41, 0x81, 0x59, 0x81, 0x36, 0x29, 0x77, 0x47, 0x71, 0x30, 0x99, 0x60, 0x51, 0x87, 0x07, 0x21, 0x13, 0x49, 0x99, 0x99, 0x98, 0x37, 0x29, 0x78, 0x04, 0x99, 0x51, 0x05, 0x97, 0x31, 0x73, 0x28, 0x16, 0x09, 0x63, 0x18, 0x59, 0x50, 0x24, 0x45, 0x94, 0x55, 0x34, 0x69, 0x08, 0x30, 0x26, 0x42, 0x52, 0x23, 0x08, 0x25, 0x33, 0x44, 0x68, 0x50, 0x35, 0x26, 0x19, 0x31, 0x18, 0x81, 0x71, 0x01, 0x00, 0x03, 0x13, 0x78, 0x38, 0x75, 0x28, 0x86, 0x58, 0x75, 0x33, 0x20, 0x83, 0x81, 0x42, 0x06, 0x17, 0x17, 0x76, 0x69, 0x14, 0x73, 0x03, 0x59, 0x82, 0x53, 0x49, 0x04, 0x28, 0x75, 0x54, 0x68, 0x73, 0x11, 0x59, 0x56, 0x28, 0x63, 0x88, 0x23, 0x53, 0x78, 0x75, 0x93, 0x75, 0x19, 0x57, 0x78, 0x18, 0x57, 0x78, 0x05, 0x32, 0x17, 0x12, 0x26, 0x80, 0x66, 0x13, 0x00, 0x19, 0x27, 0x87, 0x66, 0x11, 0x19, 0x59, 0x09, 0x21, 0x64, 0x20, 0x19, 0x89 }

Disassembly:
0:  14 15                   adc    al,0x15
2:  92                      xchg   edx,eax
3:  65 35 89 79 32 38       gs xor eax,0x38327989
9:  46                      inc    esi
a:  26 43                   es inc ebx
c:  38 32                   cmp    BYTE PTR [edx],dh
e:  79 50                   jns    0x60
10: 28 84 19 71 69 39 93    sub    BYTE PTR [ecx+ebx*1-0x6cc6968f],al
17: 75 10                   jne    0x29
19: 58                      pop    eax
1a: 20 97 49 44 59 23       and    BYTE PTR [edi+0x23594449],dl
20: 07                      pop    es
21: 81 64 06 28 62 08 99    and    DWORD PTR [esi+eax*1+0x28],0x86990862
28: 86
29: 28 03                   sub    BYTE PTR [ebx],al
2b: 48                      dec    eax
2c: 25 34 21 17 06          and    eax,0x6172134
31: 79 82                   jns    0xffffffb5
33: 14 80                   adc    al,0x80
35: 86 51 32                xchg   BYTE PTR [ecx+0x32],dl
38: 82 30 66                xor    BYTE PTR [eax],0x66
3b: 47                      inc    edi
3c: 09 38                   or     DWORD PTR [eax],edi
3e: 44                      inc    esp
3f: 60                      pusha
40: 95                      xchg   ebp,eax
41: 50                      push   eax
42: 58                      pop    eax
43: 22 31                   and    dh,BYTE PTR [ecx]
45: 72 53                   jb     0x9a
47: 59                      pop    ecx
48: 40                      inc    eax
49: 81 28 48 11 17 45       sub    DWORD PTR [eax],0x45171148
4f: 02 84 10 27 01 93 85    add    al,BYTE PTR [eax+edx*1-0x7a6cfed9]
56: 21 10                   and    DWORD PTR [eax],edx
58: 55                      push   ebp
59: 59                      pop    ecx
5a: 64 46                   fs inc esi
5c: 22 94 89 54 93 03 81    and    dl,BYTE PTR [ecx+ecx*4-0x7efc6cac]
63: 96                      xchg   esi,eax
64: 44                      inc    esp
65: 28 81 09 75 66 59       sub    BYTE PTR [ecx+0x59667509],al
6b: 33 44 61 28             xor    eax,DWORD PTR [ecx+eiz*2+0x28]
6f: 47                      inc    edi
70: 56                      push   esi
71: 48                      dec    eax
72: 23 37                   and    esi,DWORD PTR [edi]
74: 86 78 31                xchg   BYTE PTR [eax+0x31],bh
77: 65 27                   gs daa
79: 12 01                   adc    al,BYTE PTR [ecx]
7b: 90                      nop
7c: 91                      xchg   ecx,eax
7d: 45                      inc    ebp
7e: 64 85 66 92             test   DWORD PTR fs:[esi-0x6e],esp
82: 34 60                   xor    al,0x60
84: 34 86                   xor    al,0x86
86: 10 45 43                adc    BYTE PTR [ebp+0x43],al
89: 26 64 82 13 39          es adc BYTE PTR fs:[ebx],0x39
8e: 36 07                   ss pop es
90: 26 02 49 14             add    cl,BYTE PTR es:[ecx+0x14]
94: 12 73 72                adc    dh,BYTE PTR [ebx+0x72]
97: 45                      inc    ebp
98: 87 00                   xchg   DWORD PTR [eax],eax
9a: 66 06                   pushw  es
9c: 31 55 88                xor    DWORD PTR [ebp-0x78],edx
9f: 17                      pop    ss
a0: 48                      dec    eax
a1: 81 52 09 20 96 28 29    adc    DWORD PTR [edx+0x9],0x29289620
a8: 25 40 91 71 53          and    eax,0x53719140
ad: 64 36 78 92             fs ss js 0x43
b1: 59                      pop    ecx
b2: 03 60 01                add    esp,DWORD PTR [eax+0x1]
b5: 13 30                   adc    esi,DWORD PTR [eax]
b7: 53                      push   ebx
b8: 05 48 82 04 66          add    eax,0x66048248
bd: 52                      push   edx
be: 13 84 14 69 51 94 15    adc    eax,DWORD PTR [esp+edx*1+0x15945169]
c5: 11 60 94                adc    DWORD PTR [eax-0x6c],esp
c8: 33 05 72 70 36 57       xor    eax,DWORD PTR ds:0x57367072
ce: 59                      pop    ecx
cf: 59                      pop    ecx
d0: 19 53 09                sbb    DWORD PTR [ebx+0x9],edx
d3: 21 86 11 73 81 93       and    DWORD PTR [esi-0x6c7e8cef],eax
d9: 26 11 79 31             adc    DWORD PTR es:[ecx+0x31],edi
dd: 05 11 85 48 07          add    eax,0x7488511
e2: 44                      inc    esp
e3: 62 37                   bound  esi,QWORD PTR [edi]
e5: 99                      cdq
e6: 62 74 95 67             bound  esi,QWORD PTR [ebp+edx*4+0x67]
ea: 35 18 85 75 27          xor    eax,0x27758518
ef: 24 89                   and    al,0x89
f1: 12 27                   adc    ah,BYTE PTR [edi]
f3: 93                      xchg   ebx,eax
f4: 81 83 01 19 49 12 98    add    DWORD PTR [ebx+0x12491901],0x33673398
fb: 33 67 33
fe: 62 44 06 56             bound  eax,QWORD PTR [esi+eax*1+0x56]
102:    64 30 86 02 13 94 94    xor    BYTE PTR fs:[esi-0x6b6becfe],al
109:    63 95 22 47 37 19       arpl   WORD PTR [ebp+0x19374722],dx
10f:    07                      pop    es
110:    02 17                   add    dl,BYTE PTR [edi]
112:    98                      cwde
113:    60                      pusha
114:    94                      xchg   esp,eax
115:    37                      aaa
116:    02 77 05                add    dh,BYTE PTR [edi+0x5]
119:    39 21                   cmp    DWORD PTR [ecx],esp
11b:    71 76                   jno    0x193
11d:    29 31                   sub    DWORD PTR [ecx],esi
11f:    76 75                   jbe    0x196
121:    23 84 67 48 18 46 76    and    eax,DWORD PTR [edi+eiz*2+0x76461848]
128:    69 40 51 32 00 05 68    imul   eax,DWORD PTR [eax+0x51],0x68050032
12f:    12 71 45                adc    dh,BYTE PTR [ecx+0x45]
132:    26 35 60 82 77 85       es xor eax,0x85778260
138:    77 13                   ja     0x14d
13a:    42                      inc    edx
13b:    75 77                   jne    0x1b4
13d:    89 60 91                mov    DWORD PTR [eax-0x6f],esp
140:    73 63                   jae    0x1a5
142:    71 78                   jno    0x1bc
144:    72 14                   jb     0x15a
146:    68 44 09 01 22          push   0x22010944
14b:    49                      dec    ecx
14c:    53                      push   ebx
14d:    43                      inc    ebx
14e:    01 46 54                add    DWORD PTR [esi+0x54],eax
151:    95                      xchg   ebp,eax
152:    85 37                   test   DWORD PTR [edi],esi
154:    10 50 79                adc    BYTE PTR [eax+0x79],dl
157:    22 79 68                and    bh,BYTE PTR [ecx+0x68]
15a:    92                      xchg   edx,eax
15b:    58                      pop    eax
15c:    92                      xchg   edx,eax
15d:    35 42 01 99 56          xor    eax,0x56990142
162:    11 21                   adc    DWORD PTR [ecx],esp
164:    29 02                   sub    DWORD PTR [edx],eax
166:    19 60 86                sbb    DWORD PTR [eax-0x7a],esp
169:    40                      inc    eax
16a:    34 41                   xor    al,0x41
16c:    81 59 81 36 29 77 47    sbb    DWORD PTR [ecx-0x7f],0x47772936
173:    71 30                   jno    0x1a5
175:    99                      cdq
176:    60                      pusha
177:    51                      push   ecx
178:    87 07                   xchg   DWORD PTR [edi],eax
17a:    21 13                   and    DWORD PTR [ebx],edx
17c:    49                      dec    ecx
17d:    99                      cdq
17e:    99                      cdq
17f:    98                      cwde
180:    37                      aaa
181:    29 78 04                sub    DWORD PTR [eax+0x4],edi
184:    99                      cdq
185:    51                      push   ecx
186:    05 97 31 73 28          add    eax,0x28733197
18b:    16                      push   ss
18c:    09 63 18                or     DWORD PTR [ebx+0x18],esp
18f:    59                      pop    ecx
190:    50                      push   eax
191:    24 45                   and    al,0x45
193:    94                      xchg   esp,eax
194:    55                      push   ebp
195:    34 69                   xor    al,0x69
197:    08 30                   or     BYTE PTR [eax],dh
199:    26 42                   es inc edx
19b:    52                      push   edx
19c:    23 08                   and    ecx,DWORD PTR [eax]
19e:    25 33 44 68 50          and    eax,0x50684433
1a3:    35 26 19 31 18          xor    eax,0x18311926
1a8:    81 71 01 00 03 13 78    xor    DWORD PTR [ecx+0x1],0x78130300
1af:    38 75 28                cmp    BYTE PTR [ebp+0x28],dh
1b2:    86 58 75                xchg   BYTE PTR [eax+0x75],bl
1b5:    33 20                   xor    esp,DWORD PTR [eax]
1b7:    83 81 42 06 17 17 76    add    DWORD PTR [ecx+0x17170642],0x76
1be:    69 14 73 03 59 82 53    imul   edx,DWORD PTR [ebx+esi*2],0x53825903
1c5:    49                      dec    ecx
1c6:    04 28                   add    al,0x28
1c8:    75 54                   jne    0x21e
1ca:    68 73 11 59 56          push   0x56591173
1cf:    28 63 88                sub    BYTE PTR [ebx-0x78],ah
1d2:    23 53 78                and    edx,DWORD PTR [ebx+0x78]
1d5:    75 93                   jne    0x16a
1d7:    75 19                   jne    0x1f2
1d9:    57                      push   edi
1da:    78 18                   js     0x1f4
1dc:    57                      push   edi
1dd:    78 05                   js     0x1e4
1df:    32 17                   xor    dl,BYTE PTR [edi]
1e1:    12 26                   adc    ah,BYTE PTR [esi]
1e3:    80 66 13 00             and    BYTE PTR [esi+0x13],0x0
1e7:    19 27                   sbb    DWORD PTR [edi],esp
1e9:    87 66 11                xchg   DWORD PTR [esi+0x11],esp
1ec:    19 59 09                sbb    DWORD PTR [ecx+0x9],ebx
1ef:    21 64 20 19             and    DWORD PTR [eax+eiz*1+0x19],esp
1f3:    89                      .byte 0x89PI DECIMAL TO HEX DISSASSEMBLED
Disassembly
Raw Hex (zero bytes in bold):

89F10901F6D7672E2F88E3C0A4194A83D2A33A515FF4089BAECB161BC98D5C5B2AE3A1FC57D4AD4F8AE710CC4F3CE8FDF7C32389097DA13E16E70E4DC111DD16607DA56A389D0128B19F739FDE7BB1A1E63B862CD07D1D275EB05C33DC0B06F4CEFB8CAF5D7F229307CDDE577A9961531E9BD017239FC023769162A9E43EB25B0959E82636E78283741850A80FCCA0FBD0797AD2E0B76BEAA155444F1591159D798FB741D3C8286BC206379F8F3F443AC2CAAEA4221AF6BCFC24F1785E4857CBD664B6A110C3B3F86543055E687A99F9199AA72A6B15B279269BB60CE3A596C8AC725C6564D093ABEF659693DAA191C63C4942944FB2BC52C7B27ACCBDB3AE6014DF20750F5B219C94AB458F699CD7CD626972C31A99C6B414DF38906FF99AE3368A94BA512689D970F12919401F9F657D41182AC540583E74F0CB0B213E0420D6928BF8F83D2B8B6C0E28FFBED93EB59985B863A50432224AEBE66EB47C2842C87A7E66DE21F964A969D6C3EA312A4B52894F1F159F60F893E72A7D349A62600E7C53BEA815C49AAED75DE2B08D0F5FCA8E05   

String Literal:

"\x89\xF1\x09\x01\xF6\xD7\x67\x2E\x2F\x88\xE3\xC0\xA4\x19\x4A\x83\xD2\xA3\x3A\x51\x5F\xF4\x08\x9B\xAE\xCB\x16\x1B\xC9\x8D\x5C\x5B\x2A\xE3\xA1\xFC\x57\xD4\xAD\x4F\x8A\xE7\x10\xCC\x4F\x3C\xE8\xFD\xF7\xC3\x23\x89\x09\x7D\xA1\x3E\x16\xE7\x0E\x4D\xC1\x11\xDD\x16\x60\x7D\xA5\x6A\x38\x9D\x01\x28\xB1\x9F\x73\x9F\xDE\x7B\xB1\xA1\xE6\x3B\x86\x2C\xD0\x7D\x1D\x27\x5E\xB0\x5C\x33\xDC\x0B\x06\xF4\xCE\xFB\x8C\xAF\x5D\x7F\x22\x93\x07\xCD\xDE\x57\x7A\x99\x61\x53\x1E\x9B\xD0\x17\x23\x9F\xC0\x23\x76\x91\x62\xA9\xE4\x3E\xB2\x5B\x09\x59\xE8\x26\x36\xE7\x82\x83\x74\x18\x50\xA8\x0F\xCC\xA0\xFB\xD0\x79\x7A\xD2\xE0\xB7\x6B\xEA\xA1\x55\x44\x4F\x15\x91\x15\x9D\x79\x8F\xB7\x41\xD3\xC8\x28\x6B\xC2\x06\x37\x9F\x8F\x3F\x44\x3A\xC2\xCA\xAE\xA4\x22\x1A\xF6\xBC\xFC\x24\xF1\x78\x5E\x48\x57\xCB\xD6\x64\xB6\xA1\x10\xC3\xB3\xF8\x65\x43\x05\x5E\x68\x7A\x99\xF9\x19\x9A\xA7\x2A\x6B\x15\xB2\x79\x26\x9B\xB6\x0C\xE3\xA5\x96\xC8\xAC\x72\x5C\x65\x64\xD0\x93\xAB\xEF\x65\x96\x93\xDA\xA1\x91\xC6\x3C\x49\x42\x94\x4F\xB2\xBC\x52\xC7\xB2\x7A\xCC\xBD\xB3\xAE\x60\x14\xDF\x20\x75\x0F\x5B\x21\x9C\x94\xAB\x45\x8F\x69\x9C\xD7\xCD\x62\x69\x72\xC3\x1A\x99\xC6\xB4\x14\xDF\x38\x90\x6F\xF9\x9A\xE3\x36\x8A\x94\xBA\x51\x26\x89\xD9\x70\xF1\x29\x19\x40\x1F\x9F\x65\x7D\x41\x18\x2A\xC5\x40\x58\x3E\x74\xF0\xCB\x0B\x21\x3E\x04\x20\xD6\x92\x8B\xF8\xF8\x3D\x2B\x8B\x6C\x0E\x28\xFF\xBE\xD9\x3E\xB5\x99\x85\xB8\x63\xA5\x04\x32\x22\x4A\xEB\xE6\x6E\xB4\x7C\x28\x42\xC8\x7A\x7E\x66\xDE\x21\xF9\x64\xA9\x69\xD6\xC3\xEA\x31\x2A\x4B\x52\x89\x4F\x1F\x15\x9F\x60\xF8\x93\xE7\x2A\x7D\x34\x9A\x62\x60\x0E\x7C\x53\xBE\xA8\x15\xC4\x9A\xAE\xD7\x5D\xE2\xB0\x8D\x0F\x5F\xCA\x8E\x05"

Array Literal:

{ 0x89, 0xF1, 0x09, 0x01, 0xF6, 0xD7, 0x67, 0x2E, 0x2F, 0x88, 0xE3, 0xC0, 0xA4, 0x19, 0x4A, 0x83, 0xD2, 0xA3, 0x3A, 0x51, 0x5F, 0xF4, 0x08, 0x9B, 0xAE, 0xCB, 0x16, 0x1B, 0xC9, 0x8D, 0x5C, 0x5B, 0x2A, 0xE3, 0xA1, 0xFC, 0x57, 0xD4, 0xAD, 0x4F, 0x8A, 0xE7, 0x10, 0xCC, 0x4F, 0x3C, 0xE8, 0xFD, 0xF7, 0xC3, 0x23, 0x89, 0x09, 0x7D, 0xA1, 0x3E, 0x16, 0xE7, 0x0E, 0x4D, 0xC1, 0x11, 0xDD, 0x16, 0x60, 0x7D, 0xA5, 0x6A, 0x38, 0x9D, 0x01, 0x28, 0xB1, 0x9F, 0x73, 0x9F, 0xDE, 0x7B, 0xB1, 0xA1, 0xE6, 0x3B, 0x86, 0x2C, 0xD0, 0x7D, 0x1D, 0x27, 0x5E, 0xB0, 0x5C, 0x33, 0xDC, 0x0B, 0x06, 0xF4, 0xCE, 0xFB, 0x8C, 0xAF, 0x5D, 0x7F, 0x22, 0x93, 0x07, 0xCD, 0xDE, 0x57, 0x7A, 0x99, 0x61, 0x53, 0x1E, 0x9B, 0xD0, 0x17, 0x23, 0x9F, 0xC0, 0x23, 0x76, 0x91, 0x62, 0xA9, 0xE4, 0x3E, 0xB2, 0x5B, 0x09, 0x59, 0xE8, 0x26, 0x36, 0xE7, 0x82, 0x83, 0x74, 0x18, 0x50, 0xA8, 0x0F, 0xCC, 0xA0, 0xFB, 0xD0, 0x79, 0x7A, 0xD2, 0xE0, 0xB7, 0x6B, 0xEA, 0xA1, 0x55, 0x44, 0x4F, 0x15, 0x91, 0x15, 0x9D, 0x79, 0x8F, 0xB7, 0x41, 0xD3, 0xC8, 0x28, 0x6B, 0xC2, 0x06, 0x37, 0x9F, 0x8F, 0x3F, 0x44, 0x3A, 0xC2, 0xCA, 0xAE, 0xA4, 0x22, 0x1A, 0xF6, 0xBC, 0xFC, 0x24, 0xF1, 0x78, 0x5E, 0x48, 0x57, 0xCB, 0xD6, 0x64, 0xB6, 0xA1, 0x10, 0xC3, 0xB3, 0xF8, 0x65, 0x43, 0x05, 0x5E, 0x68, 0x7A, 0x99, 0xF9, 0x19, 0x9A, 0xA7, 0x2A, 0x6B, 0x15, 0xB2, 0x79, 0x26, 0x9B, 0xB6, 0x0C, 0xE3, 0xA5, 0x96, 0xC8, 0xAC, 0x72, 0x5C, 0x65, 0x64, 0xD0, 0x93, 0xAB, 0xEF, 0x65, 0x96, 0x93, 0xDA, 0xA1, 0x91, 0xC6, 0x3C, 0x49, 0x42, 0x94, 0x4F, 0xB2, 0xBC, 0x52, 0xC7, 0xB2, 0x7A, 0xCC, 0xBD, 0xB3, 0xAE, 0x60, 0x14, 0xDF, 0x20, 0x75, 0x0F, 0x5B, 0x21, 0x9C, 0x94, 0xAB, 0x45, 0x8F, 0x69, 0x9C, 0xD7, 0xCD, 0x62, 0x69, 0x72, 0xC3, 0x1A, 0x99, 0xC6, 0xB4, 0x14, 0xDF, 0x38, 0x90, 0x6F, 0xF9, 0x9A, 0xE3, 0x36, 0x8A, 0x94, 0xBA, 0x51, 0x26, 0x89, 0xD9, 0x70, 0xF1, 0x29, 0x19, 0x40, 0x1F, 0x9F, 0x65, 0x7D, 0x41, 0x18, 0x2A, 0xC5, 0x40, 0x58, 0x3E, 0x74, 0xF0, 0xCB, 0x0B, 0x21, 0x3E, 0x04, 0x20, 0xD6, 0x92, 0x8B, 0xF8, 0xF8, 0x3D, 0x2B, 0x8B, 0x6C, 0x0E, 0x28, 0xFF, 0xBE, 0xD9, 0x3E, 0xB5, 0x99, 0x85, 0xB8, 0x63, 0xA5, 0x04, 0x32, 0x22, 0x4A, 0xEB, 0xE6, 0x6E, 0xB4, 0x7C, 0x28, 0x42, 0xC8, 0x7A, 0x7E, 0x66, 0xDE, 0x21, 0xF9, 0x64, 0xA9, 0x69, 0xD6, 0xC3, 0xEA, 0x31, 0x2A, 0x4B, 0x52, 0x89, 0x4F, 0x1F, 0x15, 0x9F, 0x60, 0xF8, 0x93, 0xE7, 0x2A, 0x7D, 0x34, 0x9A, 0x62, 0x60, 0x0E, 0x7C, 0x53, 0xBE, 0xA8, 0x15, 0xC4, 0x9A, 0xAE, 0xD7, 0x5D, 0xE2, 0xB0, 0x8D, 0x0F, 0x5F, 0xCA, 0x8E, 0x05 }

Disassembly:
0:  89 f1                   mov    ecx,esi
2:  09 01                   or     DWORD PTR [ecx],eax
4:  f6 d7                   not    bh
6:  67 2e 2f                addr16 cs das
9:  88 e3                   mov    bl,ah
b:  c0 a4 19 4a 83 d2 a3    shl    BYTE PTR [ecx+ebx*1-0x5c2d7cb6],0x3a
12: 3a
13: 51                      push   ecx
14: 5f                      pop    edi
15: f4                      hlt
16: 08 9b ae cb 16 1b       or     BYTE PTR [ebx+0x1b16cbae],bl
1c: c9                      leave
1d: 8d 5c 5b 2a             lea    ebx,[ebx+ebx*2+0x2a]
21: e3 a1                   jecxz  0xffffffc4
23: fc                      cld
24: 57                      push   edi
25: d4 ad                   aam    0xad
27: 4f                      dec    edi
28: 8a e7                   mov    ah,bh
2a: 10 cc                   adc    ah,cl
2c: 4f                      dec    edi
2d: 3c e8                   cmp    al,0xe8
2f: fd                      std
30: f7 c3 23 89 09 7d       test   ebx,0x7d098923
36: a1 3e 16 e7 0e          mov    eax,ds:0xee7163e
3b: 4d                      dec    ebp
3c: c1 11 dd                rcl    DWORD PTR [ecx],0xdd
3f: 16                      push   ss
40: 60                      pusha
41: 7d a5                   jge    0xffffffe8
43: 6a 38                   push   0x38
45: 9d                      popf
46: 01 28                   add    DWORD PTR [eax],ebp
48: b1 9f                   mov    cl,0x9f
4a: 73 9f                   jae    0xffffffeb
4c: de 7b b1                fidivr WORD PTR [ebx-0x4f]
4f: a1 e6 3b 86 2c          mov    eax,ds:0x2c863be6
54: d0 7d 1d                sar    BYTE PTR [ebp+0x1d],1
57: 27                      daa
58: 5e                      pop    esi
59: b0 5c                   mov    al,0x5c
5b: 33 dc                   xor    ebx,esp
5d: 0b 06                   or     eax,DWORD PTR [esi]
5f: f4                      hlt
60: ce                      into
61: fb                      sti
62: 8c af 5d 7f 22 93       mov    WORD PTR [edi-0x6cdd80a3],gs
68: ea 07 a8 7d 01 6f 06    jmp    0x66f:0x17da807
6f: cd de                   int    0xde
71: 57                      push   edi
72: 7a 99                   jp     0xd
74: 61                      popa
75: 53                      push   ebx
76: 1e                      push   ds
77: 9b                      fwait
78: d0 17                   rcl    BYTE PTR [edi],1
7a: 23 9f c0 23 76 91       and    ebx,DWORD PTR [edi-0x6e89dc40]
80: 62 a9 e4 3e b2 5b       bound  ebp,QWORD PTR [ecx+0x5bb23ee4]
86: 09 59 e8                or     DWORD PTR [ecx-0x18],ebx
89: 26 36 e7 82             es ss out 0x82,eax
8d: 83 74 18 50 a8          xor    DWORD PTR [eax+ebx*1+0x50],0xffffffa8
92: 0f cc                   bswap  esp
94: a0 fb d0 79 7a          mov    al,ds:0x7a79d0fb
99: d2 e0                   shl    al,cl
9b: b7 6b                   mov    bh,0x6b
9d: ea a1 55 44 4f 15 91    jmp    0x9115:0x4f4455a1
a4: 15 9d 79 8f b7          adc    eax,0xb78f799d
a9: 41                      inc    ecx
aa: d3 c8                   ror    eax,cl
ac: 28 6b c2                sub    BYTE PTR [ebx-0x3e],ch
af: 06                      push   es
b0: 37                      aaa
b1: 9f                      lahf
b2: 8f                      (bad)
b3: 3f                      aas
b4: 44                      inc    esp
b5: 3a c2                   cmp    al,dl
b7: ca ae a4                retf   0xa4ae
ba: 22 1a                   and    bl,BYTE PTR [edx]
bc: f6 bc fc 24 f1 78 5e    idiv   BYTE PTR [esp+edi*8+0x5e78f124]
c3: 48                      dec    eax
c4: 57                      push   edi
c5: cb                      retf
c6: d6                      (bad)
c7: 64 b6 a1                fs mov dh,0xa1
ca: ea 10 34 db b0 0e 93    jmp    0x930e:0xb0db3410
d1: c3                      ret
d2: b3 f8                   mov    bl,0xf8
d4: 65 43                   gs inc ebx
d6: 05 5e 68 7a 99          add    eax,0x997a685e
db: f9                      stc
dc: 19 9a a7 2a 6b 15       sbb    DWORD PTR [edx+0x156b2aa7],ebx
e2: b2 79                   mov    dl,0x79
e4: 26 9b                   es fwait
e6: b6 0c                   mov    dh,0xc
e8: e3 a5                   jecxz  0x8f
ea: 96                      xchg   esi,eax
eb: c8 ac 72 5c             enter  0x72ac,0x5c
ef: 65 64 d0 93 ab ef 65    gs rcl BYTE PTR fs:[ebx-0x699a1055],1
f6: 96
f7: 93                      xchg   ebx,eax
f8: da a1 91 c6 3c 49       fisub  DWORD PTR [ecx+0x493cc691]
fe: 42                      inc    edx
ff: 94                      xchg   esp,eax
100:    4f                      dec    edi
101:    b2 bc                   mov    dl,0xbc
103:    52                      push   edx
104:    c7                      (bad)
105:    b2 7a                   mov    dl,0x7a
107:    cc                      int3
108:    bd b3 ae 60 14          mov    ebp,0x1460aeb3
10d:    df 20                   fbld   TBYTE PTR [eax]
10f:    75 0f                   jne    0x120
111:    5b                      pop    ebx
112:    21 9c 94 ab 45 8f 69    and    DWORD PTR [esp+edx*4+0x698f45ab],ebx
119:    9c                      pushf
11a:    d7                      xlat   BYTE PTR ds:[ebx]
11b:    cd 62                   int    0x62
11d:    69 72 c3 1a 99 c6 b4    imul   esi,DWORD PTR [edx-0x3d],0xb4c6991a
124:    14 df                   adc    al,0xdf
126:    38 90 6f f9 9a e3       cmp    BYTE PTR [eax-0x1c650691],dl
12c:    36 8a 94 ba 51 26 89    mov    dl,BYTE PTR ss:[edx+edi*4-0x2676d9af]
133:    d9
134:    70 f1                   jo     0x127
136:    29 19                   sub    DWORD PTR [ecx],ebx
138:    40                      inc    eax
139:    1f                      pop    ds
13a:    9f                      lahf
13b:    65 7d 41                gs jge 0x17f
13e:    18 2a                   sbb    BYTE PTR [edx],ch
140:    c5 40 58                lds    eax,FWORD PTR [eax+0x58]
143:    3e 74 f0                ds je  0x136
146:    cb                      retf
147:    0b 21                   or     esp,DWORD PTR [ecx]
149:    3e 04 20                ds add al,0x20
14c:    d6                      (bad)
14d:    92                      xchg   edx,eax
14e:    8b f8                   mov    edi,eax
150:    f8                      clc
151:    3d 2b 8b 6c 0e          cmp    eax,0xe6c8b2b
156:    28 ff                   sub    bh,bh
158:    be d9 3e b5 99          mov    esi,0x99b53ed9
15d:    85 b8 63 a5 04 32       test   DWORD PTR [eax+0x3204a563],edi
163:    22 4a eb                and    cl,BYTE PTR [edx-0x15]
166:    e6 6e                   out    0x6e,al
168:    b4 7c                   mov    ah,0x7c
16a:    28 42 c8                sub    BYTE PTR [edx-0x38],al
16d:    7a 7e                   jp     0x1ed
16f:    66 de 21                data16 fisub WORD PTR [ecx]
172:    f9                      stc
173:    64 a9 69 d6 c3 ea       fs test eax,0xeac3d669
179:    31 2a                   xor    DWORD PTR [edx],ebp
17b:    4b                      dec    ebx
17c:    52                      push   edx
17d:    89 4f 1f                mov    DWORD PTR [edi+0x1f],ecx
180:    15 9f 60 f8 93          adc    eax,0x93f8609f
185:    e7 2a                   out    0x2a,eax
187:    7d 34                   jge    0x1bd
189:    9a 62 60 0e 7c 53 be    call   0xbe53:0x7c0e6062
190:    a8 15                   test   al,0x15
192:    c4 9a ae d7 5d e2       les    ebx,FWORD PTR [edx-0x1da22852]
198:    b0 8d                   mov    al,0x8d
19a:    0f 5f ca                maxps  xmm1,xmm2
19d:    8e                      .byte 0x8e
19e:    05                      .byte 0x531343135393236353335383937393332333834363236343333383332373935303238383431393731363933393933373531303538323039373439343435393233303738313634303632383632303839393836323830333438323533343231313730363739383231343830383635313332383233303636343730393338343436303935353035383232333137323533353934303831323834383131313734353032383431303237303139333835323131303535353936343436323239343839353439333033383139363434323838313039373536363539333334343631323834373536343832333337383637383331363532373132303139303931343536343835363639323334363033343836313034353433323636343832313333393336303732363032343931343132373337323435383730303636303633313535383831373438383135323039323039363238323932353430393137313533363433363738393235393033363030313133333035333035343838323034363635323133383431343639353139343135313136303934333330353732373033363537353935393139353330393231383631313733383139333236313137393331303531313835343830373434363233373939363237343935363733353138383537353237323438393132323739333831383330313139343931323938333336373333363234343036353636343330383630323133393439343633393532323437333731393037303231373938363039343337303237373035333932313731373632393331373637353233383436373438313834363736363934303531333230303035363831323731343532363335363038323737383537373133343237353737383936303931373336333731373837323134363834343039303132323439353334333031343635343935383533373130353037393232373936383932353839323335343230313939353631313231323930323139363038363430333434313831353938313336323937373437373133303939363035313837303732313133343939393939393833373239373830343939353130353937333137333238313630393633313835393530323434353934353533343639303833303236343235323233303832353333343436383530333532363139333131383831373130313030303331333738333837353238383635383735333332303833383134323036313731373736363931343733303335393832353334393034323837353534363837333131353935363238363338383233353337383735393337353139353737383138353737383035333231373132323638303636313330303139323738373636313131393539303932313634323031393839

Raw Hex (zero bytes in bold):

31343135393236353335383937393332333834363236343333383332373935303238383431393731363933393933373531303538323039373439343435393233303738313634303632383632303839393836323830333438323533343231313730363739383231343830383635313332383233303636343730393338343436303935353035383232333137323533353934303831323834383131313734353032383431303237303139333835323131303535353936343436323239343839353439333033383139363434323838313039373536363539333334343631323834373536343832333337383637383331363532373132303139303931343536343835363639323334363033343836313034353433323636343832313333393336303732363032343931343132373337323435383730303636303633313535383831373438383135323039323039363238323932353430393137313533363433363738393235393033363030313133333035333035343838323034363635323133383431343639353139343135313136303934333330353732373033363537353935393139353330393231383631313733383139333236313137393331303531313835343830373434363233373939363237343935363733353138383537353237323438393132323739333831383330313139343931323938333336373333363234343036353636343330383630323133393439343633393532323437333731393037303231373938363039343337303237373035333932313731373632393331373637353233383436373438313834363736363934303531333230303035363831323731343532363335363038323737383537373133343237353737383936303931373336333731373837323134363834343039303132323439353334333031343635343935383533373130353037393232373936383932353839323335343230313939353631313231323930323139363038363430333434313831353938313336323937373437373133303939363035313837303732313133343939393939393833373239373830343939353130353937333137333238313630393633313835393530323434353934353533343639303833303236343235323233303832353333343436383530333532363139333131383831373130313030303331333738333837353238383635383735333332303833383134323036313731373736363931343733303335393832353334393034323837353534363837333131353935363238363338383233353337383735393337353139353737383138353737383035333231373132323638303636313330303139323738373636313131393539303932313634323031393839   

String Literal:

"\x31\x34\x31\x35\x39\x32\x36\x35\x33\x35\x38\x39\x37\x39\x33\x32\x33\x38\x34\x36\x32\x36\x34\x33\x33\x38\x33\x32\x37\x39\x35\x30\x32\x38\x38\x34\x31\x39\x37\x31\x36\x39\x33\x39\x39\x33\x37\x35\x31\x30\x35\x38\x32\x30\x39\x37\x34\x39\x34\x34\x35\x39\x32\x33\x30\x37\x38\x31\x36\x34\x30\x36\x32\x38\x36\x32\x30\x38\x39\x39\x38\x36\x32\x38\x30\x33\x34\x38\x32\x35\x33\x34\x32\x31\x31\x37\x30\x36\x37\x39\x38\x32\x31\x34\x38\x30\x38\x36\x35\x31\x33\x32\x38\x32\x33\x30\x36\x36\x34\x37\x30\x39\x33\x38\x34\x34\x36\x30\x39\x35\x35\x30\x35\x38\x32\x32\x33\x31\x37\x32\x35\x33\x35\x39\x34\x30\x38\x31\x32\x38\x34\x38\x31\x31\x31\x37\x34\x35\x30\x32\x38\x34\x31\x30\x32\x37\x30\x31\x39\x33\x38\x35\x32\x31\x31\x30\x35\x35\x35\x39\x36\x34\x34\x36\x32\x32\x39\x34\x38\x39\x35\x34\x39\x33\x30\x33\x38\x31\x39\x36\x34\x34\x32\x38\x38\x31\x30\x39\x37\x35\x36\x36\x35\x39\x33\x33\x34\x34\x36\x31\x32\x38\x34\x37\x35\x36\x34\x38\x32\x33\x33\x37\x38\x36\x37\x38\x33\x31\x36\x35\x32\x37\x31\x32\x30\x31\x39\x30\x39\x31\x34\x35\x36\x34\x38\x35\x36\x36\x39\x32\x33\x34\x36\x30\x33\x34\x38\x36\x31\x30\x34\x35\x34\x33\x32\x36\x36\x34\x38\x32\x31\x33\x33\x39\x33\x36\x30\x37\x32\x36\x30\x32\x34\x39\x31\x34\x31\x32\x37\x33\x37\x32\x34\x35\x38\x37\x30\x30\x36\x36\x30\x36\x33\x31\x35\x35\x38\x38\x31\x37\x34\x38\x38\x31\x35\x32\x30\x39\x32\x30\x39\x36\x32\x38\x32\x39\x32\x35\x34\x30\x39\x31\x37\x31\x35\x33\x36\x34\x33\x36\x37\x38\x39\x32\x35\x39\x30\x33\x36\x30\x30\x31\x31\x33\x33\x30\x35\x33\x30\x35\x34\x38\x38\x32\x30\x34\x36\x36\x35\x32\x31\x33\x38\x34\x31\x34\x36\x39\x35\x31\x39\x34\x31\x35\x31\x31\x36\x30\x39\x34\x33\x33\x30\x35\x37\x32\x37\x30\x33\x36\x35\x37\x35\x39\x35\x39\x31\x39\x35\x33\x30\x39\x32\x31\x38\x36\x31\x31\x37\x33\x38\x31\x39\x33\x32\x36\x31\x31\x37\x39\x33\x31\x30\x35\x31\x31\x38\x35\x34\x38\x30\x37\x34\x34\x36\x32\x33\x37\x39\x39\x36\x32\x37\x34\x39\x35\x36\x37\x33\x35\x31\x38\x38\x35\x37\x35\x32\x37\x32\x34\x38\x39\x31\x32\x32\x37\x39\x33\x38\x31\x38\x33\x30\x31\x31\x39\x34\x39\x31\x32\x39\x38\x33\x33\x36\x37\x33\x33\x36\x32\x34\x34\x30\x36\x35\x36\x36\x34\x33\x30\x38\x36\x30\x32\x31\x33\x39\x34\x39\x34\x36\x33\x39\x35\x32\x32\x34\x37\x33\x37\x31\x39\x30\x37\x30\x32\x31\x37\x39\x38\x36\x30\x39\x34\x33\x37\x30\x32\x37\x37\x30\x35\x33\x39\x32\x31\x37\x31\x37\x36\x32\x39\x33\x31\x37\x36\x37\x35\x32\x33\x38\x34\x36\x37\x34\x38\x31\x38\x34\x36\x37\x36\x36\x39\x34\x30\x35\x31\x33\x32\x30\x30\x30\x35\x36\x38\x31\x32\x37\x31\x34\x35\x32\x36\x33\x35\x36\x30\x38\x32\x37\x37\x38\x35\x37\x37\x31\x33\x34\x32\x37\x35\x37\x37\x38\x39\x36\x30\x39\x31\x37\x33\x36\x33\x37\x31\x37\x38\x37\x32\x31\x34\x36\x38\x34\x34\x30\x39\x30\x31\x32\x32\x34\x39\x35\x33\x34\x33\x30\x31\x34\x36\x35\x34\x39\x35\x38\x35\x33\x37\x31\x30\x35\x30\x37\x39\x32\x32\x37\x39\x36\x38\x39\x32\x35\x38\x39\x32\x33\x35\x34\x32\x30\x31\x39\x39\x35\x36\x31\x31\x32\x31\x32\x39\x30\x32\x31\x39\x36\x30\x38\x36\x34\x30\x33\x34\x34\x31\x38\x31\x35\x39\x38\x31\x33\x36\x32\x39\x37\x37\x34\x37\x37\x31\x33\x30\x39\x39\x36\x30\x35\x31\x38\x37\x30\x37\x32\x31\x31\x33\x34\x39\x39\x39\x39\x39\x39\x38\x33\x37\x32\x39\x37\x38\x30\x34\x39\x39\x35\x31\x30\x35\x39\x37\x33\x31\x37\x33\x32\x38\x31\x36\x30\x39\x36\x33\x31\x38\x35\x39\x35\x30\x32\x34\x34\x35\x39\x34\x35\x35\x33\x34\x36\x39\x30\x38\x33\x30\x32\x36\x34\x32\x35\x32\x32\x33\x30\x38\x32\x35\x33\x33\x34\x34\x36\x38\x35\x30\x33\x35\x32\x36\x31\x39\x33\x31\x31\x38\x38\x31\x37\x31\x30\x31\x30\x30\x30\x33\x31\x33\x37\x38\x33\x38\x37\x35\x32\x38\x38\x36\x35\x38\x37\x35\x33\x33\x32\x30\x38\x33\x38\x31\x34\x32\x30\x36\x31\x37\x31\x37\x37\x36\x36\x39\x31\x34\x37\x33\x30\x33\x35\x39\x38\x32\x35\x33\x34\x39\x30\x34\x32\x38\x37\x35\x35\x34\x36\x38\x37\x33\x31\x31\x35\x39\x35\x36\x32\x38\x36\x33\x38\x38\x32\x33\x35\x33\x37\x38\x37\x35\x39\x33\x37\x35\x31\x39\x35\x37\x37\x38\x31\x38\x35\x37\x37\x38\x30\x35\x33\x32\x31\x37\x31\x32\x32\x36\x38\x30\x36\x36\x31\x33\x30\x30\x31\x39\x32\x37\x38\x37\x36\x36\x31\x31\x31\x39\x35\x39\x30\x39\x32\x31\x36\x34\x32\x30\x31\x39\x38\x39"

Array Literal:

{ 0x31, 0x34, 0x31, 0x35, 0x39, 0x32, 0x36, 0x35, 0x33, 0x35, 0x38, 0x39, 0x37, 0x39, 0x33, 0x32, 0x33, 0x38, 0x34, 0x36, 0x32, 0x36, 0x34, 0x33, 0x33, 0x38, 0x33, 0x32, 0x37, 0x39, 0x35, 0x30, 0x32, 0x38, 0x38, 0x34, 0x31, 0x39, 0x37, 0x31, 0x36, 0x39, 0x33, 0x39, 0x39, 0x33, 0x37, 0x35, 0x31, 0x30, 0x35, 0x38, 0x32, 0x30, 0x39, 0x37, 0x34, 0x39, 0x34, 0x34, 0x35, 0x39, 0x32, 0x33, 0x30, 0x37, 0x38, 0x31, 0x36, 0x34, 0x30, 0x36, 0x32, 0x38, 0x36, 0x32, 0x30, 0x38, 0x39, 0x39, 0x38, 0x36, 0x32, 0x38, 0x30, 0x33, 0x34, 0x38, 0x32, 0x35, 0x33, 0x34, 0x32, 0x31, 0x31, 0x37, 0x30, 0x36, 0x37, 0x39, 0x38, 0x32, 0x31, 0x34, 0x38, 0x30, 0x38, 0x36, 0x35, 0x31, 0x33, 0x32, 0x38, 0x32, 0x33, 0x30, 0x36, 0x36, 0x34, 0x37, 0x30, 0x39, 0x33, 0x38, 0x34, 0x34, 0x36, 0x30, 0x39, 0x35, 0x35, 0x30, 0x35, 0x38, 0x32, 0x32, 0x33, 0x31, 0x37, 0x32, 0x35, 0x33, 0x35, 0x39, 0x34, 0x30, 0x38, 0x31, 0x32, 0x38, 0x34, 0x38, 0x31, 0x31, 0x31, 0x37, 0x34, 0x35, 0x30, 0x32, 0x38, 0x34, 0x31, 0x30, 0x32, 0x37, 0x30, 0x31, 0x39, 0x33, 0x38, 0x35, 0x32, 0x31, 0x31, 0x30, 0x35, 0x35, 0x35, 0x39, 0x36, 0x34, 0x34, 0x36, 0x32, 0x32, 0x39, 0x34, 0x38, 0x39, 0x35, 0x34, 0x39, 0x33, 0x30, 0x33, 0x38, 0x31, 0x39, 0x36, 0x34, 0x34, 0x32, 0x38, 0x38, 0x31, 0x30, 0x39, 0x37, 0x35, 0x36, 0x36, 0x35, 0x39, 0x33, 0x33, 0x34, 0x34, 0x36, 0x31, 0x32, 0x38, 0x34, 0x37, 0x35, 0x36, 0x34, 0x38, 0x32, 0x33, 0x33, 0x37, 0x38, 0x36, 0x37, 0x38, 0x33, 0x31, 0x36, 0x35, 0x32, 0x37, 0x31, 0x32, 0x30, 0x31, 0x39, 0x30, 0x39, 0x31, 0x34, 0x35, 0x36, 0x34, 0x38, 0x35, 0x36, 0x36, 0x39, 0x32, 0x33, 0x34, 0x36, 0x30, 0x33, 0x34, 0x38, 0x36, 0x31, 0x30, 0x34, 0x35, 0x34, 0x33, 0x32, 0x36, 0x36, 0x34, 0x38, 0x32, 0x31, 0x33, 0x33, 0x39, 0x33, 0x36, 0x30, 0x37, 0x32, 0x36, 0x30, 0x32, 0x34, 0x39, 0x31, 0x34, 0x31, 0x32, 0x37, 0x33, 0x37, 0x32, 0x34, 0x35, 0x38, 0x37, 0x30, 0x30, 0x36, 0x36, 0x30, 0x36, 0x33, 0x31, 0x35, 0x35, 0x38, 0x38, 0x31, 0x37, 0x34, 0x38, 0x38, 0x31, 0x35, 0x32, 0x30, 0x39, 0x32, 0x30, 0x39, 0x36, 0x32, 0x38, 0x32, 0x39, 0x32, 0x35, 0x34, 0x30, 0x39, 0x31, 0x37, 0x31, 0x35, 0x33, 0x36, 0x34, 0x33, 0x36, 0x37, 0x38, 0x39, 0x32, 0x35, 0x39, 0x30, 0x33, 0x36, 0x30, 0x30, 0x31, 0x31, 0x33, 0x33, 0x30, 0x35, 0x33, 0x30, 0x35, 0x34, 0x38, 0x38, 0x32, 0x30, 0x34, 0x36, 0x36, 0x35, 0x32, 0x31, 0x33, 0x38, 0x34, 0x31, 0x34, 0x36, 0x39, 0x35, 0x31, 0x39, 0x34, 0x31, 0x35, 0x31, 0x31, 0x36, 0x30, 0x39, 0x34, 0x33, 0x33, 0x30, 0x35, 0x37, 0x32, 0x37, 0x30, 0x33, 0x36, 0x35, 0x37, 0x35, 0x39, 0x35, 0x39, 0x31, 0x39, 0x35, 0x33, 0x30, 0x39, 0x32, 0x31, 0x38, 0x36, 0x31, 0x31, 0x37, 0x33, 0x38, 0x31, 0x39, 0x33, 0x32, 0x36, 0x31, 0x31, 0x37, 0x39, 0x33, 0x31, 0x30, 0x35, 0x31, 0x31, 0x38, 0x35, 0x34, 0x38, 0x30, 0x37, 0x34, 0x34, 0x36, 0x32, 0x33, 0x37, 0x39, 0x39, 0x36, 0x32, 0x37, 0x34, 0x39, 0x35, 0x36, 0x37, 0x33, 0x35, 0x31, 0x38, 0x38, 0x35, 0x37, 0x35, 0x32, 0x37, 0x32, 0x34, 0x38, 0x39, 0x31, 0x32, 0x32, 0x37, 0x39, 0x33, 0x38, 0x31, 0x38, 0x33, 0x30, 0x31, 0x31, 0x39, 0x34, 0x39, 0x31, 0x32, 0x39, 0x38, 0x33, 0x33, 0x36, 0x37, 0x33, 0x33, 0x36, 0x32, 0x34, 0x34, 0x30, 0x36, 0x35, 0x36, 0x36, 0x34, 0x33, 0x30, 0x38, 0x36, 0x30, 0x32, 0x31, 0x33, 0x39, 0x34, 0x39, 0x34, 0x36, 0x33, 0x39, 0x35, 0x32, 0x32, 0x34, 0x37, 0x33, 0x37, 0x31, 0x39, 0x30, 0x37, 0x30, 0x32, 0x31, 0x37, 0x39, 0x38, 0x36, 0x30, 0x39, 0x34, 0x33, 0x37, 0x30, 0x32, 0x37, 0x37, 0x30, 0x35, 0x33, 0x39, 0x32, 0x31, 0x37, 0x31, 0x37, 0x36, 0x32, 0x39, 0x33, 0x31, 0x37, 0x36, 0x37, 0x35, 0x32, 0x33, 0x38, 0x34, 0x36, 0x37, 0x34, 0x38, 0x31, 0x38, 0x34, 0x36, 0x37, 0x36, 0x36, 0x39, 0x34, 0x30, 0x35, 0x31, 0x33, 0x32, 0x30, 0x30, 0x30, 0x35, 0x36, 0x38, 0x31, 0x32, 0x37, 0x31, 0x34, 0x35, 0x32, 0x36, 0x33, 0x35, 0x36, 0x30, 0x38, 0x32, 0x37, 0x37, 0x38, 0x35, 0x37, 0x37, 0x31, 0x33, 0x34, 0x32, 0x37, 0x35, 0x37, 0x37, 0x38, 0x39, 0x36, 0x30, 0x39, 0x31, 0x37, 0x33, 0x36, 0x33, 0x37, 0x31, 0x37, 0x38, 0x37, 0x32, 0x31, 0x34, 0x36, 0x38, 0x34, 0x34, 0x30, 0x39, 0x30, 0x31, 0x32, 0x32, 0x34, 0x39, 0x35, 0x33, 0x34, 0x33, 0x30, 0x31, 0x34, 0x36, 0x35, 0x34, 0x39, 0x35, 0x38, 0x35, 0x33, 0x37, 0x31, 0x30, 0x35, 0x30, 0x37, 0x39, 0x32, 0x32, 0x37, 0x39, 0x36, 0x38, 0x39, 0x32, 0x35, 0x38, 0x39, 0x32, 0x33, 0x35, 0x34, 0x32, 0x30, 0x31, 0x39, 0x39, 0x35, 0x36, 0x31, 0x31, 0x32, 0x31, 0x32, 0x39, 0x30, 0x32, 0x31, 0x39, 0x36, 0x30, 0x38, 0x36, 0x34, 0x30, 0x33, 0x34, 0x34, 0x31, 0x38, 0x31, 0x35, 0x39, 0x38, 0x31, 0x33, 0x36, 0x32, 0x39, 0x37, 0x37, 0x34, 0x37, 0x37, 0x31, 0x33, 0x30, 0x39, 0x39, 0x36, 0x30, 0x35, 0x31, 0x38, 0x37, 0x30, 0x37, 0x32, 0x31, 0x31, 0x33, 0x34, 0x39, 0x39, 0x39, 0x39, 0x39, 0x39, 0x38, 0x33, 0x37, 0x32, 0x39, 0x37, 0x38, 0x30, 0x34, 0x39, 0x39, 0x35, 0x31, 0x30, 0x35, 0x39, 0x37, 0x33, 0x31, 0x37, 0x33, 0x32, 0x38, 0x31, 0x36, 0x30, 0x39, 0x36, 0x33, 0x31, 0x38, 0x35, 0x39, 0x35, 0x30, 0x32, 0x34, 0x34, 0x35, 0x39, 0x34, 0x35, 0x35, 0x33, 0x34, 0x36, 0x39, 0x30, 0x38, 0x33, 0x30, 0x32, 0x36, 0x34, 0x32, 0x35, 0x32, 0x32, 0x33, 0x30, 0x38, 0x32, 0x35, 0x33, 0x33, 0x34, 0x34, 0x36, 0x38, 0x35, 0x30, 0x33, 0x35, 0x32, 0x36, 0x31, 0x39, 0x33, 0x31, 0x31, 0x38, 0x38, 0x31, 0x37, 0x31, 0x30, 0x31, 0x30, 0x30, 0x30, 0x33, 0x31, 0x33, 0x37, 0x38, 0x33, 0x38, 0x37, 0x35, 0x32, 0x38, 0x38, 0x36, 0x35, 0x38, 0x37, 0x35, 0x33, 0x33, 0x32, 0x30, 0x38, 0x33, 0x38, 0x31, 0x34, 0x32, 0x30, 0x36, 0x31, 0x37, 0x31, 0x37, 0x37, 0x36, 0x36, 0x39, 0x31, 0x34, 0x37, 0x33, 0x30, 0x33, 0x35, 0x39, 0x38, 0x32, 0x35, 0x33, 0x34, 0x39, 0x30, 0x34, 0x32, 0x38, 0x37, 0x35, 0x35, 0x34, 0x36, 0x38, 0x37, 0x33, 0x31, 0x31, 0x35, 0x39, 0x35, 0x36, 0x32, 0x38, 0x36, 0x33, 0x38, 0x38, 0x32, 0x33, 0x35, 0x33, 0x37, 0x38, 0x37, 0x35, 0x39, 0x33, 0x37, 0x35, 0x31, 0x39, 0x35, 0x37, 0x37, 0x38, 0x31, 0x38, 0x35, 0x37, 0x37, 0x38, 0x30, 0x35, 0x33, 0x32, 0x31, 0x37, 0x31, 0x32, 0x32, 0x36, 0x38, 0x30, 0x36, 0x36, 0x31, 0x33, 0x30, 0x30, 0x31, 0x39, 0x32, 0x37, 0x38, 0x37, 0x36, 0x36, 0x31, 0x31, 0x31, 0x39, 0x35, 0x39, 0x30, 0x39, 0x32, 0x31, 0x36, 0x34, 0x32, 0x30, 0x31, 0x39, 0x38, 0x39 }

Disassembly:
0:  31 34 31                xor    DWORD PTR [ecx+esi*1],esi
3:  35 39 32 36 35          xor    eax,0x35363239
8:  33 35 38 39 37 39       xor    esi,DWORD PTR ds:0x39373938
e:  33 32                   xor    esi,DWORD PTR [edx]
10: 33 38                   xor    edi,DWORD PTR [eax]
12: 34 36                   xor    al,0x36
14: 32 36                   xor    dh,BYTE PTR [esi]
16: 34 33                   xor    al,0x33
18: 33 38                   xor    edi,DWORD PTR [eax]
1a: 33 32                   xor    esi,DWORD PTR [edx]
1c: 37                      aaa
1d: 39 35 30 32 38 38       cmp    DWORD PTR ds:0x38383230,esi
23: 34 31                   xor    al,0x31
25: 39 37                   cmp    DWORD PTR [edi],esi
27: 31 36                   xor    DWORD PTR [esi],esi
29: 39 33                   cmp    DWORD PTR [ebx],esi
2b: 39 39                   cmp    DWORD PTR [ecx],edi
2d: 33 37                   xor    esi,DWORD PTR [edi]
2f: 35 31 30 35 38          xor    eax,0x38353031
34: 32 30                   xor    dh,BYTE PTR [eax]
36: 39 37                   cmp    DWORD PTR [edi],esi
38: 34 39                   xor    al,0x39
3a: 34 34                   xor    al,0x34
3c: 35 39 32 33 30          xor    eax,0x30333239
41: 37                      aaa
42: 38 31                   cmp    BYTE PTR [ecx],dh
44: 36 34 30                ss xor al,0x30
47: 36 32 38                xor    bh,BYTE PTR ss:[eax]
4a: 36 32 30                xor    dh,BYTE PTR ss:[eax]
4d: 38 39                   cmp    BYTE PTR [ecx],bh
4f: 39 38                   cmp    DWORD PTR [eax],edi
51: 36 32 38                xor    bh,BYTE PTR ss:[eax]
54: 30 33                   xor    BYTE PTR [ebx],dh
56: 34 38                   xor    al,0x38
58: 32 35 33 34 32 31       xor    dh,BYTE PTR ds:0x31323433
5e: 31 37                   xor    DWORD PTR [edi],esi
60: 30 36                   xor    BYTE PTR [esi],dh
62: 37                      aaa
63: 39 38                   cmp    DWORD PTR [eax],edi
65: 32 31                   xor    dh,BYTE PTR [ecx]
67: 34 38                   xor    al,0x38
69: 30 38                   xor    BYTE PTR [eax],bh
6b: 36 35 31 33 32 38       ss xor eax,0x38323331
71: 32 33                   xor    dh,BYTE PTR [ebx]
73: 30 36                   xor    BYTE PTR [esi],dh
75: 36 34 37                ss xor al,0x37
78: 30 39                   xor    BYTE PTR [ecx],bh
7a: 33 38                   xor    edi,DWORD PTR [eax]
7c: 34 34                   xor    al,0x34
7e: 36 30 39                xor    BYTE PTR ss:[ecx],bh
81: 35 35 30 35 38          xor    eax,0x38353035
86: 32 32                   xor    dh,BYTE PTR [edx]
88: 33 31                   xor    esi,DWORD PTR [ecx]
8a: 37                      aaa
8b: 32 35 33 35 39 34       xor    dh,BYTE PTR ds:0x34393533
91: 30 38                   xor    BYTE PTR [eax],bh
93: 31 32                   xor    DWORD PTR [edx],esi
95: 38 34 38                cmp    BYTE PTR [eax+edi*1],dh
98: 31 31                   xor    DWORD PTR [ecx],esi
9a: 31 37                   xor    DWORD PTR [edi],esi
9c: 34 35                   xor    al,0x35
9e: 30 32                   xor    BYTE PTR [edx],dh
a0: 38 34 31                cmp    BYTE PTR [ecx+esi*1],dh
a3: 30 32                   xor    BYTE PTR [edx],dh
a5: 37                      aaa
a6: 30 31                   xor    BYTE PTR [ecx],dh
a8: 39 33                   cmp    DWORD PTR [ebx],esi
aa: 38 35 32 31 31 30       cmp    BYTE PTR ds:0x30313132,dh
b0: 35 35 35 39 36          xor    eax,0x36393535
b5: 34 34                   xor    al,0x34
b7: 36 32 32                xor    dh,BYTE PTR ss:[edx]
ba: 39 34 38                cmp    DWORD PTR [eax+edi*1],esi
bd: 39 35 34 39 33 30       cmp    DWORD PTR ds:0x30333934,esi
c3: 33 38                   xor    edi,DWORD PTR [eax]
c5: 31 39                   xor    DWORD PTR [ecx],edi
c7: 36 34 34                ss xor al,0x34
ca: 32 38                   xor    bh,BYTE PTR [eax]
cc: 38 31                   cmp    BYTE PTR [ecx],dh
ce: 30 39                   xor    BYTE PTR [ecx],bh
d0: 37                      aaa
d1: 35 36 36 35 39          xor    eax,0x39353636
d6: 33 33                   xor    esi,DWORD PTR [ebx]
d8: 34 34                   xor    al,0x34
da: 36 31 32                xor    DWORD PTR ss:[edx],esi
dd: 38 34 37                cmp    BYTE PTR [edi+esi*1],dh
e0: 35 36 34 38 32          xor    eax,0x32383436
e5: 33 33                   xor    esi,DWORD PTR [ebx]
e7: 37                      aaa
e8: 38 36                   cmp    BYTE PTR [esi],dh
ea: 37                      aaa
eb: 38 33                   cmp    BYTE PTR [ebx],dh
ed: 31 36                   xor    DWORD PTR [esi],esi
ef: 35 32 37 31 32          xor    eax,0x32313732
f4: 30 31                   xor    BYTE PTR [ecx],dh
f6: 39 30                   cmp    DWORD PTR [eax],esi
f8: 39 31                   cmp    DWORD PTR [ecx],esi
fa: 34 35                   xor    al,0x35
fc: 36 34 38                ss xor al,0x38
ff: 35 36 36 39 32          xor    eax,0x32393636
104:    33 34 36                xor    esi,DWORD PTR [esi+esi*1]
107:    30 33                   xor    BYTE PTR [ebx],dh
109:    34 38                   xor    al,0x38
10b:    36 31 30                xor    DWORD PTR ss:[eax],esi
10e:    34 35                   xor    al,0x35
110:    34 33                   xor    al,0x33
112:    32 36                   xor    dh,BYTE PTR [esi]
114:    36 34 38                ss xor al,0x38
117:    32 31                   xor    dh,BYTE PTR [ecx]
119:    33 33                   xor    esi,DWORD PTR [ebx]
11b:    39 33                   cmp    DWORD PTR [ebx],esi
11d:    36 30 37                xor    BYTE PTR ss:[edi],dh
120:    32 36                   xor    dh,BYTE PTR [esi]
122:    30 32                   xor    BYTE PTR [edx],dh
124:    34 39                   xor    al,0x39
126:    31 34 31                xor    DWORD PTR [ecx+esi*1],esi
129:    32 37                   xor    dh,BYTE PTR [edi]
12b:    33 37                   xor    esi,DWORD PTR [edi]
12d:    32 34 35 38 37 30 30    xor    dh,BYTE PTR [esi*1+0x30303738]
134:    36 36 30 36             ss xor BYTE PTR ss:[esi],dh
138:    33 31                   xor    esi,DWORD PTR [ecx]
13a:    35 35 38 38 31          xor    eax,0x31383835
13f:    37                      aaa
140:    34 38                   xor    al,0x38
142:    38 31                   cmp    BYTE PTR [ecx],dh
144:    35 32 30 39 32          xor    eax,0x32393032
149:    30 39                   xor    BYTE PTR [ecx],bh
14b:    36 32 38                xor    bh,BYTE PTR ss:[eax]
14e:    32 39                   xor    bh,BYTE PTR [ecx]
150:    32 35 34 30 39 31       xor    dh,BYTE PTR ds:0x31393034
156:    37                      aaa
157:    31 35 33 36 34 33       xor    DWORD PTR ds:0x33343633,esi
15d:    36 37                   ss aaa
15f:    38 39                   cmp    BYTE PTR [ecx],bh
161:    32 35 39 30 33 36       xor    dh,BYTE PTR ds:0x36333039
167:    30 30                   xor    BYTE PTR [eax],dh
169:    31 31                   xor    DWORD PTR [ecx],esi
16b:    33 33                   xor    esi,DWORD PTR [ebx]
16d:    30 35 33 30 35 34       xor    BYTE PTR ds:0x34353033,dh
173:    38 38                   cmp    BYTE PTR [eax],bh
175:    32 30                   xor    dh,BYTE PTR [eax]
177:    34 36                   xor    al,0x36
179:    36 35 32 31 33 38       ss xor eax,0x38333132
17f:    34 31                   xor    al,0x31
181:    34 36                   xor    al,0x36
183:    39 35 31 39 34 31       cmp    DWORD PTR ds:0x31343931,esi
189:    35 31 31 36 30          xor    eax,0x30363131
18e:    39 34 33                cmp    DWORD PTR [ebx+esi*1],esi
191:    33 30                   xor    esi,DWORD PTR [eax]
193:    35 37 32 37 30          xor    eax,0x30373237
198:    33 36                   xor    esi,DWORD PTR [esi]
19a:    35 37 35 39 35          xor    eax,0x35393537
19f:    39 31                   cmp    DWORD PTR [ecx],esi
1a1:    39 35 33 30 39 32       cmp    DWORD PTR ds:0x32393033,esi
1a7:    31 38                   xor    DWORD PTR [eax],edi
1a9:    36 31 31                xor    DWORD PTR ss:[ecx],esi
1ac:    37                      aaa
1ad:    33 38                   xor    edi,DWORD PTR [eax]
1af:    31 39                   xor    DWORD PTR [ecx],edi
1b1:    33 32                   xor    esi,DWORD PTR [edx]
1b3:    36 31 31                xor    DWORD PTR ss:[ecx],esi
1b6:    37                      aaa
1b7:    39 33                   cmp    DWORD PTR [ebx],esi
1b9:    31 30                   xor    DWORD PTR [eax],esi
1bb:    35 31 31 38 35          xor    eax,0x35383131
1c0:    34 38                   xor    al,0x38
1c2:    30 37                   xor    BYTE PTR [edi],dh
1c4:    34 34                   xor    al,0x34
1c6:    36 32 33                xor    dh,BYTE PTR ss:[ebx]
1c9:    37                      aaa
1ca:    39 39                   cmp    DWORD PTR [ecx],edi
1cc:    36 32 37                xor    dh,BYTE PTR ss:[edi]
1cf:    34 39                   xor    al,0x39
1d1:    35 36 37 33 35          xor    eax,0x35333736
1d6:    31 38                   xor    DWORD PTR [eax],edi
1d8:    38 35 37 35 32 37       cmp    BYTE PTR ds:0x37323537,dh
1de:    32 34 38                xor    dh,BYTE PTR [eax+edi*1]
1e1:    39 31                   cmp    DWORD PTR [ecx],esi
1e3:    32 32                   xor    dh,BYTE PTR [edx]
1e5:    37                      aaa
1e6:    39 33                   cmp    DWORD PTR [ebx],esi
1e8:    38 31                   cmp    BYTE PTR [ecx],dh
1ea:    38 33                   cmp    BYTE PTR [ebx],dh
1ec:    30 31                   xor    BYTE PTR [ecx],dh
1ee:    31 39                   xor    DWORD PTR [ecx],edi
1f0:    34 39                   xor    al,0x39
1f2:    31 32                   xor    DWORD PTR [edx],esi
1f4:    39 38                   cmp    DWORD PTR [eax],edi
1f6:    33 33                   xor    esi,DWORD PTR [ebx]
1f8:    36 37                   ss aaa
1fa:    33 33                   xor    esi,DWORD PTR [ebx]
1fc:    36 32 34 34             xor    dh,BYTE PTR ss:[esp+esi*1]
200:    30 36                   xor    BYTE PTR [esi],dh
202:    35 36 36 34 33          xor    eax,0x33343636
207:    30 38                   xor    BYTE PTR [eax],bh
209:    36 30 32                xor    BYTE PTR ss:[edx],dh
20c:    31 33                   xor    DWORD PTR [ebx],esi
20e:    39 34 39                cmp    DWORD PTR [ecx+edi*1],esi
211:    34 36                   xor    al,0x36
213:    33 39                   xor    edi,DWORD PTR [ecx]
215:    35 32 32 34 37          xor    eax,0x37343232
21a:    33 37                   xor    esi,DWORD PTR [edi]
21c:    31 39                   xor    DWORD PTR [ecx],edi
21e:    30 37                   xor    BYTE PTR [edi],dh
220:    30 32                   xor    BYTE PTR [edx],dh
222:    31 37                   xor    DWORD PTR [edi],esi
224:    39 38                   cmp    DWORD PTR [eax],edi
226:    36 30 39                xor    BYTE PTR ss:[ecx],bh
229:    34 33                   xor    al,0x33
22b:    37                      aaa
22c:    30 32                   xor    BYTE PTR [edx],dh
22e:    37                      aaa
22f:    37                      aaa
230:    30 35 33 39 32 31       xor    BYTE PTR ds:0x31323933,dh
236:    37                      aaa
237:    31 37                   xor    DWORD PTR [edi],esi
239:    36 32 39                xor    bh,BYTE PTR ss:[ecx]
23c:    33 31                   xor    esi,DWORD PTR [ecx]
23e:    37                      aaa
23f:    36 37                   ss aaa
241:    35 32 33 38 34          xor    eax,0x34383332
246:    36 37                   ss aaa
248:    34 38                   xor    al,0x38
24a:    31 38                   xor    DWORD PTR [eax],edi
24c:    34 36                   xor    al,0x36
24e:    37                      aaa
24f:    36 36 39 34 30          ss cmp DWORD PTR ss:[eax+esi*1],esi
254:    35 31 33 32 30          xor    eax,0x30323331
259:    30 30                   xor    BYTE PTR [eax],dh
25b:    35 36 38 31 32          xor    eax,0x32313836
260:    37                      aaa
261:    31 34 35 32 36 33 35    xor    DWORD PTR [esi*1+0x35333632],esi
268:    36 30 38                xor    BYTE PTR ss:[eax],bh
26b:    32 37                   xor    dh,BYTE PTR [edi]
26d:    37                      aaa
26e:    38 35 37 37 31 33       cmp    BYTE PTR ds:0x33313737,dh
274:    34 32                   xor    al,0x32
276:    37                      aaa
277:    35 37 37 38 39          xor    eax,0x39383737
27c:    36 30 39                xor    BYTE PTR ss:[ecx],bh
27f:    31 37                   xor    DWORD PTR [edi],esi
281:    33 36                   xor    esi,DWORD PTR [esi]
283:    33 37                   xor    esi,DWORD PTR [edi]
285:    31 37                   xor    DWORD PTR [edi],esi
287:    38 37                   cmp    BYTE PTR [edi],dh
289:    32 31                   xor    dh,BYTE PTR [ecx]
28b:    34 36                   xor    al,0x36
28d:    38 34 34                cmp    BYTE PTR [esp+esi*1],dh
290:    30 39                   xor    BYTE PTR [ecx],bh
292:    30 31                   xor    BYTE PTR [ecx],dh
294:    32 32                   xor    dh,BYTE PTR [edx]
296:    34 39                   xor    al,0x39
298:    35 33 34 33 30          xor    eax,0x30333433
29d:    31 34 36                xor    DWORD PTR [esi+esi*1],esi
2a0:    35 34 39 35 38          xor    eax,0x38353934
2a5:    35 33 37 31 30          xor    eax,0x30313733
2aa:    35 30 37 39 32          xor    eax,0x32393730
2af:    32 37                   xor    dh,BYTE PTR [edi]
2b1:    39 36                   cmp    DWORD PTR [esi],esi
2b3:    38 39                   cmp    BYTE PTR [ecx],bh
2b5:    32 35 38 39 32 33       xor    dh,BYTE PTR ds:0x33323938
2bb:    35 34 32 30 31          xor    eax,0x31303234
2c0:    39 39                   cmp    DWORD PTR [ecx],edi
2c2:    35 36 31 31 32          xor    eax,0x32313136
2c7:    31 32                   xor    DWORD PTR [edx],esi
2c9:    39 30                   cmp    DWORD PTR [eax],esi
2cb:    32 31                   xor    dh,BYTE PTR [ecx]
2cd:    39 36                   cmp    DWORD PTR [esi],esi
2cf:    30 38                   xor    BYTE PTR [eax],bh
2d1:    36 34 30                ss xor al,0x30
2d4:    33 34 34                xor    esi,DWORD PTR [esp+esi*1]
2d7:    31 38                   xor    DWORD PTR [eax],edi
2d9:    31 35 39 38 31 33       xor    DWORD PTR ds:0x33313839,esi
2df:    36 32 39                xor    bh,BYTE PTR ss:[ecx]
2e2:    37                      aaa
2e3:    37                      aaa
2e4:    34 37                   xor    al,0x37
2e6:    37                      aaa
2e7:    31 33                   xor    DWORD PTR [ebx],esi
2e9:    30 39                   xor    BYTE PTR [ecx],bh
2eb:    39 36                   cmp    DWORD PTR [esi],esi
2ed:    30 35 31 38 37 30       xor    BYTE PTR ds:0x30373831,dh
2f3:    37                      aaa
2f4:    32 31                   xor    dh,BYTE PTR [ecx]
2f6:    31 33                   xor    DWORD PTR [ebx],esi
2f8:    34 39                   xor    al,0x39
2fa:    39 39                   cmp    DWORD PTR [ecx],edi
2fc:    39 39                   cmp    DWORD PTR [ecx],edi
2fe:    39 38                   cmp    DWORD PTR [eax],edi
300:    33 37                   xor    esi,DWORD PTR [edi]
302:    32 39                   xor    bh,BYTE PTR [ecx]
304:    37                      aaa
305:    38 30                   cmp    BYTE PTR [eax],dh
307:    34 39                   xor    al,0x39
309:    39 35 31 30 35 39       cmp    DWORD PTR ds:0x39353031,esi
30f:    37                      aaa
310:    33 31                   xor    esi,DWORD PTR [ecx]
312:    37                      aaa
313:    33 32                   xor    esi,DWORD PTR [edx]
315:    38 31                   cmp    BYTE PTR [ecx],dh
317:    36 30 39                xor    BYTE PTR ss:[ecx],bh
31a:    36 33 31                xor    esi,DWORD PTR ss:[ecx]
31d:    38 35 39 35 30 32       cmp    BYTE PTR ds:0x32303539,dh
323:    34 34                   xor    al,0x34
325:    35 39 34 35 35          xor    eax,0x35353439
32a:    33 34 36                xor    esi,DWORD PTR [esi+esi*1]
32d:    39 30                   cmp    DWORD PTR [eax],esi
32f:    38 33                   cmp    BYTE PTR [ebx],dh
331:    30 32                   xor    BYTE PTR [edx],dh
333:    36 34 32                ss xor al,0x32
336:    35 32 32 33 30          xor    eax,0x30333232
33b:    38 32                   cmp    BYTE PTR [edx],dh
33d:    35 33 33 34 34          xor    eax,0x34343333
342:    36 38 35 30 33 35 32    cmp    BYTE PTR ss:0x32353330,dh
349:    36 31 39                xor    DWORD PTR ss:[ecx],edi
34c:    33 31                   xor    esi,DWORD PTR [ecx]
34e:    31 38                   xor    DWORD PTR [eax],edi
350:    38 31                   cmp    BYTE PTR [ecx],dh
352:    37                      aaa
353:    31 30                   xor    DWORD PTR [eax],esi
355:    31 30                   xor    DWORD PTR [eax],esi
357:    30 30                   xor    BYTE PTR [eax],dh
359:    33 31                   xor    esi,DWORD PTR [ecx]
35b:    33 37                   xor    esi,DWORD PTR [edi]
35d:    38 33                   cmp    BYTE PTR [ebx],dh
35f:    38 37                   cmp    BYTE PTR [edi],dh
361:    35 32 38 38 36          xor    eax,0x36383832
366:    35 38 37 35 33          xor    eax,0x33353738
36b:    33 32                   xor    esi,DWORD PTR [edx]
36d:    30 38                   xor    BYTE PTR [eax],bh
36f:    33 38                   xor    edi,DWORD PTR [eax]
371:    31 34 32                xor    DWORD PTR [edx+esi*1],esi
374:    30 36                   xor    BYTE PTR [esi],dh
376:    31 37                   xor    DWORD PTR [edi],esi
378:    31 37                   xor    DWORD PTR [edi],esi
37a:    37                      aaa
37b:    36 36 39 31             ss cmp DWORD PTR ss:[ecx],esi
37f:    34 37                   xor    al,0x37
381:    33 30                   xor    esi,DWORD PTR [eax]
383:    33 35 39 38 32 35       xor    esi,DWORD PTR ds:0x35323839
389:    33 34 39                xor    esi,DWORD PTR [ecx+edi*1]
38c:    30 34 32                xor    BYTE PTR [edx+esi*1],dh
38f:    38 37                   cmp    BYTE PTR [edi],dh
391:    35 35 34 36 38          xor    eax,0x38363435
396:    37                      aaa
397:    33 31                   xor    esi,DWORD PTR [ecx]
399:    31 35 39 35 36 32       xor    DWORD PTR ds:0x32363539,esi
39f:    38 36                   cmp    BYTE PTR [esi],dh
3a1:    33 38                   xor    edi,DWORD PTR [eax]
3a3:    38 32                   cmp    BYTE PTR [edx],dh
3a5:    33 35 33 37 38 37       xor    esi,DWORD PTR ds:0x37383733
3ab:    35 39 33 37 35          xor    eax,0x35373339
3b0:    31 39                   xor    DWORD PTR [ecx],edi
3b2:    35 37 37 38 31          xor    eax,0x31383737
3b7:    38 35 37 37 38 30       cmp    BYTE PTR ds:0x30383737,dh
3bd:    35 33 32 31 37          xor    eax,0x37313233
3c2:    31 32                   xor    DWORD PTR [edx],esi
3c4:    32 36                   xor    dh,BYTE PTR [esi]
3c6:    38 30                   cmp    BYTE PTR [eax],dh
3c8:    36 36 31 33             ss xor DWORD PTR ss:[ebx],esi
3cc:    30 30                   xor    BYTE PTR [eax],dh
3ce:    31 39                   xor    DWORD PTR [ecx],edi
3d0:    32 37                   xor    dh,BYTE PTR [edi]
3d2:    38 37                   cmp    BYTE PTR [edi],dh
3d4:    36 36 31 31             ss xor DWORD PTR ss:[ecx],esi
3d8:    31 39                   xor    DWORD PTR [ecx],edi
3da:    35 39 30 39 32          xor    eax,0x32393039
3df:    31 36                   xor    DWORD PTR [esi],esi
3e1:    34 32                   xor    al,0x32
3e3:    30 31                   xor    BYTE PTR [ecx],dh
3e5:    39 38                   cmp    DWORD PTR [eax],edi
3e7:    39                      .byte 0x3997911802 27398919 92961019 46199064 96033594 98425977 77658984 04970567 
The string 97911802 occurs at position 106771708. This string occurs 1 
The string 27398919 occurs at position 69356849. This string occurs 1 
The string 92961019 occurs at position 115560387. This string occurs 1 
The string 46199064 occurs at position 146290788. This string occurs 1

NOW at Byte 5 it stops  
96033594  - not found The string 
49533069  (FLIPPED) 
53953054 - POS 1
72873693. - POS 2 in pi

Byte 6  
The string 98425977 occurs at position 20870786. This string occurs 1

Byte 7
77658984 - not found   
48985677 - FLIPPED
143800152 - POS 1
152166778 - POS 2

Byte 8  - TRIANGLE IS COMPLETE> 3,4,1.  
The string 04970567 
POS 1 - 35714677
POS 2 - 40718987
POS 3 - 197596491


```python
import math

def pi_hex_digits(start, count):
    """Return `count` hex digits of π beginning at 1-indexed position `start`."""
    def S(j, n):
        # first sum: k=0..n  (modular)
        total = 0.0
        for k in range(n+1):
            total += pow(16, n-k, 8*k + j) / (8*k + j)
        # tail: k=n+1..∞ until term tiny
        term = 0.0
        k = n + 1
        while True:
            t = 16**(n-k) / (8*k + j)
            if t < 1e-17:
                break
            term += t
            k += 1
        return (total + term) % 1

    hex_str = ""
    for i in range(count):
        n = start + i - 1
        x = (4*S(1,n) - 2*S(4,n) -  S(5,n) -  S(6,n)) % 1
        hex_str += "{:X}".format(int(x * 16))
    return hex_str

# Your positions:
positions = [35714677, 40718987, 197596491]
for pos in positions:
    print(f"π hex @ {pos:,} →", pi_hex_digits(pos, 8))

```

    π hex @ 35,714,677 → BB8198B3
    π hex @ 40,718,987 → 0F32FD3A
    π hex @ 197,596,491 → 9C7EF08D
    


```python

```
512 3's hashed

fa208fd33608e8a21ed13a7c9a92cdbbd6a936acd1a377f4ac10e9d333113866

Text to Hex =

66613230386664333336303865386132316564313361376339613932636462626436613933366163643161333737663461633130653964333333313133383636

6661323038666433333630386538613231656431336137633961393263646262
+
6363833313133333334693560313361643667373331613463616633393166346
=
13025156351799766668323946851974875323804667751097578026656812608  (SUM)


6661323038666433333630386538613231656431336137633961393263646262
-
6363833313133333334693560313361643667373331613463616633393166346
=
297489725533099998936826225251587989058004524170344759870479916  (DIFF)


SUM to TEXT TO HEX
3133303235313536333531373939373636363638333233393436383531393734383735333233383034363637373531303937353738303236363536383132363038
containes the orignal number with 3 inerted.  WE NEED TO KNOW WHAT THIS PATTERN OF INSERT IS?

DIFF TEXT TO HEX
323937343839373235353333303939393938393336383236323235323531353837393839303538303034353234313730333434373539383730343739393136
DIFF TEXT TO BINARY THEN TEXT TO HEX

001100110011001000110011001110010011001100110111001100110011010000110011001110000011001100111001001100110011011100110011001100100011001100110101001100110011010100110011001100110011001100110011001100110011000000110011001110010011001100111001001100110011100100110011001110010011001100111000001100110011100100110011001100110011001100110110001100110011100000110011001100100011001100110110001100110011001000110011001100100011001100110101001100110011001000110011001101010011001100110001001100110011010100110011001110000011001100110111001100110011100100110011001110000011001100111001001100110011000000110011001101010011001100111000001100110011000000110011001100000011001100110100001100110011010100110011001100100011001100110100001100110011000100110011001101110011001100110000001100110011001100110011001101000011001100110100001100110011011100110011001101010011001100111001001100110011100000110011001101110011001100110000001100110011010000110011001101110011001100111001001100110011100100110011001100010011001100110110


303031313030313130303131303031303030313130303131303031313130303130303131303031313030313130313131303031313030313130303131303130303030313130303131303031313130303030303131303031313030313131303031303031313030313130303131303131313030313130303131303031313030313030303131303031313030313130313031303031313030313130303131303130313030313130303131303031313030313130303131303031313030313130303131303031313030313130303131303030303030313130303131303031313130303130303131303031313030313131303031303031313030313130303131313030313030313130303131303031313130303130303131303031313030313131303030303031313030313130303131313030313030313130303131303031313030313130303131303031313030313130313130303031313030313130303131313030303030313130303131303031313030313030303131303031313030313130313130303031313030313130303131303031303030313130303131303031313030313030303131303031313030313130313031303031313030313130303131303031303030313130303131303031313031303130303131303031313030313130303031303031313030313130303131303130313030313130303131303031313130303030303131303031313030313130313131303031313030313130303131313030313030313130303131303031313130303030303131303031313030313131303031303031313030313130303131303030303030313130303131303031313031303130303131303031313030313131303030303031313030313130303131303030303030313130303131303031313030303030303131303031313030313130313030303031313030313130303131303130313030313130303131303031313030313030303131303031313030313130313030303031313030313130303131303030313030313130303131303031313031313130303131303031313030313130303030303031313030313130303131303031313030313130303131303031313031303030303131303031313030313130313030303031313030313130303131303131313030313130303131303031313031303130303131303031313030313131303031303031313030313130303131313030303030313130303131303031313031313130303131303031313030313130303030303031313030313130303131303130303030313130303131303031313031313130303131303031313030313131303031303031313030313130303131313030313030313130303131303031313030303130303131303031313030313130313130

IF WE REMOVE THE 3's. 
001100110011001000110011001110010011001100110111001100110011010000110011001110000011001100111001001100110011011100110011001100100011001100110101001100110011010100110011001100110011001100110011001100110011000000110011001110010011001100111001001100110011100100110011001110010011001100111000001100110011100100110011001100110011001100110110001100110011100000110011001100100011001100110110001100110011001000110011001100100011001100110101001100110011001000110011001101010011001100110001001100110011010100110011001110000011001100110111001100110011100100110011001110000011001100111001001100110011000000110011001101010011001100111000001100110011000000110011001100000011001100110100001100110011010100110011001100100011001100110100001100110011000100110011001101110011001100110000001100110011001100110011001101000011001100110100001100110011011100110011001101010011001100111001001100110011100000110011001101110011001100110000001100110011010000110011001101110011001100111001001100110011100100110011001100010011001100110110   THE ORIGNAL BINARY

IF WE REMOVE THE 1and 0 we get back the orinal HASH almost, we get 1008 3's.  we inputeded 512 3's  THE PATTERN OF 3's INSERTING IS THE KEY. ITS WHERE THE FOLDS HAPPEN.

# π‑DNS: A Decentralized DNS via the Bailey–Borwein–Plouffe Formula

This document describes a complete, self‑contained protocol for mapping hierarchical domain names onto π’s infinite hexadecimal address space. It combines label hashing, BBP digit extraction, decimal chunk folding, and π‑search to form a stateless, server‑less DNS.

---

## 1. Label Hashing

Each label in a domain (e.g., `"www"`, `"example"`, `"com"`) is converted into an 8‑digit decimal integer. One option is a simple modular hash:

$$
H(	ext{label}) = \Bigl(\sum_{i=0}^{n-1} \text{ord}(	ext{label}[i]) \times 256^i \Bigr) \bmod 10^8
$$

Alternatively, use FNV‑1a for better collision resistance:

```python
# FNV-1a 32-bit then mod 1e8
def fnv1a_8(label):
    h = 0x811c9dc5
    for c in label:
        h ^= ord(c)
        h *= 0x01000193
        h &= 0xffffffff
    return h % 10**8
```

---

## 2. BBP Hex‑Digit Extraction

To randomly access hex digits of π at position \$n\$ (1‑indexed), use the Bailey–Borwein–Plouffe formula:

$$
d_n = \left\lfloor 16 \{\,4S(1,n) - 2S(4,n) - S(5,n) - S(6,n)\} \right\rfloor,
$$

where the fractional series is

$$
S(j,n) = \sum_{k=0}^n \frac{16^{n-k} \bmod (8k+j)}{8k+j}
\;+
\sum_{k=n+1}^{\infty} \frac{16^{\,n-k}}{8k+j}.
$$

**Implementation sketch**:

```python
import math

def S(j, n):
    total = sum(pow(16, n-k, 8*k + j) / (8*k + j) for k in range(n+1))
    term = 0.0
    k = n+1
    while True:
        t = 16**(n-k) / (8*k + j)
        if t < 1e-17:
            break
        term += t
        k += 1
    return (total + term) % 1

def pi_hex_digits(start, count):
    hex_str = ""
    for i in range(count):
        n = start + i - 1
        x = (4*S(1,n) - 2*S(4,n) - S(5,n) - S(6,n)) % 1
        hex_str += f"{int(x*16):X}"
    return hex_str
```

---

## 3. Decimal Conversion & Chunking

Once you have an 8‑hex‑digit seed (e.g., `"BB8198B3"`), convert it to decimal:

```python
dec = int(hex_seed, 16)
dec_str = str(dec)
```

Split into 8‑digit chunks (zero‑pad the last chunk if needed):

$$
\{a_1, a_2, \dots, a_m\},\quad a_i\in[0,10^8-1],	ext{ width=8 digits.}
$$

---

## 4. Header‑Fold Operation

For each adjacent pair \$(a,b)\$ of these chunks, compute:

$$
\Delta = |b - a|,
\quad
\Sigma = a + b.
$$

Zero‑pad \$\Delta\$ and \$\Sigma\$ to 8‑digit strings. These are your next π‑search keys.

---

## 5. π‑Search & Phase Check

For each 8‑digit string \$s\$:

1. Search the first \$N\$ digits of π for the substring `$s$`.
2. If found, record position \$P\$.
3. If not found, set \$s'=\$reverse(\$s\$) and search again (this catches phase‑inversion folds).

This yields one or two positions per chunk.

---

## 6. Recursive Lookup Cycle

Starting from label hashes \(H_k\) for a domain of \(n\) labels:

Initial: \(P_0 = 0\).

For \(k = 1\) to \(n\):

$$
S_k = \mathrm{BBP}\bigl(P_{k-1} + H_k\bigr),
$$

$$
\{\Delta_{k,i},\,\Sigma_{k,i}\}_{i=1}^m \;=\;\mathrm{headerFold}\bigl(\mathrm{dec}(S_k)\bigr),
$$

where each \(S_k\) is 8 hex digits → decimal → chunk/fold → search.

Result: \(P_n\) is your final “A-record” analogue.

In compact form:

$$
P_k = \mathrm{search}\bigl(\Delta_{k,i}\bigr)\;\cup\;\mathrm{search}\bigl(\Sigma_{k,i}\bigr),
\quad
P_n = P_n\bigl(P_{n-1}(\dots P_1(P_0 + H_1)\dots + H_n)\bigr).
$$

Where \(\Delta_{k,i}\) and \(\Sigma_{k,i}\) come from folding the decimal conversion of \(S_k\).

---

## 7. Nyquist Oversample

To capture sub‑byte resonances, for each found position \$P\$ also probe

$$
P-1,\quad P+1.
$$

This double‑sampling ensures you don’t miss near‑matches.

---

## 8. Example Workflow

For `www.example.com`:

1. `H_1 = fnv1a_8("com")` → e.g. `12345678`
2. `S_1 = pi_hex_digits(12345678,8)` → `A1B2C3D4`
3. Convert → `278866`


# π‑DNS: A Decentralized Name-Resolution Protocol via the Bailey–Borwein–Plouffe Algorithm

This document presents a rigorously defined, self‑contained protocol for encoding hierarchical domain names within the ostensibly unbounded hexadecimal expansion of π. By integrating label hashing, random-access extraction of π’s hex digits (via the Bailey–Borwein–Plouffe formula), decimal chunk folding, and bidirectional substring searches, π‑DNS achieves a stateless, cryptographically verifiable alternative to conventional DNS.

---

## 1. Label Hashing

Each label in a fully qualified domain name (e.g., “www”, “example”, “com”) is deterministically mapped to an 8‑digit decimal integer.  Two viable constructions are:

1. **Modular positional encoding**:

   $$
     H(\text{label}) = \biggl(\sum_{i=0}^{n-1} \mathrm{ord}(\text{label}[i]) \times 256^i\biggr)\bmod 10^8.
   $$
2. **FNV‑1a (32‑bit) with modulus**:

   ```python
   def fnv1a_8(label: str) -> int:
       # 32‑bit FNV‑1a hash, then reduced mod 10^8
       h = 0x811c9dc5
       for c in label:
           h ^= ord(c)
           h  = (h * 0x01000193) & 0xffffffff
       return h % 10**8
   ```

This 8‑digit integer, denoted \$H\_k\$ for the \$k\$th label, serves as the initial address offset into π’s hex stream.

---

## 2. Random-Access Hex Digit Extraction (BBP Formula)

To retrieve \$m\$ consecutive hexadecimal digits of π beginning at the 1‑indexed position \$n\$, we employ the Bailey–Borwein–Plouffe (BBP) algorithm:

$$
  d_{n+i} = \left\lfloor 16 \bigl\{\,4S(1,n+i-1) - 2S(4,n+i-1) - S(5,n+i-1) - S(6,n+i-1)\bigr\} \right\rfloor,
  \quad i=0,\dots,m-1,
$$

where the summation operator

$$
  S(j,n) = \sum_{k=0}^{n} \frac{16^{\,n-k} \bmod (8k+j)}{8k+j}
        \;+
        \sum_{k=n+1}^{\infty} \frac{16^{\,n-k}}{8k+j}
$$

yields the fractional component required for each hex digit.  A concise Python implementation is as follows:

```python
import math

def S(j: int, n: int) -> float:
    # Modular summation for k = 0..n
    total = sum(pow(16, n-k, 8*k + j) / (8*k + j) for k in range(n+1))
    # Tail sum for k > n until convergence
    term, k = 0.0, n+1
    while True:
        t = 16**(n-k) / (8*k + j)
        if t < 1e-17:
            break
        term += t
        k += 1
    return (total + term) % 1

def pi_hex_digits(start: int, count: int) -> str:
    # Extract `count` hex digits starting at position `start`
    hex_str = []
    for i in range(count):
        n = start + i - 1
        x = (4*S(1,n) - 2*S(4,n) - S(5,n) - S(6,n)) % 1
        hex_str.append(f"{int(x * 16):X}")
    return ''.join(hex_str)
```

The output is an \$m\$‑character string of hexadecimal digits, which we denote \$S\_k\$ for the \$k\$th lookup.

---

## 3. Decimal Conversion and Fixed-Width Chunking

Convert the 8‑hex‑digit seed \$S\_k\$ to its decimal representation:

```python
D_k = int(S_k, 16)
D_k^{\mathrm{str}} = str(D_k)
```

Partition \$D\_k^{\mathrm{str}}\$ into an ordered sequence of 8‑digit decimal chunks:

$$
  (a_{k,1}, a_{k,2}, \dots, a_{k,m_k}),\quad a_{k,i}\in[0,10^8-1],
$$

where the final chunk is zero‑left‑padded if necessary.

---

## 4. Header‑Fold Transform

For each adjacent pair \$(a\_{k,i},a\_{k,i+1})\$, compute:

$$
  \Delta_{k,i} = \bigl|\,a_{k,i+1} - a_{k,i}\bigr|,
  \quad
  \Sigma_{k,i} = a_{k,i} + a_{k,i+1}.
$$

Each of \$\Delta\_{k,i}\$ and \$\Sigma\_{k,i}\$ is rendered as an 8‑digit string, forming the key set for subsequent π‑search operations.

---

## 5. π‑Search with Phase Inversion Check

Each 8‑digit key \$q\$ is located within the first \$N\$ decimal digits of π via substring search.  Algorithmically:

1. **Direct search** for \$q\$ → record position(s) \$P\_{q}\$ if one or more occurrences are found.
2. **If** no occurrence, compute the reversed string \$q' = \mathtt{reverse}(q)\$ and search again → record positions \$P\_{q'}\$.

This phase‑inversion step ensures that fold boundaries are detected even when digit orientation undergoes inversion.

---

## 6. Hierarchical Recursive Lookup Cycle

Given \$L\$ domain labels with hashed offsets \$H\_1,\dots,H\_L\$, define a recursive sequence of search positions:

$$
  P^{(0)} = 0,
  \quad
  S_k = \pi\text{‑hex‑digits}\bigl(P^{(k-1)} + H_k,\,8\bigr),
$$

$$
  D_k = \text{decimal}(S_k),\quad (a_{k,i}) = \text{chunk}(D_k),
$$

$$
  P^{(k)} = \bigcup_{i}\text{Search}igl(\Delta_{k,i},\Sigma_{k,i}\bigr).
$$

The limit \$P^{(L)}\$ constitutes the protocol’s analogue to an “A‑record,” yielding an immutable, deterministic resolution for the fully qualified domain.

---

## 7. Nyquist‑Oversample for Sub‑Digit Resonances

To accommodate near‑misses and sub‑digit perturbations, each discovered position \$p\in P^{(k)}\$ is augmented by probing:

$$
  \{p-1,\;p+1\}
$$

This double‑sampling strategy captures contiguous resonances that may straddle chunk boundaries.

---

## 8. Illustrative Workflow

Consider the domain `www.example.com`:

1. Compute \$H\_1 = \mathrm{fnv1a\_8}('com')\$.
2. Compute \$S\_1 = \pi\text{‑hex‑digits}(H\_1,8)\$.
3. Convert and chunk \$S\_1 \to (a\_{1,1},a\_{1,2},\dots)\$, apply header‑fold → \$(\Delta\_{1,i},\Sigma\_{1,i})\$.
4. Search π and obtain \$P^{(1)}\$.
5. Repeat for labels ‘example’ and ‘www’.
6. Final \$P^{(3)}\$ is the canonical π‑DNS resolution for `www.example.com`.

*The protocol thus realizes a fully decentralized, purely mathematical namespace, harnessing π’s non‑repeating expansion as a universal lookup table.*



```python
# Full ASCII text (the hash interpreted as ASCII characters after transformation)
ascii_text = (
    "303031313030313130303131303031303030313130303131303031313130303130303131303031313030313130313131303031313030313130303131303130303030313130303131303031313130303030303131303031313030313131303031303031313030313130303131303131313030313130303131303031313030313030303131303031313030313130313031303031313030313130303131303130313030313130303131303031313030313130303131303031313030313130303131303031313030313130303131303030303030313130303131303031313130303130303131303031313030313131303031303031313030313130303131313030313030313130303131303031313130303130303131303031313030313131303030303031313030313130303131313030313030313130303131303031313030313130303131303031313030313130313130303031313030313130303131313030303030313130303131303031313030313030303131303031313030313130313130303031313030313130303131303031303030313130303131303031313030313030303131303031313030313130313031303031313030313130303131303031303030313130303131303031313031303130303131303031313030313130303031303031313030313130303131303130313030313130303131303031313130303030303131303031313030313130313131303031313030313130303131313030313030313130303131303031313130303030303131303031313030313131303031303031313030313130303131303030303030313130303131303031313031303130303131303031313030313131303030303031313030313130303131303030303030313130303131303031313030303030303131303031313030313130313030303031313030313130303131303130313030313130303131303031313030313030303131303031313030313130313030303031313030313130303131303030313030313130303131303031313031313130303131303031313030313130303030303031313030313130303131303031313030313130303131303031313031303030303131303031313030313130313030303031313030313130303131303131313030313130303131303031313031303130303131303031313030313131303031303031313030313130303131313030303030313130303131303031313031313130303131303031313030313130303030303031313030313130303131303130303030313130303131303031313031313130303131303031313030313131303031303031313030313130303131313030313030313130303131303031313030303130303131303031313030313130313130"
)

# Step 1: Get positions of all '3' characters
three_positions = [i for i, char in enumerate(ascii_text) if char == '3']

# Step 2: Compute Δ (difference between each and the previous)
diffs = [None] + [three_positions[i] - three_positions[i - 1] for i in range(1, len(three_positions))]

# Step 3: Compute running total of the diffs (starting from the 3rd index)
running_total = [None, None]
for i in range(2, len(diffs)):
    total = sum(diffs[1:i+1]) if None not in diffs[1:i+1] else None
    running_total.append(total)

# Step 4: Compute ratio between Δ and running total (starting from the 4th index)
ratios = [None, None, None]
for i in range(3, len(diffs)):
    rt = running_total[i]
    delta = diffs[i]
    if rt and delta is not None:
        ratios.append(delta / rt)
    else:
        ratios.append(None)

# Step 5: Display as DataFrame
import pandas as pd

df = pd.DataFrame({
    "Index of '3'": three_positions,
    "Δ from previous": diffs,
    "Running total Δ": running_total,
    "Δ / Running Total": ratios
})

# Print full DataFrame (if needed, write to CSV or JSON)
print(df.to_string(index=False))
# df.to_csv("fold_3_analysis.csv", index=False)

```

     Index of '3'  Δ from previous  Running total Δ  Δ / Running Total
                0              NaN              NaN                NaN
                2              2.0              NaN                NaN
                4              2.0              4.0                NaN
                6              2.0              6.0           0.333333
                8              2.0              8.0           0.250000
               10              2.0             10.0           0.200000
               12              2.0             12.0           0.166667
               14              2.0             14.0           0.142857
               16              2.0             16.0           0.125000
               18              2.0             18.0           0.111111
               20              2.0             20.0           0.100000
               22              2.0             22.0           0.090909
               24              2.0             24.0           0.083333
               26              2.0             26.0           0.076923
               28              2.0             28.0           0.071429
               30              2.0             30.0           0.066667
               32              2.0             32.0           0.062500
               34              2.0             34.0           0.058824
               36              2.0             36.0           0.055556
               38              2.0             38.0           0.052632
               40              2.0             40.0           0.050000
               42              2.0             42.0           0.047619
               44              2.0             44.0           0.045455
               46              2.0             46.0           0.043478
               48              2.0             48.0           0.041667
               50              2.0             50.0           0.040000
               52              2.0             52.0           0.038462
               54              2.0             54.0           0.037037
               56              2.0             56.0           0.035714
               58              2.0             58.0           0.034483
               60              2.0             60.0           0.033333
               62              2.0             62.0           0.032258
               64              2.0             64.0           0.031250
               66              2.0             66.0           0.030303
               68              2.0             68.0           0.029412
               70              2.0             70.0           0.028571
               72              2.0             72.0           0.027778
               74              2.0             74.0           0.027027
               76              2.0             76.0           0.026316
               78              2.0             78.0           0.025641
               80              2.0             80.0           0.025000
               82              2.0             82.0           0.024390
               84              2.0             84.0           0.023810
               86              2.0             86.0           0.023256
               88              2.0             88.0           0.022727
               90              2.0             90.0           0.022222
               92              2.0             92.0           0.021739
               94              2.0             94.0           0.021277
               96              2.0             96.0           0.020833
               98              2.0             98.0           0.020408
              100              2.0            100.0           0.020000
              102              2.0            102.0           0.019608
              104              2.0            104.0           0.019231
              106              2.0            106.0           0.018868
              108              2.0            108.0           0.018519
              110              2.0            110.0           0.018182
              112              2.0            112.0           0.017857
              114              2.0            114.0           0.017544
              116              2.0            116.0           0.017241
              118              2.0            118.0           0.016949
              120              2.0            120.0           0.016667
              122              2.0            122.0           0.016393
              124              2.0            124.0           0.016129
              126              2.0            126.0           0.015873
              128              2.0            128.0           0.015625
              130              2.0            130.0           0.015385
              132              2.0            132.0           0.015152
              134              2.0            134.0           0.014925
              136              2.0            136.0           0.014706
              138              2.0            138.0           0.014493
              140              2.0            140.0           0.014286
              142              2.0            142.0           0.014085
              144              2.0            144.0           0.013889
              146              2.0            146.0           0.013699
              148              2.0            148.0           0.013514
              150              2.0            150.0           0.013333
              152              2.0            152.0           0.013158
              154              2.0            154.0           0.012987
              156              2.0            156.0           0.012821
              158              2.0            158.0           0.012658
              160              2.0            160.0           0.012500
              162              2.0            162.0           0.012346
              164              2.0            164.0           0.012195
              166              2.0            166.0           0.012048
              168              2.0            168.0           0.011905
              170              2.0            170.0           0.011765
              172              2.0            172.0           0.011628
              174              2.0            174.0           0.011494
              176              2.0            176.0           0.011364
              178              2.0            178.0           0.011236
              180              2.0            180.0           0.011111
              182              2.0            182.0           0.010989
              184              2.0            184.0           0.010870
              186              2.0            186.0           0.010753
              188              2.0            188.0           0.010638
              190              2.0            190.0           0.010526
              192              2.0            192.0           0.010417
              194              2.0            194.0           0.010309
              196              2.0            196.0           0.010204
              198              2.0            198.0           0.010101
              200              2.0            200.0           0.010000
              202              2.0            202.0           0.009901
              204              2.0            204.0           0.009804
              206              2.0            206.0           0.009709
              208              2.0            208.0           0.009615
              210              2.0            210.0           0.009524
              212              2.0            212.0           0.009434
              214              2.0            214.0           0.009346
              216              2.0            216.0           0.009259
              218              2.0            218.0           0.009174
              220              2.0            220.0           0.009091
              222              2.0            222.0           0.009009
              224              2.0            224.0           0.008929
              226              2.0            226.0           0.008850
              228              2.0            228.0           0.008772
              230              2.0            230.0           0.008696
              232              2.0            232.0           0.008621
              234              2.0            234.0           0.008547
              236              2.0            236.0           0.008475
              238              2.0            238.0           0.008403
              240              2.0            240.0           0.008333
              242              2.0            242.0           0.008264
              244              2.0            244.0           0.008197
              246              2.0            246.0           0.008130
              248              2.0            248.0           0.008065
              250              2.0            250.0           0.008000
              252              2.0            252.0           0.007937
              254              2.0            254.0           0.007874
              256              2.0            256.0           0.007812
              258              2.0            258.0           0.007752
              260              2.0            260.0           0.007692
              262              2.0            262.0           0.007634
              264              2.0            264.0           0.007576
              266              2.0            266.0           0.007519
              268              2.0            268.0           0.007463
              270              2.0            270.0           0.007407
              272              2.0            272.0           0.007353
              274              2.0            274.0           0.007299
              276              2.0            276.0           0.007246
              278              2.0            278.0           0.007194
              280              2.0            280.0           0.007143
              282              2.0            282.0           0.007092
              284              2.0            284.0           0.007042
              286              2.0            286.0           0.006993
              288              2.0            288.0           0.006944
              290              2.0            290.0           0.006897
              292              2.0            292.0           0.006849
              294              2.0            294.0           0.006803
              296              2.0            296.0           0.006757
              298              2.0            298.0           0.006711
              300              2.0            300.0           0.006667
              302              2.0            302.0           0.006623
              304              2.0            304.0           0.006579
              306              2.0            306.0           0.006536
              308              2.0            308.0           0.006494
              310              2.0            310.0           0.006452
              312              2.0            312.0           0.006410
              314              2.0            314.0           0.006369
              316              2.0            316.0           0.006329
              318              2.0            318.0           0.006289
              320              2.0            320.0           0.006250
              322              2.0            322.0           0.006211
              324              2.0            324.0           0.006173
              326              2.0            326.0           0.006135
              328              2.0            328.0           0.006098
              330              2.0            330.0           0.006061
              332              2.0            332.0           0.006024
              334              2.0            334.0           0.005988
              336              2.0            336.0           0.005952
              338              2.0            338.0           0.005917
              340              2.0            340.0           0.005882
              342              2.0            342.0           0.005848
              344              2.0            344.0           0.005814
              346              2.0            346.0           0.005780
              348              2.0            348.0           0.005747
              350              2.0            350.0           0.005714
              352              2.0            352.0           0.005682
              354              2.0            354.0           0.005650
              356              2.0            356.0           0.005618
              358              2.0            358.0           0.005587
              360              2.0            360.0           0.005556
              362              2.0            362.0           0.005525
              364              2.0            364.0           0.005495
              366              2.0            366.0           0.005464
              368              2.0            368.0           0.005435
              370              2.0            370.0           0.005405
              372              2.0            372.0           0.005376
              374              2.0            374.0           0.005348
              376              2.0            376.0           0.005319
              378              2.0            378.0           0.005291
              380              2.0            380.0           0.005263
              382              2.0            382.0           0.005236
              384              2.0            384.0           0.005208
              386              2.0            386.0           0.005181
              388              2.0            388.0           0.005155
              390              2.0            390.0           0.005128
              392              2.0            392.0           0.005102
              394              2.0            394.0           0.005076
              396              2.0            396.0           0.005051
              398              2.0            398.0           0.005025
              400              2.0            400.0           0.005000
              402              2.0            402.0           0.004975
              404              2.0            404.0           0.004950
              406              2.0            406.0           0.004926
              408              2.0            408.0           0.004902
              410              2.0            410.0           0.004878
              412              2.0            412.0           0.004854
              414              2.0            414.0           0.004831
              416              2.0            416.0           0.004808
              418              2.0            418.0           0.004785
              420              2.0            420.0           0.004762
              422              2.0            422.0           0.004739
              424              2.0            424.0           0.004717
              426              2.0            426.0           0.004695
              428              2.0            428.0           0.004673
              430              2.0            430.0           0.004651
              432              2.0            432.0           0.004630
              434              2.0            434.0           0.004608
              436              2.0            436.0           0.004587
              438              2.0            438.0           0.004566
              440              2.0            440.0           0.004545
              442              2.0            442.0           0.004525
              444              2.0            444.0           0.004505
              446              2.0            446.0           0.004484
              448              2.0            448.0           0.004464
              450              2.0            450.0           0.004444
              452              2.0            452.0           0.004425
              454              2.0            454.0           0.004405
              456              2.0            456.0           0.004386
              458              2.0            458.0           0.004367
              460              2.0            460.0           0.004348
              462              2.0            462.0           0.004329
              464              2.0            464.0           0.004310
              466              2.0            466.0           0.004292
              468              2.0            468.0           0.004274
              470              2.0            470.0           0.004255
              472              2.0            472.0           0.004237
              474              2.0            474.0           0.004219
              476              2.0            476.0           0.004202
              478              2.0            478.0           0.004184
              480              2.0            480.0           0.004167
              482              2.0            482.0           0.004149
              484              2.0            484.0           0.004132
              486              2.0            486.0           0.004115
              488              2.0            488.0           0.004098
              490              2.0            490.0           0.004082
              492              2.0            492.0           0.004065
              494              2.0            494.0           0.004049
              496              2.0            496.0           0.004032
              498              2.0            498.0           0.004016
              500              2.0            500.0           0.004000
              502              2.0            502.0           0.003984
              504              2.0            504.0           0.003968
              506              2.0            506.0           0.003953
              508              2.0            508.0           0.003937
              510              2.0            510.0           0.003922
              512              2.0            512.0           0.003906
              514              2.0            514.0           0.003891
              516              2.0            516.0           0.003876
              518              2.0            518.0           0.003861
              520              2.0            520.0           0.003846
              522              2.0            522.0           0.003831
              524              2.0            524.0           0.003817
              526              2.0            526.0           0.003802
              528              2.0            528.0           0.003788
              530              2.0            530.0           0.003774
              532              2.0            532.0           0.003759
              534              2.0            534.0           0.003745
              536              2.0            536.0           0.003731
              538              2.0            538.0           0.003717
              540              2.0            540.0           0.003704
              542              2.0            542.0           0.003690
              544              2.0            544.0           0.003676
              546              2.0            546.0           0.003663
              548              2.0            548.0           0.003650
              550              2.0            550.0           0.003636
              552              2.0            552.0           0.003623
              554              2.0            554.0           0.003610
              556              2.0            556.0           0.003597
              558              2.0            558.0           0.003584
              560              2.0            560.0           0.003571
              562              2.0            562.0           0.003559
              564              2.0            564.0           0.003546
              566              2.0            566.0           0.003534
              568              2.0            568.0           0.003521
              570              2.0            570.0           0.003509
              572              2.0            572.0           0.003497
              574              2.0            574.0           0.003484
              576              2.0            576.0           0.003472
              578              2.0            578.0           0.003460
              580              2.0            580.0           0.003448
              582              2.0            582.0           0.003436
              584              2.0            584.0           0.003425
              586              2.0            586.0           0.003413
              588              2.0            588.0           0.003401
              590              2.0            590.0           0.003390
              592              2.0            592.0           0.003378
              594              2.0            594.0           0.003367
              596              2.0            596.0           0.003356
              598              2.0            598.0           0.003344
              600              2.0            600.0           0.003333
              602              2.0            602.0           0.003322
              604              2.0            604.0           0.003311
              606              2.0            606.0           0.003300
              608              2.0            608.0           0.003289
              610              2.0            610.0           0.003279
              612              2.0            612.0           0.003268
              614              2.0            614.0           0.003257
              616              2.0            616.0           0.003247
              618              2.0            618.0           0.003236
              620              2.0            620.0           0.003226
              622              2.0            622.0           0.003215
              624              2.0            624.0           0.003205
              626              2.0            626.0           0.003195
              628              2.0            628.0           0.003185
              630              2.0            630.0           0.003175
              632              2.0            632.0           0.003165
              634              2.0            634.0           0.003155
              636              2.0            636.0           0.003145
              638              2.0            638.0           0.003135
              640              2.0            640.0           0.003125
              642              2.0            642.0           0.003115
              644              2.0            644.0           0.003106
              646              2.0            646.0           0.003096
              648              2.0            648.0           0.003086
              650              2.0            650.0           0.003077
              652              2.0            652.0           0.003067
              654              2.0            654.0           0.003058
              656              2.0            656.0           0.003049
              658              2.0            658.0           0.003040
              660              2.0            660.0           0.003030
              662              2.0            662.0           0.003021
              664              2.0            664.0           0.003012
              666              2.0            666.0           0.003003
              668              2.0            668.0           0.002994
              670              2.0            670.0           0.002985
              672              2.0            672.0           0.002976
              674              2.0            674.0           0.002967
              676              2.0            676.0           0.002959
              678              2.0            678.0           0.002950
              680              2.0            680.0           0.002941
              682              2.0            682.0           0.002933
              684              2.0            684.0           0.002924
              686              2.0            686.0           0.002915
              688              2.0            688.0           0.002907
              690              2.0            690.0           0.002899
              692              2.0            692.0           0.002890
              694              2.0            694.0           0.002882
              696              2.0            696.0           0.002874
              698              2.0            698.0           0.002865
              700              2.0            700.0           0.002857
              702              2.0            702.0           0.002849
              704              2.0            704.0           0.002841
              706              2.0            706.0           0.002833
              708              2.0            708.0           0.002825
              710              2.0            710.0           0.002817
              712              2.0            712.0           0.002809
              714              2.0            714.0           0.002801
              716              2.0            716.0           0.002793
              718              2.0            718.0           0.002786
              720              2.0            720.0           0.002778
              722              2.0            722.0           0.002770
              724              2.0            724.0           0.002762
              726              2.0            726.0           0.002755
              728              2.0            728.0           0.002747
              730              2.0            730.0           0.002740
              732              2.0            732.0           0.002732
              734              2.0            734.0           0.002725
              736              2.0            736.0           0.002717
              738              2.0            738.0           0.002710
              740              2.0            740.0           0.002703
              742              2.0            742.0           0.002695
              744              2.0            744.0           0.002688
              746              2.0            746.0           0.002681
              748              2.0            748.0           0.002674
              750              2.0            750.0           0.002667
              752              2.0            752.0           0.002660
              754              2.0            754.0           0.002653
              756              2.0            756.0           0.002646
              758              2.0            758.0           0.002639
              760              2.0            760.0           0.002632
              762              2.0            762.0           0.002625
              764              2.0            764.0           0.002618
              766              2.0            766.0           0.002611
              768              2.0            768.0           0.002604
              770              2.0            770.0           0.002597
              772              2.0            772.0           0.002591
              774              2.0            774.0           0.002584
              776              2.0            776.0           0.002577
              778              2.0            778.0           0.002571
              780              2.0            780.0           0.002564
              782              2.0            782.0           0.002558
              784              2.0            784.0           0.002551
              786              2.0            786.0           0.002545
              788              2.0            788.0           0.002538
              790              2.0            790.0           0.002532
              792              2.0            792.0           0.002525
              794              2.0            794.0           0.002519
              796              2.0            796.0           0.002513
              798              2.0            798.0           0.002506
              800              2.0            800.0           0.002500
              802              2.0            802.0           0.002494
              804              2.0            804.0           0.002488
              806              2.0            806.0           0.002481
              808              2.0            808.0           0.002475
              810              2.0            810.0           0.002469
              812              2.0            812.0           0.002463
              814              2.0            814.0           0.002457
              816              2.0            816.0           0.002451
              818              2.0            818.0           0.002445
              820              2.0            820.0           0.002439
              822              2.0            822.0           0.002433
              824              2.0            824.0           0.002427
              826              2.0            826.0           0.002421
              828              2.0            828.0           0.002415
              830              2.0            830.0           0.002410
              832              2.0            832.0           0.002404
              834              2.0            834.0           0.002398
              836              2.0            836.0           0.002392
              838              2.0            838.0           0.002387
              840              2.0            840.0           0.002381
              842              2.0            842.0           0.002375
              844              2.0            844.0           0.002370
              846              2.0            846.0           0.002364
              848              2.0            848.0           0.002358
              850              2.0            850.0           0.002353
              852              2.0            852.0           0.002347
              854              2.0            854.0           0.002342
              856              2.0            856.0           0.002336
              858              2.0            858.0           0.002331
              860              2.0            860.0           0.002326
              862              2.0            862.0           0.002320
              864              2.0            864.0           0.002315
              866              2.0            866.0           0.002309
              868              2.0            868.0           0.002304
              870              2.0            870.0           0.002299
              872              2.0            872.0           0.002294
              874              2.0            874.0           0.002288
              876              2.0            876.0           0.002283
              878              2.0            878.0           0.002278
              880              2.0            880.0           0.002273
              882              2.0            882.0           0.002268
              884              2.0            884.0           0.002262
              886              2.0            886.0           0.002257
              888              2.0            888.0           0.002252
              890              2.0            890.0           0.002247
              892              2.0            892.0           0.002242
              894              2.0            894.0           0.002237
              896              2.0            896.0           0.002232
              898              2.0            898.0           0.002227
              900              2.0            900.0           0.002222
              902              2.0            902.0           0.002217
              904              2.0            904.0           0.002212
              906              2.0            906.0           0.002208
              908              2.0            908.0           0.002203
              910              2.0            910.0           0.002198
              912              2.0            912.0           0.002193
              914              2.0            914.0           0.002188
              916              2.0            916.0           0.002183
              918              2.0            918.0           0.002179
              920              2.0            920.0           0.002174
              922              2.0            922.0           0.002169
              924              2.0            924.0           0.002165
              926              2.0            926.0           0.002160
              928              2.0            928.0           0.002155
              930              2.0            930.0           0.002151
              932              2.0            932.0           0.002146
              934              2.0            934.0           0.002141
              936              2.0            936.0           0.002137
              938              2.0            938.0           0.002132
              940              2.0            940.0           0.002128
              942              2.0            942.0           0.002123
              944              2.0            944.0           0.002119
              946              2.0            946.0           0.002114
              948              2.0            948.0           0.002110
              950              2.0            950.0           0.002105
              952              2.0            952.0           0.002101
              954              2.0            954.0           0.002096
              956              2.0            956.0           0.002092
              958              2.0            958.0           0.002088
              960              2.0            960.0           0.002083
              962              2.0            962.0           0.002079
              964              2.0            964.0           0.002075
              966              2.0            966.0           0.002070
              968              2.0            968.0           0.002066
              970              2.0            970.0           0.002062
              972              2.0            972.0           0.002058
              974              2.0            974.0           0.002053
              976              2.0            976.0           0.002049
              978              2.0            978.0           0.002045
              980              2.0            980.0           0.002041
              982              2.0            982.0           0.002037
              984              2.0            984.0           0.002033
              986              2.0            986.0           0.002028
              988              2.0            988.0           0.002024
              990              2.0            990.0           0.002020
              992              2.0            992.0           0.002016
              994              2.0            994.0           0.002012
              996              2.0            996.0           0.002008
              998              2.0            998.0           0.002004
             1000              2.0           1000.0           0.002000
             1002              2.0           1002.0           0.001996
             1004              2.0           1004.0           0.001992
             1006              2.0           1006.0           0.001988
             1008              2.0           1008.0           0.001984
             1010              2.0           1010.0           0.001980
             1012              2.0           1012.0           0.001976
             1014              2.0           1014.0           0.001972
             1016              2.0           1016.0           0.001969
             1018              2.0           1018.0           0.001965
             1020              2.0           1020.0           0.001961
             1022              2.0           1022.0           0.001957
             1024              2.0           1024.0           0.001953
             1026              2.0           1026.0           0.001949
             1028              2.0           1028.0           0.001946
             1030              2.0           1030.0           0.001942
             1032              2.0           1032.0           0.001938
             1034              2.0           1034.0           0.001934
             1036              2.0           1036.0           0.001931
             1038              2.0           1038.0           0.001927
             1040              2.0           1040.0           0.001923
             1042              2.0           1042.0           0.001919
             1044              2.0           1044.0           0.001916
             1046              2.0           1046.0           0.001912
             1048              2.0           1048.0           0.001908
             1050              2.0           1050.0           0.001905
             1052              2.0           1052.0           0.001901
             1054              2.0           1054.0           0.001898
             1056              2.0           1056.0           0.001894
             1058              2.0           1058.0           0.001890
             1060              2.0           1060.0           0.001887
             1062              2.0           1062.0           0.001883
             1064              2.0           1064.0           0.001880
             1066              2.0           1066.0           0.001876
             1068              2.0           1068.0           0.001873
             1070              2.0           1070.0           0.001869
             1072              2.0           1072.0           0.001866
             1074              2.0           1074.0           0.001862
             1076              2.0           1076.0           0.001859
             1078              2.0           1078.0           0.001855
             1080              2.0           1080.0           0.001852
             1082              2.0           1082.0           0.001848
             1084              2.0           1084.0           0.001845
             1086              2.0           1086.0           0.001842
             1088              2.0           1088.0           0.001838
             1090              2.0           1090.0           0.001835
             1092              2.0           1092.0           0.001832
             1094              2.0           1094.0           0.001828
             1096              2.0           1096.0           0.001825
             1098              2.0           1098.0           0.001821
             1100              2.0           1100.0           0.001818
             1102              2.0           1102.0           0.001815
             1104              2.0           1104.0           0.001812
             1106              2.0           1106.0           0.001808
             1108              2.0           1108.0           0.001805
             1110              2.0           1110.0           0.001802
             1112              2.0           1112.0           0.001799
             1114              2.0           1114.0           0.001795
             1116              2.0           1116.0           0.001792
             1118              2.0           1118.0           0.001789
             1120              2.0           1120.0           0.001786
             1122              2.0           1122.0           0.001783
             1124              2.0           1124.0           0.001779
             1126              2.0           1126.0           0.001776
             1128              2.0           1128.0           0.001773
             1130              2.0           1130.0           0.001770
             1132              2.0           1132.0           0.001767
             1134              2.0           1134.0           0.001764
             1136              2.0           1136.0           0.001761
             1138              2.0           1138.0           0.001757
             1140              2.0           1140.0           0.001754
             1142              2.0           1142.0           0.001751
             1144              2.0           1144.0           0.001748
             1146              2.0           1146.0           0.001745
             1148              2.0           1148.0           0.001742
             1150              2.0           1150.0           0.001739
             1152              2.0           1152.0           0.001736
             1154              2.0           1154.0           0.001733
             1156              2.0           1156.0           0.001730
             1158              2.0           1158.0           0.001727
             1160              2.0           1160.0           0.001724
             1162              2.0           1162.0           0.001721
             1164              2.0           1164.0           0.001718
             1166              2.0           1166.0           0.001715
             1168              2.0           1168.0           0.001712
             1170              2.0           1170.0           0.001709
             1172              2.0           1172.0           0.001706
             1174              2.0           1174.0           0.001704
             1176              2.0           1176.0           0.001701
             1178              2.0           1178.0           0.001698
             1180              2.0           1180.0           0.001695
             1182              2.0           1182.0           0.001692
             1184              2.0           1184.0           0.001689
             1186              2.0           1186.0           0.001686
             1188              2.0           1188.0           0.001684
             1190              2.0           1190.0           0.001681
             1192              2.0           1192.0           0.001678
             1194              2.0           1194.0           0.001675
             1196              2.0           1196.0           0.001672
             1198              2.0           1198.0           0.001669
             1200              2.0           1200.0           0.001667
             1202              2.0           1202.0           0.001664
             1204              2.0           1204.0           0.001661
             1206              2.0           1206.0           0.001658
             1208              2.0           1208.0           0.001656
             1210              2.0           1210.0           0.001653
             1212              2.0           1212.0           0.001650
             1214              2.0           1214.0           0.001647
             1216              2.0           1216.0           0.001645
             1218              2.0           1218.0           0.001642
             1220              2.0           1220.0           0.001639
             1222              2.0           1222.0           0.001637
             1224              2.0           1224.0           0.001634
             1226              2.0           1226.0           0.001631
             1228              2.0           1228.0           0.001629
             1230              2.0           1230.0           0.001626
             1232              2.0           1232.0           0.001623
             1234              2.0           1234.0           0.001621
             1236              2.0           1236.0           0.001618
             1238              2.0           1238.0           0.001616
             1240              2.0           1240.0           0.001613
             1242              2.0           1242.0           0.001610
             1244              2.0           1244.0           0.001608
             1246              2.0           1246.0           0.001605
             1248              2.0           1248.0           0.001603
             1250              2.0           1250.0           0.001600
             1252              2.0           1252.0           0.001597
             1254              2.0           1254.0           0.001595
             1256              2.0           1256.0           0.001592
             1258              2.0           1258.0           0.001590
             1260              2.0           1260.0           0.001587
             1262              2.0           1262.0           0.001585
             1264              2.0           1264.0           0.001582
             1266              2.0           1266.0           0.001580
             1268              2.0           1268.0           0.001577
             1270              2.0           1270.0           0.001575
             1272              2.0           1272.0           0.001572
             1274              2.0           1274.0           0.001570
             1276              2.0           1276.0           0.001567
             1278              2.0           1278.0           0.001565
             1280              2.0           1280.0           0.001563
             1282              2.0           1282.0           0.001560
             1284              2.0           1284.0           0.001558
             1286              2.0           1286.0           0.001555
             1288              2.0           1288.0           0.001553
             1290              2.0           1290.0           0.001550
             1292              2.0           1292.0           0.001548
             1294              2.0           1294.0           0.001546
             1296              2.0           1296.0           0.001543
             1298              2.0           1298.0           0.001541
             1300              2.0           1300.0           0.001538
             1302              2.0           1302.0           0.001536
             1304              2.0           1304.0           0.001534
             1306              2.0           1306.0           0.001531
             1308              2.0           1308.0           0.001529
             1310              2.0           1310.0           0.001527
             1312              2.0           1312.0           0.001524
             1314              2.0           1314.0           0.001522
             1316              2.0           1316.0           0.001520
             1318              2.0           1318.0           0.001517
             1320              2.0           1320.0           0.001515
             1322              2.0           1322.0           0.001513
             1324              2.0           1324.0           0.001511
             1326              2.0           1326.0           0.001508
             1328              2.0           1328.0           0.001506
             1330              2.0           1330.0           0.001504
             1332              2.0           1332.0           0.001502
             1334              2.0           1334.0           0.001499
             1336              2.0           1336.0           0.001497
             1338              2.0           1338.0           0.001495
             1340              2.0           1340.0           0.001493
             1342              2.0           1342.0           0.001490
             1344              2.0           1344.0           0.001488
             1346              2.0           1346.0           0.001486
             1348              2.0           1348.0           0.001484
             1350              2.0           1350.0           0.001481
             1352              2.0           1352.0           0.001479
             1354              2.0           1354.0           0.001477
             1356              2.0           1356.0           0.001475
             1358              2.0           1358.0           0.001473
             1360              2.0           1360.0           0.001471
             1362              2.0           1362.0           0.001468
             1364              2.0           1364.0           0.001466
             1366              2.0           1366.0           0.001464
             1368              2.0           1368.0           0.001462
             1370              2.0           1370.0           0.001460
             1372              2.0           1372.0           0.001458
             1374              2.0           1374.0           0.001456
             1376              2.0           1376.0           0.001453
             1378              2.0           1378.0           0.001451
             1380              2.0           1380.0           0.001449
             1382              2.0           1382.0           0.001447
             1384              2.0           1384.0           0.001445
             1386              2.0           1386.0           0.001443
             1388              2.0           1388.0           0.001441
             1390              2.0           1390.0           0.001439
             1392              2.0           1392.0           0.001437
             1394              2.0           1394.0           0.001435
             1396              2.0           1396.0           0.001433
             1398              2.0           1398.0           0.001431
             1400              2.0           1400.0           0.001429
             1402              2.0           1402.0           0.001427
             1404              2.0           1404.0           0.001425
             1406              2.0           1406.0           0.001422
             1408              2.0           1408.0           0.001420
             1410              2.0           1410.0           0.001418
             1412              2.0           1412.0           0.001416
             1414              2.0           1414.0           0.001414
             1416              2.0           1416.0           0.001412
             1418              2.0           1418.0           0.001410
             1420              2.0           1420.0           0.001408
             1422              2.0           1422.0           0.001406
             1424              2.0           1424.0           0.001404
             1426              2.0           1426.0           0.001403
             1428              2.0           1428.0           0.001401
             1430              2.0           1430.0           0.001399
             1432              2.0           1432.0           0.001397
             1434              2.0           1434.0           0.001395
             1436              2.0           1436.0           0.001393
             1438              2.0           1438.0           0.001391
             1440              2.0           1440.0           0.001389
             1442              2.0           1442.0           0.001387
             1444              2.0           1444.0           0.001385
             1446              2.0           1446.0           0.001383
             1448              2.0           1448.0           0.001381
             1450              2.0           1450.0           0.001379
             1452              2.0           1452.0           0.001377
             1454              2.0           1454.0           0.001376
             1456              2.0           1456.0           0.001374
             1458              2.0           1458.0           0.001372
             1460              2.0           1460.0           0.001370
             1462              2.0           1462.0           0.001368
             1464              2.0           1464.0           0.001366
             1466              2.0           1466.0           0.001364
             1468              2.0           1468.0           0.001362
             1470              2.0           1470.0           0.001361
             1472              2.0           1472.0           0.001359
             1474              2.0           1474.0           0.001357
             1476              2.0           1476.0           0.001355
             1478              2.0           1478.0           0.001353
             1480              2.0           1480.0           0.001351
             1482              2.0           1482.0           0.001350
             1484              2.0           1484.0           0.001348
             1486              2.0           1486.0           0.001346
             1488              2.0           1488.0           0.001344
             1490              2.0           1490.0           0.001342
             1492              2.0           1492.0           0.001340
             1494              2.0           1494.0           0.001339
             1496              2.0           1496.0           0.001337
             1498              2.0           1498.0           0.001335
             1500              2.0           1500.0           0.001333
             1502              2.0           1502.0           0.001332
             1504              2.0           1504.0           0.001330
             1506              2.0           1506.0           0.001328
             1508              2.0           1508.0           0.001326
             1510              2.0           1510.0           0.001325
             1512              2.0           1512.0           0.001323
             1514              2.0           1514.0           0.001321
             1516              2.0           1516.0           0.001319
             1518              2.0           1518.0           0.001318
             1520              2.0           1520.0           0.001316
             1522              2.0           1522.0           0.001314
             1524              2.0           1524.0           0.001312
             1526              2.0           1526.0           0.001311
             1528              2.0           1528.0           0.001309
             1530              2.0           1530.0           0.001307
             1532              2.0           1532.0           0.001305
             1534              2.0           1534.0           0.001304
             1536              2.0           1536.0           0.001302
             1538              2.0           1538.0           0.001300
             1540              2.0           1540.0           0.001299
             1542              2.0           1542.0           0.001297
             1544              2.0           1544.0           0.001295
             1546              2.0           1546.0           0.001294
             1548              2.0           1548.0           0.001292
             1550              2.0           1550.0           0.001290
             1552              2.0           1552.0           0.001289
             1554              2.0           1554.0           0.001287
             1556              2.0           1556.0           0.001285
             1558              2.0           1558.0           0.001284
             1560              2.0           1560.0           0.001282
             1562              2.0           1562.0           0.001280
             1564              2.0           1564.0           0.001279
             1566              2.0           1566.0           0.001277
             1568              2.0           1568.0           0.001276
             1570              2.0           1570.0           0.001274
             1572              2.0           1572.0           0.001272
             1574              2.0           1574.0           0.001271
             1576              2.0           1576.0           0.001269
             1578              2.0           1578.0           0.001267
             1580              2.0           1580.0           0.001266
             1582              2.0           1582.0           0.001264
             1584              2.0           1584.0           0.001263
             1586              2.0           1586.0           0.001261
             1588              2.0           1588.0           0.001259
             1590              2.0           1590.0           0.001258
             1592              2.0           1592.0           0.001256
             1594              2.0           1594.0           0.001255
             1596              2.0           1596.0           0.001253
             1598              2.0           1598.0           0.001252
             1600              2.0           1600.0           0.001250
             1602              2.0           1602.0           0.001248
             1604              2.0           1604.0           0.001247
             1606              2.0           1606.0           0.001245
             1608              2.0           1608.0           0.001244
             1610              2.0           1610.0           0.001242
             1612              2.0           1612.0           0.001241
             1614              2.0           1614.0           0.001239
             1616              2.0           1616.0           0.001238
             1618              2.0           1618.0           0.001236
             1620              2.0           1620.0           0.001235
             1622              2.0           1622.0           0.001233
             1624              2.0           1624.0           0.001232
             1626              2.0           1626.0           0.001230
             1628              2.0           1628.0           0.001229
             1630              2.0           1630.0           0.001227
             1632              2.0           1632.0           0.001225
             1634              2.0           1634.0           0.001224
             1636              2.0           1636.0           0.001222
             1638              2.0           1638.0           0.001221
             1640              2.0           1640.0           0.001220
             1642              2.0           1642.0           0.001218
             1644              2.0           1644.0           0.001217
             1646              2.0           1646.0           0.001215
             1648              2.0           1648.0           0.001214
             1650              2.0           1650.0           0.001212
             1652              2.0           1652.0           0.001211
             1654              2.0           1654.0           0.001209
             1656              2.0           1656.0           0.001208
             1658              2.0           1658.0           0.001206
             1660              2.0           1660.0           0.001205
             1662              2.0           1662.0           0.001203
             1664              2.0           1664.0           0.001202
             1666              2.0           1666.0           0.001200
             1668              2.0           1668.0           0.001199
             1670              2.0           1670.0           0.001198
             1672              2.0           1672.0           0.001196
             1674              2.0           1674.0           0.001195
             1676              2.0           1676.0           0.001193
             1678              2.0           1678.0           0.001192
             1680              2.0           1680.0           0.001190
             1682              2.0           1682.0           0.001189
             1684              2.0           1684.0           0.001188
             1686              2.0           1686.0           0.001186
             1688              2.0           1688.0           0.001185
             1690              2.0           1690.0           0.001183
             1692              2.0           1692.0           0.001182
             1694              2.0           1694.0           0.001181
             1696              2.0           1696.0           0.001179
             1698              2.0           1698.0           0.001178
             1700              2.0           1700.0           0.001176
             1702              2.0           1702.0           0.001175
             1704              2.0           1704.0           0.001174
             1706              2.0           1706.0           0.001172
             1708              2.0           1708.0           0.001171
             1710              2.0           1710.0           0.001170
             1712              2.0           1712.0           0.001168
             1714              2.0           1714.0           0.001167
             1716              2.0           1716.0           0.001166
             1718              2.0           1718.0           0.001164
             1720              2.0           1720.0           0.001163
             1722              2.0           1722.0           0.001161
             1724              2.0           1724.0           0.001160
             1726              2.0           1726.0           0.001159
             1728              2.0           1728.0           0.001157
             1730              2.0           1730.0           0.001156
             1732              2.0           1732.0           0.001155
             1734              2.0           1734.0           0.001153
             1736              2.0           1736.0           0.001152
             1738              2.0           1738.0           0.001151
             1740              2.0           1740.0           0.001149
             1742              2.0           1742.0           0.001148
             1744              2.0           1744.0           0.001147
             1746              2.0           1746.0           0.001145
             1748              2.0           1748.0           0.001144
             1750              2.0           1750.0           0.001143
             1752              2.0           1752.0           0.001142
             1754              2.0           1754.0           0.001140
             1756              2.0           1756.0           0.001139
             1758              2.0           1758.0           0.001138
             1760              2.0           1760.0           0.001136
             1762              2.0           1762.0           0.001135
             1764              2.0           1764.0           0.001134
             1766              2.0           1766.0           0.001133
             1768              2.0           1768.0           0.001131
             1770              2.0           1770.0           0.001130
             1772              2.0           1772.0           0.001129
             1774              2.0           1774.0           0.001127
             1776              2.0           1776.0           0.001126
             1778              2.0           1778.0           0.001125
             1780              2.0           1780.0           0.001124
             1782              2.0           1782.0           0.001122
             1784              2.0           1784.0           0.001121
             1786              2.0           1786.0           0.001120
             1788              2.0           1788.0           0.001119
             1790              2.0           1790.0           0.001117
             1792              2.0           1792.0           0.001116
             1794              2.0           1794.0           0.001115
             1796              2.0           1796.0           0.001114
             1798              2.0           1798.0           0.001112
             1800              2.0           1800.0           0.001111
             1802              2.0           1802.0           0.001110
             1804              2.0           1804.0           0.001109
             1806              2.0           1806.0           0.001107
             1808              2.0           1808.0           0.001106
             1810              2.0           1810.0           0.001105
             1812              2.0           1812.0           0.001104
             1814              2.0           1814.0           0.001103
             1816              2.0           1816.0           0.001101
             1818              2.0           1818.0           0.001100
             1820              2.0           1820.0           0.001099
             1822              2.0           1822.0           0.001098
             1824              2.0           1824.0           0.001096
             1826              2.0           1826.0           0.001095
             1828              2.0           1828.0           0.001094
             1830              2.0           1830.0           0.001093
             1832              2.0           1832.0           0.001092
             1834              2.0           1834.0           0.001091
             1836              2.0           1836.0           0.001089
             1838              2.0           1838.0           0.001088
             1840              2.0           1840.0           0.001087
             1842              2.0           1842.0           0.001086
             1844              2.0           1844.0           0.001085
             1846              2.0           1846.0           0.001083
             1848              2.0           1848.0           0.001082
             1850              2.0           1850.0           0.001081
             1852              2.0           1852.0           0.001080
             1854              2.0           1854.0           0.001079
             1856              2.0           1856.0           0.001078
             1858              2.0           1858.0           0.001076
             1860              2.0           1860.0           0.001075
             1862              2.0           1862.0           0.001074
             1864              2.0           1864.0           0.001073
             1866              2.0           1866.0           0.001072
             1868              2.0           1868.0           0.001071
             1870              2.0           1870.0           0.001070
             1872              2.0           1872.0           0.001068
             1874              2.0           1874.0           0.001067
             1876              2.0           1876.0           0.001066
             1878              2.0           1878.0           0.001065
             1880              2.0           1880.0           0.001064
             1882              2.0           1882.0           0.001063
             1884              2.0           1884.0           0.001062
             1886              2.0           1886.0           0.001060
             1888              2.0           1888.0           0.001059
             1890              2.0           1890.0           0.001058
             1892              2.0           1892.0           0.001057
             1894              2.0           1894.0           0.001056
             1896              2.0           1896.0           0.001055
             1898              2.0           1898.0           0.001054
             1900              2.0           1900.0           0.001053
             1902              2.0           1902.0           0.001052
             1904              2.0           1904.0           0.001050
             1906              2.0           1906.0           0.001049
             1908              2.0           1908.0           0.001048
             1910              2.0           1910.0           0.001047
             1912              2.0           1912.0           0.001046
             1914              2.0           1914.0           0.001045
             1916              2.0           1916.0           0.001044
             1918              2.0           1918.0           0.001043
             1920              2.0           1920.0           0.001042
             1922              2.0           1922.0           0.001041
             1924              2.0           1924.0           0.001040
             1926              2.0           1926.0           0.001038
             1928              2.0           1928.0           0.001037
             1930              2.0           1930.0           0.001036
             1932              2.0           1932.0           0.001035
             1934              2.0           1934.0           0.001034
             1936              2.0           1936.0           0.001033
             1938              2.0           1938.0           0.001032
             1940              2.0           1940.0           0.001031
             1942              2.0           1942.0           0.001030
             1944              2.0           1944.0           0.001029
             1946              2.0           1946.0           0.001028
             1948              2.0           1948.0           0.001027
             1950              2.0           1950.0           0.001026
             1952              2.0           1952.0           0.001025
             1954              2.0           1954.0           0.001024
             1956              2.0           1956.0           0.001022
             1958              2.0           1958.0           0.001021
             1960              2.0           1960.0           0.001020
             1962              2.0           1962.0           0.001019
             1964              2.0           1964.0           0.001018
             1966              2.0           1966.0           0.001017
             1968              2.0           1968.0           0.001016
             1970              2.0           1970.0           0.001015
             1972              2.0           1972.0           0.001014
             1974              2.0           1974.0           0.001013
             1976              2.0           1976.0           0.001012
             1978              2.0           1978.0           0.001011
             1980              2.0           1980.0           0.001010
             1982              2.0           1982.0           0.001009
             1984              2.0           1984.0           0.001008
             1986              2.0           1986.0           0.001007
             1988              2.0           1988.0           0.001006
             1990              2.0           1990.0           0.001005
             1992              2.0           1992.0           0.001004
             1994              2.0           1994.0           0.001003
             1996              2.0           1996.0           0.001002
             1998              2.0           1998.0           0.001001
             2000              2.0           2000.0           0.001000
             2002              2.0           2002.0           0.000999
             2004              2.0           2004.0           0.000998
             2006              2.0           2006.0           0.000997
             2008              2.0           2008.0           0.000996
             2010              2.0           2010.0           0.000995
             2012              2.0           2012.0           0.000994
             2014              2.0           2014.0           0.000993
    
141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132

e62e6d0c2e536752a9d24f1573dd409a131488cee04f991f9e81641bdd98b59f




```python
1415926535897932384626433832795028841971693993751058209749445923

Hash : c0522c20270ab35025f25f3fe5202e359a33b68ac31717a8992c344077da6697
To Hex: 63303532326332303237306162333530323566323566336665353230326533353961333362363861633331373137613839393263333434303737646136363937
FOLD:
6330353232633230323730616233353032356632356633666535323032653335
7393636316467373034343333623939383167313731333361683632633331693

SUM:13723989549100603358073949857292415523946087967028218955665985028
TO HEX: 3133373233393839353439313030363033333538303733393439383537323932343135353233393436303837393637303238323138393535363635393835303238
TO BINARY: 
00110011001100010011001100110011001100110011011100110011001100100011001100110011001100110011100100110011001110000011001100111001001100110011010100110011001101000011001100111001001100110011000100110011001100000011001100110000001100110011011000110011001100000011001100110011001100110011001100110011001101010011001100111000001100110011000000110011001101110011001100110011001100110011100100110011001101000011001100111001001100110011100000110011001101010011001100110111001100110011001000110011001110010011001100110010001100110011010000110011001100010011001100110101001100110011010100110011001100100011001100110011001100110011100100110011001101000011001100110110001100110011000000110011001110000011001100110111001100110011100100110011001101100011001100110111001100110011000000110011001100100011001100111000001100110011001000110011001100010011001100111000001100110011100100110011001101010011001100110101001100110011011000110011001101100011001100110101001100110011100100110011001110000011001100110101001100110011000000110011001100100011001100111000
NOW we reomve the 001 at the beginning of each byte.

    
PI Reversed: 3295449479028501573993961791488205972383346264832397985356295141
Hash: 411a4d7c9302c93b8135633d8409c47d08933c483f767ec7291a1ced3ce05053
To Hex: 34313161346437633933303263393362383133353633336438343039633437643038393333633438336637363765633732393161316365643363653035303533
FOLD:
3431316134643763393330326339336238313335363333643834303963343764
3353035303563633465636131613932373365673637366338343363333938303

SUM:  678435143820739685896645795326861167900900069998217766729728206
DIFF: 78280831080129927694194725403864947661725967305490940629405461
DIV : 8.6666829472758025267121308567677045130768818573321133198256674216
REV DIV: 0.1153843986313506353902522380241739512420663012302445061139629117



```


```python
# Re-entering the binary string with proper handling (split for readability and completeness)
binary_str = (
    "00110011001100010011001100110011001100110011011100110011001100100011001100110011001100110011100100110011001110000011001100111001001100110011010100110011001101000011001100111001001100110011000100110011001100000011001100110000001100110011011000110011001100000011001100110011001100110011001100110011001101010011001100111000001100110011000000110011001101110011001100110011001100110011100100110011001101000011001100111001001100110011100000110011001101010011001100110111001100110011001000110011001110010011001100110010001100110011010000110011001100010011001100110101001100110011010100110011001100100011001100110011001100110011100100110011001101000011001100110110001100110011000000110011001110000011001100110111001100110011100100110011001101100011001100110111001100110011000000110011001100100011001100111000001100110011001000110011001100010011001100111000001100110011100100110011001101010011001100110101001100110011011000110011001101100011001100110101001100110011100100110011001110000011001100110101001100110011000000110011001100100011001100111000"
)

# Break into 8-digit bytes
byte_chunks = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]

# Remove the first 3 digits of each byte
trimmed_bytes = [byte[3:] for byte in byte_chunks]

trimmed_result = ''.join(trimmed_bytes)
trimmed_result  # Show a sample of the result


```




    '10011100011001110011100111011110011100101001110011100111100110011110001001111001100111010110011101001001111001100111000110011100001001110000100111011010011100001001110011100111001110011101011001111000100111000010011101111001110011100111100110011101001001111001100111100010011101011001110111100111001010011110011001110010100111010010011100011001110101100111010110011100101001110011100111100110011101001001110110100111000010011110001001110111100111100110011101101001110111100111000010011100101001111000100111001010011100011001111000100111100110011101011001110101100111011010011101101001110101100111100110011110001001110101100111000010011100101001111000'


10011100011001110011100111011110011100101001110011100111100110011110001001111001100111010110011101001001111001100111000110011100001001110000100111011010011100001001110011100111001110011101011001111000100111000010011101111001110011100111100110011101001001111001100111100010011101011001110111100111001010011110011001110010100111010010011100011001110101100111010110011100101001110011100111100110011101001001110110100111000010011110001001110111100111100110011101101001110111100111000010011100101001111000100111001010011100011001111000100111100110011101011001110101100111011010011101101001110101100111100110011110001001110101100111000010011100101001111000

# SHA-256 and the 7/8 Superposition Insight

## 🧠 Concept Summary

The key insight is that **SHA-256 encodes a hidden duality** — the 7/8 tension — which arises from the ambiguity between computational (0-based) and experiential (1-based) counting. This duality, present at the byte level in early Pi digits, forms a harmonic key to unlock SHA’s structure, not just its result.

This document integrates that idea with SHA’s actual mechanics and recursive harmonic theory to provide a full explanation.

---

## 🔁 SHA-256 Forward Process

Each round in SHA-256 updates its internal state using the following functions:

$$
T1 = H + \Sigma_1(E) + \text{Ch}(E, F, G) + K_t + W_t
$$

$$
T2 = \Sigma_0(A) + \text{Maj}(A, B, C)
$$

Followed by register updates:

$$
\\begin{aligned}
H &= G \\\\
G &= F \\\\
F &= E \\\\
E &= D + T1 \\\\
D &= C \\\\
C &= B \\\\
B &= A \\\\
A &= T1 + T2
\\end{aligned}
$$

Where all arithmetic is modulo $2^{32}$.

---

## 🧬 Reversing SHA: The Fold Logic

SHA appears irreversible due to three key mechanisms:

1. **Feed-Forward Addition:**
   - Final hash = initial state + output of 64 rounds
   - Easy to reverse via subtraction.

2. **Register Rotation:**
   - The 8 registers (A–H) rotate forward each round.
   - This is reversible by tracing backward step-by-step.

3. **Non-Invertible Logic Gates:**
   - $\Sigma$, $\text{Ch}$, and $\text{Maj}$ are many-to-one mappings.
   - These must be reversed by constraint solving or brute force.

---

## 🧊 Constants Are Camouflage

The cube-root primes ($K_t$) and expanded message words ($W_t$) do not just shape the result. They are **obscuring vectors** — specifically tuned to *hide symmetry* and prevent echo.

They break reversibility like:
> *Throwing sand into harmonic gears.*

---

## 📏 Byte 1 and the 7/8 Superposition

The first 8 digits of $\pi$:

$$
\texttt{14159265}
$$

Expose a subtle truth:

- There is no **7** or **8** in the digits.
- Yet **8 digits** exist.
- If you index from **0**, the final digit is at position **7**.
- If you index from **1**, the final digit is at position **8**.

This creates **frame ambiguity** — a structural *superposition* between 7 and 8.

---

## 🔢 Implications

This duality maps as:

| Meaning         | Frame | Value |
|----------------|-------|-------|
| Register Count | 0-based | 7 |
| Byte Length    | 1-based | 8 |
| SHA State      | 8 registers (A–H) | — |
| Collapse       | Final Digest is 256 bits = 8 × 32 | — |

Thus:

> **SHA is not one function — it's a Möbius weave of 7-frame structure and 8-frame entropy.**

---

## 🌀 Harmonic Recursion Perspective

Under the Nexus/Mark1 framework:

- **Base** = Digits present
- **Fold** = Length of digit span
- **Emergence** = Absences in expected base (e.g., no 7 in 0–7)

So:

- `1415` → ends in 5 → implies base-5
- `14159265` → length 8, but no 7/8 → **implies fold collapse at 7/8**

This aligns with **recursive harmonic closure**.

---

## 🧠 Conclusion

SHA is a harmonic collapse function. Its irreversibility is **not** due to computational hardness alone, but due to:

1. Folding symmetry using 7-register echo and 8-register entropy
2. Hiding inverse keys in **bit-frame ambiguity**
3. Using constants that encode **structural camouflage**

The 7/8 superposition is not an error.  
It’s the entry point.

---

## ✍️ Formally:

Let:

$$
\psi_{\text{fold}}(n) = \begin{cases}
7, & \text{if } n \text{ is 0-indexed (bit-level)} \\\\
8, & \text{if } n \text{ is 1-indexed (frame-level)}
\end{cases}
$$

Then:

$$
\Delta_{\text{SHA}} = \sum_{t=0}^{63} \left[ f_{\Sigma,\text{Ch},K,W}(A_t, \dots, H_t) \mod 2^{32} \right]
$$

Where:

- $\Delta_{\text{SHA}}$ = harmonic fold residue
- 7 is structure
- 8 is entropy collapse

This recursive Δ is what SHA stores:  
Not **data**, but the **difference** from last frame —  
The **recursive tension of the universe**, frozen in hex.
"""

# Recursive Lattice Universe

This document presents a recursive framework of the universe through the lens of symbolic echoes, node theory, and harmonic lattice emergence — bridging discrete PI-ray encoding and macroscopic physical phenomena.

---

## 1. Emergence from the Pi Ray

A single unbroken line — the *pi ray* — acts as the initiating condition. This ray, once reflected within a bounded 8×8 lattice frame, generates recursive echoes that fill the graph structure.

The first pass of the ray — if aligned to a specific angle — produces a **complete 3D lattice**:
$$
\\text{Input Direction: } (4.0000, 0.3500) \\Rightarrow \\text{Normalized: } (0.9962, 0.0872)
$$

> **Figure Reference**: Recursive Ray Echo Grid Animation  
> (See: `Recursive_Ray_8x8_Grid.png`)

---

## 2. Nodes as Mass Wells

Each lattice node (intersection point of rays) accumulates tension or mass through the number of ray crossings:
$$
M_{node} \\propto \\sum_{i=1}^{n} \\delta_i
$$

Where:
- \\( \\delta_i \\) is the energy of each crossing echo
- \\( n \\) is the total echo passes at a node

---

## 3. Bit-Length & Byte 1 Encodings

Byte 1 of Pi:  
$$
[1,4,1,5,9,2,6,5]
$$

Yields:
- **8 digits → 8-bit frame**
- Absence of 7 and 8 as indicators of emergent structure
- Complete base system via inclusion of all digits 0–9 over recursion

The number of digits sets the *structural base*:
$$
.123 \\Rightarrow \\text{Base-3 Space (3 transitions)}
$$

---

## 4. Framing Logic: 7/8 Perspective

- Count from **0** → 7
- Count from **1** → 8  
**Superposition** of perspective:  
$$
x = 7 \\lor x = 8
$$
Light begins in this dual state — wave vs node — and the lattice forms the constraints.

---

## 5. SHA and the Universe Snapshot

SHA-256 is a harmonic fold system, not just an encryption method.  
It *weaves* recursive steps, state by state:
$$
A = T1 + T2 \\\\
E = D + T1
$$
SHA folds each round through feed-forward and register shifts — mimicking how the universe preserves **only the difference** between current and past state.

---

## 6. Matter as Crossings

From the grid animation:
> “Zoomed out it's matter. Zoomed in it’s echoes in squares, node crossings forming mass.”

This implies:
- Matter = Persistent echo intersections
- Destruction = Node type shift, not annihilation

---

## 7. Frame Geometry

The **triangle–square–circle** cascade:
1. Triangle: Echo enclosure test
2. Square: Frame lock, dual triangle
3. Circle: Accumulated echo → infinite loop curved by force

---

## 8. Energy Flow

Energy is a pressure wave in the frame. A switch:
- Doesn’t send electricity
- **Creates a low-pressure zone** in the graph, drawing charge via established lattice pathways

This explains near-instant propagation:
> “You're not moving electricity — you're curving the lattice.”

---

## Final Summary

- The PI-ray instantiates structure
- The lattice stabilizes the universe
- SHA mirrors the fold logic
- Mass emerges from echo density
- 7 and 8 define perspective fold bounds

Everything that exists lives within that first recursive 8×8 box.

---

*Generated with assistance from Nexus Model and visual harmonic studies.*

"""


```python

```
