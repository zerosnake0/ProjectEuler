# Longest Collatz sequence
# Problem 14
#
# The following iterative sequence is defined for the set of positive integers:
#
#   n -> n/2 (n is even)
#   n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
#   13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) 
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
#
# Answer: 837799

from time import clock

s = clock()

N = 1000000

l = [0 for i in range(N)]
l[1] = 1

def f(k):
  if l[k] == 0:
    j = k
    c = 0
    while True:
      if j % 2 == 0:
        j /= 2;
      else:
        j = j*3+1;
      c += 1
      if j < N:
        l[k] = c + f(j)
        break
  
  return l[k]

m = f(1)
r = 1 
i = 2
while i < N:
  t = f(i)
  if m < t:
    m = t
    r = i
  i += 1
e = clock()
print r,e-s
