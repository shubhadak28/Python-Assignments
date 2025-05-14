# -*- coding: utf-8 -*-
"""
7. Write a Python program to find the list of words
   that are longer than given words

"""


words=["shubhada","hi","learniing","python"]

length=int(input("enter length to compare"))
longWords =[]

for w in words:
    if len(w) >length:
        longWords.append(w)

print(f"words longer than {length} characters :",longWords)