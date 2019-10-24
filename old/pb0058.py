def bPrime(n):
	if(n < 2):
		return False
	if(n == 2):
		return True
	if(n%2 == 0):
		return False
	i = 3;
	while(i * i <= n):
		if(n%i==0):
			return False
		i += 2
	return True

i = 1
d = 1
b = True
c = 1
cp = 0
while(b):
	c += 4
	d += 1
	for j in range(4):
		i += d
		if(bPrime(i)):
			cp += 1
	d += 1
	if(c > cp * 10):
		b = False

print d
	