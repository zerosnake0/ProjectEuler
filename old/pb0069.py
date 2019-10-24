##############################
#                            #
# f(n) = n * PI_{p|n}(1-1/p) #
#                            #
##############################

def bPrime(n):
	if(n < 2):
		return False
	if(n == 2):
		return True
	if(n%2 == 0):
		return False
	i = 3;
	while(i * i <= n):
		if(n%i==0):
			return False
		i += 2
	return True

n = 2
i = 3
while(n * i < 1000000):
	n *= i
	i += 2
	while(not(bPrime(i))):
		i += 2

print n