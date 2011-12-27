#Problem 21
#05 July 2002
#Let d( n ) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n ). If d( a ) = b and d( b ) = a , where a   b ,
# then a and b are an amicable pair and each of a and b are called amicable
# numbers.  For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20,
# 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
# 2, 4, 71 and 142; so d(284) = 220.  Evaluate the sum of all the amicable
# numbers under 10000.
#
#----------

import time
s = time.time()

def find_sum_of_divisors(n):
	sum_divisors = 0
	divisors = []
	for b in range(1, n):
		if n % b == 0:
			divisors.append(b)
			sum_divisors += b
	return sum_divisors

divisors_list = []
for a in range(1, 10000):
	divisors_list.append(find_sum_of_divisors(a))
	print a
	
print divisors_list

total_sum = 0

for c in range(len(divisors_list)):
	num = c + 1
	ds = 0
	ds = find_sum_of_divisors(divisors_list[c])
	print ds
	if ds == num and ds != divisors_list[c]:
		total_sum += num
		print "number: ", num
		
print "Total sum: ", total_sum
print "in ", time.time() - s