#WAP to print table of given no


num=int(input('Enter Number '))

print("Table of ",num)

i=1
while i<=10:
    print(f"{num} * {i} ={num*i}")
    i+=1
    
    
'''
    
i=1             i<=10               num*i        i+=1
1               1<=10               2*1=2        1+1=2
2               2<=10               2*2=4        2+1=3
3               3<=10               2*3=6        3+1=4
4


10            10<=10                2*10=20     10+1=11
11             false

    '''