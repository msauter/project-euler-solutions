#Problem 9
#25 January 2002
#A Pythagorean triplet is a set of three natural numbers, a   b   c , for
#which,   a 2 + b 2 = c 2  For example, 3 2 + 4 2 = 9 + 16 = 25 = 5 2 .  There
#exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the 
#product abc .
#
#----------

for a in range(420, 999):
	print a
	for b in range(a):
		for c in range(b):
			if (c*c + b*b) == (a*a) and a+b+c == 1000:
				print "abc = ", a*b*c
				print a
				print b
				print c