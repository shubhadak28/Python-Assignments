#sum of even numbers  1 to n

num=int(input("enter number"))

sumEven=0

a=1

while a<=num:
    if a%2==0:
        sumEven+=a
    a+=1
    
print("Sum of all even numbers between 1 to", num, "is",sumEven)