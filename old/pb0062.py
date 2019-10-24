def key(ll):
	return "%d,%d,%d,%d,%d,%d,%d,%d,%d,%d" % (ll[0],ll[1],ll[2],ll[3],ll[4],ll[5],ll[6],ll[7],ll[8],ll[9])

max = 10000

lst = {}

for i in range(max):
	j = i*i*i
	l = [0]*10
	while(j > 0):
		l[j%10] += 1
		j /= 10
	k = key(l)
	if(not(k in lst)):
		lst[k] = []
	lst[k].append(i)

min = max
for i in lst:
	if(len(lst[i]) == 5):
		if(lst[i][0] < min):
			min = lst[i][0]

print min*min*min