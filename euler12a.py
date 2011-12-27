#Unsolved
#
#
#
#
#--------------------------

import time, math
s = time.time()
divisors = 0
xth_triangle_number = 1
triangle_number = 0

while divisors <= 500:

	triangle_number += xth_triangle_number
	divisors = 0
	print triangle_number
	n = xth_triangle_number
	if triangle_number % 2 == 0:
		for b in range(1, (triangle_number/2)):
			if triangle_number % b == 0:
				divisors += 1
	else:
		for b in range(1, int(triangle_number/2) + 1):
			if triangle_number % b == 0:
				divisors += 1
	divisors += 1
	print "Divisors: ", divisors
	xth_triangle_number += 1
	
print "Triangle number = ", triangle_number
print "Time: ", time.time() - s