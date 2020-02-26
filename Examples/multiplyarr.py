# Write a code to multiply
# Matrices using 2D array and using loops
from numpy import *

A = ([
		[1,2,3],
		[4,5,6]

	])
for row in A:
	for col in row:
		print(col ,end="")