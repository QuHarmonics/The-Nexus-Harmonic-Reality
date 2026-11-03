#!/usr/bin/env python3
"""
THE MACHINE IN 3D. No probe. Just the fixed structure, watched.
The output slots are fixed. The machine is fixed. The values are constrained.
That is the fixed points -- so render them and see what stands and what streams.

x : nibble 0..7  within a register  (the carry gradient: low->high weight)
y : register a..h                    (the shift / delay line)
z : round 0..63                      (the unfold; time is an axis, route at rest)

Two registers (a,e) are the only sites where a value is *made* (T1+T2, d+T1) --
the fixed windows, drawn bright, carry-colored. The other six only *hold and
shift* what those two made -- the delay line, drawn faint, value-colored, with
flow lines so the streaming is visible. Two nodes stand; the field streams.
"""
import numpy as np, plotly.graph_objects as go
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
def nib_carry(x,y):   # per-nibble carry-out (8 flags) of x+y
    cin=0; out=[]
    for j in range(8):
        s=((x>>(4*j))&0xF)+((y>>(4*j))&0xF)+cin; c=1 if s>=16 else 0; out.append(c); cin=c
    return out

def run(seed,h0):
    W=list(seed)+[0]*48
    for t in range(16,64):
        W[t]=(s1(W[t-2])+W[t-7]+s0(W[t-15])+W[t-16])&MASK32
    st=list(h0)
    states=[]; acarry=[]; ecarry=[]
    for t in range(64):
        a,b,c,d,e,f,g,h=st
        T1=(h+S1(e)+Ch(e,f,g)+K[t]+W[t])&MASK32
        T2=(S0(a)+Maj(a,b,c))&MASK32
        an=(T1+T2)&MASK32; en=(d+T1)&MASK32
        acarry.append(nib_carry(T1,T2)); ecarry.append(nib_carry(d,T1))
        st=[an,a,b,c,en,e,f,g]
        states.append(list(st))
    return states,acarry,ecarry

states,acarry,ecarry=run([0x61626380]+[0]*14+[0x18],list(IV))
REG='abcdefgh'
def nib(val,j): return (val>>(4*j))&0xF

fig=go.Figure()

# --- the delay line: six streaming registers (b,c,d,f,g,h) faint, value-colored ---
xs,ys,zs,cs,tx=[],[],[],[],[]
for t in range(64):
    for r in range(8):
        if REG[r] in 'ae': continue
        for j in range(8):
            xs.append(j); ys.append(r); zs.append(t); cs.append(nib(states[t][r],j))
            tx.append(f"{REG[r]}[{j}]={nib(states[t][r],j):X} r{t}")
fig.add_trace(go.Scatter3d(x=xs,y=ys,z=zs,mode='markers',
    marker=dict(size=2.2,color=cs,colorscale='Viridis',cmin=0,cmax=15,opacity=0.28),
    hovertext=tx,hoverinfo='text',name='delay line (holds & shifts)'))

# --- flow lines: the shift a->b->c->d and e->f->g->h (the streaming) ---
lx,ly,lz=[],[],[]
for t in range(61):
    for j in range(8):
        for chain in [[0,1,2,3],[4,5,6,7]]:       # a->b->c->d , e->f->g->h
            for k,r in enumerate(chain):
                lx.append(j); ly.append(r); lz.append(t+k)
            lx.append(None); ly.append(None); lz.append(None)
fig.add_trace(go.Scatter3d(x=lx,y=ly,z=lz,mode='lines',
    line=dict(color='rgba(120,140,200,0.10)',width=1),name='shift (streaming)',hoverinfo='skip'))

# --- the two FIXED WINDOWS: a and e, bright, carry-colored (the fixed points) ---
for r,carry,cname,label in [(0,acarry,'#ff2d2d','a-window (T1+T2)'),
                            (4,ecarry,'#ff9500','e-window (d+T1)')]:
    xs,ys,zs,col,sz,tx=[],[],[],[],[],[]
    for t in range(64):
        for j in range(8):
            xs.append(j); ys.append(r); zs.append(t)
            hot = carry[t][j]==1
            col.append(cname if hot else 'rgba(60,60,80,0.5)')
            sz.append(6.5 if hot else 3.0)
            tx.append(f"{REG[r]}[{j}]={nib(states[t][r],j):X}  carry={'YES' if hot else 'no'}  r{t}")
    fig.add_trace(go.Scatter3d(x=xs,y=ys,z=zs,mode='markers',
        marker=dict(size=sz,color=col,opacity=0.95),hovertext=tx,hoverinfo='text',name=label))

fig.update_layout(
    title=dict(text="THE MACHINE — two fixed windows stand, six registers stream<br>"
                    "<sub>fixed slots · fixed machine · constrained values = the fixed points</sub>",
               font=dict(color='white',size=18),x=0.5),
    paper_bgcolor='#0a0a0a',
    scene=dict(
        xaxis=dict(title='nibble 0→7  (carry gradient)',color='white',backgroundcolor='#0a0a0a',gridcolor='#222'),
        yaxis=dict(title='register a→h  (shift / delay)',tickvals=list(range(8)),ticktext=list(REG),
                   color='white',backgroundcolor='#0a0a0a',gridcolor='#222'),
        zaxis=dict(title='round 0→63  (the unfold)',color='white',backgroundcolor='#0a0a0a',gridcolor='#222'),
        camera=dict(eye=dict(x=1.9,y=1.5,z=1.1)),
        aspectratio=dict(x=1,y=1,z=2.2)),
    legend=dict(font=dict(color='white'),bgcolor='rgba(20,20,20,0.6)'),
    margin=dict(l=0,r=0,t=70,b=0))

out='/mnt/user-data/outputs/sha_machine_3d.html'
fig.write_html(out,include_plotlyjs='cdn')
print("saved",out)
# also a static preview
try:
    fig.write_image('/mnt/user-data/outputs/sha_machine_3d.png',width=1400,height=1000,scale=1)
    print("saved png preview")
except Exception as e:
    print("png preview skipped:",str(e)[:80])
