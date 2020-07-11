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

a = ["walid1","walid2","walid3","walid4","walid4"]
print(a)
print(' ')

a.append("walid5") #Adds an "walid5" at the end of the list
print(a)
print(' ')

a.remove("walid1") # Removes "walid1"from the list or you can use a.clear() to removes all elements
print(a)
print(' ')

b = a.copy() # Make a copy of a list
print(b)
print(' ')

b.append("walid3") # add other "walid3" to b list 
c = b.count("walid3") # to know how much "walid3" in b list, here there is 2 "walid3"
print(c)
print(' ')

e = ["python1","python2","python3"]
e.extend(a) # Add the elements of a list, to the end of the e list
print(e)
print(' ')

a.index("walid4")
print(a) # Returns the index of "walid2" in a list
print(' ')

a.insert(0, "walid1") # we use insert() to adds an element at the specified position
print(a)
print(' ')

a.pop(3) # wa use pop()	to remove an element at the specified position
print(a)
print(' ')

a.reverse() # Reverses the order of a list
print(a)
print(' ')

k = ["a","c","b","f","e","i","j"]
k.sort() # Sorts the list
print(k)
print(' ')

