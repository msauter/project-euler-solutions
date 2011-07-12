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