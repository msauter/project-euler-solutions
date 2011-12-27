#Problem 42
#25 April 2003
#The n th term of the sequence of triangle numbers is given by, t n = n ( n +1)
#; so the first ten triangle numbers are:  1, 3, 6, 10, 15, 21, 28, 36, 45, 55,
# ...  By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value. For
# example, the word value for SKY is 19 + 11 + 25 = 55 = t 10 . If the word
# value is a triangle number then we shall call the word a triangle word.  Usin
#g words.txt (right click and 'Save Link/Target As...'), a 16K text file
# containing nearly two-thousand common English words, how many are triangle
#
#----------

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