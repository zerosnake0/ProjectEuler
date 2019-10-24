from math import sqrt


def Pen(x):
  return x*(3*x-1)/2

def bPen(x):
  pdt = 24 * x + 1
  rt = int(sqrt(pdt))
  if(rt*rt != pdt):
    return False
  return ((rt + 1) % 6 == 0)

lst = []
i = 0
b = True
while(b):
  l = len(lst)
  i += 1
  p = Pen(i)
  lst.append(p)
  for j in range(l):
    sum = p + lst[j]
    if(not(bPen(sum))):
      continue
    diff = p - lst[j]
    if(bPen(diff)):
      print diff
      b = False
      break
