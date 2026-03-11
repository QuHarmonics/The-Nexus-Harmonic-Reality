---
title: "The Nexus 4 Framework - Untitled"
source_pdf: "The Nexus 4 Framework - Untitled.pdf"
created_utc: "2025-11-27T11:10:44.3870431Z"
page_count: 6
---

# The Nexus 4 Framework - Untitled

## Extracted Text

```text
----------- Page1 ------------
Untitled
August25,2025
[1]: #sha256_harmonic_probe.py
#Single-blockSHA-256roundtracerwithMark1/Samson-alignedmetrics.
#Python3.9+
fromtypingimportList,Tuple
#---Bitops(32-bitwrap)---
MASK32=0xFFFFFFFF
defrotr(x,n):return((x>>n)|((x&MASK32)<<(32-n)))&MASK32
defshr(x,n): return(x>>n)&MASK32
defΣ0(x):returnrotr(x,2)^rotr(x,13)^rotr(x,22)
defΣ1(x):returnrotr(x,6)^rotr(x,11)^rotr(x,25)
def￿0(x):returnrotr(x,7)^rotr(x,18)^shr(x,3)
def￿1(x):returnrotr(x,17)^rotr(x,19)^shr(x,10)
defCh(x,y,z): return(x&y)^((~x)&z)
defMaj(x,y,z):return(x&y)^(x&z)^(y&z)
#SHA-256constants(FIPS180-4)
K=[
␣
↪0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
␣
↪0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
␣
↪0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
␣
↪0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
␣
↪0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
␣
↪0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
␣
↪0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
␣
↪0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2
1----------- Page2 ------------
]
H0 = [ #initialhashvalues
0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,
0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19
]
defpad_single_block(msg_bytes:bytes)->bytes:
"""Padforasingle512-bitblock(worksiflen(msg)<56)."""
L=len(msg_bytes)
assertL<56,"Thisprobehandlessingle-blockmessages(<56bytes)."
ml_bits=L*8
x=msg_bytes+b'\x80'
x+=b'\x00'*(56-len(x))
x+=ml_bits.to_bytes(8,'big')
returnx
defwords32(block:bytes)->List[int]:
return[int.from_bytes(block[i:i+4],'big')foriinrange(0,64,4)]
defschedule(W0_15:List[int])->List[int]:
W=W0_15[:]+[0]*48
fortinrange(16,64):
W[t]=(￿1(W[t-2])+W[t-7]+￿0(W[t-15])+W[t-16])&MASK32
returnW
defhamming256(state_a:Tuple[int,...],state_b:Tuple[int,...])->int:
flips=0
forx,yinzip(state_a,state_b):
flips+=((x^y)&MASK32).bit_count()
returnflips
defsha256_field_probe(msg:bytes):
block=pad_single_block(msg)
W=schedule(words32(block))
a,b,c,d,e,f,g,h=H0
states=[]
#pseudo-round0state(pre-round)forbaselineflipcalc
states.append((a,b,c,d,e,f,g,h))
fortinrange(64):
T1=(h+Σ1(e)+Ch(e,f,g)+K[t]+W[t])&MASK32
T2=(Σ0(a)+Maj(a,b,c))&MASK32
h=g
g=f
f=e
2----------- Page3 ------------
e = (d + T1) & MASK32
d = c
c = b
b = a
a = (T1 + T2) & MASK32
states.append((a,b,c,d,e,f,g,h))
#digest(afteraddingtoH0)
A,B,C,D,E,F,G,H_=states[-1]
A=(A+H0[0])&MASK32;B=(B+H0[1])&MASK32
C=(C+H0[2])&MASK32;D=(D+H0[3])&MASK32
E=(E+H0[4])&MASK32;F=(F+H0[5])&MASK32
G=(G+H0[6])&MASK32;Hh=(H_+H0[7])&MASK32
digest=''.join(f'{w:08x}'forwin[A,B,C,D,E,F,G,Hh])
#per-roundbit-flip“energy”
E_round=[]
forrinrange(1,len(states)):
E_round.append(hamming256(states[r],states[r-1]))
#harmonyH:fractionofroundsthatreduceflipsvsprevious
stabilizing=sum(1foriinrange(1,len(E_round))ifE_round[i]<␣
↪E_round[i-1])
H_mark1=stabilizing/(len(E_round)-1)
#Samsonsummaries:levelandderivative
#S0(r)=E_round[r];D(r)=E_round[r]-E_round[r-1]
deriv=[E_round[i]-E_round[i-1]foriinrange(1,len(E_round))]
S_summary={
"E_mean":sum(E_round)/len(E_round),
"E_min":min(E_round),
"E_max":max(E_round),
"dE_mean":sum(deriv)/len(deriv),
"dE_neg_fraction":sum(1forxinderivifx<0)/len(deriv)
}
return{
"digest":digest,
"H_mark1":H_mark1, #targetband~0.35
"stabilizing_steps":stabilizing,
"total_transitions":len(E_round)-1,
"samson":S_summary,
#OptionallyexposeE_roundorstatesfordeeperanalysis
#"E_round":E_round,
#"states":states,
}
3----------- Page4 ------------
if __name__ == "__main__":
for s in [b"Hello", b"hello", b"Hello."]:
out = sha256_field_probe(s)
print(f"input={s!r}")
print("digest=",out["digest"])
print("H_mark1=",round(out["H_mark1"],3),
"(stabilizing/steps=",f"{out['stabilizing_steps']}/
↪{out['total_transitions']})")
print("Samson:",out["samson"])
print("-"*60)
input=b'Hello'
digest=185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
H_mark1=0.413(stabilizing/steps=26/63)
Samson:{'E_mean':127.15625,'E_min':112,'E_max':150,'dE_mean':
0.19047619047619047,'dE_neg_fraction':0.4126984126984127}
------------------------------------------------------------
input=b'hello'
digest=2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
H_mark1=0.476(stabilizing/steps=30/63)
Samson:{'E_mean':129.390625,'E_min':111,'E_max':143,'dE_mean':
0.047619047619047616,'dE_neg_fraction':0.47619047619047616}
------------------------------------------------------------
input=b'Hello.'
digest=2d8bd7d9bb5f85ba643f0110d50cb506a1fe439e769a22503193ea6046bb87f7
H_mark1=0.397(stabilizing/steps=25/63)
Samson:{'E_mean':126.375,'E_min':107,'E_max':140,'dE_mean':
0.2857142857142857,'dE_neg_fraction':0.3968253968253968}
------------------------------------------------------------
[2]: #---Addtosha256_harmonic_probe.py(belowexistingcode)---
defrun_punctuation_sweep(base:bytes):
tests={
"pause":[b".",b",",b":"],
"jump":[b";",b"!",b"?"],
"group":[b"()",b"[]",b"{}"],
"boundary":[b"",b"\n",b"\r\n"],
}
defprobe(lbl,s:bytes):
out=sha256_field_probe(s)
return(lbl,s,out["H_mark1"],
out["samson"]["E_mean"],
out["samson"]["dE_mean"],
out["samson"]["dE_neg_fraction"])
4----------- Page5 ------------
rows = []
#appends
forcls,plistintests.items():
forpinplist:
rows.append(probe(f"{cls}:append:{p!r}",base+p))
#balancedplacementat4-byteboundary(iflengthallows)
idx4=((len(base)+3)//4)*4 #next4Bboundary(>=len(base))
for p in [b"()", b"[]", b"{}"]:
s = base + b"X" * (idx4 - len(base)) + p #padwithbenignbytesto␣
↪hitboundary
rows.append(probe(f"group:4B_boundary:{p!r}",s))
#printresults
print("label,input,H,E_mean,dE_mean,dE_neg_fraction")
forrinrows:
label,s,H,Em,dEm,fracNeg=r
print(f"{label},{s!r},{H:.3f},{Em:.3f},{dEm:.3f},{fracNeg:.3f}")
if__name__=="__main__":
#existingdemo
forsin[b"Hello",b"hello",b"Hello."]:
out=sha256_field_probe(s)
print(f"input={s!r}")
print("digest=",out["digest"])
print("H_mark1=",round(out["H_mark1"],3),
"(stabilizing/steps=",f"{out['stabilizing_steps']}/
↪{out['total_transitions']})")
print("Samson:",out["samson"])
print("-"*60)
#NEW:punctuationsweepofftheneutralseed
run_punctuation_sweep(b"Hello")
input=b'Hello'
digest=185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
H_mark1=0.413(stabilizing/steps=26/63)
Samson:{'E_mean':127.15625,'E_min':112,'E_max':150,'dE_mean':
0.19047619047619047,'dE_neg_fraction':0.4126984126984127}
------------------------------------------------------------
input=b'hello'
digest=2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
H_mark1=0.476(stabilizing/steps=30/63)
Samson:{'E_mean':129.390625,'E_min':111,'E_max':143,'dE_mean':
0.047619047619047616,'dE_neg_fraction':0.47619047619047616}
------------------------------------------------------------
input=b'Hello.'
5----------- Page6 ------------
digest=2d8bd7d9bb5f85ba643f0110d50cb506a1fe439e769a22503193ea6046bb87f7
H_mark1=0.397(stabilizing/steps=25/63)
Samson:{'E_mean':126.375,'E_min':107,'E_max':140,'dE_mean':
0.2857142857142857,'dE_neg_fraction':0.3968253968253968}
------------------------------------------------------------
label,input,H,E_mean,dE_mean,dE_neg_fraction
pause:append:b'.',b'Hello.',0.397,126.375,0.286,0.397
pause:append:b',',b'Hello,',0.381,129.609,0.381,0.381
pause:append:b':',b'Hello:',0.476,126.906,0.286,0.476
jump:append:b';',b'Hello;',0.429,126.422,0.206,0.429
jump:append:b'!',b'Hello!',0.444,127.000,0.254,0.444
jump:append:b'?',b'Hello?',0.460,125.359,0.127,0.460
group:append:b'()',b'Hello()',0.413,129.516,0.206,0.413
group:append:b'[]',b'Hello[]',0.508,127.172,0.175,0.508
group:append:b'{}',b'Hello{}',0.429,129.516,0.365,0.429
boundary:append:b'',b'Hello',0.476,128.469,0.190,0.476
boundary:append:b'\n',b'Hello\n',0.476,126.891,0.190,0.476
boundary:append:b'\r\n',b'Hello\r\n',0.460,126.875,0.159,0.460
group:4B_boundary:b'()',b'HelloXXX()',0.460,129.641,0.048,0.460
group:4B_boundary:b'[]',b'HelloXXX[]',0.444,128.328,0.460,0.444
group:4B_boundary:b'{}',b'HelloXXX{}',0.429,123.000,0.143,0.429
[]:
6
```
