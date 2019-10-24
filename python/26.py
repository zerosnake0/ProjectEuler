# Reciprocal cycles
# Problem 26
#
# A unit fraction contains 1 in the numerator. The decimal representation of
# the unit fractions with denominators 2 to 10 are given:
#
#   1/2  = 0.5
#   1/3  = 0.(3)
#   1/4  = 0.25
#   1/5  = 0.2
#   1/6  = 0.1(6)
#   1/7  = 0.(142857)
#   1/8  = 0.125
#   1/9	 = 0.(1)
#   1/10 = 0.1
#
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
# seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle
# in its decimal fraction part.
#
# Answer: 983

#  1/n = m / ((999...9) * 10^k)
# 10/n = m / ((999...9) * 10^(k-1))
# if n can be evenly divided by 2 or 5, then it has the same cycle length as 
# n/2 or n/5, which should be less than n, so there's no need to check n when
# it's a multiplier of 2 or 5. Therefore we have only 1/n = 0.(?...?)
D = 1000
mc = 0
md = 2
for d in range(3,D):
  if d % 2 != 0 and d % 5 != 0:
    k = 0
    r = 10
    while True:
      r = (r%d)*10
      k += 1
      if r == 10:
        break
    if k > mc:
      mc = k
      md = d
print md
    