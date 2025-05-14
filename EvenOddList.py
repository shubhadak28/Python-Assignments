'''
3. WAP to create a list such that new list
 contains alternate even and odd from given list
'''

lists=[1,2,3,4,5,6,7,8,44,33,22,234,11]

even=[num for num in lists if num%2==0]
odd=[num for num in lists if num%2!=0]

print ("Original list ",lists)
print("even lists",even)
print("odd lists",odd)