decimal = ""
expression = 1
for a in range(1, 1000001):
	decimal += str(a)
	
print decimal

for b in range(1, len(decimal)):
	if b == 10 or b == 100 or b == 1000 or b == 10000 or b == 100000 or b == 1000000:
		expression = expression * int(decimal[b - 1])
		
print expression