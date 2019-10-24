# 10001st prime
# Problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
# that the 6th prime is 13.
#
# What is the 10001st prime number?
#
# Answer: 104743

from time import clock
from prime import *

max = 10001

def f1(n):
  if(n == 1):
    return 2
  c = 1
  a = 1
  while(c < max):
    a += 2
    if(isPrime(a)):
      c += 1
  return a

def f2(n):
  arr = primeList(n)
  return arr[-1]
    
t = 10
s = clock()
for i in range(t):
  r = f1(max)
e = clock()
print r, (e-s)/t    # 0.25

s = clock()
for i in range(t):
  r = f2(max)
e = clock()
print r, (e-s)/t    # 0.13
