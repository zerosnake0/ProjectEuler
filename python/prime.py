# -*- coding: UTF-8 -*-

from math import sqrt
from math import trunc

# input : integer N
# output : True if N is prime, False if not
def isPrime(n):
  if(n == 2):
    return True
  if(n <= 1 or n&1 == 0):
    return False
  k = 3
  m = trunc(sqrt(n))
  while(k <= m):
    if(n % k == 0):
      return False
    k += 2
  return True

# input : integer N
# output : L, a list of N+1 boolean, L[k] is True if k is prime, False if not
def primeBoolList(n):
  arr = [(i&1 != 0) for i in range(n+1)]
  arr[1] = False
  arr[2] = True
  for i in range(3, n+1, 2):
    if(arr[i]):
      for j in range(i * i, n+1, i):
        arr[j] = False
  return arr

# input : integer N
# output : L, a list of N first primes
def primeList(n):
  arr = []
  if(n > 0):
    arr.append(2)
    c = 1
    k = 3
    while(c < n):
      a = trunc(sqrt(k))
      b = True
      for i in arr:   # dont use for i in range(c), much slower!!!
                      # iter() with next() faster than index 
                      # but also slower than this
        if(i > a):
          break
        if(k % i == 0):
          b = False
          break
      if(b):
        arr.append(k)
        c += 1
      k += 2
        
  return arr

# input : integer N
# output : L, a list of all primes less than N
def primeListBelow(n):
  arr = []
  if(n > 2):
    arr.append(2)
    k = 3
    while(k < n):
      a = trunc(sqrt(k))
      b = True
      for i in arr:   # dont use for i in range(c), much slower!!!
                      # iter() with next() faster than index 
                      # but also slower than this
        if(i > a):
          break
        if(k % i == 0):
          b = False
          break
      if(b):
        arr.append(k)
      k += 2

  return arr
