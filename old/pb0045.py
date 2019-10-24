from math import sqrt

def bTri(x):
	pdt = 8 * x + 1
	rt = int(sqrt(pdt))
	if(rt*rt != pdt):
		return False
	return (rt & 0x1 != 0)

def bPen(x):
	pdt = 24 * x + 1
	rt = int(sqrt(pdt))
	if(rt*rt != pdt):
		return False
	return ((rt + 1) % 6 == 0)

h = 40755
n = 143
b = True

while(b):
	h += 4 * n + 1
	n += 1
	if(not(bPen(h))):
		continue
	if(not(bTri(h))):
		continue
	b = False
	print h