# -*- coding: utf-8 -*-
"""
9. Write a Python program to print a specified list
  after removing the 0th, 4th and 5th elements. Go to the editor


"""
remove=[0,4,5]

lists=["hi","Here","goods""laughter","byee","smile"]

for index in sorted(remove, reverse=True):
    lists.pop(index)
    
print ("updated lits:",lists)