#Problem 24
#16 August 2002
#A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1 and 2 are:  012  021  102  120  201  210 
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
# 5, 6, 7, 8 and 9?
#
#----------


digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
digit_list = []

def factorial(q):
	factorial = 1
	for n in range(1, q + 1):
		factorial = factorial*n
	return factorial

def convert(p):
	number = 0
	for b in range(len(p)):
		number += p[b]*(10**(9-b))
	return number

digint = 0
running_count = 999999
for c in range(10):
	fac = factorial(9 - c)
	di = int(running_count / fac)
	print "di = ", di
	digint = digits[di]
	digits.pop(di)
	rc = running_count % fac
	print "rc =", rc
	digit_list.append(digint)
	running_count = rc
	
print digit_list
print convert(digit_list)