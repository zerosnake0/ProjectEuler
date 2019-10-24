def dc(n):
	l = [0] * 10
	while(n > 0):
		l[n%10] += 1
		n /= 10
	return l

k = 1
res = 0
while(res == 0):
	for i in range(k,k*5/3+1):
		lst = dc(i)
		j = 2
		while(j <= 6):
			l = dc(j*i)
			if(l != lst):
				break
			j += 1
		if(j == 7):
			res = i
			break
	k *= 10

for i in range(1,7):
	print res*i