from time import time

tb = time()

max = 1000000

frac = [1] * 10
for i in range(2,10):
	frac[i] = i * frac[i-1]

def f(n):
	sum = 0
	while(n > 0):
		sum += frac[n%10]
		n /= 10
	return sum

res = 0
n = {}
for i in range(max):
	if(i in n):
		continue
	l = {i:0}
	j = f(i)
	k = 1
	bS = False
	while(not(j in l)):
		if(j in n):
			bS = True
			for it in l:
				n[it] = n[j] + k - l[it]
				if(it < max and n[it] == 60):
					res += 1
			break
		l[j] = k
		j = f(j)
		k += 1
	if(bS):
		continue
	for it in l:
		if(l[it] < l[j]):
			n[it] = k - l[it]
		else:
			n[it] = j - l[j]
		if(it < max and n[it] == 60):
			res += 1

print res
print time()-tb