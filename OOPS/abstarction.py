from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print('Car start with a key ')

class Bike(Vehicle):
    def start(self):
        print('Bike starts with a button ')


car = Car()
bike = Bike()

car.start()
bike.start()