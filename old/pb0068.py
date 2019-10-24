res = []
l = []
for a in range(1,10):
	l.append(a)
	for b in range(1,10):
		if(b in l):
			continue
		l.append(b)
		sum = 10 + a + b
		for c in range(1,10):
			if(c in l):
				continue
			cc = sum - b - c
			if(cc <= 0 or cc >= 10 or cc == c or cc in l):
				continue
			l.append(c)
			l.append(cc)
			for d in range(1,10):
				if(d in l):
					continue
				dd = sum - c - d
				if(dd <= 0 or dd >= 10 or dd == d or dd in l):
					continue
				l.append(d)
				l.append(dd)
				for e in range(1,10):
					if(e in l):
						continue
					ee = sum - d - e
					if(ee <= 0 or ee >= 10 or ee == e or ee in l):
						continue
					l.append(e)
					l.append(ee)
					aa = sum - e - a
					if(aa > 0 and aa < 10 and not(aa in l)):
						l.append(aa)
						res.append(l[:])
						l.pop()
					l.pop()
					l.pop()
				l.pop()
				l.pop()
			l.pop()
			l.pop()
		l.pop()
	l.pop()

ss = []
for r in res:
	s1 = "%d%d%d" % (r[3],r[1],r[2])
	s2 = "%d%d%d" % (r[5],r[2],r[4])
	s3 = "%d%d%d" % (r[7],r[4],r[6])
	s4 = "%d%d%d" % (r[8],r[6],r[0])
	s5 = "10%d%d" % (r[0],r[1])
	m = min(r[3],r[5],r[7],r[8])
	if(r[3] == m):
		ss.append("%s%s%s%s%s" % (s1,s2,s3,s4,s5))
	elif(r[5] == m):
		ss.append("%s%s%s%s%s" % (s2,s3,s4,s5,s1))
	elif(r[7] == m):
		ss.append("%s%s%s%s%s" % (s3,s4,s5,s1,s2))
	else:
		ss.append("%s%s%s%s%s" % (s4,s5,s1,s2,s3))

print max(ss)
	