# Integer right triangles
# Problem 39
#
# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p <= 1000, is the number of solutions maximised?
#
# Answer: 840

# a^2 + b^2 = (p - a - b)^2
# p^2 - 2(a+b)p +2ab = 0
# p^2 = 2(p-a)(p-b)

from math import sqrt, trunc

MAX = 1000

p = 122
mp = 120
mc = 3
while p <= MAX:
  m = p*p/2
  k = 2
  l = trunc(sqrt(m))

  c = 0
  while k <= l:
    if m % k == 0:
      c += 1
    k += 1
    
  if c > mc:
    mp = p
    mc = c
  
  p += 2

print mp