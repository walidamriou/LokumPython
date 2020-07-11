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

# basic
a = ("walid1", "walid2", "walid3") # create Tuple
# use tuple()
a = tuple(("walid1", "walid2", "walid3"))
print(a)
print(a[2]) # print "walid3"
print(a[-1]) # print "walid3" with Negative Indexing
print(a[0:2]) # print "walid1" and "walid2" , the element of position 2 is NOT included
              # you can Range of Negative Indexes
print(' ')

# Change Tuple Values
"""
 Tuples are unchangeable, that mean once a tuple is created, you cannot change its values. 
 to change tuple valures you need to convert the tuple into a list, change the list, and 
 convert the list back into a tuple.
"""

b = list (a) # b is the copy converted to list of a
b[0] = "walid0" # change the first element from "walid1" to "walid0"
a = tuple(b) # now, a is the copy converted to ruble of b 
print(a)
print(' ')

# Check if Item Exists
print("walid6" in a) # false, because there is not "walid6" in a Tuple
print(' ')

# Tuple Length
print(len(a))
print(' ')

# Add Items or Remove Items
"""
you cannot add or Removeitems or to/from Tuples, but use the methode of convert it to list to do that
"""


# Create Tuple With One Item
d = ("Python1",) # you need to put comma (,) or the type of the d change
print(d)
print(' ')

# Join Two Tuples
e = a + d 
print(e)
print(' ')

# get the number of times a specified value occurs in a tuple
print(a.count("walid1"))
print(a.count("walid2"))
print(' ')

# get the position of where a element in a Tuple
print(a.index("walid2"))
print(a.index("walid3"))
print(' ')

# Loop Through a Tuple
"""
we use this methode to print all of element of Tuple
"""
for i in a:
  print(i)
