"""Compiled native-frame runtimes for the original R2,R3,R4. ANF products are Boolean AND and sums are XOR."""

def forward_2(x):
    a=(x>>1)&1
    b=(x>>0)&1
    out_a=1 ^ a
    out_b=b ^ a
    return (out_a<<1) | (out_b<<0)

def inverse_2(x):
    a=(x>>1)&1
    b=(x>>0)&1
    out_a=1 ^ a
    out_b=1 ^ b ^ a
    return (out_a<<1) | (out_b<<0)

def forward_3(x):
    a=(x>>2)&1
    b=(x>>1)&1
    c=(x>>0)&1
    out_a=b ^ a
    out_b=c ^ b ^ a ^ (a & b)
    out_c=1 ^ c ^ b ^ (a & b)
    return (out_a<<2) | (out_b<<1) | (out_c<<0)

def inverse_3(x):
    a=(x>>2)&1
    b=(x>>1)&1
    c=(x>>0)&1
    out_a=1 ^ c ^ b
    out_b=1 ^ c ^ b ^ a
    out_c=1 ^ c ^ (a & c) ^ (a & b)
    return (out_a<<2) | (out_b<<1) | (out_c<<0)

def forward_4(x):
    a=(x>>3)&1
    b=(x>>2)&1
    c=(x>>1)&1
    d=(x>>0)&1
    out_a=b ^ a ^ (b & d) ^ (b & c)
    out_b=a ^ (c & d) ^ (b & d) ^ (b & c) ^ (a & d) ^ (a & b & d)
    out_c=d ^ c ^ a ^ (a & d) ^ (a & b) ^ (a & c & d) ^ (a & b & d) ^ (a & b & c)
    out_d=1 ^ d ^ b ^ (c & d) ^ (b & d) ^ (b & c) ^ (a & c) ^ (b & c & d) ^ (a & b & d) ^ (a & b & c)
    return (out_a<<3) | (out_b<<2) | (out_c<<1) | (out_d<<0)

def inverse_4(x):
    a=(x>>3)&1
    b=(x>>2)&1
    c=(x>>1)&1
    d=(x>>0)&1
    out_a=1 ^ d ^ c ^ a ^ (c & d) ^ (a & b) ^ (a & b & c)
    out_b=1 ^ d ^ c ^ (c & d) ^ (b & c) ^ (a & d) ^ (a & b) ^ (a & b & d)
    out_c=1 ^ d ^ c ^ b ^ a ^ (b & c) ^ (a & c) ^ (a & c & d) ^ (a & b & d) ^ (a & b & c)
    out_d=1 ^ d ^ b ^ a ^ (b & c) ^ (a & d) ^ (a & c) ^ (a & b) ^ (a & b & d) ^ (a & b & c)
    return (out_a<<3) | (out_b<<2) | (out_c<<1) | (out_d<<0)

def partner_word(n,x):
    r=int(format(x,f'0{n}b')[::-1],2)
    return r if r!=x else x^((1<<n)-1)

if __name__=='__main__':
    for n in (2,3,4):
        forward=globals()['forward_'+str(n)];inverse=globals()['inverse_'+str(n)]
        for x in range(1<<n):
            assert inverse(forward(x))==x
            assert partner_word(n,partner_word(n,x))==x
            assert partner_word(n,forward(partner_word(n,x)))==inverse(x)
        print('R'+str(n)+': complete reversible runtime passed')
