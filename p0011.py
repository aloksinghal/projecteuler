array = []
with open("p0011_input.txt", "r") as ins:
    for line in ins:
    	split_line = [float(i) for i in  line.strip("\n").split(" ")]
        array.append(split_line)

maxProduct = 0

for i in range(0, len(array)):
	for j in range(0, len(array)):
	
		try:
			product = array[i][j] * array[i][j+1] * array[i][j+2] * array[i][j+3]
			if product > maxProduct:
				maxProduct = product
		except Exception as e:
			pass
		try:
			product = array[i][j] * array[i+1][j] * array[i+2][j] * array[i+3][j]
			if product>maxProduct:
				maxProduct = product
		except Exception as e:
			pass
		try:
			product = array[i][j] * array[i+1][j+1] * array[i+2][j+2] * array[i+3][j+3]
			if product>maxProduct:
				maxProduct = product
		except Exception as e:
			pass
		try:
			product = array[i][j] * array[i+1][j-1] * array[i+2][j-2] * array[i+3][j-3]
			if product>maxProduct:
				maxProduct = product
		except Exception as e:
			pass
print maxProduct