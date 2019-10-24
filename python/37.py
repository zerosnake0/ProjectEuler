# Truncatable primes
# Problem 37
#
# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and remain prime
# at each stage: 3797, 797, 97, and 7. Similarly we can work from right to
# left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to
# right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
#
# Answer: 748317

# the most left and the most right must be 2, 3, 5 or 7
from math import log10
from math import trunc

from prime import primeBoolList

N = 11
MAX = 1000000

def f(count, beg, end, sum):
  L = primeBoolList(end)
  i = beg
  while i <= end:
    k = trunc(log10(i))
    k = pow(10, k)
    f = i / k
    
    # check the most left digit
    if f not in (2,3,5,7):
      i += k
      continue
    
    # left to right
    j = i
    while L[j] and k > 0:
      j = j % k
      k /= 10
    if k == 0:
      # right to left
      j = i / 10
      while L[j] and j != 0:
        j /= 10
      if j == 0:
        sum += i
        count -= 1
        if count == 0:
          return sum
          
    # check the most right digit
    if i % 10 == 7:
      i += 6
    else:
      i += 2
  
  if N > 0:
    return f(count, end+1, end*10, sum)
  

print f(N, 23, MAX, 0)