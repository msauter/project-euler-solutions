import time
s = time.time()
names_file = open("/Users/matthewsauter/python_programs/names.txt")
names_string = names_file.read()
b = 1
names_list = []
for a in range(len(names_string)):
	if names_string[a] == ",":
		temp_string = names_string[b:a-1]
		names_list.append(temp_string)
		b = a + 2
	if a == (len(names_string) - 1):
		temp_string = names_string[b:a]
		names_list.append(temp_string)
names_list.sort()
print names_list

running_total = 0

for c in range(len(names_list)):
	name_total = 0
	print c
	print names_list[c]
	for d in names_list[c]:
		number = ord(d) - 64
		name_total += number
	print name_total
	running_total += (name_total * (c + 1))
	
print "Total: ", running_total
print "in: ", time.time() - s