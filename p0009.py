a = 0
b = 0

while a < 500:
	while b < 500:
		c = 1000 - a - b
		#print a,b,c
		if (a*a + b*b == c*c):
			print a*b*c
			print a, b, c
			break
		b += 1
	a+=1
	b = 0	