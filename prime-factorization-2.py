from math import sqrt

max_test = 2*(10**6)

# bprime[i] = 0                      if i is prime
#             one prime divisor of i if i is not prime
bprime = [(2-2*(i&1)) for i in xrange(max_test+1)]
bprime[2] = 0

# the even numbers are dealt, now the odd ones
i = 3
while i <= max_test:
    if bprime[i] == 0:
        j = i*i
        while j <= max_test:
            bprime[j] = i
            j += i*2
    i += 2
    
sum_divisor = [0 for i in xrange(max_test+1)]
i = 2
while i <= max_test:
    if bprime[i] == 0:
        sum_divisor[i] = i
    else:
        sum_divisor[i] = sum_divisor[i/bprime[i]] + bprime[i]
    i += 1
            
result = 0
num_tests = int(raw_input())

i = 0
while i < num_tests:
    test = int(raw_input())
    result += sum_divisor[test]
    i += 1
  
print result