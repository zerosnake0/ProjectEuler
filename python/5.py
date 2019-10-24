# Smallest multiple
# Problem 5
#
# 2520 is the smallest number that can be divided by each of the numbers from 
# 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?
#
# Anser: 232792560

from math import log
from math import trunc
from time import clock

from prime import primeBoolList
from util import pow
from util import pgcd

def f1(n):
  arr = primeBoolList(n)

  pdt = pow(2, trunc(log(n, 2)));

  for i in range(3, n+1, 2):
    if(arr[i]):
      k = trunc(log(n, i))
      pdt *= pow(i, k)
            
  return pdt

def f2(n):
  pdt = 1;
  for i in range(2, n+1):
    pdt *= i / pgcd(pdt, i)
  return pdt
    
max = 20
t = 10000

s = clock()
for i in range(t):
  r = f1(max)
e = clock()
print r, (e-s)/t    # 2.65e-5
                
s = clock()
for i in range(t):
  r = f2(max)
e = clock()
print r, (e-s)/t    # 2.10e-5


max = 100
t = 10000

s = clock()
for i in range(t):
  r = f1(max)
e = clock()
print r, (e-s)/t    # 8.55e-5
                
s = clock()
for i in range(t):
  r = f2(max)
e = clock()
print r, (e-s)/t    # 1.83e-4
