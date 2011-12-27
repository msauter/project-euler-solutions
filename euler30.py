#Problem 30
#08 November 2002
#Surprisingly there are only three numbers that can be written as the sum of
# fourth powers of their digits:  1634 = 1 4 + 6 4 + 3 4 + 4 4 8208 = 8 4 + 2 4
# + 0 4 + 8 4 9474 = 9 4 + 4 4 + 7 4 + 4 4  As 1 = 1 4 is not a sum it is not
# included.  The sum of these numbers is 1634 + 8208 + 9474 = 19316.  Find the
# sum of all the numbers that can be written as the sum of fifth powers of thei
#r digits.
#
#----------


import time
s = time.time()
sum_list = []
for a in range(10):
	for b in range(10):
		for c in range(10):
			for d in range(10):
				for e in range(10):
					for f in range(10):
						number = a * 100000 + b * 10000 + c * 1000 + d * 100 + e * 10 + f
						fifth_sum = a**5 + b**5 + c**5 + d**5 + e**5 + f**5
						if number == fifth_sum and number > 1:
							sum_list.append(number)

print sum_list
final_sum = 0
for g in sum_list:
	final_sum += g
print final_sum
print time.time() - s