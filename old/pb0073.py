max = 12000

l = []
for i in range(max+1):
	l.append([0] * (max+1))

def gcd(a,b):
	if(l[a][b] == 0):
		if(a < b):
			l[a][b] = gcd(b,a)
		elif(b == 0):
			l[a][b] = a
		else:
			l[a][b] = gcd(b, a%b)
	return l[a][b]

d = 1
sum = 0
while(d < max):
	d += 1
	left = d/3 + 1
	right = d/2
	if(d%2 != 0):
		right += 1
	for i in range(left,right):
		if(gcd(i,d)==1):
			sum += 1

print sum