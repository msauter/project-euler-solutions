import time
s = time.time()
size = 4
routes = 0
options = size * 2
matrix = []

for a in range(options - 1):
	for b in range(a + 1, options):
		for c in range(b + 1, options):
			for d in range(c + 1, options):
				new_matrix = []
				for z in range(options):
					new_matrix.append(0)
				new_matrix[a] = 1
				new_matrix[b] = 1
				new_matrix[c] = 1
				new_matrix[d] = 1
				matrix.append(new_matrix)
				routes += 1
				print new_matrix, "a = ", a, "b = ", b, "c = ", c, "d = ", d
		

print matrix
print "Routes: ", routes
print time.time() - s