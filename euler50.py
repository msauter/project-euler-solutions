#Problem 50
#15 August 2003
#The prime 41, can be written as the sum of six consecutive primes:  41 = 2 + 3
# + 5 + 7 + 11 + 13  This is the longest sum of consecutive primes that adds to
# a prime below one-hundred.  The longest sum of consecutive primes below
# one-thousand that adds to a prime, contains 21 terms, and is equal to 953. 
# Which prime, below one-million, can be written as the sum of the most
# consecutive primes?
#
#----------


import time, math
s = time.time()
prime_list = [2]

def is_prime(p):
	isprime = True
	sp = int(math.sqrt(p)) + 1
	for x in range(2, sp):
		if (p % x == 0 and p != x):
			isprime = False
			break
	return isprime

for q in range(3,1000000,2):
	if is_prime(q):
		prime_list.append(q)
		print q

print prime_list

lc = 0
bigprime = 0

for z in range(len(prime_list)):
	cpsum = prime_list[z]
	count = 1
	while cpsum < 1000000:
		if z + count < len(prime_list):
			cpsum += prime_list[z + count]
		else:
			break
		count += 1
		if is_prime(cpsum) and cpsum < 1000000 and count > lc:
			lc = count
			bigprime = cpsum
			print bigprime, lc
	
print "The largest prime is...", bigprime, " with ", lc, " consecutive primes!"
print "time: ", time.time() - s