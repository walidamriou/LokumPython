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
a = {"name": "walid","age": 25,"github_username": "walidamriou"} # note: key:valure
a = dict(name="walid", age=25, github_username="walidamriou")

print(a)
print(' ')

# Dictionary Length
print(len(a))
print(' ')
# Check if Key Exists
print("facebook_username" in a ) # false, because there is non "facebook_username" in a 
print(' ')

# Accessing Items
print(a["name"]) # or: print(a.get("name"))
print(' ')

# Change Values
a["age"] = 23
print(a)
print(' ')

# Adding Items
a["twitter_username"] = "walidamriou" # Adding an item is done by using a new index key and assigning a value to it
print(a)
print(' ')

# Removing Items
a.pop("github_username") 
# del a["github_username"] # other method to remove a item
print(a)
print(' ')

# Copy a Dictionary
"""
Don't write b = a , because b will only be a reference to a, and changes made in b will automatically also be made in a
use copy() or dict()
"""
b = a.copy() 
b = dict(a) # other method
print(b)
print(' ')

# Empties the dictionary
b.clear()
print(b)
print(' ')

# Delete the dictionary
del b

# Loop Through a Dictionary
"""
you will get the keys only here
"""
for i in a :
   print(i)
print('')
"""
to loop and get the keys with the valures 
"""
for i in a :
    print(str(i)+":"+str(a[i]))
print(' ')
"""
Other method to get the keys with the valures
"""
for i, j in a.items():
  print(i, j)
print(' ')

"""
to loop and get the valures only
"""
for i in a.values():
  print(i)
print(' ')

# Nested Dictionaries or a dictionary can also contain many dictionaries
c = {
    "python1":{
        "name":"python pythono",
        "age":20
    },
    "python2":{
        "name":"python pythona",
        "age":36
    },
    "python3":{
        "name":"python pythony",
        "age":10
    },
    "python4":a
}

print(c)
print(' ')

"""
Note:
Other methods, we use:
      * fromkeys() to returns a dictionary with the specified keys and value
      * get() to returns the value of the specified key
      * items()	to returns a list containing a tuple for each key value pair
      * keys() to returns a list containing the dictionary's keys
      * popitem() to removes the last inserted key-value pair
      * setdefault() to returns the value of the specified key. If the key does not exist: insert the key, with the specified value
      * update() to updates the dictionary with the specified key-value pairs
"""