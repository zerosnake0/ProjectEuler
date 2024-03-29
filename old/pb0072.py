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

def f(n):
	l = [0] * 10
	while(n > 0):
		l[n%10] += 1
		n /= 10
	return l

max = 1000001

bp = [True] * max
bp[0] = bp[1] = False

i = 4
while(i < max):
	bp[i] = False
	i += 2

plst = [2]
i = 3
while(i < max):
	if(bp[i]):
		plst.append(i)
		for j in range(i*i, max, i*2):
			bp[j] = False
	i += 2

phi = [1,1]
i = 2
while(i < max):
	if(bp[i]):
		phi.append(i-1)
	else:
		for p in plst:
			if(i%p == 0):
				j = i
				c = 0
				while(j%p == 0):
					j /= p
					c += 1
				if(j==1):
					phi.append(i/p*(p-1))
				else:
					phi.append(phi[j]*phi[i/j])
				break
	i += 1

d = 2
sum = 0
while(d < max):
	sum += phi[d]
	d += 1

print sum