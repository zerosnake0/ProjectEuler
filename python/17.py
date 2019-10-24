# Number letter counts
# Problem 17
#
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out 
# in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 
# letters. The use of "and" when writing out numbers is in compliance with British usage.
#
# Answer: 21124

l=["zero","one","two","three","four",
   "five","six","seven","eight","nine",
   "ten","eleven","twelve","thirteen","fourteen",
   "fifteen","sixteen","seventeen","eighteen","nighteen"]
l2=["twenty","thrity","forty","fifty",
    "sixty","seventy","eighty","nighty"]
    
# 1~9
r1 = 0
for i in range(1, 10):
  r1 += len(l[i])

# 10~19
r2 = 0
for i in range(10, 20):
  r2 += len(l[i])

r3 = 0
# 20,30,40,50,60,70,80,90
for i in l2:
  r3 += len(i)
# 1~99
r3 = r1 + r2 + r3 * 10 + r1 * len(l2)

r4 = (r1 + 9 * len("hundred")) * 100 + len("and") * 9 * 99
r4 += r3 * 10 + len(l[1]) + len("thousand")

print r4
