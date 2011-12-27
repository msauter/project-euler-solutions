#Problem 5
#30 November 2001
#2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.  What is the smallest positive number that is
# evenly divisible by all of the numbers from 1 to 20?
#
#----------

divisible = False
number = 2520
while divisible == False:
	divisible = True
	for a in range(1, 21):
		if number % a != 0:
			divisible = False
	if divisible == False:
		number = number + 2520

print "final: ", number