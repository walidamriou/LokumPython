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

"""
When an error occurs, or exception as we call it, Python will normally stop and generate
an error message. These exceptions can be handled using the try statement. so Python will
generate an error message but without stop the execution.
Without the try block, the program will crash and raise an error:
"""

# Exception Handling
# here we will use variable "a" without define it 
try:
    print(a)
except:
    print("An exception occurred")
print("Welcome") # python will print "welcome" so there is an error but the execution doesn't stop
print(' ')

# Multi Exceptions
try:
  print(a)
except NameError:
  print("Variable a isn't defined")
except:
  print("there is other problem in you code")
print(' ')

# Else (the logic of use: if there is error print it, else print there isn't error here)
a=5
try:
    print(a)
except NameError:
    print("Variable a isn't defined")
except:
    print("there is other problem in you code")
else:
    print("there is non error here")
print(' ')

# Finally (will be executed regardless if the try get an error or not)
try:
  print(b)
except NameError:
  print("Variable a isn't defined")
except:
  print("there is other problem in you code")
finally:
    print("The 'try except' is finished")
print(' ')

# List of exveptions in python here: 
# https://docs.python.org/3/library/exceptions.html