def person(name,**data):

	print(name)
	for i,j in data.items():
		print(i,j)

person("Aniket",age=28,city="mumbai",mobile=9975487763)