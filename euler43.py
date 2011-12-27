#Problem 43
#09 May 2003
#The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
# each of the digits 0 to 9 in some order, but it also has a rather interesting
# sub-string divisibility property.  Let d 1 be the 1 st digit, d 2 be the 2 nd
# digit, and so on. In this way, we note the following:   d 2 d 3 d 4 =406 is
# divisible by 2  d 3 d 4 d 5 =063 is divisible by 3  d 4 d 5 d 6 =635 is
# divisible by 5  d 5 d 6 d 7 =357 is divisible by 7  d 6 d 7 d 8 =572 is
# divisible by 11  d 7 d 8 d 9 =728 is divisible by 13  d 8 d 9 d 10 =289 is
# divisible by 17   Find the sum of all 0 to 9 pandigital numbers with this
# property.
#
#----------

import itertools

pan_sum = 0

for a in itertools.permutations(range(10)):
	print a
	str_a = ''
	for b in range(len(a)):
		str_a += str(a[b])
	print str_a
	d2 = 100*int(str_a[1]) + 10*int(str_a[2]) + int(str_a[3])
	d3 = 100*int(str_a[2]) + 10*int(str_a[3]) + int(str_a[4])
	d4 = 100*int(str_a[3]) + 10*int(str_a[4]) + int(str_a[5])
	d5 = 100*int(str_a[4]) + 10*int(str_a[5]) + int(str_a[6])
	d6 = 100*int(str_a[5]) + 10*int(str_a[6]) + int(str_a[7])
	d7 = 100*int(str_a[6]) + 10*int(str_a[7]) + int(str_a[8])
	d8 = 100*int(str_a[7]) + 10*int(str_a[8]) + int(str_a[9])
	if d2 % 2 == 0 and d3 % 3 == 0 and d4 % 5 == 0 and d5 % 7 == 0 and d6 % 11 == 0 and d7 % 13 == 0 and d8 % 17 == 0:
		pan_sum += int(str_a)
		print "Yeeeeeeeaaaaaaaahhhhhhhhh it's: ", str_a
		
print pan_sum