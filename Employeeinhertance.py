class Employee:
    def __init__(self,name,salary):
        self._name=name
        self._salary=salary
        
    '''   
    def display(self):
        print(f"Name:{self.name}")
        print(f"Salary :{self.salary}")
    '''
    def __str__(self):
        return f"Name:{self._name},Salary :{self._salary}"
    
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
        
    '''    
    def display(self):
        super().display()
        print(f"Department :{self.department}")    
    '''
    
    def __str__(self):
        base=super().__str__()
        return f"{base},Department: {self.department}"

emp= Employee("Shan", 45000)    
mgr=Manager("Joe", 550000, "IT")

print("Employee Information")
print(emp)

print("\nManager Information")
print(mgr)