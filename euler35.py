import time, math
s = time.time()

def is_prime(num):
	isprime = True
	sp = int(math.sqrt(num)) + 1
	for x in range(2, sp):
		if (num % x == 0 and num != x):
			isprime = False
			break
	if isprime == True:
		print num
		if num < 10:
			prime_list.append(num)
		
	return isprime

prime_list = [2]

for p in range(3, 10 ,2):
	isprime = True
	is_prime(p)
		
print prime_list
		
for g in range(1, 10, 2):
	for h in range(1, 10, 2):
		number = g * 10 + h
		if is_prime(number):
			number2 = h * 10 + g
			if is_prime(number2):
				prime_list.append(number)
				prime_list.append(number2)
		
for f in range(1, 10, 2):	
	for g in range(1, 10, 2):
		for h in range(1, 10, 2):
			number = f * 100 + g * 10 + h
			if is_prime(number):
				number2 = h * 100 + f * 10 + g
				if is_prime(number2):
					number3 = g * 100 + h * 10 + f
					if is_prime(number3):
						prime_list.append(number)
						prime_list.append(number2)
						prime_list.append(number3)
		
for e in range(1, 10, 2):
	for f in range(1, 10, 2):	
		for g in range(1, 10, 2):
			for h in range(1, 10, 2):
				number = e * 1000 + f * 100 + g * 10 + h
				if is_prime(number):
					number2 = h * 1000 + e * 100 + f * 10 + g
					if is_prime(number2):
						number3 = g * 1000 + h * 100 + e * 10 + f
						if is_prime(number3):
							number4 = f * 1000 + g * 100 + h * 10 + e
							if is_prime(number4):
								prime_list.append(number)
								prime_list.append(number2)
								prime_list.append(number3)
								prime_list.append(number4)
		
for d in range(1, 10, 2):
	for e in range(1, 10, 2):
		for f in range(1, 10, 2):	
			for g in range(1, 10, 2):
				for h in range(1, 10, 2):
					number = d * 10000 + e * 1000 + f * 100 + g * 10 + h
					if is_prime(number):
						number2 = h * 10000 + d * 1000 + e * 100 + f * 10 + g
						if is_prime(number2):
							number3 = g * 10000 + h * 1000 + d * 100 + e * 10 + f
							if is_prime(number3):
								number4 = f * 10000 + g * 1000 + h * 100 + d * 10 + e
								if is_prime(number4):
									number5 = e * 10000 + f * 1000 + g * 100 + h * 10 + d
									if is_prime(number5):
										prime_list.append(number)
										prime_list.append(number2)
										prime_list.append(number3)
										prime_list.append(number4)
										prime_list.append(number5)
		
for c in range(1, 10, 2):
	for d in range(1, 10, 2):
		for e in range(1, 10, 2):
			for f in range(1, 10, 2):	
				for g in range(1, 10, 2):
					for h in range(1, 10, 2):
						number = c * 100000 + d * 10000 + e * 1000 + f * 100 + g * 10 + h
						if is_prime(number):
							number2 = h * 100000 + c * 10000 + d * 1000 + e * 100 + f * 10 + g
							if is_prime(number2):
								number3 = g * 100000 + h * 10000 + c * 1000 + d * 100 + e * 10 + f
								if is_prime(number3):
									number4 = f * 100000 + g * 10000 + h * 1000 + c * 100 + d * 10 + e
									if is_prime(number4):
										number5 = e * 100000 + f * 10000 + g * 1000 + h * 100 + c * 10 + d
										if is_prime(number5):
											number6 = d * 100000 + e * 10000 + f * 1000 + g * 100 + h * 10 + c
											if is_prime(number6):
												prime_list.append(number)
												prime_list.append(number2)
												prime_list.append(number3)
												prime_list.append(number4)
												prime_list.append(number5)
												prime_list.append(number6)
		
prime_list = list(set(prime_list))
prime_list.sort()

print prime_list
print len(prime_list)
print "time: ", time.time() - s