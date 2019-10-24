# Champernowne's constant
# Problem 40
#
# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
#
# Answer: 210

MAX = 1000000

i = 1
s = "."
while len(s) <= MAX+1:
  s += str(i)
  i += 1

m = 1
k = 1
while k <= MAX:
  m *= int(s[k])
  k *= 10
  
print m
