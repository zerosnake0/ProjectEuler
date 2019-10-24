def gcd(a,b):
	if(a < b):
		return gcd(b,a)
	if(b == 0):
		return a
	return gcd(b, a%b)

max = 1000000
nn = 1
dd = max
d = 1
while(d < max):
	d += 1
	n = d * 3 / 7
	while(n > 1 and gcd(n,d)!=1):
		n -= 1
	if(n*dd>d*nn and d != 7):
		nn = n
		dd = d

print nn,dd