# -*- coding: UTF-8 -*-

def pow(a, b):
  if(b == 0):
    return 1
  if(b == 1):
    return a
  r = pow(a, b/2)
  r *= r
  if(b % 2 == 1):
    r *= a
  return r
    
def pgcd(a, b):
  if(a < b):
    return pgcd(b, a)
  if(b == 0):
    return a
  return pgcd(b, a % b)

  
def combination(n, k):
  l = n - k
  if l > k:
    return combination(n, l)
  r = 1
  i = n
  while i > k:
    r *= i
    i -= 1
  i = 2
  while i <= l:
    r /= i
    i += 1
  return r
  
# sum(n^2) = n(n+1)(2n+1)/6
def sumofsquare(n):
  return n*(n+1)*(2*n+1)/6
