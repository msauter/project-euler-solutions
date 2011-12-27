#Unsolved
#
#Problem 23
#02 August 2002
#A perfect number is a number for which the sum of its proper divisors is
#exactly equal to the number. For example, the sum of the proper divisors of 28
# would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.  
#A number n is called deficient if the sum of its proper divisors is less than 
#n and it is called abundant if this sum exceeds n .   As 12 is the smallest
# abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be
# written as the sum of two abundant numbers is 24. By mathematical analysis,
#it can be shown that all integers greater than 28123 can be written as the sum
# of two abundant numbers. However, this upper limit cannot be reduced any
# further by analysis even though it is known that the greatest number that
# cannot be expressed as the sum of two abundant numbers is less than this
# limit.  Find the sum of all the positive integers which cannot be written as
# the sum of two abundant numbers.
#
#----------


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