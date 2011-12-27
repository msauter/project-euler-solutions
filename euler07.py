#Problem 7
#28 December 2001
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see tha
#t the 6th prime is 13.  What is the 10 001st prime number?
#
#----------

prime_list = []
for p in range(105000):
	if (p % 2 != 0 or p == 2) and (p % 3 != 0 or p == 3) and (p % 5 != 0 or p == 5):
		prime_list.append(p)

for x in range(2, 1000):
	for y in prime_list:
		if y % x == 0 and y != x:
			prime_list.remove(y)
			print y
	
print prime_list
print len(prime_list)
print prime_list[10001]
