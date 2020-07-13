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

# Import modules
import module1
import module2 as functions2
from module3 import print_age
from module4 import *         # this import method to remove module name when 
                              # call the functions
module1.print_name("walid1")
print(' ')
functions2.print_name("walid2") # modulename.functionname()
print(' ')
print_age(23) 
print(' ')
print_name_module4("walid4")
print_age_module4(25)