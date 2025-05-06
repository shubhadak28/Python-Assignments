'''
4.Accept the bike price from user & add road tax as follows
 
     Price > 80000   15 % TAX
     Price > 40000 & <80000  10% TAX
     Else                       5% TAX

'''

bikePrice = int(input("Enter the bike price: "))

if bikePrice > 80000:
    tax_percentage = 0.15
    
elif bikePrice > 40000 and bikePrice <= 80000:
    tax_percentage = 0.10
else:
    tax_percentage = 0.05

road_tax = bikePrice * tax_percentage

print("Road tax:", road_tax)
print("Total cost (bike price + road tax):", bikePrice + road_tax)
