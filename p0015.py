n = 20
paths = 1

for i in range (0, n):
	paths = paths *  ((2 * n) - i)
	paths = paths/(i + 1)

print paths