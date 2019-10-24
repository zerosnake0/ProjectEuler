# Lexicographic permutations
# Problem 24
#
# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1 and 2 are:
#
#   012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
# 5, 6, 7, 8 and 9?
#
# Answer: 2783915460

import math

N=10
M=1000000
m = math.factorial(N)
L=range(N)

M -= 1
l=0
for i in range(N):
  m /= N-i
  j = M/m
  M -= j*m
  l = l*10 + L[j]
  L = L[:j] + L[j+1:]

print l