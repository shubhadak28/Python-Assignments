#Python program to concatenate two strings without using join() method.


def concatenate_strings(str1, str2):
  result = str1 + str2
  return result

string1 = "Hello"
string2 = "World"
concatenated_string = concatenate_strings(string1, string2)
print(concatenated_string) 
