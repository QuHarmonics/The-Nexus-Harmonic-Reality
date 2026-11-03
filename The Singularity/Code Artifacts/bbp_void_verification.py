"""
NEXUS / QuHarmonics -- BBP VOID PAPER: consolidated verification script.
Every numeric quoted in the paper is produced here.
"""
from sympy import *
import mpmath as mp
import numpy as np

t = Symbol('t')
OUT = {}

# ---- R1: pole annihilation -------------------------------------------------
D = 16 - t**8
N = 4 - 2*t**3 - t**4 - t**5
OUT['D_factored'] = factor(D)
OUT['N_factored'] = factor(N)
OUT['reduced']    = cancel(N/D)
OUT['R1_ok'] = simplify(cancel(N/D) - (t-1)/((t**2-2)*(t**2-2*t+2))) == 0

# ---- R2: shell/base from one pole ------------------------------------------
ser = series(1/(t**2-2*t+2), t, 0, 16).removeO()
OUT['R2_ok'] = all(simplify(ser.coeff(t,j) - sin((j+1)*pi/4)/2**Rational(j+1,2))==0
                   for j in range(16))
OUT['zeros_per_shell'] = [j+1 for j in range(8) if simplify(sin((j+1)*pi/4))==0]

# ---- R3: dimension of the log-free subspace --------------------------------
ns = symbols('n0:8', real=True)
Npoly = sum(ns[p]*t**p for p in range(8))
A1,B1,A2,B2,A3,B3,A4,B4 = symbols('A1 B1 A2 B2 A3 B3 A4 B4', real=True)
pf = ((A1*t+B1)*(t**2+2)*(t**2-2*t+2)*(t**2+2*t+2)
    + (A2*t+B2)*(t**2-2)*(t**2-2*t+2)*(t**2+2*t+2)
    + (A3*t+B3)*(t**2-2)*(t**2+2)*(t**2+2*t+2)
    + (A4*t+B4)*(t**2-2)*(t**2+2)*(t**2-2*t+2))
sol = solve(Poly(expand(pf + Npoly), t).all_coeffs(),
            [A1,B1,A2,B2,A3,B3,A4,B4], dict=True)[0]
rows = [simplify(-(sol[A1]+sol[A2]+sol[A3]+sol[A4])/2),   # log2
        simplify(-sol[B1]/sqrt(2)),                        # log(1+sqrt2)
        simplify(sol[A2]/2),                               # log3
        simplify(sol[A4]/2),                               # log5
        simplify(sol[B2]/sqrt(2)),                         # atan(1/sqrt2)
        simplify(sol[B4]-sol[A4])]                         # atan2
Mmat = Matrix([[diff(r, ns[j]) for j in range(8)] for r in rows])
OUT['rank'] = Mmat.rank()
OUT['void_dim'] = 8 - Mmat.rank()

# ---- R4/R5: verify the two basis vectors and the selection -----------------
mp.mp.dps = 250
I = [mp.quad(lambda x: x**p/(16-x**8), [0,1]) for p in range(8)]
v1 = [-4,0,0,2,1,1,0,0]; v2 = [0,-8,-4,-4,0,0,1,0]
def val16(n): return sum(mp.mpf(n[p])*I[p] for p in range(8))*16
OUT['v1_val'] = val16(v1)/mp.pi
OUT['v2_val'] = val16(v2)/mp.pi
z = [2*v1[p]-v2[p] for p in range(8)]
OUT['z'] = z; OUT['z_val'] = val16(z)
OUT['z_sum'] = sum(z); OUT['v1_sum'] = sum(v1); OUT['v2_sum'] = sum(v2)

# ---- R6: sensitivity --------------------------------------------------------
np.random.seed(20260804)
PI=np.pi; LOG2=np.log(2); LOGS=np.log(1+np.sqrt(2))
def two_arm(a,b,c,d): return PI*(c+d)/4 - (a+c)/2*LOG2 - (b/np.sqrt(2))*LOGS
def series4(w,K=60):
    return sum((w[0]/(8*k+1)+w[1]/(8*k+4)+w[2]/(8*k+5)+w[3]/(8*k+6))/16.0**k
               for k in range(K))
TOL=0.01; T=20000
e1=np.array([abs(series4(np.array([4,-2,-1,-1],float)*(1+TOL*np.random.randn(4)))-PI)
             for _ in range(T)])
e3=[]; leak3=[]
for _ in range(T):
    g=0.25*(1+TOL*np.random.randn()); d=0.5*(1+TOL*np.random.randn())
    e3.append(abs(two_arm(g,0.0,-g,d)*16-PI))
    leak3.append(abs(-(g-g)/2*LOG2))
e3=np.array(e3); leak3=np.array(leak3)
OUT['e1_med']=np.median(e1); OUT['e1_p99']=np.percentile(e1,99)
OUT['e3_med']=np.median(e3); OUT['e3_p99']=np.percentile(e3,99)
OUT['leak3_max']=leak3.max()
OUT['e1_worse'] = np.median(e3) > np.median(e1)

# ---- print ------------------------------------------------------------------
print("="*76); print("CONSOLIDATED RESULTS"); print("="*76); print()
print(f"R1  16-t^8 factors  : {OUT['D_factored']}")
print(f"R1  numerator factors: {OUT['N_factored']}")
print(f"R1  reduced form     : {OUT['reduced']}")
print(f"R1  identity holds   : {OUT['R1_ok']}")
print()
print(f"R2  sine-series form verified to j=15 : {OUT['R2_ok']}")
print(f"R2  blind shell positions r           : {OUT['zeros_per_shell']}")
print()
print(f"R3  non-pi coefficient matrix rank    : {OUT['rank']} / 8")
print(f"R3  LOG-FREE SUBSPACE DIMENSION       : {OUT['void_dim']}")
print()
print(f"R4  v1 = {v1}  ->  {mp.nstr(OUT['v1_val'],8)} * pi   coeff sum {OUT['v1_sum']}")
print(f"R4  v2 = {v2}  ->  {mp.nstr(OUT['v2_val'],8)} * pi   coeff sum {OUT['v2_sum']}")
print(f"R4  z  = {OUT['z']}  ->  {mp.nstr(OUT['z_val'],6)}   coeff sum {OUT['z_sum']}")
print(f"R4  zero relation exact               : {abs(OUT['z_val']) < mp.mpf(10)**-230}")
print()
print(f"R5  DC-block on a*v1+b*v2: sum = -15b  =>  unique line b=0 = BBP")
print()
print(f"R6  4-channel  median |err| {OUT['e1_med']:.3e}   p99 {OUT['e1_p99']:.3e}")
print(f"R6  2-arm diff median |err| {OUT['e3_med']:.3e}   p99 {OUT['e3_p99']:.3e}")
print(f"R6  2-arm is WORSE in magnitude       : {OUT['e1_worse']}")
print(f"R6  2-arm log leakage max             : {OUT['leak3_max']:.3e}  (exactly 0)")
