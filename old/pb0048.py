sum = 0
for i in range(1,1001):
	pdt = 1
	for j in range(i):
		pdt *= i
		pdt %= 10000000000
	sum += pdt
	sum %= 10000000000

print sum