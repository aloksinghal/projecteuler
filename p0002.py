
sum = 0
def get_next_two_fibbonaci(first,second):
	return second, first+second
curr_fibbonaci = 1
second = 1
while curr_fibbonaci < 4000000:
	if curr_fibbonaci %2 ==0:
		sum+= curr_fibbonaci
	second, curr_fibbonaci = get_next_two_fibbonaci(second,curr_fibbonaci)
	print second, curr_fibbonaci, sum

print sum