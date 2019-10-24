# Number spiral diagonals
# Problem 28
#
# Starting with the number 1 and moving to the right in a clockwise direction a
# 5 by 5 spiral is formed as follows:
#
#   21 22 23 24 25
#   20  7  8  9 10
#   19  6  1  2 11
#   18  5  4  3 12
#   17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
#
# Answer: 669171001

# (2*i+1)^2+((2*i+1)+1)*k, k=1,2,3,4
# sum = 4*(2*i+1)^2 +20*(i+1) = 16*i^2+36*i+24, i = 0, ... , (N-1)/2-1
#                             = 16*i^2+4*i+4, i = 1, ... , (N-1)/2
# SUM = 16 * n(n+1)(2n+1)/6 + 4 * n(n+1)/2 + 4 * n
# +1 for the 1 in the center

from util import sumofsquare

N = 1001
n = (N-1)/2
print 2*(8*sumofsquare(n)+n*(n+3))+1

