import itertools

count = 0

for a in itertools.permutations(range(10)):
	print a
	count += 1
	if count == 1000000:
		break