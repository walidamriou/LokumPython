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

# basics
for i in range(0, 3):
    print("step:",i)
print(' ')

for i in range(1, 5):
    print("step:",i)
print(' ')

"""
The range() function defaults to increment the sequence by 1, however it is possible
to specify the increment value by adding a third parameter
"""
for i in range(0, 10, 2) : #increment by 2
    print("step:",i)
print(' ')

# Else
for i in range(2):
  print(i)
else:
  print("The end of the loop!")
print(' ')

# Looping Through a String
txt = "Lokum"
for i in txt :
    print(i)
print(' ')

# The break Statement
names = ["walid1", "walid2", "walid3","walid4"]
for i in names :
  if i == "walid3":
    break
  print(i)
print(' ')

# The continue Statement
for i in names :
  if i == "walid3":
    continue
  print(i)
print(' ')

# Nested Loops ( loop inside a loop)
names1 = ["walid1", "walid2", "walid3"]
names2 = ["python1", "python2", "python3"]

for i in names1:
  for j in names2:
    print(i, j)
print(' ')

# The pass Statement (for For without content)
for i in [0, 1, 2]:
  pass