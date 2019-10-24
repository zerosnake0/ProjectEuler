n=1
d=1

def gcd(a,b):
	if (a>b):
		return gcd(b,a)
	if (a==0):
		return b
	return gcd(b%a, a)

for a in range(1,10):
	for b in range (1,10):
		if(b != a):
			for c in range(1,10):
				nn = 10*a+b
				dd = 10*b+c
				if (nn*c == dd*a):
					n *= nn
					d *= dd

print d/gcd(n,d)