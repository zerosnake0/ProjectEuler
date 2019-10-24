def d(n):
	i = 1
	p = 1
	k = 1
	while(p+k<=n):
		p += k
		i += 1
		j = i
		k = 0
		while(j>0):
			k += 1
			j /= 10
	k = p + k - n
	j = i
	while(k>1):
		j /= 10
		k -= 1
	return j%10

print d(1) * d(10) * d(100) * d(1000) * d(10000) * d(100000) * d(1000000)
