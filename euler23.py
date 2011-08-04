import itertools

abundant_list = []

for a in range(2, 28124):
	divisors_list = []
	for b in range(1, a):
		if a % b == 0:
			divisors_list.append(b)
	div_sum = 0
	for d in divisors_list:
		div_sum += d
	if div_sum > a:
		abundant_list.append(a)
	print a
		
print abundant_list

sa_list = []

for c in itertools.permutations(abundant_list, 2):
	print c
	psum = 0
	for q in c:
		psum += q
	print psum
	if psum < 28124:
		sa_list.append(psum)
		
total_sum = 0
		
for x in range(1, 28124):
	if (x in sa_list) == False:
		total_sum += x

print total_sum