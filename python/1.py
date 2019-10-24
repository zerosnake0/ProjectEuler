# Multiples of 3 and 5
# Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# Answer: 233168

max = 1000 - 1
a = 3; b = 5
c = a * b

def f(k):
  return (1 + k) * k / 2

res = f(max / a) * a + f(max / b) * b - f(max / c) * c

print res
