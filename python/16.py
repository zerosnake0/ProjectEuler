# Power digit sum
# Problem 16
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?
#
# Answer: 1366

l = [1]
j = 1 # len(l)

k = 0
while k < 1000:
  r = 0
  i = 0
  while i < j:
    l[i] = l[i] * 2 + r
    if l[i] > 9:
      l[i] -= 10
      r = 1
    else:
      r = 0
    i += 1
  if r > 0:
    l.append(1)
    j += 1
  k += 1
  
print sum(l)
