#2.Python Program to count occurrence of a given characters in string.


def count_char_occurrences(input_string, char):

  count = 0
  for c in input_string:
    if c == char:
      count += 1
  return count

input_string = input("Enter a string: ")
char_to_count = input("Enter the character to count: ")

occurrences = count_char_occurrences(input_string,char_to_count)

print("The character string",input_string,"Apperes occurence ",occurrences)