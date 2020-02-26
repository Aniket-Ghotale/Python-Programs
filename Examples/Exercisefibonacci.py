#print first 50 fibonacci numbers...

list1 = [0, 1]
for i in range(48):
    list1.append(list1[-1]+list1[-2])
print('bye')
print(list1)