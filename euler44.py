#Unsolved
#
#
#
#
#--------------------------



pent_list = []

for a in range(1, 5000):
	pent_a = a*(3*a - 1)/2
	print pent_a
	pent_list.append(pent_a)
	
pent_d_list = []
	
for b in range(len(pent_list)):
	print b
	for c in range(b, len(pent_list)):
		pent_sum = pent_list[b] + pent_list[c]
		pent_diff = pent_list[c] - pent_list[b]
		if (pent_sum in pent_list) and (pent_diff in pent_list):
			pent_d_list.append(pent_diff)

print sorted(pent_d_list)