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
i = 1
while i < 10:
  print("step: "+str(i)) 
  i += 1
print(' ')

# The else Statement
while i < 10:
  print("step: "+str(i)) 
  i += 1
else:
  print("the loop end")
print(' ')

# The break Statement
"""
The break statement will terminate the innermost loop.
"""
i = 1
while i < 10:
  if i == 5 : 
      break
  print("step: "+str(i)) 
  i += 1
print(' ')

# The continue Statement
"""
The continue statement is used to skip the rest of the code 
inside a loop for the current iteration only. Loop does not 
terminate but continues on with the next iteration.
"""
i = 1
while i < 10:
  if i == 6 : 
      continue
  print("step: "+str(i)) 
  i += 1
print(' ')
