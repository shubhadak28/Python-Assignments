# -*- coding: utf-8 -*-
"""
9. Write a Python program to find the repeated items of a tuple

"""

tup=(8,6,8,4,3,4,2,7,8,1,3,1)

repeated= list({x for x in tup if tup.count(x)>1})
print(repeated)