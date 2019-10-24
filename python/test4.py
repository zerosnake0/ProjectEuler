# Enter your code here. Read input from STDIN. Print output to STDOUT
from time import clock
beg = clock()

from math import sqrt

num_tests = int(raw_input())

tests = []
for i in xrange(num_tests):
    tests.append(int(raw_input()))

tests.sort()
    
maxroot = 2*10**6
bprime = [bool(i&1) for i in xrange(maxroot)]   # the even numbers greater than 2 are not prime
bprime[2] = 1

sum_advisors = 0

for i in xrange(2,maxroot):
    if bprime[i]:
        # update the bool prime list
        for j in xrange(i*i,maxroot,i):
            bprime[j] = 0

print sum_advisors

print clock() - beg