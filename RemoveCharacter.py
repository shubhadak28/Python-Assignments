#1.Python program to remove given character from String.


def remove_char(input_string, char_to_remove):

  
  new_string = input_string.replace(char_to_remove, "")
  return new_string

string = "Hello, World!"
char_to_remove = ","
result = remove_char(string, char_to_remove)
print(result)

