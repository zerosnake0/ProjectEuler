# Names scores
# Problem 22
#
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name
# score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
# would obtain a score of 938 x 53 = 49714.
#
# What is the total of all the name scores in the file?
#
# Answer: 871198282

f=open('22_names.txt','r')
s=f.read()
f.close()

s=s.split(',')
s.sort()

k = 1
sum = 0
for i in s:
  l = len(i) - 1
  j = 1
  r = 0
  while j < l:
    r += ord(i[j]) - ord('A') + 1
    j += 1
  sum += r * k
  k += 1
  
print sum

