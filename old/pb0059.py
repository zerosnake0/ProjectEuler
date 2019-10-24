file = open("pb0059_cipher1.txt")
str = file.read().split(',')
file.close()

l = len(str)
for i in range(l):
	str[i] = int(str[i])

lo = ord('a')
up = ord('z')+1

for a in range(lo,up):
	for b in range(lo,up):
		for c in range(lo,up):
			key = [a,b,c]
			lst = str[:]
			for i in range(l):
				lst[i] ^= key[i%3]
				lst[i] = chr(lst[i])

			se = " the "
			i = 0
			while(i < l-4):
				j = 0
				while(j < 5):
					if(lst[i+j] != se[j]):
						break;
					j += 1
				if(j == 5):
					print key
					for j in range(3):
						key[j] = chr(key[j])
					print key
					break;
				i += 1

			if(i < l-4):
				sum = 0
				for i in range(l):
					sum += ord(lst[i])
				print sum
				