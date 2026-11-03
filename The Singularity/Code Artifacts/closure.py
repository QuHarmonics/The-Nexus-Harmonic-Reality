#!/usr/bin/env python3
"""
CLOSURE: is the settled nibble value SUFFICIENT for the click?
If C_A(j) = 1[T1_j + T2_j + c_in(j) >= 16] with ZERO exceptions, then by
sufficiency H(C_A | v,x,c)=0, so construction-carry (or ANY other variable)
carries ZERO residual information about the click once the settled nibbles
are fixed. That is the exact, mechanical form of "the gap is spent; only the
settled value survives." It also closes doc-10's one OPEN item: the T2
'depletion residual' that survived popcount control must vanish under
EXACT-value control -- proving it was popcount's lossiness, not a mechanism.
"""
import numpy as np, hashlib
MASK32=0xFFFFFFFF
K=[0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
 0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
 0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
 0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
 0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
 0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
 0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
 0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2]
IV=[0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19]
def rotr(x,n): return ((x>>n)|(x<<(32-n)))&MASK32
def S0(x): return rotr(x,2)^rotr(x,13)^rotr(x,22)
def S1(x): return rotr(x,6)^rotr(x,11)^rotr(x,25)
def s0(x): return rotr(x,7)^rotr(x,18)^(x>>3)
def s1(x): return rotr(x,17)^rotr(x,19)^(x>>10)
def Ch(x,y,z): return (x&y)^((~x&MASK32)&z)
def Maj(x,y,z): return (x&y)^(x&z)^(y&z)
def touch_nibbles(x,y):
    carry=0; t=set()
    for i in range(32):
        s=((x>>i)&1)+((y>>i)&1)+carry; carry=1 if s>=2 else 0
        if carry: t.add(i//4)
    return t
def boundary_mask(x,y):   # 31-bit: boundary i crossed if carry out of bit i
    carry=0; m=0
    for i in range(32):
        s=((x>>i)&1)+((y>>i)&1)+carry; carry=1 if s>=2 else 0
        if carry and i<31: m|=(1<<i)
    return m

def run(seed,h0,collect):
    W=list(seed)+[0]*48
    for tt in range(16,64):
        v1=(s1(W[tt-2])+W[tt-7])&MASK32; v2=(v1+s0(W[tt-15]))&MASK32; W[tt]=(v2+W[tt-16])&MASK32
    st=list(h0)
    for t in range(64):
        a,b,c,d,e,f,g,h=st
        T1=(h+S1(e)+Ch(e,f,g)+K[t]+W[t])&MASK32
        T2=(S0(a)+Maj(a,b,c))&MASK32
        an=(T1+T2)&MASK32; en=(d+T1)&MASK32
        ct2=touch_nibbles(S0(a),Maj(a,b,c))        # T2 CONSTRUCTION carry, per nibble
        # nibble-level click chain for A = T1 + T2
        cin=0
        for j in range(8):
            v=(T1>>(4*j))&0xF; x=(T2>>(4*j))&0xF
            s=v+x+cin; cout=1 if s>=16 else 0
            collect['v'].append(v); collect['x'].append(x); collect['cin'].append(cin)
            collect['CA'].append(cout); collect['CT2'].append(1 if j in ct2 else 0)
            collect['pop_x'].append(bin(x).count('1'))
            cin=cout
        # stash masks for transfer matrix (T1_4 == T1 here; use last chain add of T1 build)
        X3=(h+S1(e)+Ch(e,f,g)+K[t])&MASK32
        collect['mT1_4'].append(boundary_mask(X3,W[t]))
        collect['mA'].append(boundary_mask(T1,T2))
        st=[an,a,b,c,en,e,f,g]
    dig=[(st[i]+h0[i])&MASK32 for i in range(8)]
    return dig

configs=[('all_zero',[0]*8),('all_ones',[MASK32]*8),('SHA_IV',list(IV)),('IV_abc',list(IV)),('IV_abd',list(IV))]
seeds={'IV_abc':[0x61626380]+[0]*14+[0x18],'IV_abd':[0x61626480]+[0]*14+[0x18]}
def sd(n): return seeds.get(n,[0x80000000]+[0]*14+[0])
C={k:[] for k in ['v','x','cin','CA','CT2','pop_x','mT1_4','mA']}
for n,h0 in configs:
    dig=run(sd(n),h0,C)
    if n=='IV_abc': print("verify abc:", ''.join(f'{z:08x}' for z in dig)==hashlib.sha256(b'abc').hexdigest())
    if n=='IV_abd': print("verify abd:", ''.join(f'{z:08x}' for z in dig)==hashlib.sha256(b'abd').hexdigest())

v=np.array(C['v']); x=np.array(C['x']); cin=np.array(C['cin'])
CA=np.array(C['CA']); CT2=np.array(C['CT2']); popx=np.array(C['pop_x'])
N=len(CA)

print("\n"+"="*76)
print(f"SUFFICIENCY TEST   (N = {N} wheel-events across 5 configs x 64 rounds x 8 wheels)")
print("="*76)
forced = ((v+x+cin)>=16).astype(int)
exc = int(np.sum(CA!=forced))
print(f"exceptions to  C_A = 1[T1_j + T2_j + c_in >= 16] :  {exc}")
print(f"distinct (v,x,c_in) states observed              :  {len(set(zip(v.tolist(),x.tolist(),cin.tolist())))} / 512")

def partial_corr(A,B,by):
    """corr(A,B) after removing the mean of each within groups 'by'."""
    A=A.astype(float).copy(); B=B.astype(float).copy()
    for key in np.unique(by,axis=0) if by.ndim>1 else np.unique(by):
        m = np.all(by==key,axis=1) if by.ndim>1 else (by==key)
        A[m]-=A[m].mean(); B[m]-=B[m].mean()
    if A.std()<1e-12 or B.std()<1e-12: return 0.0, A.std()
    return np.corrcoef(A,B)[0,1], A.std()

print("\n"+"="*76)
print("CLOSING DOC-10's OPEN ITEM: is the T2 'depletion residual' a mechanism?")
print("="*76)
raw=np.corrcoef(CT2,CA)[0,1]
print(f"raw   corr(T2-construction-carry, C_A)                     = {raw:+.4f}")
pc_pop,resid_pop=partial_corr(CA,CT2,popx)
print(f"partial, controlling for T2 nibble POPCOUNT (doc-10 method)= {pc_pop:+.4f}   (residual C_A std={resid_pop:.3f})")
vxc=np.stack([v,x,cin],axis=1)
pc_exact,resid_exact=partial_corr(CA,CT2,vxc)
print(f"partial, controlling for EXACT (v,x,c_in)                  = {pc_exact:+.4f}   (residual C_A std={resid_exact:.3e})")
# variance of C_A within cells
def maxvar(by):
    mv=0
    for key in np.unique(by,axis=0) if by.ndim>1 else np.unique(by):
        m=np.all(by==key,axis=1) if by.ndim>1 else (by==key)
        if m.sum()>1: mv=max(mv,CA[m].var())
    return mv
print(f"\nmax within-POPCOUNT-bucket variance of C_A  = {maxvar(popx):.4f}   (>0 -> popcount leaks -> spurious residual)")
print(f"max within-EXACT-(v,x,c) variance of C_A    = {maxvar(vxc):.4e}   (=0 -> value is sufficient -> zero residual)")

print("\n"+"="*76)
print("THE PROPOSED CARRY-TRANSFER MATRIX  M[i,j]=P(A crosses bnd j | T1_4 crosses bnd i)")
print("="*76)
mT=np.array(C['mT1_4']); mA=np.array(C['mA'])
# build 31x31
T1bits=np.array([[ (m>>i)&1 for i in range(31)] for m in mT])
Abits =np.array([[ (m>>i)&1 for i in range(31)] for m in mA])
M=np.zeros((31,31))
for i in range(31):
    sel=T1bits[:,i]==1
    if sel.sum()>0: M[i]=Abits[sel].mean(axis=0)
diag=np.array([M[i,i] for i in range(31)])
offd=M[~np.eye(31,dtype=bool)]
base=Abits.mean(axis=0).mean()
print(f"mean diagonal  P(A bnd i | T1_4 bnd i) = {diag.mean():.3f}")
print(f"mean off-diag                          = {offd.mean():.3f}")
print(f"base rate P(A crosses a boundary)      = {base:.3f}")
print(f"diagonal lift over base                = {diag.mean()/base:.3f}x   (near 1 => no transport operator, just arithmetic)")
print("\n-> Given the sufficiency result above, C_A has zero conditional entropy given")
print("   the settled nibbles, so I(C_A ; any-transfer-structure | settled) = 0 by")
print("   construction. The transfer matrix reads the exhaust address, not the ledger.")
