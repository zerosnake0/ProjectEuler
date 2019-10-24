# Largest prime factor
# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
# Answer: 6857

from math import sqrt
from math import trunc
from time import clock

nb = 600851475143

def g(n):
  """ n is odd """ 
  a = trunc(sqrt(n))
  if(a % 2 == 0):
    a -= 1
  while(n % a != 0):
    a -= 2
  if(a == 1):
    return n
  while(n % a == 0):
    n /= a
  b = g(n)
  if(b >= a):
    return b
  return max(g(a), b)
    
def f(n):
  while(n & 1 == 0):
    n >>= 1
  if(n == 1):
    return 2
  return g(n)

print f(nb)

# t = 10
# s = clock()
# for i in range(t):
#   r = f(nb)
# e = clock()
# print r, (e-s)/t
