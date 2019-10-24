def pow(a,b):
	if(b == 0):
		return 1
	r = pow(a,b/2)
	r = r * r

	if(b%2 == 0):
		return r
	else:
		return r * a

max = 0
for a in range(2,100):
	for b in range(100):
		i = pow(a,b)
		sum = 0
		while(i > 0):
			sum += i%10;
			i /= 10
		if(sum > max):
			max = sum

print max