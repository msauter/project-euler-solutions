#Unsolved
#
#
#
#
#--------------------------

import time, itertools
s = time.time()
key_file = open("/Users/matthewsauter/python_programs/Project-Euler-Solutions/keylog.txt")
key_string = key_file.read()

print key_string

key_list = []
for a in range(0, len(key_string), 5):
	key_list.append(key_string[a: a + 3])
	
print key_list

for b in itertools.combinations(key_list, 2):
	print b
	cl1 = []
	cl2 = []
	for d in range(3):
		cl1.append(int(b[0][d]))
	for d in range(3):
		cl2.append(int(b[1][d]))
	print cl1, cl2
	for e in range(3):
		for f in range(3):
			if cl1[e] == cl2[f]:
				