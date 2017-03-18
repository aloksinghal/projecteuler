def get_sum():
	sum = 0
	n=1
	while n<1000:
		if (n%3==0) or (n%5==0):
			sum+=n
		n+=1
	return sum

print get_sum()