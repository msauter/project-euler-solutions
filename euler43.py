import itertools

pan_sum = 0

for a in itertools.permutations(range(10)):
	print a
	str_a = ''
	for b in range(len(a)):
		str_a += str(a[b])
	print str_a
	d2 = 100*int(str_a[1]) + 10*int(str_a[2]) + int(str_a[3])
	d3 = 100*int(str_a[2]) + 10*int(str_a[3]) + int(str_a[4])
	d4 = 100*int(str_a[3]) + 10*int(str_a[4]) + int(str_a[5])
	d5 = 100*int(str_a[4]) + 10*int(str_a[5]) + int(str_a[6])
	d6 = 100*int(str_a[5]) + 10*int(str_a[6]) + int(str_a[7])
	d7 = 100*int(str_a[6]) + 10*int(str_a[7]) + int(str_a[8])
	d8 = 100*int(str_a[7]) + 10*int(str_a[8]) + int(str_a[9])
	if d2 % 2 == 0 and d3 % 3 == 0 and d4 % 5 == 0 and d5 % 7 == 0 and d6 % 11 == 0 and d7 % 13 == 0 and d8 % 17 == 0:
		pan_sum += int(str_a)
		print "Yeeeeeeeaaaaaaaahhhhhhhhh it's: ", str_a
		
print pan_sum