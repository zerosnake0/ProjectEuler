file = open("pb0054_poker.txt")
str = file.read().split()
file.close()


lst = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
	

def foo(l):
	flush = True
	straight = True

	for i in range(1,5):
		if(l[i][1] != l[0][1]):
			flush = False

	for i in range(5):
		l[i] = lst[l[i][0]]

	l.sort()
	
	pCount = []
	pCard  = []

	i = 1
	while(i < 5):
		if(l[i] != l[i-1]+1):
			straight = False
		if(l[i] == l[i-1]):
			j = i + 1
			while(j < 5 and l[j] == l[i]):
				j += 1
			pCount.append(j+1-i)
			pCard.append(l[i])
			i = j
		else:
			i += 1

	if(len(pCount) == 2):
		if(pCount[0] < pCount[1]):
			tmp = pCount[0]
			pCount[0] = pCount[1]
			pCount[1] = tmp
			tmp = pCard[0]
			pCard[0] = pCard[1]
			pCard[1] = tmp
		elif(pCount[0] == pCount[1]):
			if(pCard[0] < pCard[1]):
				tmp = pCard[0]
				pCard[0] = pCard[1]
				pCard[1] = tmp

	if(straight):
		if(flush):
			return [9,l[4]]
		else:
			return [5,l[4]]
	
	if(pCount == []):
		if(flush):
			return [6,l[4],l[3],l[2],l[1],l[0]]
		else:
			return [1,l[4],l[3],l[2],l[1],l[0]]

	if(pCount[0] == 4):
		return [8,pCard[0]]
	

	if(len(pCount) == 2):
		if(pCount[0] == 3):
			return [7,pCard[0],pCard[1]]
		else:
			l.remove(pCard[0]);
			l.remove(pCard[0]);
			l.remove(pCard[1]);
			l.remove(pCard[1]);
			return [3,pCard[0],pCard[1],l[0]]

	if(pCount[0] == 3):
		l.remove(pCard[0])
		l.remove(pCard[0])
		l.remove(pCard[0])
		return [4,pCard[0],l[1],l[0]]

	l.remove(pCard[0])
	l.remove(pCard[0])
	return [2,pCard[0],l[2],l[1],l[0]]

c = 0
for i in range(len(str)/10):
	j = i*10
	l1 = str[j:j+5]
	l2 = str[j+5:j+10]
	r1 = foo(l1)
	r2 = foo(l2)
	if(r1 > r2):
		c += 1

print c
