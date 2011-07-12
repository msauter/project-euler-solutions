for a in range(420, 999):
	print a
	for b in range(a):
		for c in range(b):
			if (c*c + b*b) == (a*a) and a+b+c == 1000:
				print "abc = ", a*b*c
				print a
				print b
				print c