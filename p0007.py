count = 0
n = 2
import math
def is_prime(n):
	if n==2:
		return True
	flag = True
	start = 2

	while start <= math.sqrt(n):
		if n % start ==0:
			flag = False
			return flag
		start += 1
	return flag

while count<10001:
	if is_prime(n):
		print n
		count += 1
	if count==10001:
		print n
	n +=1










