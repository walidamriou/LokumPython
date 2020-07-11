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

b=len(a) #  we get the length of a string by len()
print(b)

print(a[0]) # print L
print(a[0]+a[1]+a[2]+a[3]+a[4]) # print Lokum
print(a[0:4]) # print Lokum by slice syntax
print(a[6:]) # print Python
print(a[-6:]) # print Python by negative Indexing
print(a[-12:-7]) # print Lokum by negative Indexing
print(a[-b:-7]) # print Lokum by negative Indexing and length of the string


# Remove whitespace from the begining or the end of strings
e = " Lokum Python "
print(e) 
f = e.strip()
print(f) # print "Lokum Python"

# Lower and Upper case

g = " Python is programming language "
g_lower = g.lower()
g_upper = g.upper()
g_lower_withot_whitespace = g.lower().strip()

print(g)
print(g_lower)
print(g_upper)
print(g_lower_withot_whitespace)

# replace
g_remplace_P = g.replace("P","G"); #remplace P by G so Python will be Gython hhhh :D 
print(g_remplace_P)

# splits the string into substrings
h = "Python, is, programming, language"
h_arr_substrings = h.split(",") # separator by ,
print(h_arr_substrings)
print(h_arr_substrings[0]) # print Python

# check if a certain phrase or character is present in or not in a string
i = "Python is programming language"
check_Python = "Python" in i
print(check_Python) # if "Python" in i, check_Python = true 
check_GoLang = "Golang" not in i
print(check_GoLang) #if "Golang not" in i check_Golang = true