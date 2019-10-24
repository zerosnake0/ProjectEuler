from time import clock
beg = clock()

m = 10**9 + 7
n = input()
t = map(int, raw_input().split())

print 2, t[2]
for i in xrange(2,n):
  if t[i] > t[2]:
    print i, t[i]
    break