#Problem 48
#18 July 2003
#The series, 1 1 + 2 2 + 3 3 + ... + 10 10 = 10405071317.  Find the last ten
# digits of the series, 1 1 + 2 2 + 3 3 + ... + 1000 1000 .
#
#----------

import time
s = time.time()

sum = 0
for a in range(1, 1001):
	print a
	sum += a**a

print sum
print time.time() - s