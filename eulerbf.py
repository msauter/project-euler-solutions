primes = set([2]) 
value = 3 
while len(primes) < 10001: 
	isPrime = True 
	for k in primes: 
		if value % k == 0: 
			value += 2 
			isPrime = False 
			break 
	if isPrime: 
		primes.add(value) 
	if len(primes) == 10001: 
		print "10001th prime = " + str(value) 
		break 
	else: 
		value += 2