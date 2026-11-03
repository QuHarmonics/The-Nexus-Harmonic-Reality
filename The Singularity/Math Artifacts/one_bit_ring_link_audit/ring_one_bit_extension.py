def partner(word):
    r=word[::-1]
    return r if r!=word else ''.join('1' if b=='0' else '0' for b in word)

def canonical(word):
    return min(word,partner(word))

def inherited(word):
    return canonical('1'+word+'1')

def even_to_odd(word,middle):
    assert len(word)%2==0 and word==canonical(word)
    h=len(word)//2
    return word[:h]+str(middle)+word[h:]

def odd_to_even(word,branch):
    assert len(word)%2==1 and word==canonical(word)
    h=len(word)//2;middle=int(word[h]);parent=word[:h]+word[h+1:]
    if middle==1:
        return inherited(parent) if branch==0 else '0'+parent+'0'
    return '0'+parent+'1' if branch==0 else '0'+partner(parent)+'1'

def undo_odd_to_even(word):
    assert len(word)%2==0 and word==canonical(word)
    inside=word[1:-1]
    if word!=word[::-1] and word[0]==word[-1]=='1':
        parent=inside;middle=1;branch=0
    elif word==word[::-1] and word[:2]=='01':
        parent=''.join('1' if b=='0' else '0' for b in inside);middle=1;branch=0
    elif word[0]==word[-1]=='0':
        parent=inside;middle=1;branch=1
    elif word[0]=='0' and word[-1]=='1':
        middle=0
        if inside==canonical(inside):parent=inside;branch=0
        else:parent=partner(inside);branch=1
    else:
        raise AssertionError('outside canonical target grammar')
    return even_to_odd(parent,middle),branch

if __name__=='__main__':
    checks=0
    for L in range(4,13,2):
        for value in range(1<<L):
            word=format(value,f'0{L}b')
            if word!=canonical(word):continue
            for middle in (0,1):
                odd=even_to_odd(word,middle)
                for branch in (0,1):
                    target=odd_to_even(odd,branch)
                    assert undo_odd_to_even(target)==(odd,branch)
                    checks+=1
    print('Exact two-step return checks:',checks)
