import time
s = time.time()

def fac(q):		
	factorial = 1
	for n in range(1, q + 1):
		factorial = factorial*n
	return factorial
	
count = 0
	
for a in range(1, 101):
	for r in range(1, a):
		comb = (fac(a)) / (fac(r) * fac(a - r))
		if comb > 1000000:
			count += 1
			
print count
print time.time() - s