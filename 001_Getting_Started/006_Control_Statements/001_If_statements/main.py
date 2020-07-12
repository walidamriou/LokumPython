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
# IF 

a = 5 
b = 6

# Equals 
if a == 5 : 
    print("a equals b")
print(' ')

# Not Equals 
if b != 5 : 
    print("a not equals b")
print(' ')

# Less than 
if a < b : 
    print("a less than b")
print(' ')

# Less than or equal to
if a <= b :
    print("a less than or equal to b")
print(' ')

# Greater than 
if b > a :
    print("b greater than a")
print(' ')

# Greater than or equal to 
if b >= a :
    print("b greater than or equal to a")
print(' ')

# Short If, if you have only one statement
if a < b : print("a less than b")

# Elif (like else if in other languages)
if a > b : 
    print("a greater than b")
elif a < b :
    print("b greater than a")
print(' ')

# Else
if a > b :
    print("a greater than b")
else:
    print("b greater than a")
print(' ')

# Short If / Else
print("a greater than b") if a > b else print("b greater than a")
print(' ')
# or 
print(">") if a > b else print("<") if a < b else ("=")
print(' ')

# Logical operator, with conditional statements
# AND
c = 10
if a > b and a == b :
    print("a > b and a = c")
else:
    print(" other things -_-")
print(' ')

# OR
if a > b or c > a : 
    print("ok, a > b or c > a ")
print(' ')

# Nested if statements (if statements inside if statements)
if b > a :
    if c > b : 
        print(" c > a ")
print(' ')

# The pass Statement 
"""
if you for some reason have an if statement with no content, 
put in the pass statement to avoid getting an error.)
"""
if b > a : 
    pass
print(' ')