#Python program to count alphabets, digits and special characters.

s = "Hello123!"
l_c = 0
d_c = 0

for char in s:
  
    if char.isalpha():  
        l_c += 1
        
    elif char.isdigit(): 
        d_c += 1

print(f"Letters: {l_c}")
print(f"Digits: {d_c}")