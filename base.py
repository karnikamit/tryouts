def base(n, k):
    '''
    	base(decimal no, base(2,16))
        
        base 2 for binary
        base 16 for Hex
    '''
    if k == 2:
        base = []
        b = n%2
        base.append(b)
        while n > 1:
            n //=  2    #Floor division by the base
            a = n%2     #Getting the remainder
            base.append(a)
            
        base.reverse()
    if k == 16:
        base16 = {0:0}
        for i in range(1,10):
            base16[i] = i
        alph = ['A', 'B', 'C', 'D', 'E', 'F']
        for i in range(len(alph)):
            base16[i+10] = alph[i]
        base = []
        b = n%k
        if b in base16:
            base.append(base16[b])
        while n > 1:
            n //=  k
            a = n%k
            if a in base16:
                base.append(base16[a])
                      
        base.reverse()
    print (base)

