import time
s = time.time()

number_list = []

for a in range(2, 101):
	print a
	for b in range(2, 101):
		c = a**b
		add = True
		for d in number_list:
			if d == c:
				add = False
		if add == True:
			number_list.append(c)

number_list.sort()
print number_list
print len(number_list)
print time.time() - s