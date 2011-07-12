import time
s = time.time()
number = 1
num_sum = 1
for a in range(501):
	for b in range(4):
		number += a*2
		if a != 0:
			num_sum += number
		print "running number: ", number
	print "a: ", a
	print "sum: ", num_sum
	
print time.time() - s