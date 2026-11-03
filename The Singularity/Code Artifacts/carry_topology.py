#!/usr/bin/env python3
"""
SHA-256 FULL-SUBSTRATE CARRY TOPOLOGY
Traces the carry mask of EVERY elementary two-input addition in the round
function AND the message schedule -- not only the two state-write adders
(a' = T1+T2, e' = d+T1) that the 64-slot activity map can see.

Answers doc-4's falsifiable split: are the A/E windows the SOURCE of the
carry dynamics, or the OUTPUT FACE of a deeper carry cascade?
"""
import hashlib

MASK32 = 0xFFFFFFFF
K = [
 0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
 0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
 0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
 0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
 0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
 0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
 0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
 0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2]
IV = [0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19]

def rotr(x,n): return ((x>>n)|(x<<(32-n)))&MASK32
def S0(x): return rotr(x,2)^rotr(x,13)^rotr(x,22)
def S1(x): return rotr(x,6)^rotr(x,11)^rotr(x,25)
def s0(x): return rotr(x,7)^rotr(x,18)^(x>>3)
def s1(x): return rotr(x,17)^rotr(x,19)^(x>>10)
def Ch(x,y,z): return (x&y)^((~x&MASK32)&z)
def Maj(x,y,z): return (x&y)^(x&z)^(y&z)

def add_trace(x,y):
    """x+y mod 2^32, plus the carry ripple: count of the 31 internal bit
    boundaries crossed by the carry, the nibble-touch set, and carry-out."""
    carry=0; boundaries=0; touched=set()
    for i in range(32):
        s=((x>>i)&1)+((y>>i)&1)+carry
        carry=1 if s>=2 else 0
        if carry:
            if i<31: boundaries+=1      # carry crosses boundary between bit i and i+1
            touched.add(i//4)
    return (x+y)&MASK32, boundaries, touched, carry

# ordered addition sites
COMP_SITES = ['T1_a','T1_b','T1_c','T1_d','T2','A','E']   # 7 per round
SCHED_SITES= ['W_a','W_b','W_c']                          # 3 per round (t>=16)
ALL_SITES  = SCHED_SITES + COMP_SITES                     # column order for the map

def compress(seed, h0):
    # schedule, instrumented
    W=list(seed)+[0]*48
    sched_bd={}  # (t,site)->boundaries
    for t in range(16,64):
        v1,b1,_,_ = add_trace(s1(W[t-2]), W[t-7])
        v2,b2,_,_ = add_trace(v1,         s0(W[t-15]))
        v3,b3,_,_ = add_trace(v2,         W[t-16])
        W[t]=v3
        sched_bd[(t,'W_a')]=b1; sched_bd[(t,'W_b')]=b2; sched_bd[(t,'W_c')]=b3
    # compression, instrumented
    st=list(h0)
    comp_bd={}
    active_sites_per_round=[]
    for t in range(64):
        a,b,c,d,e,f,g,h=st
        u1,b1,_,_ = add_trace(h,      S1(e))
        u2,b2,_,_ = add_trace(u1,     Ch(e,f,g))
        u3,b3,_,_ = add_trace(u2,     K[t])
        T1,b4,_,_ = add_trace(u3,     W[t])
        T2,b5,_,_ = add_trace(S0(a),  Maj(a,b,c))
        an,b6,tA,_= add_trace(T1,     T2)
        en,b7,tE,_= add_trace(d,      T1)
        for site,val in zip(COMP_SITES,[b1,b2,b3,b4,b5,b6,b7]):
            comp_bd[(t,site)]=val
        # count carry-active addition sites this round (boundaries>0)
        n_active = sum(1 for v in [b1,b2,b3,b4,b5,b6,b7] if v>0)
        n_active += sum(1 for s in SCHED_SITES if sched_bd.get((t,s),0)>0)
        active_sites_per_round.append(n_active)
        st=[an,a,b,c,en,e,f,g]
    digest=[(st[i]+h0[i])&MASK32 for i in range(8)]
    return digest, sched_bd, comp_bd, active_sites_per_round

def seed_empty(): return [0x80000000]+[0]*14+[0]
def seed_abc():   return [0x61626380]+[0]*14+[0x18]
def seed_abd():   return [0x61626480]+[0]*14+[0x18]

configs=[
 ('all_zero_empty',[0]*8,               seed_empty()),
 ('all_ones_empty',[MASK32]*8,          seed_empty()),
 ('SHA_IV_empty',  list(IV),            seed_empty()),
 ('IV_abc',        list(IV),            seed_abc()),
 ('IV_abd',        list(IV),            seed_abd()),
]

print("="*74)
print("SHA-256 FULL-SUBSTRATE CARRY TOPOLOGY")
print("="*74)

results={}
for name,h0,seed in configs:
    dig,sbd,cbd,active = compress(seed,h0)
    results[name]=(sbd,cbd,active)
    if name=='IV_abc':
        ref=hashlib.sha256(b'abc').hexdigest()
        mine=''.join(f'{x:08x}' for x in dig)
        print(f"verify abc: {mine==ref}")
    if name=='IV_abd':
        ref=hashlib.sha256(b'abd').hexdigest()
        mine=''.join(f'{x:08x}' for x in dig)
        print(f"verify abd: {mine==ref}")

# ---- DECISIVE RESULT: how many carry-active addition sites per round? ----
print("\n" + "-"*74)
print("CARRY-ACTIVE ADDITION SITES PER ROUND  (the 64-slot map sees only 2: A,E)")
print("-"*74)
print(f"{'config':>16s} {'min':>5s} {'mean':>6s} {'max':>5s}   (rounds 16-63 include 3 schedule sites)")
for name in results:
    a=results[name][2]
    late=a[16:]  # rounds with schedule active
    print(f"{name:>16s} {min(a):5d} {sum(a)/len(a):6.2f} {max(a):5d}   late-round mean={sum(late)/len(late):.2f}")

# ---- per-site carry ripple density (mean boundaries crossed / 31) ----
print("\n" + "-"*74)
print("MEAN CARRY RIPPLE PER SITE  (internal bit-boundaries crossed, out of 31)")
print("  A and E are starred -- these are the only two visible on the state map")
print("-"*74)
hdr=f"{'config':>16s}"
for s in ALL_SITES:
    tag=s+('*' if s in ('A','E') else '')
    hdr+=f"{tag:>7s}"
print(hdr)
for name in results:
    sbd,cbd,_=results[name]
    row=f"{name:>16s}"
    for s in ALL_SITES:
        if s in SCHED_SITES:
            vals=[sbd[(t,s)] for t in range(16,64)]
        else:
            vals=[cbd[(t,s)] for t in range(64)]
        row+=f"{sum(vals)/len(vals):7.2f}"
    print(row)

# ---- fraction of rounds each site carries AT ALL ----
print("\n" + "-"*74)
print("FRACTION OF ROUNDS WITH ANY CARRY, PER SITE  (IV_abc)")
print("-"*74)
sbd,cbd,_=results['IV_abc']
for s in ALL_SITES:
    if s in SCHED_SITES:
        vals=[sbd[(t,s)] for t in range(16,64)]; denom='16-63'
    else:
        vals=[cbd[(t,s)] for t in range(64)]; denom='0-63'
    frac=sum(1 for v in vals if v>0)/len(vals)
    print(f"  {s:>5s}  {frac*100:6.1f}%   (rounds {denom})")
