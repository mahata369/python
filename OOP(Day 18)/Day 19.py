'''
Inheritance: mechanism where one class(child) acquire the properties and method of parent class
child class uses parent class's code
syntax:
class Parent:
    pass
class Child(Parent):
    pass
'''

# class Person:
#     def show(self):
#         print("This is a preson")
    

# class Student(Person):
#     def display(self):
#         print("This is student")

# s = Student()
# s.show()
# s.display()

# p = Person()
# p.display()

# Inheritance with constructor

# class Peson:
#     def __init__(self, name):
#         self.name = name

# class Student(Peson):
#     def display(self):
#         print(f"Name: {self.name}")

# s = Student("Ram")
# s.display()

# Super() keyword

class Person:
    def __init__(self, name):
        print("Parent constructor called")
        self.name = name

    def show():
        print("Student information:")

class Student(Person):

    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def display(self):
        super().show()
        print(f"Name {self.name}\nRoll {self.roll}")

s = Student("Ram", 101)
s.display()


