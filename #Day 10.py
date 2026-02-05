# Function:block of code that perform specific task and run only when it is called
"""
Syntax:
  def function_name():
  statement
  code
  logic

fnction_name()

uses:
Reduces repetition
Modular program
code reusability
"""

#Types of functions in python:

#Function with no parameter and no return value

# def greet():
#     print("Hello world")
# greet()

#Function with parameter and no return value
# def greet(name): # name is parameter and it is variable
#     print(f"Hi {name}")

# greet("Nimisha")#nimisha is argument

#Function with no parameter but return value
# def greet():
#     return "Hello world"

# x=greet()
# print(x)
# print(greet())

#function with parameter and return value
# def add(a,b):
#     return a+b

# result = add(5,4)
# print(result)

#for string
# def greeting(name):
#     str = f"Hello {name}"
#     return str
# print(greeting("Nimisha"))

#Default argument function
# def greet(name="cma"):
#     print(f"Hello {name}")

# greet()
# greet("anuj")

#keyword argument function
# def student(name,age):
#     print(name,age)
# student(age=20, name="anuj")#order of argument and parameter doesnot matter here

# Variable length argument function

# def add(*num):#num is stored as tuple here
#     total = 0
#     for i in num:
#         total +=i 
#     return total

# print(add(1,2,4))
# print(add(10,20,40,50,2,6))#we can pass many arguments in this functon

#for string
# def greet(*args):
#     for i in args:
#         print(f"Hello {i}")

# greet("Anuj","Nimisha")
# greet("Cma")

#Keyword variable length arguments

# def student(**data):#data is stored as dictionary here
#     print(data)
#     print(type(data))
#     for k,v in data.items():
#         print(k,":", v)

# student(name="Ram",age=20)
# student(name="Ram",age=20,city="Dhangadhi")

# Nested dictioonary using keyword 


#string methods

# text="Hello world"
# ''''''
# ''''''



# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.strip())

# str="Hello java"
# print(str.replace("Java","Python"))

# str1="Apple,Orange,Kiwi"
# print(str1.split(","))

# lst = ["Apple","Mango","Kiwi"]
# print(" ".join(lst))

# print(str1.find("Apple"))#it gives the index of list

# print(str1.count(","))

# print(str.startswith("Hello"))
# print(str.endswith("java"))
