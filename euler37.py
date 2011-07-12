import time, math
s = time.time()

count = 0
pn = 11
p_sum = 0

def is_prime(num):
	isprime = True
	sp = int(math.sqrt(num)) + 1
	for x in range(2, sp):
		if (num % x == 0 and num != x):
			isprime = False
			break		
	if num == 1:
		isprime = False
	return isprime

def listize(n):
	n_string = str(n)
	n_list = []
	for b in range(len(n_string)):
		n_list.append(n_string[b])
	return n_list
	
while count < 11:
	if is_prime(pn):
		pnl = listize(pn)
		trunc_list = []
		if pnl[0] != 1 and pnl[-1] != 1:
			for a in range(len(pnl)):
				pn1 = ""
				pn2 = ""
				#print "a = ", a
				for c in range(a):
					pn1 += str(pnl[c])
					pn2 = str(pnl[-c - 1]) + pn2
					#print "c = ", c
					#print "pn1: ", pn1
					#print "pn2: ", pn2
				if pn1 == "":
					pn1 = 0
				if pn2 == "":
					pn2 = 0
				trunc_list.append(pn1)
				trunc_list.append(pn2)
				if is_prime(int(pn1)) == False or is_prime(int(pn2)) == False:
					break
				if a == len(pnl) - 1:
					count += 1
					p_sum += pn
					print pn
					print trunc_list
	pn += 2
	spn = str(pn)
	if spn[-1] == 1:
		pn +=2
	if spn[-1] == 9:
		pn += 4
	if spn[0] == 1:
		pn = 2 * (10 ** len(spn)) + 3
	if spn[0] == 9:
		pn = 2 * (10 ** (len(spn) + 1)) + 3
	
print p_sum
print time.time() - s