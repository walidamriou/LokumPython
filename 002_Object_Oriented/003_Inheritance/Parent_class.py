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
class Person:
  def __init__(self, name, age):
    self.person_name = name
    self.person_age = age

  def print_person_info(self):
    print("The name of this person is", self.person_name,"and the age is ", self.person_age)
    print(' ')

#Use the Person class to create an object, and then execute the printname method:

# x = Person("John", 25)
# x.printname()