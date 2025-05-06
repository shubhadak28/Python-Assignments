#8. Write a Python program to enter P, T, R and calculate Simple Interest.

P=int(input('Enter Principal'))

T=int(input('Enter Time'))

R=int(input('Enter Rate'))

SimpleInterest = (P * R * T) / 100

print("Simple Interest is ",SimpleInterest)