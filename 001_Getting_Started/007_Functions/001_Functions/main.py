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

# basics

# Creating & calling a Function
def First_function(): # create by def keyword
  print("First function :D")
First_function() # call the function
print(' ')

# The pass Statement
def empty_function():
  pass # pass statement to avoid getting an error

# Function with Arguments
def print_names(name): # name here is a parameter
    print("your name is:",name)
print_names("Walid") # "walid" here is argument
print(' ')

# Multi Arguments
"""
Note: If you function has two parameters so you should put two arguments
"""
def print_names(name,age): # name and age  is a parameters
    print("your name is:",name,"and you age is:",age)
print_names("Walid",25) # "walid" and 25  is arguments
print_names("python",22) # We send arguments with the key = value syntax

print(' ')

# Arbitrary Arguments (*args)
"""
When we don't know how many arguments that will be passed into a function.
"""
def print_my_names(*names):
  print("my names is:",names[0],"and",names[1],"and",names[2])

print_my_names("walid1", "walid2", "walid3","walid4")
print(' ')

# Arbitrary Keyword Arguments (**kwargs)
"""
When we don't know how many arguments that will be passed into a function,
and we send by a dictionary of arguments.
"""
def print_my_names(**names):
  print("my names is:",names["name1"],"and",names["name2"],"and",names["name3"]) 

print_my_names(name1="walid1", name2="walid2", name3="walid3",name4="walid4")
print(' ')


# Default Parameter 
"""
The function use the default valures when we call it without arguments
"""
def print_my_names(name1 = "python"): # the default valure of name1 is "python"
  print("My name is " + name1)

print_my_names("walid") # print My name is walid
print_my_names() # print My name is python
print(' ')

# Passing a List

def print_my_names(names):
  for i in names:
    print("My name is",i)
print(' ')

names_list = ["python1", "python2", "python3"]

print_my_names(names_list)

# Return Values
def addition_two(number):
  return number + 2

a = 3
b = addition_two(a) 
print("the addition of",a," with 2, is: ",b)
print(' ')

# Recursion Function
"""
 see: https://www.datacamp.com/community/tutorials/understanding-recursive-functions-python?utm_source=adwords_ppc&utm_campaignid=10267161064&utm_adgroupid=102842301792&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332602034358&utm_targetid=dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9069720&gclid=EAIaIQobChMI-PeAoYPL6gIVV4jVCh0L-QcgEAAYASAAEgJGO_D_BwE
 f(n) = f(n-1) if n>=1 
 and f(n)=1 if n < 1
"""

def recursion_funtion(n):
  if(n >= 1):
    f = n + recursion_funtion(n - 1)
    print("f(n)=",f)
  else:
    f = 1
    print("f(n)=",f)
  return f

recursion_funtion(6)
print(' ')