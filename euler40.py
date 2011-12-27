#Problem 40
#28 March 2003
#An irrational decimal fraction is created by concatenating the positive
# integers:  0.12345678910 1 112131415161718192021...  It can be seen that the
# 12 th digit of the fractional part is 1.  If d n represents the n th digit of
# the fractional part, find the value of the following expression.  d 1   d 10 
#  d 100   d 1000   d 10000   d 100000   d 1000000
#
#----------

decimal = ""
expression = 1
for a in range(1, 1000001):
	decimal += str(a)
	
print decimal

for b in range(1, len(decimal)):
	if b == 10 or b == 100 or b == 1000 or b == 10000 or b == 100000 or b == 1000000:
		expression = expression * int(decimal[b - 1])
		
print expression