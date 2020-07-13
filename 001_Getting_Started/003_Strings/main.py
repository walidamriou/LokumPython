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

# place number in string by format
Year = 36
Month = 7
Day = 11
The_string_1 = "Today is {} from the month {} and the year {} "
print(The_string_1.format(Day,Month,Year))
The_string_2 = "Today is {2} from the month {0} and the year {1} "
print(The_string_2.format(Month,Year,Day))

"""
Notes: 
-- Escape characters used in Python: 
\n	New Line	
\"  Double Quote
\'	Single Quote	
\\	Backslash	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
\r	Carriage Return	
\t	Tab	
\b	Backspace	

-- all  string methodes:
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isidentifier()	Returns True if the string is an identifier
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rstrip()	Returns a right trim version of the string
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
"""