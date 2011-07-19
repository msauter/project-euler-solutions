import time
s = time.time()

def revadd(num):
	snum = str(num)
	rsnum = snum[::-1]
	return int(snum) + int(rsnum)
	
lychrel = 0

for a in range(1, 10000):
	itrs = 0
	palin = False
	q = a
	while itrs < 50 and palin == False:
		tq = revadd(q)
		stq = str(tq)
		if stq == stq[::-1]:
			palin = True
		q = tq
		itrs += 1
		if itrs == 50:
			lychrel += 1
			
print lychrel
print time.time() - s