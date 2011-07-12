number = 1
for a in range(1000):
	number = 2*number
	
print number

number_string = str(number)

print number_string

number_list = []

for b in range(len(number_string)):
	ns = int(number_string[b])
	number_list.append(ns)
	
print number_list

number_sum = 0

for c in range(len(number_list)):
	number_sum = number_sum + number_list[c]
	
print "The sum is: ", number_sum