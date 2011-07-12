import time
s = time.time()

sum = 0
for a in range(1, 1001):
	print a
	sum += a**a

print sum
print time.time() - s