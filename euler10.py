import time
s = time.time()
prime_list = [2]
number = 3
for p in range(3,2000000,2):
	if (p % 2 != 0 or p == 2) and (p % 3 != 0 or p == 3) and (p % 5 != 0 or p == 5) and (p % 7 != 0 or p == 7) and (p % 11 != 0 or p == 11) and (p % 13 != 0 or p == 13) and (p % 17 != 0 or p == 17) and (p % 19 != 0 or p == 19) and (p % 23 != 0 or p == 23) and (p % 29 != 0 or p == 29):
		prime_list.append(p)
print prime_list

for x in range(2, 100000):
	for y in prime_list:
		if y % x == 0 and y != x:
			prime_list.remove(y)
			print y

print prime_list

prime_sum = 0

for z in range(len(prime_list)):
	prime_sum = prime_sum + prime_list[z]
	
print prime_sum
print "time: ", time.time() - s