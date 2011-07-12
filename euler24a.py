import itertools

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print list(itertools.permutations(digits))[1000000]