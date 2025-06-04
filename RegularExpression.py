import re

text = "Hello World"
result = re.match(r"Hello", text)
print(result.group() if result else "No match")


text = "Say Hello to the World"
result = re.search(r"Hello", text)
print(result.group() if result else "No match")


text = "One: 1, Two: 2, Three: 3"
numbers = re.findall(r"\d", text)
print(numbers)


text = "AB12 CD34 EF56"
matches = re.finditer(r"\d+", text)
for match in matches:
    print(match.group())



text = "Today is 04-06-2025"
new_text = re.sub(r"\d{2}-\d{2}-\d{4}", "DATE", text)
print(new_text)


text = "apple,banana;grape orange"
parts = re.split(r"[ ,;]+", text)
print(parts)
