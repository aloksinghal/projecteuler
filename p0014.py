cache_dict = {}

i = 1
max_length = 1
retur_value = 0
def get_collatz_length(i):
	if i == 1:
		return 1
	elif i in cache_dict:
		return cache_dict[i]
	elif i%2==0:
	    collatzi =  1 + get_collatz_length(i/2)
	    cache_dict[i] = collatzi
	    return collatzi
	else:
		collatzi =  1 + get_collatz_length(3*i+1)
		cache_dict[i] = collatzi
		return collatzi 

while i < 1000000:
	collatz_length = get_collatz_length(i)
	print collatz_length,i
	if collatz_length>max_length:
		max_length = collatz_length
		return_value = i

	i += 1

print max_length,return_value
	



