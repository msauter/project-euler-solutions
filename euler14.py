number = 0
longest = 0
starting_number = 0
for a in range(1, 1000000):
	count = 1
	number = a
	print a
	while number != 1:
		if number % 2 == 0:
			number = number / 2
		else:
			number = 3 * number + 1
		count += 1
	if count > longest:
		longest = count
		starting_number = a
		
print "The longest count is: ", longest
print "which is generated from the starting number: ", starting_number