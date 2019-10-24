# Coin sums
# Problem 31
#
# In England the currency is made up of pound, f, and pence, p, and there are
# eight coins in general circulation:
#
#   1p, 2p, 5p, 10p, 20p, 50p, f1 (100p) and f2 (200p).
#
# It is possible to make f2 in the following way:
#
# 1xf1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
#
# How many different ways can f2 be made using any number of coins?
#
# Answer: 73682

S = 200
L = [1,2,5,10,20,50,100,200]

def g(s,l,i):
  if s == 0:
    return 1
    
  if i < 0:
    return 0
    
  r = 0
  m = 0
  while m <= s:
    r += g(s-m, l, i-1)
    m += l[i]
    
  return r

def f(s,l):
  return g(s,l,len(l)-1)
  
print f(S,L)
  