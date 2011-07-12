import time
s = time.time()

def xth_factorial(q):		
	factorial = 1
	for n in range(1, q + 1):
		factorial = factorial*n
	return factorial

total_sum = 0
fac_number_list = []

for b in range(4):
	for c in range(10):
		for d in range(10):
			for e in range(10):
				for f in range(10):	
					for g in range(10):
						for h in range(10):
							number = b * 1000000 + c * 100000 + d * 10000 + e * 1000 + f * 100 + g * 10 + h
							if b != 0:
								fac = xth_factorial(b) + xth_factorial(c) + xth_factorial(d) + xth_factorial(e) + xth_factorial(f) + xth_factorial(g) + xth_factorial(h)
							if b == 0:
								fac = xth_factorial(c) + xth_factorial(d) + xth_factorial(e) + xth_factorial(f) + xth_factorial(g) + xth_factorial(h)
							if b == 0 and c == 0:
								fac = xth_factorial(d) + xth_factorial(e) + xth_factorial(f) + xth_factorial(g) + xth_factorial(h)
							if b == 0 and c == 0 and d == 0:
								fac = xth_factorial(e) + xth_factorial(f) + xth_factorial(g) + xth_factorial(h)
							if b == 0 and c == 0 and d == 0 and e == 0:
								fac = xth_factorial(f) + xth_factorial(g) + xth_factorial(h)
							if b == 0 and c == 0 and d == 0 and e == 0 and f == 0:
								fac = xth_factorial(g) + xth_factorial(h)
							if b == 0 and c == 0 and d == 0 and e == 0 and f == 0 and g == 0:
								fac = xth_factorial(h)
							if number == fac and number > 2:
								print fac
								fac_number_list.append(fac)
								total_sum += fac

print fac_number_list
print total_sum
print "time: ", time.time() - s, " seconds"