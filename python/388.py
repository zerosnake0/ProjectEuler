# Distinct Lines
# Problem 388
#
# Consider all lattice points (a,b,c) with 0 <= a,b,c <= N.
#
# From the origin O(0,0,0) all lines are drawn to the other lattice points.
# Let D(N) be the number of distinct such lines.
#
# You are given that D(1 000 000) = 831 909 254 469 114 121.
#
# Find D(10^10). Give as your answer the first nine digits followed by the last
# nine digits.

from util import pow

N = 1000000
r = 0
a = 0
while a <= N:
  b = 0
  while b < a:
    c = 0
    while c < b:
      c += 1
    b += 1
  a += 1
  if a % 1000 == 0:
    print a,b,c

    
# a <= b <= c:
#
#   a < b < c (8)
#   a = b < c (3)
#   a = b = c (1)
#   a < b = c (3)