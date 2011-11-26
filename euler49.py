import math, itertools
prime_list = []

for p in range(1001, 10000, 2):
	isprime = True
	sp = int(math.sqrt(p)) + 1
	for x in range(2, sp):
		if (p % x == 0 and p != x):
			isprime = False
			break
	if isprime == True:
		print p
		prime_list.append(p)
		
print prime_list

perm_of_prime = []

for n in prime_list:
	str_n = str(n)
	dig = []
	for s in str_n:
		dig.append(int(s))
	print dig
	p_list = [n]
	perm = False
	for i in itertools.permutations(dig):
		i2 = 1000*i[0] + 100*i[1] + 10*i[2] + i[3]
		print i2
		for b in prime_list:
			if i2 == b and i2 !=n:
				add = True
				perm = True
				for c in p_list:
					if c == i2:
						add = False
				if add == True:
					p_list.append(i2)
	if perm == True:
		perm_of_prime.append(p_list)
		
print perm_of_prime

final_list = []

for pp in perm_of_prime:
	pps = sorted(pp)
	print pps
	for w in range(len(pps) - 2):
		increment = pps[w+1] - pps[w]
		if (pps[w+1] + increment) == pps[w+2]:
			final_list.append(pps)
				
print final_list