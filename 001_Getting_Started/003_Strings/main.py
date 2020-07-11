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

# one strings
a = "LokumPython"
print(a)
b='LokumPython'
print(b)

# Multiline Strings

c = """
       Lokum methode to learn programming languages
       will help you to learn in a practical way, 
       through the comments in the program lines.
    """
print(c)

d = '''
       Lokum methode to learn programming languages
       will help you to learn in a practical way, 
       through the comments in the program lines.
    '''
print(d)

# Working with Strings as Arrays

a = "Lokum Python"
print(a[0]) # print L
print(a[0]+a[1]+a[2]+a[3]+a[4]) # print Lokum
print(a[0:4]) # print Lokum by slice syntax
print(a[6:]) # print Python