# -*- coding: utf-8 -*-
"""
Problem: Write a function that returns the number of unique words in a paragraph.


Input: "This is a test. This test is easy."


Output: 5 ({'this', 'is', 'a', 'test', 'easy'})

"""

paragraph="This is a test. This test is easy."

#words=set(paragraph.lower().split())

words=set(paragraph.lower().replace("."," ").split())

uniquewords=set(words)

print(len(words),uniquewords)
