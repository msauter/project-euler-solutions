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