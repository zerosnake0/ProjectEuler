# Goldbach's other conjecture
# Problem 46
#
# It was proposed by Christian Goldbach that every odd composite number can be
# written as the sum of a prime and twice a square.
#
#   9 = 7 + 2 x 1^2
#   15 = 7 + 2 x 2^2
#   21 = 3 + 2 x 3^2
#   25 = 7 + 2 x 3^2
#   27 = 19 + 2 x 2^2
#   33 = 31 + 2 x 1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a
# prime and twice a square?
#
# Answer: 5777

from prime import isPrime

n = 3
while True:
  i = n
  k = 2
  while i > 0:
    if isPrime(i):
      break
    i -= k
    k += 4
  if i <= 0:
    print n
    break
  n += 2