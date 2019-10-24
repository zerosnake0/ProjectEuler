def conc(x,y):
	j = y
	i = 1
	while(j > 0):
		i *= 10
		j /= 10
	return x * i + y

max = 1000
res = []
while(res == []):
	mm = max * max
	bp = [True] * mm
	bp[0] = bp[1] = False
	i = 4
	while(i < mm):
		bp[i] = False
		i += 2
	i = 3
	while(i < mm):
		if(bp[i]):
			j = i
			while(j * i < mm):
				bp[j * i] = False
				j += 2
		i += 2
	
	for a in range(3, max, 2):
		if(not(bp[a])):
			continue
		lsta = [a]
		for b in range(a+2, max, 2):
			if(not(bp[b])):
				continue
			bb = True
			for i in lsta:
				if(not(bp[conc(b,i)] and bp[conc(i,b)])):
					bb = False
					break
			if(not(bb)):
				continue
			lstb = [a,b]
			for c in range(b+2, max, 2):
				if(not(bp[c])):
					continue
				bb = True
				for i in lstb:
					if(not(bp[conc(c,i)] and bp[conc(i,c)])):
						bb = False
						break
				if(not(bb)):
					continue
				lstc = [a,b,c]
				for d in range(c+2, max, 2):
					if(not(bp[d])):
						continue
					bb = True
					for i in lstc:
						if(not(bp[conc(d,i)] and bp[conc(i,d)])):
							bb = False
							break
					if(not(bb)):
						continue
					lstd = [a,b,c,d]
					for e in range(d+2, max, 2):
						if(not(bp[e])):
							continue
						bb = True
						for i in lstd:
							if(not(bp[conc(e,i)] and bp[conc(i,e)])):
								bb = False
								break
						if(not(bb)):
							continue
						lste = [a,b,c,d,e]
						res.append(lste)
	max *= 10

print res

min = 0
for i in range(len(res[0])):
	min += res[0][i]

for i in range(1,len(res)):
	sum = 0
	for j in range(len(res[i])):
		sum += res[i][j]
	if(sum < min):
		min = sum

print min