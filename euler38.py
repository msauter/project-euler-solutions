#Problem 38
#28 February 2003
#Take the number 192 and multiply it by each of 1, 2, and 3:  192 1 = 192 192 2
# = 384 192 3 = 576 By concatenating each product we get the 1 to 9 pandigital,
# 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#  The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
# and 5, giving the pandigital, 918273645, which is the concatenated product of
# 9 and (1,2,3,4,5).  What is the largest 1 to 9 pandigital 9-digit number that
# can be formed as the concatenated product of an integer with (1,2, ... , n )
# where n  1?
#
#----------


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