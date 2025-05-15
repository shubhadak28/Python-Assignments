'''
16. Write a Python program to sort list of tuple based on sum
Input: [(4, 5), (2, 3), (6, 7), (2, 8)]
Output: [(2, 3), (4, 5), (2, 8), (6, 7)]"
'''

def sumtuple(tup):
    return sum(tup)

tup=[(4, 5), (2, 3), (6, 7), (2, 8)]

sort=sorted(tup,key=sumtuple)
print(sort)
