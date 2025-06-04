num1=int(input('Enter 1st Number'))

num2=int(input('Enter 2nd  Number'))

print('1. addition')
print('2. substraction')
print('3. multiplication')
print('4. division')
print('5. mod')
print('6. exponentation')
print('7. floor division')
print("8.Go to main menu")

opt=int(input('---------select your option-------'))

match opt:
        case 1: print("Addition",num1+num2)
        case 2: print("substraction",num1-num2)
        case 3: print("multiplication",num1*num2)
        case 4: print("division",num1/num2)
        case 5: print("mod",num1%num2)
        case 6: print("exponentation",num1**num2)
        case 7: print("floor division",num1//num2)
        case 8:print ("Here is the Main Menue")
        case default: print("Enter valid Option")

            
