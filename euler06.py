#Problem 6
#14 December 2001
#The sum of the squares of the first ten natural numbers is,  1 2 + 2 2 + ... +
# 10 2 = 385  The square of the sum of the first ten natural numbers is,  (1 + 
#2 + ... + 10) 2 = 55 2 = 3025  Hence the difference between the sum of the
# squares of the first ten natural numbers and the square of the sum is 3025 38
#5 = 2640.  Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.
#
#----------


sum_sq = 0
sq_sum = 25502500
for a in range (1, 101):
	sum_sq = sum_sq + (a * a)
	
print "final: ", (sq_sum - sum_sq)