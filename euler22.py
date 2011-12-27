#Problem 22
#19 July 2002
#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name
# score.  For example, when the list is sorted into alphabetical order, COLIN,
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
# COLIN would obtain a score of 938 53 = 49714.  What is the total of all the
# name scores in the file?
#
#----------


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