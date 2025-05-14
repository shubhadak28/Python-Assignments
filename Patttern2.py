'''
           1
         1 2
      1 2 3 
   1 2 3 4
1 2 3 4 5 

'''

row=5
for i in range(1,row+1):
    
    for space in range(row-i):
        print(" ",end=" ")
        
    for num in range (1,i+1):
        print(num,end=" ")
    print()
    
'''
outer from 1 to 5 
represenr currebt row
i=1
spae 5-1=4 print 4 spc
num =1 o/p              1

i=2
spc 3
num 1 2 
 o p      1 2
 
 
 i=3 
 spc 2
 num 1 2 3
 i=4 
 space 1 
 1234
 i=5 spc 0 
 12345
'''