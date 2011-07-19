from fractions import Fraction

prod = 1

for a in range(1, 10):
	for b in range(1, 10):
		for c in range(1, 10):
			for d in range(1, 10):
				frac = Fraction((a * 10 + b), (c * 10 + d))
				if frac < 1 and (frac == Fraction(a, d) or frac == Fraction(b, c)) and (a == d or b == c):
					print (a * 10 + b), (c * 10 + d), frac
					prod = prod * frac
					
print Fraction(prod)