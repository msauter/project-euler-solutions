import time
s = time.time()

mds = 0
for a in range(1, 100):
	for b in range(1, 100):
		num = a ** b
		str_num = str(num)
		dig_sum = 0
		for c in range(len(str_num)):
			dig_sum += int(str_num[c])
		if dig_sum > mds:
			mds = dig_sum
			
print mds
print time.time() - s