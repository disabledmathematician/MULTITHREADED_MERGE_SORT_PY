# Charles Thomas Wallace Truscott Watters

from math import floor
def bs(L):
	s = {}
	for x in range(len(L)):
		s[floor(L[x] * 10 ** 1) % 11] = []
	for x in range(len(L)):
		s[floor(L[x] * 10 ** 1) % 11].append(L[x])
	print(s)
L = [0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00, 1.05]
bs(L)