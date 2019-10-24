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

sum = 0
c = 0
i = 21
while(c < 11):
	i += 2
	if(not(bPrime(i))):
		continue
	k = 10
	b = True
	while(k < i):
		if(not(bPrime(i%k))):
			b = False
			break
		k *= 10
	
	if(not(b)):
		continue
		
	j = i/10
	while(j > 0):
		if(not(bPrime(j))):
			b = False
			break
		j /= 10

	if(b):
		c += 1
		sum += i

print sum
