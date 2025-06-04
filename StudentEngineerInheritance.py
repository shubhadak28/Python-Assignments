class Student:
      def __init__(self,name,roll_no,sub1,sub2,sub3):
          self._name =name
          self._roll_no=roll_no
          self._sub1=sub1
          self._sub2=sub2
          self._sub3=sub3
          
      def calculae_percentage(self):
          total=self._sub1+self._sub2+self._sub3
          outOf=300
          return (total/outOf)*100
      
      def __str__(self):
          return(f"Nmae :{self._name},Roll No :{self._roll_no},"
                 f"Percentage :{self.calculae_percentage(): .2f}%")
          

class EngineerStud(Student):
    def __init__(self,name,roll_no,sub1,sub2,sub3,branch):
        super().__init__(name,roll_no,sub1,sub2,sub3)
        self._branch=branch
        
    def __str__(self):
        return f"{super().__str__()}, Branch :{self._branch}"
    
    
student1= EngineerStud("Krishna", 21, 88, 98, 87, "Computer")
print(student1)
          
         