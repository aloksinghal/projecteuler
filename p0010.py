from utils import *

i = 2
sum_prime = 0
excluded_number_list = set()

def get_multiples_upto_n(num, n):
	multiplier = 2
	return_set = set()
	while num * multiplier < n :
		return_set.add(num*multiplier)
		multiplier += 1
	return return_set

while i < 2000000:
	print i
	#print excluded_number_list
	if i not in excluded_number_list:
		if is_prime(i):
			sum_prime += i
			multiples = get_multiples_upto_n(i,2000000)
			for multiple in multiples:
				excluded_number_list.add(multiple)
	i += 1
print sum_prime

