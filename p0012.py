import math

def get_nth_triangular_number(n):
	return (n*(n+1))/2

number_of_divisors_hashmap = {}
flag = False
n=1

def find_all_divisors_count(n):
	count = 0
	for i in range(1,int(math.sqrt(n)) + 1):
		if n%i==0:
			if i != math.sqrt(n):
				count += 2
			else:
				count += 1
	print n , count
	return count


while not flag:
	number = get_nth_triangular_number(n)
	if n %2 ==0:
		divisors_count = find_all_divisors_count(n/2) * find_all_divisors_count(n+1)
	else:
		divisors_count = find_all_divisors_count((n+1)/2) * find_all_divisors_count(n)
	if divisors_count >= 500:
		print number
		flag = True
	n += 1

