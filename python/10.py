# Summation of primes
# Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#
# Answer: 142913828922

from prime import *

M = 2000000
arr = primeBoolList(M-1)
r = 2
i = 3
while i < M:
  if arr[i]:
    r += i
  i += 2
print r