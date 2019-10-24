# Special Pythagorean triplet
# Problem 9
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, 
# for which,
#
#   a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#
# Answer: 31875000


################################
#    a^2 + b^2 = (S - a - b)^2 #
# => 2(S - a)(S - b) = S^2     #
################################

from math import trunc
from math import sqrt

S = 1000

M = S*S/2
m = M/S
i = trunc(sqrt(M))
while i > m:
  if M % i == 0:
    a = 1000 - M/i
    b = 1000 - i
    c = 1000 - a - b
    print a*b*c
    break
  i -= 1