import json



# Answer 1)
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89, 23]
unique_list = []
def unique_val(lst, u_lst):
    for i in lst:
        if i not in u_lst:
            u_lst.append(i)

unique_val(sample_list,unique_list)
print("Answer-1: ",unique_list)


#Answer 2)
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
unique_values = []
unique_val(sample_dict.values(),unique_values)
print("Answer-2: ", unique_values)

#Answer 3)
str1 = "ron03at038[2g577e29@#8496"
list_num = [int(i) for i in str1 if i.isdigit()]
sum = 0
for i in list_num:
    sum += i 

avg = sum/len(list_num)

print("Answer-3: Sum:",sum, " Average:", avg)

#Answer 4)
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

data = json.loads(sample_json1)
sal = data["company"]["employee"]["payble"]["salary"]
print("Answer-4: ",sal)

#Answer 5)
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price
    def to_Json(self):
        dict = {"Name":self.name, "Engine":self.engine, "Price":self.price}
        js = json.dumps(dict)
        return js

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
json_file = vehicle.to_Json()
print("Answer-5: ", json_file)


