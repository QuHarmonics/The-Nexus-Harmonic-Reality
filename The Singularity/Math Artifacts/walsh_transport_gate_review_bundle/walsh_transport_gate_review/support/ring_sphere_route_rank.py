import math
from functools import lru_cache

def partner(word):
    r=word[::-1]
    return r if r!=word else ''.join('1' if b=='0' else '0' for b in word)
def canonical(word):return min(word,partner(word))
def insert_middle(word,m):
    h=len(word)//2
    return word[:h]+str(m)+word[h:]
def lift(odd,d):
    h=len(odd)//2;m=int(odd[h]);x=odd[:h]+odd[h+1:]
    if d==0:return canonical(str(m)+x+str(m))
    return '0'+(partner(x) if m else x)+'1'
def undo_even(word):
    inside=word[1:-1]
    if word!=word[::-1] and word[0]==word[-1]=='1':x=inside;m=1;d=0
    elif word==word[::-1] and word[:2]=='01':
        x=''.join('1' if b=='0' else '0' for b in inside);m=1;d=0
    elif word[0]==word[-1]=='0':x=inside;m=0;d=0
    elif word[0]=='0' and word[-1]=='1':
        m=0 if inside==canonical(inside) else 1;x=inside if m==0 else partner(inside);d=1
    else:raise ValueError('noncanonical even word')
    return insert_middle(x,m),d

def encode(word):
    a=canonical(word);side=int(a!=word);reverse_route=[]
    while len(a)>1:
        n=len(a)
        if n==2:reverse_route.append(a[1]);a='0'
        elif n%2:
            h=n//2;reverse_route.append(a[h]);a=a[:h]+a[h+1:]
        else:a,d=undo_even(a);reverse_route.append(str(d))
    return ''.join(reversed(reverse_route)),side

def decode(route,side):
    a='0';twice_z=-1
    for b in route:
        bit=int(b);n=len(a)
        if n==1:a='0'+b;twice_z+=2*bit-1
        elif n%2==0:a=insert_middle(a,bit);twice_z+=2*bit-1
        else:
            h=n//2;m=int(a[h]);x=a[:h]+a[h+1:]
            s=-1 if m==1 and x==x[::-1] else 1
            twice_z=s*(twice_z+(2*m-1)*(-1 if bit else 1));a=lift(a,bit)
    if side:
        if a==a[::-1]:twice_z=-twice_z
        a=partner(a)
    assert twice_z==2*a.count('1')-len(a)
    return a,twice_z/2

@lru_cache(maxsize=16384)
def weighted_prefix(n,t):
    if t<=0:return (0,)*(n+1),(0,)*(n+1)
    t=min(t,1<<n);bound=format(t-1,f'0{n}b')
    cmp=lambda a,b:(a>b)-(a<b);states={(0,0,0,-1,0):1}
    for i in range(n//2):
        new={}
        for (cl,cr,mirror,first,w),count in states.items():
            for a in (0,1):
                for b in (0,1):
                    key=(cl or cmp(a,int(bound[i])),cmp(b,int(bound[n-1-i])) or cr,
                         mirror or cmp(a,b),a if i==0 else first,w+a+b)
                    new[key]=new.get(key,0)+count
        states=new
    C=[0]*(n+1);T=[0]*(n+1)
    for (cl,cr,mirror,first,w),count in states.items():
        for center in ((0,1) if n%2 else (None,)):
            order=cl
            if n%2:order=order or cmp(center,int(bound[n//2]))
            order=order or cr;leading=center if n==1 else first
            weight=w+(center if center is not None else 0)
            if order<=0 and (mirror<0 or (mirror==0 and leading==0)):
                C[weight]+=count
                if mirror==0:T[weight]+=count
    return tuple(C),tuple(T)

def location(word):
    n=len(word);a=canonical(word);r=sum(weighted_prefix(n,int(a,2))[0]);N=1<<n;M=N//2
    i=r if word==a else N-1-r
    return N-1-i if n>1 and i in (M-1,M) else i

def band_rank(word):
    n=len(word);w=word.count('1');i=location(word)
    if n==1:return 0
    N=1<<n;M=N//2;C,T=weighted_prefix(n,N)
    largest='1'*(n//2-1)+'0'+'1'*((n+1)//2)
    wa=largest.count('1');wp=partner(largest).count('1')
    if i<M-1:return weighted_prefix(n,int(word,2))[0][w]
    if i==M-1:return C[w]-int(wa==w)
    if i==M:return C[w]-int(wa==w)+int(wp==w)
    a=partner(word);c,t=weighted_prefix(n,int(a,2)+1)
    H=c[w]-t[w]+t[n-w]
    return math.comb(n,w)-H

def route_to_coordinates(route,side):
    word,z=decode(route,side)
    return {'word':word,'n':len(word),'z':z,'ring_position':location(word),'within_latitude_rank':band_rank(word)}
