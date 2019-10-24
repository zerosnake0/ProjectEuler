# Counting Sundays
# Problem 19
#
# You are given the following information, but you may prefer to do some
# research for yourself.
#
#   * 1 Jan 1900 was a Monday.
#   * Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#   * A leap year occurs on any year evenly divisible by 4, but not on a century
#     unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century 
# (1 Jan 1901 to 31 Dec 2000)?
#
# Answer: 171

d = 365 + 1
y = 1901
m = 1
l = [31,28,31,30,31,30,
     31,31,30,31,30,31]

c = 0
while y < 2001:
  for i in range(12):
    if d % 7 == 0:
      c += 1
    d += l[i]
    if i == 1:
      if (y % 400 == 0) or ((y % 4 == 0) and (y % 100 != 0)):
        d += 1
  y += 1
print c
