# Circular primes
# Problem 35
#
# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
# 73, 79, and 97.
#
# How many circular primes are there below one million?
#
# Answer: 55

from math import trunc
from math import log10

from prime import primeBoolList
from util import pow

N = 1000000
L = primeBoolList(N)

def rotate(n):
  k = trunc(log10(n))
  if k == 0:
    return n
  return n/10 + n%10 * pow(10,k)
  
s = 0
for i in range(2,N+1):
  if L[i]:
    c = 1
    k = rotate(i)
    while k != i and L[k]:
      c += 1
      L[k] = False
      k = rotate(k)
    if k == i:
      s += c

print s
      