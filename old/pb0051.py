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

def cal(x, mask):
	res = 0
	f = 1
	while(mask > 0):
		if(mask&1 == 1):
			res += f * (x%10)
			x /= 10
		f *= 10
		mask >>= 1
	return res

def search(n, nDigits, nFamily):
	max = 1
	for i in range(n - nDigits):
		max *= 10

	min = 1
	for i in range(n-1):
		min *= 10

	minp = min*10;
	for i in range((1<<nDigits)-1, 1<<n):
		c = 0
		j = i
		mult = 0
		f = 1
		while(j > 0 and c <= nDigits):
			if(j&1 == 1):
				c += 1
				mult += f
			f *= 10
			j >>= 1
		if(c != nDigits):
			continue
		func = lambda x: cal(x, (1<<n) - i -1)
		
		for j in range(max):
			p = func(j)
			c = 0
			m = -1
			for k in range(10):
				if(c + 10 - k < nFamily):
					break;
				if(p >= min):
					if(bPrime(p)):
						c += 1
						if(m == -1):
							m = p
				p += mult
			
			if(c == nFamily and m < minp):
				minp = m

	if(minp == min*10):
		return -1

	return minp
			

print search(4,3,8)
print search(5,3,8)
print search(6,3,8)
