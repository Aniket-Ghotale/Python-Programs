from numpy import *
a=array([1,2,3,4,5])
b=array([5,4,3,2,1])
c=len(a)
for i in range(0,5):
    c = (a[i]+b[i])
print(c)

arr1 =array([1,2,3,4])
arr2 =array([5,6,7,3])
b = len(arr1)
for a in range (b):
    x = arr1[a]+ arr2[a]
    print (x,' ',end='')