res = 0

lst = [1,1]
lstlen = 2

while(lstlen <= 101):
	for i in range(lstlen):
		if(lst[i] > 1000000):
			res += 1
	lst.append(1)
	for i in range(lstlen-1,0,-1):
		lst[i] += lst[i-1]
	lstlen += 1

print res