import itertools, math

def convert(l):
	lsum = ''
	for b in l:
		lsum += str(b)
	return int(lsum)
	
def is_prime(p):
	isprime = True
	sp = int(math.sqrt(p)) + 1
	for x in range(2, sp):
		if (p % x == 0 and p != x):
			isprime = False
			break
	return isprime

for a in itertools.permutations('7654321', 7):
	number = convert(a)
	print number
	if is_prime(number):
		print "It's prime!  And the number is... ", number
		break
	