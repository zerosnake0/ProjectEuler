# Digit factorials
# Problem 34
#
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
#
# Answer: 40730

N = 10
l = [1]
for i in range(1,10):
  l.append(l[-1]*i)
m = l[9]
k = m*2

while k > N:
  N *= 10
  k += m
k -= m
  
S = 0
i = 3
while i <= k:
  j = i
  s = 0
  while j > 0:
    r = j%10
    j /= 10
    s += l[r]
    if s > i:
      break
  if s == i:
    S += s
  i += 1
  
print S
