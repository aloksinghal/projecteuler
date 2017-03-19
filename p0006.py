def find_sum_of_squares(start, end):
	sum = 0
	while start <= end:
		sum += (start*start)
		start +=1
	return sum
	
def find_square_of_sum(start,end):
	sum = 0
	while start<=end:
		sum+= start
		start +=1
	return sum**2

sum_of_squares = find_sum_of_squares(1,100)
square_of_sum = find_square_of_sum(1,100)

print square_of_sum - sum_of_squares