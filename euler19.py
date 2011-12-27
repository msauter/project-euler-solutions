#Problem 19
#14 June 2002
#You are given the following information, but you may prefer to do some researc
#h for yourself.   1 Jan 1900 was a Monday.  Thirty days has September, April,
# June and November. All the rest have thirty-one, Saving February alone, Which
# has twenty-eight, rain or shine. And on leap years, twenty-nine.  A leap year
# occurs on any year evenly divisible by 4, but not on a century unless it is
# divisible by 400.   How many Sundays fell on the first of the month during th
#e twentieth century (1 Jan 1901 to 31 Dec 2000)?
#
#----------


import time
s = time.time()

running_total = 0
day = 0

def sunday_check(n):
	sc = n % 7
	if sc == 6:
		return 1 
	else:
		return 0

for y in range(0, 101):
	for jan in range(31):
		day += 1
	running_total += sunday_check(day)
	if y % 4 != 0 or (y % 4 == 0 and (y + 1900) % 100 == 0 and (y + 1900) % 400 != 0):
		for feb in range(28):	
			day += 1
	else:
		for feb in range(29):
			day += 1
	running_total += sunday_check(day)
	for mar in range(31):
		day += 1
	running_total += sunday_check(day)
	for apr in range(30):
		day += 1
	running_total += sunday_check(day)	
	for may in range(31):
		day += 1
	running_total += sunday_check(day)
	for jun in range(30):
		day += 1
	running_total += sunday_check(day)	
	for jul in range(31):
		day += 1
	running_total += sunday_check(day)	
	for aug in range(31):
		day += 1
	running_total += sunday_check(day)	
	for sep in range(30):
		day += 1
	running_total += sunday_check(day)	
	for oct in range(31):
		day += 1
	running_total += sunday_check(day)	
	for nov in range(30):
		day += 1
	running_total += sunday_check(day)	
	for dec in range(31):
		day += 1
	running_total += sunday_check(day)
	if y == 0:
		running_total = 0
		
print running_total
print time.time() - s