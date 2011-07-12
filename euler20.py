number = 1

for a in range(1, 101):
	number = number * a
	
print number

number_string = str(number)
number_sum = 0
for b in range(len(number_string)):
	number_sum += int(number_string[b])
	
print "The sum is: ", number_sum