def nFac(x):
	r = 0
	while(x & 0x1 == 0):
		x /= 2
		r = 1

	m = x/3 + 1
	for i in range(3,m,2):
		if(x % i != 0):
			continue
		r += 1
		if(r > 4):
			return False
		while(x % i == 0):
			x /= i

	return (r == 4)
		
n = 2 * 3 * 5 * 7
count = 0

while(count < 4):
	if(nFac(n)):
		count += 1
	else:
		count = 0
	n += 1

print (n - 4)
