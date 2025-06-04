class Product:
    def __init__(self,code="",name="",price=0.0):
        self.code=code
        self.name=name
        self.price=price
        
    def __str__(self):
        return f"code :{self.code},Name :{self.name},Price:{self.price :.2f}"
    
class ProductManager(Product):
    def __init__(self):
        self.products=[]                  #it can hold all the product class object
        
    def add_products(self):
        code=input("Enter code :")
        name=input("Enter name :")
        try:
            price =float(input("Enter Price :"))
        except ValueError:          #if the user input is ivalid we can handle error by this
            price =0.0              #when user not pass anything it gives 0.00
        self.products.append(Product(code,name,price))
        print("Product Added.\n")
        
    def list_products(self):
        if not self.products:           #checks list is not empty
            print("\n No Products found.\n")
        else:
            for p in self.products:         #loop iterate throght all products stored n list
                print(p)                    #print list
            print()
                      
    def find_products(self,code):
        for p in self.products:
            if p.code==code:
                return p
        return None
    
    def modify_products(self):
        code=input("enter code to modify :")
        p=self.find_products(code)
        if p:
            p.name=input("Enter new name")
            try:
                p.price=float(input("Enter new price:"))
            except ValueError:
                print("Invalid price")
            print("\nProduct Modified.\n")
        else:
            print("\nProduct not found")
        
    def delete_products(self):
        code=input("Enter code to delete :")
        p=self.find_products(code)
        if p:
            self.products.remove(p)
            print("\nProduct deleted.\n")
        else:
            print("\nProduct not found")
            
    def view_by_code(self):
        code=input("Enter code to view: ")
        p=self.find_products(code)
        if p:
            print(p,"\n")
        else:
            print("\nProduct not found")
            
            
manager=ProductManager()
while True:
      print("```````Products Menue````````````")
      print("\n1.Add\n2.List\n3.Modify\n4.Delete\n5.View by code\n6.Exit.")
      print("---------------------------------")
      choice=input("\nchoice:")
      if choice=='1':
          manager.add_products()
      elif choice=='2':
            manager.list_products()
      elif choice=='3':
            manager.modify_products()
      elif choice=='4':
            manager.delete_products()
      elif choice=='5':
            manager.view_by_code()
      elif choice=='6':
            print("Existing...")
            break
      else:
            print("Invalid Choice")

            
            
            
            
        