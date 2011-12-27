#Problem 56
#07 November 2003
#A googol (10 100 ) is a massive number: one followed by one-hundred zeros; 100
# 100 is almost unimaginably large: one followed by two-hundred zeros. Despite
# their size, the sum of the digits in each number is only 1.  Considering
# natural numbers of the form, a b , where a, b  100, what is the maximum
# digital sum?
#
#----------


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