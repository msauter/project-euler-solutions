sum_sq = 0
sq_sum = 25502500
for a in range (1, 101):
	sum_sq = sum_sq + (a * a)
	
print "final: ", (sq_sum - sum_sq)