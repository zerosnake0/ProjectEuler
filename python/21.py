# Amicable numbers
# Problem 21
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
# each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 
# 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 
# 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.
#
# Answer: 31626

N = 10000
l = [1 for i in range(N)]

i = 2
while i < (N+1)/2:
  j = i*2
  while j < N:
    l[j] += i
    j += i
  i += 1
  
i = 2
s = 0
while i < N:
  j = l[i]
  if j > i and j < N and i == l[j]:
    s += i + j
  i += 1

print s
