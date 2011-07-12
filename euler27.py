import time, math
s = time.time()

def is_prime(num):
	isprime = True
	if num <= 0:
		return False
	sp = int(math.sqrt(num)) + 1
	for x in range(2, sp):
		if (num % x == 0 and num != x):
			isprime = False
			break
	return isprime

prime_list = [2]
for p in range(3,1000,2):
	if is_prime(p):
		print p
		prime_list.append(p)
		
highest = 0
product = 0
		
for b in prime_list:
	for a in range(-1000, 1000):
		print a
		for n in range(79):
			quad = n * n + a * n + b
			if is_prime(quad) == False:
				if n > highest:
					highest = n
					product = a * b
				break
				
print highest
print product
print time.time() - s