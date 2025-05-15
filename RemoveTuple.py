# -*- coding: utf-8 -*-
"""
12. Write a Python program to remove an item from a tuple.

"""


tup=(1,4,6,7)

tupList=list(tup) #convert to list

tupList.remove(4)   
tu=tuple(tupList) #convert to tuple

print(tup)