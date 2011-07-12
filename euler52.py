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