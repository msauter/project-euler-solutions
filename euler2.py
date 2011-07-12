previous = 1
current = 1
fib = 1
running_count = 0
while fib <= 4000000:
	fib = current + previous
	print fib
	previous = current
	current = fib
	if fib % 2 == 0:
		running_count = running_count + fib
print "running count = ", running_count