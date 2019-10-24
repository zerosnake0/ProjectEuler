M = 10**9+7 # is a prime

def C(N,K):
    s = 0
    sign = 1
    c = 1

    for i in xrange(K):
        if i % 10000 == 1:
            print i, s

        s += sign * c * pow(K-i, N, M)
        s %= M

        # See inverse modulo
        c = c * (N + 1 - i) * pow(i + 1, M-2, M)
        c %= M
        sign = -sign

    return s % M

print C(100,40)
print C(10**7,4*10**6)
