def factorial(num):
	list = []
	x = num
	while (x>0):
		for x in range(num,-1,-1):
			list.append(x)
			
			# print(list)
	
	list2 = list[:-1]
	# print(list2)
	product = 1
	for y in list2:
		product *= y
	return product

# factorial(8)
# factorial(18)
# factorial(45)

