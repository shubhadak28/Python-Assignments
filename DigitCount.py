#count digits of any number

num=int(input("Enter Number"))

count=0

#to check negative number manually positive
if num<0:
    num=-num   # num -(-9)= 9
    
# to count 0

if num==0:
    count=1
else:
    while num>0:  #10>0  
        count+=1  #count=0+1  
        num=num//10  #num=10//10 = 1
        
        
print("number of digits", count)