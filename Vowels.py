'''
Problem: Write a function that returns the number of unique vowels in a word.


Input: "education"


Output: 5
'''

word='education'
vowels=set("aeiou")

uniqueVowels=set(word).intersection(vowels) #find common from both sets

print(uniqueVowels)
print(len(uniqueVowels))