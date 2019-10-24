# Counting Castles
# Problem 502
#
# We define a block to be a rectangle with a height of 1 and an integer-valued
# length. Let a castle be a configuration of stacked blocks.
#
# Given a game grid that is w units wide and h units tall, a castle is
# generated according to the following rules:

#   1. Blocks can be placed on top of other blocks as long as nothing sticks
#      out past the edges or hangs out over open space.
#   2. All blocks are aligned/snapped to the grid.
#   3. Any two neighboring blocks on the same row have at least one unit of
#      space between them.
#   4. The bottom row is occupied by a block of length w.
#   5. The maximum achieved height of the entire castle is exactly h.
#   6. The castle is made from an even number of blocks.
#
# The following is a sample castle for w=8 and h=5:
#
#   --x---x-  (2 blocks, 1x1, 1x1)
#   --x---xx  (2 blocks, 1x1, 2x1)
#   -xx-x-xx  (3 blocks, 2x1, 1x1, 2x1)
#   xxxxx-xx  (2 blocks, 5x1, 2x1)
#   xxxxxxxx  (bottom block, 8x1)
#
# Let F(w,h) represent the number of valid castles, given grid parameters w and
# h.
#
# For example, F(4,2) = 10, F(13,10) = 3729050610636, F(10,13) = 37959702514,
# and F(100,100) mod 1 000 000 007 = 841913936.
#
# Find (F(1012,100) + F(10000,10000) + F(100,1012)) mod 1 000 000 007.

# top row for F(4,2)
# x--- -x-- --x- ---x
# xx-- -xx- --xx
# xxx- -xxx
# xxxx

