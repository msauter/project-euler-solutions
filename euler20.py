#Problem 20
#21 June 2002
#n ! means n  ( n  1) ... 3 2 1  For example, 10! = 10 9 ... 3 2 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27
#.  Find the sum of the digits in the number 100!
#
#----------


number = 1

for a in range(1, 101):
	number = number * a
	
print number

number_string = str(number)
number_sum = 0
for b in range(len(number_string)):
	number_sum += int(number_string[b])
	
print "The sum is: ", number_sum