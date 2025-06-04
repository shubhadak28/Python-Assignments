class NameException(Exception):                  #custom Exception class inherits Exception class
      
    def __init__(self,message="Name is Require"):       #custom msg
        super().__init__(message)
        
class User:
    def accpet(self,name):
        if name:                      #checks if name is not empty print if exists
            self.name=name
        else:
            raise NameException("Name is require")
            
    def __str__(self):
        return f"Name of user is {self.name}"

    
    
user1=User()       

try:
    user1.accpet("")       #empty name for give exception
except NameException() as e:
    print("Error",e)
else:
    print(user1)               #if not any excpetion then print user
        