#Problem 17
#17 May 2002
#If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.  If all the
# numbers from 1 to 1000 (one thousand) inclusive were written out in words, ho
#w many letters would be used?   NOTE: Do not count spaces or hyphens. For
# example, 342 (three hundred and forty-two) contains 23 letters and 115 (one
# hundred and fifteen) contains 20 letters. The use of "and" when writing out
# numbers is in compliance with British usage.
#
#----------


import time
s = time.time()

one = 3
two = 3
three = 5
four = 4
five = 4
six = 3
seven = 5
eight = 5
nine = 4
ten = 3
eleven = 6
twelve = 6
thirteen = 8
fourteen = 8
fifteen = 7
sixteen = 7
seventeen = 9
eighteen = 8
nineteen = 8
twenty = 6
thirty = 6
forty = 5
fifty = 5
sixty = 5
seventy = 7
eighty = 6
ninety = 6
hundred = 7
thousand = 8

count = 0
for h in range(10):
	for a in range(1, 20):
		if a == 1 or a == 2 or a == 6 or a == 10:
			count += 3
		if a == 3 or a == 7 or a == 8:
			count += 5
		if a == 4 or a == 5 or a == 9:
			count += 4
		if a == 11 or a == 12:
			count += 6
		if a == 13 or a == 14 or a == 18 or a == 19:
			count += 8
		if a == 15 or a == 16:
			count += 7
		if a == 17:
			count += 9
		if h > 0:
			count += 3
			# accounting for the "and"
		if h == 1 or h == 2 or h == 6:
			count += (3 + hundred)
		if h == 3 or h == 7 or h == 8:
			count += (5 + hundred)
		if h == 4 or h == 5 or h == 9:
			count += (4 + hundred)
	for b in range(20, 100):
		c = 0
		if b >= 20 and b < 30:
			count += twenty
			c = 20
		if b >= 30 and b < 40:
			count += thirty
			c = 30
		if b >= 40 and b < 50:
			count += forty
			c = 40
		if b >= 50 and b < 60:
			count += fifty
			c = 50
		if b >= 60 and b < 70:
			count += sixty
			c = 60
		if b >= 70 and b < 80:
			count += seventy
			c = 70
		if b >= 80 and b < 90:
			count += eighty
			c = 80
		if b >= 90 and b < 100:
			count += ninety
			c = 90
		n = b - c
		if n == 1 or n == 2 or n == 6:
			count += 3
		if n == 3 or n == 7 or n == 8:
			count += 5
		if n == 4 or n == 5 or n == 9:
			count += 4
		
		if h > 0:
			count += 3
			# accounting for the "and"
			
		if h == 1 or h == 2 or h == 6:
			count += (3 + hundred)
		if h == 3 or h == 7 or h == 8:
			count += (5 + hundred)
		if h == 4 or h == 5 or h == 9:
			count += (4 + hundred)
			
	if h == 1 or h == 2 or h == 6:
		count += (3 + hundred)
	if h == 3 or h == 7 or h == 8:
		count += (5 + hundred)
	if h == 4 or h == 5 or h == 9:
		count += (4 + hundred)

count += (one + thousand)


print count
print time.time() - s