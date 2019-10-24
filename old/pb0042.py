file = open("pb0042_words.txt")
str = file.read().split(',')
file.close()

max = 0;
for i in range(len(str)):
	l = len(str[i]) - 2;
	if(l > max):
		max = l

max *= 26

n = 1
lst = []
t = 1
while(t <= max):
	lst.append(t)
	n += 1
	t += n

c = 0;
for i in range(len(str)):
	l = len(str[i]) - 2
	sum = 0
	for j in range(1,1+l):
		sum += ord(str[i][j]) - ord('A') + 1
	for j in range(len(lst)):
		if(sum == lst[j]):
			print str[i],sum
			c += 1
			break

print c
		