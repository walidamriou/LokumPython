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

# The declaration of the variables in Python like that:  <variable name> = <value>

# Integer
a = 2 # or by specify a the type: x = int(2)	
print(a)

# Integer
b = 9223372036854775807
print(b)

# Floating point
pi = 3.14 # or or by specify a the type: Pi = float(3.14)	
print(pi)

# String (but like char)
c = 'A'
print(c)

# String
name = 'Lokum Python' # or by specify a the type: name = str("Lokum Python")	
print(name)

# 'Lokum Python' or "Lokum Python" is the same as
name = "Lokum Python"
print(name)

# Boolean
d = True # or by specify a the type: d = bool(True)
print(d)

# Empty value or null data type
e = None
print(e)

# complex
f1=1j + 12 # or by specify a the type: x = complex(1j + 12)	
f2=12j
print(f1)
print(f2)

# tuple
x = ("apple", "banana", "cherry") # or by specify a the type: x = tuple(("apple", "banana", "cherry"))	
print(x)	
print(x[0])

# range
x = range(6)	
print(x)	
# dict
x = {"name" : "walid", "age" : 25} # or by specify a the type: x = dict(name="walid", age=25)		
print(x)
print(x['name']) # or print(x["name"])

# set
x = {"apple", "banana", "cherry"} # or by specify a the type: x = set(("apple", "banana", "cherry"))	
print(x)

# frozenset
x = frozenset({"apple", "banana", "cherry"})		

# bytes
x = b"Hello" # or by specify a the type: x = bytes(b"Hello")	

# bytearray
x = bytearray(5) 	

# memoryview
x = memoryview(bytes(5))

# list
g = ["apple", "banana", "cherry"] # or by specify a the type: x = list(("apple", "banana", "cherry"))	

#Legal variable names:
projectname = "LokumPython"
project_name = "LokumPython"
_project_name = "LokumPython"
projectName = "LokumPython"
PROJECTNAME = "LokumPython"
projectname1 = "LokumPython"

print(projectname)
print(project_name)
print(_project_name)
print(projectName)
print(PROJECTNAME)
print(projectname1)

#Illegal variable names:
# 2projectname = "LokumPython"
# project-name = "LokumPython"
# project name = "LokumPython"
# $projectname = "LokumPython"

# Assign Value to Multiple Variables
x, y, z = "Oranga", "Banano", "binina" # names from my mind :D 
print(x)
print(y)
print(z)

# assign the same value to multiple variables
x = y = z = "Oranga"
print(x)
print(y)
print(z)

# Print with combine both text and a variable
print("So it is "+ x)

