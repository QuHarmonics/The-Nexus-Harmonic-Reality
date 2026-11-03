from fractions import Fraction as F
from witness_Kd import A_profile, qD, word_at
half=F(1,2)
print("closest-to-seam witness per D: the two tail words and where the reader lands")
print(" D  j(D-1) s/L(D-1)  word(M+j,D-1)            j(D)  s/L(D)   word(M+j,D)")
for D in range(9,19):
    comps=[(a-half,b-half) for a,b in A_profile(qD(D),D) if a>=half]
    d=comps[0][0] + (comps[0][1]-comps[0][0])/2          # midpoint delta of nearest comp
    out=[]
    for L in (D-1,D):
        M=1<<(L-1); y=d*(1<<L); j=int(y); fr=y-j; s=int(fr*L)
        w=word_at(M+j,L)
        mark=w[:s]+"["+w[s]+"]"+w[s+1:]
        out.append((j,float(fr),mark))
    (j1,f1,w1),(j2,f2,w2)=out
    print(f"{D:2d}  {j1:4d}  {f1:.3f}   {w1:<26s} {j2:4d}  {f2:.3f}  {w2}")
