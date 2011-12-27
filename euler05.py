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