# Digit cancelling fractions
# Problem 33
#
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician
# in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which
# is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less
# than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.
#
# Answer: 100

from util import pgcd

N=1
D=1
for i in range(1,10):
  for j in range(1,10):
    if i != j:
      for k in range(1,10):
        n = i*10+j
        d = j*10+k
        if n*k == d*i:
          N *= i
          D *= k

print D/pgcd(N,D)