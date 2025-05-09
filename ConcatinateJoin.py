#Python program to concatenate two strings using join() method.


def concatenate_strings(str1, str2):
    return "".join([str1, str2])

string1 = "Hello"
string2 = "World"
result = concatenate_strings(string1, string2)
print(result)  
