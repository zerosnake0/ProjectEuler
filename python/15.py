# Lattice paths
# Problem 15
#
# Starting in the top left corner of a 2x2 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.
#
#   xxxxx  xxx-+  xxx-+  x-+-+  x-+-+  x-+-+
#   | | x  | x |  | x |  x | |  x | |  x | |
#   +-+-x  +-xxx  +-x-+  xxxxx  xxx-+  x-+-+
#   | | x  | | x  | x |  | | x  | x |  x | |
#   +-+-x  +-+-x  +-xxx  +-+-x  +-xxx  xxxxx
#
# How many such routes are there through a 20x20 grid?
#
# Answer: 137846528820

from util import combination

M=20
N=20
  
print combination(M+N, M)
