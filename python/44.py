# Pentagon numbers
# Problem 44
#
# Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. The first ten
# pentagonal numbers are:
#
#   1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
#
# It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference,
# 70 - 22 = 48, is not pentagonal.
#
# Find the pair of pentagonal numbers, Pj and Pk, for which their sum and
# difference are pentagonal and D = |Pk - Pj| is minimised; what is the value
# of D?
#
# Answer: 5482660

# Pn = k(3k-1)/2
# 3k^2 - k - 2Pn = 0
#
# Pn+i - Pn = (6n+3i-1)i/2

from math import sqrt, trunc

i = 1
D = 0
while D == 0:
  d = i * (3*i-1)
  j = 1
  while True:
    if d % j == 0:
      n = d/j+1-3*j
      if n < 6:
        break
      if n % 6 == 0:
        n /= 6
        k = n+j
        sum = (k*(3*k-1)+n*(3*n-1))/2
        l = (1+trunc(sqrt(1+24*sum)))/6
        if 3*l*l-l-2*sum == 0:
          D = d/2
          break
    j += 1
  i += 1
  
print D