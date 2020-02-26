#pass list to function
def count(fst):
	even = 0
	odd = 0

	for i in fst:

		if i%2 == 0:
			even +=1
		else:
			odd +=1

	return even,odd


fst = [20,25,14,19,16,24,28,47,26]

even,odd = count(	fst)

print("Even : {} and Odd : {}".format(even,odd))