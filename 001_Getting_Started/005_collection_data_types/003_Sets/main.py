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
a = {"walid1", "walid2", "walid3","walid4"}
a = set({"walid1", "walid2", "walid3","walid4"})
print(a) # Sets are unordered, see the print result 
print(' ')

# Get the Length of a Set
print(len(a))
# Check if Item Exists
print("walid6" in a) # false, because there is not "walid6" in a Set
print(' ')

# Change Set Values
"""
Once a set is created, you cannot change its items, but you can add new items.

"""

# add item to Set
a.add("walid5")
print(a)
print(' ')

# add multi items to Set

a.update(["walid6","walid7","walid8","walid9"])
print(a)
print(' ')

# Remove Item
a.remove("walid9") # If the item to remove does not exist, remove() will raise an error
a.discard("walid20") # If the item to remove does not exist, discard() will NOT raise an error
"""
There is other method by using pop() but because Sets are unordered, so when using the pop() 
method, you will not know which item that gets removed. because this method will remove the 
last item.
"""

# Add Items
a.add("walid12") # To add one item to a set use the add() method
print(a)
a.update({"walid11","walid13"}) # To add more than one item to a set use the update() method.
print(a)
print(' ')

# copy, Join Two Sets and delete a Set
b = a.copy()
print(b)
e = {"Python1","Python2"} # create e Set
c=a.union(e) # Join Two Sets a and e
print(c)
del b 
# print(b) # if you remove # from this line, you will get error tell you the name 'b' is not defined
print(' ')

# Loop Through a Set
for i in a:
  print(i)
print(' ')

"""
Note: 
 We use: * clear()	to removes all the elements from the set 
         * remove()	to removes the specified element
         * difference()	to returns a set containing the difference between two or more sets
         * difference_update()	to removes the items in this set that are also included in another, specified set
         * discard()	to remove the specified item
         * intersection()	to returns a set, that is the intersection of two other sets
         * intersection_update()	to removes the items in this set that are not present in other, specified set(s)
         * isdisjoint()	to returns whether two sets have a intersection or not
         * issubset()	to returns whether another set contains this set or not
         * issuperset()	to returns whether this set contains another set or not
         * symmetric_difference()	to returns a set with the symmetric differences of two sets
         * symmetric_difference_update()	to inserts the symmetric differences from this set and another
"""

