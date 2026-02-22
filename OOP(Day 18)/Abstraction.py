# Abstraction: hides implementation and show only functionality

from abc import ABC, abstractmethod

class Vechile(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vechile):
    def start(self):
        print("Car starts with key")

class Bike(Vechile):
    def start(self):
        print("Bike start with kick")

c =Car()
c.start()

b= Bike()
b.start()

