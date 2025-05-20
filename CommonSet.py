'''
Problem: Given two lists, return a set of elements common to both.


Input: [1, 2, 3, 4] and [3, 4, 5, 6]


Output: {3, 4}

'''

list1=[1,2,3,4]
list2=[3, 4, 5, 6]

common=set(list1).intersection(set(list2)) #to find common elements between two sets 
print(common)
