import time
s = time.time()

def palin_check(z):
	z_str = str(z)
	rev_z = z_str[::-1]
	if z_str == rev_z:
		return True
	else:
		return False

palin_sum = 0
for a in range(1000000):
	if palin_check(a):
		a_bin = str(bin(a))
		print a
		print a_bin
		stripped_bin = a_bin[2:]
		print stripped_bin
		if palin_check(stripped_bin):
			palin_sum += a
			
print palin_sum
print time.time() - s