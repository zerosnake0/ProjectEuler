# Coded triangle numbers
# Problem 42
#
# The nth term of the sequence of triangle numbers is given by,
# tn = 1/2*n(n+1); so the first ten triangle numbers are:
#
#   1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value. For
# example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
# is a triangle number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
# containing nearly two-thousand common English words, how many are triangle
# words?
#
# Answer: 162

f = open('42_words.txt','r')
s = f.read()
f.close()

s = s.split(',')
n = []

for w in s:
  l = len(w)-1
  sum = 0
  for i in range(1,l):
    sum += ord(w[i]) - ord('A') + 1
  n.append(sum)
  
n.sort()

m = []
t = 1
k = 1
while True:
  if t > n[-1]:
    break
  m.append(t)
  k += 1
  t += k

c = 0
for sum in n:
  if sum in m:
    c += 1
    
print c