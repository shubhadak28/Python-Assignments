#3.Python program to replace the string space with a given character.


def replace_space_with_character(input_string, replacement_char):
 
  return input_string.replace(" ", replacement_char)

string_input = "This is a string"
char_input = "_"
output_string = replace_space_with_character(string_input, char_input)
print(output_string)