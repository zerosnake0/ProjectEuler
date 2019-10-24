# Pandigital products
# Problem 32
#
# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
# through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
# multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only
# include it once in your sum.
#
# Answer: 45228

# 99*99=9801    8 digits
# 100*100=10000 11 digits
# so we can only have xx*xxx=xxxx
#                  or x*xxxx=xxxx

D = {}

def f(a,b,c,d):
  i = a
  while i <= b:
    j = c
    while j <= d:
      m = i*j
      if m > 9876:
        break
      l = 0
      for k in (i,j,m):
        while k != 0:
          r = k%10
          l |= 1<<r
          k /= 10
      if l == (1<<10)-2:
        D[m] = 1
      j += 1
    i += 1

f(12,98,123,987)
f(2,9,1234,9876)

s = 0
for i in D:
  s += i
print s
  
