# Prime permutations
# Problem 49
#
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
# increases by 3330, is unusual in two ways: (i) each of the three terms are
# prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this
# sequence?
#
# Answer: 296962999629

from prime import primeBoolList

def arePermutation(m,n):
  c = [0] * 10
  for i in range(4):
    c[m%10] += 1
    c[n%10] -= 1
    m /= 10
    n /= 10
  return c == [0] * 10
    

l = primeBoolList(9999)

i = 1001

while i <= 9999:
  if i != 1487 and l[i]:
    j = i+2
    k = i+4
    while k <= 9999:
      if l[j] and l[k]:
        if arePermutation(i,j) and arePermutation(i,k):
          print "%d%d%d" % (i,j,k)
        
      j += 2
      k += 4
    
  i += 2