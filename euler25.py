import time

s = time.time()
fib_n = 1
fib_n1 = 1
count = 3

while fib_n1 < 10**999:
	next_fib = fib_n + fib_n1
	fib_n = fib_n1
	fib_n1 = next_fib
	print next_fib
	print "count: ", count
	count += 1
	
print time.time() - s