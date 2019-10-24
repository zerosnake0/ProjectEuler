def pow(a,b):
	if(b == 0):
		return 1
	r = pow(a,b/2)
	r = r * r

	if(b%2 == 0):
		return r
	else:
		return r * a
n = 1

n9 = 9
n10 = 1

while(n9 > n10):
	n += 1
	n9 *= 9
	n10 *= 10

r = {}

for i in range(1,n):
	for j in range(1,10):
		k = pow(j,i)
		c = 0
		kk = k
		while(kk > 0):
			c += 1
			kk /= 10
		if(c == i):
			r[k] = 0

print len(r)