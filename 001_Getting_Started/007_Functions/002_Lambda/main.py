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
A lambda function is a small anonymous function
lambda arguments : expression
"""

# Basics
# example 1 
f = lambda a : a * 2 + 20 # F(x) = x * 2 + 20
print("F(x)=",f(10)) # F(x)=10*2+20=20+20=40

# example 2
f = lambda a, b, c : a * 2 + b * 3 + c * 10 # F(x) = a*2+b*3+c*10
print("F(x1,x2,x3)=",f(3, 5, 20)) # F(3,5,20)=3*2+5*3+20*10=6+15+200=221

# example 3
def equation(x):
  return lambda a : a * x

body_function = equation(15) # F(x)=x*15

print("F(x)=",body_function(10)) # F(x)=10*15=150 