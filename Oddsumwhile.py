#sum of odd numbers  1 to n

num=int(input("enter number"))

sumOdd=0

a=1

while a<=num:
    if a%2!=0:
        sumOdd+=a
    a+=1
    
print("Sum of all odd numbers between 1 to", num, "is",sumOdd)