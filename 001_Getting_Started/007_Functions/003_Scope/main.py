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

# Local Scope
def print_age_1():
  age = 22
  print("My age is",age)
print_age_1()
print(' ')

# You can call the local scope from Function Inside other Function
def print_age_2(): # function 1
  age = 23 # local scope
  def body_print_age(): # function 2
      print("My age is",age) # you can use the local scope from function 1 because function 2 inside function 1
  body_print_age()
print_age_2()
print(' ')

# Global Scope
age = 24
def print_age_3():
  print("My age is",age)
print_age_3()
print(' ')

# Local and Global scopes in same time
age = 25 # Global scope
def print_age_4():
  age = 26 # Local scope  
  print("My age is",age) # this print will use Local scope

print_age_4()
print("My age is",age) # this print will use Global scope

# Using Global Keyword
def print_age_5():
  global age1 # How, age is Global scope 
  age1 = 28 
  print("(Local) My age is",age1) # this print will use Global scope
print_age_5()
print("(Global) My age is",age1) # this print will use Global scope

# global variable inside a function
age = 25 # Global scope
def print_age_6():
  global age # to use global scope    
  print("My age is",age) # this print will use Local scope
print_age_6()
