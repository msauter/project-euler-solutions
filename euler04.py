raw_products = []
palindrome = False
check1 = 999
check2 = 999
while palindrome == False:
	product = check1 * check2
	product_string = str(product)
	palindrome = True
	if len(product_string) % 2 == 0:
		for a in range((len(product_string) / 2)):
			char = product_string[a]
			char2 = product_string[-(1+a)]
			print char, char2
			if char != char2:
				palindrome = False
	else:
		for b in range(((len(product_string) - 1) / 2)):
			char = product_string[b]
			char2 = product_string[-(1+b)]
			print char, char2
			if char != char2:
				palindrome = False
	print check1, check2, product
	if check2 != 913:
		check2 = check2 - 1
	else:
		check2 = 999
		check1 = check1 - 1