# Self powers
# Problem 48
#
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
#
# Answer: 9110846700

MAX = 1000
N = pow(10,10)

def pow(a, b, n):
  if(b == 0):
    return 1
  if(b == 1):
    return a % n
  r = pow(a, b/2, n)
  r *= r
  if(b % 2 == 1):
    r *= a
  return r % n

s = 0
i = 1
while i <= MAX:
  s += pow(i,i,N)
  i += 1
  
print s % N