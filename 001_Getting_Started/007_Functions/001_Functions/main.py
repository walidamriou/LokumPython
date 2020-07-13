"""
 ******************************************************************** 

  LokumPython
  To Learn Go Programming Language with small programs examples
  Project Website: LokumPython.walidamriou.com
  Github: https://github.com/walidamriou/LokumPython

  Copyright CC 2020 Walid Amriou
  This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License
   
  Last update: July 2020

 ******************************************************************** 
"""

# basics

# Creating & calling a Function
def First_function(): # create by def keyword
  print("First function :D")
First_function() # call the function
print(' ')

# Function with Arguments
def print_names(name): # name here is a parameter
    print("your name is:",name)
print_names("Walid") # "walid" here is argument
print(' ')

# Multi Arguments
def print_names(name,age): # name and age  is a parameters
    print("your name is:",name,"and you age is:",age)
print_names("Walid",25) # "walid" and 25  is arguments
print(' ')

# Arbitrary Arguments
"""
When we don't know how many arguments that will be passed into a function
"""
def print_my_names(*names):
  print("my names is:",names[0],"and",names[1],"and",names[2])

print_my_names("walid2", "walid2", "walid3","walid4")
print(' ')
