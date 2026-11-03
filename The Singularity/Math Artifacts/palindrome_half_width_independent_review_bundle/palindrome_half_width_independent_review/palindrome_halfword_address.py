def reverse_bits(x,h):
    return int(format(x,f'0{h}b')[::-1],2) if h else 0

def rectangle(u,v,h):
    H=1<<h
    if u<=0 or v<=0:return 0
    if u>=H:return min(v,H)
    if v>=H:return min(u,H)
    a=format(u-1,f'0{h}b');b=format(v-1,f'0{h}b');states={(0,0):1}
    cmp=lambda x,y:(x>y)-(x<y)
    for j in range(h):
        new={}
        for (left,right),count in states.items():
            for bit in (0,1):
                key=(left or cmp(bit,int(a[j])),cmp(bit,int(b[h-1-j])) or right)
                new[key]=new.get(key,0)+count
        states=new
    return sum(c for (l,r),c in states.items() if l<=0 and r<=0)

def palindrome_word(n,u):
    m=(n+1)//2
    if not 0<=u<1<<m:raise ValueError('half-word out of range')
    prefix=format(u,f'0{m}b')
    return prefix+(prefix[::-1] if n%2==0 else prefix[:-1][::-1])

def palindrome_address(n,u):
    if n==1:return u
    m=(n+1)//2;H=1<<m
    if not 0<=u<H:raise ValueError('half-word out of range')
    if u>=H//2:return (1<<n)-1-palindrome_address(n,H-1-u)
    if n%2==0:
        B=reverse_bits(u,m)
        return u*H-u*(u-1)//2+B-rectangle(B,u+1,m)
    h=m-1;H0=1<<h;A=u>>1;c=u&1;B=reverse_bits(A,h)
    return 2*A*H0-A*(A-1)+c*(H0-A)+B-rectangle(B,A+1,h)
