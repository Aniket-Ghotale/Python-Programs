""" Global vs Local variable
Global variable means outside the function
Local variable means inside the function"""

a = 10
print(id(a))
def something():
	a = 9

	x = globals()['a']
	print(id(x))
	print("In function",a)

	globals()['a'] = 15

something()
print("outside",a)