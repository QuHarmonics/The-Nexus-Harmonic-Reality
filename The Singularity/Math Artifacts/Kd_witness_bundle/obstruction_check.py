from fractions import Fraction as F
from witness_Kd import word_at, A_profile, qD
def cf(L, j):
    a = L // 2
    if j == 0: return "1"*(a-1)+"0"+"1"*(L-a)                    # C_L
    if L % 2 == 0:
        return {1:"1"*(a+1)+"0"+"1"*(a-2), 2:"1"*(a-1)+"010"+"1"*(a-2), 3:"1"*a+"00"+"1"*(a-2)}[j]
    return {1:"1"*a+"00"+"1"*(a-1), 2:"1"*(a+2)+"0"+"1"*(a-2), 3:"1"*(a-1)+"0110"+"1"*(a-2)}[j]
bad=[(L,j) for L in range(7,41) for j in range(4) if word_at((1<<(L-1))+j, L)!=cf(L,j)]
print("closed forms word(M+j), j=0..3, L=7..40:", "all hold" if not bad else f"FAIL {bad[:8]}")
bad6=[j for j in range(4) if word_at(32+j,6)!=cf(6,j)]
print("  L=6:", "holds" if not bad6 else f"fails at j={bad6}")
print("\nobstruction: A_{q_D} within 2^-(D-2) of the seam (both sides)")
half=F(1,2)
for D in range(8, 23):
    w=F(1,1<<(D-2))
    n=len(A_profile(qD(D), D, lo=half-w, hi=half+w))
    print(f"  D={D:2d}: components in (1/2 - 2^-{D-2}, 1/2 + 2^-{D-2}) = {n}")
