from math import sqrt

def f(d):
	a = int(sqrt(d))
	b = 1
	k = a*a - d*b*b

	while(k != 1):
		k2 = abs(k)
		m = 0
		min = d
		minm = m
		while(m*m <= d):
			if((a+b*m) % k2 == 0):
				diff = d - m*m
				if(diff < min):
					min = diff
					minm = m
			m += 1
		while(True):
			if((a+b*m) % k2 == 0):
				diff = m*m - d
				if(diff < min):
					min = diff
					minm = m
				break
			m += 1
		m = minm
		aa = (a*m+d*b)/k2
		bb = (a+b*m)/k2
		kk = (m*m-d)/k
		a = aa
		b = bb
		k = kk

	return a

max = 0
maxd = 0
for d in range(1000):
	j = int(sqrt(d))
	if(j*j == d):
		continue
	r = f(d)
	if(r>max):
		max = r
		maxd = d

print maxd
