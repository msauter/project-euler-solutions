import time
s = time.time()
sum_list = []
for a in range(10):
	for b in range(10):
		for c in range(10):
			for d in range(10):
				for e in range(10):
					for f in range(10):
						number = a * 100000 + b * 10000 + c * 1000 + d * 100 + e * 10 + f
						fifth_sum = a**5 + b**5 + c**5 + d**5 + e**5 + f**5
						if number == fifth_sum and number > 1:
							sum_list.append(number)

print sum_list
final_sum = 0
for g in sum_list:
	final_sum += g
print final_sum
print time.time() - s