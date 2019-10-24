# Pandigital prime
# Problem 41
#
# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
# also prime.
#
# What is the largest n-digit pandigital prime that exists?
#
# Answer: 7652413

# 1~2, 1~3, 1~5, 1~6, 1~8, 1~9 sum divisable by 3
# we test 1~4, 1~7

from prime import isPrime

def f(n):
  if n == 1:
    return [1]
  
  l = f(n-1)
  r = []
  d = 1
  for i in range(n):
    for k in l:
      r.append(k/d * 10 * d + n*d + k%d)
    d *= 10
  return r

m = 0
for i in f(7):
  if i > m and isPrime(i):
    m = i

if m == 0:
  for i in f(4):
    if i > m and isPrime(i):
      m = i
    
print m