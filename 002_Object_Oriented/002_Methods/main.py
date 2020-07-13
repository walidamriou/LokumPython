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

# Create method
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def print_name(self): # Create method
      print("My name is ",self.name)

a = Person("python", 26)
print(a.name)
print(a.age)
a.print_name() #call method (function)
print(' ')


