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

# Create print_info as a Class
class print_info:
    name = "walid"
    age = 25

# Create a Object
a = print_info()
print("My name is ",a.name)
print("My age is ",a.age)
print(' ')

# The __init__() Function
"""
Use the __init__() function to assign values to object properties,
or other operations that are necessary to do when the object is being created
"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

b = Person("python", 26)
b.age = 30
print(b.name)
print(b.age)
del b.age # Delete Object Properties
del b # Delete object
# print(b.age) # don't use this because the object has deleted

print(' ')

# The pass Statement
class Algeria: # Algeria is empty class so we use pass statement  
  pass

"""
Notes:
- ython deletes unneeded objects (built-in types or class instances) automatically to free 
the memory space. The process by which Python periodically reclaims blocks of memory that no 
longer are in use is termed Garbage Collection.


"""