max = 0
maxp = 0
for p in range(12,1001):
	count = 0
	for c in range(p/3, p/2):
		for a in range(1, c/2):
			b = p - a - c
			if(a > b):
				continue
			if(a*a + b*b == c*c):
				count += 1
	if(count > max):
		max = count
		maxp = p

print maxp