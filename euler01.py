#Problem 1
#05 October 2001
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.  Find the sum of all the
# multiples of 3 or 5 below 1000.
#
#----------


z = 0
for x in range(999):
	m = x + 1
	if m % 3 == 0 or m % 5 == 0:
		z = z + m
print z