# WAP to check given no is palindrome or not. Original =Reverse


num=int(input('Enter Number'))

number=num
reverseNumber=0

while num>0:
      digit =num%10    
      reverseNumber=reverseNumber*10+digit       #to shift the digit to add new digit
      num//=10                                 
      
if number==reverseNumber:
    print(number,' is Palindrome Number')
else:
    print(number, ' is Not palindrome')
    
    
    

    '''
num>0      digit=num%10        r_n=r_n*10+d    num//=10       removes last digit
121>0      d=121%10=1          r=0*10+1=1      121//10=12
12>0       d=12%10=2           r=1*10+2=12     12//10=1
1>0        d=1%10=1            r=12*10+1=121   1//10=0
    '''
    
    



