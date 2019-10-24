# 1000-digit Fibonacci number
# Problem 25
#
# The Fibonacci sequence is defined by the recurrence relation:
#
#   F(n) = F(n-1) + F(n-2), where F(1) = 1 and F(2) = 1.
#
# Hence the first 12 terms will be:
#
#   F(1) = 1
#   F(2) = 1
#   F(3) = 2
#   F(4) = 3
#   F(5) = 5
#   F(6) = 8
#   F(7) = 13
#   F(8) = 21
#   F(9) = 34
#   F(10) = 55
#   F(11) = 89
#   F(12) = 144
#
# The 12th term, F(12), is the first term to contain three digits.
#
# What is the first term in the Fibonacci sequence to contain 1000 digits?
#
# Answer: 4782



def add(n1,n2):
  l1 = len(n1)
  l2 = len(n2)
  if l1 < l2:
    return add(n2,n1)
  r = 0
  i = 0
  n3 = []
  while i < l2:
    c = n1[i] + n2[i] + r
    r = c / 10
    n3.append(c%10)
    i += 1
  while i < l1:
    c = n1[i] + r
    r = c / 10
    n3.append(c%10)
    i += 1
  if r > 0:
    n3.append(r)
  return n3

L=1000
a = [1]
b = [1]

i = 1
while len(a) < L:
  c = add(a,b)
  a = b
  b = c
  i += 1
print i
