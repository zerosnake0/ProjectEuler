m = 10**9 + 7
n = input()
t = map(int, raw_input().split())

def f(l,r):
  if (r-l) == 1:
    return 1
  for i in xrange(l+1,r):
    if t[i] > t[l]:
      return 0
  res = 0
  for i in xrange(2,r-l,2):
    rl = f(l+1,l+i)
    if rl != 0:
      rr = f(l+i,r)
      res += rl * rr
  return res

print f(0,len(t))
    