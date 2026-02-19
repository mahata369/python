# Types of inheritance
# Single inheritance: one parent -> one child: A->B

# class Animal:
#     def sound(self):
#         print("Animal makes sound")

# class Dog:
#     def bark(self):
#         print("Dog Barks")

# dog = Dog()
# dog.sound()
# dog.bark()

# Multilevel inheritance: Grandfather -> father -> child: A -> B ->c
# class GrandFather:
#     def land(self):
#         print("Grandfather's land")

# class Father(GrandFather):
#     def house(self):
#         print("Father's house")

# class Son:
#     def car(self):
#         print("Son's car")

# son =Son()
# print("Calling using son's object")
# son.land()
# son.house()
# son.car()
# print("Calling using father's object")
# father = Father()
# father.house()
# father.land()

# multiple inheritance: one child  -> multiple parents: (A,B) -> C here A and B are unrelated
# class Father:
#     def eyes(self):
#         print("Has brown eyes")

# class Mother:
#     def face(self):
#         print("Has round face")

# class Child(Father,Mother):
#     def skills(self):
#         print("Child's skills")

# child = Child()
# child.eyes()
# child.face()
# child.skills()

# Hierarchial inheritance: one parent -> multiple child: A->(B<C)

# class Vechile:
#     def engine(self):
#         print("Has engine")

#     def horn(self):
#         print("has horn")

# class Bike(Vechile):
#     def tyre(self):
#         print("Has 2 tyres")

# class Car(Vechile):
#     def tyre(self):
#         print("Has 4 tyres")

# bike = Bike()
# print("Bike......")
# bike.engine()
# bike.horn()
# bike.tyre()

# car = Car()
# print("Car....")
# car.engine()
# car.horn()
# car.tyre()

# Hybrid inheritance: combination of all inheriance(it has not fix structure)

# class A:
#     def showA(self):
#         print("class A")

# class B(A):
#     def showB(self):
#         print("class B")

# class C(A):
#     def showC(self):
#         print("class C")

# class D(B, C):
#     def showD(self):
#         print("class D")
# d = D()
# d.showA()
# d.showB()
# d.showC()
# d.showD()






