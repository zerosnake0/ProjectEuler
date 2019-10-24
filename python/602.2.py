M = 10**9+7

def C(N,K):
    s = 0
    sign = 1
    d = [1]*(N+2)
    for i in xrange(2,N+2):
        if i % 10000 == 0:
            print i
        for j in xrange(i-1,0,-1):
            d[j] = (d[j] + d[j-1]) % M
    
    for i in xrange(K):
        if i % 10000 == 1:
            print i, s
            
        s = s + sign * d[i] * pow(K-i, N, M)
        s = s % M
       
        sign = -sign

    return s % M
    
print C(100,40)
print C(10**7,4*10**6)
