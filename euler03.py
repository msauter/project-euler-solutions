#Problem 3
#02 November 2001   
#The prime factors of 13195 are 5, 7, 13 and 29.  
#What is the largest prime factor of the number 600851475143 ?   
#
#-------------------------

number = 600851475143
prime_numbers_list = []
check = 2
while check <= number:
	if number % check == 0:
		prime_numbers_list.append(check)
		print check
		number = number / check
		print "number: ", number
	check = check + 1
		
print prime_numbers_list