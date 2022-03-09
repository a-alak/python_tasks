# Python tasks - SPEDA interview

# 1)
# Write a function, that counts the number of times a unique value is represented in the list
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89, 23]

# 2)
# Find all unique values of this dictionary
sample_dict = {
    "jan": 47,
    "feb": 52,
    "march": 47,
    "April": 44,
    "May": 52,
    "June": 53,
    "july": 54,
    "Aug": 44,
    "Sept": 54,
}

# 3)
# Find sum and average of all digits (0-9) in this string
str1 = "ron03at038[2g577e29@#8496"

# 4)
# Find the value of "salary" in the following JSON 
sample_json1 = """{
   "company":{
      "employee":{
         "name":"emma",
         "payble":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# 5)
# Expand the class with a method that returns a JSON representation of an instance of the class
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price
vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)  # example instance