"""Law tail words, exact zero sets (J = 2^(D-2-floor(2D/3))):
 D=3m+1: ring D-1 zeros {floor((3m-1)/2), 2m}        ring D zeros {m, floor(3m/2), 2m+1}
 D=3m  : ring D-1 zeros {floor((3m-2)/2), 2m-1}      ring D zeros {m, floor((3m-1)/2), 2m}
 reader lands on 2m (resp 2m-1) at ring D-1 and on m at ring D."""
from witness_Kd import word_at
def zeros(w): return {i for i,c in enumerate(w) if c=="0"}
bad=[]
for D in range(13, 76):
    if D%3==2: continue
    J = 1 << (D-2-(2*D)//3)
    w1 = word_at((1<<(D-2))+J, D-1); w2 = word_at((1<<(D-1))+2*J+1, D)
    if D%3==1:
        m=(D-1)//3; z1={(3*m-1)//2, 2*m};   z2={m, (3*m)//2, 2*m+1}
    else:
        m=D//3;     z1={(3*m-2)//2, 2*m-1}; z2={m, (3*m-1)//2, 2*m}
    if zeros(w1)!=z1 or zeros(w2)!=z2: bad.append((D,sorted(zeros(w1)),sorted(z1),sorted(zeros(w2)),sorted(z2)))
print("tail-word zero sets, D = 0,1 mod 3, 13..75:", "all exact" if not bad else bad[:5])
