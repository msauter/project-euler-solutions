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
prime_list = [2]

for p in range(3,500,2):
	isprime = True
	sp = int(math.sqrt(p)) + 1
	for x in range(2, sp):
		if (p % x == 0 and p != x):
			isprime = False
			break
	if isprime:
		print p
		prime_list.append(p)

while divisors <= 10:

	triangle_number += xth_triangle_number
	print triangle_number
	n = xth_triangle_number
	print "formula: ", (n*(n+1))/2
#	pf_range = int(math.sqrt(triangle_number)) + 1
	prime_factors = []
	for b in range(1, triangle_number + 1):
		if triangle_number % b == 0:
			for c in prime_list:
				if c == b:
					prime_factors.append(b)
	prime_factors_exp = []
	for c in range(1, len(prime_factors) + 1):
		c_prime = 1
		prime_factors_exp.append([])
		for d in range(triangle_number):
			c_prime = c_prime * prime_factors[c - 1]
			if triangle_number % c_prime == 0:
				prime_factors_exp[c - 1].append(d + 1)
	print prime_factors, prime_factors_exp
	divisors += 1
	print "Divisors: ", divisors
	xth_triangle_number += 1
	
print "Triangle number = ", triangle_number
print "Time: ", time.time() - s