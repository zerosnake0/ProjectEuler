# Sum square difference
# Problem 6
#
# The sum of the squares of the first ten natural numbers is,
#
#   1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
#
#   (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.
#
# Answer: 25164150

n = 100

# sum(n)^2 = (n(n+1)/2) ^ 2
# sum(n^2) = n(n+1)(2n+1)/6

k = n + 1
l = n * k / 2

print l * (l - (n + k) / 3)
