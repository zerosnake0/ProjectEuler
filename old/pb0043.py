sum = 0

i = 0
while(i < 986):
	i += 17
	c = 0
	j = i
	b = True
	for k in range(3):
		f = 1 << (j % 10)
		if(c & f):
			b = False
			break
		c |= f
		j /= 10
	if(not(b)):
		continue
	for i2 in range(10):
		f = 1 << i2
		if(c & f):
			continue
		c2 = c | f
		if((i2*100 + i / 10) % 13 != 0):
			continue
		for i3 in range(10):
			f = 1 << i3
			if(c2 & f):
				continue
			c3 = c2 | f
			if((i3*100 + i2*10 + i/100) % 11 != 0):
				continue
			for i4 in range(10):
				f = 1 << i4
				if(c3 & f):
					continue
				c4 = c3 | f
				if((i4*100 + i3*10 + i2) % 7 != 0):
					continue
				for i5 in range(10):
					f = 1 << i5
					if(c4 & f):
						continue
					c5 = c4 | f
					if((i5*100 + i4*10 + i3) % 5 != 0):
						continue
					for i6 in range(10):
						f = 1 << i6
						if(c5 & f):
							continue
						c6 = c5 | f
						if((i6+i5+i4)%3 != 0):
							continue
						if(i5%2 != 0):
							continue
						lst = []
						c6 = 0x3ff - c6
						ii = 0
						while(c6 > 0):
							if(c6 & 0x1):
								lst.append(ii)
							c6 >>= 1
							ii += 1
						sum += (lst[0]+lst[1]) * 1100000000 +\
							            (i6 * 10000000 +\
								     i5 * 1000000 +\
								     i4 * 100000 +\
								     i3 * 10000 +\
								     i2 * 1000 +\
								     i)*2

print sum
