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

max = 0
for i in range(7654321, 1234566, -1):
	j = i
	c = 0
	while(j > 0):
		k = j % 10
		if(k == 0):
			break
		f = 1 << (k - 1)
		if(c & f):
			break
		c |= f
		j /= 10
	if(j > 0 or c != 0x7F):
		continue
	if(bPrime(i)):
		print i
		break
