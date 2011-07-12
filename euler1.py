z = 0
for x in range(1000):
	m = x + 1
	if m % 3 == 0 or m % 5 == 0:
		z = z + m
	print z