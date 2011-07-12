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
for c in range(100000):
	sa_list.append(False)
	
for e in range(len(abundant_list)):
	print e
	for f in range(e, len(abundant_list)):
		print "alist f: ", abundant_list[f]
		print "alist e: ", abundant_list[e]
		sa_list[abundant_list[f] + abundant_list[e] - 2] = True
		
total_sum = 0
for g in range(28124):
	if sa_list[g] == False:
		total_sum += (g + 1)
		
print total_sum