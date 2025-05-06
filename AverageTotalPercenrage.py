#7. Write a Python program to enter marks of five subjects and calculate total,
 
#average and percentage.


sub1=int(input('Enter Subject1 marks'))
sub2=int(input('Enter Subject2 marks'))
sub3=int(input('Enter Subject3 marks'))
sub4=int(input('Enter Subject4 marks'))
sub5=int(input('Enter Subject5 marks'))

total=sub1+sub2+sub3+sub4+sub5

print('total is ',total)

average=total/5

print("average is ",average)

percentage=total/500*100

print('Percentage is ',percentage)
