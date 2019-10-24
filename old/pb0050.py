max = 1000000
bp = [True] * max
bp[0] = bp[1] = False

i = 4
while(i<max):
	bp[i] = False
	i += 2

i = 3
while(i<max):
	if(bp[i]):
		j = i * i
		d = i * 2
		while(j<max):
			bp[j] = False
			j += d
	i += 1

i = 2
maxc = 0
maxsum = 0
while(i < max):
	if(bp[i]):
		c = 1
		j = i + 1
		sum = i
		while(j < max):
			if(bp[j]):
				sum += j
				c += 1
				if(sum >= max):
					break
				if(bp[sum] and (c > maxc)):
					maxc = c
					maxsum = sum
			j += 1
	i += 1

print maxsum