import time, math
s = time.time()
prime_list = [2]
number = 3
for p in range(3,2000000,2):
	isprime = True
	sp = int(math.sqrt(p)) + 1
	for x in range(2, sp):
		if (p % x == 0 and p != x):
			isprime = False
			break
	if isprime == True:
		print p
		prime_list.append(p)

print prime_list

prime_sum = 0

for z in range(len(prime_list)):
	prime_sum = prime_sum + prime_list[z]
	
print prime_sum
print "time: ", time.time() - s