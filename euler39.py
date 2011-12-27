#Problem 39
#14 March 2003
#If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.  {20,48,52},
# {24,45,51}, {30,40,50}  For which value of p  1000, is the number of solution
#s maximised?
#
#----------


import math, time
s = time.time()

largest = 0
p_val = 0

for p in range(3, 1001):
	count = 0
	for a in range(1, p - 1):
		for b in range(1, a - 1):
			c = math.sqrt(a*a + b*b)
			if a + b + c == p:
				count += 1
				trip = [a, b, c]
				print trip
	if count > largest:
		largest = count
		p_val = p
				
print p_val
print time.time() - s