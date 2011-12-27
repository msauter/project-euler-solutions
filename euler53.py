#Problem 53
#26 September 2003
#There are exactly ten ways of selecting three from five, 12345:  123, 124, 125
#, 134, 135, 145, 234, 235, 245, and 345  In combinatorics, we use the notation
#, 5 C 3 = 10.  In general,     n C r =  n ! r !( n r )!  ,where r   n , n ! = 
#n ( n 1) ... 3 2 1, and 0! = 1.     It is not until n = 23, that a value
# exceeds one-million: 23 C 10 = 1144066.  How many, not necessarily distinct,
# values of n C r , for 1  n  100, are greater than one-million?
#
#----------


import time
s = time.time()

def fac(q):		
	factorial = 1
	for n in range(1, q + 1):
		factorial = factorial*n
	return factorial
	
count = 0
	
for a in range(1, 101):
	for r in range(1, a):
		comb = (fac(a)) / (fac(r) * fac(a - r))
		if comb > 1000000:
			count += 1
			
print count
print time.time() - s