bTri = 0x1
bSqu = 0x2
bPen = 0x4
bHex = 0x8
bHep = 0x10
bOct = 0x20
bLst = [bTri,bSqu,bPen,bHex,bHep,bOct]

min = 1000
max = 10000
pp = [0] * max

n = 1
p = n*(n+1)/2
while(p < max):
	pp[p] |= bTri
	p += n + 1
	n += 1

n = 1
p = n*n
while(p < max):
	pp[p] |= bSqu
	p += 2 * n +1
	n += 1

n = 1
p = n*(3*n-1)/2
while(p < max):
	pp[p] |= bPen
	p += 3 * n + 1
	n += 1

n = 1
p = n*(2*n-1)
while(p < max):
	pp[p] |= bHex
	p += 4 * n + 1
	n += 1

n = 1
p = n*(5*n-3)/2
while(p < max):
	pp[p] |= bHep
	p += 5 * n + 1
	n += 1

n = 1
p = n*(3*n-2)
while(p < max):
	pp[p] |= bOct
	p += 6 * n + 1
	n += 1

def check(lst,v):
	if(v == 0):
		return True

	if(lst == []):
		return False

	ll = len(lst)
	for b in bLst:
		if(pp[lst[0]] & b == 0):
			continue
		if(v & b == 0):
			continue
		if(check(lst[1:ll],v^b)):
			return True

	return False

for a in range(min,max):
	if(pp[a] == 0):
		continue
	sufa = a % 100
	if(sufa < 10):
		continue
	for b in range(sufa*100,(sufa+1)*100):
		if(pp[b] == 0):
			continue
		sufb = b % 100
		if(sufb < 10):
			continue
		for c in range(sufb*100,(sufb+1)*100):
			if(pp[c] == 0):
				continue
			sufc = c % 100
			if(sufc < 10):
				continue
			for d in range(sufc*100,(sufc+1)*100):
				if(pp[d] == 0):
					continue
				sufd = d % 100
				if(sufd < 10):
					continue
				for e in range(sufd*100,(sufd+1)*100):
					if(pp[e] == 0):
						continue
					sufe = e % 100
					if(sufe < 10):
						continue
					f = sufe*100 + a/100
					if(pp[f] == 0):
						continue
					if(check([a,b,c,d,e,f],0x3F)):
						print a,b,c,d,e,f
						print pp[a],pp[b],pp[c],pp[d],pp[e],pp[f]
						print a+b+c+d+e+f