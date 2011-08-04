def str_to_list(s):
	sl = []
	for y in s:
		sl.append(y)
	return sl
	
psum = 0
plist = []

for a in range(1, 1000):
	print "A = ", a
	if a < 100:
		for b in range(1, 10000):
			c = a * b
			nstr = str(a) + str(b) + str(c)
			nlist1 = str_to_list(nstr)
			nlist2 = list(set(nlist1))
			nlist1.sort()
			nlist2.sort()
			if nlist1 == nlist2:
				for q in range(len(nlist1)):
					if q + 1 != int(nlist1[q]):
						break
					if q + 1 == len(nlist1) and q + 1 == 9:
						print nlist1
						plist.append(int(c))
	if a >= 100:
		for b in range(1, 1000):
			c = a * b
			nstr = str(a) + str(b) + str(c)
			nlist1 = str_to_list(nstr)
			nlist2 = list(set(nlist1))
			nlist1.sort()
			nlist2.sort()
			if nlist1 == nlist2:
				for q in range(len(nlist1)):
					if q + 1 != int(nlist1[q]):
						break
					if q + 1 == len(nlist1) and q + 1 == 9:
						print nlist1
						plist.append(int(c))
						
plist = list(set(plist))
for y in plist:
	psum += y
	
print plist				
print "And the sum of the products is...", psum