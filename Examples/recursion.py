import sys
sys.setrecursionlimit(20)
print(sys.getrecursionlimit())

i = 0

def recur():
	global i
	i += 1
	print("Hello",i)
	recur()

recur()



