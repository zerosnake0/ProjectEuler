# Pandigital multiples
# Problem 38
#
# Take the number 192 and multiply it by each of 1, 2, and 3:
#
#   192 x 1 = 192
#   192 x 2 = 384
#   192 x 3 = 576
#
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We
# will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
# and 5, giving the pandigital, 918273645, which is the concatenated product of
# 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as
# the concatenated product of an integer with (1,2, ... , n) where n > 1?
#
# Answer: 932718654

# given 918273645, the concatenated product of 9 and (1,2,3,4,5)
# the largest must be bigger so the number must begin with a 9
#
# 9 * (1,2,3,4,5) => 918273645
# 9x * (1,2,3,4) => 9x, 1xx, 2xx, 3xx less or more digits
# 9xx * (1,2,3) => 9xx, 1xxx, 2xxx    less or more digits
# 9xxx * (1,2) => ok!
#
# 91xx     => 91xx1xxxx, double 1
# 94xx     => 94xx18[8/9], double 8 or 9
# 9[5-9]xx => 9xxx19xxx, double 9
#
# try with 93xx
# 93xx     => 93xx18[6/7]xx
# 937x     => 937x187xx, double 7
# 936x     => 936x1872x, x must be less than 5, we have 4 and 5, no!
# 935x     => 935x187[0/1]x, zero or double 1
# 934x     => 934x186[8/9]x, double 8 or 9
# 932x     => 932x186[4/5]x, we have 4,5,7
# finally we found 9327 => 932718654

print 932718654