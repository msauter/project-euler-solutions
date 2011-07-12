count = 0
for a in range(1):
	if a * 200 == 200:
		count += 1
	for b in range(2):
		if a * 200 + b * 100 == 200:
			count += 1
		for c in range(4):
			if a * 200 + b * 100 + c * 50 == 200:
				count += 1
			for d in range(10):
				if a * 200 + b * 100 + c * 50 + d * 20 == 200:
					count += 1
				for e in range(20):
					if a * 200 + b * 100 + c * 50 + d * 20 + e * 10 == 200:
						count += 1
					for f in range(40):
						if a * 200 + b * 100 + c * 50 + d * 20 + e * 10 + f * 5 == 200:
							count += 1
						for g in range(100):
							if a * 200 + b * 100 + c * 50 + d * 20 + e * 10 + f * 5 + g * 2 == 200:
								count += 1
							for h in range(200):
								if a * 200 + b * 100 + c * 50 + d * 20 + e * 10 + f * 5 + g * 2 + h == 200:
									count += 1
									
print count