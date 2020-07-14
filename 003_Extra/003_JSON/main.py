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

import json

# from JSON to Python dictionary (Parse JSON)
# JSON structure example (JSON string)
data_json1 =  '{ "name":"walid", "age":25, "city":"berlin", "education":"Hardware & Software"}'
# parse json_example to dictionary
data1 = json.loads(data_json1)
print(data1["name"])
print(data1["education"])
print(' ')

# Convert from Python to JSON
# a Python object (dict):
data2 = {
  "name": "olaf",
  "age": 25,
  "city": "berlin",
  "education":"Mobile & Software"
}
# convert into JSON by dumps()
data_json2 = json.dumps(data2)
# the result is a JSON String
print(data_json2)
print(' ')

# Convert from dict, list, tuple, string, int, float, True, False and None to Json
data3 = {
  "name": "Walid",
  "age": 25,
  "married": False,
  "divorced": False,
  "Certificates": ("bachelor","Masters"),
  "car": None,
  "Graduation projects rates": [
    {"Graduate": "Bachelor", "rate": 18},
    {"Graduate": "Masters", "rate": 19}
  ]
}

data_json3=json.dumps(data3)
print(data_json3)
print(' ')
# Using the separators parameter to change the default separator
data_json4=json.dumps(data_json3, indent=4, separators=(". ", " = "))
print(data_json4)
print(' ')

"""
The Full documentation of the JSON library:
https://docs.python.org/3/library/json.html
"""
