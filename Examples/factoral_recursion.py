def fact(n):

	if n == 0:
		return 1

	return n * fact(n-1) # 5 * (5-1)! 
						 # 5 * 4!  
						 # 5 * 4 * 3 * 2 * 1
						 # 120



result = fact(5)
print(result)

