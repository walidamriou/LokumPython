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
To write to an existing file, we use this parameters with the open() function
"a" - Append ( will append to the end of the file )
"w" - Write ( will overwrite any existing content )
"""

# add a text to the info.txt file (Write to an Existing File)
file1= open("info.txt", "a")
file1.write("\n Text2: Python  is a high-level programming language for general-purpose programming.") # We use \n in the beginning of the text to write it in new line
file1.close()

# open and read the file 
file1 = open("info.txt", "r")
print(file1.read())

# Create a New File
file2 = open("info2.txt", "x") # we use parameter "w" to create file if does not exist
# Write text to the new file
file2= open("info2.txt", "a")
file2.write("\n Text1: first text in the file 2.") 
file2.close()
file2 = open("info2.txt", "r")
print(file2.read())