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
We will use open() function to open files, we use this modes to open the files:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"""
file = open("./info.txt", "r") # open info.txt with read mode
print(file.read())

"""
If you are using a VScode extension to developing with Python you may get an error: 
    FileNotFoundError: [Errno 2] No such file or directory: './info.txt'
Please use the terminal, not the extension to run this type of codes.

"""