#Unsolved
#
#Problem 79
#17 September 2004
#A common security method used for online banking is to ask the user for three
# random characters from a passcode. For example, if the passcode was 531278,
# they may ask for the 2nd, 3rd, and 5th characters; the expected reply would
# be: 317.  The text file, keylog.txt , contains fifty successful login
# attempts.  Given that the three characters are always asked for in order,
# analyse the file so as to determine the shortest possible secret passcode of
#
#----------

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
				