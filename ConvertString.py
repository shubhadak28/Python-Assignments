"""
6. Write a Python program to convert a tuple to a string.

"""

tup=('hi','python','learn')

result=' '.join(tup)

print(result)



t1=(1,5,7,'python','easy','learning')

res=' '.join(str(val) for val in t1) #convert each element of the tuple to string
                                      # join() combines strin and seperate by space 
print(res)
