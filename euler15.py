#Problem 15
#19 April 2002
#Starting in the top left corner of a 2 2 grid, there are 6 routes (without
# backtracking) to the bottom right corner.     How many routes are there
# through a 20 20 grid?
#
#----------


import time
s = time.time()
size = 20
options = size * 2
n_fac = 1
k_fac = 1

for a in range(1, options + 1):
	n_fac = n_fac * a
	
for b in range(1, size + 1):
	k_fac = k_fac * b
	
print (n_fac/(k_fac * k_fac))
print time.time() - s