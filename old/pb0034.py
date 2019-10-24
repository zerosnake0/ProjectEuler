f = []
f.append(1)
for i in range(1,10):
	f.append(f[i-1]*i)

r = 0
for i in range(3,2550000):
	j = i
	k = 0
	while(j > 0):
		k += f[j%10]
		j /= 10
	if(k == i):
		r += i

print r
