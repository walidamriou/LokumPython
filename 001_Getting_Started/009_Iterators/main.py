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
Lists, tuples, dictionaries, and sets are all iterable objects. 
They are iterable containers which you can get an iterator from.
"""

# Lists
names = ("walid1", "walid2", "walid3")
name = iter(names)

print(next(name))
print(next(name))
print(next(name))
print(' ')
# String 
txt = "Lokum"
character = iter(txt)
print(next(character))
print(next(character))
print(next(character))
print(next(character))
print(next(character))
print(' ')

# Using Loop 
for name in names:
  print(name)
print(' ')

# Create an Iterator with Oject Oriented method
"""
You need to going read part 002 Object Oriented and back here 
"""
# Create an iterator that returns numbers, starting with 0
# and each sequence (next) will increase by one 
class iterator_1:
  def __iter__(self):
    self.a = 0
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

a1 = iterator_1()
b1 = iter(a1)

print(next(b1))
print(next(b1))
print(next(b1))
print(next(b1))
print(' ')


# Create an Iterator with Oject Oriented method to stop the work of next() statements 

class iterator_2:
  def __iter__(self):
    self.a = 0
    return self

  def __next__(self):
    if self.a <= 20: # stop when 20
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

a2 = iterator_2()
b1 = iter(a2)

for x in a2:  # see here we don't have the number of the loop 
  print(x)