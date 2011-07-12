import time
s = time.time()
words_file = open("/Users/matthewsauter/python_programs/words.txt")
words_string = words_file.read()
b = 1
words_list = []
for a in range(len(words_string)):
	if words_string[a] == ",":
		temp_string = words_string[b:a-1]
		words_list.append(temp_string)
		b = a + 2
	if a == (len(words_string) - 1):
		temp_string = words_string[b:a]
		words_list.append(temp_string)
words_list.sort()
print words_list

words_score = []
highest = 0

for c in range(len(words_list)):
	word_total = 0
	print c
	print words_list[c]
	for d in words_list[c]:
		number = ord(d) - 64
		word_total += number
	if word_total > highest:
		highest = word_total
	print word_total
	words_score.append(word_total)
	
n = 1	
running_total = 0
e = 0
while e <= highest:
	e = (n * (n + 1)) / 2
	print e
	for f in words_score:
		if e == f:
			running_total += 1
	n = n + 1
	
print "Running total: ", running_total
print "in: ", time.time() - s