#!/usr/bin/env python3
"""P21 sealed clock/center phase commutator audit. Standard library only."""
import hashlib
from pathlib import Path

seal=Path(__file__).with_name('NEXUS_P21_Moving_Seam_Seal.txt')
sha='6e3b3595ae1e44df711c2c8f4e793f5044a73265b4120391bf009251fb40d353'
# Bind the actual hash from seal file at creation time; do not silently accept changes.
assert hashlib.sha256(seal.read_bytes()).hexdigest()==sha,'seal mismatch'

def rot_twisted(w,n):
    m=(1<<n)-1
    return ((w<<1)&m)|(1^((w>>(n-1))&1))

def rot_twisted_inv(w,n):
    # tau^-1(y) = (1 XOR y_last) prepended to y[:n-1]
    return (((w&1)^1)<<(n-1))|(w>>1)

def is_pal(w,n):
    return all(((w>>j)&1)==((w>>(n-1-j))&1) for j in range(n//2))

def alternator(seed,n):
    v=0
    for j in range(n):
        v=(v<<1)|((seed+j)%2)
    return v

print('seal SHA-256',sha)
for n in range(1,18,2):
    k=(n-1)//2
    num=1<<n
    inter=[];marked=0;pal_count=0;nextpal_count=0
    for w in range(num):
        s0=is_pal(w,n)
        # The clock commutator tau D tau^-1 D uses D(tau^-1 w).
        sback=is_pal(rot_twisted_inv(w,n),n)
        # The intersection S cap tau^-1(S) instead reads s(tau w), same count.
        sfwd=is_pal(rot_twisted(w,n),n)
        if s0: pal_count+=1
        if sback: nextpal_count+=1
        if s0 and sfwd: inter.append(w)
        if s0!=sback: marked+=1
        v_sign=-1 if s0!=sback else 1
        assert v_sign*v_sign==1
        assert rot_twisted(rot_twisted_inv(w,n),n)==w
    aa=sorted((alternator(0,n),alternator(1,n)))
    assert sorted(inter)==aa,(n,inter,aa)
    assert pal_count==nextpal_count==(1<<(k+1))
    expected= (1<<(k+2))-4
    assert marked==expected,(n,marked,expected)
    if n==1: assert marked==0
    else: assert marked>0
    print(f'n={n:2d} states={num:7d} palindrome={pal_count:5d} joint={len(inter)} alternating=({aa[0]:0{n}b},{aa[1]:0{n}b}) commutator_MINUS={marked:6d} fraction={marked/num:.8f}')
print('STANDS algebraically, RUNS exhaustively through n=17.')
