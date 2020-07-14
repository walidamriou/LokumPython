"""
 ******************************************************************** 

  LokumPython
  To Learn Python Programming Language with small programs examples
  Project Website: LokumPython.walidamriou.com
  Github: https://github.com/walidamriou/LokumPython

  Copyright CC 2020 Walid Amriou
  This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License
   
  Last update: July 2020

 ******************************************************************** 
"""

from Parent_class import *

# Create Develeper as Child Class and use Person as parent class
class Develeper(Person):
  pass # Use the pass keyword when you do not want to add any other properties or methods to the class

# Create object from Person class (The parent class)
a = Person("Walid", 25)
a.print_person_info()

# create object from Develeper class (The child class) 
b = Develeper("Olaf", 25)
b.print_person_info()

# Use __init()__ to edit the properties of the child that Inherited from the parent
"""
When you add the __init__() function, the child class will no longer inherit the parent's
 __init__() function. That mean The child's __init__() function overrides the inheritance 
 of the parent's __init__() function.
"""
class Student1(Person):
    pass
    

# How to keep the inheritance of the parent's __init__() function

# There are two methodes
# method 1 using the name of the parent class

class Student2(Person):
  def __init__(self, name, age):
    Person.__init__(self, name, age)

# method 2 using the super() Function (without need to use the parent class name)
class Student3(Person):
  def __init__(self, name, age):
    super().__init__(name, age)

# Add Properties to child class after inherited all Properties and methodes from the parent class
class Student4(Person):
    def __init__(self,name,age,education_field):
        super().__init__(name,age)
        self.education_field=education_field # add new Properties
    
c = Student4("Walid",25,"electronics") 

# Add Methods
# we inherite the Student 4 to Student 5 and add a method to print the name, the age and the field 

class Student5(Student4):
    def __init__(self,name,age,education_field):
        super().__init__(name,age,education_field)
    def print_studient_info(self) :
        """
        Rememper to use self.person_name because Student4 use the person_name and person_age
        as Properties from the parent_class (inherated it), and Student5 inherated all Properties
        from Student4 so it inherated person_name, person_age and education_field  
        """
        print("The name of this student is", self.person_name,", the age is ", self.person_age,"The field of the education is",self.education_field)

d = Student5("Olfa",25,"Mobile")
d.print_studient_info()