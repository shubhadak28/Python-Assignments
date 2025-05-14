num = 1
for row in range(1, 5):
    for col in range(1, row + 1):
        print(num, end=" ")
        num += 1
    print()
    
    
'''
num=1  outer loop range(1,5)  = 1,2,3,4
       inner      range(1,row+1) = runs 1 to row  (iteration depens on the row)
       increamets num by 1
       
    
    i=1 inner loop j=1 print 1 then num=2
    o/p 1
    i=2
    inner j=1 print 2 num=3
    inner j=2 print=3 num=4
    o/p 2 3
    i=3
    inner =1 prnt 4 num=5
    j=2 print 5 num=6
    j=3 print 6 num=7
    o/p
    4 5 6
    
    i=4
    j=1 print 7 num=8
    j=2 print 8num=9
    j=3 print 9num=10
    j=4 print 10 num=11
    o/p
    7 8 9 10
    
    final 
    1
    2 3
    4 5 6 
    7 8 9 10
    
        
'''