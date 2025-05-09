#Python program to replace the string space with a given character using replace() method.


def replace_space_with_character(input_string, replacement_char):
 
  new_string = input_string.replace(" ", replacement_char)
  return new_string

my_string = "This is a string using function"
new_character = "_"
modified_string = replace_space_with_character(my_string, new_character)
print(modified_string) 

