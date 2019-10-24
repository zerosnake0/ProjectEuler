import string

def rev(n):
	s = str(n)[::-1]
	r = string.atoi(s)
	return r


def bPa(n):
	s = str(n)
	l = len(s)
	for i in range(l/2+1):
		if(s[i] != s[l-1-i]):
			return False
	return True
	

c = 0
for i in range(10000):
	k = i
	for j in range(50):
		k += rev(k)
		if(bPa(k)):
			c += 1
			break

print 10000 - c