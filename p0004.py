def is_palindrome(number):
	number = str(number)
	new_number = number[::-1]
	if new_number==number:
		return True
	return False

i = 999
j = 999

max_palindrome = 0

while (i>1):
	pal_flag = False
	j=999
	while(j>1):
		pal_flag = is_palindrome(i*j)
		if pal_flag:
			current_largest = i * j
			if current_largest>max_palindrome:
				max_palindrome=current_largest
		j-=1
	i-=1

print max_palindrome