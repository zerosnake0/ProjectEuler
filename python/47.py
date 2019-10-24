# Distinct primes factors
# Problem 47
#
# The first two consecutive numbers to have two distinct prime factors are:
#
#   14 = 2 x 7
#   15 = 3 x 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
#   644 = 2^2 x 7 x 23
#   645 = 3 x 5 x 43
#   646 = 2 x 17 x 19.
#
# Find the first four consecutive integers to have four distinct prime factors.
# What is the first of these numbers?
#
# Answer: 134043

from time import clock

N = 4

# method 1, much faster
beg = clock()
l = 200000

def f(l):
  print l
  p = [0] * l
  r = -1
  i = 2
  count = 0
  while i < l:
    if p[i] == N:
      if count == N - 1:
        r = i - N + 1
        break
      count += 1
    else:
      count = 0
      if p[i] == 0:
        j = i+i
        while j < l:
          p[j] += 1
          j += i
    i += 1
  
  if r != -1:
    return r
  else:
    return f(l*10)
  
print f(l), clock()-beg    

# method 2
beg = clock()

p = [2]

n = 3
count = 0
r = -1
while True:
  i = n
  c = 0
  l = []
  for j in p:
    if j > i:
      break
    if i % j == 0:
      l.append(j)
      c += 1
      i /= j
      while i % j == 0:
        i /= j
  if c == N:
    if count == N - 1:
      r = n - N + 1
      break
    count += 1
  else:
    count = 0
    if c == 0:
      p.append(n)
  
  n += 1
  
print r, clock()-beg
