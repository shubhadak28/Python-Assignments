'''

5. Write a Python program to count the number 
   of strings where the string length is 2 or more
   and the first and last character are same from a given list of strings.

'''

lists=["hello","bye","python","learning","good"," aa","121"]

count=0
for s in lists:
    if len(s) >=2 and s[0] == s[-1]:
        count+=1
        
print("number of strings where the string length is 2 or more", count)