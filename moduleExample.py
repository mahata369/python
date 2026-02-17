# def add(a,b):
#     return a+b

# def subtraction(a,b):
#     return a-b

# def multiplication(a,b):
#     return a*b

# def division(a,b):
#     return a/b


# def add_student():
#    try:
#         name = input("Enter name: ")
#         age = int(input("Enter age: "))
#         marks = int(input("Enter marks: "))
#          # Creating new unique id
#         try:
#            with open("student.txt", "r") as f:
#             lines = f.readline()
#             if lines:
#                last_list = lines[-1]
#                last_id = int(last_list.split(",")[0])
#                new_id = last_id + 1
#             else:
#                new_id=1
#             f.write(f"{name},{age},{marks}\n")


#         except FileNotFoundError:
#          print("File not found")
#      # Adding data in the file
#    with open("student.txt","a") as f:
#      f.write(f"{new_id},{name},{age},{marks}\n")
#    print("Added sucessfully")

#     except FileNotFoundError:
#    print("File not found")


# area.py
import math

def circle_area(r):
    if r < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi *r*r

def rectangle_area(l,b):
    if l < 0 or b< 0:
        raise ValueError("Length and breadth cannot be negative")
    return l*b

# convert.py
def km_to_miles(km):
    if km < 0:
        raise ValueError("Distance cannot be negative")
    return km*0.621371

def celsius_to_fahrenheit(c):
    return (c*9/5) + 32


# number_utils.py

def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def prime_check(n):
    if n <=1:
        return False
    
    for i in range(2,int(n**0.5) +1 ):
        if n % i ==0:
            return False
        
    return True