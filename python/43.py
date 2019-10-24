# Sub-string divisibility
# Problem 43
#
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up
# of each of the digits 0 to 9 in some order, but it also has a rather
# interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
#   d2d3d4=406 is divisible by 2
#   d3d4d5=063 is divisible by 3
#   d4d5d6=635 is divisible by 5
#   d5d6d7=357 is divisible by 7
#   d6d7d8=572 is divisible by 11
#   d7d8d9=728 is divisible by 13
#   d8d9d10=289 is divisible by 17
#
# Find the sum of all 0 to 9 pandigital numbers with this property.
#
# Answer: 16695334890

# d2d3d4 divisible by 2 => d4 in (0,2,4,6,8)
# d3d4d5 divisible by 3 => d3+d4+d5 divisible by 3
# d4d5d6 divisible by 5 => d6 in (0,5)

# the code is a bit ugly but it will be too slow if we use a method similar to problem 41
s = 0
for d1 in range(1,10):
  f1 = 1<<d1
  for d2 in range(10):
    f2 = 1<<d2
    if (f1&f2):
      continue
    f2 |= f1
    for d3 in range(10):
      f3 = 1<<d3
      if (f2&f3):
        continue
      f3 |= f2
      for d4 in range(0,10,2):
        f4 = 1<<d4
        if (f3&f4):
          continue
        f4 |= f3
        for d5 in range(10):
          f5 = 1<<d5
          if (f4&f5):
            continue
          if (d3+d4+d5)%3 != 0:
            continue
          f5 |= f4
          for d6 in (0,5):
            f6 = 1<<d6
            if (f5&f6):
              continue
            f6 |= f5
            for d7 in range(10):
              f7 = 1<<d7
              if (f6&f7):
                continue
              if (100*d5+10*d6+d7)%7 != 0:
                continue
              f7 |= f6
              for d8 in range(10):
                f8 = 1<<d8
                if (f7&f8):
                  continue
                if (100*d6+10*d7+d8)%11 != 0:
                  continue
                f8 |= f7
                for d9 in range(10):
                  f9 = 1<<d9
                  if (f8&f9):
                    continue
                  if (100*d7+10*d8+d9)%13 != 0:
                    continue
                  f9 |= f8
                  for d10 in range(10):
                    f10 = 1<<d10
                    if (f9&f10):
                      continue
                    if (100*d8+10*d9+d10)%17 != 0:
                      continue
                    s += (((((((((d1*10+d2)*10+d3)*10+d4)*10+d5)*10+d6)*10+d7)*10+d8)*10+d9)*10+d10)

print s
