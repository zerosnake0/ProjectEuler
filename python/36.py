# Double-base palindromes
# Problem 36
#
# The decimal number, 585 = 1001001001_2(binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include
# leading zeros.)
#
# Answer: 872187

MAX=1000000

def f(n,k):
  m = []
  while n > 0:
    m.append(n%k)
    n /= k
  l = len(m)
  for i in range(l/2):
    if m[i] != m[l-1-i]:
      return False
  return True
  
i = 0
s = 0
while i < MAX:
  if f(i,10) and f(i,2):
    s += i
  i += 1
print s