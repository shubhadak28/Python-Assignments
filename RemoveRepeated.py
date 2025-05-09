#Python program to remove repeated character from string.


input_string = input("Enter the string: ")
unique_chars = {}
for char in input_string:
    if char not in unique_chars:
        unique_chars[char] = True
result = ''.join(unique_chars.keys())
print(result)