# write a code to dfind a factorial of 
# agiven number.
no=int(input("Enter any number: "))
fact=1
for n in range(no,1,-1):
    fact=fact*n
print("The factorial of ",no," is: ",fact)