# Largest palindrome product
# Problem 4
#
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 * 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# Answer: 906609

from math import sqrt
from math import trunc
from time import clock

def g(k):
  s = trunc(sqrt(k))
  m = max(100, k/1000+1)
  while(s >= m):
    if(k % s == 0):
      return k
    s -= 1
  return -1

def f():
  # abccba
  for i in range(999, 99, -1):
    a = i / 100
    b = (i / 10) % 10
    c = i % 10
    k = c * 100 + b * 10 + a
    k += i * 1000
    if(g(k) != -1):
      return k

  # abcba
  for i in range(99, 9, -1):
    for j in range(9, 0, -1):
      k = i / 10 + (i % 10) * 10
      k += i * 1000 + j * 100
      if(g(k) != -1):
        return k

  return -1
        
s = clock()
r = f()
e = clock()
print r, e-s

##########################
# Method 2 from overview #
##########################
def reverse(n):
  p = 0
  while (n > 0):
    p = p * 10 + n % 10
    n /= 10
  return p

def f2():
  m = 0
  a = 999
  while (a >= 100):
    if (a % 11 == 0):
      b = 999
      d = 1
    else:
      b = 990
      d = 11
    while (b >= a):
      c = a*b
      if (c <= m):
        break
      if (c == reverse(c)):
        m = c
        break
      b -= d
    a -= 1
  return m
  
s = clock()
r = f2()
e = clock()
print r, e-s
