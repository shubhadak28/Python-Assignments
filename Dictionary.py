d={}
print(type(d))

myD={ "name":"XYZ","age":45,"city":"Pune"}

print(myD)

myD["age"]=34
myD["email"]="abc@gmail.com"

print(myD.get("name","not found"))
print(myD.get("contact","not found"))

print(myD)

del myD["age"]

print("\nafter delete",myD)

for key,value in myD.items():
    print('key=',key,'value=',value)
    

for k in myD.keys():
    print(k)
 
    
for v in myD.values():
    print(v)

    
    
    