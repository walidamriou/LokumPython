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

# Arithmetic Operators

# Addition
print(10+10) # 10 + 10 = 20
print(' ')

# Subtraction
print(20-10) # 20 - 10 = 10 
print(' ')

# Multiplication
print(10*5) # 10 * 5 = 50
print(' ')

# Division
print(50/5) # 50 / 5 = 10 but re
print(' ')

# Modulus
print(100%3) # 100 / 3 = 33 (+ 1) ; so 100 % 3 = 1 
print(' ')

# Exponentiation 
print(10**2) # 10^2=100
print(' ')

# Floor division
print(20//3) # 20 / 3 = 6 (+3) so 20 // 3 = 3   
print(' ')


# Assignment Operators
a = 5 
print (a)
print(' ')

a += 2 # a = a + 2 and here a = 5 + 3 = 8 
print(a)
print(' ')

a -= 3 # a = a - 3 and here a = 8 - 3 = 5
print(a)
print(' ')

a*= 2 # a = a * 2 and here a = 5 * 2 = 10 
print(a)
print(' ')

a/=5 # a = a / 5 and here a = 10 / 2 = 5
print(a)
print(' ')

a%=2 # a = a % 2 and here a = 5 % 2 = 1 
print(a)
print(' ')

b = 20 
b//=6  # b = b // 6 and here b = 20 // 6 = 3
print(b)
print(' ')

b **=2 # b = b ** 2 and here b = 3 ** 2 = 9
print(b)
print(' ')

b &= 10 # b = b & 10 and here 10 is 1010 in binary, 9 is 1001 in binary; so 1001 & 1010 = 1000 
        # so 1000 is 8 in dec so b = 8  
print(b)
print(' ')

b|=3 # like what we do with & operation (AND operation) and | operation is OR operation
print(b)
print(' ')

b^=3 
print(b)
print(' ')

b>>=2 
print(b)
print(' ')

b<<=5
print(b)
print(' ')

# Comparison Operators 

print(10==2) # false, because 10 not equal 2
print(10!=2) # true, because 10 not equal 2
print(10>2) # true
print(10<2) # false
print(10>=2) # true
print(10<=2) # false
print(' ')

# Logical Operators
e=12
print(e < 50 and  e > 2	) # Returns True if both statements are true, here return true
print(e < 12 or e <= 100) # Returns True if one of the statements is true	
print(not(e < 50 and  e > 2	)) # Reverse the result, returns False if the result is true, here return false
print(' ')

# Identity Operators
f=23
print(e is f) # Returns True if both variables are the same object, here return false
print(e is not f) # Returns True if both variables are not the same object	, here return true
print(' ')

# Membership Operators
list_names = ["walid1", "walid2","walid3"];

print("walid1" in list_names) # Returns True if a sequence with the specified value is present in the object	
print("walid5" not in list_names) #Returns True if a sequence with the specified value is not present in the object	
print(' ')

# Bitwise Operators

# I have used bin() to convert from decimal to binary
print(bin(1&1)) # AND Sets each bit to 1 if both bits are 1
print(bin(1|1)) # OR	Sets each bit to 1 if one of two bits is 1
print(bin(1 ^ 1)) # XOR	Sets each bit to 1 if only one of two bits is 1
print(bin(~1)) # NOT	Inverts all the bits
print(bin(1<<1)) # Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(bin(1>>1)) # Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
print(' ')

