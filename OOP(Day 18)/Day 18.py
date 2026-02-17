# Object oriented programming
'''
Class: Blueprint of an object
syntax to create class
class ClassName:
      satement
      variables

Syabtax to create object
obj = ClassName()
'''
#Simple class and object
# class Student:
#     pass

# student1 = Student()
# print(student1)


#Attributes
# class Student:
#     name="Ram"
#     age = 20

# student1 = Student()
# print(student1.name)
# print(student1.age)

# Method inside class

# class Student:

#     def greet(self,name):
#         print(f"Welcome {name}")

# name = input("Enter name: ")
# student1 = Student()
# student1.greet("Anuj")

# Constructor: runs automatically when object is created

# class Person:
    
#     def __init__(self):
#         print("Object created.Constructor invoked automatically")

# p1=Person()
# p2=Person()
# p3=Person()


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age = age

#     def display(self):
#         print(f"Name:{self.name}")
#         print(f"Age:{self.age}")


# p1 = Person("Ram", 20)
# p2 = Person("Hari", 21)
# p3 = Person("Sita", 22)

# p1.display()
# p2.display()
# p3.display()


# self:is a reference to the current object


# class Student:
#     def set_name(self,name):
#         self.Name=name

#     def show(self):
#         print(self.Name)

# s1= Student()
# s1.set_name("Ram")
# s1.show()

# # Student.set_name(s1,"Ram")

# class Counter:
#     def __init__(self):
#         self.count=0

#     def increment(self):
#         self.count += 1

# c1 = Counter()
# c2 = Counter()

# c1.increment()
# c1.increment()
# c2.increment()

# print(c1.count)
# print(c2.count)

'''
Acess control:
Deciding which data can be  accessed from  outside the class and which should be hidden

public: acessible everywhere(default)
protected: accessible in class and child class(_variable)
private: acessible only inside class(syntax: __variable)

'''
# Public Example

# class Student:
#     def __init__(self):
#         self.name = "Ram"  # Public varialble

#     def show(self):
#         print(self.name)

# s = Student()
# print(s.name)
# s.show()



# Protected Example

# class Person:
#     def __init__(self):
#         self._age = 20  # protected variable

# class Student(Person):
#     def show(self):
#         print(f"Age {self._age}")

# s = Student()
# s.show()



        

        
       