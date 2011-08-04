def str_to_list(s):
	sl = []
	for y in s:
		sl.append(y)
	return sl
	
maxpan = 0

for a in range(1, 10000):
	for b in range(2, 8):
		concat = ''
		for c in range(1, b):
			p = a * c
			concat += str(p)
		clist1 = str_to_list(concat)
		clist2 = list(set(clist1))
		clist1.sort()
		clist2.sort()
		if clist1 == clist2:
			for q in range(len(clist1)):
				if q + 1 != int(clist1[q]):
					break
				if q + 1 == len(clist1) and q + 1 == 9:
					print concat
					if int(concat) > maxpan:
						maxpan = int(concat)
						
print "The largest pandigital is...", maxpan