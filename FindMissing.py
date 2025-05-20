# -*- coding: utf-8 -*-
"""
Problem: Given two lists of integers where one is a subset of the other (with some elements missing), 
         find the missing elements using sets.


Input: original = [1, 2, 3, 4, 5], received = [2, 3, 5]


Output: {1, 4}

"""

original=[1,2,3,4,5]
received=[2,3,5]

missing=set(original).difference(set(received)) #difference finds unique from both sets

print('missing elemets are',missing)