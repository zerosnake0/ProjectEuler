# Factorial digit sum
# Problem 20
#
# n! means n x (n-1) x ... x 3 x 2 x 1
#
# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 
# 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!
#
# Answer: 648

N = 100
L = [1]
l = 1 # len(L)

i = 2
while i <= N:
  r = 0
  j = 0
  while j < l:
    L[j] = L[j] * i + r
    r = L[j] / 10
    L[j] = L[j] % 10
    j += 1
  while r > 0:
    L.append(r % 10)
    l += 1
    r /= 10
  i += 1
print sum(L)
