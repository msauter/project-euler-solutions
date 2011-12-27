#Problem 52
#12 September 2003
#It can be seen that the number, 125874, and its double, 251748, contain
#exactly the same digits, but in a different order.  Find the smallest positive
# integer, x , such that 2 x , 3 x , 4 x , 5 x , and 6 x , contain the same
# digits.
#
#----------


import time
s = time.time()

order = False
a = 2

def listize(n):
	n_string = str(n)
	n_list = []
	for b in range(len(n_string)):
		n_list.append(n_string[b])
	n_list.sort()
	return n_list
	
while order == False:
	if listize(a) == listize(2 * a) == listize(3 * a) == listize(4 * a) == listize(5 * a) == listize(6 * a):
		order = True
	a += 1
	
print a - 1
print time.time() - s