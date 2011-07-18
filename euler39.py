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