# Day 9
# Dictionary: collection of data stored in key:value pair
"""
 syntax:
# dict_name={
#         key1:valuse1,
#         key2:value2,
#         .
#         .
#         .
#         key-n:value-n
# }
# """
#Example
# student={"name":"Ram","age":20, "city":"kathmandu"}
# print(student)

# properties:
# mutable
# key-value Pair 
# keys are unique
# allows duplicate
# unordered

# Acessing values using key
# student ={"name":"Ram","age":20, "city":"kathmandu"}
# # print(student["name"])
# # print(student["age"])
# # print(student["city"])

# #Accessing values using get() method
# print(student.get("name"))

#looping through dictionary
#student ={"name":"anuj", "age":20, "city":"kathmandu"}
#looping through key
# for k in student:
#     print(k)
#looping through value
# for v in student.values():
#print(v)

#using both
# for k,v in student.items():
#     print(k,v)


#Methods in dictionary
"""
get():acessing value using key
key():return all the keys in dict
values():return all th values in dict
items():return key-value pair
update():add new data or  update existing data
pop():removes data using key
popitem():removes last item
clear():removes all data
copy():copies dictionary and stores in new variable
fromkey():create dictionary with keys
"""
# student = {"name":"Ram", "age":20, "city":"kathmandu"}
# print(student.get("name"))
# print(student.keys())
# print(student.values())

# for k,v in student.items():
#     print(k,v)

# #update existing data
# student.update({"age":21})
# print(student)

# #insert/add  new data
# student.update({"roll": 1})
# print(student)

# #pop()
# student.pop("age")
# print(student)

# #popitem()
# student.popitem()
# print(student)

# #clear()
# student.clear()
# print(student)

# #copy()
# student1=student.copy()
# print(student1)

# #fromkey()
# keys=["a", "b", "c"]
# d =dict.fromkeys(keys,0)
# print(d)

# Another method of creating dictionary from user input

# d={}

# n=int(input("how many data? "))
# for i in range(1,n+1):
#     name=input("Enter name")
#     age=int(input("Enter age "))
#     d[name]= age #it makes key-value pair

# print(d)

#converting list to dictionary
# ls =[["Ram",21],["shyam",20]]
# print(dict(ls))

#searching in dictionary

d={
    "name":["Ram","Shyam","Hari"],
    "age":[22,22,20],
    "address":["kathmandu","lalitpur","bhaktpur"]
}

found=False
for i in d["name"]:
    if i.lower() == "shyam":
        print("Found")
        found=True
if not found:
    print("Not found")
    