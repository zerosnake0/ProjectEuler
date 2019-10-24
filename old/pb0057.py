n = 3
d = 2
c = 0
for i in range(1000):
	nn = n
	dd = d
	while(dd > 0):
		nn /= 10
		dd /= 10
	if(nn > 0):
		c += 1
	dd = n + d
	nn = dd + d
	d = dd
	n = nn

print c
	
	