# Consecutive prime sum
# Problem 50
#
# The prime 41, can be written as the sum of six consecutive primes:
#
#   41 = 2 + 3 + 5 + 7 + 11 + 13
#
# This is the longest sum of consecutive primes that adds to a prime below
# one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a
# prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most
# consecutive primes?
#
# Answer: 997651

MAX = 1000000

from prime import *
from time import clock

beg = clock()

l = primeListBelow(MAX)
ll = len(l)

r = 0
k = 21
S = sum(l[:k])
while S < MAX:
  S += l[k]
  k += 1

while r == 0 and k > 22:
  k -= 1
  S -= l[k]
  s = S
  i = k
  while s < MAX:
    if isPrime(s):
      r = s
      break
    s += l[i] - l[i-k]
    i += 1
  
print r, clock() - beg

  




