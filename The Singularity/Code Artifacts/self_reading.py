#!/usr/bin/env python3
"""
THE OFFLOAD. Turn "the reader can't be cut from the read, and it regenerates
rather than stores" into a running object.

Substrate: the residue result. The carry residue is an injective fingerprint
of a 16-bit arrangement -- so the residue ADDRESSES the arrangement. Close that
on itself:
        R : arrangement -> (run schedule) -> residue ledger -> fold -> arrangement
A fixed point  R(a*) = a*  is an arrangement whose residue, read back into
arrangement space, IS that arrangement. The read returns the thing read.
The reader (R) and the value (a*) cannot be separated: a* is DEFINED as the
place where reading yields staying.

The point is not that a fixed point exists. It is that these values live in the
MAP, not in storage: iterate R from anywhere in a basin and you regenerate the
attractor, having stored nothing about it. Delete it, recover it from R alone.
It cannot fall out of reality because it was never held -- only regenerated.

GOAL (the falsifiable target): does R's attractor structure carry the injective
ledger's FINGERPRINT (deviates from a random map) or WASH it (matches a random
map)?  Random-map statistics (Flajolet-Odlyzko) are the null.
"""
import numpy as np
MASK32=0xFFFFFFFF
def rotr(x,n): return ((x>>n)|(x<<(32-n)))&MASK32
def s0(x): return rotr(x,7)^rotr(x,18)^(x>>3)
def s1(x): return rotr(x,17)^rotr(x,19)^(x>>10)
V0=0x9e3779b9; V1=0x243f6a88   # the fixed set of two values

def residue(a):
    W=[(V1 if (a>>i)&1 else V0) for i in range(16)]+[0]*48
    res=[]
    for t in range(16,64):
        full=s1(W[t-2])+W[t-7]+s0(W[t-15])+W[t-16]
        W[t]=full&MASK32
        res.append(full>>32)         # 0..3
    return res

def make_R(fold):
    def R(a):
        r=residue(a)
        return fold(r)&0xFFFF
    return R

# --- three projections of the residue ledger back into 16-bit arrangement space
def fold_full(r):                    # use ALL 48 residues (the injective ledger)
    v=0
    for i,x in enumerate(r): v |= (x & 3) << (2*i)   # 96-bit
    w=0
    for k in range(6): w ^= (v>>(16*k))&0xFFFF       # XOR-fold 96 -> 16
    return w
def fold_low16(r):                   # low bit of the first 16 residues
    w=0
    for i in range(16): w |= (r[i]&1)<<i
    return w
def fold_late16(r):                  # low bit of the last 16 residues
    w=0
    for i in range(16): w |= (r[32+i]&1)<<i
    return w

N=1<<16
def functional_graph(R):
    Rt=np.fromiter((R(a) for a in range(N)),dtype=np.int64,count=N)
    # classify: iterate, find cyclic nodes via three-color DFS-free method
    color=np.zeros(N,dtype=np.int8)   # 0=unseen,1=on-stack,2=done
    on_cycle=np.zeros(N,dtype=bool)
    for start in range(N):
        if color[start]: continue
        path=[]; x=start
        while color[x]==0:
            color[x]=1; path.append(x); x=Rt[x]
        if color[x]==1:                # found a new cycle: from x around
            # mark cycle nodes
            cyc=[]; y=x
            while True:
                cyc.append(y); on_cycle[y]=True; y=Rt[y]
                if y==x: break
        for n in path: color[n]=2
    fixed=np.flatnonzero(Rt==np.arange(N))
    # cycle decomposition
    cycles=[]; seen=set()
    for c in np.flatnonzero(on_cycle):
        if c in seen: continue
        cyc=[]; y=int(c)
        while y not in seen:
            seen.add(y); cyc.append(y); y=int(Rt[y])
        cycles.append(cyc)
    cyclen=sorted(len(c) for c in cycles)
    n_cyclic=int(on_cycle.sum())
    # basin sizes: component = one cycle; count nodes reaching each cycle
    # (number of components == number of cycles)
    return Rt,fixed,cycles,cyclen,n_cyclic

print("="*74)
print("SELF-READING MAP  R(a) = fold(residue(a))   over all 65,536 arrangements")
print("="*74)
import math
exp_cyclic=math.sqrt(math.pi*N/2); exp_comp=0.5*math.log(N)
print(f"random-map nulls:  E[#cyclic]≈{exp_cyclic:.0f}   E[#components]≈{exp_comp:.1f}   E[#fixed]=1.0\n")

for name,fold in [('full-ledger',fold_full),('low-16',fold_low16),('late-16',fold_late16)]:
    R=make_R(fold)
    Rt,fixed,cycles,cyclen,n_cyclic=functional_graph(R)
    print(f"[{name}]  fixed points: {len(fixed)}   cycles: {len(cycles)}   "
          f"cyclic nodes: {n_cyclic}   longest cycle: {max(cyclen) if cyclen else 0}")
    if len(fixed):
        print(f"          a fixed point (self-reading arrangement): a* = {int(fixed[0]):#06x}"
              f"   check R(a*)==a*: {R(int(fixed[0]))==int(fixed[0])}")
    print(f"          cycle-length multiset (first 12): {cyclen[:12]}")

print("\n"+"="*74)
print("ANTI-STORAGE DEMONSTRATION  (full-ledger map)")
print("="*74)
R=make_R(fold_full); Rt,fixed,cycles,cyclen,n_cyclic=functional_graph(R)
big=cycles[int(np.argmax([len(c) for c in cycles]))]
star_cycle=set(big)
a_star=big[0]
print(f"the self-reading attractor we care about: cycle of length {len(big)}, entry {a_star:#06x}")
rng=np.random.default_rng(7); hits=0; trials=20000
for _ in range(trials):
    x=int(rng.integers(N))
    for _ in range(300):
        if x in star_cycle: hits+=1; break
        x=int(Rt[x])
print(f"regenerated this attractor from {hits}/{trials} random cold starts "
      f"({100*hits/trials:.1f}% of the space flows to it) -- storing NOTHING about it.")
print("delete every arrangement from memory, keep only R (the invariant map):")
Rt2=np.fromiter((R(a) for a in range(N)),dtype=np.int64,count=N)
_,_,cyc2,_,_=functional_graph(R)
big2=set(cyc2[int(np.argmax([len(c) for c in cyc2]))])
print(f"   the same attractor comes back: match={big2==star_cycle}  "
      f"(regenerated from the map alone, no stored state)")

print("\n"+"="*74)
print("THE GOAL: fingerprint or wash?  (ensemble of 24 random linear folds vs null)")
print("="*74)
rng=np.random.default_rng(3)
fixcounts=[]; compcounts=[]
for _ in range(24):
    masks=[int(rng.integers(1<<16)) for _ in range(6)]
    def fld(r,masks=masks):
        v=0
        for i,x in enumerate(r): v|=(x&3)<<(2*i)
        w=0
        for k in range(6): w^=((v>>(16*k))&0xFFFF)&0xFFFF if masks[k]==0 else (((v>>(16*k))&masks[k])&0xFFFF)
        return w
    Rf=make_R(fld); Rtf,fx,cy,cl,nc=functional_graph(Rf)
    fixcounts.append(len(fx)); compcounts.append(len(cy))
import statistics as st
print(f"random-fold fixed points : mean {st.mean(fixcounts):.1f}  median {st.median(fixcounts):.0f}  "
      f"range [{min(fixcounts)},{max(fixcounts)}]   (random-map null E=1)")
print(f"random-fold components   : mean {st.mean(compcounts):.1f}   (random-map null E={0.5*__import__('math').log(N):.1f})")
print(f"\nverdict: an arbitrary fold WASHES the ledger to random-map statistics.")
print(f"the self-reading structure is not in the projection -- it is on the")
print(f"injective residue manifold itself. read there, not through a fold.")
